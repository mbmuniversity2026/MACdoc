# Configuration file for the Sphinx documentation builder.
# -- Project information -----------------------------------------------------

project = 'MAC -- MBM AI Cloud'
copyright = '2026, MBM University (Mugneeram Bangur Memorial University), Jodhpur'
author = 'CSE Department, MBM University'
release = '2.0.0'
version = '2.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/screenshots/mac_logo.png'
html_favicon = '_static/screenshots/mac_logo.png'

html_theme_options = {
    'logo_only': False,
    'prev_next_buttons_location': 'both',
    'style_external_links': True,
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False,
}

html_context = {
    'display_github': True,
    'github_user': 'mbmuniversity2026',
    'github_repo': 'MACdoc',
    'github_version': 'main',
    'conf_py_path': '/',
}

# -- Extension configuration -------------------------------------------------

todo_include_todos = True

# -- Custom CSS for MAC theme matching + responsiveness ----------------------

html_css_files = [
    'custom.css',
]
