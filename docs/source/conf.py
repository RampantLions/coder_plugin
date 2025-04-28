# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Coder Plugin'
copyright = '2025, Joshua Wiechman'
author = 'Joshua Wiechman'

# Dynamically get version from package metadata
try:
    from coder_plugin import __version__ as release
except ImportError:
    release = '0.0.1'

version = release

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
]

templates_path = ['_templates']
exclude_patterns = []

autosummary_generate = True
autodoc_class_attributes = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
# html_theme = 'alabaster'
# html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".venv"]

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
    'member-order': 'bysource',
    'special-members': '__init__',
}

# Napoleon settings
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True

# -- Custom autodoc-skip-member handler --------------------------------------

def skip_public_class_vars(app, what, name, obj, skip, options):
    """Skip class variables that are manually documented to avoid duplicate entries."""
    if what == "class" and name in {"name", "parent_group", "plugin_group"}:
        return True
    return skip

def setup(app):
    app.connect("autodoc-skip-member", skip_public_class_vars)

