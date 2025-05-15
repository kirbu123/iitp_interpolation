"""Sphinx configuration for IITP_INTERPOLATION documentation."""

import os
import sys
from datetime import datetime

# Add project directory to Python path
sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------
project = "IITP_INTERPOLATION"
author = "Bunin Kirill"
copyright = f"{datetime.now().year}, {author}"

# -- General configuration ---------------------------------------------------
extensions = [
    'autoapi.extension',          # Automatic API documentation
    'sphinx.ext.autodoc',         # Include documentation from docstrings
    'sphinx.ext.napoleon',        # Support for Google/Numpy docstrings
    'sphinx.ext.viewcode',        # Add links to source code
    'sphinx.ext.intersphinx',     # Link to other projects' documentation
    'sphinx.ext.mathjax',        # Render math
    'sphinx_copybutton',         # Add copy button to code blocks
    'sphinx_design',             # Better design elements
    'sphinx.ext.autosummary',    # Generate autosummary
    'sphinx.ext.githubpages',    # For GitHub Pages integration
]

# AutoAPI configuration
autoapi_dirs = ['../src/iitp_interpolation/techniques']
autoapi_options = [
    'members',
    'undoc-members',
    'show-inheritance',
    'show-module-summary',
    'special-members',
    'imported-members',
]
autoapi_python_class_content = 'both'  # Show both class and __init__ docstrings
autoapi_member_order = 'bysource'     # Keep original source ordering

# Napoleon settings for docstring parsing
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True

# Autodoc settings
autodoc_typehints = 'description'
autodoc_default_options = {
    'members': True,
    'show-inheritance': True,
    'special-members': '__init__',
}
autodoc_mock_imports = []  # List any problematic imports to mock

# -- Options for HTML output -------------------------------------------------
html_theme = 'furo'  # Modern, clean theme (install with: pip install furo)
# Alternative good themes: 'sphinx_book_theme', 'pydata_sphinx_theme'


html_theme_options = {
    'source_repository': 'https://github.com/kirbu123/iitp_interpolation',
    'source_branch': 'main',
    'source_directory': 'docs/',
}


# Add any paths that contain custom static files (e.g., style sheets)
html_static_path = ['_static']

# Custom CSS
html_css_files = [
    'custom.css',
]

# Favicon
html_favicon = '_static/favicon.ico'

# Logo
html_logo = '_static/logo.png'

# -- Additional settings ------------------------------------------------------
# Enable numbered figures
numfig = True

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/', None),
}

# Don't show "View page source" link
html_show_sourcelink = False

# Control documentation version warning
versionwarning_messages = {
    'latest': 'This is the development version.',
}
versionwarning_admonition_type = 'tip'