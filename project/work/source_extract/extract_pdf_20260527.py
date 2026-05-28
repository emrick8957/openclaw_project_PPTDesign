from pathlib import Path
from pypdf import PdfReader
pdf = Path(r'examples\人工智能在自动化生产系统基于模型的系统工程（MBSE）中的应用.pdf')
out = Path(r'project\work\source_extract\AI4MBSE_pdf_text_20260527.txt')
out.parent.mkdir(parents=True, exist_ok=True)
r = PdfReader(str(pdf))
texts = []
for i, p in enumerate(r.pages, 1):
    t = p.extract_text() or ''
    texts.append(f'\n\n===== PAGE {i} =====\n{t}')
out.write_text(''.join(texts), encoding='utf-8')
print('pages', len(r.pages), 'chars', sum(len(x) for x in texts), 'out', out)
