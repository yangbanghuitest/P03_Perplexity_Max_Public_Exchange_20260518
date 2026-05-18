"""Figure 4. AIS trajectory cleaning and scene-time interpolation.

Two panels:
(a) raw AIS dots vs cleaned tracks for several vessels
(b) interpolation to satellite acquisition time t_s, with the ±5-min window
    shown as a band, and the interpolated position marked.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from pathlib import Path

import sys; sys.path.insert(0, '/home/user/workspace/paper_v2/code')
from figs_setup import COLORS, save


DATA = Path("/home/user/workspace/paper_v2/data")


def fig4():
    raw = pd.read_csv(DATA / "scene_0005_ais_raw.csv")
    clean = pd.read_csv(DATA / "scene_0005_ais_clean.csv")
    # find 6 well-populated MMSIs for (a)
    counts = raw['mmsi'].value_counts()
    candidates = counts[(counts >= 30) & (counts <= 60)].index[:6]

    fig, axs = plt.subplots(1, 2, figsize=(13.5, 5.5),
                            gridspec_kw=dict(width_ratios=[1.3, 1.0]))

    # ---- (a) raw vs cleaned trajectories ----
    palette = ['#20808D', '#A84B2F', '#1B474D', '#944454', '#D19900', '#7A39BB']
    ax = axs[0]
    for k, mmsi in enumerate(candidates):
        ra = raw[raw['mmsi'] == mmsi].sort_values('ts')
        ca = clean[clean['mmsi'] == mmsi].sort_values('ts')
        ax.plot(ra['lon'], ra['lat'], 'o', color=palette[k % 6],
                markersize=2.5, alpha=0.4, zorder=2)
        ax.plot(ca['lon'], ca['lat'], '-', color=palette[k % 6],
                linewidth=1.5, alpha=0.95, zorder=3)
        ax.scatter(ca['lon'].iloc[-1], ca['lat'].iloc[-1],
                   marker='>', s=42, color=palette[k % 6],
                   edgecolor='white', linewidth=0.6, zorder=4)

    # also show some "invalid" rows (where lat,lon out of range)
    bad = raw[(raw['lat'] > 90) | (raw['lat'] < -90)]
    if len(bad):
        ax.scatter([], [], marker='x', color=COLORS['red'],
                   s=40, label='invalid AIS (removed)')

    ax.set_xlabel('Longitude (°E)')
    ax.set_ylabel('Latitude (°N)')
    ax.set_title('(a) Per-MMSI track reconstruction',
                 loc='left', fontsize=10, weight='bold')

    legend1 = [
        Line2D([0], [0], marker='o', linestyle='None',
               color=COLORS['muted'], markerfacecolor=COLORS['muted'],
               markersize=4, label='Raw AIS points'),
        Line2D([0], [0], linestyle='-', color=COLORS['muted'], lw=1.5,
               label='Cleaned, MMSI-grouped track'),
        Line2D([0], [0], marker='>', linestyle='None',
               color=COLORS['muted'], markerfacecolor=COLORS['muted'],
               markersize=8, label='Last cleaned position'),
    ]
    ax.legend(handles=legend1, loc='best', fontsize=8,
              framealpha=0.9, edgecolor=COLORS['grid'])

    # ---- (b) time-axis interpolation diagram ----
    ax2 = axs[1]
    # take one mmsi, plot ts vs lat
    mmsi = candidates[0]
    ca = clean[clean['mmsi'] == mmsi].sort_values('ts').reset_index(drop=True)
    # define t_s as the median sample time
    t_s = ca['ts'].median()
    rel = ca['ts'] - t_s

    # Restrict the time window we show to [-400, +400] s
    rng_lo, rng_hi = -400, 400

    # ±5-min interpolation band (in DATA coordinates)
    ax2.axvspan(-300, 300, color=COLORS['gold'], alpha=0.18, zorder=0)

    # raw samples (markers)
    in_window = (rel >= rng_lo) & (rel <= rng_hi)
    ax2.scatter(rel[in_window], ca['lat'][in_window],
                color=COLORS['teal'], s=26, zorder=3,
                label='AIS samples', edgecolor='white', linewidth=0.6)

    # interpolate at t_s, plot interpolated point
    idx = (rel <= 0).sum() - 1
    t0 = rel.iloc[idx]; t1 = rel.iloc[idx + 1]
    a = (0 - t0) / (t1 - t0)
    lat_i = ca['lat'].iloc[idx] + a * (ca['lat'].iloc[idx + 1] - ca['lat'].iloc[idx])
    ax2.plot([t0, t1], [ca['lat'].iloc[idx], ca['lat'].iloc[idx + 1]],
             '--', color=COLORS['teal_dark'], lw=1.4, zorder=2)
    ax2.scatter([0], [lat_i], marker='*', s=200, color=COLORS['terra'],
                edgecolor='white', linewidth=0.8, zorder=4,
                label='Interpolated at $t_s$')
    # vertical t_s line
    ax2.axvline(0, color=COLORS['terra'], lw=1.0, ls=':')

    ax2.set_xlim(rng_lo, rng_hi)
    # set sensible y range based on local samples
    yvals = ca['lat'][in_window]
    if len(yvals) > 0:
        y_pad = max(0.0005, (yvals.max() - yvals.min()) * 0.20)
        ax2.set_ylim(yvals.min() - y_pad, yvals.max() + y_pad)

    # text labels: ALWAYS in axes coords
    ax2.text(0.5, 0.96, '±5-min interpolation window',
             ha='center', va='top', fontsize=9, color=COLORS['gold'],
             weight='bold', transform=ax2.transAxes,
             bbox=dict(facecolor='white', edgecolor='none', alpha=0.85, pad=2))
    ax2.text(0.50, 0.04, 'satellite $t_s$',
             ha='center', va='bottom', fontsize=8.5, color=COLORS['terra'],
             weight='bold', transform=ax2.transAxes,
             bbox=dict(facecolor='white', edgecolor='none', alpha=0.85, pad=2))

    ax2.set_xlabel('Time relative to $t_s$ (s)')
    ax2.set_ylabel('Latitude (°N)')
    ax2.set_title('(b) Scene-time interpolation for one MMSI',
                  loc='left', fontsize=10, weight='bold')
    ax2.legend(loc='lower right', fontsize=8, framealpha=0.95,
               edgecolor=COLORS['grid'])

    fig.suptitle('AIS scene-time reconstruction aligns cooperative tracks to the SAR acquisition instant',
                 fontsize=11, weight='bold', y=1.02)
    plt.tight_layout()
    save(fig, "fig04_ais_interp")


if __name__ == "__main__":
    fig4()
