"""
Core QIF objects.

Submodules:
- channel: channel matrices / mechanisms
- gvulnerability: g-vulnerability and related leakage quantities
- hyper: hyper-distributions over secrets
- luncertainty: L-uncertainty measures
- secrets: priors / secret spaces
"""

from typing import TYPE_CHECKING

from .secrets import Secrets
from .channel import Channel
from .hyper import Hyper
from .gvulnerability import GVulnerability
from .luncertainty import LUncertainty

__all__ = ["Secrets", "Channel", "Hyper", "GVulnerability", "LUncertainty"]

if TYPE_CHECKING:  # pragma: no cover
    from . import channel as channel  # noqa: F401
    from . import gvulnerability as gvulnerability  # noqa: F401
    from . import hyper as hyper  # noqa: F401
    from . import luncertainty as luncertainty  # noqa: F401
    from . import secrets as secrets  # noqa: F401


def __getattr__(name: str):
    if name in __all__:
        import importlib
        return importlib.import_module(f"{__name__}.{name}")
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return sorted(list(globals().keys()) + __all__)
