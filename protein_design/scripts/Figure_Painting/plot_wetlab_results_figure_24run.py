from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
from PIL import Image, ImageDraw
from reportlab.pdfgen import canvas

from plot_wetlab_results_figure import (
    draw_text_centered,
    draw_text_right,
    find_font,
    panel_scale,
)
from plot_wetlab_results_figure_v2 import extract_glucose_timecourse
from figure_palette import GRID, INK, MUTED, PALETTE


REPO_ROOT = Path(__file__).resolve().parents[3]
FORMAL_MAPPING = (
    REPO_ROOT
    / "protein_design"
    / "tables"
    / "wetlab_runsheet"
    / "formal_24_run_result_mapping.csv"
)
DEFAULT_OUTPUT_DIR = REPO_ROOT / "protein_design" / "figures" / "wetlab_results_v2"
PANEL_WIDTH = 1040
PANEL_HEIGHT = 620
PLOT_X0 = 95
PLOT_Y0 = 120
PLOT_WIDTH = 905
PLOT_HEIGHT = 305

COLORS = {
    # Reuse colors already present in Fig. 2c, Fig. 2d and Fig. 4.
    "55 C +US": "#E67E22",
    "60 C +US": "#245F78",
    "55 C no US": "#9AA0A6",
    "55 C, 2 h": "#F5B43F",
    "55 C, 3 h": "#E67E22",
    "55 C, 4 h": "#C83E4D",
    "60 C, 2 h": "#245F78",
    "60 C, 4 h": "#7E6AA2",
    "Prediction": PALETTE["blue"],
    "Validation": PALETTE["green"],
    "Ink": INK,
    "Muted": MUTED,
    "Grid": GRID,
}


def _hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16)


def _rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    return "#{:02X}{:02X}{:02X}".format(*rgb)


def _interpolate_color(start: str, end: str, fraction: float) -> str:
    fraction = max(0.0, min(1.0, fraction))
    sr, sg, sb = _hex_to_rgb(start)
    er, eg, eb = _hex_to_rgb(end)
    return _rgb_to_hex(
        (
            round(sr + (er - sr) * fraction),
            round(sg + (eg - sg) * fraction),
            round(sb + (eb - sb) * fraction),
        )
    )


def reduction_color(value: float) -> str:
    """Sequential manuscript-palette color for IgG-binding reduction."""

    if value <= 50:
        return _interpolate_color(PALETTE["blue_light"], PALETTE["cyan"], value / 50)
    return _interpolate_color(PALETTE["cyan"], PALETTE["green_dark"], (value - 50) / 50)


def contrast_text_color(fill: str) -> str:
    r, g, b = _hex_to_rgb(fill)
    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return "white" if luminance < 128 else COLORS["Ink"]


def fonts(scale: int) -> dict[str, object]:
    return {
        "title": find_font(["arialbd.ttf", "Arial Bold.ttf", "DejaVuSans-Bold.ttf"], 37 * scale),
        "subtitle": find_font(["arialbd.ttf", "Arial Bold.ttf", "DejaVuSans-Bold.ttf"], 26 * scale),
        "axis_label": find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], 27 * scale),
        "tick": find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], 25 * scale),
        "small": find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], 23 * scale),
        "tiny": find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], 20 * scale),
        "micro": find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], 17 * scale),
    }


def results() -> pd.DataFrame:
    df = pd.read_csv(FORMAL_MAPPING)
    for column in ["temperature_C", "time_h", "reduction_pct_vs_untreated_N", "error_pct"]:
        df[column] = pd.to_numeric(df[column], errors="coerce")
    return df


def draw_axes(draw, x0, y0, width, height, font_set, ymin=0, ymax=100, ticks=None) -> None:
    ticks = ticks or [0, 25, 50, 75, 100]
    _, sy = panel_scale(x0, y0, width, height, 0, 1, ymin, ymax)
    for tick in ticks:
        y = sy(tick)
        draw.line([(x0, y), (x0 + width, y)], fill=COLORS["Grid"], width=2)
        draw_text_right(draw, (x0 - 10, y), str(tick), font_set["tick"], COLORS["Muted"])
    draw.line([(x0, y0 + height), (x0 + width, y0 + height)], fill=COLORS["Ink"], width=3)
    draw.line([(x0, y0), (x0, y0 + height)], fill=COLORS["Ink"], width=3)


def draw_error_bar(draw, x, y, error_height, scale, color=None) -> None:
    color = color or COLORS["Ink"]
    width = max(1, int(1.2 * scale))
    cap = 7 * scale
    draw.line([(x, y - error_height), (x, y + error_height)], fill=color, width=width)
    draw.line([(x - cap, y - error_height), (x + cap, y - error_height)], fill=color, width=width)
    draw.line([(x - cap, y + error_height), (x + cap, y + error_height)], fill=color, width=width)


def save_pdf_from_png(png_path: Path, pdf_path: Path) -> None:
    image = Image.open(png_path)
    page_width = image.width / 2
    page_height = image.height / 2
    pdf = canvas.Canvas(str(pdf_path), pagesize=(page_width, page_height))
    pdf.drawInlineImage(image, 0, 0, width=page_width, height=page_height)
    pdf.showPage()
    pdf.save()


def plot_panel_a(df: pd.DataFrame, output_dir: Path, scale: int = 2) -> list[Path]:
    width, height = PANEL_WIDTH * scale, PANEL_HEIGHT * scale
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    fs = fonts(scale)
    s = lambda value: value * scale

    x0, y0, w, h = s(PLOT_X0), s(PLOT_Y0), s(PLOT_WIDTH), s(PLOT_HEIGHT)
    draw_text_centered(draw, (x0 + w / 2, y0 - s(62)), "4 h hexose bridge", fs["title"], COLORS["Ink"])
    draw_axes(draw, x0, y0, w, h, fs)
    sx, sy = panel_scale(x0, y0, w, h, -0.6, 3.6, 0, 100)

    donors = ["lactose", "glucose", "galactose", "mannose"]
    labels = ["Lactose", "Glucose", "Galactose", "Mannose"]
    series = [
        ("55 C +US", 55, "+US", -42),
        ("60 C +US", 60, "+US", 0),
        ("55 C no US", 55, "no US", 42),
    ]
    bar_width = s(31)
    for donor_index, donor in enumerate(donors):
        for series_name, temp, ultrasound, offset in series:
            row = df[
                df["donor"].eq(donor)
                & df["temperature_C"].eq(temp)
                & df["time_h"].eq(4)
                & df["ultrasound"].eq(ultrasound)
            ].iloc[0]
            value = float(row["reduction_pct_vs_untreated_N"])
            error = float(row["error_pct"])
            x = sx(donor_index) + s(offset)
            y = sy(value)
            draw.rectangle([(x - bar_width / 2, y), (x + bar_width / 2, sy(0))], fill=COLORS[series_name])
            draw_error_bar(draw, x, y, abs(sy(value + error) - sy(value)), scale)
            label_y = min(y - s(18), sy(value + error) - s(15))
            draw_text_centered(draw, (x, label_y), f"{value:.1f}", fs["tiny"], COLORS["Muted"])
        draw_text_centered(draw, (sx(donor_index), sy(0) + s(45)), labels[donor_index], fs["small"], COLORS["Ink"])

    draw.text((x0 - s(72), y0 - s(45)), "Reduction (%)", font=fs["axis_label"], fill=COLORS["Ink"])
    draw_text_centered(draw, (x0 + w / 2, y0 + h + s(92)), "Donor", fs["axis_label"], COLORS["Ink"])
    legend_x, legend_y = x0 + w / 2 - s(230), y0 + h + s(145)
    for idx, (series_name, _, _, _) in enumerate(series):
        lx = legend_x + s(idx * 165)
        draw.rectangle([(lx, legend_y - s(11)), (lx + s(27), legend_y + s(11))], fill=COLORS[series_name])
        draw.text((lx + s(38), legend_y - s(15)), series_name, font=fs["small"], fill=COLORS["Ink"])

    png_path = output_dir / "Figure_3a_v2.png"
    pdf_path = output_dir / "Figure_3a_v2.pdf"
    image.save(png_path)
    save_pdf_from_png(png_path, pdf_path)
    return [png_path, pdf_path]


def plot_panel_b_grouped_bar(df: pd.DataFrame, output_dir: Path, scale: int = 2) -> list[Path]:
    width, height = PANEL_WIDTH * scale, PANEL_HEIGHT * scale
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    fs = fonts(scale)
    s = lambda value: value * scale

    x0, y0, w, h = s(75), s(PLOT_Y0), s(945), s(305)
    draw_text_centered(
        draw,
        (x0 + w / 2, y0 - s(62)),
        "Short-window anchors and process controls",
        fs["title"],
        COLORS["Ink"],
    )
    draw_axes(draw, x0, y0, w, h, fs)
    _, sy = panel_scale(x0, y0, w, h, 0, 1, 0, 100)

    blocks = [
        (
            "No-sugar controls",
            [
                ("R21", "", "55 C, 2 h", COLORS["55 C, 2 h"]),
                ("R22", "", "55 C, 3 h", COLORS["55 C, 3 h"]),
                ("R23", "", "55 C, 4 h", COLORS["55 C, 4 h"]),
                ("R24", "", "60 C, 4 h", COLORS["60 C, 4 h"]),
            ],
        ),
        (
            "Hexose anchors",
            [
                ("R13", "Lac.", "60 C, 2 h", COLORS["60 C, 2 h"]),
                ("R14", "Glc.", "60 C, 2 h", COLORS["60 C, 2 h"]),
                ("R15", "Lac.", "55 C, 3 h", COLORS["55 C, 3 h"]),
                ("R16", "Glc.", "55 C, 3 h", COLORS["55 C, 3 h"]),
            ],
        ),
        (
            "Pentose branch",
            [
                ("R17", "Ara.", "55 C, 2 h", COLORS["55 C, 2 h"]),
                ("R19", "Rib.", "55 C, 2 h", COLORS["55 C, 2 h"]),
                ("R18", "Ara.", "55 C, 3 h", COLORS["55 C, 3 h"]),
                ("R20", "Rib.", "55 C, 3 h", COLORS["55 C, 3 h"]),
            ],
        ),
    ]

    total_slots = sum(len(items) for _, items in blocks) + (len(blocks) - 1) * 0.95
    slot_w = w / total_slots
    bar_width = min(s(46), slot_w * 0.54)
    source_rows = []

    cursor = 0.0
    for block_index, (block_label, items) in enumerate(blocks):
        block_start = cursor
        for run_id, donor_label, condition_label, color in items:
            subset = df[df["run_id"].eq(run_id)]
            if subset.empty:
                raise ValueError(f"Missing run {run_id} for Fig. 3b")
            row = subset.iloc[0]
            value = float(row["reduction_pct_vs_untreated_N"])
            error = float(row["error_pct"])
            x = x0 + (cursor + 0.5) * slot_w
            y = sy(value)
            draw.rectangle(
                [(x - bar_width / 2, y), (x + bar_width / 2, sy(0))],
                fill=color,
            )
            draw_error_bar(
                draw,
                x,
                y,
                abs(sy(value + error) - sy(value)),
                scale,
                color=COLORS["Muted"],
            )
            draw_text_centered(draw, (x, y - s(17)), f"{value:.0f}", fs["micro"], COLORS["Muted"])
            if donor_label:
                draw_text_centered(draw, (x, sy(0) + s(28)), donor_label, fs["micro"], COLORS["Ink"])
                draw_text_centered(draw, (x, sy(0) + s(50)), condition_label.replace(" C", ""), fs["micro"], COLORS["Muted"])
            else:
                draw_text_centered(draw, (x, sy(0) + s(40)), condition_label.replace(" C", ""), fs["micro"], COLORS["Muted"])
            source_rows.append(
                {
                    "block": block_label,
                    "donor": "No sugar" if str(row["no_sugar_control"]).lower() == "yes" else str(row["donor"]).title(),
                    "condition": condition_label,
                    "run_id": row["run_id"],
                    "reduction_pct": value,
                    "error_pct": error,
                    "status": "available",
                }
            )
            cursor += 1.0

        block_center = x0 + (block_start + len(items) / 2) * slot_w
        draw_text_centered(draw, (block_center, sy(0) + s(86)), block_label, fs["small"], COLORS["Ink"])
        if block_index < len(blocks) - 1:
            divider_x = x0 + (cursor + 0.38) * slot_w
            draw.line(
                [(divider_x, y0 + s(12)), (divider_x, sy(0) + s(66))],
                fill=COLORS["Grid"],
                width=max(1, int(s(1.5))),
            )
            cursor += 0.95

    draw.text((x0 - s(72), y0 - s(45)), "Reduction (%)", font=fs["axis_label"], fill=COLORS["Ink"])
    legend_items = [
        ("55 C, 2 h", COLORS["55 C, 2 h"]),
        ("55 C, 3 h", COLORS["55 C, 3 h"]),
        ("55 C, 4 h", COLORS["55 C, 4 h"]),
        ("60 C, 2 h", COLORS["60 C, 2 h"]),
        ("60 C, 4 h", COLORS["60 C, 4 h"]),
    ]
    legend_x, legend_y = x0 + w / 2 - s(365), y0 + h + s(165)
    for idx, (series_name, color) in enumerate(legend_items):
        lx = legend_x + s(idx * 150)
        draw.rectangle([(lx, legend_y - s(10)), (lx + s(25), legend_y + s(10))], fill=color)
        draw.text((lx + s(36), legend_y - s(15)), series_name, font=fs["small"], fill=COLORS["Ink"])

    png_path = output_dir / "Figure_3b_v2.png"
    pdf_path = output_dir / "Figure_3b_v2.pdf"
    source_path = output_dir / "Figure_3b_v2_bar_source_data.csv"
    image.save(png_path)
    save_pdf_from_png(png_path, pdf_path)
    pd.DataFrame(source_rows).to_csv(source_path, index=False, encoding="utf-8-sig")
    return [png_path, pdf_path, source_path]

def plot_panel_b_matrix(df: pd.DataFrame, output_dir: Path, scale: int = 2) -> list[Path]:
    width, height = PANEL_WIDTH * scale, PANEL_HEIGHT * scale
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    fs = fonts(scale)
    s = lambda value: value * scale

    x0, y0 = s(190), s(120)
    cell_w, cell_h = s(148), s(58)
    gap = s(8)
    matrix_w = cell_w * 5 + gap * 4
    matrix_h = cell_h * 5 + gap * 4

    draw_text_centered(
        draw,
        (x0 + matrix_w / 2, y0 - s(62)),
        "Short-window run matrix",
        fs["title"],
        COLORS["Ink"],
    )

    donors = [
        ("none", "No sugar"),
        ("lactose", "Lactose"),
        ("glucose", "Glucose"),
        ("arabinose", "Arabinose"),
        ("ribose", "Ribose"),
    ]
    conditions = [
        (55, 2, "55 C, 2 h"),
        (55, 3, "55 C, 3 h"),
        (55, 4, "55 C, 4 h"),
        (60, 2, "60 C, 2 h"),
        (60, 4, "60 C, 4 h"),
    ]

    for col, (_, label) in enumerate(donors):
        cx = x0 + col * (cell_w + gap) + cell_w / 2
        draw_text_centered(draw, (cx, y0 - s(22)), label, fs["small"], COLORS["Ink"])
    draw_text_right(draw, (x0 - s(18), y0 - s(22)), "Condition", fs["small"], COLORS["Ink"])

    source_rows = []
    for row_index, (temp, time_h, condition_label) in enumerate(conditions):
        cy = y0 + row_index * (cell_h + gap) + cell_h / 2
        draw_text_right(draw, (x0 - s(18), cy), condition_label, fs["small"], COLORS["Ink"])
        for col, (donor, donor_label) in enumerate(donors):
            left = x0 + col * (cell_w + gap)
            top = y0 + row_index * (cell_h + gap)
            subset = df[
                df["donor"].eq(donor)
                & df["temperature_C"].eq(temp)
                & df["time_h"].eq(time_h)
                & df["ultrasound"].eq("+US")
            ]
            if subset.empty:
                draw.rounded_rectangle(
                    [(left, top), (left + cell_w, top + cell_h)],
                    radius=int(s(6)),
                    fill=PALETTE["grey_fill"],
                    outline=PALETTE["grid_blue"],
                    width=max(1, int(s(1))),
                )
                draw_text_centered(
                    draw,
                    (left + cell_w / 2, top + cell_h / 2),
                    "--",
                    fs["small"],
                    COLORS["Muted"],
                )
                source_rows.append(
                    {
                        "donor": "No sugar" if str(row["no_sugar_control"]).lower() == "yes" else str(row["donor"]).title(),
                        "condition": condition_label,
                        "run_id": None,
                        "reduction_pct": None,
                        "error_pct": None,
                        "status": "not in planned matrix",
                    }
                )
                continue

            record = subset.iloc[0]
            value = float(record["reduction_pct_vs_untreated_N"])
            error = float(record["error_pct"])
            fill = reduction_color(value)
            text_color = contrast_text_color(fill)
            draw.rounded_rectangle(
                [(left, top), (left + cell_w, top + cell_h)],
                radius=int(s(6)),
                fill=fill,
                outline="white",
                width=max(1, int(s(2))),
            )
            draw_text_centered(
                draw,
                (left + cell_w / 2, top + s(18)),
                str(record["run_id"]),
                fs["tiny"],
                text_color,
            )
            draw_text_centered(
                draw,
                (left + cell_w / 2, top + s(40)),
                f"{value:.1f} +/- {error:.1f}%",
                fs["micro"],
                text_color,
            )
            source_rows.append(
                {
                    "donor": "No sugar" if str(row["no_sugar_control"]).lower() == "yes" else str(row["donor"]).title(),
                    "condition": condition_label,
                    "run_id": record["run_id"],
                    "reduction_pct": value,
                    "error_pct": error,
                    "status": "available",
                }
            )

    draw_text_centered(
        draw,
        (x0 + matrix_w / 2, y0 + matrix_h + s(50)),
        "Donor / control",
        fs["axis_label"],
        COLORS["Ink"],
    )
    legend_x, legend_y = x0 + s(40), y0 + matrix_h + s(100)
    legend_w, legend_h = s(430), s(16)
    for idx in range(int(legend_w)):
        fraction = idx / max(1, legend_w - 1)
        color = reduction_color(fraction * 100)
        draw.line(
            [(legend_x + idx, legend_y), (legend_x + idx, legend_y + legend_h)],
            fill=color,
            width=1,
        )
    draw.rectangle(
        [(legend_x, legend_y), (legend_x + legend_w, legend_y + legend_h)],
        outline=PALETTE["grey_line"],
        width=max(1, int(s(1))),
    )
    for tick, label in [(0, "0"), (50, "50"), (100, "100")]:
        tx = legend_x + legend_w * tick / 100
        draw.line(
            [(tx, legend_y + legend_h), (tx, legend_y + legend_h + s(6))],
            fill=COLORS["Muted"],
            width=max(1, int(s(1))),
        )
        draw_text_centered(draw, (tx, legend_y + legend_h + s(22)), label, fs["tiny"], COLORS["Muted"])
    draw.text(
        (legend_x + legend_w + s(20), legend_y - s(4)),
        "IgG-binding reduction (%)",
        font=fs["tiny"],
        fill=COLORS["Ink"],
    )

    png_path = output_dir / "Figure_3b_v2.png"
    pdf_path = output_dir / "Figure_3b_v2.pdf"
    source_path = output_dir / "Figure_3b_v2_matrix_source_data.csv"
    image.save(png_path)
    save_pdf_from_png(png_path, pdf_path)
    pd.DataFrame(source_rows).to_csv(source_path, index=False, encoding="utf-8-sig")
    return [png_path, pdf_path, source_path]


def plot_panel_b(
    df: pd.DataFrame,
    output_dir: Path,
    scale: int = 2,
    style: str = "bar",
) -> list[Path]:
    if style == "bar":
        return plot_panel_b_grouped_bar(df, output_dir, scale=scale)
    return plot_panel_b_matrix(df, output_dir, scale=scale)


def plot_panel_c(output_dir: Path, scale: int = 2, left_style: str = "band") -> list[Path]:
    # Keep the locked evidence order: glucose is marginal-effect calibration;
    # ribose 60 C, 4 h is the pre-validation recommendation and validation.
    from plot_wetlab_results_figure_v2 import plot_panel_c as plot_panel_c_v2

    return plot_panel_c_v2(output_dir, scale=scale, left_style=left_style)


def make_composite_preview(output_dir: Path) -> Path:
    panel_a = Image.open(output_dir / "Figure_3a_v2.png").convert("RGB")
    panel_b = Image.open(output_dir / "Figure_3b_v2.png").convert("RGB")
    panel_c = Image.open(output_dir / "Figure_3c_v2.png").convert("RGB")
    top_width = panel_a.width + panel_b.width
    top_height = max(panel_a.height, panel_b.height)
    c_height = round(panel_c.height * top_width / panel_c.width)
    panel_c = panel_c.resize((top_width, c_height), Image.Resampling.LANCZOS)
    combined = Image.new("RGB", (top_width, top_height + c_height), "white")
    combined.paste(panel_a, (0, 0))
    combined.paste(panel_b, (panel_a.width, 0))
    combined.paste(panel_c, (0, top_height))
    path = output_dir / "Figure_3_v2_composite_preview.png"
    combined.save(path)
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description="Draw Fig. 3 using the complete 24-run matrix.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--panel-c-left-style", choices=["errorbar", "band"], default="band")
    parser.add_argument(
        "--panel-b-style",
        choices=["matrix", "bar"],
        default="bar",
        help="Render Fig. 3b as a clean grouped bar chart or condition matrix.",
    )
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    df = results()
    written = []
    written.extend(plot_panel_a(df, args.output_dir))
    written.extend(plot_panel_b(df, args.output_dir, style=args.panel_b_style))
    written.extend(plot_panel_c(args.output_dir, left_style=args.panel_c_left_style))
    written.append(make_composite_preview(args.output_dir))
    source_path = args.output_dir / "Figure_3_v2_source_data.csv"
    df.to_csv(source_path, index=False, encoding="utf-8-sig")
    written.append(source_path)

    for path in written:
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()

















