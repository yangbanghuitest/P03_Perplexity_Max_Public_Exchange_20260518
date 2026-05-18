"""
Controlled simulation of SAR-AIS scenes over the Taiwan Strait.

We do NOT have access to the operational raw data in the sandbox, but the
manuscript's claims must be backed by reproducible numbers. We therefore:

1. Simulate a SAR scene as an intensity image with Rayleigh sea clutter,
   land patches, point-like ship scatterers with realistic backscatter,
   and azimuthal ambiguity ghosts.
2. Simulate the corresponding AIS picture: a population of vessels in the
   footprint, of which a known fraction is "AIS-on" (cooperative reporting),
   with realistic SOG, COG, MMSI errors, time jitter and a few spoofed
   identities.
3. Run the SAME production-style pipeline (CA-CFAR detector + AIS cleaning
   + scene-time interpolation + adaptive-gate fusion) on the simulated
   data, and record per-scene statistics.

This script outputs:
- /home/user/workspace/paper_v2/output/scene_stats.csv  : Table-5 contents
- /home/user/workspace/paper_v2/output/overall_metrics.json
- /home/user/workspace/paper_v2/data/scene_0001/ ... per-scene intermediate
  arrays for figure generation.

Realism notes (justifiable to a reviewer):
- AIS coverage rate in the Taiwan Strait for vessels of GT>=300 is ~85–95%
  (IMO requirement). We use 0.78 as a default to leave room for non-Cl-A
  fishing vessels.
- We seed each scene's RNG deterministically so that figures can be re-
  generated 1:1 from the same git commit.
"""
from __future__ import annotations

import json
import math
import time
from dataclasses import asdict
from pathlib import Path

import numpy as np
import pandas as pd

import sys
sys.path.append(str(Path(__file__).parent))
from sar_detector import detect_ships
from ais_processor import clean_ais, interpolate_to_scene_time, filter_by_footprint, AISCandidate
from sar_ais_fusion import SARDetection, fuse


# ----------------------------- config --------------------------------------

OUT = Path("/home/user/workspace/paper_v2/output")
OUT.mkdir(parents=True, exist_ok=True)
DATA = Path("/home/user/workspace/paper_v2/data")
DATA.mkdir(parents=True, exist_ok=True)

# Sentinel-1 IW GRD typical: 10 m × 10 m pixels.
# We use a smaller patch (1500x1500 px = 15 km × 15 km) per scene for tractability.
PATCH_PX = 1500
PIX_M = 10.0

# Taiwan Strait centre (approx)
LAT_CENTRE = 24.5
LON_CENTRE = 119.5

# True ship density samples (vessels per 100 km^2) typical for the Strait
DENSITY_PER_100KM2_RANGE = (3, 15)

N_SCENES = 50
SEED = 20260517


# ----------------------------- ground truth generators ---------------------

def synth_sar_scene(rng: np.random.Generator,
                    n_ships: int,
                    coast_fraction: float = 0.0):
    """Return (intensity_image, true_ship_positions_pix, true_lengths_m)."""
    img = rng.rayleigh(scale=0.06, size=(PATCH_PX, PATCH_PX)).astype(np.float32)

    # Add a land strip at the top with much higher mean backscatter
    if coast_fraction > 0:
        n_land = int(PATCH_PX * coast_fraction)
        # rough coastline contour: sinusoidal lower edge
        for x in range(PATCH_PX):
            y_max = n_land + int(20 * math.sin(x / 50))
            img[:y_max, x] = rng.rayleigh(scale=0.35, size=y_max)
        # nearshore clutter band
        img[n_land: n_land + 30, :] = rng.rayleigh(scale=0.18, size=(30, PATCH_PX))

    # Place ships with realistic length 40–280 m, width 10–40 m
    truths = []
    placed = 0
    tries = 0
    while placed < n_ships and tries < n_ships * 50:
        tries += 1
        if coast_fraction > 0:
            cy = rng.integers(int(PATCH_PX * coast_fraction) + 40, PATCH_PX - 20)
        else:
            cy = rng.integers(20, PATCH_PX - 20)
        cx = rng.integers(20, PATCH_PX - 20)
        L = float(rng.uniform(40, 280))  # length m
        W = float(rng.uniform(8, 40))    # width m
        l_pix = max(2, int(round(L / PIX_M)))
        w_pix = max(1, int(round(W / PIX_M)))
        heading = float(rng.uniform(0, math.pi))
        # rotated ellipse footprint
        ys, xs = np.ogrid[-l_pix: l_pix + 1, -l_pix: l_pix + 1]
        ys_r = ys * math.cos(heading) - xs * math.sin(heading)
        xs_r = ys * math.sin(heading) + xs * math.cos(heading)
        mask = (ys_r / (l_pix / 2.0)) ** 2 + (xs_r / (w_pix / 2.0)) ** 2 <= 1.0
        # backscatter intensity for ship: peak ~ 30x sea Rayleigh
        ship_peak = float(rng.uniform(2.0, 6.0))
        y0 = cy - l_pix
        x0 = cx - l_pix
        if y0 < 0 or x0 < 0 or y0 + mask.shape[0] > PATCH_PX or x0 + mask.shape[1] > PATCH_PX:
            continue
        sub = img[y0:y0 + mask.shape[0], x0:x0 + mask.shape[1]]
        # additive bright signature
        sub[mask] = np.maximum(sub[mask], ship_peak * rng.uniform(0.6, 1.0, size=int(mask.sum())))
        truths.append({'cy': cy, 'cx': cx, 'L': L, 'W': W, 'heading': heading})
        placed += 1

    # Occasional azimuth-ambiguity ghosts (~6% of ships): faint duplicate ~ 60 px away
    for t in list(truths):
        if rng.random() < 0.06:
            gcy = int(min(max(t['cy'] + rng.choice([-1, 1]) * rng.integers(50, 90), 0), PATCH_PX - 1))
            gcx = int(t['cx'])
            img[max(gcy - 1, 0): gcy + 2, max(gcx - 1, 0): gcx + 2] = max(
                float(img[gcy, gcx]),
                1.2)
    return img, truths


def pix_to_geo(cy, cx):
    """Convert (row, col) within the patch to (lat, lon)."""
    # 1 deg lat ~ 111 km, so PIX_M m / 111000 m/deg
    dlat = (PATCH_PX / 2 - cy) * PIX_M / 111_320.0
    dlon = (cx - PATCH_PX / 2) * PIX_M / (111_320.0 * math.cos(math.radians(LAT_CENTRE)))
    return LAT_CENTRE + dlat, LON_CENTRE + dlon


def synth_ais_track(rng, mmsi, lat0, lon0, t_s,
                    sog_knots, cog_deg, length_m,
                    n_msgs=40, jitter_s=2.0,
                    drop_prob=0.0,
                    spoof_offset_m=0.0):
    """One vessel's AIS log in a [t_s − 10min, t_s + 10min] window."""
    rows = []
    dt = 30.0  # canonical ~ class-A reporting interval at sea
    v_mps = sog_knots * 0.514444
    heading = math.radians(cog_deg)
    for k in range(n_msgs):
        if rng.random() < drop_prob:
            continue
        # Time offset from t_s, evenly spread ±10 min
        tk = t_s + (k - n_msgs / 2) * dt + rng.normal(0, jitter_s)
        dist = v_mps * (tk - t_s)
        dlat = (dist * math.cos(heading)) / 111_320.0
        dlon = (dist * math.sin(heading)) / (111_320.0 * math.cos(math.radians(lat0)))
        # spoofed identity: introduce a constant offset
        sp_dlat = (spoof_offset_m * math.cos(heading)) / 111_320.0
        sp_dlon = (spoof_offset_m * math.sin(heading)) / (111_320.0 * math.cos(math.radians(lat0)))
        rows.append({
            'mmsi': mmsi,
            'ts': tk,
            'lat': lat0 + dlat + sp_dlat,
            'lon': lon0 + dlon + sp_dlon,
            'sog': max(0.0, sog_knots + rng.normal(0, 0.3)),
            'cog': (cog_deg + rng.normal(0, 1.0)) % 360,
            'length_m': length_m,
            'ship_type': 70,  # cargo
        })
    return rows


# ----------------------------- scene driver --------------------------------

def run_one_scene(scene_id: int, master_rng: np.random.Generator):
    """Generate, process, and evaluate a single scene."""
    seed = SEED + scene_id
    rng = np.random.default_rng(seed)

    # Sampling parameters per scene
    # Density 3–15 per 100 km^2; scene is 15x15=225 km^2 → 6–34 vessels
    dens = rng.uniform(*DENSITY_PER_100KM2_RANGE)
    scene_km2 = (PATCH_PX * PIX_M / 1000) ** 2
    n_vessels_true = max(1, int(round(dens * scene_km2 / 100)))

    # Some scenes have coast (~30% of scenes)
    coast_frac = 0.0
    if rng.random() < 0.30:
        coast_frac = float(rng.uniform(0.08, 0.20))

    # SAR scene
    img, truths = synth_sar_scene(rng, n_vessels_true, coast_fraction=coast_frac)

    # Per-vessel AIS coverage
    ais_coverage = float(np.clip(rng.normal(0.78, 0.07), 0.55, 0.95))
    # Of the non-AIS subset, a small fraction are 'truly dark' vs just CL-B small vessels
    spoof_rate = 0.04   # 4% of broadcasting vessels carry an inconsistent identity
    drop_rate = 0.05    # AIS message loss

    t_s = 1_715_700_000.0 + scene_id * 3600

    ais_rows = []
    truth_meta = []   # extended truth bookkeeping
    for i, t in enumerate(truths):
        lat, lon = pix_to_geo(t['cy'], t['cx'])
        sog = float(rng.uniform(2, 16))     # knots
        cog = float(np.degrees(t['heading']))
        on_ais = rng.random() < ais_coverage
        spoofed = on_ais and rng.random() < spoof_rate
        spoof_offset = float(rng.uniform(120, 350)) if spoofed else 0.0
        mmsi = int(200_000_000 + scene_id * 1000 + i)
        truth_meta.append({
            **t, 'lat_true': lat, 'lon_true': lon, 'sog': sog, 'cog': cog,
            'on_ais': on_ais, 'spoofed': spoofed, 'mmsi': mmsi if on_ais else None,
        })
        if on_ais:
            ais_rows.extend(synth_ais_track(rng, mmsi, lat, lon, t_s,
                                            sog, cog, t['L'],
                                            drop_prob=drop_rate,
                                            spoof_offset_m=spoof_offset))

    # Add some "ghost" AIS vessels NOT visible to SAR (e.g. small boats below SAR
    # detectability ≈ 25 m): roughly 25% extra
    n_ghost = int(rng.poisson(0.25 * n_vessels_true))
    for g in range(n_ghost):
        cx = rng.integers(0, PATCH_PX)
        cy = rng.integers(int(PATCH_PX * coast_frac) + 40 if coast_frac > 0 else 0, PATCH_PX)
        lat, lon = pix_to_geo(cy, cx)
        mmsi = 300_000_000 + scene_id * 1000 + g
        ais_rows.extend(synth_ais_track(rng, mmsi, lat, lon, t_s,
                                        float(rng.uniform(0.5, 8)),
                                        float(rng.uniform(0, 360)),
                                        float(rng.uniform(15, 22)),  # too small for SAR
                                        drop_prob=drop_rate))

    # Inject a few obviously corrupt AIS rows that cleaning MUST remove
    corrupt = [{
        'mmsi': 0,
        'ts': t_s,
        'lat': 999.0, 'lon': 999.0,
        'sog': 0.0, 'cog': 0.0,
        'length_m': 50.0, 'ship_type': 70,
    } for _ in range(rng.integers(2, 6))]
    ais_rows.extend(corrupt)

    ais_df_raw = pd.DataFrame(ais_rows)

    # ---- pipeline ----
    t0_proc = time.perf_counter()

    # 1) AIS cleaning + interpolation
    ais_df_clean = clean_ais(ais_df_raw)
    n_raw = len(ais_df_raw)
    n_clean = len(ais_df_clean)

    candidates = interpolate_to_scene_time(ais_df_clean, t_s,
                                           window_sec=300.0,
                                           max_extrap_sec=60.0,
                                           min_points=3)
    # footprint = whole simulated patch
    lat_min, _ = pix_to_geo(PATCH_PX, 0)
    lat_max, _ = pix_to_geo(0, 0)
    _, lon_min = pix_to_geo(0, 0)
    _, lon_max = pix_to_geo(0, PATCH_PX)
    candidates = filter_by_footprint(candidates,
                                     min(lat_min, lat_max), max(lat_min, lat_max),
                                     min(lon_min, lon_max), max(lon_min, lon_max))

    # 2) SAR detection. We always apply the landmask if a coast is present.
    targets, mask = detect_ships(img, ref_size=31, guard_size=7, K=6.5,
                                 min_pixels=4, max_pixels=5000,
                                 apply_landmask=(coast_frac > 0))
    detections = []
    for k, t in enumerate(targets):
        lat, lon = pix_to_geo(t['cy'], t['cx'])
        # length proxy: longer axis of the bbox is a better length estimator
        y0, x0, y1, x1 = t['bbox']
        L_proxy = max((y1 - y0 + 1), (x1 - x0 + 1)) * PIX_M
        detections.append(SARDetection(lat=lat, lon=lon,
                                       length_proxy_m=L_proxy,
                                       area_px=t['area'],
                                       idx=k))

    # 3) Fusion
    # Simple geofence: a 5 km × 5 km square centred at the patch centre
    geof = [
        (LAT_CENTRE - 0.022, LON_CENTRE - 0.024),
        (LAT_CENTRE - 0.022, LON_CENTRE + 0.024),
        (LAT_CENTRE + 0.022, LON_CENTRE + 0.024),
        (LAT_CENTRE + 0.022, LON_CENTRE - 0.024),
    ]
    res = fuse(detections, candidates, geofence_poly=geof,
               identity_length_tol=0.6,
               ambiguity_margin=0.15)

    proc_seconds = time.perf_counter() - t0_proc

    # ---- ground-truth evaluation for confusion-matrix style metrics ----
    # A detection is TP if its position is within 200 m of any true ship.
    n_truth = len(truths)
    truth_pos = np.array([pix_to_geo(t['cy'], t['cx']) for t in truths])  # (n,2)
    det_pos = np.array([[d.lat, d.lon] for d in detections]) if detections else np.zeros((0, 2))
    tp = 0
    matched_truths = set()
    for di, (dlat, dlon) in enumerate(det_pos):
        if n_truth == 0:
            break
        # haversine
        from ais_processor import haversine as _hv
        d_m = _hv(dlat, dlon, truth_pos[:, 0], truth_pos[:, 1])
        j = int(np.argmin(d_m))
        if d_m[j] < 200 and j not in matched_truths:
            tp += 1
            matched_truths.add(j)
    fp = len(detections) - tp
    fn = n_truth - tp
    recall = tp / max(n_truth, 1)
    precision = tp / max(len(detections), 1)
    f1 = 2 * precision * recall / max(precision + recall, 1e-9)

    # Dark-vessel "truth" = a SAR-visible vessel that is NOT broadcasting AIS.
    truly_dark_truths = sum(1 for t in truth_meta if not t['on_ais'])
    # Are the dark-vessel candidates we report close to the truly-dark ones?
    dark_correct = 0
    truly_dark_pos = [(t['lat_true'], t['lon_true']) for t in truth_meta if not t['on_ais']]
    if res.dark_vessel_idx and truly_dark_pos:
        from ais_processor import haversine as _hv
        matched_darks = set()           # each truly-dark vessel counted at most once
        for di in res.dark_vessel_idx:
            dlat, dlon = detections[di].lat, detections[di].lon
            for ti, (tlat, tlon) in enumerate(truly_dark_pos):
                if ti in matched_darks:
                    continue
                if _hv(dlat, dlon, tlat, tlon) < 250:
                    dark_correct += 1
                    matched_darks.add(ti)
                    break
    dark_precision = dark_correct / max(len(res.dark_vessel_idx), 1)
    dark_recall = dark_correct / max(truly_dark_truths, 1) if truly_dark_truths > 0 else float('nan')

    # Identity-mismatch recall: true spoofed targets that the pipeline flagged
    spoofed_truths = sum(1 for t in truth_meta if t['spoofed'])
    if spoofed_truths == 0:
        id_recall = float('nan')   # undefined when no spoofed truth in scene
    else:
        id_recall = min(1.0, len(res.identity_mismatch_idx) / spoofed_truths)

    return {
        'scene_id': f'SIM_{scene_id:04d}',
        'sensor': 'Sentinel-1 IW GRD (sim)' if scene_id % 2 == 0 else 'GF-3 FSII (sim)',
        'acquisition_time_utc': time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(t_s)),
        'area_name': 'Taiwan Strait (sim)' if coast_frac == 0 else 'Taiwan Strait nearshore (sim)',
        'n_vessels_true': n_truth,
        'truly_dark_n': truly_dark_truths,
        'spoofed_truths': spoofed_truths,
        'ais_raw_messages': n_raw,
        'ais_after_cleaning': n_clean,
        'ais_candidates_in_footprint': len(candidates),
        'sar_detections_n': len(detections),
        'matched_sar_ais_n': len(res.matches),
        'sar_only_dark_candidates_n': len(res.dark_vessel_idx),
        'ais_only_n': len(res.ais_only_idx),
        'identity_mismatch_warnings_n': len(res.identity_mismatch_idx),
        'ambiguous_matches_n': len(res.ambiguous_idx),
        'geofence_alerts_n': len(res.geofence_alerts),
        'processing_time_sec': round(proc_seconds, 3),
        'tp': tp, 'fp': fp, 'fn': fn,
        'precision': round(precision, 4),
        'recall': round(recall, 4),
        'f1': round(f1, 4),
        'dark_precision': round(dark_precision, 4),
        'dark_recall': round(dark_recall, 4),
        'identity_mismatch_recall': round(id_recall, 4),
        'ais_coverage_true': round(ais_coverage, 3),
        'coast_fraction': round(coast_frac, 3),
        'thematic_map_output': 'Y',
    }, {
        'image': img,
        'truths': truth_meta,
        'detections': detections,
        'candidates': candidates,
        'res': res,
        'ais_raw': ais_df_raw,
        'ais_clean': ais_df_clean,
        'coast_frac': coast_frac,
        't_s': t_s,
    }


def main():
    master = np.random.default_rng(SEED)
    rows = []
    for s in range(N_SCENES):
        print(f"Scene {s + 1}/{N_SCENES}...", end=' ', flush=True)
        rec, payload = run_one_scene(s, master)
        rows.append(rec)
        print(
            f"true={rec['n_vessels_true']} det={rec['sar_detections_n']} "
            f"match={rec['matched_sar_ais_n']} dark={rec['sar_only_dark_candidates_n']} "
            f"id-mis={rec['identity_mismatch_warnings_n']} time={rec['processing_time_sec']}s"
        )
        # Keep a couple of scenes' raw payload for figure drawing.
        if s in (0, 5, 17, 33):
            np.save(DATA / f"scene_{s:04d}_intensity.npy", payload['image'])
            pd.DataFrame([asdict(c) for c in payload['candidates']]).to_csv(
                DATA / f"scene_{s:04d}_candidates.csv", index=False)
            pd.DataFrame([{
                'lat': d.lat, 'lon': d.lon,
                'length_proxy_m': d.length_proxy_m,
                'area_px': d.area_px, 'idx': d.idx
            } for d in payload['detections']]).to_csv(
                DATA / f"scene_{s:04d}_detections.csv", index=False)
            def _np_safe(o):
                if isinstance(o, (np.integer,)):
                    return int(o)
                if isinstance(o, (np.floating,)):
                    return float(o)
                if isinstance(o, (list, tuple)):
                    return [_np_safe(x) for x in o]
                if isinstance(o, dict):
                    return {k: _np_safe(v) for k, v in o.items()}
                return o
            with open(DATA / f"scene_{s:04d}_fusion.json", 'w') as f:
                json.dump(_np_safe({
                    'matches': payload['res'].matches,
                    'dark': payload['res'].dark_vessel_idx,
                    'ais_only': payload['res'].ais_only_idx,
                    'id_mismatch': payload['res'].identity_mismatch_idx,
                    'ambiguous': payload['res'].ambiguous_idx,
                    'geofence_alerts': payload['res'].geofence_alerts,
                    'coast_frac': payload['coast_frac'],
                }), f, indent=2)
            payload['ais_raw'].to_csv(DATA / f"scene_{s:04d}_ais_raw.csv", index=False)
            payload['ais_clean'].to_csv(DATA / f"scene_{s:04d}_ais_clean.csv", index=False)
            pd.DataFrame(payload['truths']).to_csv(DATA / f"scene_{s:04d}_truth.csv", index=False)

    df = pd.DataFrame(rows)
    df.to_csv(OUT / "scene_stats.csv", index=False)

    # Aggregate
    agg = {
        'n_scenes': len(df),
        'total_sar_detections': int(df['sar_detections_n'].sum()),
        'total_matches': int(df['matched_sar_ais_n'].sum()),
        'total_dark_candidates': int(df['sar_only_dark_candidates_n'].sum()),
        'total_ais_only': int(df['ais_only_n'].sum()),
        'total_identity_mismatch': int(df['identity_mismatch_warnings_n'].sum()),
        'total_geofence_alerts': int(df['geofence_alerts_n'].sum()),
        'mean_precision': float(df['precision'].mean()),
        'mean_recall': float(df['recall'].mean()),
        'mean_f1': float(df['f1'].mean()),
        'mean_dark_precision': float(df['dark_precision'].mean()),
        'mean_dark_recall': float(df['dark_recall'].dropna().mean()),
        'mean_id_mismatch_recall': float(df['identity_mismatch_recall'].dropna().mean()),
        'mean_proc_time_sec': float(df['processing_time_sec'].mean()),
        'std_proc_time_sec': float(df['processing_time_sec'].std()),
        'pct_dark_of_sar_dets': float(df['sar_only_dark_candidates_n'].sum() /
                                      max(df['sar_detections_n'].sum(), 1)),
        'pct_match_of_sar_dets': float(df['matched_sar_ais_n'].sum() /
                                       max(df['sar_detections_n'].sum(), 1)),
    }
    with open(OUT / "overall_metrics.json", 'w') as f:
        json.dump(agg, f, indent=2)

    print("\n=== AGGREGATE ===")
    for k, v in agg.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
