from __future__ import annotations

import argparse
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.pdfgen import canvas


REPO_ROOT = Path(__file__).resolve().parents[3]
RAW_WORKBOOK_DIR = os.environ.get("GLYCATION_RAW_WORKBOOK_DIR")
RESULT_ROOT = Path(RAW_WORKBOOK_DIR) if RAW_WORKBOOK_DIR else None
DEFAULT_MAPPING = RESULT_ROOT / "filled_run_mapping_results_v3.xlsx" if RESULT_ROOT else None
DEFAULT_TIMECOURSE = (
    RESULT_ROOT / "2026.3.19-\u5355\u7cd6\u4e8c\u7cd6-\u7cd6\u57fa\u5316-\u6570\u636e\u6574\u7406.xlsx"
    if RESULT_ROOT
    else None
)
DEFAULT_OUTPUT_DIR = REPO_ROOT / "protein_design" / "figures" / "wetlab_results"

DONOR_LABELS = {
    "none": "No sugar",
    "lactose": "Lactose",
    "glucose": "Glucose",
    "galactose": "Galactose",
    "mannose": "Mannose",
    "arabinose": "Arabinose",
    "ribose": "Ribose",
}

CHINESE_DONOR_LABELS = {
    "\u6838\u7cd6": "Ribose",
    "\u6728\u7cd6": "Xylose",
    "\u963f\u62c9\u4f2f\u7cd6": "Arabinose",
    "\u8461\u8404\u7cd6": "Glucose",
    "\u679c\u7cd6": "Fructose",
    "\u534a\u4e73\u7cd6": "Galactose",
    "\u4e73\u7cd6": "Lactose",
    "\u9ea6\u82bd\u7cd6": "Maltose",
    "\u7ea4\u7ef4\u4e8c\u7cd6": "Cellobiose",
}

COLORS = {
    "55 C": "#49C2D9",
    "60 C": "#143E7D",
    "+US": "#4E7D3A",
    "-US": "#A8ADB5",
    "No sugar": "#A8ADB5",
    "Prediction": "#2F69B1",
    "Validation": "#4E7D3A",
    "Ribose": "#4E7D3A",
}


@dataclass
class BridgeRow:
    donor: str
    temp: int
    reduction_pct: float
    error_pct: float | None


@dataclass
class ThreeHourRow:
    donor: str
    ultrasound: str
    reduction_pct: float
    error_pct: float | None


@dataclass
class TimeCourseRow:
    donor: str
    time_h: float
    ultrasound: str
    reduction_pct: float
    error_pct: float


def find_font(candidates: Iterable[str], size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    font_dirs = [
        Path("C:/Windows/Fonts"),
        Path("/usr/share/fonts/truetype/dejavu"),
        Path("/usr/share/fonts/truetype/liberation2"),
    ]
    for directory in font_dirs:
        for name in candidates:
            path = directory / name
            if path.exists():
                return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont | ImageFont.ImageFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0], box[3] - box[1]


def draw_text_centered(
    draw: ImageDraw.ImageDraw,
    xy: tuple[float, float],
    text: str,
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
    fill: str,
) -> None:
    w, h = text_size(draw, text, font)
    draw.text((xy[0] - w / 2, xy[1] - h / 2), text, font=font, fill=fill)


def draw_text_right(
    draw: ImageDraw.ImageDraw,
    xy: tuple[float, float],
    text: str,
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
    fill: str,
) -> None:
    w, h = text_size(draw, text, font)
    draw.text((xy[0] - w, xy[1] - h / 2), text, font=font, fill=fill)


def read_table(path: Path, sheet: str, header_label: str) -> pd.DataFrame:
    raw = pd.read_excel(path, sheet_name=sheet, header=None)
    header_row = None
    for idx, row in raw.iterrows():
        values = [str(v) for v in row.tolist() if not pd.isna(v)]
        if header_label in values:
            header_row = idx
            break
    if header_row is None:
        raise ValueError(f"Could not find header {header_label!r} in {path.name}:{sheet}")
    return pd.read_excel(path, sheet_name=sheet, header=header_row)


def extract_bridge(mapping_path: Path) -> list[BridgeRow]:
    df = read_table(mapping_path, "Source_Extracts", "source_file")
    df = df[df["source_file"].astype(str).str.contains("2026.3.20", na=False)]
    keep = df[df["source_donor"].isin(["none", "lactose", "glucose", "galactose", "mannose"])].copy()
    keep = keep[keep["source_temp_C"].isin([55, 60])]
    rows: list[BridgeRow] = []
    for _, row in keep.iterrows():
        reduction = float(row["source_reduction_pct_vs_source_N"]) * 100
        value_mean = float(row["source_value_mean"])
        error = float(row["source_error"])
        baseline = value_mean / (1 - float(row["source_reduction_pct_vs_source_N"]))
        rows.append(
            BridgeRow(
                donor=DONOR_LABELS[str(row["source_donor"])],
                temp=int(row["source_temp_C"]),
                reduction_pct=reduction,
                error_pct=error / baseline * 100,
            )
        )
    return rows


def extract_three_hour(mapping_path: Path) -> list[ThreeHourRow]:
    df = read_table(mapping_path, "Source_Extracts", "source_file")
    df = df[df["source_file"].astype(str).str.contains("2026.3.19", na=False)]
    df = df[df["source_time_h"].eq(3)]
    df = df[df["source_donor"].isin(["lactose", "glucose", "arabinose", "ribose"])]
    rows: list[ThreeHourRow] = []
    for _, row in df.iterrows():
        reduction_fraction = float(row["source_reduction_pct_vs_source_N"])
        value_mean = float(row["source_value_mean"])
        error = float(row["source_error"])
        baseline = value_mean / (1 - reduction_fraction)
        rows.append(
            ThreeHourRow(
                donor=DONOR_LABELS[str(row["source_donor"])],
                ultrasound=str(row["source_ultrasound"]),
                reduction_pct=reduction_fraction * 100,
                error_pct=error / baseline * 100,
            )
        )
    return rows


def extract_timecourse(path: Path) -> tuple[list[TimeCourseRow], tuple[float, float], float, float]:
    df = pd.read_excel(path, sheet_name="Sheet1", header=None)
    baseline_mean = float(df.iloc[1, 1])
    rows: list[TimeCourseRow] = []
    for idx in range(2, len(df)):
        label = df.iloc[idx, 0]
        if pd.isna(label) or "-" not in str(label):
            continue
        donor_cn, time_text = str(label).split("-", 1)
        donor = CHINESE_DONOR_LABELS.get(donor_cn)
        if donor is None:
            continue
        time_h = float(time_text.lower().replace("h", "").strip())
        for ultrasound, value_col, error_col in [("-US", 1, 2), ("+US", 4, 5)]:
            value = df.iloc[idx, value_col]
            error = df.iloc[idx, error_col]
            if pd.isna(value) or pd.isna(error):
                continue
            mean = float(value)
            sd = float(error)
            rows.append(
                TimeCourseRow(
                    donor=donor,
                    time_h=time_h,
                    ultrasound=ultrasound,
                    reduction_pct=(1 - mean / baseline_mean) * 100,
                    error_pct=sd / baseline_mean * 100,
                )
            )

    # Right-side validation entry in the workbook: label, raw value, reduction, reduction sd.
    validation_mean_pct = float(df.iloc[2, 12]) * 100
    validation_sd_pct = float(df.iloc[2, 13]) * 100
    predicted_center = 86.0
    predicted_range = (82.0, 93.0)
    return rows, predicted_range, predicted_center, validation_sd_pct if validation_sd_pct else 1.7


def panel_scale(
    x0: float, y0: float, width: float, height: float, xmin: float, xmax: float, ymin: float, ymax: float
):
    def sx(x: float) -> float:
        return x0 + ((x - xmin) / (xmax - xmin)) * width

    def sy(y: float) -> float:
        return y0 + ((ymax - y) / (ymax - ymin)) * height

    return sx, sy


def draw_axes_png(
    draw: ImageDraw.ImageDraw,
    x0: float,
    y0: float,
    width: float,
    height: float,
    yticks: list[float],
    ylabels: list[str],
    tick_font,
    ink: str,
    muted: str,
    grid: str,
) -> None:
    for tick, label in zip(yticks, ylabels):
        _, sy = panel_scale(x0, y0, width, height, 0, 1, min(yticks), max(yticks))
        y = sy(tick)
        draw.line([(x0, y), (x0 + width, y)], fill=grid, width=2)
        draw_text_right(draw, (x0 - 10, y), label, tick_font, muted)
    draw.line([(x0, y0 + height), (x0 + width, y0 + height)], fill=ink, width=3)
    draw.line([(x0, y0), (x0, y0 + height)], fill=ink, width=3)


def draw_wetlab_png(
    bridge: list[BridgeRow],
    three_hour: list[ThreeHourRow],
    timecourse: list[TimeCourseRow],
    predicted_range: tuple[float, float],
    predicted_center: float,
    validation_sd: float,
    output_path: Path,
    scale: int = 2,
) -> None:
    width, height = 1800 * scale, 1320 * scale
    image = Image.new("RGB", (width, height), "#ffffff")
    draw = ImageDraw.Draw(image)

    def s(v: float) -> float:
        return v * scale

    title_font = find_font(["arialbd.ttf", "Arial Bold.ttf", "DejaVuSans-Bold.ttf"], 30 * scale)
    label_font = find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], 24 * scale)
    tick_font = find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], 20 * scale)
    small_font = find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], 19 * scale)
    bold_font = find_font(["arialbd.ttf", "Arial Bold.ttf", "DejaVuSans-Bold.ttf"], 22 * scale)
    panel_font = find_font(["arialbd.ttf", "Arial Bold.ttf", "DejaVuSans-Bold.ttf"], 34 * scale)

    ink = "#202124"
    muted = "#5f6368"
    grid = "#DDE7F5"

    # Panel geometry.
    pa = (s(115), s(125), s(720), s(360))
    pb = (s(1010), s(125), s(650), s(360))
    pc = (s(115), s(690), s(1545), s(360))

    def panel_title(x, y, letter, text):
        draw.text((x - s(58), y - s(60)), letter, font=panel_font, fill=ink)
        draw.text((x, y - s(54)), text, font=title_font, fill=ink)

    # Panel a.
    x0, y0, w, h = pa
    panel_title(x0, y0, "a", "Matched 4 h bridge screen")
    draw_axes_png(draw, x0, y0, w, h, [0, 25, 50, 75, 100], ["0", "25", "50", "75", "100"], tick_font, ink, muted, grid)
    sx, sy = panel_scale(x0, y0, w, h, -0.7, 4.7, 0, 100)
    donor_order = ["No sugar", "Lactose", "Glucose", "Galactose", "Mannose"]
    bridge_map = {(row.donor, row.temp): row for row in bridge}
    bar_w = s(26)
    for i, donor in enumerate(donor_order):
        for j, temp in enumerate([55, 60]):
            row = bridge_map.get((donor, temp))
            if not row:
                continue
            x = sx(i) + (j - 0.5) * bar_w * 1.2
            y = sy(row.reduction_pct)
            color = COLORS[f"{temp} C"]
            draw.rectangle([(x - bar_w / 2, y), (x + bar_w / 2, sy(0))], fill=color)
            if row.error_pct:
                ey = abs(sy(row.reduction_pct + row.error_pct) - sy(row.reduction_pct))
                draw.line([(x, y - ey), (x, y + ey)], fill=ink, width=max(1, int(s(1.2))))
                draw.line([(x - s(7), y - ey), (x + s(7), y - ey)], fill=ink, width=max(1, int(s(1.2))))
                draw.line([(x - s(7), y + ey), (x + s(7), y + ey)], fill=ink, width=max(1, int(s(1.2))))
        draw_text_centered(draw, (sx(i), sy(0) + s(45)), donor, small_font, ink)
    draw.text((x0 - s(82), y0 - s(25)), "Reduction (%)", font=label_font, fill=ink)
    draw_text_centered(draw, (x0 + w / 2, y0 + h + s(98)), "Condition", label_font, ink)
    # Legend.
    lx, ly = x0 + s(420), y0 + s(28)
    for j, temp in enumerate([55, 60]):
        draw.rectangle([(lx + s(j * 150), ly - s(13)), (lx + s(j * 150 + 32), ly + s(13))], fill=COLORS[f"{temp} C"])
        draw.text((lx + s(j * 150 + 42), ly - s(13)), f"{temp} C", font=small_font, fill=ink)

    # Panel b.
    x0, y0, w, h = pb
    panel_title(x0, y0, "b", "3 h short-window donor screen")
    draw_axes_png(draw, x0, y0, w, h, [0, 25, 50, 75, 100], ["0", "25", "50", "75", "100"], tick_font, ink, muted, grid)
    sx, sy = panel_scale(x0, y0, w, h, -0.6, 3.6, 0, 100)
    donor_order_b = ["Lactose", "Glucose", "Arabinose", "Ribose"]
    three_map = {(row.donor, row.ultrasound): row for row in three_hour}
    for i, donor in enumerate(donor_order_b):
        for j, us in enumerate(["-US", "+US"]):
            row = three_map.get((donor, us))
            if not row:
                continue
            x = sx(i) + (j - 0.5) * bar_w * 1.25
            y = sy(row.reduction_pct)
            color = COLORS[us]
            draw.rectangle([(x - bar_w / 2, y), (x + bar_w / 2, sy(0))], fill=color)
            if row.error_pct:
                ey = abs(sy(row.reduction_pct + row.error_pct) - sy(row.reduction_pct))
                draw.line([(x, y - ey), (x, y + ey)], fill=ink, width=max(1, int(s(1.2))))
                draw.line([(x - s(7), y - ey), (x + s(7), y - ey)], fill=ink, width=max(1, int(s(1.2))))
        draw_text_centered(draw, (sx(i), sy(0) + s(45)), donor, small_font, ink)
    draw.text((x0 - s(82), y0 - s(25)), "Reduction (%)", font=label_font, fill=ink)
    lx, ly = x0 + s(350), y0 + s(28)
    for j, us in enumerate(["-US", "+US"]):
        draw.rectangle([(lx + s(j * 138), ly - s(13)), (lx + s(j * 138 + 32), ly + s(13))], fill=COLORS[us])
        draw.text((lx + s(j * 138 + 42), ly - s(13)), us, font=small_font, fill=ink)

    # Panel c.
    x0, y0, w, h = pc
    panel_title(x0, y0, "c", "Ribose validation and local time course")
    ymin, ymax = 60, 96
    sx, sy = panel_scale(x0, y0, w, h, 2.2, 24.8, ymin, ymax)
    for tick in [60, 70, 80, 90]:
        y = sy(tick)
        draw.line([(x0, y), (x0 + w, y)], fill=grid, width=2)
        draw_text_right(draw, (x0 - s(10), y), str(tick), tick_font, muted)
    draw.line([(x0, y0 + h), (x0 + w, y0 + h)], fill=ink, width=3)
    draw.line([(x0, y0), (x0, y0 + h)], fill=ink, width=3)

    ribose = [row for row in timecourse if row.donor == "Ribose" and row.time_h in [3, 6, 9, 12, 18, 24]]
    for us in ["-US", "+US"]:
        subset = sorted([row for row in ribose if row.ultrasound == us], key=lambda r: r.time_h)
        color = COLORS[us]
        points = [(sx(row.time_h), sy(row.reduction_pct)) for row in subset]
        if len(points) > 1:
            draw.line(points, fill=color, width=int(s(4)))
        for row, (x, y) in zip(subset, points):
            r = s(7)
            draw.ellipse([(x - r, y - r), (x + r, y + r)], fill=color)
            ey = abs(sy(row.reduction_pct + row.error_pct) - sy(row.reduction_pct))
            draw.line([(x, y - ey), (x, y + ey)], fill=color, width=max(1, int(s(1.2))))

    # Prediction range and observed validation.
    x_pred = sx(4)
    draw.line([(x_pred - s(18), sy(predicted_range[0])), (x_pred - s(18), sy(predicted_range[1]))], fill=COLORS["Prediction"], width=int(s(5)))
    draw.line([(x_pred - s(32), sy(predicted_range[0])), (x_pred - s(4), sy(predicted_range[0]))], fill=COLORS["Prediction"], width=int(s(3)))
    draw.line([(x_pred - s(32), sy(predicted_range[1])), (x_pred - s(4), sy(predicted_range[1]))], fill=COLORS["Prediction"], width=int(s(3)))
    draw.ellipse([(x_pred - s(25), sy(predicted_center) - s(6)), (x_pred - s(11), sy(predicted_center) + s(6))], fill=COLORS["Prediction"])

    validation_mean = 85.6
    x_val = sx(4.25)
    y_val = sy(validation_mean)
    r = s(10)
    draw.polygon([(x_val, y_val - r), (x_val + r, y_val), (x_val, y_val + r), (x_val - r, y_val)], fill=COLORS["Validation"])
    ey = abs(sy(validation_mean + validation_sd) - sy(validation_mean))
    draw.line([(x_val, y_val - ey), (x_val, y_val + ey)], fill=COLORS["Validation"], width=int(s(2)))
    draw.text((x_val + s(18), y_val - s(18)), "Observed 85.6%", font=small_font, fill=COLORS["Validation"])

    for tick in [3, 4, 6, 9, 12, 18, 24]:
        x = sx(tick)
        draw.line([(x, y0 + h), (x, y0 + h + s(10))], fill=ink, width=int(s(2)))
        draw_text_centered(draw, (x, y0 + h + s(40)), str(tick), tick_font, ink)
    draw.text((x0 - s(82), y0 - s(25)), "Reduction (%)", font=label_font, fill=ink)
    draw_text_centered(draw, (x0 + w / 2, y0 + h + s(94)), "Reaction time (h)", label_font, ink)

    lx, ly = x0 + s(735), y0 - s(38)
    legend_items = [("-US", COLORS["-US"]), ("+US", COLORS["+US"]), ("Prediction", COLORS["Prediction"]), ("Validation", COLORS["Validation"])]
    for idx, (label, color) in enumerate(legend_items):
        px = lx + s(idx * 180)
        draw.line([(px, ly), (px + s(38), ly)], fill=color, width=int(s(4)))
        draw.text((px + s(48), ly - s(13)), label, font=small_font, fill=ink)

    image.save(output_path)


def draw_wetlab_pdf(
    bridge: list[BridgeRow],
    three_hour: list[ThreeHourRow],
    timecourse: list[TimeCourseRow],
    predicted_range: tuple[float, float],
    predicted_center: float,
    validation_sd: float,
    output_path: Path,
) -> None:
    # Keep a high-resolution PDF companion for direct manuscript import.
    png_tmp = output_path.with_suffix(".preview.png")
    draw_wetlab_png(bridge, three_hour, timecourse, predicted_range, predicted_center, validation_sd, png_tmp, scale=2)
    img = Image.open(png_tmp)
    pdf = canvas.Canvas(str(output_path), pagesize=(900, 660))
    pdf.drawInlineImage(img, 0, 0, width=900, height=660)
    pdf.showPage()
    pdf.save()
    png_tmp.unlink(missing_ok=True)


def _panel_fonts(scale: int) -> dict[str, ImageFont.FreeTypeFont | ImageFont.ImageFont]:
    return {
        "title": find_font(["arialbd.ttf", "Arial Bold.ttf", "DejaVuSans-Bold.ttf"], 30 * scale),
        "label": find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], 24 * scale),
        "tick": find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], 20 * scale),
        "small": find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], 19 * scale),
    }


def _draw_bar_error(
    draw: ImageDraw.ImageDraw,
    x: float,
    y: float,
    ey: float,
    scale: int,
    ink: str,
) -> None:
    def s(v: float) -> float:
        return v * scale

    width = max(1, int(s(1.2)))
    draw.line([(x, y - ey), (x, y + ey)], fill=ink, width=width)
    draw.line([(x - s(8), y - ey), (x + s(8), y - ey)], fill=ink, width=width)
    draw.line([(x - s(8), y + ey), (x + s(8), y + ey)], fill=ink, width=width)


def draw_panel_a_png(bridge: list[BridgeRow], output_path: Path, scale: int = 2) -> None:
    width, height = 900 * scale, 540 * scale
    image = Image.new("RGB", (width, height), "#ffffff")
    draw = ImageDraw.Draw(image)

    def s(v: float) -> float:
        return v * scale

    fonts = _panel_fonts(scale)
    ink = "#202124"
    muted = "#5f6368"
    grid = "#DDE7F5"
    x0, y0, w, h = s(95), s(125), s(780), s(305)

    draw.text((x0, y0 - s(62)), "4 h bridge screen", font=fonts["title"], fill=ink)
    draw_axes_png(draw, x0, y0, w, h, [0, 25, 50, 75, 100], ["0", "25", "50", "75", "100"], fonts["tick"], ink, muted, grid)

    sx, sy = panel_scale(x0, y0, w, h, -0.6, 4.6, 0, 100)
    donor_order = ["No sugar", "Lactose", "Glucose", "Galactose", "Mannose"]
    bridge_map = {(row.donor, row.temp): row for row in bridge}
    bar_w = s(38)
    for i, donor in enumerate(donor_order):
        for j, temp in enumerate([55, 60]):
            row = bridge_map.get((donor, temp))
            if not row:
                continue
            x = sx(i) + (j - 0.5) * bar_w * 1.22
            y = sy(row.reduction_pct)
            draw.rectangle([(x - bar_w / 2, y), (x + bar_w / 2, sy(0))], fill=COLORS[f"{temp} C"])
            if row.error_pct:
                ey = abs(sy(row.reduction_pct + row.error_pct) - sy(row.reduction_pct))
                _draw_bar_error(draw, x, y, ey, scale, ink)
        draw_text_centered(draw, (sx(i), sy(0) + s(44)), donor, fonts["small"], ink)

    draw.text((x0 - s(82), y0 - s(26)), "Reduction (%)", font=fonts["label"], fill=ink)
    draw_text_centered(draw, (x0 + w / 2, y0 + h + s(92)), "Condition", fonts["label"], ink)

    lx, ly = x0 + w - s(300), y0 - s(38)
    for j, temp in enumerate([55, 60]):
        draw.rectangle([(lx + s(j * 150), ly - s(13)), (lx + s(j * 150 + 34), ly + s(13))], fill=COLORS[f"{temp} C"])
        draw.text((lx + s(j * 150 + 44), ly - s(13)), f"{temp} C", font=fonts["small"], fill=ink)

    image.save(output_path)


def draw_panel_b_png(three_hour: list[ThreeHourRow], output_path: Path, scale: int = 2) -> None:
    width, height = 900 * scale, 540 * scale
    image = Image.new("RGB", (width, height), "#ffffff")
    draw = ImageDraw.Draw(image)

    def s(v: float) -> float:
        return v * scale

    fonts = _panel_fonts(scale)
    ink = "#202124"
    muted = "#5f6368"
    grid = "#DDE7F5"
    x0, y0, w, h = s(95), s(125), s(780), s(305)

    draw.text((x0, y0 - s(62)), "3 h donor screen", font=fonts["title"], fill=ink)
    draw_axes_png(draw, x0, y0, w, h, [0, 25, 50, 75, 100], ["0", "25", "50", "75", "100"], fonts["tick"], ink, muted, grid)

    sx, sy = panel_scale(x0, y0, w, h, -0.5, 3.5, 0, 100)
    donor_order = ["Lactose", "Glucose", "Arabinose", "Ribose"]
    three_map = {(row.donor, row.ultrasound): row for row in three_hour}
    bar_w = s(40)
    for i, donor in enumerate(donor_order):
        for j, us in enumerate(["-US", "+US"]):
            row = three_map.get((donor, us))
            if not row:
                continue
            x = sx(i) + (j - 0.5) * bar_w * 1.22
            y = sy(row.reduction_pct)
            draw.rectangle([(x - bar_w / 2, y), (x + bar_w / 2, sy(0))], fill=COLORS[us])
            if row.error_pct:
                ey = abs(sy(row.reduction_pct + row.error_pct) - sy(row.reduction_pct))
                _draw_bar_error(draw, x, y, ey, scale, ink)
        draw_text_centered(draw, (sx(i), sy(0) + s(44)), donor, fonts["small"], ink)

    draw.text((x0 - s(82), y0 - s(26)), "Reduction (%)", font=fonts["label"], fill=ink)

    lx, ly = x0 + w - s(250), y0 - s(38)
    for j, us in enumerate(["-US", "+US"]):
        draw.rectangle([(lx + s(j * 135), ly - s(13)), (lx + s(j * 135 + 34), ly + s(13))], fill=COLORS[us])
        draw.text((lx + s(j * 135 + 44), ly - s(13)), us, font=fonts["small"], fill=ink)

    image.save(output_path)


def draw_panel_c_png(
    timecourse: list[TimeCourseRow],
    predicted_range: tuple[float, float],
    predicted_center: float,
    validation_sd: float,
    output_path: Path,
    scale: int = 2,
) -> None:
    width, height = 1600 * scale, 560 * scale
    image = Image.new("RGB", (width, height), "#ffffff")
    draw = ImageDraw.Draw(image)

    def s(v: float) -> float:
        return v * scale

    fonts = _panel_fonts(scale)
    ink = "#202124"
    muted = "#5f6368"
    grid = "#DDE7F5"
    x0, y0, w, h = s(110), s(120), s(1410), s(315)
    ymin, ymax = 60, 96

    draw.text((x0, y0 - s(62)), "Ribose validation and local time course", font=fonts["title"], fill=ink)
    sx, sy = panel_scale(x0, y0, w, h, 2.2, 24.8, ymin, ymax)
    for tick in [60, 70, 80, 90]:
        y = sy(tick)
        draw.line([(x0, y), (x0 + w, y)], fill=grid, width=2)
        draw_text_right(draw, (x0 - s(10), y), str(tick), fonts["tick"], muted)
    draw.line([(x0, y0 + h), (x0 + w, y0 + h)], fill=ink, width=3)
    draw.line([(x0, y0), (x0, y0 + h)], fill=ink, width=3)

    ribose = [row for row in timecourse if row.donor == "Ribose" and row.time_h in [3, 6, 9, 12, 18, 24]]
    for us in ["-US", "+US"]:
        subset = sorted([row for row in ribose if row.ultrasound == us], key=lambda r: r.time_h)
        color = COLORS[us]
        points = [(sx(row.time_h), sy(row.reduction_pct)) for row in subset]
        if len(points) > 1:
            draw.line(points, fill=color, width=int(s(4)))
        for row, (x, y) in zip(subset, points):
            r = s(7)
            draw.ellipse([(x - r, y - r), (x + r, y + r)], fill=color)
            ey = abs(sy(row.reduction_pct + row.error_pct) - sy(row.reduction_pct))
            draw.line([(x, y - ey), (x, y + ey)], fill=color, width=max(1, int(s(1.2))))

    x_pred = sx(4)
    draw.line([(x_pred - s(18), sy(predicted_range[0])), (x_pred - s(18), sy(predicted_range[1]))], fill=COLORS["Prediction"], width=int(s(5)))
    draw.line([(x_pred - s(32), sy(predicted_range[0])), (x_pred - s(4), sy(predicted_range[0]))], fill=COLORS["Prediction"], width=int(s(3)))
    draw.line([(x_pred - s(32), sy(predicted_range[1])), (x_pred - s(4), sy(predicted_range[1]))], fill=COLORS["Prediction"], width=int(s(3)))
    draw.ellipse([(x_pred - s(25), sy(predicted_center) - s(6)), (x_pred - s(11), sy(predicted_center) + s(6))], fill=COLORS["Prediction"])

    validation_mean = 85.6
    x_val = sx(4.25)
    y_val = sy(validation_mean)
    r = s(10)
    draw.polygon([(x_val, y_val - r), (x_val + r, y_val), (x_val, y_val + r), (x_val - r, y_val)], fill=COLORS["Validation"])
    ey = abs(sy(validation_mean + validation_sd) - sy(validation_mean))
    draw.line([(x_val, y_val - ey), (x_val, y_val + ey)], fill=COLORS["Validation"], width=int(s(2)))
    draw.text((x_val + s(18), y_val - s(18)), "Observed 85.6%", font=fonts["small"], fill=COLORS["Validation"])

    for tick in [3, 4, 6, 9, 12, 18, 24]:
        x = sx(tick)
        draw.line([(x, y0 + h), (x, y0 + h + s(10))], fill=ink, width=int(s(2)))
        draw_text_centered(draw, (x, y0 + h + s(40)), str(tick), fonts["tick"], ink)

    draw.text((x0 - s(82), y0 - s(26)), "Reduction (%)", font=fonts["label"], fill=ink)
    draw_text_centered(draw, (x0 + w / 2, y0 + h + s(92)), "Reaction time (h)", fonts["label"], ink)

    lx, ly = x0 + s(700), y0 - s(38)
    legend_items = [("-US", COLORS["-US"]), ("+US", COLORS["+US"]), ("Prediction", COLORS["Prediction"]), ("Validation", COLORS["Validation"])]
    for idx, (label, color) in enumerate(legend_items):
        px = lx + s(idx * 175)
        draw.line([(px, ly), (px + s(38), ly)], fill=color, width=int(s(4)))
        draw.text((px + s(48), ly - s(13)), label, font=fonts["small"], fill=ink)

    image.save(output_path)


def draw_png_pdf(png_path: Path, pdf_path: Path) -> None:
    img = Image.open(png_path)
    page_width = img.width / 2
    page_height = img.height / 2
    pdf = canvas.Canvas(str(pdf_path), pagesize=(page_width, page_height))
    pdf.drawInlineImage(img, 0, 0, width=page_width, height=page_height)
    pdf.showPage()
    pdf.save()


def draw_separate_panels(
    bridge: list[BridgeRow],
    three_hour: list[ThreeHourRow],
    timecourse: list[TimeCourseRow],
    predicted_range: tuple[float, float],
    predicted_center: float,
    validation_sd: float,
    output_dir: Path,
    prefix: str,
) -> list[Path]:
    panel_pngs = [
        output_dir / f"{prefix}_panel_a.png",
        output_dir / f"{prefix}_panel_b.png",
        output_dir / f"{prefix}_panel_c.png",
    ]
    draw_panel_a_png(bridge, panel_pngs[0])
    draw_panel_b_png(three_hour, panel_pngs[1])
    draw_panel_c_png(timecourse, predicted_range, predicted_center, validation_sd, panel_pngs[2])

    written: list[Path] = []
    for png_path in panel_pngs:
        pdf_path = png_path.with_suffix(".pdf")
        draw_png_pdf(png_path, pdf_path)
        written.extend([png_path, pdf_path])
    return written


def main() -> None:
    parser = argparse.ArgumentParser(description="Draw wet-lab refinement and validation results figure.")
    parser.add_argument("--mapping", type=Path, default=DEFAULT_MAPPING)
    parser.add_argument("--timecourse", type=Path, default=DEFAULT_TIMECOURSE)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--basename", default="wetlab_results_figure")
    args = parser.parse_args()
    if args.mapping is None or args.timecourse is None:
        parser.error(
            "This legacy plotting script requires the original raw wet-lab workbooks. "
            "Set GLYCATION_RAW_WORKBOOK_DIR or pass --mapping and --timecourse explicitly."
        )

    bridge = extract_bridge(args.mapping)
    three_hour = extract_three_hour(args.mapping)
    timecourse, predicted_range, predicted_center, validation_sd = extract_timecourse(args.timecourse)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    png_path = args.output_dir / f"{args.basename}.png"
    pdf_path = args.output_dir / f"{args.basename}.pdf"
    csv_path = args.output_dir / f"{args.basename}_source_data.csv"

    draw_wetlab_png(bridge, three_hour, timecourse, predicted_range, predicted_center, validation_sd, png_path)
    draw_wetlab_pdf(bridge, three_hour, timecourse, predicted_range, predicted_center, validation_sd, pdf_path)
    panel_paths = draw_separate_panels(
        bridge=bridge,
        three_hour=three_hour,
        timecourse=timecourse,
        predicted_range=predicted_range,
        predicted_center=predicted_center,
        validation_sd=validation_sd,
        output_dir=args.output_dir,
        prefix=args.basename.replace("_figure", ""),
    )

    rows = []
    for row in bridge:
        rows.append({"panel": "a", **row.__dict__})
    for row in three_hour:
        rows.append({"panel": "b", **row.__dict__})
    for row in timecourse:
        if row.donor == "Ribose":
            rows.append({"panel": "c", **row.__dict__})
    rows.append({"panel": "c", "donor": "Ribose", "time_h": 4, "ultrasound": "+US", "reduction_pct": 85.6, "error_pct": validation_sd, "role": "observed_validation"})
    rows.append({"panel": "c", "donor": "Ribose", "time_h": 4, "ultrasound": "+US", "reduction_pct": predicted_center, "error_pct": None, "role": f"prediction_range_{predicted_range[0]}_{predicted_range[1]}"})
    pd.DataFrame(rows).to_csv(csv_path, index=False)

    print(f"Wrote {png_path}")
    print(f"Wrote {pdf_path}")
    for panel_path in panel_paths:
        print(f"Wrote {panel_path}")
    print(f"Wrote {csv_path}")
    print(f"Bridge rows: {len(bridge)}; 3h rows: {len(three_hour)}; timecourse rows: {len(timecourse)}")


if __name__ == "__main__":
    main()

