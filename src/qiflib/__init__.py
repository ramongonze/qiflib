"""
qiflib — A tiny, focused Python library for Quantitative Information Flow (QIF): model secrets, channels, and analyze leakage via the g-vulnerability framework.

Keep this module import-light so packaging/docs don't pull heavy deps early.
"""

from typing import TYPE_CHECKING

__version__ = "1.0"  # keep version here if you like

__all__ = ["core", "util", "__version__"]

# Editor/typing help without importing heavy stuff at runtime
if TYPE_CHECKING:  # pragma: no cover
    from . import core as core  # noqa: F401
    from . import util as util  # noqa: F401


def __getattr__(name: str):
    """Lazy-load subpackages on first access (avoids importing numpy during build)."""
    if name in {"core", "util"}:
        import importlib
        return importlib.import_module(f"{__name__}.{name}")
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return sorted(list(globals().keys()) + __all__)
