from __future__ import annotations

import argparse
import os
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
from figure_palette import GRID, INK, MUTED, PALETTE, blend


REPO_ROOT = Path(__file__).resolve().parents[3]
RESULT_ROOT = Path(
    os.environ.get("GLYCATION_RAW_WORKBOOK_DIR", REPO_ROOT / "data" / "raw_wetlab_workbooks")
)
FORMAL_MAPPING = (
    REPO_ROOT
    / "protein_design"
    / "tables"
    / "wetlab_runsheet"
    / "formal_17_run_result_mapping.csv"
)
SOURCE_MAPPING = RESULT_ROOT / "filled_run_mapping_results_v3.xlsx"
TIMECOURSE_WORKBOOK = (
    RESULT_ROOT / "2026.3.19-\u5355\u7cd6\u4e8c\u7cd6-\u7cd6\u57fa\u5316-\u6570\u636e\u6574\u7406.xlsx"
)
TWO_HOUR_WORKBOOK = RESULT_ROOT / "2026.1.21 \u03b2-Lg-\u7cd6\u57fa\u5316-\u81f4\u654f.xlsx"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "protein_design" / "figures" / "wetlab_results_v2"

COLORS = {
    "55 C": PALETTE["cyan"],
    "60 C": PALETTE["blue_dark"],
    "60 C, 2 h": PALETTE["blue"],
    "55 C, 2 h": blend(PALETTE["cyan"], amount=0.34),
    "55 C, 3 h": PALETTE["cyan"],
    "55 C -US": PALETTE["grey_line"],
    "55 C +US": PALETTE["green"],
    "Prediction": PALETTE["blue"],
    "Validation": PALETTE["green"],
    "GlucoseLine": "#E67E22",
    "Band": blend("#F7A24F", amount=0.64),
    "BandEdge": "#F7A24F",
    "Guide": blend("#E67E22", amount=0.68),
    "Ink": INK,
    "Muted": MUTED,
    "Grid": GRID,
}


def fonts(scale: int) -> dict[str, object]:
    return {
        "title": find_font(["arialbd.ttf", "Arial Bold.ttf", "DejaVuSans-Bold.ttf"], 34 * scale),
        "subtitle": find_font(["arialbd.ttf", "Arial Bold.ttf", "DejaVuSans-Bold.ttf"], 24 * scale),
        "axis_label": find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], 24 * scale),
        "tick": find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], 23 * scale),
        "small": find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], 21 * scale),
        "tiny": find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], 18 * scale),
    }


def read_table(path: Path, sheet: str, header_label: str) -> pd.DataFrame:
    raw = pd.read_excel(path, sheet_name=sheet, header=None)
    for idx, row in raw.iterrows():
        values = [str(value) for value in row.tolist() if not pd.isna(value)]
        if header_label in values:
            return pd.read_excel(path, sheet_name=sheet, header=idx)
    raise ValueError(f"Could not find header {header_label!r} in {path.name}:{sheet}")


def source_error_lookup() -> dict[tuple[str, int, float, str], float]:
    source = read_table(SOURCE_MAPPING, "Source_Extracts", "source_file")
    lookup: dict[tuple[str, int, float, str], float] = {}
    for _, row in source.iterrows():
        source_file = str(row["source_file"])
        donor = str(row["source_donor"])
        time_h = float(row["source_time_h"])
        ultrasound = str(row["source_ultrasound"])
        reduction = float(row["source_reduction_pct_vs_source_N"])
        mean = float(row["source_value_mean"])
        error = float(row["source_error"])
        baseline = mean / (1 - reduction)
        if "2026.3.20" in source_file:
            temp = int(row["source_temp_C"])
        elif "2026.3.19" in source_file:
            temp = 55
        else:
            continue
        lookup[(donor, temp, time_h, ultrasound)] = error / baseline * 100

    two_hour = pd.read_excel(TWO_HOUR_WORKBOOK, sheet_name="\u6570\u636e\u6574\u7406", header=None)
    baseline = float(two_hour.iloc[4, 1])
    rows = {
        ("arabinose", 55, 2.0, "+US"): 21,
        ("glucose", 60, 2.0, "+US"): 25,
        ("lactose", 60, 2.0, "+US"): 29,
    }
    for key, row_idx in rows.items():
        lookup[key] = float(two_hour.iloc[row_idx, 6]) / baseline * 100
    return lookup


def formal_results() -> pd.DataFrame:
    df = pd.read_csv(FORMAL_MAPPING)
    df["temperature_C"] = pd.to_numeric(df["temperature_C"])
    df["time_h"] = pd.to_numeric(df["time_h"])
    df["reduction_pct_vs_untreated_N"] = pd.to_numeric(
        df["reduction_pct_vs_untreated_N"], errors="coerce"
    )
    errors = source_error_lookup()
    df["error_pct"] = [
        errors.get(
            (
                str(row.donor),
                int(row.temperature_C),
                float(row.time_h),
                str(row.ultrasound),
            )
        )
        for row in df.itertuples()
    ]
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
    width, height = 900 * scale, 620 * scale
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    fs = fonts(scale)

    def s(value: float) -> float:
        return value * scale

    x0, y0, w, h = s(95), s(120), s(780), s(305)
    draw_text_centered(
        draw,
        (x0 + w / 2, y0 - s(62)),
        "Matched 4 h bridge",
        fs["title"],
        COLORS["Ink"],
    )
    draw_axes(draw, x0, y0, w, h, fs)
    sx, sy = panel_scale(x0, y0, w, h, -0.6, 4.6, 0, 100)

    donors = ["none", "lactose", "glucose", "galactose", "mannose"]
    labels = ["No sugar", "Lactose", "Glucose", "Galactose", "Mannose"]
    selected = df[df["run_id"].isin([f"R{i:02d}" for i in range(1, 9)] + ["R16", "R17"])]
    bar_width = s(36)
    for donor_index, donor in enumerate(donors):
        for temp_index, temp in enumerate([55, 60]):
            row = selected[
                selected["donor"].eq(donor) & selected["temperature_C"].eq(temp)
            ].iloc[0]
            value = float(row["reduction_pct_vs_untreated_N"])
            error = float(row["error_pct"])
            x = sx(donor_index) + (temp_index - 0.5) * bar_width * 1.22
            y = sy(value)
            draw.rectangle(
                [(x - bar_width / 2, y), (x + bar_width / 2, sy(0))],
                fill=COLORS[f"{temp} C"],
            )
            draw_error_bar(draw, x, y, abs(sy(value + error) - sy(value)), scale)
        draw_text_centered(draw, (sx(donor_index), sy(0) + s(45)), labels[donor_index], fs["small"], COLORS["Ink"])

    draw.text((x0 - s(72), y0 - s(45)), "Reduction (%)", font=fs["axis_label"], fill=COLORS["Ink"])
    draw_text_centered(
        draw,
        (x0 + w / 2, y0 + h + s(92)),
        "Condition",
        fs["axis_label"],
        COLORS["Ink"],
    )

    legend_x, legend_y = x0 + w / 2 - s(135), y0 + h + s(145)
    for idx, temp in enumerate([55, 60]):
        lx = legend_x + s(idx * 150)
        draw.rectangle([(lx, legend_y - s(13)), (lx + s(34), legend_y + s(13))], fill=COLORS[f"{temp} C"])
        draw.text((lx + s(44), legend_y - s(13)), f"{temp} C", font=fs["small"], fill=COLORS["Ink"])

    png_path = output_dir / "Figure_3a_v2.png"
    pdf_path = output_dir / "Figure_3a_v2.pdf"
    image.save(png_path)
    save_pdf_from_png(png_path, pdf_path)
    return [png_path, pdf_path]


def plot_panel_b(df: pd.DataFrame, output_dir: Path, scale: int = 2) -> list[Path]:
    width, height = 900 * scale, 620 * scale
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    fs = fonts(scale)

    def s(value: float) -> float:
        return value * scale

    x0, y0, w, h = s(95), s(120), s(780), s(305)
    draw_text_centered(
        draw,
        (x0 + w / 2, y0 - s(62)),
        "Run-sheet anchors",
        fs["title"],
        COLORS["Ink"],
    )
    draw_axes(draw, x0, y0, w, h, fs)
    sx, sy = panel_scale(x0, y0, w, h, -0.5, 3.5, 0, 100)

    donors = ["lactose", "glucose", "arabinose", "ribose"]
    labels = ["Lactose", "Glucose", "Arabinose", "Ribose"]
    run_lookup = {
        ("lactose", "60 C, 2 h"): "R09",
        ("lactose", "55 C, 3 h"): "R11",
        ("glucose", "60 C, 2 h"): "R10",
        ("glucose", "55 C, 3 h"): "R12",
        ("arabinose", "55 C, 2 h"): "R13",
        ("arabinose", "55 C, 3 h"): "R14",
        ("ribose", "55 C, 3 h"): "R15",
    }
    conditions = ["60 C, 2 h", "55 C, 2 h", "55 C, 3 h"]
    offsets = {"60 C, 2 h": -s(38), "55 C, 2 h": 0, "55 C, 3 h": s(38)}
    bar_width = s(32)

    for donor_index, donor in enumerate(donors):
        for condition in conditions:
            run_id = run_lookup.get((donor, condition))
            if run_id is None:
                continue
            row = df[df["run_id"].eq(run_id)].iloc[0]
            value = float(row["reduction_pct_vs_untreated_N"])
            error = float(row["error_pct"])
            x = sx(donor_index) + offsets[condition]
            y = sy(value)
            draw.rectangle(
                [(x - bar_width / 2, y), (x + bar_width / 2, sy(0))],
                fill=COLORS[condition],
            )
            draw_error_bar(draw, x, y, abs(sy(value + error) - sy(value)), scale)
            draw_text_centered(draw, (x, y - s(18)), run_id, fs["tiny"], COLORS["Muted"])
        draw_text_centered(draw, (sx(donor_index), sy(0) + s(45)), labels[donor_index], fs["small"], COLORS["Ink"])

    draw.text((x0 - s(72), y0 - s(45)), "Reduction (%)", font=fs["axis_label"], fill=COLORS["Ink"])
    draw_text_centered(
        draw,
        (x0 + w / 2, y0 + h + s(92)),
        "Donor",
        fs["axis_label"],
        COLORS["Ink"],
    )

    legend_x, legend_y = x0 + w / 2 - s(220), y0 + h + s(145)
    legend_spacing = [0, 145, 290]
    for idx, condition in enumerate(conditions):
        lx = legend_x + s(legend_spacing[idx])
        draw.rectangle([(lx, legend_y - s(11)), (lx + s(27), legend_y + s(11))], fill=COLORS[condition])
        draw.text((lx + s(34), legend_y - s(11)), condition, font=fs["tiny"], fill=COLORS["Ink"])

    png_path = output_dir / "Figure_3b_v2.png"
    pdf_path = output_dir / "Figure_3b_v2.pdf"
    image.save(png_path)
    save_pdf_from_png(png_path, pdf_path)
    return [png_path, pdf_path]


def extract_glucose_timecourse() -> tuple[pd.DataFrame, float]:
    raw = pd.read_excel(TIMECOURSE_WORKBOOK, sheet_name="Sheet1", header=None)
    baseline = float(raw.iloc[1, 1])
    rows = []
    for idx in range(2, len(raw)):
        label = raw.iloc[idx, 0]
        if pd.isna(label) or not str(label).startswith("\u8461\u8404\u7cd6-"):
            continue
        time_h = float(str(label).split("-", 1)[1].lower().replace("h", "").strip())
        mean = raw.iloc[idx, 4]
        error = raw.iloc[idx, 5]
        if pd.isna(mean) or pd.isna(error):
            continue
        rows.append(
            {
                "time_h": time_h,
                "reduction_pct": (1 - float(mean) / baseline) * 100,
                "error_pct": float(error) / baseline * 100,
            }
        )
    validation_sd = float(raw.iloc[2, 13]) * 100
    return pd.DataFrame(rows), validation_sd


def plot_panel_c(
    output_dir: Path,
    scale: int = 2,
    left_style: str = "errorbar",
) -> list[Path]:
    width, height = 1600 * scale, 680 * scale
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    fs = fonts(scale)
    right_title_font = find_font(
        ["arialbd.ttf", "Arial Bold.ttf", "DejaVuSans-Bold.ttf"],
        28 * scale,
    )
    right_value_font = find_font(
        ["arialbd.ttf", "Arial Bold.ttf", "DejaVuSans-Bold.ttf"],
        24 * scale,
    )
    right_label_font = find_font(
        ["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"],
        21 * scale,
    )
    rate_sup_font = find_font(
        ["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"],
        16 * scale,
    )

    def s(value: float) -> float:
        return value * scale

    def draw_rate_label(center: tuple[float, float], value: float) -> None:
        base = f"+{value:.2f} pp h"
        superscript = "-1"
        base_box = draw.textbbox((0, 0), base, font=fs["tiny"])
        sup_box = draw.textbbox((0, 0), superscript, font=rate_sup_font)
        base_width = base_box[2] - base_box[0]
        base_height = base_box[3] - base_box[1]
        sup_width = sup_box[2] - sup_box[0]
        total_width = base_width + sup_width + s(1)
        x = center[0] - total_width / 2
        y = center[1] - base_height / 2
        draw.text((x, y), base, font=fs["tiny"], fill=COLORS["Muted"])
        draw.text(
            (x + base_width + s(1), y - s(5)),
            superscript,
            font=rate_sup_font,
            fill=COLORS["Muted"],
        )

    x0, y0, w, h = s(100), s(135), s(900), s(330)
    rx0, rw = s(1120), s(390)
    draw_text_centered(
        draw,
        (width / 2, y0 - s(83)),
        "Marginal-effect evidence and final validation",
        fs["title"],
        COLORS["Ink"],
    )
    draw_text_centered(
        draw,
        (x0 + w / 2, y0 - s(35)),
        "Glucose time course (55 \u00b0C, +US)",
        fs["subtitle"],
        COLORS["Ink"],
    )
    draw_text_centered(
        draw,
        (rx0 + rw / 2, y0 - s(35)),
        "Ribose recommendation (60 \u00b0C, 4 h)",
        right_title_font,
        COLORS["Ink"],
    )

    draw_axes(draw, x0, y0, w, h, fs, ymin=65, ymax=100, ticks=[70, 80, 90, 100])
    sx, sy = panel_scale(x0, y0, w, h, 2.2, 24.8, 65, 100)
    timecourse, validation_sd = extract_glucose_timecourse()
    timecourse = timecourse.sort_values("time_h")
    points = [
        (sx(float(row.time_h)), sy(float(row.reduction_pct)))
        for row in timecourse.itertuples()
    ]
    upper_points = [
        (
            sx(float(row.time_h)),
            sy(float(row.reduction_pct + row.error_pct)),
        )
        for row in timecourse.itertuples()
    ]
    lower_points = [
        (
            sx(float(row.time_h)),
            sy(float(row.reduction_pct - row.error_pct)),
        )
        for row in timecourse.itertuples()
    ]
    if left_style == "band":
        draw.polygon(
            upper_points + list(reversed(lower_points)),
            fill=COLORS["Band"],
        )
        draw.line(
            upper_points,
            fill=COLORS["BandEdge"],
            width=max(1, int(s(3.5))),
        )
        draw.line(
            lower_points,
            fill=COLORS["BandEdge"],
            width=max(1, int(s(3.5))),
        )
    draw.line(points, fill=COLORS["GlucoseLine"], width=int(s(4)))
    for row, (x, y) in zip(timecourse.itertuples(), points):
        if left_style == "errorbar":
            radius = s(7)
            draw.ellipse(
                [(x - radius, y - radius), (x + radius, y + radius)],
                fill=COLORS["GlucoseLine"],
            )
        if left_style == "errorbar":
            error_height = abs(
                sy(float(row.reduction_pct + row.error_pct))
                - sy(float(row.reduction_pct))
            )
            draw_error_bar(draw, x, y, error_height, scale, COLORS["GlucoseLine"])
        draw_text_centered(
            draw,
            (x, y - s(21)),
            f"{row.reduction_pct:.1f}",
            fs["tiny"],
            COLORS["Muted"],
        )

    rows = list(timecourse.itertuples())
    for first, second in zip(rows, rows[1:]):
        gain_per_hour = (
            float(second.reduction_pct) - float(first.reduction_pct)
        ) / (float(second.time_h) - float(first.time_h))
        mid_x = (sx(float(first.time_h)) + sx(float(second.time_h))) / 2
        mid_y = min(
            sy(float(first.reduction_pct)),
            sy(float(second.reduction_pct)),
        ) - s(34)
        draw_rate_label((mid_x, mid_y), gain_per_hour)

    for tick in [3, 6, 9, 12, 18, 24]:
        x = sx(tick)
        draw.line([(x, y0 + h), (x, y0 + h + s(10))], fill=COLORS["Ink"], width=int(s(2)))
        draw_text_centered(draw, (x, y0 + h + s(40)), str(tick), fs["tick"], COLORS["Ink"])
    draw.text(
        (x0 - s(72), y0 - s(45)),
        "Reduction (%)",
        font=fs["axis_label"],
        fill=COLORS["Ink"],
    )
    draw_text_centered(
        draw,
        (x0 + w / 2, y0 + h + s(92)),
        "Reaction time (h)",
        fs["axis_label"],
        COLORS["Ink"],
    )

    _, rsy = panel_scale(rx0, y0, rw, h, 0, 1, 0, 100)
    for tick in [0, 25, 50, 75, 100]:
        y = rsy(tick)
        draw.line([(rx0, y), (rx0 + rw, y)], fill=COLORS["Grid"], width=2)
        draw_text_right(
            draw,
            (rx0 - s(9), y),
            str(tick),
            right_label_font,
            COLORS["Muted"],
        )
    draw.line(
        [(rx0, y0 + h), (rx0 + rw, y0 + h)],
        fill=COLORS["Ink"],
        width=3,
    )
    draw.line([(rx0, y0), (rx0, y0 + h)], fill=COLORS["Ink"], width=3)
    draw.line(
        [(x0 + w + s(55), y0 - s(10)), (x0 + w + s(55), y0 + h + s(15))],
        fill=COLORS["Grid"],
        width=max(2, int(s(1))),
    )

    prediction_center = 86.0
    prediction_low, prediction_high = 82.0, 93.0
    x_prediction = rx0 + rw * 0.30
    x_validation = rx0 + rw * 0.72
    y_prediction = rsy(prediction_center)
    y_validation = rsy(85.6)
    baseline_y = rsy(0)
    bar_width = s(105)
    draw.rectangle(
        [
            (x_prediction - bar_width / 2, y_prediction),
            (x_prediction + bar_width / 2, baseline_y),
        ],
        fill=COLORS["Prediction"],
    )
    draw.rectangle(
        [
            (x_validation - bar_width / 2, y_validation),
            (x_validation + bar_width / 2, baseline_y),
        ],
        fill=COLORS["Validation"],
    )

    # Prediction interval is asymmetric around the central estimate.
    prediction_top = rsy(prediction_high)
    prediction_bottom = rsy(prediction_low)
    cap = s(17)
    draw.line(
        [(x_prediction, prediction_top), (x_prediction, prediction_bottom)],
        fill=COLORS["Ink"],
        width=max(2, int(s(1.5))),
    )
    draw.line(
        [(x_prediction - cap, prediction_top), (x_prediction + cap, prediction_top)],
        fill=COLORS["Ink"],
        width=max(2, int(s(1.5))),
    )
    draw.line(
        [(x_prediction - cap, prediction_bottom), (x_prediction + cap, prediction_bottom)],
        fill=COLORS["Ink"],
        width=max(2, int(s(1.5))),
    )

    validation_top = rsy(85.6 + validation_sd)
    validation_bottom = rsy(85.6 - validation_sd)
    draw.line(
        [(x_validation, validation_top), (x_validation, validation_bottom)],
        fill=COLORS["Ink"],
        width=max(2, int(s(1.5))),
    )
    draw.line(
        [(x_validation - cap, validation_top), (x_validation + cap, validation_top)],
        fill=COLORS["Ink"],
        width=max(2, int(s(1.5))),
    )
    draw.line(
        [(x_validation - cap, validation_bottom), (x_validation + cap, validation_bottom)],
        fill=COLORS["Ink"],
        width=max(2, int(s(1.5))),
    )

    draw_text_centered(
        draw,
        (x_prediction, prediction_top - s(23)),
        "86.0% (82-93%)",
        right_value_font,
        COLORS["Prediction"],
    )
    draw_text_centered(
        draw,
        (x_validation, validation_top - s(23)),
        "85.6 \u00b1 1.7%",
        right_value_font,
        COLORS["Validation"],
    )
    draw_text_centered(
        draw,
        (rx0 + rw / 2, y0 + h + s(70)),
        "\u0394 = -0.4 pp",
        right_label_font,
        COLORS["Muted"],
    )
    draw_text_centered(
        draw,
        (x_prediction, y0 + h + s(42)),
        "Predicted",
        right_label_font,
        COLORS["Ink"],
    )
    draw_text_centered(
        draw,
        (x_validation, y0 + h + s(42)),
        "Observed",
        right_label_font,
        COLORS["Ink"],
    )

    legend_x, legend_y = x0 + w / 2 - s(105), y0 + h + s(150)
    draw.line(
        [(legend_x, legend_y), (legend_x + s(34), legend_y)],
        fill=COLORS["GlucoseLine"],
        width=int(s(4)),
    )
    draw.text(
        (legend_x + s(48), legend_y - s(17)),
        (
            "Mean reduction and error range"
            if left_style == "band"
            else "Glucose marginal evidence"
        ),
        font=fs["small"],
        fill=COLORS["Ink"],
    )

    png_path = output_dir / "Figure_3c_v2.png"
    pdf_path = output_dir / "Figure_3c_v2.pdf"
    source_path = output_dir / "Figure_3c_v2_source_data.csv"
    source_rows = timecourse.copy()
    source_rows["series"] = "glucose_55C_plusUS_marginal_evidence"
    source_rows["condition"] = "glucose, 55 C, +US"
    validation_rows = pd.DataFrame(
        [
            {
                "time_h": 4.0,
                "reduction_pct": prediction_center,
                "error_pct": None,
                "series": "agent_prediction",
                "condition": "ribose, 60 C, +US",
                "range_low": prediction_low,
                "range_high": prediction_high,
            },
            {
                "time_h": 4.0,
                "reduction_pct": 85.6,
                "error_pct": validation_sd,
                "series": "wetlab_validation",
                "condition": "ribose, 60 C, +US",
                "range_low": None,
                "range_high": None,
            },
        ]
    )
    pd.concat([source_rows, validation_rows], ignore_index=True).to_csv(
        source_path,
        index=False,
        encoding="utf-8-sig",
    )
    image.save(png_path)
    save_pdf_from_png(png_path, pdf_path)
    return [png_path, pdf_path, source_path]


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
    parser = argparse.ArgumentParser(description="Draw an alternative condition-aware Fig. 3.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument(
        "--panel-c-left-style",
        choices=["errorbar", "band"],
        default="errorbar",
        help="Render the glucose time course using error bars or a mean/error band.",
    )
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    results = formal_results()
    written = []
    written.extend(plot_panel_a(results, args.output_dir))
    written.extend(plot_panel_b(results, args.output_dir))
    written.extend(
        plot_panel_c(
            args.output_dir,
            left_style=args.panel_c_left_style,
        )
    )
    written.append(make_composite_preview(args.output_dir))
    source_path = args.output_dir / "Figure_3_v2_source_data.csv"
    results.to_csv(source_path, index=False, encoding="utf-8-sig")
    written.append(source_path)

    for path in written:
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()












