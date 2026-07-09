from __future__ import annotations

import argparse
import csv
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

from plot_wetlab_results_figure import find_font
from figure_palette import GRID, INK, MUTED, PALETTE, WHITE, blend


REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_DATA = (
    REPO_ROOT
    / "protein_design"
    / "tables"
    / "glycation_results_organized"
    / "long_timecourse.csv"
)
DEFAULT_VALIDATION = (
    REPO_ROOT
    / "protein_design"
    / "tables"
    / "glycation_results_organized"
    / "ribose_validation.csv"
)
DEFAULT_OUT = REPO_ROOT / "protein_design" / "figures" / "supplementary_wetlab_landscape_options"

DONORS = ["ribose", "xylose", "arabinose", "glucose", "fructose", "galactose", "lactose", "maltose", "cellobiose"]
TIMES = [3, 6, 9, 12, 18, 24]

FONT_REGULAR = Path("C:/Windows/Fonts/arial.ttf")
FONT_BOLD = Path("C:/Windows/Fonts/arialbd.ttf")

MANUSCRIPT_BAR_COLORS = {
    "no US": "#9AA0A6",
    "+US": "#E67E22",
    "validation": "#C85E62",
}


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    path = FONT_BOLD if bold and FONT_BOLD.exists() else FONT_REGULAR
    if path.exists():
        return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def manuscript_fonts(scale: float = 1.0) -> dict[str, ImageFont.FreeTypeFont]:
    def size(value: int) -> int:
        return int(round(value * scale))

    return {
        "title": find_font(["arialbd.ttf", "Arial Bold.ttf", "DejaVuSans-Bold.ttf"], size(37)),
        "subtitle": find_font(["arialbd.ttf", "Arial Bold.ttf", "DejaVuSans-Bold.ttf"], size(26)),
        "axis_label": find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], size(27)),
        "tick": find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], size(25)),
        "small": find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], size(23)),
        "tiny": find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], size(20)),
        "micro": find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], size(17)),
    }


def draw_text_font(
    draw: ImageDraw.ImageDraw,
    xy: tuple[float, float],
    text: str,
    fnt: ImageFont.FreeTypeFont,
    fill: str = INK,
    anchor: str = "la",
) -> None:
    draw.text(xy, text, font=fnt, fill=fill, anchor=anchor)


def text_bbox_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def read_rows(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def get_validation(path: Path) -> dict | None:
    rows = read_rows(path)
    if not rows:
        return None
    row = rows[0]
    return {
        "time": float(row["time_h"]),
        "value": float(row["reduction_pct_vs_native"]),
        "error": float(row["error_pct"]),
    }


def matrix(rows: list[dict], arm: str) -> list[list[float]]:
    values = [[float("nan") for _ in TIMES] for _ in DONORS]
    for row in rows:
        if row["ultrasound"] != arm:
            continue
        donor = row["donor"]
        time_h = int(float(row["time_h"]))
        if donor in DONORS and time_h in TIMES:
            values[DONORS.index(donor)][TIMES.index(time_h)] = float(row["reduction_pct_vs_native"])
    return values


def errors(rows: list[dict], arm: str) -> list[list[float]]:
    values = [[0.0 for _ in TIMES] for _ in DONORS]
    for row in rows:
        if row["ultrasound"] != arm:
            continue
        donor = row["donor"]
        time_h = int(float(row["time_h"]))
        if donor in DONORS and time_h in TIMES:
            values[DONORS.index(donor)][TIMES.index(time_h)] = float(row.get("error_pct_vs_native") or 0)
    return values


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16)


def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    return "#{:02X}{:02X}{:02X}".format(*rgb)


def lerp(a: int, b: int, t: float) -> int:
    return round(a + (b - a) * t)


def interp_color(stops: list[str], t: float) -> str:
    t = max(0, min(1, t))
    if t == 1:
        return stops[-1]
    scaled = t * (len(stops) - 1)
    idx = int(scaled)
    local = scaled - idx
    a = hex_to_rgb(stops[idx])
    b = hex_to_rgb(stops[idx + 1])
    return rgb_to_hex(tuple(lerp(a[i], b[i], local) for i in range(3)))


def reduction_color(value: float, vmin: float = 50, vmax: float = 96) -> str:
    stops = [PALETTE["blue_light"], PALETTE["cyan"], PALETTE["green_light"], PALETTE["green"], PALETTE["green_dark"]]
    return interp_color(stops, (value - vmin) / (vmax - vmin))


def delta_color(value: float) -> str:
    # -2 -> pale blue, 0 -> white, 11 -> green
    if value < 0:
        return interp_color(["#D9E4F4", WHITE], (value + 2) / 2)
    return interp_color([WHITE, PALETTE["cyan"], PALETTE["green"]], value / 11)


def draw_text(draw: ImageDraw.ImageDraw, xy: tuple[float, float], text: str, size: int, fill: str = INK, bold: bool = False, anchor: str = "la") -> None:
    draw.text(xy, text, font=font(size, bold), fill=fill, anchor=anchor)


def text_size(draw: ImageDraw.ImageDraw, text: str, size: int, bold: bool = False) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=font(size, bold))
    return box[2] - box[0], box[3] - box[1]


def rounded_label(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fill: str = "#F7F9FC", outline: str = GRID) -> None:
    draw.rounded_rectangle(box, radius=16, fill=fill, outline=outline, width=2)
    x0, y0, x1, _ = box
    y = y0 + 24
    for i, line in enumerate(text.split("\n")):
        draw_text(draw, (x0 + 22, y + i * 27), line, 20 if i == 0 else 18, "#C85E62" if i == 0 else INK, bold=i == 0)


def save_outputs(img: Image.Image, out_dir: Path, stem: str) -> tuple[Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    png = out_dir / f"{stem}.png"
    pdf = out_dir / f"{stem}.pdf"
    img.save(png, "PNG")
    width_pt = img.width * 72 / 220
    height_pt = img.height * 72 / 220
    c = canvas.Canvas(str(pdf), pagesize=(width_pt, height_pt))
    c.drawImage(ImageReader(str(png)), 0, 0, width=width_pt, height=height_pt)
    c.showPage()
    c.save()
    return png, pdf


def draw_colorbar(draw: ImageDraw.ImageDraw, x: int, y: int, w: int, h: int, mode: str) -> None:
    for i in range(w):
        t = i / max(1, w - 1)
        if mode == "reduction":
            color = reduction_color(50 + t * 46)
        else:
            color = delta_color(-2 + t * 13)
        draw.line((x + i, y, x + i, y + h), fill=color)
    draw.rectangle((x, y, x + w, y + h), outline=GRID, width=1)
    if mode == "reduction":
        labels = [("50", x), ("73", x + w // 2), ("96", x + w)]
        title = "IgG-binding reduction (%)"
    else:
        labels = [("-2", x), ("0", x + int(w * 2 / 13)), ("+11", x + w)]
        title = "+US - no-US (pp)"
    for lab, lx in labels:
        draw_text(draw, (lx, y + h + 28), lab, 17, MUTED, anchor="ma")
    draw_text(draw, (x + w / 2, y - 9), title, 18, INK, bold=True, anchor="ms")


def draw_heatmap_panel(
    draw: ImageDraw.ImageDraw,
    data: list[list[float]],
    x: int,
    y: int,
    cell_w: int,
    cell_h: int,
    title: str,
    show_y: bool = True,
    mode: str = "reduction",
    annotate_ribose: bool = True,
) -> None:
    draw_text(draw, (x + cell_w * len(TIMES) / 2, y - 48), title, 26, INK, bold=True, anchor="mm")
    for j, t in enumerate(TIMES):
        draw_text(draw, (x + j * cell_w + cell_w / 2, y - 16), str(t), 19, INK, bold=True, anchor="mm")
    for i, donor in enumerate(DONORS):
        if show_y:
            draw_text(draw, (x - 18, y + i * cell_h + cell_h / 2), donor, 19, INK if donor == "ribose" else MUTED, bold=donor == "ribose", anchor="rm")
        for j in range(len(TIMES)):
            value = data[i][j]
            color = reduction_color(value) if mode == "reduction" else delta_color(value)
            box = (x + j * cell_w, y + i * cell_h, x + (j + 1) * cell_w, y + (i + 1) * cell_h)
            draw.rectangle(box, fill=color, outline=WHITE, width=2)
            if (mode == "delta") or (annotate_ribose and donor == "ribose"):
                label = f"{value:+.1f}" if mode == "delta" else f"{value:.0f}"
                fill = WHITE if (mode == "reduction" and value >= 84) or (mode == "delta" and value >= 7) else INK
                draw_text(draw, (box[0] + cell_w / 2, box[1] + cell_h / 2), label, 17, fill, bold=donor == "ribose", anchor="mm")
    # Ribose row outline.
    draw.rectangle((x, y, x + cell_w * len(TIMES), y + cell_h), outline=PALETTE["green_dark"], width=4)
    draw_text(draw, (x + cell_w * len(TIMES) / 2, y + cell_h * len(DONORS) + 42), "Reaction time (h)", 20, INK, bold=True, anchor="mm")


def option_1(rows: list[dict], validation: dict | None, out_dir: Path):
    img = Image.new("RGB", (3000, 1650), WHITE)
    draw = ImageDraw.Draw(img)
    draw_text(draw, (150, 94), "Option 1. Complete donor-time landscape", 42, INK, bold=True)
    draw_text(draw, (150, 145), "Best for showing that ribose is part of a coherent high-reduction region.", 25, MUTED)
    no_us = matrix(rows, "no US")
    us = matrix(rows, "+US")
    draw_heatmap_panel(draw, no_us, 430, 280, 145, 105, "No ultrasound", True)
    draw_heatmap_panel(draw, us, 1630, 280, 145, 105, "Ultrasound assisted", False)
    draw_colorbar(draw, 1100, 1380, 800, 32, "reduction")
    if validation:
        rounded_label(draw, (2170, 1260, 2860, 1458), f"Final validation\nribose, 60 C, 4 h, +US\n{validation['value']:.1f} +/- {validation['error']:.1f}%")
    return save_outputs(img, out_dir, "option_1_dual_heatmap")


def option_2(rows: list[dict], validation: dict | None, out_dir: Path):
    img = Image.new("RGB", (2100, 1650), WHITE)
    draw = ImageDraw.Draw(img)
    draw_text(draw, (130, 94), "Option 2. Ultrasound-effect heatmap", 42, INK, bold=True)
    draw_text(draw, (130, 145), "Best for showing that ultrasound benefit is donor- and time-dependent.", 25, MUTED)
    no_us = matrix(rows, "no US")
    us = matrix(rows, "+US")
    delta = [[us[i][j] - no_us[i][j] for j in range(len(TIMES))] for i in range(len(DONORS))]
    draw_heatmap_panel(draw, delta, 520, 280, 150, 105, "+US minus no-US", True, mode="delta", annotate_ribose=True)
    draw_colorbar(draw, 700, 1380, 700, 32, "delta")
    if validation:
        rounded_label(draw, (1420, 1260, 1990, 1458), f"Reference point\nfinal ribose validation\n{validation['value']:.1f} +/- {validation['error']:.1f}%")
    return save_outputs(img, out_dir, "option_2_ultrasound_delta_heatmap")


def plot_xy(draw: ImageDraw.ImageDraw, x0: int, y0: int, w: int, h: int, x: float, y: float, y_min: float = 48, y_max: float = 98) -> tuple[float, float]:
    px = x0 + (x - 3) / (24 - 3) * w
    py = y0 + h - (y - y_min) / (y_max - y_min) * h
    return px, py


def line(draw: ImageDraw.ImageDraw, pts: list[tuple[float, float]], fill: str, width: int = 3, joint: str = "curve") -> None:
    if len(pts) >= 2:
        draw.line(pts, fill=fill, width=width, joint=joint)


def option_3(rows: list[dict], validation: dict | None, out_dir: Path):
    img = Image.new("RGB", (2200, 1500), WHITE)
    draw = ImageDraw.Draw(img)
    draw_text(draw, (130, 94), "Option 3. Ribose-focused trajectory", 42, INK, bold=True)
    draw_text(draw, (130, 145), "Best for explaining why the final ribose point is not isolated.", 25, MUTED)
    x0, y0, w, h = 330, 270, 1580, 930
    for tick in [50, 60, 70, 80, 90]:
        _, py = plot_xy(draw, x0, y0, w, h, 3, tick)
        draw.line((x0, py, x0 + w, py), fill=GRID, width=2)
        draw_text(draw, (x0 - 28, py), str(tick), 19, MUTED, anchor="rm")
    for t in TIMES:
        px, _ = plot_xy(draw, x0, y0, w, h, t, 48)
        draw_text(draw, (px, y0 + h + 36), str(t), 19, INK, bold=True, anchor="mm")
    by = {(r["donor"], r["ultrasound"]): [] for r in rows}
    for r in rows:
        by.setdefault((r["donor"], r["ultrasound"]), []).append(r)
    for donor in DONORS:
        if donor == "ribose":
            continue
        for arm in ["no US", "+US"]:
            series = sorted(by.get((donor, arm), []), key=lambda r: float(r["time_h"]))
            pts = [plot_xy(draw, x0, y0, w, h, float(r["time_h"]), float(r["reduction_pct_vs_native"])) for r in series]
            line(draw, pts, PALETTE["grey_line"], 2)
    for arm, color, width in [("no US", PALETTE["cyan"], 5), ("+US", PALETTE["green_dark"], 7)]:
        series = sorted(by.get(("ribose", arm), []), key=lambda r: float(r["time_h"]))
        pts = [plot_xy(draw, x0, y0, w, h, float(r["time_h"]), float(r["reduction_pct_vs_native"])) for r in series]
        line(draw, pts, color, width)
        for px, py in pts:
            draw.ellipse((px - 8, py - 8, px + 8, py + 8), fill=color, outline=WHITE, width=2)
    if validation:
        px, py = plot_xy(draw, x0, y0, w, h, validation["time"], validation["value"])
        draw.line((px, py - 45, px, py + 45), fill="#C85E62", width=4)
        draw.ellipse((px - 13, py - 13, px + 13, py + 13), fill="#C85E62", outline=WHITE, width=3)
        draw.line((px + 12, py, px + 290, py - 170), fill="#C85E62", width=3)
        draw_text(draw, (px + 308, py - 180), f"Final validation\n{validation['value']:.1f} +/- {validation['error']:.1f}%", 23, "#C85E62", bold=True)
    draw.line((x0, y0, x0, y0 + h, x0 + w, y0 + h), fill=GRID, width=3)
    draw_text(draw, (x0 + w / 2, y0 + h + 92), "Reaction time (h)", 24, INK, bold=True, anchor="mm")
    draw_text(draw, (x0, y0 - 34), "IgG-binding reduction (%)", 24, INK, bold=True, anchor="ls")
    rounded_label(draw, (1380, 1010, 2060, 1190), "Legend\nribose +US: dark green\nribose no-US: cyan\nother donors: grey")
    return save_outputs(img, out_dir, "option_3_ribose_focus_trajectory")


def option_4(rows: list[dict], validation: dict | None, out_dir: Path):
    img = Image.new("RGB", (2200, 1500), WHITE)
    draw = ImageDraw.Draw(img)
    draw_text(draw, (130, 94), "Option 4. +US donor ranking over time", 42, INK, bold=True)
    draw_text(draw, (130, 145), "Best for showing ribose remains top-ranked through the early-to-mid window.", 25, MUTED)
    us = matrix(rows, "+US")
    ranks = [[0 for _ in TIMES] for _ in DONORS]
    for j in range(len(TIMES)):
        order = sorted(range(len(DONORS)), key=lambda i: us[i][j], reverse=True)
        for rank, i in enumerate(order, start=1):
            ranks[i][j] = rank
    x0, y0, w, h = 330, 280, 1480, 880
    for r in range(1, 10):
        py = y0 + (r - 1) / 8 * h
        draw.line((x0, py, x0 + w, py), fill=GRID, width=2)
        draw_text(draw, (x0 - 28, py), str(r), 20, MUTED, anchor="rm")
    for j, t in enumerate(TIMES):
        px = x0 + j / (len(TIMES) - 1) * w
        draw_text(draw, (px, y0 + h + 38), str(t), 20, INK, bold=True, anchor="mm")
    for i, donor in enumerate(DONORS):
        pts = []
        for j in range(len(TIMES)):
            px = x0 + j / (len(TIMES) - 1) * w
            py = y0 + (ranks[i][j] - 1) / 8 * h
            pts.append((px, py))
        if donor == "ribose":
            line(draw, pts, PALETTE["green_dark"], 7)
            for j, (px, py) in enumerate(pts):
                draw.ellipse((px - 10, py - 10, px + 10, py + 10), fill=PALETTE["green_dark"], outline=WHITE, width=3)
                draw_text(draw, (px, py - 29), f"{us[i][j]:.0f}", 17, PALETTE["green_dark"], bold=True, anchor="mm")
            draw_text(draw, (x0 - 56, pts[0][1]), "ribose", 24, PALETTE["green_dark"], bold=True, anchor="rm")
        else:
            line(draw, pts, PALETTE["grey_line"], 3)
            draw_text(draw, (pts[-1][0] + 34, pts[-1][1]), donor, 17, MUTED, anchor="lm")
    draw_text(draw, (x0 + w / 2, y0 + h + 95), "Reaction time (h)", 24, INK, bold=True, anchor="mm")
    draw_text(draw, (x0, y0 - 34), "Rank by reduction (1 = highest)", 24, INK, bold=True, anchor="ls")
    if validation:
        rounded_label(draw, (1320, 1185, 2100, 1365), f"Final validation\nribose, 60 C, 4 h, +US\n{validation['value']:.1f} +/- {validation['error']:.1f}%")
    return save_outputs(img, out_dir, "option_4_plusUS_rank_bump")


def option_5(rows: list[dict], validation: dict | None, out_dir: Path):
    img = Image.new("RGB", (3000, 1650), WHITE)
    draw = ImageDraw.Draw(img)
    draw_text(draw, (150, 94), "Option 5. Compact +US landscape with ultrasound-benefit summary", 42, INK, bold=True)
    draw_text(draw, (150, 145), "Balanced option: shows the +US result surface and the local contribution of ultrasound.", 25, MUTED)
    no_us = matrix(rows, "no US")
    us = matrix(rows, "+US")
    delta = [[us[i][j] - no_us[i][j] for j in range(len(TIMES))] for i in range(len(DONORS))]
    draw_heatmap_panel(draw, us, 430, 280, 145, 105, "+US reduction landscape", True)
    draw_heatmap_panel(draw, delta, 1630, 280, 145, 105, "+US benefit", False, mode="delta")
    draw_colorbar(draw, 770, 1380, 560, 32, "reduction")
    draw_colorbar(draw, 1885, 1380, 560, 32, "delta")
    if validation:
        rounded_label(draw, (2260, 175, 2920, 372), f"Final validation\nribose, 60 C, 4 h, +US\n{validation['value']:.1f} +/- {validation['error']:.1f}%")
    return save_outputs(img, out_dir, "option_5_compact_heatmap_plus_delta")


def draw_mini_donor_panel(
    draw: ImageDraw.ImageDraw,
    rows: list[dict],
    donor: str,
    x0: int,
    y0: int,
    w: int,
    h: int,
    validation: dict | None = None,
) -> None:
    y_min, y_max = 48, 98
    draw.rectangle((x0, y0, x0 + w, y0 + h), outline=GRID, width=2)
    for tick in [50, 70, 90]:
        py = y0 + h - (tick - y_min) / (y_max - y_min) * h
        draw.line((x0, py, x0 + w, py), fill="#EEF3FA", width=2)
        draw_text(draw, (x0 - 9, py), str(tick), 14, MUTED, anchor="rm")
    for t in [3, 12, 24]:
        px = x0 + (t - 3) / (24 - 3) * w
        draw_text(draw, (px, y0 + h + 21), str(t), 14, MUTED, anchor="mm")
    draw_text(draw, (x0 + w / 2, y0 - 16), donor, 20, PALETTE["green_dark"] if donor == "ribose" else INK, bold=True, anchor="mm")

    by_arm = {}
    for arm in ["no US", "+US"]:
        series = sorted(
            [r for r in rows if r["donor"] == donor and r["ultrasound"] == arm],
            key=lambda r: float(r["time_h"]),
        )
        by_arm[arm] = series
    for arm, color, width in [("no US", PALETTE["cyan"], 4), ("+US", PALETTE["green_dark"], 5)]:
        pts = []
        for r in by_arm[arm]:
            t = float(r["time_h"])
            v = float(r["reduction_pct_vs_native"])
            px = x0 + (t - 3) / (24 - 3) * w
            py = y0 + h - (v - y_min) / (y_max - y_min) * h
            pts.append((px, py))
        line(draw, pts, color, width)
        for px, py in pts:
            draw.ellipse((px - 5, py - 5, px + 5, py + 5), fill=color, outline=WHITE, width=1)

    if donor == "ribose" and validation:
        t, v = validation["time"], validation["value"]
        px = x0 + (t - 3) / (24 - 3) * w
        py = y0 + h - (v - y_min) / (y_max - y_min) * h
        draw.line((px, py - 28, px, py + 28), fill="#C85E62", width=3)
        draw.ellipse((px - 8, py - 8, px + 8, py + 8), fill="#C85E62", outline=WHITE, width=2)
        draw_text(draw, (px + 14, py - 35), f"{v:.1f} +/- {validation['error']:.1f}%", 15, "#C85E62", bold=True, anchor="la")


def option_6(rows: list[dict], validation: dict | None, out_dir: Path):
    img = Image.new("RGB", (2400, 1800), WHITE)
    draw = ImageDraw.Draw(img)
    draw_text(draw, (130, 94), "Option 6. One donor per panel", 42, INK, bold=True)
    draw_text(draw, (130, 145), "Small multiples show each donor trajectory without line overlap.", 25, MUTED)
    draw_text(draw, (1850, 118), "no-US", 22, PALETTE["cyan"], bold=True)
    draw.line((1940, 130, 2035, 130), fill=PALETTE["cyan"], width=5)
    draw_text(draw, (2070, 118), "+US", 22, PALETTE["green_dark"], bold=True)
    draw.line((2130, 130, 2225, 130), fill=PALETTE["green_dark"], width=6)

    start_x, start_y = 245, 300
    panel_w, panel_h = 520, 330
    gap_x, gap_y = 185, 150
    for idx, donor in enumerate(DONORS):
        row = idx // 3
        col = idx % 3
        x0 = start_x + col * (panel_w + gap_x)
        y0 = start_y + row * (panel_h + gap_y)
        draw_mini_donor_panel(draw, rows, donor, x0, y0, panel_w, panel_h, validation)
        if col == 0:
            draw_text(draw, (x0 - 70, y0 + panel_h / 2), "Reduction (%)", 16, INK, bold=True, anchor="mm")
        if row == 2:
            draw_text(draw, (x0 + panel_w / 2, y0 + panel_h + 58), "Reaction time (h)", 17, INK, bold=True, anchor="mm")
    return save_outputs(img, out_dir, "option_6_one_donor_per_panel")


def individual_donor_panels(rows: list[dict], validation: dict | None, out_dir: Path) -> list[tuple[str, Path, Path]]:
    panel_dir = out_dir / "individual_donor_panels"
    panel_dir.mkdir(parents=True, exist_ok=True)
    outputs = []
    for donor in DONORS:
        img = Image.new("RGB", (980, 720), WHITE)
        draw = ImageDraw.Draw(img)
        draw_text(draw, (70, 62), f"{donor}", 34, PALETTE["green_dark"] if donor == "ribose" else INK, bold=True)
        draw_text(draw, (70, 103), "IgG-binding reduction over reaction time", 20, MUTED)
        draw_text(draw, (640, 68), "no-US", 18, PALETTE["cyan"], bold=True)
        draw.line((705, 80, 780, 80), fill=PALETTE["cyan"], width=4)
        draw_text(draw, (810, 68), "+US", 18, PALETTE["green_dark"], bold=True)
        draw.line((860, 80, 935, 80), fill=PALETTE["green_dark"], width=5)
        draw_mini_donor_panel(draw, rows, donor, 125, 180, 760, 400, validation)
        png, pdf = save_outputs(img, panel_dir, f"donor_panel_{donor}")
        outputs.append((f"donor_panel_{donor}", png, pdf))
    return outputs


def draw_bar_donor_panel(
    draw: ImageDraw.ImageDraw,
    rows: list[dict],
    donor: str,
    x0: int,
    y0: int,
    w: int,
    h: int,
    validation: dict | None = None,
    value_labels: bool = False,
) -> None:
    y_min, y_max = 0, 100
    panel_bottom = y0 + h
    draw.rectangle((x0, y0, x0 + w, y0 + h), outline=GRID, width=2)
    for tick in [0, 50, 75, 100]:
        py = y0 + h - (tick - y_min) / (y_max - y_min) * h
        draw.line((x0, py, x0 + w, py), fill="#EEF3FA", width=2)
        if tick > 0:
            draw_text(draw, (x0 - 9, py), str(tick), 13, MUTED, anchor="rm")
    draw_text(draw, (x0 + w / 2, y0 - 16), donor, 20, PALETTE["green_dark"] if donor == "ribose" else INK, bold=True, anchor="mm")

    donor_rows = {
        (r["ultrasound"], int(float(r["time_h"]))): r
        for r in rows
        if r["donor"] == donor
    }
    group_w = w / len(TIMES)
    bar_w = group_w * 0.28
    gap = group_w * 0.06
    for j, t in enumerate(TIMES):
        cx = x0 + group_w * j + group_w / 2
        for arm, offset, color in [
            ("no US", -bar_w / 2 - gap, PALETTE["cyan"]),
            ("+US", bar_w / 2 + gap, PALETTE["green_dark"]),
        ]:
            row = donor_rows.get((arm, t))
            if not row:
                continue
            val = float(row["reduction_pct_vs_native"])
            err = float(row.get("error_pct_vs_native") or 0)
            bx0 = cx + offset - bar_w / 2
            bx1 = cx + offset + bar_w / 2
            by = y0 + h - (val - y_min) / (y_max - y_min) * h
            draw.rounded_rectangle((bx0, by, bx1, panel_bottom), radius=4, fill=color, outline=color)
            # error bar
            e_top = y0 + h - min(y_max, val + err) / y_max * h
            e_bottom = y0 + h - max(y_min, val - err) / y_max * h
            ex = (bx0 + bx1) / 2
            draw.line((ex, e_top, ex, e_bottom), fill=INK, width=2)
            draw.line((ex - 8, e_top, ex + 8, e_top), fill=INK, width=2)
            draw.line((ex - 8, e_bottom, ex + 8, e_bottom), fill=INK, width=2)
            if value_labels and (donor == "ribose" or t in [3, 12, 24]):
                draw_text(draw, (ex, by - 12), f"{val:.0f}", 12, color, bold=True, anchor="mm")
        draw_text(draw, (cx, panel_bottom + 21), str(t), 13, MUTED, anchor="mm")

    if donor == "ribose" and validation:
        # Validation is a different condition, so it is shown as a point rather than a grouped bar.
        group_w = w / len(TIMES)
        px = x0 + group_w * 0.35
        py = y0 + h - validation["value"] / y_max * h
        err = validation["error"]
        e_top = y0 + h - min(y_max, validation["value"] + err) / y_max * h
        e_bottom = y0 + h - max(y_min, validation["value"] - err) / y_max * h
        draw.line((px, e_top, px, e_bottom), fill="#C85E62", width=3)
        draw.line((px - 9, e_top, px + 9, e_top), fill="#C85E62", width=3)
        draw.line((px - 9, e_bottom, px + 9, e_bottom), fill="#C85E62", width=3)
        draw.ellipse((px - 9, py - 9, px + 9, py + 9), fill="#C85E62", outline=WHITE, width=2)
        draw_text(draw, (px + 15, py - 26), f"{validation['value']:.1f} +/- {validation['error']:.1f}%", 14, "#C85E62", bold=True, anchor="la")


def option_7(rows: list[dict], validation: dict | None, out_dir: Path):
    img = Image.new("RGB", (2500, 1850), WHITE)
    draw = ImageDraw.Draw(img)
    draw_text(draw, (130, 94), "Option 7. One donor per panel, grouped bars", 42, INK, bold=True)
    draw_text(draw, (130, 145), "Each time point is represented by paired no-US and +US bars with error bars.", 25, MUTED)
    draw_text(draw, (1850, 118), "no-US", 22, PALETTE["cyan"], bold=True)
    draw.rectangle((1940, 105, 1995, 135), fill=PALETTE["cyan"])
    draw_text(draw, (2040, 118), "+US", 22, PALETTE["green_dark"], bold=True)
    draw.rectangle((2100, 105, 2155, 135), fill=PALETTE["green_dark"])
    draw_text(draw, (2195, 118), "validation", 22, "#C85E62", bold=True)
    draw.ellipse((2320, 111, 2342, 133), fill="#C85E62")

    start_x, start_y = 250, 310
    panel_w, panel_h = 540, 345
    gap_x, gap_y = 190, 150
    for idx, donor in enumerate(DONORS):
        row = idx // 3
        col = idx % 3
        x0 = start_x + col * (panel_w + gap_x)
        y0 = start_y + row * (panel_h + gap_y)
        draw_bar_donor_panel(draw, rows, donor, x0, y0, panel_w, panel_h, validation, value_labels=False)
        if col == 0:
            draw_text(draw, (x0 - 82, y0 + panel_h / 2), "Reduction (%)", 16, INK, bold=True, anchor="mm")
        if row == 2:
            draw_text(draw, (x0 + panel_w / 2, y0 + panel_h + 58), "Reaction time (h)", 17, INK, bold=True, anchor="mm")
    return save_outputs(img, out_dir, "option_7_one_donor_grouped_bars")


def individual_donor_bar_panels(rows: list[dict], validation: dict | None, out_dir: Path) -> list[tuple[str, Path, Path]]:
    panel_dir = out_dir / "individual_donor_bar_panels"
    panel_dir.mkdir(parents=True, exist_ok=True)
    outputs = []
    for donor in DONORS:
        img = Image.new("RGB", (1060, 760), WHITE)
        draw = ImageDraw.Draw(img)
        draw_text(draw, (70, 62), f"{donor}", 34, PALETTE["green_dark"] if donor == "ribose" else INK, bold=True)
        draw_text(draw, (70, 103), "Grouped bars for each reaction time", 20, MUTED)
        draw_text(draw, (660, 68), "no-US", 18, PALETTE["cyan"], bold=True)
        draw.rectangle((730, 58, 775, 84), fill=PALETTE["cyan"])
        draw_text(draw, (810, 68), "+US", 18, PALETTE["green_dark"], bold=True)
        draw.rectangle((860, 58, 905, 84), fill=PALETTE["green_dark"])
        draw_bar_donor_panel(draw, rows, donor, 135, 185, 790, 430, validation, value_labels=True)
        png, pdf = save_outputs(img, panel_dir, f"donor_bar_panel_{donor}")
        outputs.append((f"donor_bar_panel_{donor}", png, pdf))
    return outputs


def y_to_panel(y0: int, h: int, value: float, y_min: float = 0, y_max: float = 100) -> float:
    return y0 + h - (value - y_min) / (y_max - y_min) * h


def draw_manuscript_error_bar(
    draw: ImageDraw.ImageDraw,
    x: float,
    y_top: float,
    y_bottom: float,
    color: str = INK,
    width: int = 3,
    cap: int = 10,
) -> None:
    draw.line((x, y_top, x, y_bottom), fill=color, width=width)
    draw.line((x - cap, y_top, x + cap, y_top), fill=color, width=width)
    draw.line((x - cap, y_bottom, x + cap, y_bottom), fill=color, width=width)


def draw_manuscript_bar_panel(
    draw: ImageDraw.ImageDraw,
    rows: list[dict],
    donor: str,
    x0: int,
    y0: int,
    w: int,
    h: int,
    fs: dict[str, ImageFont.FreeTypeFont],
    validation: dict | None = None,
    show_y_label: bool = False,
    show_x_label: bool = False,
    label_values: bool = False,
    show_panel_title: bool = True,
) -> None:
    donor_title = donor.capitalize()
    title_color = PALETTE["green_dark"] if donor == "ribose" else INK
    if show_panel_title:
        draw_text_font(draw, (x0 + w / 2, y0 - 52), donor_title, fs["small"], title_color, "mm")

    for tick in [0, 25, 50, 75, 100]:
        py = y_to_panel(y0, h, tick)
        draw.line((x0, py, x0 + w, py), fill=GRID, width=2)
        draw_text_font(draw, (x0 - 16, py), str(tick), fs["tiny"], MUTED, "rm")

    draw.line((x0, y0, x0, y0 + h), fill=INK, width=3)
    draw.line((x0, y0 + h, x0 + w, y0 + h), fill=INK, width=3)

    donor_rows = {
        (r["ultrasound"], int(float(r["time_h"]))): r
        for r in rows
        if r["donor"] == donor
    }
    group_w = w / len(TIMES)
    bar_w = min(44, group_w * 0.25)
    gap = max(7, group_w * 0.05)
    for j, time_h in enumerate(TIMES):
        cx = x0 + group_w * j + group_w / 2
        for arm, offset, color in [
            ("no US", -bar_w / 2 - gap, MANUSCRIPT_BAR_COLORS["no US"]),
            ("+US", bar_w / 2 + gap, MANUSCRIPT_BAR_COLORS["+US"]),
        ]:
            row = donor_rows.get((arm, time_h))
            if not row:
                continue
            value = float(row["reduction_pct_vs_native"])
            error = float(row.get("error_pct_vs_native") or 0)
            x = cx + offset
            y = y_to_panel(y0, h, value)
            draw.rectangle((x - bar_w / 2, y, x + bar_w / 2, y0 + h), fill=color)

            y_top = y_to_panel(y0, h, min(100, value + error))
            y_bottom = y_to_panel(y0, h, max(0, value - error))
            draw_manuscript_error_bar(draw, x, y_top, y_bottom, MUTED, width=2, cap=7)

            if label_values:
                label = f"{value:.0f}"
                label_w, _ = text_bbox_size(draw, label, fs["micro"])
                label_fill = color if label_w < bar_w + 12 else MUTED
                draw_text_font(draw, (x, min(y - 10, y_top - 7)), label, fs["micro"], label_fill, "mm")

        draw_text_font(draw, (cx, y0 + h + 44), str(time_h), fs["tiny"], MUTED, "mm")

    if donor == "ribose" and validation:
        # The final point uses ribose at 60 C and 4 h, so it is shown as a
        # validation marker rather than grouped into the 55 C time-course bars.
        px = x0 + group_w * 0.38
        py = y_to_panel(y0, h, validation["value"])
        y_top = y_to_panel(y0, h, min(100, validation["value"] + validation["error"]))
        y_bottom = y_to_panel(y0, h, max(0, validation["value"] - validation["error"]))
        draw_manuscript_error_bar(
            draw,
            px,
            y_top,
            y_bottom,
            MANUSCRIPT_BAR_COLORS["validation"],
            width=3,
            cap=10,
        )
        draw.ellipse((px - 10, py - 10, px + 10, py + 10), fill=MANUSCRIPT_BAR_COLORS["validation"], outline=WHITE, width=2)
        label = f"{validation['value']:.1f}"
        draw_text_font(draw, (px + 18, py - 28), label, fs["micro"], MANUSCRIPT_BAR_COLORS["validation"], "la")

    if show_y_label:
        draw_text_font(draw, (x0 - 22, y0 - 66), "Reduction (%)", fs["tiny"], INK, "ra")
    if show_x_label:
        draw_text_font(draw, (x0 + w / 2, y0 + h + 98), "Reaction time (h)", fs["tiny"], INK, "mm")


def draw_manuscript_bar_legend(
    draw: ImageDraw.ImageDraw,
    center_x: int,
    y: int,
    fs: dict[str, ImageFont.FreeTypeFont],
    include_validation: bool = True,
) -> None:
    items = [
        ("No ultrasound", MANUSCRIPT_BAR_COLORS["no US"], "square"),
        ("Ultrasound assisted", MANUSCRIPT_BAR_COLORS["+US"], "square"),
    ]
    if include_validation:
        items.append(("Final validation", MANUSCRIPT_BAR_COLORS["validation"], "dot"))
    item_widths = []
    for label, _, _ in items:
        label_w, _ = text_bbox_size(draw, label, fs["small"])
        item_widths.append(38 + label_w + 58)
    total = sum(item_widths) - 58
    x = center_x - total / 2
    for (label, color, shape), item_width in zip(items, item_widths):
        if shape == "square":
            draw.rectangle((x, y - 14, x + 28, y + 14), fill=color)
        else:
            draw.ellipse((x + 2, y - 13, x + 28, y + 13), fill=color)
        draw_text_font(draw, (x + 40, y), label, fs["small"], INK, "lm")
        x += item_width


def option_8(rows: list[dict], validation: dict | None, out_dir: Path):
    img = Image.new("RGB", (2850, 2380), WHITE)
    draw = ImageDraw.Draw(img)
    fs = manuscript_fonts(3.0)

    draw_text_font(draw, (1425, 112), "Donor-time IgG-binding reduction landscape", fs["title"], INK, "mm")
    draw_text_font(draw, (70, 275), "Reduction (%)", fs["tiny"], INK, "la")

    start_x, start_y = 430, 350
    panel_w, panel_h = 610, 355
    gap_x, gap_y = 160, 225
    for idx, donor in enumerate(DONORS):
        row = idx // 3
        col = idx % 3
        x0 = start_x + col * (panel_w + gap_x)
        y0 = start_y + row * (panel_h + gap_y)
        draw_manuscript_bar_panel(
            draw,
            rows,
            donor,
            x0,
            y0,
            panel_w,
            panel_h,
            fs,
            validation=None,
            show_y_label=False,
            show_x_label=row == 2,
            label_values=False,
        )

    draw_manuscript_bar_legend(draw, 1425, 2295, fs, include_validation=False)
    return save_outputs(img, out_dir, "option_8_manuscript_style_grouped_bars")


def individual_donor_bar_panels_manuscript(rows: list[dict], validation: dict | None, out_dir: Path) -> list[tuple[str, Path, Path]]:
    panel_dir = out_dir / "individual_donor_bar_panels_manuscript"
    panel_dir.mkdir(parents=True, exist_ok=True)
    outputs = []
    fs = manuscript_fonts(1.18)
    for donor in DONORS:
        img = Image.new("RGB", (1180, 820), WHITE)
        draw = ImageDraw.Draw(img)
        draw_text_font(
            draw,
            (590, 70),
            f"{donor.capitalize()}",
            fs["title"],
            PALETTE["green_dark"] if donor == "ribose" else INK,
            "mm",
        )
        draw_text_font(draw, (590, 120), "Grouped bars for each reaction time", fs["small"], MUTED, "mm")
        draw_manuscript_bar_panel(
            draw,
            rows,
            donor,
            150,
            205,
            880,
            410,
            fs,
            validation=None,
            show_y_label=True,
            show_x_label=True,
            label_values=True,
            show_panel_title=False,
        )
        draw_manuscript_bar_legend(draw, 590, 755, fs, include_validation=False)
        png, pdf = save_outputs(img, panel_dir, f"donor_bar_panel_{donor}_manuscript")
        outputs.append((f"donor_bar_panel_{donor}_manuscript", png, pdf))
    return outputs


def write_manifest(outputs: list[tuple[str, Path, Path]], out_dir: Path) -> None:
    notes = {
        "option_1_dual_heatmap": "Complete no-US/+US landscape; strongest general supplementary figure candidate.",
        "option_2_ultrasound_delta_heatmap": "Emphasizes donor- and time-dependent ultrasound contribution.",
        "option_3_ribose_focus_trajectory": "Emphasizes ribose trajectory and final validation in the full landscape.",
        "option_4_plusUS_rank_bump": "Emphasizes ribose ranking across the +US time course.",
        "option_5_compact_heatmap_plus_delta": "Compact combined view of +US landscape and ultrasound benefit.",
        "option_6_one_donor_per_panel": "Small-multiple version with one mini trajectory panel per donor.",
        "option_7_one_donor_grouped_bars": "Small-multiple grouped-bar version with one mini bar chart per donor.",
        "option_8_manuscript_style_grouped_bars": "Main-text bar-chart style with larger fonts, bottom legend and no validation overlay.",
    }
    with (out_dir / "landscape_options_manifest.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["option", "png", "pdf", "suggested_use"])
        for stem, png, pdf in outputs:
            writer.writerow([stem, str(png), str(pdf), notes.get(stem, "")])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--validation", type=Path, default=DEFAULT_VALIDATION)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    rows = read_rows(args.data)
    validation = get_validation(args.validation)
    outputs = []
    for stem, fn in [
        ("option_1_dual_heatmap", option_1),
        ("option_2_ultrasound_delta_heatmap", option_2),
        ("option_3_ribose_focus_trajectory", option_3),
        ("option_4_plusUS_rank_bump", option_4),
        ("option_5_compact_heatmap_plus_delta", option_5),
        ("option_6_one_donor_per_panel", option_6),
        ("option_7_one_donor_grouped_bars", option_7),
        ("option_8_manuscript_style_grouped_bars", option_8),
    ]:
        png, pdf = fn(rows, validation, args.output_dir)
        outputs.append((stem, png, pdf))
        print(png)
        print(pdf)
    outputs.extend(individual_donor_panels(rows, validation, args.output_dir))
    outputs.extend(individual_donor_bar_panels(rows, validation, args.output_dir))
    outputs.extend(individual_donor_bar_panels_manuscript(rows, validation, args.output_dir))
    write_manifest(outputs, args.output_dir)


if __name__ == "__main__":
    main()
