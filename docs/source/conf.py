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

from importlib.metadata import version as pkg_version
release = pkg_version("qiflib")

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

myst_enable_extensions = [
    "dollarmath",      # <-- enables $ and $$ math blocks
    "amsmath",         # optional, for more LaTeX environments
    "colon_fence",
    "deflist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

# Nice display of type hints
autodoc_typehints = "description"   # or "both"

templates_path = ["_templates"]
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Intersphinx (optional)
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None)
}

# -- HTML output ------------------------------------------------------------
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"

# Optional: if you have modules that are heavy to import, mock them
autodoc_mock_imports = ["numpy"]
