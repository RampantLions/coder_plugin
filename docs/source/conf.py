# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import shutil
sys.path.insert(0, os.path.abspath('../../src'))

# -- Path setup --------------------------------------------------------------

__location__ = os.path.dirname(__file__)

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.join(__location__, "../src"))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Coder Plugin'
copyright = '2025, Joshua Wiechman'
author = 'Joshua Wiechman'
repository = "https://github.com/RampantLions/coder_plugin/"

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
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx", # Link to other projects' documentation
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode", # Add links to highlighted source code
    "sphinx.ext.githubpages",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon", # Support for NumPy and Google style docstrings
    'sphinx.ext.todo',
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
    "sphinx-prompt",
    "sphinxemoji.sphinxemoji",
    "sphinx_github_role"
]

templates_path = ['_templates']
exclude_patterns = []
source_suffix = ".rst"
autodoc_class_attributes = False

# Order members as they appear in the source code
autodoc_member_order = 'bysource'
autosummary_generate = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_theme = "furo"
html_theme = 'piccolo_theme'
# html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".venv"]

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
    'member-order': 'bysource',
    'special-members': '__init__',
}

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"
pygments_dark_style = "monokai"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {
#     "sidebar_hide_name": True,
#     "navigation_with_keys": True,
#     "light_css_variables": {
#         "color-brand-primary": "#2980B9",
#         "color-brand-content": "#005CA0",
#         "color-brand-muted": "#E7F2FA",
#         "color-brand-logo-background": "#156EAD",
#     },
#     "dark_css_variables": {
#         "color-brand-content": "#0A93FB",
#         "color-brand-muted": "#00091A",
#     },
# }

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = "gfx/sidebar.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = "gfx/logo.ico"

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Napoleon settings
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_google_docstring = True     # Enable Google-style docstrings
napoleon_numpy_docstring = True      # Enable NumPy-style docstrings

todo_include_todos = True            # Show TODO entries in the output

# -- Options for LaTeX output ------------------------------------------------

# latex_elements = {
#     # The paper size ("letterpaper" or "a4paper").
#     # "papersize": "letterpaper",
#     # The font size ("10pt", "11pt" or "12pt").
#     # "pointsize": "10pt",
#     # Additional stuff for the LaTeX preamble.
#     # "preamble": "",
# }

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
# latex_documents = [
#     (
#         "index",
#         "user_guide.tex",
#         "PyScaffold Documentation",
#         "PyScaffold Contributors",
#         "manual",
#     )
# ]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = "gfx/logo.png"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True

# -- External mapping --------------------------------------------------------
python_version = ".".join(map(str, sys.version_info[0:2]))

# intersphinx config
intersphinx_mapping = {
    "python": ("https://docs.python.org/" + python_version, None),
}
extlinks = {
    "issue": (f"{repository}/issues/%s", "issue #%s"),
    "pr": (f"{repository}/pull/%s", "PR #%s"),
    "discussion": (f"{repository}/discussions/%s", "discussion #%s"),
    "pypi": ("https://pypi.org/project/%s", "%s"),
    # "github" is handled by sphinx_github_role
}

# intersphinx_mapping = {
#     "sphinx": ("https://www.sphinx-doc.org/en/master", None),
#     "python": ("https://docs.python.org/" + python_version, None),
#     "matplotlib": ("https://matplotlib.org", None),
#     "numpy": ("https://numpy.org/doc/stable", None),
#     "sklearn": ("https://scikit-learn.org/stable", None),
#     "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
#     "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
#     "setuptools": ("https://setuptools.pypa.io/en/stable/", None),
#     "configupdater": ("https://configupdater.readthedocs.io/en/stable/", None),
# }
# extlinks = {
#     "issue": (f"{repository}/issues/%s", "issue #%s"),
#     "pr": (f"{repository}/pull/%s", "PR #%s"),
#     "discussion": (f"{repository}/discussions/%s", "discussion #%s"),
#     "pypi": ("https://pypi.org/project/%s", "%s"),
#     # "github" is handled by sphinx_github_role
# }

# -- Custom autodoc-skip-member handler --------------------------------------

def skip_public_class_vars(app, what, name, obj, skip, options):
    """Skip class variables that are manually documented to avoid duplicate entries."""
    if what == "class" and name in {"name", "parent_group", "plugin_group"}:
        return True
    return skip

def setup(app):
    app.connect("autodoc-skip-member", skip_public_class_vars)

