from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from pypdf import PdfReader
p=Path('output/harvard_cv_header')
r=PdfReader(p/'main.pdf')
assert len(r.pages)==1
links=[a.get_object().get('/A',{}).get('/URI') for a in r.pages[0].get('/Annots',[])]
print('PDF pages:',len(r.pages),'Link targets:',links)
source=Path('D:/TexStudio/harvard_cv_template')
for d in ['sections']:
    for f in (p/d).glob('*.tex'):
        assert f.read_bytes()==(source/d/f.name).read_bytes(), f
assert (p/'main.tex').read_bytes()==(source/'main.tex').read_bytes()
with ZipFile('output/harvard_cv_header.zip','w',ZIP_DEFLATED) as z:
    for f in p.rglob('*'):
        if f.is_file() and (f.suffix=='.tex' and not f.name.startswith('fallback-') or f.name in ['README.md','main.pdf','preview.png']):
            z.write(f,Path('harvard_cv_header')/f.relative_to(p))
print('ZIP ready. Original content unchanged.')
