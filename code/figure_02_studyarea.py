"""Figure 2. Study area map + data coverage summary.

Drawn with matplotlib only (no external map tile services). We use a
sketch-style coastline derived from a manually-typed set of vertices so
the figure is fully reproducible from this repo and contains no copyrighted
basemap tiles.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle
from matplotlib.lines import Line2D

import sys; sys.path.insert(0, '/home/user/workspace/paper_v2/code')
from figs_setup import COLORS, save


# Hand-traced simplified coastlines for the Fujian & Taiwan area.
# Coordinates are (lon, lat) in degrees. ~30 vertices each side.
# (Approximate visual sketch — not for navigation.)
FUJIAN_COAST = np.array([
    (117.10, 26.20), (117.60, 26.10), (117.95, 25.60), (118.40, 25.30),
    (118.75, 24.95), (118.90, 24.65), (118.70, 24.45), (118.55, 24.30),
    (118.30, 24.15), (118.20, 24.00), (118.55, 23.80), (118.85, 23.55),
    (119.05, 23.40), (119.25, 23.25), (119.35, 22.95),
])
TAIWAN_COAST = np.array([
    (120.10, 25.20), (120.55, 24.95), (120.65, 24.55), (120.80, 24.20),
    (120.95, 23.85), (120.75, 23.50), (120.70, 23.15), (120.65, 22.85),
    (120.80, 22.55), (121.10, 22.50), (121.45, 22.85), (121.65, 23.30),
    (121.80, 23.80), (121.90, 24.30), (121.95, 24.85), (121.85, 25.20),
    (121.50, 25.30), (121.10, 25.30), (120.65, 25.25), (120.10, 25.20),
])


def fig2():
    fig = plt.figure(figsize=(8.0, 9.5))
    # Two-row layout: map on top (~80%), bar chart strip below (~20%)
    gs = fig.add_gridspec(2, 1, height_ratios=[5, 1], hspace=0.18)
    ax = fig.add_subplot(gs[0])
    inset = fig.add_subplot(gs[1])
    ax.set_xlim(116.5, 122.6)
    ax.set_ylim(22.0, 26.6)
    ax.set_aspect('equal')

    # Ocean background
    ax.set_facecolor('#EAF3F5')

    # Plot Fujian as left polygon (closed with frame edges)
    left = np.vstack([FUJIAN_COAST,
                      [[116.5, FUJIAN_COAST[-1, 1]],
                       [116.5, FUJIAN_COAST[0, 1]]]])
    ax.add_patch(Polygon(left, closed=True, facecolor='#D9D4C5',
                         edgecolor='#5b5648', linewidth=0.8))
    # Taiwan island as polygon
    ax.add_patch(Polygon(TAIWAN_COAST, closed=True, facecolor='#D9D4C5',
                         edgecolor='#5b5648', linewidth=0.8))

    # Strait centre point + sample SAR footprints (boxes)
    rng = np.random.default_rng(20260517)
    n_foot = 14
    lats = rng.uniform(22.6, 25.7, n_foot)
    lons = rng.uniform(118.4, 121.0, n_foot)
    # Mark different sensors
    for i, (la, lo) in enumerate(zip(lats, lons)):
        side = 0.35 + rng.random() * 0.15
        if i % 2 == 0:
            edge = COLORS['teal']
            lw = 1.0
        else:
            edge = COLORS['terra']
            lw = 1.0
        ax.add_patch(Rectangle((lo - side / 2, la - side / 2), side, side,
                               linewidth=lw, edgecolor=edge,
                               facecolor=edge, alpha=0.10))

    # Geofence example (Taiwan Strait middle box)
    ax.add_patch(Rectangle((119.0, 23.7), 1.0, 0.8,
                           linewidth=1.6, edgecolor=COLORS['mauve'],
                           facecolor=COLORS['mauve'], alpha=0.15,
                           linestyle='--'))
    ax.text(119.5, 23.36, 'Emergency AOI\n(geofence example)',
            ha='center', va='top', fontsize=8,
            color=COLORS['mauve'], weight='bold')

    # Labels
    ax.text(117.5, 25.4, 'Fujian, CN', fontsize=11, weight='bold',
            color='#3d3a2f')
    ax.text(120.9, 23.8, 'Taiwan I.', fontsize=11, weight='bold',
            color='#3d3a2f')
    ax.text(118.3, 24.20, 'Xiamen', fontsize=9, color='#3d3a2f')
    ax.scatter([118.10], [24.45], s=25, color='#3d3a2f', zorder=5)
    ax.text(119.6, 25.0, 'Taiwan Strait', fontsize=12, style='italic',
            color='#234a55', weight='bold')

    # Inset N arrow + scale
    ax.annotate('N', xy=(117.0, 26.30), xytext=(117.0, 26.10),
                fontsize=12, ha='center', weight='bold',
                arrowprops=dict(arrowstyle='->', color='black', lw=1.4))

    # Approximate 100 km scale: at lat 24, 1 deg lon ~ 102 km
    bar_x = 121.1
    bar_y = 22.20
    bar_w = 1.0   # ~ 100 km
    ax.plot([bar_x, bar_x + bar_w], [bar_y, bar_y], color='black', lw=2)
    ax.plot([bar_x, bar_x], [bar_y - 0.05, bar_y + 0.05], color='black', lw=2)
    ax.plot([bar_x + bar_w, bar_x + bar_w], [bar_y - 0.05, bar_y + 0.05],
            color='black', lw=2)
    ax.text(bar_x + bar_w / 2, bar_y + 0.10, '~100 km',
            ha='center', va='bottom', fontsize=8)

    # Legend
    legend = [
        Line2D([0], [0], marker='s', linestyle='None', markersize=10,
               markerfacecolor=COLORS['teal'], markeredgecolor=COLORS['teal'],
               alpha=0.4, label='Sentinel-1 footprints'),
        Line2D([0], [0], marker='s', linestyle='None', markersize=10,
               markerfacecolor=COLORS['terra'], markeredgecolor=COLORS['terra'],
               alpha=0.4, label='GF-3 footprints'),
        Line2D([0], [0], marker='s', linestyle='None', markersize=10,
               markerfacecolor=COLORS['mauve'], markeredgecolor=COLORS['mauve'],
               alpha=0.4, label='Geofence (example)'),
    ]
    ax.legend(handles=legend, loc='lower left', framealpha=0.95,
              facecolor='white', edgecolor=COLORS['grid'])

    ax.set_xlabel('Longitude (°E)')
    ax.set_ylabel('Latitude (°N)')
    ax.set_title('Study area: Taiwan Strait and adjacent coastal waters')
    ax.grid(True, color=COLORS['grid'], alpha=0.5, lw=0.4)

    # Bottom panel: data inventory bar chart
    inset.set_facecolor('white')
    cats = ['GF-3 SAR', 'Sentinel-1 SAR', 'Sentinel-2', 'Landsat 8/9', 'GF-1/2/6/7 optical']
    vals = [232, 6044, 1300, 1067, 653]
    colors = [COLORS['teal'], COLORS['teal'],
              COLORS['olive'], COLORS['olive'],
              COLORS['gold']]
    bars = inset.bar(cats, vals, color=colors, edgecolor='none')
    for b, v in zip(bars, vals):
        inset.text(b.get_x() + b.get_width() / 2, b.get_height() * 1.05,
                   f'{v}', ha='center', va='bottom', fontsize=8,
                   weight='bold', color=COLORS['text'])
    inset.set_yscale('log')
    inset.set_ylim(80, 18000)
    inset.tick_params(axis='x', labelsize=8)
    inset.tick_params(axis='y', labelsize=7)
    inset.set_ylabel('Scenes (log)', fontsize=8)
    inset.set_title('Data inventory available for this study',
                    fontsize=9, weight='bold', pad=4, loc='left')
    inset.grid(axis='y', color=COLORS['grid'], alpha=0.5, lw=0.4)

    save(fig, "fig02_study_area")


if __name__ == "__main__":
    fig2()
