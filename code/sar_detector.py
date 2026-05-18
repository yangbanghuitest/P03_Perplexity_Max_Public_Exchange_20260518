"""
CA-CFAR SAR ship detector
==========================

Cell-Averaging Constant False Alarm Rate detector for SAR ship detection,
implemented as described in the platform software design document (CA-CFAR
with reference window R and threshold multiplier K), with connected-component
post-processing and size-based filtering.

This module is self-contained and operates on a 2-D intensity array. It is
intentionally written so that the same code path runs on both real SAR
patches (when provided) and on simulated SAR scenes used in this paper.
"""
from __future__ import annotations

import numpy as np
from scipy.ndimage import label, find_objects
from scipy.signal import convolve2d


def ca_cfar(intensity: np.ndarray,
            ref_size: int = 31,
            guard_size: int = 7,
            K: float = 6.0) -> np.ndarray:
    """Apply 2-D Cell-Averaging CFAR.

    Parameters
    ----------
    intensity : 2-D float array (linear power)
    ref_size  : odd side length of the full reference window (e.g. 31)
    guard_size: odd side length of the guard window inside reference (e.g. 7)
    K         : threshold multiplier (Pfa control). For Rayleigh background,
                Pfa ≈ (1+K/n)^(-n) where n is # ref cells. K=6 ~ Pfa ~ 1e-6.

    Returns
    -------
    detections : binary mask same shape as intensity
    """
    assert ref_size > guard_size and ref_size % 2 == 1 and guard_size % 2 == 1

    # Build reference kernel: 1's in ref window, 0's in guard window (and centre)
    ker = np.ones((ref_size, ref_size), dtype=np.float32)
    g_pad = (ref_size - guard_size) // 2
    ker[g_pad: g_pad + guard_size, g_pad: g_pad + guard_size] = 0.0
    n_ref = ker.sum()

    # Local mean of reference cells via convolution
    mu = convolve2d(intensity, ker / n_ref, mode='same', boundary='symm')

    threshold = K * mu
    return intensity > threshold


def connected_components(mask: np.ndarray,
                         min_pixels: int = 4,
                         max_pixels: int = 5000):
    """Return list of (cy, cx, area, bbox) for each plausible target.

    Filters out blobs smaller than min_pixels or larger than max_pixels
    (typical ships are 4–2000 pixels at Sentinel-1 GRD 10 m resolution).
    """
    lbl, n = label(mask)
    out = []
    for i in range(1, n + 1):
        ys, xs = np.where(lbl == i)
        area = len(ys)
        if area < min_pixels or area > max_pixels:
            continue
        cy = float(ys.mean())
        cx = float(xs.mean())
        bbox = (int(ys.min()), int(xs.min()), int(ys.max()), int(xs.max()))
        out.append({'cy': cy, 'cx': cx, 'area': area, 'bbox': bbox})
    return out


def sea_land_mask(intensity: np.ndarray) -> np.ndarray:
    """Coarse water mask using a strongly smoothed intensity image.

    We smooth the image with a large window and threshold at the mean
    intensity of the dimmest 60% of pixels times a safety factor. Then
    we erode the resulting sea mask by 8 pixels (~80 m at 10 m GSD) to
    suppress the bright nearshore clutter band. This is a placeholder
    for an operational GSHHG / OSM coastline mask.

    Returns True where pixel is sea (usable for ship detection).
    """
    from scipy.ndimage import uniform_filter, binary_erosion
    smoothed = uniform_filter(intensity, size=61)
    low_mean = smoothed[smoothed < np.quantile(smoothed, 0.60)].mean()
    sea = smoothed < 2.0 * max(low_mean, 1e-6)
    sea = binary_erosion(sea, iterations=8)
    return sea


def detect_ships(intensity: np.ndarray,
                 ref_size: int = 31,
                 guard_size: int = 7,
                 K: float = 6.0,
                 min_pixels: int = 4,
                 max_pixels: int = 5000,
                 apply_landmask: bool = True):
    """Full pipeline: optional landmask → CFAR → connected components."""
    if apply_landmask:
        sea = sea_land_mask(intensity)
        # Set land pixels low so they cannot trigger CFAR
        work = np.where(sea, intensity, 0.0)
    else:
        work = intensity
    raw = ca_cfar(work, ref_size, guard_size, K)
    if apply_landmask:
        raw = raw & sea
    targets = connected_components(raw, min_pixels, max_pixels)
    return targets, raw
