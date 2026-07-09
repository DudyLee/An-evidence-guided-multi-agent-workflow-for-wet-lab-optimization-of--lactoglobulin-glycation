from pathlib import Path
from xml.sax.saxutils import escape

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


# Keep SVG output more stable/editable across repeated runs and Office/Visio import.
plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["svg.hashsalt"] = "netglycate-panel-d"
plt.rcParams["font.family"] = "Arial"


# =========================
# NetGlycate result data
# =========================
sequence_length = 162

# position, score, predicted_yes
data = [
    (8, -0.916, False),
    (14, 0.804, True),
    (47, 0.925, True),
    (60, -0.942, False),
    (69, -0.907, False),
    (70, 0.818, True),
    (75, -0.832, False),
    (77, -0.862, False),
    (83, -0.707, False),
    (91, -0.905, False),
    (100, 0.803, True),
    (101, 0.801, True),
    (135, -0.923, False),
    (138, -0.960, False),
    (141, -0.858, False),
]

pos_yes_x = [x for x, _, y in data if y]
pos_yes_y = [s for _, s, y in data if y]

neg_x = [x for x, _, y in data if not y]
neg_y = [s for _, s, y in data if not y]


def write_visio_safe_svg(save_path: Path) -> None:
    """Write a simple SVG using only basic primitives for stable Visio import."""
    width = 900
    height = 380
    margin_left = 78
    margin_right = 28
    margin_top = 62
    margin_bottom = 72
    plot_w = width - margin_left - margin_right
    plot_h = height - margin_top - margin_bottom
    y_min = -1.1
    y_max = 1.1

    def x_scale(x: float) -> float:
        return margin_left + (x / (sequence_length + 5)) * plot_w

    def y_scale(y: float) -> float:
        return margin_top + ((y_max - y) / (y_max - y_min)) * plot_h

    def line(x1, y1, x2, y2, color, width_px=1.0):
        return (
            f'<line x1="{x1:.3f}" y1="{y1:.3f}" x2="{x2:.3f}" y2="{y2:.3f}" '
            f'stroke="{color}" stroke-width="{width_px}" stroke-linecap="round"/>'
        )

    def circle(cx, cy, r, color):
        return f'<circle cx="{cx:.3f}" cy="{cy:.3f}" r="{r:.3f}" fill="{color}"/>'

    def text(x, y, value, size=12, anchor="middle", weight="400", color="#202124"):
        return (
            f'<text x="{x:.3f}" y="{y:.3f}" text-anchor="{anchor}" '
            f'font-family="Arial, Helvetica, sans-serif" font-size="{size}" '
            f'font-weight="{weight}" fill="{color}">{escape(str(value))}</text>'
        )

    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        text(
            width / 2,
            30,
            "NetGlycate-predicted glycation-prone lysine sites in beta-LG",
            size=18,
            weight="700",
        ),
    ]

    # Horizontal grid and threshold.
    for tick in [-1.0, -0.5, 0.0, 0.5, 1.0]:
        y = y_scale(tick)
        is_zero = tick == 0
        parts.append(
            line(
                margin_left,
                y,
                width - margin_right,
                y,
                "#7a7f85" if is_zero else "#e3e1dc",
                1.2 if is_zero else 0.8,
            )
        )
        label = "0" if tick == 0 else f"{tick:.1f}"
        parts.append(text(margin_left - 12, y + 4, label, size=12, anchor="end", color="#4f555b"))

    # Stems and points.
    for position, score, predicted in data:
        x = x_scale(position)
        y = y_scale(score)
        y0 = y_scale(0)
        color = "#e67e22" if predicted else "#9aa0a6"
        parts.append(line(x, y0, x, y, color, 2.2 if predicted else 1.5))
        parts.append(circle(x, y, 4.4 if predicted else 3.4, color))

    # Labels for predicted sites. Offset K100/K101 to prevent overlap.
    label_offsets = {100: (-10, -14), 101: (14, -14)}
    for position, score, predicted in data:
        if not predicted:
            continue
        dx, dy = label_offsets.get(position, (0, -10))
        parts.append(text(x_scale(position) + dx, y_scale(score) + dy, f"K{position}", size=12))

    # Axes and ticks.
    x_axis_y = y_scale(y_min)
    parts.append(line(margin_left, x_axis_y, width - margin_right, x_axis_y, "#202124", 1.2))
    parts.append(line(margin_left, margin_top, margin_left, x_axis_y, "#202124", 1.2))
    for tick in [0, 20, 40, 60, 80, 100, 120, 140, 160]:
        x = x_scale(tick)
        parts.append(line(x, x_axis_y, x, x_axis_y + 5, "#202124", 1.0))
        parts.append(text(x, x_axis_y + 22, tick, size=12))

    parts.append(text(margin_left + plot_w / 2, height - 18, "Sequence position", size=14))
    # Avoid rotated text because Visio sometimes imports SVG transforms poorly.
    parts.append(text(18, margin_top - 12, "NetGlycate score", size=13, anchor="start"))

    # Legend.
    legend_x = 94
    legend_y = 312
    parts.append(line(legend_x, legend_y, legend_x + 28, legend_y, "#9aa0a6", 1.5))
    parts.append(circle(legend_x + 14, legend_y, 3.8, "#9aa0a6"))
    parts.append(text(legend_x + 42, legend_y + 4, "Other lysine residues", size=12, anchor="start"))

    parts.append(line(legend_x + 215, legend_y, legend_x + 243, legend_y, "#e67e22", 2.2))
    parts.append(circle(legend_x + 229, legend_y, 4.4, "#e67e22"))
    parts.append(
        text(
            legend_x + 257,
            legend_y + 4,
            "Predicted glycation-prone sites (YES)",
            size=12,
            anchor="start",
        )
    )

    parts.append(line(legend_x + 545, legend_y, legend_x + 573, legend_y, "#7a7f85", 1.2))
    parts.append(text(legend_x + 587, legend_y + 4, "Threshold = 0", size=12, anchor="start"))

    parts.append("</svg>")
    save_path.write_text("\n".join(parts), encoding="utf-8")


def main() -> None:
    save_dir = Path(__file__).resolve().parents[1] / "figures" / "evidence_stats"
    save_dir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(9, 3.8), dpi=300)

    # Threshold line
    ax.axhline(0, linewidth=1.0, color="gray", alpha=0.8)

    # All non-YES lysines
    for x, y in zip(neg_x, neg_y):
        ax.vlines(x, 0, y, linewidth=1.5, color="#9aa0a6", alpha=0.9)
        ax.scatter(x, y, s=24, color="#9aa0a6", zorder=3)

    # Predicted YES lysines
    for x, y in zip(pos_yes_x, pos_yes_y):
        ax.vlines(x, 0, y, linewidth=2.2, color="#e67e22", alpha=0.95)
        ax.scatter(x, y, s=34, color="#e67e22", zorder=4)

    # Annotate top predicted sites
    for x, y in zip(pos_yes_x, pos_yes_y):
        ax.text(x, y + 0.06, f"K{x}", ha="center", va="bottom", fontsize=9)

    # Axis settings
    ax.set_xlim(0, sequence_length + 5)
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlabel("Sequence position", fontsize=10)
    ax.set_ylabel("NetGlycate score", fontsize=10)
    ax.set_title(
        "NetGlycate-predicted glycation-prone lysine sites in beta-LG",
        fontsize=11,
    )

    # Ticks
    ax.set_xticks([0, 20, 40, 60, 80, 100, 120, 140, 160])
    ax.tick_params(axis="both", labelsize=9)

    # Simplify spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    legend_handles = [
        Line2D(
            [0],
            [0],
            color="#9aa0a6",
            marker="o",
            linestyle="-",
            linewidth=1.5,
            markersize=5,
            label="Other lysine residues",
        ),
        Line2D(
            [0],
            [0],
            color="#e67e22",
            marker="o",
            linestyle="-",
            linewidth=2.2,
            markersize=5,
            label="Predicted glycation-prone sites (YES)",
        ),
        Line2D(
            [0],
            [0],
            color="gray",
            linestyle="-",
            linewidth=1.0,
            label="Threshold = 0",
        ),
    ]
    ax.legend(handles=legend_handles, frameon=False, fontsize=8, loc="lower left")

    fig.tight_layout()
    fig.savefig(save_dir / "netglycate_panel_d.png", bbox_inches="tight", dpi=300)
    fig.savefig(save_dir / "netglycate_panel_d.pdf", bbox_inches="tight")
    # Matplotlib SVGs can import poorly in Visio because they use clipPath,
    # transforms, and marker collections. Keep this as a reference export.
    fig.savefig(save_dir / "netglycate_panel_d_matplotlib.svg", bbox_inches="tight")

    # Use this SVG for Visio/Office workflows.
    write_visio_safe_svg(save_dir / "netglycate_panel_d.svg")
    plt.show()


if __name__ == "__main__":
    main()
