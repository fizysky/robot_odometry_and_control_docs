# Configuration file for the Sphinx documentation builder.

import sys
import re
import subprocess, os
# If we are building locally, or the build on Read the Docs looks like a PR
# build, prefer to use the version of the theme in this repo, not the installed
# version of the theme.
def is_development_build():
    # PR builds have an interger version
    re_version = re.compile(r'^[\d]+$')
    if 'READTHEDOCS' in os.environ:
        version = os.environ.get('READTHEDOCS_VERSION', '')
        if re_version.match(version):
            return True
        return False
    return True

if is_development_build():
    sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.abspath('./demo/'))

import revitron_sphinx_theme
# -- Project information



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
    'revitron_sphinx_theme',
    "breathe",
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'revitron_sphinx_theme'
html_theme_path = ["../../", ]

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
# breathe_default_members = ('members', 'undoc-members', 'private-members' , 'protected-members')
