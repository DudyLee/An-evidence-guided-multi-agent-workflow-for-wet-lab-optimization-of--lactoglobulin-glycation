"""Virtual Lab package."""

from virtual_lab.__about__ import __version__
from virtual_lab.agent import Agent


__all__ = [
    "__version__",
    "Agent",
    "run_meeting",
]


def __getattr__(name: str):
    """Load optional runtime helpers only when they are requested."""
    if name == "run_meeting":
        from virtual_lab.run_meeting import run_meeting

        return run_meeting
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
