from pathlib import Path
import shutil
p=Path('output/harvard_cv_centered_sections')
p.mkdir(exist_ok=True)
old=Path('output/harvard_cv_header')
for d in ['config','data','sections']:
    shutil.copytree(old/d,p/d,dirs_exist_ok=True)
shutil.copy2(old/'main.tex',p/'main.tex')
f=p/'config/commands.tex'
s=f.read_text(encoding='utf-8')
s=s.replace(r'\CVEmail\cvlinkmark',r'\CVEmail').replace(r'\CVLinkedInText\cvlinkmark',r'\CVLinkedInText').replace(r'\CVGitHubText\cvlinkmark',r'\CVGitHubText')
a=s.index(r'  \sbox{\CVIdentityBox}')
b=s.index(r'  \vspace{6pt}',a)
s=s[:a]+r'''  {\fontsize{19.5}{21.5}\selectfont\bfseries\CVName\par}%
  \vspace{1.8pt}%
  {\fontsize{9.4}{10.7}\selectfont\color{CVMuted}\CVRole\par}%
'''+s[b:]
a=s.index(r'\newcommand{\cvsection}')
b=s.index('% =========================================================',a)
s=s[:a]+r'''\newsavebox{\CVSectionBox}
\newlength{\CVSectionRule}
\newcommand{\cvsection}[1]{%
  \par\vspace{10pt}%
  \Needspace{3\baselineskip}%
  \begingroup
  \sbox{\CVSectionBox}{\color{CVAccent}\bfseries
    \fontsize{10.7}{11.8}\selectfont\MakeUppercase{#1}}%
  \setlength{\CVSectionRule}{\dimexpr(\linewidth-\wd\CVSectionBox-20pt)/2\relax}%
  \noindent\makebox[\linewidth][c]{%
    {\color{CVRule}\rule[0.5ex]{\CVSectionRule}{0.42pt}}\hspace{10pt}%
    \usebox{\CVSectionBox}\hspace{10pt}%
    {\color{CVRule}\rule[0.5ex]{\CVSectionRule}{0.42pt}}}\par
  \endgroup\vspace{4pt}%
}
% Use only for project URLs; the indicator is clickable with the label.
\newcommand{\cvprojectlink}[2]{\href{#1}{#2\cvlinkmark}}

'''+s[b:]
s=s.replace(r'\newsavebox{\CVIdentityBox}'+'\n','').replace(r'\newlength{\CVSideRule}'+'\n','')
f.write_text(s,encoding='utf-8')
f=p/'sections/projects.tex'
f.write_text(f.read_text(encoding='utf-8').replace(r'\href{',r'\cvprojectlink{'),encoding='utf-8')
(p/'README.md').write_text('''# Centered section titles variant

Compile main.tex with LuaLaTeX twice.

Name and role remain centered without side rules. Contact icons remain, with no extra external-link marks. Section titles are centered between equal horizontal rules. Project links use \\cvprojectlink{URL}{label}, which adds a clickable external-link indicator.

Font Awesome 5 is optional with text-safe fallback. All displayed CV content is preserved. The LinkedIn URL is percent-encoded to preserve accented characters in PDF links.

Changed source files versus the original: config/packages.tex, config/commands.tex, data/personal.tex (URL encoding), sections/projects.tex (link wrapper). theme.tex and other sections are unchanged.
''',encoding='utf-8')
