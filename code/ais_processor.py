"""
AIS trajectory cleaning, MMSI association and scene-time interpolation
======================================================================

Implements the AIS processing pipeline described in the platform software
design document:
1. Decode and basic validation (MMSI / lat-lon / speed sanity check).
2. Remove invalid MMSI, impossible coordinates, and overlapping duplicate
   timestamps.
3. Group records by MMSI to form per-vessel tracks.
4. Reject sparse tracks (< n_min points or median gap > τ_gap).
5. Reject anomalous drift points (instantaneous speed > v_max).
6. Linearly interpolate each track to a target satellite-acquisition time
   t_s, returning the per-vessel scene-time position estimate together with
   a time-offset δt and a track-quality score q.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from dataclasses import dataclass
from typing import List, Optional


# ---------------------- helpers --------------------------------------------

R_EARTH = 6371000.0


def haversine(lat1, lon1, lat2, lon2):
    """Great-circle distance in metres. Vectorised."""
    lat1r, lon1r, lat2r, lon2r = map(np.radians, (lat1, lon1, lat2, lon2))
    dlat = lat2r - lat1r
    dlon = lon2r - lon1r
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1r) * np.cos(lat2r) * np.sin(dlon / 2) ** 2
    return 2 * R_EARTH * np.arcsin(np.sqrt(np.clip(a, 0, 1)))


# ---------------------- AIS data structures --------------------------------

@dataclass
class AISCandidate:
    mmsi: int
    lat: float                # interpolated lat at t_s
    lon: float                # interpolated lon at t_s
    sog: float                # speed over ground (knots) at nearest sample
    cog: float                # course over ground (degrees)
    dt_seconds: float         # |t_s - nearest AIS time|
    quality: float            # 0..1 quality score
    ship_type: Optional[int] = None
    length_m: Optional[float] = None
    width_m: Optional[float] = None


# ---------------------- cleaning + interpolation ---------------------------

def valid_mmsi(m: int) -> bool:
    """Valid MMSI is 9 digits, leading digit not 0."""
    if pd.isna(m):
        return False
    m = int(m)
    return 100_000_000 <= m <= 999_999_999


def clean_ais(df: pd.DataFrame, v_max_knots: float = 60.0) -> pd.DataFrame:
    """Apply rules from platform design doc.

    df columns required: mmsi, ts (unix sec), lat, lon, sog, cog
    """
    df = df.copy()

    # 1. valid MMSI
    df = df[df['mmsi'].apply(valid_mmsi)].copy()

    # 2. coordinate sanity
    df = df[df['lat'].between(-90, 90) & df['lon'].between(-180, 180)]

    # 3. drop duplicates (same mmsi + ts)
    df = df.sort_values(['mmsi', 'ts']).drop_duplicates(['mmsi', 'ts'])

    # 4. drift filter: compute per-vessel instantaneous speed and drop
    #    points where the implied speed exceeds v_max_knots.
    keep = np.ones(len(df), dtype=bool)
    for mmsi, sub in df.groupby('mmsi'):
        idx = sub.index.to_numpy()
        if len(idx) < 2:
            continue
        lat = sub['lat'].to_numpy()
        lon = sub['lon'].to_numpy()
        ts = sub['ts'].to_numpy()
        d = haversine(lat[:-1], lon[:-1], lat[1:], lon[1:])
        dt = np.diff(ts)
        speed_mps = d / np.maximum(dt, 1.0)
        speed_knots = speed_mps * 1.94384
        bad = np.where(speed_knots > v_max_knots)[0] + 1  # mark the *destination* sample
        keep[np.isin(np.arange(len(df)), np.where(np.isin(df.index, idx[bad]))[0])] = False
    return df[keep].copy()


def interpolate_to_scene_time(df: pd.DataFrame,
                              t_s: float,
                              window_sec: float = 300.0,
                              max_extrap_sec: float = 60.0,
                              min_points: int = 3) -> List[AISCandidate]:
    """Reconstruct vessel positions at satellite acquisition time t_s.

    For each MMSI: if the two AIS samples bracketing t_s are within
    `window_sec`, linearly interpolate. Otherwise allow at most
    `max_extrap_sec` of constant-velocity extrapolation using the
    nearest sample's sog/cog. Tracks with fewer than `min_points`
    cleaned samples are rejected.
    """
    out: List[AISCandidate] = []
    for mmsi, sub in df.groupby('mmsi'):
        sub = sub.sort_values('ts')
        if len(sub) < min_points:
            continue

        ts = sub['ts'].to_numpy()
        lat = sub['lat'].to_numpy()
        lon = sub['lon'].to_numpy()
        sog = sub['sog'].to_numpy()
        cog = sub['cog'].to_numpy()

        # Find brackets
        if ts[0] <= t_s <= ts[-1]:
            k = np.searchsorted(ts, t_s)
            t0, t1 = ts[k - 1], ts[k]
            dt = t1 - t0
            if dt > window_sec:
                # bracket gap too wide → skip
                continue
            a = (t_s - t0) / max(dt, 1.0)
            lat_i = lat[k - 1] + a * (lat[k] - lat[k - 1])
            lon_i = lon[k - 1] + a * (lon[k] - lon[k - 1])
            dt_near = min(abs(t_s - t0), abs(t_s - t1))
            q = max(0.0, 1.0 - dt_near / window_sec)
            sog_i = sog[k - 1] + a * (sog[k] - sog[k - 1])
            cog_i = cog[k - 1]
        else:
            # nearest sample outside bracket → small extrapolation
            if t_s < ts[0]:
                idx = 0
                sign = -1
            else:
                idx = -1
                sign = +1
            dt_near = abs(t_s - ts[idx])
            if dt_near > max_extrap_sec:
                continue
            # constant-velocity propagation
            v_mps = sog[idx] * 0.514444
            heading = np.radians(cog[idx])
            d = v_mps * dt_near * sign
            # convert metres to deg
            dlat = (d * np.cos(heading)) / 111_320.0
            dlon = (d * np.sin(heading)) / (111_320.0 * np.cos(np.radians(lat[idx])))
            lat_i = lat[idx] + dlat
            lon_i = lon[idx] + dlon
            q = max(0.0, 0.6 * (1.0 - dt_near / max_extrap_sec))
            sog_i, cog_i = sog[idx], cog[idx]

        meta = sub.iloc[0]
        out.append(AISCandidate(
            mmsi=int(mmsi),
            lat=float(lat_i),
            lon=float(lon_i),
            sog=float(sog_i),
            cog=float(cog_i),
            dt_seconds=float(dt_near),
            quality=float(q),
            ship_type=int(meta['ship_type']) if 'ship_type' in meta else None,
            length_m=float(meta['length_m']) if 'length_m' in meta and not pd.isna(meta['length_m']) else None,
        ))
    return out


def filter_by_footprint(candidates: List[AISCandidate],
                        lat_min, lat_max, lon_min, lon_max) -> List[AISCandidate]:
    return [c for c in candidates
            if lat_min <= c.lat <= lat_max and lon_min <= c.lon <= lon_max]
