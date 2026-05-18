"""Figure 1. Overall SAR-AIS spatiotemporal evidence fusion framework.

A clean six-block flow diagram drawn with matplotlib primitives. We avoid
external diagram tools to keep figures fully reproducible from this repo.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

import sys; sys.path.insert(0, '/home/user/workspace/paper_v2/code')
from figs_setup import COLORS, CLASS_COLORS, save


def box(ax, x, y, w, h, text, fc, ec, tc='white', fs=8.5, weight='bold'):
    rect = FancyBboxPatch((x, y), w, h,
                          boxstyle="round,pad=0.02,rounding_size=0.04",
                          linewidth=0.8,
                          edgecolor=ec, facecolor=fc, zorder=2)
    ax.add_patch(rect)
    ax.text(x + w / 2, y + h / 2, text,
            ha='center', va='center', color=tc, fontsize=fs,
            weight=weight, zorder=3, wrap=True)


def arrow(ax, x1, y1, x2, y2, color=COLORS['text'], lw=1.2, style="-|>"):
    arr = FancyArrowPatch((x1, y1), (x2, y2),
                          arrowstyle=style,
                          mutation_scale=11,
                          color=color, linewidth=lw, zorder=1)
    ax.add_patch(arr)


def fig1():
    fig, ax = plt.subplots(figsize=(11.0, 6.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.set_axis_off()

    # ===== top row: inputs =====
    box(ax, 0.30, 4.9, 1.9, 0.7,
        "SAR scenes\n(GF-3 / S-1)", COLORS['teal_dark'], COLORS['teal_dark'])
    box(ax, 2.40, 4.9, 1.9, 0.7,
        "AIS messages\n(static + dynamic)", COLORS['teal_dark'], COLORS['teal_dark'])
    box(ax, 4.50, 4.9, 1.9, 0.7,
        "Vessel attribute DB\n+ ship chip library", COLORS['teal_dark'], COLORS['teal_dark'])
    box(ax, 6.60, 4.9, 1.9, 0.7,
        "Emergency layers\n(geofence / AOI)", COLORS['teal_dark'], COLORS['teal_dark'])

    # ===== second row: SAR branch and AIS branch (parallel), with gap =====
    box(ax, 0.30, 3.65, 4.10, 0.65,
        "SAR preprocess  •  land mask  •  CA-CFAR  •  CC analysis\n"
        r"$D = \{p_i,\; t_s,\; f_i,\; c_i\}$",
        COLORS['teal'], COLORS['teal'], fs=8)
    box(ax, 5.60, 3.65, 4.10, 0.65,
        "AIS decode  •  MMSI / speed checks  •  per-MMSI tracks\n"
        r"$A_v = \{p_{v,k},\; t_{v,k},\; s_{v,k},\; \theta_{v,k},\; m_v\}$",
        COLORS['gold'], COLORS['gold'], tc=COLORS['text'], fs=8)

    # ===== AIS scene-time interpolation =====
    box(ax, 5.60, 2.55, 4.10, 0.60,
        "Scene-time interp ±5 min  •  footprint filter\n"
        r"$A(t_s) = \{\hat{p}_j,\; m_j,\; \delta t_j,\; q_j\}$",
        COLORS['gold'], COLORS['gold'], tc=COLORS['text'], fs=8)

    # ===== fusion engine =====
    box(ax, 1.30, 1.45, 7.4, 0.70,
        "Adaptive-gate SAR–AIS association  •  Hungarian assignment  •  ambiguity rules",
        COLORS['terra'], COLORS['terra'], fs=9)

    # ===== bottom row: five evidence classes =====
    cls_names = [('Matched\ncooperative', CLASS_COLORS['matched']),
                 ('Dark-vessel\ncandidate',  CLASS_COLORS['dark']),
                 ('AIS-only',              CLASS_COLORS['ais_only']),
                 ('Identity\nmismatch',    CLASS_COLORS['identity_mismatch']),
                 ('Geofence\nviolation',   CLASS_COLORS['geofence'])]
    x0 = 0.30
    w = 1.85
    gap = 0.05
    for i, (lbl, c) in enumerate(cls_names):
        x = x0 + i * (w + gap)
        box(ax, x, 0.20, w, 0.75, lbl, c, c, fs=8.5)

    # ===== arrows =====
    # top inputs -> branches
    arrow(ax, 1.25, 4.90, 2.30, 4.30)       # SAR in -> SAR branch
    arrow(ax, 3.35, 4.90, 3.35, 4.30)       # AIS in -> top edge of SAR branch (visual coherence)
    arrow(ax, 5.45, 4.90, 6.40, 4.30)       # vessel DB -> AIS branch
    arrow(ax, 7.55, 4.90, 7.65, 4.30)       # emergency layers -> AIS branch (right)

    arrow(ax, 7.65, 3.65, 7.65, 3.15)       # AIS branch -> interp
    arrow(ax, 2.30, 3.65, 3.50, 2.20, lw=1.4)  # SAR -> fusion
    arrow(ax, 7.65, 2.55, 6.50, 2.20, lw=1.4)  # interp -> fusion

    # fusion -> evidence row
    for i, (_, c) in enumerate(cls_names):
        x = 0.30 + i * (w + gap) + w / 2
        arrow(ax, 5.0, 1.45, x, 0.97, color=c, lw=1.0)

    # title
    ax.text(5, 5.85, "SAR-AIS spatiotemporal evidence fusion framework",
            ha='center', va='bottom', fontsize=12, weight='bold', color=COLORS['text'])
    ax.text(5, 5.65, "Inputs → SAR / AIS branches → time alignment → adaptive-gate fusion → five evidence classes",
            ha='center', va='bottom', fontsize=8.5, color=COLORS['muted'])
    save(fig, "fig01_framework")


if __name__ == "__main__":
    fig1()
