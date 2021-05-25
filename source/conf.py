# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
print(os.path.abspath('.'))
import sphinx_rtd_theme
from sphinx.locale import _
from _static.imgs.hidden_code_block import HiddenCodeBlock
from _static.imgs.hidden_code_block import depart_hcb_html
from _static.imgs.hidden_code_block import visit_hcb_html
from _static.imgs.hidden_code_block import hidden_code_block

# -- Project information -----------------------------------------------------

project = 'Mozaiti'
copyright = '20210430, mozaiti'
author = 'mozaiti'

# The full version, including alpha/beta/rc tags
release = 'v1'

html_logo = './_static/imgs/logo.gif'

# -- General configuration ---------------------------------------------------

# source_suffix = '.rst'
source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}
source_suffix = ['.rst', '.md']

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'recommonmark',
    'sphinx_markdown_tables',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx_togglebutton',
    'sphinx.ext.todo',
    #'_static.imgs.hidden_code_block'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

exclude_patterns = ['_build']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

html_theme_options = {
    'navigation_depth': 6,
}

todo_include_todos = True
#todo_emit_warnings = True

#html_context = {
#    'display_github': True,
#    'github_user': 'buskill',
#    'github_repo': 'buskill-app',
#    'github_version': 'master/docs/',
#}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Extensions to theme docs
def setup(app):
    from sphinx.domains.python import PyField
    from sphinx.util.docfields import Field
    
    app.add_directive('hidden-code-block', HiddenCodeBlock)
    app.add_node(hidden_code_block, html=(visit_hcb_html, depart_hcb_html))

    app.add_object_type(
        'confval',
        'confval',
        objname='configuration value',
        indextemplate='pair: %s; configuration value',
        doc_field_types=[
            PyField(
                'type',
                label=_('Type'),
                has_arg=False,
                names=('type',),
                bodyrolename='class'
            ),
            Field(
                'default',
                label=_('Default'),
                has_arg=False,
                names=('default',),
            ),
        ]
    )
