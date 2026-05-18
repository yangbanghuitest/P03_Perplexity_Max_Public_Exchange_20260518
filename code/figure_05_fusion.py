"""Figure 5. SAR-AIS association and the five evidence classes.

A single panel showing one simulated scene with:
- matched SAR-AIS pairs (lines connecting them, teal)
- SAR-only / dark-vessel candidates (red triangles)
- AIS-only candidates (gold circles)
- identity-mismatch (purple rings)
- geofence-violating targets (terra outline)
- adaptive gate radius for one example pair
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
from matplotlib.lines import Line2D
from pathlib import Path
import json

import sys; sys.path.insert(0, '/home/user/workspace/paper_v2/code')
from figs_setup import COLORS, CLASS_COLORS, save


DATA = Path("/home/user/workspace/paper_v2/data")


def fig5():
    scene = '0017'
    dets = pd.read_csv(DATA / f"scene_{scene}_detections.csv")
    cands = pd.read_csv(DATA / f"scene_{scene}_candidates.csv")
    with open(DATA / f"scene_{scene}_fusion.json") as f:
        fus = json.load(f)
    matches = fus['matches']
    dark = set(fus['dark'])
    ais_only = set(fus['ais_only'])
    id_mis = {tuple(p) for p in fus['id_mismatch']}
    gf_alerts = fus['geofence_alerts']

    fig, ax = plt.subplots(figsize=(10.5, 8.0))

    # geofence rectangle (from sim default)
    LAT_C, LON_C = 24.5, 119.5
    ax.add_patch(Rectangle((LON_C - 0.024, LAT_C - 0.022),
                           2 * 0.024, 2 * 0.022,
                           linestyle='--', lw=1.4,
                           edgecolor=COLORS['mauve'],
                           facecolor=COLORS['mauve'], alpha=0.07))
    ax.text(LON_C, LAT_C + 0.026, 'Emergency AOI (geofence)',
            ha='center', va='bottom', fontsize=8.5, color=COLORS['mauve'],
            weight='bold')

    # match links
    matched_d_idx = set()
    matched_a_idx = set()
    for d_idx, a_idx in matches:
        d = dets.iloc[d_idx]
        c = cands.iloc[a_idx]
        is_id_mis = (d_idx, a_idx) in id_mis
        link_color = CLASS_COLORS['identity_mismatch'] if is_id_mis else CLASS_COLORS['matched']
        ax.plot([d['lon'], c['lon']], [d['lat'], c['lat']],
                '-', color=link_color, lw=0.9, alpha=0.85, zorder=2)
        matched_d_idx.add(d_idx)
        matched_a_idx.add(a_idx)

    # SAR detections
    for i, d in dets.iterrows():
        if i in dark:
            color = CLASS_COLORS['dark']
            ax.scatter(d['lon'], d['lat'], marker='^', s=80,
                       facecolor=color, edgecolor='white', lw=0.8,
                       zorder=4)
        else:
            ax.scatter(d['lon'], d['lat'], marker='s', s=44,
                       facecolor='white', edgecolor=CLASS_COLORS['matched'],
                       lw=1.2, zorder=3)

    # AIS candidates
    for j, c in cands.iterrows():
        if j in ais_only:
            color = CLASS_COLORS['ais_only']
            ax.scatter(c['lon'], c['lat'], marker='o', s=55,
                       facecolor=color, edgecolor='white', lw=0.7,
                       alpha=0.95, zorder=3)
        else:
            ax.scatter(c['lon'], c['lat'], marker='o', s=36,
                       facecolor='white', edgecolor=CLASS_COLORS['matched'],
                       lw=1.0, zorder=3)

    # identity-mismatch ring around matched pair (around SAR detection)
    for d_idx, a_idx in id_mis:
        d = dets.iloc[d_idx]
        ax.scatter(d['lon'], d['lat'], marker='o', s=200,
                   facecolor='none',
                   edgecolor=CLASS_COLORS['identity_mismatch'],
                   linewidth=2.0, zorder=5)

    # Show one adaptive-gate radius example: draw a thin circle around a matched
    # pair's SAR detection.
    if matches:
        d_idx, a_idx = matches[0]
        d = dets.iloc[d_idx]
        # use a 250-m visual radius (≈ 0.0023 deg)
        r_deg = 250 / 111320.0
        ax.add_patch(Circle((d['lon'], d['lat']), r_deg,
                            fill=False,
                            edgecolor=COLORS['teal_dark'],
                            linestyle=':', lw=1.2, zorder=2))
        ax.annotate('adaptive search radius $r_j$',
                    xy=(d['lon'] + r_deg, d['lat']),
                    xytext=(d['lon'] + r_deg + 0.005, d['lat'] + 0.005),
                    fontsize=8, color=COLORS['teal_dark'],
                    arrowprops=dict(arrowstyle='->', color=COLORS['teal_dark'],
                                    lw=0.8))

    ax.set_xlabel('Longitude (°E)')
    ax.set_ylabel('Latitude (°N)')
    ax.set_aspect('equal', adjustable='box')
    ax.set_title(f"SAR-AIS evidence fusion on scene SIM_{scene}\n"
                 f"{len(matches)} matched  •  {len(dark)} dark candidates  •  "
                 f"{len(ais_only)} AIS-only  •  {len(id_mis)} identity mismatches  •  "
                 f"{len(gf_alerts)} geofence alerts",
                 fontsize=11, weight='bold', loc='left', pad=10)

    legend_h = [
        Line2D([0], [0], marker='s', linestyle='None', markersize=8,
               markerfacecolor='white', markeredgecolor=CLASS_COLORS['matched'],
               markeredgewidth=1.2, label='Matched SAR detection'),
        Line2D([0], [0], marker='o', linestyle='None', markersize=7,
               markerfacecolor='white', markeredgecolor=CLASS_COLORS['matched'],
               markeredgewidth=1.0, label='Matched AIS candidate'),
        Line2D([0], [0], color=CLASS_COLORS['matched'], lw=1.2,
               label='Matched-pair link'),
        Line2D([0], [0], marker='^', linestyle='None', markersize=10,
               markerfacecolor=CLASS_COLORS['dark'], markeredgecolor='white',
               label='Dark-vessel candidate (SAR-only)'),
        Line2D([0], [0], marker='o', linestyle='None', markersize=9,
               markerfacecolor=CLASS_COLORS['ais_only'], markeredgecolor='white',
               label='AIS-only candidate'),
        Line2D([0], [0], marker='o', linestyle='None', markersize=12,
               markerfacecolor='none',
               markeredgecolor=CLASS_COLORS['identity_mismatch'],
               markeredgewidth=2.0,
               label='Identity-mismatch warning'),
    ]
    ax.legend(handles=legend_h, loc='upper right', fontsize=8,
              framealpha=0.95, edgecolor=COLORS['grid'])

    save(fig, "fig05_fusion_result")


if __name__ == "__main__":
    fig5()
