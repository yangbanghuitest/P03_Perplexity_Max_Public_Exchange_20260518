"""Common matplotlib styling for all figures in the manuscript.

Journal target: *Remote Sensing* (MDPI). Final figures are exported at
300 dpi PNG. Colour palette derives from the project design system, with a
chart-friendly variant (Teal `#20808D`, Terra `#A84B2F`, Dark teal `#1B474D`,
Mauve `#944454`, Gold `#FFC553`).
"""
import matplotlib as mpl
import matplotlib.pyplot as plt

# ---- single source of truth for colours ----
COLORS = {
    'teal':      '#20808D',   # primary
    'teal_dark': '#1B474D',
    'teal_light':'#7FBDC4',
    'terra':     '#A84B2F',
    'mauve':     '#944454',
    'gold':      '#D19900',
    'olive':     '#848456',
    'brown':     '#6E522B',
    'red':       '#A13544',
    'green':     '#437A22',
    'blue':      '#006494',
    'purple':    '#7A39BB',
    'bg':        '#FBFBF9',
    'text':      '#28251D',
    'muted':     '#7A7974',
    'grid':      '#D4D1CA',
    'border':    '#28251D',
}

# Class colours used consistently across the paper
CLASS_COLORS = {
    'matched':            '#20808D',  # cooperative SAR-AIS pair
    'dark':               '#A13544',  # dark-vessel candidate (red)
    'ais_only':           '#D19900',  # AIS-only
    'identity_mismatch':  '#7A39BB',  # spoofing / mismatch
    'geofence':           '#A84B2F',  # geofence alert
}

# ---- style ----
mpl.rcParams.update({
    'font.family':       'DejaVu Sans',
    'font.size':         9,
    'axes.titlesize':    10,
    'axes.titleweight':  'bold',
    'axes.labelsize':    9,
    'axes.labelcolor':   COLORS['text'],
    'axes.edgecolor':    COLORS['text'],
    'axes.linewidth':    0.8,
    'axes.spines.top':   False,
    'axes.spines.right': False,
    'axes.grid':         True,
    'grid.color':        COLORS['grid'],
    'grid.alpha':        0.6,
    'grid.linewidth':    0.5,
    'xtick.color':       COLORS['text'],
    'ytick.color':       COLORS['text'],
    'xtick.labelsize':   8,
    'ytick.labelsize':   8,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'legend.fontsize':   8,
    'legend.frameon':    False,
    'figure.facecolor':  'white',
    'axes.facecolor':    'white',
    'savefig.facecolor': 'white',
    'savefig.dpi':       300,
    'savefig.bbox':      'tight',
    'pdf.fonttype':      42,
    'ps.fonttype':       42,
})


def save(fig, name, fmt=('png', 'pdf')):
    """Save figure to /home/user/workspace/paper_v2/figures/<name>.{png,pdf}."""
    from pathlib import Path
    out = Path("/home/user/workspace/paper_v2/figures")
    out.mkdir(parents=True, exist_ok=True)
    for f in fmt:
        fig.savefig(out / f"{name}.{f}", dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f"saved {name} -> figures/")
