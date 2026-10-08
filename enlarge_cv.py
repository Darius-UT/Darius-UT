from pathlib import Path
import shutil
p=Path('output/harvard_cv_readable')
old=Path('output/harvard_cv_centered_sections')
p.mkdir(exist_ok=True)
for d in ['config','data','sections']:
    shutil.copytree(old/d,p/d,dirs_exist_ok=True)
shutil.copy2(old/'main.tex',p/'main.tex')
f=p/'config/commands.tex'
s=f.read_text(encoding='utf-8')
for a,b in {
    '{9.4}{10.7}':'{10.2}{12.0}',
    '{10.7}{11.8}':'{11.2}{13.0}',
    '{9.9}{11.0}':'{10.7}{12.6}',
    '{8.85}{10.0}':'{9.6}{11.5}',
    '{9.05}{10.2}':'{10.0}{12.0}',
    '{9.05}{10.35}':'{10.2}{12.6}',
    '{9.0}{10.25}':'{10.2}{12.6}',
    r'\vspace{10pt}':r'\vspace{12pt}',
    r'\endgroup\vspace{4pt}':r'\endgroup\vspace{5.5pt}',
    r'\arraystretch}{0.98}':r'\arraystretch}{1.06}',
    r'\vspace{0.55pt}':r'\vspace{1.8pt}',
    r'\vspace{0.9pt}':r'\vspace{2pt}',
    r'\vspace{1.2pt}':r'\vspace{2pt}',
    r'\makebox[1.32in]':r'\makebox[1.40in]',
}.items(): s=s.replace(a,b)
f.write_text(s,encoding='utf-8')
f=p/'config/theme.tex'
s=f.read_text(encoding='utf-8').replace('itemsep=1.15pt','itemsep=2.1pt').replace('topsep=1.4pt','topsep=2.4pt')
f.write_text(s,encoding='utf-8')
(p/'README.md').write_text('''# Readable centered-section CV

Compile main.tex twice with LuaLaTeX.

Body text: 10.2 pt with 12.6 pt baseline spacing. Entity headings: 10.7 pt. Metadata: 9.6 pt. Section titles: 11.2 pt, centered between equal rules. Slightly wider spacing for bullets and skill rows improves readability and page balance.

Contact icons are retained without external-link marks. Project URLs use \\cvprojectlink{URL}{label} with a clickable indicator. Font Awesome 5 is optional with a text fallback. The displayed personal data and section content are unchanged.

Relative to the previous centered-section variant, only config/commands.tex and config/theme.tex were revised.
''',encoding='utf-8')
