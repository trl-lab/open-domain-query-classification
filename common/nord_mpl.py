"""
Nord Color Palette for Matplotlib
==================================

A carefully selected subset of Nord colors optimized for data visualization.
Provides maximum color differentiation for clear, beautiful plots.

Based on the Nord color palette: https://www.nordtheme.com
"""

# Full Nord color definitions (for reference)
NORD_COLORS = {
    # Polar Night
    'nord0': '#2E3440',
    'nord1': '#3B4252',
    'nord2': '#434C5E',
    'nord3': '#4C566A',
    # Snow Storm
    'nord4': '#D8DEE9',
    'nord5': '#E5E9F0',
    'nord6': '#ECEFF4',
    # Frost
    'nord7': '#8FBCBB',  # Teal
    'nord8': '#88C0D0',  # Cyan
    'nord9': '#81A1C1',  # Light Blue
    'nord10': '#5E81AC', # Blue
    # Aurora
    'nord11': '#BF616A', # Red
    'nord12': '#D08770', # Orange
    'nord13': '#EBCB8B', # Yellow
    'nord14': '#A3BE8C', # Green
    'nord15': '#B48EAD', # Purple
}

# Matplotlib palette: Maximum differentiation from Frost + Aurora
# Excludes nord8 and nord9 (too similar to nord7 and nord10)
# Colors ordered for maximum contrast between adjacent colors
NORD_PALETTE = [
    '#5E81AC',  # nord10 - Blue
    '#D08770',  # nord12 - Orange (complementary to blue)
    '#A3BE8C',  # nord14 - Green
    '#BF616A',  # nord11 - Red
    '#B48EAD',  # nord15 - Purple
    '#EBCB8B',  # nord13 - Yellow
    '#8FBCBB',  # nord7  - Teal
]

# Named colors for semantic use
NORD_MPL = {
    'blue': '#5E81AC',      # nord10
    'orange': '#D08770',    # nord12
    'green': '#A3BE8C',     # nord14
    'red': '#BF616A',       # nord11
    'purple': '#B48EAD',    # nord15
    'yellow': '#EBCB8B',    # nord13
    'teal': '#8FBCBB',      # nord7
}

# Alternative palettes for specific use cases

# Sequential palette (single hue progression)
NORD_BLUES = [
    '#8FBCBB',  # nord7  - Light teal
    '#88C0D0',  # nord8  - Cyan
    '#81A1C1',  # nord9  - Light blue
    '#5E81AC',  # nord10 - Blue
    '#4C566A',  # nord3  - Dark blue-gray
]

# Diverging palette (for data centered around zero)
NORD_DIVERGING = [
    '#BF616A',  # nord11 - Red (negative)
    '#D08770',  # nord12 - Orange
    '#EBCB8B',  # nord13 - Yellow (neutral)
    '#A3BE8C',  # nord14 - Green
    '#5E81AC',  # nord10 - Blue (positive)
]

# Colorblind-friendly subset (high contrast)
NORD_COLORBLIND = [
    '#5E81AC',  # nord10 - Blue
    '#D08770',  # nord12 - Orange
    '#EBCB8B',  # nord13 - Yellow
    '#8FBCBB',  # nord7  - Teal
]


def set_palette(palette='default'):
    """
    Set the Nord color palette for matplotlib.
    
    Parameters
    ----------
    palette : str, optional
        Which palette to use. Options:
        - 'default': Main 7-color palette (recommended)
        - 'blues': Sequential blues palette
        - 'diverging': Diverging red-to-blue palette
        - 'colorblind': Colorblind-friendly subset
    
    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> from common.nord_mpl import set_palette
    >>> set_palette('default')
    >>> plt.plot([1, 2, 3], [1, 4, 2])
    """
    import matplotlib.pyplot as plt
    
    palettes = {
        'default': NORD_PALETTE,
        'blues': NORD_BLUES,
        'diverging': NORD_DIVERGING,
        'colorblind': NORD_COLORBLIND,
    }
    
    if palette not in palettes:
        raise ValueError(f"Unknown palette '{palette}'. Choose from: {list(palettes.keys())}")
    
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=palettes[palette])
    return palettes[palette]


def get_color(name):
    """
    Get a specific Nord color by name.
    
    Parameters
    ----------
    name : str
        Color name (e.g., 'blue', 'red', 'nord10')
    
    Returns
    -------
    str
        Hex color code
    
    Examples
    --------
    >>> from common.nord_mpl import get_color
    >>> plt.plot([1, 2, 3], color=get_color('blue'))
    """
    if name in NORD_MPL:
        return NORD_MPL[name]
    elif name in NORD_COLORS:
        return NORD_COLORS[name]
    else:
        raise ValueError(f"Unknown color '{name}'")


def show_palette(palette='default', figsize=(10, 2)):
    """
    Display a palette with color swatches and hex codes.
    
    Parameters
    ----------
    palette : str, optional
        Which palette to show
    figsize : tuple, optional
        Figure size (width, height)
    """
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    
    palettes = {
        'default': NORD_PALETTE,
        'blues': NORD_BLUES,
        'diverging': NORD_DIVERGING,
        'colorblind': NORD_COLORBLIND,
    }
    
    colors = palettes.get(palette, NORD_PALETTE)
    
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlim(0, len(colors))
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    for i, color in enumerate(colors):
        rect = mpatches.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='white', linewidth=2)
        ax.add_patch(rect)
        ax.text(i + 0.5, 0.5, color, ha='center', va='center', 
                fontsize=9, color='white', weight='bold',
                bbox=dict(boxstyle='round', facecolor='black', alpha=0.3))
    
    plt.title(f'Nord Palette: {palette}', fontsize=14, pad=10)
    plt.tight_layout()
    return fig


def demo_plot():
    """
    Create a demo plot showing the palette in action.
    """
    import matplotlib.pyplot as plt
    import numpy as np
    
    set_palette('default')
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    
    # Line plot
    x = np.linspace(0, 10, 100)
    for i in range(len(NORD_PALETTE)):
        y = np.sin(x + i * 0.5) + i * 0.3
        ax1.plot(x, y, label=f'Series {i+1}', linewidth=2)
    
    ax1.set_title('Line Plot with Nord Colors', fontsize=12, weight='bold')
    ax1.set_xlabel('X axis')
    ax1.set_ylabel('Y axis')
    ax1.legend(loc='upper left', frameon=True, fancybox=True)
    ax1.grid(True, alpha=0.3)
    
    # Bar plot
    categories = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    values = [23, 45, 56, 78, 32, 67, 43]
    bars = ax2.bar(categories, values)
    
    # Color each bar with palette
    for bar, color in zip(bars, NORD_PALETTE):
        bar.set_color(color)
    
    ax2.set_title('Bar Plot with Nord Colors', fontsize=12, weight='bold')
    ax2.set_xlabel('Category')
    ax2.set_ylabel('Value')
    ax2.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    return fig


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    
    print("Nord Color Palette for Matplotlib")
    print("=" * 50)
    print(f"\nMain palette ({len(NORD_PALETTE)} colors):")
    for i, color in enumerate(NORD_PALETTE, 1):
        print(f"  {i}. {color}")
    
    print("\nGenerating visualizations...")
    
    # Show all palettes
    for palette_name in ['default', 'blues', 'diverging', 'colorblind']:
        show_palette(palette_name)
    
    # Demo plot
    demo_plot()
    
    plt.show()
