"""
Utility helpers shared across the library.

Submodules:
- probability: probability utilities (distributions, normalization, etc.)
- types: common type aliases and protocol definitions
"""

from typing import TYPE_CHECKING

from .probability import check_prob_distribution
from .types import (
    is_int,
    is_float,
    is_string,
    is_list,
    is_dict,
    is_set,
    is_numpy_array,
    is_2d_list_matrix,
    is_2d_numpy_matrix,
    is_function,
)

__all__ = [
    "check_prob_distribution",
    "is_int",
    "is_float",
    "is_string",
    "is_list",
    "is_dict",
    "is_set",
    "is_numpy_array",
    "is_2d_list_matrix",
    "is_2d_numpy_matrix",
    "is_function",
]

if TYPE_CHECKING:  # pragma: no cover
    from . import probability as probability  # noqa: F401
    from . import types as types  # noqa: F401


def __getattr__(name: str):
    if name in __all__:
        import importlib
        return importlib.import_module(f"{__name__}.{name}")
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return sorted(list(globals().keys()) + __all__)
