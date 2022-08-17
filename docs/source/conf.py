# Configuration file for the Sphinx documentation builder.

# -- Project information

import subprocess, os

project = 'Robot\n odometry & control'
copyright = '2022, Piotr'
author = 'Piotr'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    "breathe",
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'collapse_navigation': False,
    'logo_only': True,
    'sticky_navigation': True,
    'navigation_depth': -1,
}
html_logo = "images/logoW.png"


# -- Options for EPUB output
epub_show_urls = 'footnote'

breathe_projects = {"My Project": "../xml/"}
breathe_default_project = "My Project"
