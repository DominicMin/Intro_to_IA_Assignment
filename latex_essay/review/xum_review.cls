\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{xum_review}[2024/01/01 Xiamen University Malaysia Review Template]

% 基于article类
\LoadClass[a4paper,12pt]{article}

% 必需的包
\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{geometry}
\RequirePackage{fancyhdr}
\RequirePackage{setspace}
\RequirePackage{parskip}
\RequirePackage{url}
\RequirePackage{tocloft}
\RequirePackage[natbibapa]{apacite}
\RequirePackage{etoolbox}
\RequirePackage{lastpage}
\RequirePackage[colorlinks=true,linkcolor=black,citecolor=black,urlcolor=cyan]{hyperref}

% 超链接设置
\hypersetup{
    bookmarks=true,
    pdftitle={Review},
    pdfauthor={Xiamen University Malaysia}
}

% 页面设置
\geometry{
    top=2.5cm,
    bottom=2.5cm,
    left=2.5cm,
    right=2.5cm,
    headheight=15pt
}

% 页眉页脚设置
\pagestyle{fancy}
\fancyhf{}
\fancyhead[C]{XIAMEN UNIVERSITY MALAYSIA}
\fancyfoot[C]{Page \thepage\ of \pageref{LastPage}}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% 首页样式
\fancypagestyle{plain}{
    \fancyhf{}
    \fancyhead[C]{XIAMEN UNIVERSITY MALAYSIA}
    \fancyfoot[C]{}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
}

% 行距设置为1.5倍
\onehalfspacing

% 段落设置
\setlength{\parskip}{0.5\baselineskip}
\setlength{\parindent}{0.5in}

% 标题格式设置
\renewcommand{\maketitle}{
    \begin{center}
        {\LARGE\bfseries\@title\par}
        \vspace{1em}
        {\large\@author\par}
        \vspace{0.5em}
        {\large\@date\par}
    \end{center}
    \vspace{2em}
}

% 目录格式
\renewcommand{\contentsname}{Contents}

% 目录中的点线设置
\renewcommand{\cftsecleader}{\cftdotfill{\cftdotsep}}
\renewcommand{\cftsubsecleader}{\cftdotfill{\cftdotsep}}
\renewcommand{\cftsubsubsecleader}{\cftdotfill{\cftdotsep}}

% 引用格式设置
\bibliographystyle{apacite}
\renewcommand{\refname}{References}

% 将References添加到目录
\renewcommand{\bibsection}{\section*{\refname}\addcontentsline{toc}{section}{\refname}}

% 节标题格式
\renewcommand{\section}{\@startsection{section}{1}{\z@}%
    {-3.5ex \@plus -1ex \@minus -.2ex}%
    {2.3ex \@plus.2ex}%
    {\normalfont\Large\bfseries}}

\renewcommand{\subsection}{\@startsection{subsection}{2}{\z@}%
    {-3.25ex\@plus -1ex \@minus -.2ex}%
    {1.5ex \@plus .2ex}%
    {\normalfont\large\bfseries}}

\renewcommand{\subsubsection}{\@startsection{subsubsection}{3}{\z@}%
    {-3.25ex\@plus -1ex \@minus -.2ex}%
    {1.5ex \@plus .2ex}%
    {\normalfont\normalsize\bfseries}}

% 图表标题格式
\RequirePackage{caption}
\captionsetup{
    font=small,
    labelfont=bf,
    textfont=it,
    margin=10pt
}

\endinput 