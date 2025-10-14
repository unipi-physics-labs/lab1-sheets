%
% This is shamelessy stolen and adapted from the arstexnica class by the
% Italian TeX user group (GUIT):
% http://www.guit.sssup.it/arstexnica/
%
% All the mistakes are my responsibility!
% Luca Baldini <luca.baldini@pi.infn.it>
%

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{lab1-article}[2013/03/01 v0.0.1 Document class for PLS]

\def\@pjp{paper}
\AtEndOfClass{%
  \let\tableofcontents\relax
  \def\@openarticle{}
  \def\@closearticle{\@makecolophon}
}

\LoadClass[a4paper,twocolumn,twoside,10pt]{article}
\RequirePackage{dblfloatfix}
\RequirePackage{balance}
\RequirePackage{textcomp}
\RequirePackage{geometry}
\geometry{%
   hmargin=2.25cm,
   vmargin={2.cm,2.5cm},
   bindingoffset=0mm,
   columnsep=15pt
}

\usepackage{hyperref}
\usepackage{amsmath}

\newif\if@fvrbex
\newif\if@hyperref
\def\@part[#1]#2{%
    \ifnum \c@secnumdepth >\m@ne
      \refstepcounter{part}%
      \addcontentsline{toc}{part}{\thepart\hspace{1em}#1}%
    \else
      \addcontentsline{toc}{part}{#1}%
    \fi
    {\parindent \z@ \raggedright
     \interlinepenalty \@M
     \normalfont
     \ifnum \c@secnumdepth >\m@ne
       \Large\bfseries \partname\nobreakspace\thepart:
       \par\nobreak
     \fi
%      \huge \bfseries #2%
     #2%
     \markboth{}{}\par}%
    \nobreak
    \vskip 3ex
    \@afterheading}
\def\@spart#1{%
    {\parindent \z@ \raggedright
     \interlinepenalty \@M
     \normalfont
%      \huge \bfseries #1\par}%
     \Large \bfseries #1\par}%
     \nobreak
     \vskip 3ex
     \@afterheading}
\renewcommand{\section}{\@startsection{section}{1}{\z@}%
  {-1\baselineskip \@plus -.2ex \@minus -.1ex}{.5\baselineskip \@plus .2ex}{\normalfont\large\scshape}}
\renewcommand{\subsection}{\@startsection{subsection}{2}{\z@}%
   {-0.5\baselineskip \@plus -.2ex \@minus -.1ex}{1ex \@plus .2ex}{\normalfont\normalsize\scshape}}
\renewcommand{\subsubsection}{\@startsection{subsubsection}{3}{\z@}%
    {-0.5\baselineskip \@plus -.2ex \@minus -.1ex}{1ex \@plus .2ex}{\normalfont\normalsize\itshape}}
\renewcommand{\paragraph}{\@startsection{paragraph}{4}{\z@}%
    {-0.5\baselineskip \@plus -.2ex \@minus -.1ex}{1ex \@plus .2ex}{\normalfont\normalsize\scshape}}
\renewcommand{\subparagraph}{\@startsection{subparagraph}{5}{\z@}%
    {-0.5\baselineskip \@plus -.2ex \@minus -.1ex}{1ex \@plus .2ex}{\normalfont\normalsize\itshape}}

\newcommand{\pretitle}[1]{\def\@atpretitle{#1}}
\newcommand{\posttitle}[1]{\def\@atposttitle{#1}}
\newcommand{\preauthor}[1]{\def\@atpreauthor{#1}}
\newcommand{\postauthor}[1]{\def\@atpostauthor{#1}}
\newcommand{\predate}[1]{\def\@atpredate{#1}}
\newcommand{\postdate}[1]{\def\@atpostdate{#1}}

\pretitle{%
  \begin{center}\LARGE\scshape
}
\posttitle{%
  \par\end{center}%
  \vskip 15pt
}
\preauthor{}
\postauthor{}
\predate{}
\postdate{}

\newcommand{\maketitlehooka}{}
\newcommand{\maketitlehookb}{}
\newcommand{\maketitlehookc}{}
\newcommand{\maketitlehookd}{}

\newcommand{\thanksmarkseries}[1]{%
  \def\@atmarkseries{\renewcommand{\thefootnote}{\@nameuse{#1}{footnote}}}}
\newcommand{\symbolthanksmark}{\thanksmarkseries{fnsymbol}}
\newcommand{\@atcontmark}{\setcounter{footnote}{0}}
\newcommand{\continuousmarks}{\def\@atcontmark{}}
\newcommand{\thanksheadextra}[2]{%
  \def\@atthanksheadpre{#1}%
  \def\@atthanksheadpost{#2}}
\newcommand{\thanksfootextra}[2]{%
  \def\thanksfootpre{#1}%
  \def\thanksfootpost{#2}}

\DeclareRobustCommand{\thanksmark}[1]{\footnotemark[#1]}
\newcommand{\thanksgap}[1]{\hspace{#1}}
\newcommand{\tamark}{\@thefnmark}

\newlength{\thanksmarkwidth}
\newlength{\thanksmargin}
\newcommand{\thanksscript}[1]{\textsuperscript{#1}}
\newcommand{\makethanksmarkhook}{}

\newcommand{\thanksfootmark}{%
  \hb@xt@\thanksmarkwidth{\hfil\normalfont\thanksscript{%
    \thanksfootpre \tamark \thanksfootpost}}}

\newcommand{\makethanksmark}{%
  \leavevmode%
  \makethanksmarkhook\relax
  \parindent 1em\noindent
  \leftskip\thanksmargin\relax
  \advance\leftskip \thanksmarkwidth \null\nobreak\hskip -\leftskip
  \thanksfootmark
}

\newcommand{\usethanksrule}{\let\footnoterule\thanksrule}
\newcommand{\cancelthanksrule}{\let\footnoterule\@atfootnoterule}

\symbolthanksmark

\thanksheadextra{}{}
\thanksfootextra{}{}
\setlength{\thanksmarkwidth}{1.8em}
\setlength{\thanksmargin}{-\thanksmarkwidth}

\AtBeginDocument{%
  \let\AtBeginDocument\AtEndOfPackage
  \let\thanksrule\footnoterule
  \let\@atfootnoterule\footnoterule
}

\renewcommand{\maketitle}{\par
  \begingroup
    \@atmarkseries
    \def\@makefnmark{\rlap{\@textsuperscript{%
       \normalfont\@atthanksheadpre \tamark \@atthanksheadpost}}}%
    \long\def\@makefntext##1{\makethanksmark ##1}
        \twocolumn[\@maketitle]%
        %\thispagestyle{plain}%
        \@thanks
  \endgroup
  \@atcontmark  %  \setcounter{footnote}{0}%
}

\renewcommand{\title}[2][\@empty]{%
  \gdef\@title{#2}%
  \begingroup
  \renewcommand{\thanks}[1]{}
  \renewcommand{\thanksmark}[1]{}
  \renewcommand{\thanksgap}[1]{}
  \ifx#1\@empty%
    \protected@xdef\thetitle{#2}%
  \else
    \protected@xdef\thetitle{#1}%
  \fi
  \endgroup
}
\newcounter{author}
\setcounter{author}{0}
\def\addto@theauthorlist#1{
  \begingroup
  \renewcommand{\thanks}[1]{}
  \renewcommand{\thanksmark}[1]{}
  \renewcommand{\thanksgap}[1]{}
  \xdef\theauthorlist{%
    \theauthorlist\ifnum\c@author=\@ne\else,\ \fi#1}
  \endgroup
}
\renewcommand{\author}[1]{}
\edef\theauthorlist{}
\def\@authorlist{%
  \@tempcntb\@ne
  \@whilenum\c@author>\@tempcntb\do{%
    {\@nameuse{author@\@Roman{\@tempcntb}}, }%
    \advance\@tempcntb\@ne
  }%
  \@nameuse{author@\@Roman{\@tempcntb}}
}

\newcommand{\address}[1]{%
  \expandafter\gdef\csname address@\Roman{author}\endcsname{#1}
}
\newcommand{\netaddress}[1]{%
  \expandafter\gdef\csname netaddress@\Roman{author}\endcsname{#1}
}
\newcounter{title}
\setcounter{title}{0}
%\newcommand{\theHtitle}{\arabic{title}}
\def\title@toc@entry#1{%
  \if@hyperref
  \xdef\@currentHref{title.\theHtitle}%
  \Hy@raisedlink{\hyper@anchorstart{\@currentHref}\hyper@anchorend}%
  \else\fi
  \csname toc@entry@#1\endcsname}
\let\toc@entry@paper\relax

\newwrite\AT@lst

\newcommand\ATarticlelist{%
  \begin{center}
  \large
  \list{}{\parsep=0pt \let\makelabel\ATindexlabel \labelsep=1em \listparindent=2.5em}
  \makeatletter
  \input{artlist.lst}%
  \makeatother
  \endlist
  \end{center}
}
\newcommand\ATindexlabel[1]{%
  \makebox[2.5em][r]{#1}}
\newcommand\@titleline[3]{%
  \item[#3] #2\par%
  \textit{#1}
}
\def\@atdate#1{\csname date@#1\endcsname}
\let\date@paper\relax

\def\@maketitle{%
  \stepcounter{title}
  \title@toc@entry{\@pjp}
  \vspace{\@articlesep}
  \maketitlehooka
  {\@atpretitle \@title \@atposttitle}
  \maketitlehookb
  {\@atpreauthor \@authorlist \@atpostauthor}
  \maketitlehookc
  {\@atdate{\@pjp}}
  \maketitlehookd
  \par
  %\vskip 1.5em
}

\def\@makecolophon{%
  \nopagebreak\vfill%
  \hfill{\scriptsize Versione \input{version} compilata il \today.}
}

\newlength\sigindent
\setlength\sigindent{.25\columnwidth}
\def\@makesig{%
  \if@fvrbex\long\def\@gobble##1{}\else\fi
  \renewcommand{\thanks}[1]{}
  \renewcommand{\thanksmark}[1]{}
  \renewcommand{\thanksgap}[1]{}
  \vspace{\DropSig}
  \list{}{\topsep\z@ \parsep\z@ \leftmargin=\sigindent \partopsep\z@}
  \@tempcntb\z@
  \@whilenum\c@author>\@tempcntb\do{%
    \advance\@tempcntb\@ne
    \item[\SigSymbol]
    \@usenempty{author@\@Roman{\@tempcntb}}\par\nobreak
    \@usenempty{address@\@Roman{\@tempcntb}}\par\nobreak
    \texttt{\@usenempty{netaddress@\@Roman{\@tempcntb}}}
    }
  \endlist
  \gdef\@thanks{}
  \if@fvrbex\def\@gobble##1{}\else\fi
}
\def\AT@tablecaptions{%
  \setlength{\belowcaptionskip}{\abovecaptionskip}%
  \setlength{\abovecaptionskip}{0pt}%
}
\def\AT@figurecaptions{}
\AtBeginDocument{%
\long\def\@makecaption#1#2{%
  \@nameuse{AT@\@captype captions}
  \footnotesize
  \vskip\abovecaptionskip
  \sbox\@tempboxa{\textsc{#1}: #2}%
  \ifdim \wd\@tempboxa >\hsize
    \textsc{#1}: #2\par
  \else
    \global \@minipagefalse
    \hb@xt@\hsize{\hfil\box\@tempboxa\hfil}%
  \fi
  \vskip\belowcaptionskip}
}
\newcounter{article}
\newenvironment{article}{%
  \@openarticle}{\@closearticle}
%\newcommand{\theHarticle}{\arabic{article}}

\def\@paperheada{{\sc\small Dipartimento di Fisica E. Fermi, Universit\`a di Pisa}}
\def\@paperheadb{{\sc\small Laboratori didattici del primo anno}}

%\def\ps@paper{%
%  \def\@oddfoot{\hfil\thepage\hfil}
%  \def\@evenfoot{\hfil\thepage\hfil}
%  \def\@oddhead{\@paperhead\hfil\thetitle}
%  \def\@evenhead{\theauthorlist\hfil\@paperhead}
%}

\def\ps@paper{%
  \def\@oddfoot{}
  \def\@evenfoot{}
  \def\@oddhead{\@paperheada\hfil\@paperheadb}
  \def\@evenhead{\@paperheada\hfil\@paperheadb}
}


\let\ps@toc\ps@empty
\AtBeginDocument{%
  \pagestyle{\@pjp}
  \let\AT@thebibliography\thebibliography
  \def\thebibliography{%
    \let\sloppy\@atbibliopatch
    \AT@thebibliography
  }
  \@ifpackageloaded{fvrb-ex}{\@fvrbextrue}{\@fvrbexfalse}
  \@ifpackageloaded{hyperref}{\@hyperreftrue}{\@hyperreffalse}
}
\def\@atbibliopatch{%
  \@atbibfont
  \@atbibjustification
}
\def\@atbibfont{}
\def\@atbibjustification{}%{\raggedright}

\def\toclevel@title{0}
\let\@oldtoc\tableofcontents
\def\BlackBoxes{\overfullrule=5\p@}
\def\NoBlackBoxes{\overfullrule=\z@}
\newcommand*\pkgname[1]{\textsf{#1}}
\newcommand*\clsname[1]{\textsf{#1}}
\newcommand*\optname[1]{\textsf{#1}}
\newcommand*\envname[1]{\textsf{#1}}
\DeclareRobustCommand\cmdname[1]{\texttt{\char`\\#1}}
\DeclareRobustCommand\meta[1]{%
  \ensuremath{\langle}\emph{#1}\ensuremath{\rangle}}
\def\@cfgfound{\ClassInfo{pls-article}{Info loaded from \jobname.cfg.}}
\def\@cfgnotfound{\ClassWarning{pls-article}{Config file not found.}}

\def\@usenempty#1{%
  \csname #1\endcsname
  \global\expandafter\let\csname #1\endcsname\@empty
}

\def\footnoterule{}
\def\class@name{pls-article}
\newlength\@articlesep
\setlength\@articlesep\z@

\newcommand\IssueLine{{\IssueLineFont Numero \AT@number, \AT@month\ \AT@year}}
\newcommand\IssueLineFont{\Large\itshape}
\newcommand\@headfont{\itshape}
\newcommand*\SigSymbol{\ensuremath{\triangleright}}
\newlength\DropSig
\setlength\DropSig{2\baselineskip}
\newlength{\arswidth}

\renewcommand\@makefntext[1]{%
    \parindent 1em%
    \@thefnmark.\kern1.5mm#1}

%% thanks to C. Beccari
\def\manualbalance{%
 \ifvmode
   \vfill
   \penalty -\@M%
 \else
   \@bsphack
   \vadjust{\vspace{\z@\@plus1fill}\penalty -\@M}%
   \@esphack
 \fi}

\usepackage[italian]{babel}
\frenchspacing

\usepackage{tikz}
\usepackage{fancyvrb}
\fvset{frame=single,numbers=left,numbersep=3pt,fontsize=\normalsize,
       baselinestretch=1.0, rulecolor=\color{lightgray}}


\newcommand{\labsection}[1]{\section*{#1}}
\newcommand{\labsubsection}[1]{\subsection*{#1}}
\newcommand{\secsummary}{\labsection{Sommario}}
\newcommand{\secintro}{\labsection{Introduzione}}
\newcommand{\secmaterials}{\labsection{Materiale a disposizione}}
\newcommand{\secmaterialsdad}{\labsection{Materiale necessario}}
\newcommand{\secdefinitions}{\labsection{Definizioni}}
\newcommand{\secconsiderations}{\labsection{Considerazioni pratiche}}
\newcommand{\secmeasurements}{\labsection{Misure ed analisi}}
\newcommand{\subsecdataformat}{\labsubsection{Il formato dei dati}}
\newcommand{\secappendix}[1]{\section{Appendice: #1}}

\newcommand{\menuitem}[1]{\emph{#1}}


\endinput
