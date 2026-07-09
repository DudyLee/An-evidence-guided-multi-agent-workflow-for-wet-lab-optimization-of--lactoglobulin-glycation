"""Shared manuscript figure palette anchored to Fig. 2b.

Fig. 2b is treated as the visual anchor for the manuscript. The core colors
below are copied from ``draw_fig2b_evidence_components.py``; the numbered
``color`` aliases are kept for backward compatibility with existing plotting
scripts, but they now resolve to blue/green/neutral variants from the Fig. 2b
system rather than to a separate warm palette.
"""

from __future__ import annotations

FIG2B_ANCHOR = {
    "ink": "#202124",
    "muted": "#5F6368",
    "blue": "#2F69B1",
    "blue_dark": "#143E7D",
    "blue_light": "#EAF3FF",
    "cyan": "#49C2D9",
    "green": "#4E7D3A",
    "grid": "#DDE7F5",
    "grey_fill": "#F7F9FC",
    "grey_line": "#A8ADB5",
    "white": "#FFFFFF",
}

PALETTE = {
    "color1": FIG2B_ANCHOR["blue_dark"],
    "color2": FIG2B_ANCHOR["blue"],
    "color3": FIG2B_ANCHOR["cyan"],
    "color4": FIG2B_ANCHOR["green"],
    "color5": "#6F9E5A",
    "color6": FIG2B_ANCHOR["blue_light"],
    "color7": FIG2B_ANCHOR["grid"],
    "color8": FIG2B_ANCHOR["grey_fill"],
    "color9": FIG2B_ANCHOR["grey_line"],
    "color10": "#315924",
    "color11": "#0F2F5E",
    "blue_dark": FIG2B_ANCHOR["blue_dark"],
    "blue": FIG2B_ANCHOR["blue"],
    "blue_light": FIG2B_ANCHOR["blue_light"],
    "cyan": FIG2B_ANCHOR["cyan"],
    "green": FIG2B_ANCHOR["green"],
    "green_dark": "#315924",
    "green_light": "#DCEAD4",
    "grid_blue": FIG2B_ANCHOR["grid"],
    "grey_fill": FIG2B_ANCHOR["grey_fill"],
    "grey_line": FIG2B_ANCHOR["grey_line"],
    "muted": FIG2B_ANCHOR["muted"],
}

INK = FIG2B_ANCHOR["ink"]
MUTED = FIG2B_ANCHOR["muted"]
GRID = FIG2B_ANCHOR["grid"]
WHITE = FIG2B_ANCHOR["white"]


def _hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16)


def blend(foreground: str, background: str = WHITE, amount: float = 0.72) -> str:
    """Blend foreground toward background; larger amount makes a lighter tint."""

    fr, fg, fb = _hex_to_rgb(foreground)
    br, bg, bb = _hex_to_rgb(background)
    rgb = (
        round(fr * (1 - amount) + br * amount),
        round(fg * (1 - amount) + bg * amount),
        round(fb * (1 - amount) + bb * amount),
    )
    return "#{:02X}{:02X}{:02X}".format(*rgb)
