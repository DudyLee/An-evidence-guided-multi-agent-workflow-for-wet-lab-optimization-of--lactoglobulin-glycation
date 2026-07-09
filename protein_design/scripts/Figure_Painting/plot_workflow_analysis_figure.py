from __future__ import annotations

import argparse
import csv
import html
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping


INK = "#202124"
MUTED = "#5F6368"
GRID = "#E7E3DC"
WHITE = "#FFFFFF"

PHASE_ORDER = [
    "team_selection",
    "project_specification",
    "tools_selection",
    "execution_planning",
    "iteration1_discussion",
]

PHASE_LABELS = {
    "team_selection": "Team selection",
    "project_specification": "Project specification",
    "tools_selection": "Tools selection",
    "execution_planning": "Execution planning",
    "iteration1_discussion": "First iteration",
}

CONTRIBUTOR_ORDER = [
    "Human Researcher",
    "Principal Investigator",
    "Maillard Reaction Chemistry and Process Scientist",
    "Allergenicity and Immunoassay Interpretation Scientist",
    "Experimental Design and Evidence Synthesis Scientist",
    "Scientific Critic",
]

CONTRIBUTOR_LABELS = {
    "Human Researcher": "Human researcher",
    "Principal Investigator": "Principal investigator",
    "Maillard Reaction Chemistry and Process Scientist": "Maillard chemistry",
    "Allergenicity and Immunoassay Interpretation Scientist": "Allergenicity",
    "Experimental Design and Evidence Synthesis Scientist": "Experimental design",
    "Scientific Critic": "Scientific critic",
}

CONTRIBUTOR_COLORS = {
    "Human Researcher": "#C83E4D",
    "Principal Investigator": "#245F78",
    "Maillard Reaction Chemistry and Process Scientist": "#7E6AA2",
    "Allergenicity and Immunoassay Interpretation Scientist": "#6F8F4E",
    "Experimental Design and Evidence Synthesis Scientist": "#E77D22",
    "Scientific Critic": "#9AA0A6",
}

# Audited values reproduced from the five discussion phases analysed in the
# manuscript. The notebook can pass freshly calculated values to override them.
DEFAULT_PHASE_COUNTS = {
    "team_selection": {
        "Human Researcher": 588,
        "Principal Investigator": 3_134,
    },
    "project_specification": {
        "Human Researcher": 501,
        "Principal Investigator": 62_448,
        "Maillard Reaction Chemistry and Process Scientist": 15_338,
        "Allergenicity and Immunoassay Interpretation Scientist": 22_702,
        "Experimental Design and Evidence Synthesis Scientist": 20_062,
        "Scientific Critic": 7_362,
    },
    "tools_selection": {
        "Human Researcher": 241,
        "Principal Investigator": 55_504,
        "Maillard Reaction Chemistry and Process Scientist": 18_160,
        "Allergenicity and Immunoassay Interpretation Scientist": 21_972,
        "Experimental Design and Evidence Synthesis Scientist": 19_416,
        "Scientific Critic": 10_048,
    },
    "execution_planning": {
        "Human Researcher": 553,
        "Principal Investigator": 76_430,
        "Maillard Reaction Chemistry and Process Scientist": 16_212,
        "Allergenicity and Immunoassay Interpretation Scientist": 18_306,
        "Experimental Design and Evidence Synthesis Scientist": 24_200,
        "Scientific Critic": 12_156,
    },
    "iteration1_discussion": {
        "Human Researcher": 263,
        "Principal Investigator": 49_190,
        "Maillard Reaction Chemistry and Process Scientist": 16_202,
        "Allergenicity and Immunoassay Interpretation Scientist": 22_826,
        "Experimental Design and Evidence Synthesis Scientist": 29_474,
        "Scientific Critic": 8_164,
    },
}


def _hex_to_rgb(color: str) -> tuple[float, float, float]:
    color = color.lstrip("#")
    return tuple(int(color[index : index + 2], 16) / 255 for index in (0, 2, 4))


def _pdf_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def _text_width(value: str, size: float, bold: bool = False) -> float:
    width = 0.0
    for char in value:
        if char in "ilI1.,:;|'":
            factor = 0.27
        elif char in "MW@%":
            factor = 0.85
        elif char == " ":
            factor = 0.28
        else:
            factor = 0.53
        width += factor * size
    return width * (1.04 if bold else 1.0)


@dataclass
class Operation:
    kind: str
    values: dict[str, object]


class VectorDrawing:
    def __init__(self, width: float, height: float, title: str):
        self.width = width
        self.height = height
        self.title = title
        self.operations: list[Operation] = []

    def line(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        color: str = INK,
        width: float = 1.0,
    ) -> None:
        self.operations.append(
            Operation(
                "line",
                {
                    "x1": x1,
                    "y1": y1,
                    "x2": x2,
                    "y2": y2,
                    "color": color,
                    "width": width,
                },
            )
        )

    def rect(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        fill: str,
        stroke: str | None = None,
        stroke_width: float = 0.0,
        radius: float = 0.0,
    ) -> None:
        self.operations.append(
            Operation(
                "rect",
                {
                    "x": x,
                    "y": y,
                    "width": width,
                    "height": height,
                    "fill": fill,
                    "stroke": stroke,
                    "stroke_width": stroke_width,
                    "radius": radius,
                },
            )
        )

    def polygon(
        self,
        points: Iterable[tuple[float, float]],
        fill: str,
        stroke: str | None = None,
        stroke_width: float = 0.0,
    ) -> None:
        self.operations.append(
            Operation(
                "polygon",
                {
                    "points": list(points),
                    "fill": fill,
                    "stroke": stroke,
                    "stroke_width": stroke_width,
                },
            )
        )

    def circle(
        self,
        x: float,
        y: float,
        radius: float,
        fill: str,
        stroke: str | None = None,
        stroke_width: float = 0.0,
    ) -> None:
        self.operations.append(
            Operation(
                "circle",
                {
                    "x": x,
                    "y": y,
                    "radius": radius,
                    "fill": fill,
                    "stroke": stroke,
                    "stroke_width": stroke_width,
                },
            )
        )

    def text(
        self,
        x: float,
        y: float,
        value: str,
        size: float,
        color: str = INK,
        bold: bool = False,
        anchor: str = "start",
    ) -> None:
        self.operations.append(
            Operation(
                "text",
                {
                    "x": x,
                    "y": y,
                    "value": value,
                    "size": size,
                    "color": color,
                    "bold": bold,
                    "anchor": anchor,
                },
            )
        )

    def save_svg(self, path: Path) -> None:
        parts = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            (
                f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" '
                f'height="{self.height}" viewBox="0 0 {self.width} {self.height}">'
            ),
            f"<title>{html.escape(self.title)}</title>",
            f'<rect width="{self.width}" height="{self.height}" fill="#FFFFFF"/>',
        ]
        for operation in self.operations:
            values = operation.values
            if operation.kind == "line":
                parts.append(
                    (
                        f'<line x1="{values["x1"]:.2f}" y1="{values["y1"]:.2f}" '
                        f'x2="{values["x2"]:.2f}" y2="{values["y2"]:.2f}" '
                        f'stroke="{values["color"]}" stroke-width="{values["width"]:.2f}"/>'
                    )
                )
            elif operation.kind == "rect":
                stroke = (
                    f' stroke="{values["stroke"]}" stroke-width="{values["stroke_width"]:.2f}"'
                    if values["stroke"]
                    else ""
                )
                parts.append(
                    (
                        f'<rect x="{values["x"]:.2f}" y="{values["y"]:.2f}" '
                        f'width="{values["width"]:.2f}" height="{values["height"]:.2f}" '
                        f'rx="{values["radius"]:.2f}" fill="{values["fill"]}"{stroke}/>'
                    )
                )
            elif operation.kind == "polygon":
                points = " ".join(
                    f"{x:.2f},{y:.2f}" for x, y in values["points"]
                )
                stroke = (
                    f' stroke="{values["stroke"]}" stroke-width="{values["stroke_width"]:.2f}"'
                    if values["stroke"]
                    else ""
                )
                parts.append(
                    f'<polygon points="{points}" fill="{values["fill"]}"{stroke}/>'
                )
            elif operation.kind == "circle":
                stroke = (
                    f' stroke="{values["stroke"]}" stroke-width="{values["stroke_width"]:.2f}"'
                    if values["stroke"]
                    else ""
                )
                parts.append(
                    (
                        f'<circle cx="{values["x"]:.2f}" cy="{values["y"]:.2f}" '
                        f'r="{values["radius"]:.2f}" fill="{values["fill"]}"{stroke}/>'
                    )
                )
            elif operation.kind == "text":
                parts.append(
                    (
                        f'<text x="{values["x"]:.2f}" y="{values["y"]:.2f}" '
                        f'text-anchor="{values["anchor"]}" dominant-baseline="middle" '
                        f'font-family="Helvetica, Arial, sans-serif" '
                        f'font-size="{values["size"]:.2f}" '
                        f'font-weight="{"700" if values["bold"] else "400"}" '
                        f'fill="{values["color"]}">{html.escape(str(values["value"]))}</text>'
                    )
                )
        parts.append("</svg>")
        path.write_text("\n".join(parts), encoding="utf-8")

    def save_pdf(self, path: Path) -> None:
        commands: list[str] = []
        for operation in self.operations:
            values = operation.values
            if operation.kind == "line":
                r, g, b = _hex_to_rgb(str(values["color"]))
                commands.extend(
                    [
                        f"{r:.4f} {g:.4f} {b:.4f} RG",
                        f"{float(values['width']):.3f} w",
                        (
                            f"{float(values['x1']):.3f} "
                            f"{self.height - float(values['y1']):.3f} m "
                            f"{float(values['x2']):.3f} "
                            f"{self.height - float(values['y2']):.3f} l S"
                        ),
                    ]
                )
            elif operation.kind == "rect":
                x = float(values["x"])
                y = self.height - float(values["y"]) - float(values["height"])
                width = float(values["width"])
                height = float(values["height"])
                r, g, b = _hex_to_rgb(str(values["fill"]))
                commands.append(f"{r:.4f} {g:.4f} {b:.4f} rg")
                if values["stroke"]:
                    sr, sg, sb = _hex_to_rgb(str(values["stroke"]))
                    commands.extend(
                        [
                            f"{sr:.4f} {sg:.4f} {sb:.4f} RG",
                            f"{float(values['stroke_width']):.3f} w",
                            f"{x:.3f} {y:.3f} {width:.3f} {height:.3f} re B",
                        ]
                    )
                else:
                    commands.append(
                        f"{x:.3f} {y:.3f} {width:.3f} {height:.3f} re f"
                    )
            elif operation.kind == "polygon":
                points = list(values["points"])
                if not points:
                    continue
                r, g, b = _hex_to_rgb(str(values["fill"]))
                commands.append(f"{r:.4f} {g:.4f} {b:.4f} rg")
                x0, y0 = points[0]
                path_commands = [f"{x0:.3f} {self.height - y0:.3f} m"]
                for x, y in points[1:]:
                    path_commands.append(f"{x:.3f} {self.height - y:.3f} l")
                path_commands.append("h")
                if values["stroke"]:
                    sr, sg, sb = _hex_to_rgb(str(values["stroke"]))
                    commands.extend(
                        [
                            f"{sr:.4f} {sg:.4f} {sb:.4f} RG",
                            f"{float(values['stroke_width']):.3f} w",
                            " ".join(path_commands) + " B",
                        ]
                    )
                else:
                    commands.append(" ".join(path_commands) + " f")
            elif operation.kind == "circle":
                x = float(values["x"])
                y = self.height - float(values["y"])
                radius = float(values["radius"])
                control = radius * 0.5522847498
                r, g, b = _hex_to_rgb(str(values["fill"]))
                commands.append(f"{r:.4f} {g:.4f} {b:.4f} rg")
                circle_path = (
                    f"{x + radius:.3f} {y:.3f} m "
                    f"{x + radius:.3f} {y + control:.3f} "
                    f"{x + control:.3f} {y + radius:.3f} "
                    f"{x:.3f} {y + radius:.3f} c "
                    f"{x - control:.3f} {y + radius:.3f} "
                    f"{x - radius:.3f} {y + control:.3f} "
                    f"{x - radius:.3f} {y:.3f} c "
                    f"{x - radius:.3f} {y - control:.3f} "
                    f"{x - control:.3f} {y - radius:.3f} "
                    f"{x:.3f} {y - radius:.3f} c "
                    f"{x + control:.3f} {y - radius:.3f} "
                    f"{x + radius:.3f} {y - control:.3f} "
                    f"{x + radius:.3f} {y:.3f} c h"
                )
                if values["stroke"]:
                    sr, sg, sb = _hex_to_rgb(str(values["stroke"]))
                    commands.extend(
                        [
                            f"{sr:.4f} {sg:.4f} {sb:.4f} RG",
                            f"{float(values['stroke_width']):.3f} w",
                            circle_path + " B",
                        ]
                    )
                else:
                    commands.append(circle_path + " f")
            elif operation.kind == "text":
                value = str(values["value"])
                size = float(values["size"])
                bold = bool(values["bold"])
                x = float(values["x"])
                anchor = str(values["anchor"])
                width = _text_width(value, size, bold)
                if anchor == "middle":
                    x -= width / 2
                elif anchor == "end":
                    x -= width
                y = self.height - float(values["y"]) - size * 0.34
                r, g, b = _hex_to_rgb(str(values["color"]))
                commands.extend(
                    [
                        f"{r:.4f} {g:.4f} {b:.4f} rg",
                        (
                            f"BT /{'F2' if bold else 'F1'} {size:.3f} Tf "
                            f"{x:.3f} {y:.3f} Td ({_pdf_escape(value)}) Tj ET"
                        ),
                    ]
                )

        stream = "\n".join(commands).encode("latin-1", errors="replace")
        objects = [
            b"<< /Type /Catalog /Pages 2 0 R >>",
            b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
            (
                f"<< /Type /Page /Parent 2 0 R "
                f"/MediaBox [0 0 {self.width:.3f} {self.height:.3f}] "
                f"/Resources << /Font << /F1 4 0 R /F2 5 0 R >> >> "
                f"/Contents 6 0 R >>"
            ).encode("ascii"),
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>",
            b"<< /Length " + str(len(stream)).encode("ascii") + b" >>\nstream\n"
            + stream
            + b"\nendstream",
        ]

        payload = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
        offsets = [0]
        for index, obj in enumerate(objects, start=1):
            offsets.append(len(payload))
            payload.extend(f"{index} 0 obj\n".encode("ascii"))
            payload.extend(obj)
            payload.extend(b"\nendobj\n")
        xref_offset = len(payload)
        payload.extend(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
        payload.extend(b"0000000000 65535 f \n")
        for offset in offsets[1:]:
            payload.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
        payload.extend(
            (
                f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\n"
                f"startxref\n{xref_offset}\n%%EOF\n"
            ).encode("ascii")
        )
        path.write_bytes(bytes(payload))


class ScaledCanvas:
    def __init__(
        self,
        drawing: VectorDrawing,
        x: float,
        y: float,
        width: float,
        height: float,
        base_width: float,
        base_height: float,
    ):
        self.drawing = drawing
        self.x = x
        self.y = y
        self.sx = width / base_width
        self.sy = height / base_height
        self.ss = min(self.sx, self.sy)

    def _point(self, x: float, y: float) -> tuple[float, float]:
        return self.x + x * self.sx, self.y + y * self.sy

    def line(self, x1: float, y1: float, x2: float, y2: float, **kwargs) -> None:
        p1 = self._point(x1, y1)
        p2 = self._point(x2, y2)
        kwargs["width"] = float(kwargs.get("width", 1.0)) * self.ss
        self.drawing.line(*p1, *p2, **kwargs)

    def rect(
        self, x: float, y: float, width: float, height: float, **kwargs
    ) -> None:
        px, py = self._point(x, y)
        kwargs["stroke_width"] = float(kwargs.get("stroke_width", 0.0)) * self.ss
        kwargs["radius"] = float(kwargs.get("radius", 0.0)) * self.ss
        self.drawing.rect(px, py, width * self.sx, height * self.sy, **kwargs)

    def polygon(self, points: Iterable[tuple[float, float]], **kwargs) -> None:
        kwargs["stroke_width"] = float(kwargs.get("stroke_width", 0.0)) * self.ss
        self.drawing.polygon([self._point(x, y) for x, y in points], **kwargs)

    def circle(self, x: float, y: float, radius: float, **kwargs) -> None:
        px, py = self._point(x, y)
        kwargs["stroke_width"] = float(kwargs.get("stroke_width", 0.0)) * self.ss
        self.drawing.circle(px, py, radius * self.ss, **kwargs)

    def text(self, x: float, y: float, value: str, size: float, **kwargs) -> None:
        px, py = self._point(x, y)
        self.drawing.text(px, py, value, size * self.ss, **kwargs)


def _wrap_text(value: str, max_width: float, size: float, bold: bool = False) -> list[str]:
    words = value.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if current and _text_width(candidate, size, bold) > max_width:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def _draw_multiline(
    canvas: ScaledCanvas,
    x: float,
    y: float,
    value: str,
    max_width: float,
    size: float,
    line_height: float,
    *,
    color: str = INK,
    bold: bool = False,
    anchor: str = "middle",
) -> None:
    lines = _wrap_text(value, max_width, size, bold)
    start_y = y - (len(lines) - 1) * line_height / 2
    for index, line in enumerate(lines):
        canvas.text(
            x,
            start_y + index * line_height,
            line,
            size,
            color=color,
            bold=bold,
            anchor=anchor,
        )


def _normalise_counts(
    phase_counts: Mapping[str, Mapping[str, int]] | None,
) -> dict[str, dict[str, int]]:
    source = phase_counts or DEFAULT_PHASE_COUNTS
    normalised: dict[str, dict[str, int]] = {}
    for phase in PHASE_ORDER:
        phase_values = source.get(phase, {})
        normalised[phase] = {
            contributor: int(phase_values.get(contributor, 0))
            for contributor in CONTRIBUTOR_ORDER
        }
    return normalised


def _draw_search_funnel(canvas: ScaledCanvas) -> None:
    canvas.text(18, 40, "a", 30, bold=True, anchor="start")
    canvas.text(
        800,
        42,
        "Stage-wise narrowing of the experimental search space",
        30,
        bold=True,
        anchor="middle",
    )
    stages = [
        (
            "Literature-visible envelope",
            "Semantically grouped variable levels",
            "~1.12 million plausible combinations",
            "#EAF3FF",
        ),
        (
            "Study-feasible envelope",
            "Scope and feasibility constraints",
            "",
            "#DDE7F5",
        ),
        (
            "Project-specified candidates",
            "High-value scientific questions",
            "",
            "#F7F9FC",
        ),
        (
            "Operational decision space",
            "Matched comparisons",
            "",
            "#EAF3FF",
        ),
        (
            "Execution-ready matrix",
            "Completeness audit",
            "24 planned / 24 result-bearing",
            "#DCEAD4",
        ),
        (
            "Comparator-aware refinement",
            "Focused adjudication",
            "",
            "#CFE2C8",
        ),
        (
            "Final validation candidate",
            "Locked recommendation",
            "1 candidate",
            "#DDE7F5",
        ),
    ]
    left = 42
    gap = 15
    stage_width = (1600 - left * 2 - gap * 6) / 7
    centre_y = 230
    heights = [222, 202, 184, 166, 148, 130, 112]
    for index, (title, note, metric, color) in enumerate(stages):
        x = left + index * (stage_width + gap)
        height = heights[index]
        y = centre_y - height / 2
        point = 17
        points = [
            (x, y),
            (x + stage_width - point, y),
            (x + stage_width, centre_y),
            (x + stage_width - point, y + height),
            (x, y + height),
            (x + (point if index else 0), centre_y),
        ]
        canvas.polygon(points, fill=color, stroke=WHITE, stroke_width=2)
        text_x = x + stage_width / 2
        _draw_multiline(
            canvas,
            text_x,
            centre_y - 31,
            title,
            stage_width - 42,
            18,
            21,
            bold=True,
        )
        _draw_multiline(
            canvas,
            text_x,
            centre_y + 23,
            note,
            stage_width - 43,
            16,
            19,
            color=MUTED,
        )
        if metric:
            canvas.text(
                text_x,
                centre_y + height / 2 + 28,
                metric,
                16,
                color=INK,
                bold=True,
                anchor="middle",
            )
    canvas.text(
        800,
        394,
        "Conceptual stages; widths are not proportional to candidate counts.",
        16,
        color=MUTED,
        anchor="middle",
    )


def _phase_percentages(
    counts: Mapping[str, Mapping[str, int]],
) -> dict[str, dict[str, float]]:
    percentages: dict[str, dict[str, float]] = {}
    for phase in PHASE_ORDER:
        total = sum(counts[phase].values())
        percentages[phase] = {
            contributor: (100 * counts[phase][contributor] / total if total else 0)
            for contributor in CONTRIBUTOR_ORDER
        }
    return percentages


def _label_color(fill: str) -> str:
    red, green, blue = _hex_to_rgb(fill)
    luminance = 0.2126 * red + 0.7152 * green + 0.0722 * blue
    return INK if luminance > 0.62 else WHITE


def _draw_phase_composition(
    canvas: ScaledCanvas,
    counts: Mapping[str, Mapping[str, int]],
) -> None:
    canvas.text(18, 42, "b", 30, bold=True, anchor="start")
    canvas.text(
        450,
        42,
        "Role composition across workflow phases",
        30,
        bold=True,
        anchor="middle",
    )
    percentages = _phase_percentages(counts)
    plot_left = 250
    plot_right = 860
    plot_top = 108
    plot_bottom = 490
    plot_width = plot_right - plot_left
    for tick in [0, 25, 50, 75, 100]:
        x = plot_left + plot_width * tick / 100
        canvas.line(x, plot_top, x, plot_bottom, color=GRID, width=1.5)
        canvas.text(x, plot_bottom + 27, str(tick), 20, color=MUTED, anchor="middle")

    bar_height = 52
    row_gap = 22
    for row, phase in enumerate(PHASE_ORDER):
        y = plot_top + row * (bar_height + row_gap)
        canvas.text(
            plot_left - 17,
            y + bar_height / 2,
            PHASE_LABELS[phase],
            20,
            anchor="end",
        )
        current_x = plot_left
        for contributor in CONTRIBUTOR_ORDER:
            percentage = percentages[phase][contributor]
            width = plot_width * percentage / 100
            if width <= 0:
                continue
            color = CONTRIBUTOR_COLORS[contributor]
            canvas.rect(current_x, y, width, bar_height, fill=color)
            if percentage >= 9.0:
                canvas.text(
                    current_x + width / 2,
                    y + bar_height / 2,
                    f"{percentage:.1f}%",
                    18,
                    color=_label_color(color),
                    bold=True,
                    anchor="middle",
                )
            elif (
                contributor == "Scientific Critic"
                and percentage >= 4.0
            ):
                canvas.text(
                    current_x + width / 2,
                    y + bar_height / 2,
                    f"{percentage:.1f}%",
                    14,
                    color=_label_color(color),
                    bold=True,
                    anchor="middle",
                )
            elif (
                contributor == "Human Researcher"
                and percentage < 4.0
            ):
                marker_x = current_x + max(width / 2, 1.5)
                canvas.line(
                    marker_x,
                    y + 1,
                    marker_x,
                    y - 8,
                    color=color,
                    width=1.5,
                )
                canvas.text(
                    marker_x + 5,
                    y - 11,
                    f"{percentage:.1f}%",
                    14,
                    color=color,
                    bold=True,
                    anchor="start",
                )
            current_x += width
        canvas.line(
            plot_left, y, plot_right, y, color="#A8ADB5", width=1.0
        )
        canvas.line(
            plot_left,
            y + bar_height,
            plot_right,
            y + bar_height,
            color="#A8ADB5",
            width=1.0,
        )
        canvas.line(
            plot_left, y, plot_left, y + bar_height, color="#A8ADB5", width=1.0
        )
        canvas.line(
            plot_right,
            y,
            plot_right,
            y + bar_height,
            color="#A8ADB5",
            width=1.0,
        )
    canvas.text(
        (plot_left + plot_right) / 2,
        plot_bottom + 59,
        "Share of words within phase (%)",
        20,
        anchor="middle",
    )

    legend_x = 80
    legend_y = 592
    column_width = 285
    for index, contributor in enumerate(CONTRIBUTOR_ORDER):
        row = index // 3
        column = index % 3
        x = legend_x + column * column_width
        y = legend_y + row * 45
        canvas.rect(x, y - 11, 26, 22, fill=CONTRIBUTOR_COLORS[contributor])
        canvas.text(
            x + 37,
            y,
            CONTRIBUTOR_LABELS[contributor],
            18,
            anchor="start",
        )


def _contributor_totals(
    counts: Mapping[str, Mapping[str, int]],
) -> dict[str, int]:
    return {
        contributor: sum(counts[phase][contributor] for phase in PHASE_ORDER)
        for contributor in CONTRIBUTOR_ORDER
    }


def _draw_contributor_totals(
    canvas: ScaledCanvas,
    counts: Mapping[str, Mapping[str, int]],
) -> None:
    canvas.text(18, 42, "c", 30, bold=True, anchor="start")
    canvas.text(
        450,
        42,
        "Cumulative discussion contribution",
        30,
        bold=True,
        anchor="middle",
    )
    totals = _contributor_totals(counts)
    agent_total = sum(
        total
        for contributor, total in totals.items()
        if contributor != "Human Researcher"
    )
    human_total = totals["Human Researcher"]
    canvas.text(
        450,
        80,
        f"All agents: {agent_total / 1000:.1f}k words   |   Human: {human_total / 1000:.1f}k words",
        19,
        color=MUTED,
        anchor="middle",
    )

    display_order = [
        "Principal Investigator",
        "Experimental Design and Evidence Synthesis Scientist",
        "Allergenicity and Immunoassay Interpretation Scientist",
        "Maillard Reaction Chemistry and Process Scientist",
        "Scientific Critic",
        "Human Researcher",
    ]
    plot_left = 255
    plot_right = 850
    plot_top = 117
    plot_bottom = 565
    plot_width = plot_right - plot_left
    maximum = 270_000
    for tick in [0, 50_000, 100_000, 150_000, 200_000, 250_000]:
        x = plot_left + plot_width * tick / maximum
        canvas.line(x, plot_top, x, plot_bottom, color=GRID, width=1.5)
        canvas.text(
            x,
            plot_bottom + 27,
            f"{tick / 1000:.0f}",
            20,
            color=MUTED,
            anchor="middle",
        )

    bar_height = 43
    row_gap = 25
    for row, contributor in enumerate(display_order):
        y = plot_top + row * (bar_height + row_gap)
        value = totals[contributor]
        width = plot_width * value / maximum
        canvas.text(
            plot_left - 17,
            y + bar_height / 2,
            CONTRIBUTOR_LABELS[contributor],
            20,
            anchor="end",
        )
        canvas.rect(
            plot_left,
            y,
            max(width, 3),
            bar_height,
            fill=CONTRIBUTOR_COLORS[contributor],
        )
        if contributor == "Human Researcher":
            canvas.circle(
                plot_left + width,
                y + bar_height / 2,
                6,
                fill=CONTRIBUTOR_COLORS[contributor],
            )
        canvas.text(
            plot_left + max(width, 3) + 12,
            y + bar_height / 2,
            f"{value / 1000:.1f}k",
            19,
            color=INK,
            bold=True,
            anchor="start",
        )
    canvas.text(
        (plot_left + plot_right) / 2,
        plot_bottom + 59,
        "Total words (thousands)",
        20,
        anchor="middle",
    )


def _render_panel(
    output_dir: Path,
    stem: str,
    title: str,
    base_width: float,
    base_height: float,
    renderer,
) -> tuple[Path, Path]:
    drawing = VectorDrawing(base_width, base_height, title)
    canvas = ScaledCanvas(
        drawing, 0, 0, base_width, base_height, base_width, base_height
    )
    renderer(canvas)
    svg_path = output_dir / f"{stem}.svg"
    pdf_path = output_dir / f"{stem}.pdf"
    drawing.save_svg(svg_path)
    drawing.save_pdf(pdf_path)
    return svg_path, pdf_path


def _write_counts_csv(
    output_path: Path,
    counts: Mapping[str, Mapping[str, int]],
) -> None:
    percentages = _phase_percentages(counts)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["phase", "contributor", "words", "phase_pct"],
        )
        writer.writeheader()
        for phase in PHASE_ORDER:
            for contributor in CONTRIBUTOR_ORDER:
                writer.writerow(
                    {
                        "phase": phase,
                        "contributor": contributor,
                        "words": counts[phase][contributor],
                        "phase_pct": f"{percentages[phase][contributor]:.4f}",
                    }
                )


def _write_summary_json(
    output_path: Path,
    counts: Mapping[str, Mapping[str, int]],
) -> None:
    totals = _contributor_totals(counts)
    phase_percentages = _phase_percentages(counts)
    payload = {
        "phase_counts": counts,
        "contributor_totals": totals,
        "human_total": totals["Human Researcher"],
        "agent_total": sum(
            value
            for contributor, value in totals.items()
            if contributor != "Human Researcher"
        ),
        "highlight_percentages": {
            "project_specification_pi": phase_percentages[
                "project_specification"
            ]["Principal Investigator"],
            "tools_selection_pi": phase_percentages["tools_selection"][
                "Principal Investigator"
            ],
            "execution_planning_pi": phase_percentages["execution_planning"][
                "Principal Investigator"
            ],
            "iteration1_experimental_design": phase_percentages[
                "iteration1_discussion"
            ]["Experimental Design and Evidence Synthesis Scientist"],
        },
    }
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def generate_workflow_analysis_figures(
    phase_counts: Mapping[str, Mapping[str, int]] | None = None,
    output_dir: str | Path = Path("figures/workflow_analysis"),
) -> dict[str, Path]:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    counts = _normalise_counts(phase_counts)

    outputs: dict[str, Path] = {}
    outputs["counts_csv"] = output_dir / "workflow_word_counts.csv"
    outputs["summary_json"] = output_dir / "workflow_analysis_summary.json"
    _write_counts_csv(outputs["counts_csv"], counts)
    _write_summary_json(outputs["summary_json"], counts)

    a_svg, a_pdf = _render_panel(
        output_dir,
        "Figure_4a_search_funnel",
        "Stage-wise narrowing of the experimental search space",
        1600,
        430,
        _draw_search_funnel,
    )
    b_svg, b_pdf = _render_panel(
        output_dir,
        "Figure_4b_phase_composition",
        "Role composition across workflow phases",
        900,
        700,
        lambda canvas: _draw_phase_composition(canvas, counts),
    )
    c_svg, c_pdf = _render_panel(
        output_dir,
        "Figure_4c_contributor_totals",
        "Cumulative discussion contribution",
        900,
        700,
        lambda canvas: _draw_contributor_totals(canvas, counts),
    )
    outputs.update(
        {
            "panel_a_svg": a_svg,
            "panel_a_pdf": a_pdf,
            "panel_b_svg": b_svg,
            "panel_b_pdf": b_pdf,
            "panel_c_svg": c_svg,
            "panel_c_pdf": c_pdf,
        }
    )

    combined = VectorDrawing(
        1600,
        1090,
        "Workflow efficiency and human-agent collaboration",
    )
    _draw_search_funnel(
        ScaledCanvas(combined, 0, 0, 1600, 430, 1600, 430)
    )
    _draw_phase_composition(
        ScaledCanvas(combined, 0, 430, 800, 660, 900, 700), counts
    )
    _draw_contributor_totals(
        ScaledCanvas(combined, 800, 430, 800, 660, 900, 700), counts
    )
    outputs["combined_svg"] = output_dir / "Figure_4_workflow_analysis.svg"
    outputs["combined_pdf"] = output_dir / "Figure_4_workflow_analysis.pdf"
    combined.save_svg(outputs["combined_svg"])
    combined.save_pdf(outputs["combined_pdf"])
    return outputs


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Draw the workflow-efficiency and human-agent analysis figure."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("protein_design/figures/workflow_analysis"),
    )
    parser.add_argument(
        "--counts-json",
        type=Path,
        help="Optional JSON file containing phase-to-contributor word counts.",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    counts = None
    if args.counts_json:
        counts = json.loads(args.counts_json.read_text(encoding="utf-8"))
    outputs = generate_workflow_analysis_figures(counts, args.output_dir)
    for name, path in outputs.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()


