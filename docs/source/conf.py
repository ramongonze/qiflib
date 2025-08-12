import os
import sys
from datetime import datetime

# -- Path setup: ensure "src" is on sys.path -------------------------------
# Repo root / docs / source / conf.py -> two levels up gets repo root
ROOT = os.path.abspath(os.path.join(__file__, "..", "..", ".."))
SRC = os.path.join(ROOT, "src")
sys.path.insert(0, SRC)

# -- Project information ----------------------------------------------------
project = "qiflib"
author = "Ramon Gonçalves Gonze"
copyright = f"{datetime.now():%Y}, {author}"
# If you keep a __version__ in qiflib/__init__.py, you can import it:
try:
    from qiflib import __version__ as version
except Exception:
    version = ""
release = version

# -- General configuration --------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",            # Google/NumPy docstrings
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx_autodoc_typehints",       # nice type hints in docs
    "myst_parser",                    # optional: Markdown support
]
autosummary_generate = True
autodoc_typehints = "description"     # cleaner signatures

# Napoleon settings for Google/NumPy-style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_use_ivar = True           # allow "Attributes:" / :ivar: to become attributes
napoleon_attr_annotations = True

# Nice display of type hints
autodoc_typehints = "description"   # or "both"

templates_path = ["_templates"]
exclude_patterns = []

# MyST (Markdown) tweaks (optional)
myst_enable_extensions = ["colon_fence", "deflist"]

# Intersphinx (optional)
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None)
}

# -- HTML output ------------------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 4,
}

# Optional: if you have modules that are heavy to import, mock them
autodoc_mock_imports = ["numpy"]
