"""Figure 3. SAR ship detection example.

Four panels using scene 5 of the simulation:
(a) Simulated SAR intensity image (dB scale)
(b) Sea-land mask overlay
(c) CFAR detection binary map
(d) Detected ship boxes with bounding boxes
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path
import json

import sys; sys.path.insert(0, '/home/user/workspace/paper_v2/code')
from figs_setup import COLORS, save
from sar_detector import sea_land_mask, ca_cfar, connected_components


DATA = Path("/home/user/workspace/paper_v2/data")


def fig3():
    full = np.load(DATA / "scene_0005_intensity.npy")
    # zoom into a 700x700 patch in the centre where many ships exist
    H, W = full.shape
    cy, cx = H // 2, W // 2
    SIZE = 700
    y0, y1 = cy - SIZE // 2, cy + SIZE // 2
    x0, x1 = cx - SIZE // 2, cx + SIZE // 2
    img = full[y0:y1, x0:x1]

    # Convert to dB for display (clip)
    img_db = 10 * np.log10(np.maximum(img, 1e-3))
    img_db_clip = np.clip(img_db, -25, 10)

    sea = sea_land_mask(img)
    raw_cfar = ca_cfar(np.where(sea, img, 0.0), 31, 7, 6.5)
    raw_cfar = raw_cfar & sea
    targets = connected_components(raw_cfar, 4, 5000)

    fig, axs = plt.subplots(1, 4, figsize=(15.5, 4.6))
    panels = ['(a) SAR intensity (dB, simulated)',
              '(b) Sea-land mask',
              '(c) CA-CFAR binary map',
              '(d) Detected ship targets']

    for ax in axs:
        ax.set_aspect('equal')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.grid(False)
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_color(COLORS['border'])
            spine.set_linewidth(0.6)

    im = axs[0].imshow(img_db_clip, cmap='gray', vmin=-25, vmax=10)
    axs[0].set_title(panels[0], loc='left', fontsize=10, weight='bold')
    cb = fig.colorbar(im, ax=axs[0], fraction=0.046, pad=0.02)
    cb.set_label('Backscatter (dB)', fontsize=8)
    cb.ax.tick_params(labelsize=7)

    # mask overlay
    axs[1].imshow(img_db_clip, cmap='gray', vmin=-25, vmax=10)
    overlay = np.zeros((*sea.shape, 4))
    overlay[~sea] = [0.65, 0.30, 0.18, 0.55]   # terra alpha
    axs[1].imshow(overlay)
    axs[1].set_title(panels[1], loc='left', fontsize=10, weight='bold')

    # cfar binary (white background, teal pixels for detections)
    cfar_disp = np.ones((*raw_cfar.shape, 3))
    cfar_disp[raw_cfar] = [32 / 255, 128 / 255, 141 / 255]   # teal
    # dilate detection pixels for visibility
    from scipy.ndimage import binary_dilation
    big = binary_dilation(raw_cfar, iterations=3)
    cfar_disp[big] = [32 / 255, 128 / 255, 141 / 255]
    axs[2].imshow(cfar_disp)
    axs[2].set_title(panels[2], loc='left', fontsize=10, weight='bold')
    axs[2].text(0.02, 0.98, f"{raw_cfar.sum()} pixels above CFAR threshold",
                transform=axs[2].transAxes, ha='left', va='top',
                fontsize=8, color=COLORS['teal_dark'], weight='bold',
                bbox=dict(facecolor='white', edgecolor='none', alpha=0.9, pad=2))

    # ships
    axs[3].imshow(img_db_clip, cmap='gray', vmin=-25, vmax=10)
    for t in targets:
        ty0, tx0, ty1, tx1 = t['bbox']
        pad = 14
        rect = Rectangle((tx0 - pad, ty0 - pad),
                         (tx1 - tx0) + 2 * pad,
                         (ty1 - ty0) + 2 * pad,
                         linewidth=1.4, edgecolor=COLORS['gold'],
                         facecolor='none')
        axs[3].add_patch(rect)
    axs[3].set_title(panels[3], loc='left', fontsize=10, weight='bold')
    axs[3].text(0.02, 0.98, f"N = {len(targets)} targets",
                transform=axs[3].transAxes, ha='left', va='top',
                fontsize=9, color=COLORS['gold'], weight='bold',
                bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=2))

    # global title
    fig.suptitle('SAR ship detection pipeline applied to a simulated GF-3-like scene',
                 fontsize=11, weight='bold', y=1.02)

    plt.tight_layout()
    save(fig, "fig03_sar_detection")


if __name__ == "__main__":
    fig3()
