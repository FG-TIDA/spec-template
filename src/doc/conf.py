import datetime
import fnmatch
import os
import shutil

# =============================================================================
# Basic Sphinx configuration
# =============================================================================

source_suffix = {'.rst': 'restructuredtext'}
master_doc = 'index'

# Files beginning with "_" are helper/template files and should not be built
# as standalone pages.
exclude_patterns = ['_*.rst', '*/_*.rst']

pygments_style = 'colorful'

# =============================================================================
# FG-TIDA Working Group Charter metadata
#
# When a new WG repository is created from this template, authors should
# update the values in this section.
# =============================================================================

project = '<WG acronym>'
release = '<charter version>'
html_title = '<WG acronym> Charter'
author = 'FG-TIDA'

numfig = True

# ---------------------------------------------------------------------------
# PDF filename
#
# A stable filename is used regardless of the WG name.
#
#   wg-charter.tex -> wg-charter.pdf
#
# This allows the GitHub Actions workflow to always know which file to copy.
# ---------------------------------------------------------------------------

latex_documents = [
    (
        master_doc,
        'wg-charter.tex',
        project,
        author,
        'manual',
    ),
]

# ---------------------------------------------------------------------------
# Cover metadata
#
# Example for a real WG:
#
# cover_title = 'WG1: Trust Frameworks'
# cover_series = 'FG-TIDA Working Group Charter'
# cover_subject = 'WG-TF'
# cover_subtitle = 'Charter version 1.0 — Approved'
# ---------------------------------------------------------------------------

cover_title = '<Full name of the Working Group>'
cover_series = 'FG-TIDA Working Group Charter'
cover_subject = '<WG acronym>'
cover_subtitle = '<Charter version and status>'

# =============================================================================
# Sphinx extensions
# =============================================================================

extensions = [
    'sphinxcontrib.httpdomain',
    'sphinxcontrib.plantuml',
    'sphinxcontrib.openapi',
    'sphinx_copybutton',
]

# =============================================================================
# PlantUML
# =============================================================================

plantuml = os.environ.get('PLANTUML', 'plantuml')
plantuml_output_format = 'svg'

# =============================================================================
# Templates and static files
# =============================================================================

templates_path = ['_templates']

html_static_path = [
    '_static',
    'images',
]

html_css_files = [
    'osia-furo.css',
]

html_js_files = [
    'osia-sidebar.js',
]

# =============================================================================
# Global reStructuredText substitutions
# =============================================================================

rst_prolog = '''

.. meta::
   :http-equiv=X-UA-Compatible: IE=9

.. |tick| unicode:: U+2714
   :trim:

.. |project| replace:: ''' + project + '''
.. |release| replace:: ''' + release + '''
.. |cover-title| replace:: ''' + cover_title + '''
.. |cover-series| replace:: ''' + cover_series + '''
.. |cover-subject| replace:: ''' + cover_subject + '''
.. |cover-subtitle| replace:: ''' + cover_subtitle + '''

.. role:: todo

.. raw:: html

   <style>

       .todo {
           background-color: #f3f375;
           font-style: italic;
       }

       .wy-table-responsive table td,
       .wy-table-responsive table th {
           white-space: normal !important;
       }

       .wy-table-responsive {
           overflow: visible !important;
       }

       tr th.head {
           background-color: #00A0DD;
           color: white;
       }

       li p {
           margin-top: 3px;
       }

       dl.py.function {
           margin-top: 20px;
       }

       dl dd p {
           margin: 0;
       }

       figcaption p {
           text-align: center !important;
       }

   </style>

'''

# =============================================================================
# HTML output configuration
# =============================================================================

html_theme = 'furo'

html_theme_options = {
    'sidebar_hide_name': False,
}

html_logo = 'images/TIDA_logo.png'

html_show_sourcelink = False

copyright = '<year>, International Telecommunication Union'

html_context = {
    'project': project,
    'version': release,
    'copyright': copyright,
}

html_last_updated_fmt = '%b %d, %Y'

html_extra_path = ['yaml']

# =============================================================================
# LaTeX / PDF output configuration
# =============================================================================

from sphinx.highlighting import PygmentsBridge
from pygments.formatters.latex import LatexFormatter


class CustomLatexFormatter(LatexFormatter):
    def __init__(self, **options):
        super().__init__(**options)
        self.verboptions = r'formatcom=\footnotesize'


PygmentsBridge.latex_formatter = CustomLatexFormatter


latex_elements = {

    'papersize': 'a4paper',

    'pointsize': '10pt',

    'figure_align': 'H',

    'preamble': u'''

\\usepackage{bbding,pifont}
\\usepackage{attachfile}

\\attachfilesetup{color=0 0.5 0.5}

\\DeclareUnicodeCharacter{2714}{\\Checkmark}

\\newcommand{\\DUroletodo}[1]{\\colorbox{yellow}{#1}}

\\usepackage{color}
\\usepackage{colortbl}

\\definecolor{tableheader}{rgb}{0,0.627,0.867}

\\usepackage{makeidx}
\\usepackage[columns=1]{idxlayout}

\\usepackage{draftwatermark}
\\SetWatermarkScale{0.5}

\\usepackage{tikz}
\\usetikzlibrary{positioning,calc}

\\definecolor{ituBg}{HTML}{2A2D31}
\\definecolor{ituRed}{HTML}{B91E1E}
\\definecolor{ituAccent}{HTML}{29ABE2}

''' + r'''

\renewcommand*{\sphinxstyletheadfamily}
    {\cellcolor{tableheader}\sffamily\color{white}}

\AtBeginDocument{%

  \renewcommand{\sphinxtableofcontents}{%
    \begingroup
      \parskip = 0mm
      \tableofcontents
    \endgroup
    \if@openright
      \cleardoublepage
    \else
      \clearpage
    \fi
  }%

  \title{FG-TIDA Working Group Charter}%

''' + r'''
  \release{''' + release + r'''}%
}

\makeatletter

\AtBeginDocument{%
  \let\tidaorigmakechapterhead\@makechapterhead
}

\newcommand{\tidahidenextchapterhead}{%
  \renewcommand{\@makechapterhead}[1]{%
    \global\let\@makechapterhead\tidaorigmakechapterhead
  }%
}

\makeatother

\newcommand{\tidaskipnextchapter}{%
  \let\tidaorigchapter\chapter
  \def\chapter##1{%
    \cleardoublepage%
    \let\chapter\tidaorigchapter%
  }%
}

\newcommand{\tidacenternextsection}{%
  \let\tidaorigsection\section

  \def\section##1{%

    \par
    \addvspace{1.5em}%

    \begin{center}
      {\normalfont\Large\bfseries ##1\par}
    \end{center}%

    \par
    \addvspace{0.5em}%

    \addcontentsline{toc}{section}{##1}%

    \let\section\tidaorigsection%
  }%
}

\newcommand{\tidacenternextsubsection}{%
  \let\tidaorigsubsection\subsection

  \def\subsection##1{%

    \par
    \addvspace{2.5em}%

    \begin{center}
      {\normalfont\large\bfseries ##1\par}
    \end{center}%

    \par
    \addvspace{1em}%

    \addcontentsline{toc}{subsection}{##1}%

    \let\subsection\tidaorigsubsection%
  }%
}

\newcommand{\tidafrontmatter}{%

  \setcounter{secnumdepth}{-1}%

  \pagestyle{plain}%

  \pagenumbering{roman}%
}

\newcommand{\tidamainmatter}{%

  \setcounter{secnumdepth}{2}%

  \setcounter{chapter}{0}%

  \pagestyle{normal}%

  \pagenumbering{arabic}%
}

''' + r'''

\newcommand{\coverTitle}{''' + cover_title + r'''}

\newcommand{\coverSeries}{''' +
cover_series.replace('–', '--') +
r'''}

\newcommand{\coverSubject}{''' +
cover_subject.replace('–', '--') +
r'''}

\newcommand{\coverSubtitle}{''' + cover_subtitle + r'''}

''' + r'''

% --------------------------------------------------------------------------
% FG-TIDA Working Group Charter cover
% --------------------------------------------------------------------------

\newcommand{\tidamaketitle}{%

  \begin{titlepage}

    \thispagestyle{empty}

    \begin{tikzpicture}[remember picture,overlay]

      % --------------------------------------------------------------------
      % Top-left banner
      % --------------------------------------------------------------------

      \node[
        anchor=north west,
        inner sep=0pt
      ]
      at ([xshift=1.5cm,yshift=-1.3cm]current page.north west)
      {
        \sffamily
        \Large
        \textcolor{ituAccent}{\textbf{ITU}}
        \textbf{Publications}
      };

      \node[
        anchor=north west,
        inner sep=0pt
      ]
      at ([xshift=1.5cm,yshift=-1.9cm]current page.north west)
      {
        \sffamily
        \normalsize
        FG-TIDA
      };

      % --------------------------------------------------------------------
      % Top-right banner
      % --------------------------------------------------------------------

      \node[
        anchor=north east,
        inner sep=0pt
      ]
      at ([xshift=-1.5cm,yshift=-1.3cm]current page.north east)
      {
        \sffamily
        \normalsize
        \textbf{International Telecommunication Union}
      };

      \node[
        anchor=north east,
        inner sep=0pt
      ]
      at ([xshift=-1.5cm,yshift=-1.9cm]current page.north east)
      {
        \sffamily
        \small
        Standardization Sector
      };

      % --------------------------------------------------------------------
      % Red horizontal banner
      % --------------------------------------------------------------------

      \fill[ituRed]
        ([yshift=-2.6cm]current page.north west)
        rectangle
        ([yshift=-2.95cm]current page.north east);

      % Downward red triangle

      \fill[ituRed]
        ([xshift=2cm,yshift=-2.95cm]current page.north west)
        --
        ([xshift=2.7cm,yshift=-2.95cm]current page.north west)
        --
        ([xshift=2.35cm,yshift=-3.4cm]current page.north west)
        --
        cycle;

      % --------------------------------------------------------------------
      % Document title
      % --------------------------------------------------------------------

      \node[
        anchor=north west,
        inner sep=0pt,
        text width=18cm
      ]
      at ([xshift=1.5cm,yshift=-4.8cm]current page.north west)
      {
        \sffamily
        \hyphenpenalty=10000
        \exhyphenpenalty=10000
        \sloppy

        {\huge Working Group Charter}\\[0.4cm]

        {\Huge\bfseries \coverTitle}\\[1.2cm]

        {\Large \coverSeries}\\[0.5cm]

        {\Large \coverSubject}
      };

      % --------------------------------------------------------------------
      % Separator
      % --------------------------------------------------------------------

      \draw[
        black,
        line width=0.4pt
      ]
      ([xshift=1.5cm,yshift=-12.5cm]current page.north west)
      --
      ([xshift=-1.5cm,yshift=-12.5cm]current page.north east);

      % --------------------------------------------------------------------
      % Charter version / status
      % --------------------------------------------------------------------

      \node[
        anchor=north west,
        inner sep=0pt,
        text width=18cm
      ]
      at ([xshift=1.5cm,yshift=-13cm]current page.north west)
      {
        \sffamily
        \hyphenpenalty=10000
        \exhyphenpenalty=10000
        \sloppy
        \LARGE
        \bfseries
        \coverSubtitle
      };

      % --------------------------------------------------------------------
      % FG-TIDA logo
      % --------------------------------------------------------------------

      \node[
        anchor=south east,
        inner sep=0pt
      ]
      at ([xshift=-1.5cm,yshift=1.5cm]current page.south east)
      {
        \includegraphics[width=2.5cm]{tida-logo.png}
      };

    \end{tikzpicture}

  \end{titlepage}

  \cleardoublepage

  \setcounter{footnote}{0}

  \relax
  \let\maketitle\relax
}

''',

    'maketitle': r'\tidamaketitle\tidafrontmatter',

    'tableofcontents': '',

    'atendofbody': '',

    'classoptions': ',english,openany,oneside',
}

# =============================================================================
# Draft watermark
# =============================================================================

latex_elements['preamble'] += '\\SetWatermarkText{}'

# =============================================================================
# Copy images into the LaTeX build directory
# =============================================================================


def setup(app):
    """
    Copy PDF and PNG images from src/doc/images into the active Sphinx output
    directory.

    This keeps images available for both HTML and LaTeX/PDF builds.
    """

    os.makedirs(app.outdir, exist_ok=True)

    images_directory = os.path.join(app.srcdir, 'images')

    if not os.path.isdir(images_directory):
        return

    for root, dirs, files in os.walk(images_directory):

        for pattern in ('*.pdf', '*.png'):

            for filename in fnmatch.filter(files, pattern):

                source = os.path.join(root, filename)
                destination = os.path.join(app.outdir, filename)

                shutil.copy(source, destination)
