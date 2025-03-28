# -*- coding: utf-8 -*-
#
# The Sphinx config values used in the CodeQL documentation that is published
# at codeql.github.com/docs
#
# Note that not all possible configuration values are present in this file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.
#
# For details of all possible config values,
# see https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# -- GENERAL CONFIG VALUES ------------------------------------------------

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = '.rst'

# The master toctree document.
master_doc = 'contents'

# General information about the project.
project = u'CodeQL documentation'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'CodeQL'

# Output file base name for HTML help builder.
htmlhelp_basename = 'CodeQL'

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# The encoding of source files.
source_encoding = 'utf-8-sig'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# The default language for syntax highlighting. We need to explicitly set this to "none",
# otherwise Sphinx tries to highlight any unlabeled code samples as "python3".
# See https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-highlight_language.

highlight_language = "none"

# Import the QL Lexer to use for syntax highlighting
import os
import sys

import sphinx as sphinx_mod


def setup(sphinx):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from qllexer import QLLexer
    sphinx.add_lexer("ql", QLLexer() if sphinx_mod.version_info[0] <= 3 else QLLexer)

# The version of CodeQL for the current release you're documenting, acts as replacement for
# |version| and |release|. Not currently used.

# The short X.Y version.
# version = u'3.0'
# The full version, including alpha/beta/rc tags.
# release = u'3.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# -- Global HTML configuration -------------------------------------

# The theme to use for HTML pages. See  https://github.com/bitprophet/alabaster/blob/master/alabaster/static/alabaster.css_t
# Many of the built-in theme styles are overridden by the static stylesheets in html_static_path.
html_theme = 'alabaster'

# HTML theme options used to customize the look and feel of the docs.
html_theme_options = {'font_size': '16px',
                      'body_text': '#333',
                      'link': '#2F1695',
                      'link_hover': '#2F1695',
                      'show_powered_by': False,
                      # 'nosidebar':True,
                      'head_font_family': '-apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji"',
                      "sidebar_width": "330px",
                      'page_width': '1130px'
                      }

# Path to the folder that contains the project's HTML template
# templates_path = ['_templates']

# Path to the folder that contains static stylesheets
# html_static_path = ['_static']

# Copy the static landing page for codeql.github.com/docs when building this sphinx project
html_extra_path = ['index.html']

html_favicon = 'images/site/favicon.ico'

# Exclude these paths from being built by Sphinx
exclude_patterns = ['vale*', '_static', '_templates', 'reusables', 'images', 'support', 'ql-training', 'query-help', '_build', '*.py*', 'README.rst', 'codeql-for-visual-studio-code']
