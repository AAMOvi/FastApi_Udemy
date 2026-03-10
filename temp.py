import matplotlib
matplotlib.use('Agg')  # non-GUI backend
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

# Figure size
fig, ax = plt.subplots(figsize=(16, 3))
ax.axis('off')

# Box size
box_width = 2
box_height = 0.3

# Box positions (x, y)
positions = {
    'F': (0, 0.5),
    'U': (4, 0.5),
    'G': (8, 0.5),
    "F'": (12, 0.5),
    'Head': (16, 0.5)
}

# Box labels
labels = {
    'F': "F\n(Decoder Features)",
    'U': "U\n(Uncertainty Map)",
    'G': "G\n(Spatial Gate)",
    "F'": "F'\n(Refined Features)",
    'Head': "Head\n(Segmentation Output)"
}

# Box colors
colors = {
    'F': '#8fbcd4',    # light blue
    'U': '#f7b267',    # light orange
    'G': '#90be6d',    # light green
    "F'": '#8fbcd4',   # light blue
    'Head': '#b197fc'  # light purple
}

# Draw boxes with rounded corners
for key, (x, y) in positions.items():
    box = FancyBboxPatch((x-box_width/2, y-box_height/2), box_width, box_height,
                         boxstyle="round,pad=0.02", facecolor=colors[key], 
                         edgecolor='black', linewidth=1.5)
    ax.add_patch(box)
    ax.text(x, y, labels[key], ha='center', va='center', fontsize=9, fontweight='bold')

# Draw arrows
arrow_style = dict(arrowstyle='-|>', mutation_scale=15, color='black', lw=2)
arrow_pairs = [('F','U'), ('U','G'), ('G',"F'"), ("F'",'Head')]

for start, end in arrow_pairs:
    x_start, y_start = positions[start]
    x_end, y_end = positions[end]
    # arrow from right edge of start box to left edge of end box
    arrow = FancyArrowPatch((x_start + box_width/2, y_start), 
                            (x_end - box_width/2, y_end), **arrow_style)
    ax.add_patch(arrow)

# Set axis limits
ax.set_xlim(-1, 17)
ax.set_ylim(0, 1)

plt.tight_layout()
plt.savefig("UGBM_schematic_colored.png", dpi=300)
print("UGBM schematic saved as 'UGBM_schematic_colored.png'")