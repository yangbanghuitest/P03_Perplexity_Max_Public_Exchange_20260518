"""
SAR-AIS spatiotemporal evidence fusion
======================================

Given:
- a set of SAR detections D = {(lat, lon, length_proxy, area), ...}
- a set of interpolated AIS candidates A = {(mmsi, lat, lon, sog, cog, dt, q, length), ...}

This module produces:
1. an adaptive search radius for each SAR-AIS candidate pair,
2. a multi-term matching cost,
3. a global assignment using the Hungarian algorithm on valid pairs,
4. classification of every SAR detection / AIS candidate into one of
   {matched, dark-vessel-candidate, ais-only, identity-mismatch, ambiguous},
5. geofence-violation flagging.
"""
from __future__ import annotations

import numpy as np
from dataclasses import dataclass, field
from typing import List, Optional, Tuple
from scipy.optimize import linear_sum_assignment

from ais_processor import AISCandidate, haversine


# ----------------- data types ----------------------------------------------

@dataclass
class SARDetection:
    lat: float
    lon: float
    length_proxy_m: float
    area_px: int
    intensity: float = 0.0
    idx: int = 0       # original index


@dataclass
class FusionResult:
    matches: List[Tuple[int, int]]            # (sar_idx, ais_idx)
    dark_vessel_idx: List[int]                # SAR-only detections
    ais_only_idx: List[int]                   # AIS-only candidates
    identity_mismatch_idx: List[Tuple[int, int]]
    ambiguous_idx: List[Tuple[int, int]]
    geofence_alerts: List[int]                # indices (SAR or AIS) violating fence
    pair_costs: dict = field(default_factory=dict)


# ----------------- adaptive radius and cost --------------------------------

def adaptive_radius_m(c: AISCandidate,
                      r0: float = 200.0,
                      alpha: float = 0.6,
                      beta: float = 50.0,
                      gamma: float = 80.0,
                      sigma_geo: float = 1.0,
                      sigma_sar: float = 1.0) -> float:
    """r_j = r0 + alpha * |dt|*v + beta*sigma_geo + gamma*sigma_sar (in metres)."""
    v_mps = c.sog * 0.514444
    return r0 + alpha * c.dt_seconds * v_mps + beta * sigma_geo + gamma * sigma_sar


def matching_cost(d: SARDetection,
                  c: AISCandidate,
                  r_j: float,
                  w_d: float = 1.0,
                  w_l: float = 0.5,
                  w_h: float = 0.0,
                  w_q: float = 0.3) -> Optional[float]:
    """Return matching cost in [0, ~3] or None if outside gate."""
    dist = haversine(d.lat, d.lon, c.lat, c.lon)
    if dist > r_j:
        return None
    # length inconsistency
    if c.length_m and c.length_m > 0:
        len_err = abs(d.length_proxy_m - c.length_m) / max(c.length_m, 1.0)
        len_err = min(len_err, 1.0)
    else:
        len_err = 0.5  # neutral
    quality_penalty = 1.0 - c.quality
    return (w_d * (dist / r_j)
            + w_l * len_err
            + w_q * quality_penalty)


# ----------------- main fusion ---------------------------------------------

def fuse(detections: List[SARDetection],
         candidates: List[AISCandidate],
         identity_length_tol: float = 0.4,
         ambiguity_margin: float = 0.15,
         geofence_poly: Optional[list] = None,
         **kwargs) -> FusionResult:
    """Run the full fusion pipeline.

    Parameters
    ----------
    detections, candidates : as above
    identity_length_tol : if matched pair's |L_sar - L_ais|/L_ais > tol
                          ⇒ identity-mismatch warning
    ambiguity_margin    : if the second-best cost is within this distance
                          of the best cost ⇒ mark ambiguous
    geofence_poly       : optional list of (lat, lon) polygon vertices.
    """
    n_d = len(detections)
    n_a = len(candidates)
    if n_d == 0 and n_a == 0:
        return FusionResult([], [], [], [], [], [])

    # Build cost matrix (np.inf where gate fails)
    BIG = 1e6
    C = np.full((n_d, max(n_a, 1)), BIG, dtype=np.float64)
    R = np.zeros_like(C)
    for i, d in enumerate(detections):
        for j, c in enumerate(candidates):
            r_j = adaptive_radius_m(c)
            R[i, j] = r_j
            cost = matching_cost(d, c, r_j)
            if cost is not None:
                C[i, j] = cost

    pair_costs = {(i, j): float(C[i, j]) for i in range(n_d) for j in range(n_a) if C[i, j] < BIG}

    # Global assignment via Hungarian on a padded matrix
    if n_a > 0:
        nrow = max(n_d, n_a)
        ncol = nrow
        Cpad = np.full((nrow, ncol), BIG, dtype=np.float64)
        Cpad[:n_d, :n_a] = C
        row_ind, col_ind = linear_sum_assignment(Cpad)
    else:
        row_ind = np.arange(n_d)
        col_ind = np.full(n_d, -1)

    matches: List[Tuple[int, int]] = []
    matched_d = set()
    matched_a = set()
    ambiguous = []
    id_mismatch = []
    for ri, ci in zip(row_ind, col_ind):
        if ri >= n_d or ci >= n_a:
            continue
        if C[ri, ci] >= BIG:
            continue
        # Check ambiguity: is there a second-best within margin?
        best = C[ri, ci]
        row = C[ri, :n_a].copy()
        row[ci] = BIG
        second = row.min()
        if second < BIG and (second - best) < ambiguity_margin:
            ambiguous.append((ri, ci))
            # Still accept the assignment, but flagged
        matches.append((ri, ci))
        matched_d.add(ri)
        matched_a.add(ci)

        # Identity check
        d = detections[ri]
        c = candidates[ci]
        if c.length_m and c.length_m > 0:
            if abs(d.length_proxy_m - c.length_m) / c.length_m > identity_length_tol:
                id_mismatch.append((ri, ci))

    dark = [i for i in range(n_d) if i not in matched_d]
    ais_only = [j for j in range(n_a) if j not in matched_a]

    geofence_alerts = []
    if geofence_poly is not None:
        from shapely.geometry import Polygon, Point
        poly = Polygon([(lon, lat) for lat, lon in geofence_poly])
        for i, d in enumerate(detections):
            if poly.contains(Point(d.lon, d.lat)):
                geofence_alerts.append(('SAR', i))
        for j, c in enumerate(candidates):
            if poly.contains(Point(c.lon, c.lat)):
                geofence_alerts.append(('AIS', j))

    return FusionResult(
        matches=matches,
        dark_vessel_idx=dark,
        ais_only_idx=ais_only,
        identity_mismatch_idx=id_mismatch,
        ambiguous_idx=ambiguous,
        geofence_alerts=geofence_alerts,
        pair_costs=pair_costs,
    )


def evidence_score(is_dark, is_mismatch, is_geofence, low_quality, is_ambiguous,
                   w=(0.40, 0.25, 0.20, 0.10, 0.05)) -> float:
    """Final emergency evidence score in [0, 1]."""
    flags = np.array([is_dark, is_mismatch, is_geofence, low_quality, is_ambiguous], dtype=float)
    return float(np.dot(flags, np.array(w)))
