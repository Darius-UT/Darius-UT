from pathlib import Path
p=Path('output/harvard_cv_header')
f=p/'config/packages.tex'
s=f.read_text(encoding='utf-8')
s += r'''
% Optional icon package; all packages load at preamble scope.
\newif\ifCVIcons
\IfFileExists{fontawesome5.sty}{\CVIconstrue}{\CVIconsfalse}
\ifCVIcons
  \usepackage{fontawesome5}
\fi
'''
f.write_text(s,encoding='utf-8')
f=p/'config/commands.tex'
s=f.read_text(encoding='utf-8')
a=s.index(r'\newcommand{\makecvheader}')
b=s.index('% =========================================================',a)
header=r'''
% Fixed-width contact icons keep their baseline and spacing consistent.
\newcommand{\cvcontacticon}[2]{%
  \makebox[1.15em][c]{\ifCVIcons\faIcon{#1}\else\textsf{#2}\fi}\hspace{0.25em}%
}
\newcommand{\cvlinkmark}{%
  \hspace{0.22em}{\fontsize{6.8}{7.5}\selectfont
  \ifCVIcons\faIcon{external-link-alt}\else\ensuremath{\nearrow}\fi}%
}
\newsavebox{\CVIdentityBox}
\newsavebox{\CVContactBox}
\newlength{\CVSideRule}
\newcommand{\cvcontacts}{%
  \href{mailto:\CVEmail}{\cvcontacticon{envelope}{@}\CVEmail\cvlinkmark}%
  \contactsep\cvcontacticon{phone}{T}\CVPhone%
  \contactsep\cvcontacticon{map-marker-alt}{L}\CVLocation%
  \ifdefempty{\CVLinkedInURL}{}{\contactsep
    \href{\CVLinkedInURL}{\cvcontacticon{linkedin}{in}\CVLinkedInText\cvlinkmark}}%
  \ifdefempty{\CVGitHubURL}{}{\contactsep
    \href{\CVGitHubURL}{\cvcontacticon{github}{GH}\CVGitHubText\cvlinkmark}}%
}
\newcommand{\makecvheader}{%
  \par\begingroup\centering
  \sbox{\CVIdentityBox}{\begin{tabular}{@{}c@{}}
    {\fontsize{19.5}{21.5}\selectfont\bfseries\CVName}\\[1.8pt]
    {\fontsize{9.4}{10.7}\selectfont\color{CVMuted}\CVRole}
  \end{tabular}}%
  \setlength{\CVSideRule}{\dimexpr(\linewidth-\wd\CVIdentityBox-24pt)/2\relax}%
  \noindent\makebox[\linewidth][c]{%
    {\color{CVRule}\rule[0.4ex]{\CVSideRule}{0.4pt}}\hspace{12pt}%
    \usebox{\CVIdentityBox}\hspace{12pt}%
    {\color{CVRule}\rule[0.4ex]{\CVSideRule}{0.4pt}}}\par
  \vspace{6pt}%
  {\fontsize{8.7}{10.5}\selectfont\color{CVMuted}%
    \sbox{\CVContactBox}{\cvcontacts}%
    \ifdim\wd\CVContactBox>\linewidth
      % Safe wrap for longer personal data; never shrink contact text.
      \cvcontacts\par
    \else
      \noindent\makebox[\linewidth][c]{\usebox{\CVContactBox}}\par
    \fi
  }%
  \endgroup\vspace{5.5pt}%
}

'''
s=s[:a]+header+s[b:]
f.write_text(s,encoding='utf-8')
(p/'README.md').write_text('''# Centered icon header variant

Compile main.tex with LuaLaTeX twice. Only config/packages.tex and config/commands.tex differ from the supplied project. Personal data and all sections are preserved.

The two equal rules flank the centered name/role block. Contact icons use fontawesome5 when installed; otherwise compact text labels (@, T, L, in, GH) are used. Every linked contact has an external-link mark; email opens the mail application. Phone and location remain plain text. Longer contact data wraps without shrinking the font.

To test the fallback, add \\CVIconsfalse immediately after \\input{config/packages} in main.tex.
''',encoding='utf-8')
