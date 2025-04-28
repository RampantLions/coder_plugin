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
    "sphinx.ext.autodoc", # Automatically document docstrings
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx", # Link to other projects' documentation
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode", # Add links to highlighted source code
    "sphinx.ext.githubpages",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon", # Support for NumPy and Google style docstrings
    "sphinx_autodoc_typehints",
    'sphinx.ext.todo',  # Support for TODO entries
    "sphinx_copybutton",
]

templates_path = ['_templates']
exclude_patterns = []

autodoc_class_attributes = False

# Order members as they appear in the source code
autodoc_member_order = 'bysource'
autosummary_generate = True

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
napoleon_google_docstring = True     # Enable Google-style docstrings
napoleon_numpy_docstring = True      # Enable NumPy-style docstrings

# todo config
todo_include_todos = True            # Show TODO entries in the output

# intersphinx config
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# -- Custom autodoc-skip-member handler --------------------------------------

def skip_public_class_vars(app, what, name, obj, skip, options):
    """Skip class variables that are manually documented to avoid duplicate entries."""
    if what == "class" and name in {"name", "parent_group", "plugin_group"}:
        return True
    return skip

def setup(app):
    app.connect("autodoc-skip-member", skip_public_class_vars)

