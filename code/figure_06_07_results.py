"""Figures 6 and 7: scene-level results from 50 simulated scenes.

Figure 6. Per-scene composition of the five evidence classes (stacked bars)
          + confusion matrix for SAR ship detection vs ground-truth.
Figure 7. Detection-quality figures: precision/recall/F1 scatter,
          processing-time histogram, and Pareto comparison with literature.
"""
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from pathlib import Path

import sys; sys.path.insert(0, '/home/user/workspace/paper_v2/code')
from figs_setup import COLORS, CLASS_COLORS, save


OUT = Path("/home/user/workspace/paper_v2/output")
df = pd.read_csv(OUT / "scene_stats.csv")
metrics = json.load(open(OUT / "overall_metrics.json"))


# ----------------------- Figure 6 -----------------------------------------
def fig6():
    fig = plt.figure(figsize=(13.5, 5.5))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.5, 1.0], wspace=0.30)

    # (a) stacked bar: composition per scene
    ax = fig.add_subplot(gs[0])
    scenes = np.arange(1, len(df) + 1)
    bottom = np.zeros(len(df))
    series = [
        ('Matched cooperative', df['matched_sar_ais_n'], CLASS_COLORS['matched']),
        ('Dark-vessel candidate', df['sar_only_dark_candidates_n'], CLASS_COLORS['dark']),
        ('AIS-only',              df['ais_only_n'],                 CLASS_COLORS['ais_only']),
        ('Identity mismatch',     df['identity_mismatch_warnings_n'], CLASS_COLORS['identity_mismatch']),
        ('Geofence alert',        df['geofence_alerts_n'],          CLASS_COLORS['geofence']),
    ]
    for name, vals, c in series:
        ax.bar(scenes, vals, bottom=bottom, color=c, edgecolor='white',
               linewidth=0.4, label=name, width=0.85)
        bottom = bottom + vals.values

    ax.set_xlabel('Scene index')
    ax.set_ylabel('Number of vessels / alerts per scene')
    ax.set_title('(a) Per-scene composition of the five evidence classes (50 simulated scenes)',
                 loc='left', fontsize=10, weight='bold')
    ax.legend(loc='upper right', fontsize=8, framealpha=0.95,
              edgecolor=COLORS['grid'], ncol=2)
    ax.set_xlim(0.3, 50.7)
    ax.grid(axis='y', color=COLORS['grid'], alpha=0.5, lw=0.4)

    # (b) confusion-matrix style summary
    ax2 = fig.add_subplot(gs[1])
    tp = int(df['tp'].sum())
    fp = int(df['fp'].sum())
    fn = int(df['fn'].sum())
    # We do not know "true negatives" for SAR detection.
    cm = np.array([[tp, fn], [fp, 0]])
    labels = [['TP\n(detected\nship)', 'FN\n(missed\nship)'],
              ['FP\n(false\nalarm)',   'TN\n(undefined)']]
    cmap = plt.cm.Blues
    norm = plt.Normalize(vmin=0, vmax=max(cm.max(), 1))
    for i in range(2):
        for j in range(2):
            ax2.add_patch(plt.Rectangle((j, 1 - i), 1, 1,
                                        facecolor=cmap(norm(cm[i, j])) if (i, j) != (1, 1) else '#EEEEEE',
                                        edgecolor='white', linewidth=2))
            txt = labels[i][j] + (f'\n\n{cm[i, j]}' if (i, j) != (1, 1) else '\n\n—')
            ax2.text(j + 0.5, 1 - i + 0.5, txt, ha='center', va='center',
                     fontsize=10, weight='bold',
                     color='white' if cm[i, j] > cm.max() * 0.5 else COLORS['text'])
    # Headers
    ax2.text(0.5, 2.20, 'Predicted: ship', ha='center', va='bottom',
             fontsize=9, weight='bold', color=COLORS['text'])
    ax2.text(1.5, 2.20, 'Predicted: no ship', ha='center', va='bottom',
             fontsize=9, weight='bold', color=COLORS['text'])
    ax2.text(-0.05, 1.5, 'Truth: ship', ha='right', va='center',
             fontsize=9, weight='bold', color=COLORS['text'],
             rotation=90)
    ax2.text(-0.05, 0.5, 'Truth: no ship', ha='right', va='center',
             fontsize=9, weight='bold', color=COLORS['text'],
             rotation=90)
    # Metrics underneath
    P = metrics['mean_precision']
    R = metrics['mean_recall']
    F = metrics['mean_f1']
    ax2.text(1.0, -0.42,
             f"mean Precision = {P:.3f}    mean Recall = {R:.3f}    mean F1 = {F:.3f}",
             ha='center', va='center', fontsize=10, color=COLORS['text'],
             weight='bold')
    ax2.set_xlim(-0.5, 2.10)
    ax2.set_ylim(-0.7, 2.6)
    ax2.set_aspect('equal')
    ax2.set_axis_off()
    ax2.set_title('(b) SAR detection vs. ground truth (50 scenes pooled)',
                  loc='left', fontsize=10, weight='bold')

    save(fig, "fig06_scene_composition")


# ----------------------- Figure 7 -----------------------------------------
def fig7():
    fig = plt.figure(figsize=(13.5, 5.0))
    gs = fig.add_gridspec(1, 3, wspace=0.32)

    # (a) Precision-Recall scatter per scene, sized by SAR detection count
    ax = fig.add_subplot(gs[0])
    sc = ax.scatter(df['recall'], df['precision'],
                    s=20 + 1.2 * df['sar_detections_n'],
                    c=df['n_vessels_true'], cmap='viridis',
                    edgecolor='white', linewidth=0.5, alpha=0.85)
    cb = fig.colorbar(sc, ax=ax, fraction=0.05, pad=0.02)
    cb.set_label('True vessels per scene', fontsize=8)
    cb.ax.tick_params(labelsize=7)
    ax.plot([0, 1], [0, 1], '--', color=COLORS['muted'], lw=0.6)
    # Iso-F1 contours
    for f in [0.5, 0.7, 0.8, 0.9]:
        r = np.linspace(f / (2 - f) + 1e-3, 1, 100)
        p = f * r / (2 * r - f)
        keep = (p > 0) & (p <= 1.05)
        ax.plot(r[keep], p[keep], ':', color=COLORS['muted'], lw=0.5,
                alpha=0.6)
        ax.text(0.98, p[keep][-1] - 0.01, f'F1={f}',
                fontsize=7, color=COLORS['muted'])
    ax.set_xlim(0, 1.05)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel('Recall')
    ax.set_ylabel('Precision')
    ax.set_title('(a) Per-scene SAR detection P/R\n(marker size ∝ #detections)',
                 loc='left', fontsize=10, weight='bold')

    # (b) Processing-time histogram
    ax2 = fig.add_subplot(gs[1])
    ax2.hist(df['processing_time_sec'], bins=15,
             color=COLORS['teal'], edgecolor='white', linewidth=0.6)
    mu = df['processing_time_sec'].mean()
    ax2.axvline(mu, color=COLORS['terra'], lw=1.4, ls='--')
    ax2.text(mu, ax2.get_ylim()[1] * 0.95, f'  μ = {mu:.2f} s', va='top',
             ha='left', fontsize=9, color=COLORS['terra'], weight='bold')
    ax2.set_xlabel('Processing time per scene (s, single core)')
    ax2.set_ylabel('Number of scenes')
    ax2.set_title('(b) Throughput at 15 km × 15 km / scene\n(deployment budget: ≤ 60 min)',
                  loc='left', fontsize=10, weight='bold')

    # (c) Class share donut
    ax3 = fig.add_subplot(gs[2])
    totals = [
        ('Matched cooperative', metrics['total_matches'],          CLASS_COLORS['matched']),
        ('Dark-vessel cand.',  metrics['total_dark_candidates'],   CLASS_COLORS['dark']),
        ('AIS-only',            metrics['total_ais_only'],         CLASS_COLORS['ais_only']),
        ('Identity mismatch',   metrics['total_identity_mismatch'], CLASS_COLORS['identity_mismatch']),
        ('Geofence alert',      metrics['total_geofence_alerts'],   CLASS_COLORS['geofence']),
    ]
    vals = [t[1] for t in totals]
    labels = [f"{t[0]}\n({t[1]})" for t in totals]
    colors = [t[2] for t in totals]
    wedges, _ = ax3.pie(vals, colors=colors, startangle=90,
                        wedgeprops=dict(width=0.42, edgecolor='white', linewidth=2))
    # central label
    total_all = sum(vals)
    ax3.text(0, 0.10, f"{total_all}", ha='center', va='center',
             fontsize=18, weight='bold', color=COLORS['text'])
    ax3.text(0, -0.15, "evidence items\nin 50 scenes",
             ha='center', va='center', fontsize=8, color=COLORS['muted'])
    ax3.set_title('(c) Aggregate composition of the\nevidence-fusion product',
                  loc='left', fontsize=10, weight='bold')
    # custom legend below
    ax3.legend(wedges, labels, loc='center left',
               bbox_to_anchor=(1.05, 0.5),
               fontsize=8, frameon=False)

    save(fig, "fig07_aggregate_metrics")


if __name__ == "__main__":
    fig6()
    fig7()
