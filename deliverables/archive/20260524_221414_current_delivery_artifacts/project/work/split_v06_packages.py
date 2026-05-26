import os, re, json, shutil, zipfile
from pathlib import Path

root = Path(r'C:\Users\Administrator\cursor\feishu-bot4-workspace')
work = root / 'project' / 'work'
deliver = root / 'deliverables'
skill = root / 'skills' / 'huawei_ppt_master'

outline = (work / 'outline_v0.6.md').read_text(encoding='utf-8')
page_copy = (work / 'page_copy_v0.6.md').read_text(encoding='utf-8')
page_design = (work / 'page_design_v0.6.md').read_text(encoding='utf-8')
deck = json.loads((work / 'deck_spec_v0.6.json').read_text(encoding='utf-8'))

ranges = [(1, 10), (11, 16)]
base = 'huawei_cloud_competitiveness_2026-05-04_v0.6'

def split_sections(text):
    lines = text.splitlines()
    header = []
    sections = []
    i = 0
    while i < len(lines) and not re.match(r'^##\s+P\d+', lines[i]):
        header.append(lines[i])
        i += 1
    current = []
    while i < len(lines):
        if re.match(r'^##\s+P\d+', lines[i]) and current:
            sections.append('\n'.join(current).rstrip())
            current = [lines[i]]
        else:
            current.append(lines[i])
        i += 1
    if current:
        sections.append('\n'.join(current).rstrip())
    return '\n'.join(header).rstrip(), sections

def page_no_from_section(sec):
    return int(re.match(r'^##\s+P(\d+)', sec).group(1))

copy_header, copy_sections = split_sections(page_copy)
design_header, design_sections = split_sections(page_design)

lines = outline.splitlines()
outline_header = []
idx = 0
while idx < len(lines) and not lines[idx].startswith('## '):
    outline_header.append(lines[idx])
    idx += 1
chapters = []
current_chapter = None
current_page = []
while idx < len(lines):
    line = lines[idx]
    if line.startswith('## '):
        if current_page:
            current_chapter['pages'].append('\n'.join(current_page).rstrip())
            current_page = []
        if current_chapter:
            chapters.append(current_chapter)
        current_chapter = {'title': line, 'pages': []}
    elif line.startswith('### P'):
        if current_page:
            current_chapter['pages'].append('\n'.join(current_page).rstrip())
        current_page = [line]
    else:
        if current_chapter is None:
            outline_header.append(line)
        else:
            current_page.append(line)
    idx += 1
if current_page and current_chapter:
    current_chapter['pages'].append('\n'.join(current_page).rstrip())
if current_chapter:
    chapters.append(current_chapter)

for start, end in ranges:
    pkg_name = f'{base}_P{start:02d}-P{end:02d}'
    out_dir = deliver / pkg_name
    zip_path = deliver / f'{pkg_name}.zip'
    shutil.rmtree(out_dir, ignore_errors=True)
    out_dir.mkdir(parents=True, exist_ok=True)

    parts = ['\n'.join(outline_header).rstrip(), '']
    for ch in chapters:
        selected = []
        for pg in ch['pages']:
            m = re.match(r'^### P(\d+)', pg)
            if m and start <= int(m.group(1)) <= end:
                selected.append(pg)
        if selected:
            parts.append(ch['title'])
            parts.append('')
            for s in selected:
                parts.append(s)
                parts.append('')
    parts.append('## 后续逐页文案建议')
    parts.append(f'- 本分包仅包含 P{start}~P{end} 内容。')
    (out_dir / '01_outline.md').write_text('\n'.join(parts).rstrip() + '\n', encoding='utf-8')
    (out_dir / '02_page_copy.md').write_text(copy_header + '\n\n' + '\n\n'.join([s for s in copy_sections if start <= page_no_from_section(s) <= end]) + '\n', encoding='utf-8')
    (out_dir / '03_page_design.md').write_text(design_header + '\n\n' + '\n\n'.join([s for s in design_sections if start <= page_no_from_section(s) <= end]) + '\n', encoding='utf-8')
    deck_subset = {
        'deck_title': deck['deck_title'],
        'audience': deck['audience'],
        'style': deck['style'],
        'package_range': f'P{start}-P{end}',
        'slides': [s for s in deck['slides'] if start <= s['slide_no'] <= end]
    }
    (out_dir / '04_deck_spec.json').write_text(json.dumps(deck_subset, ensure_ascii=False, indent=2), encoding='utf-8')
    (out_dir / 'README.md').write_text(
        f'# 华为云竞争力深度洞察 - 分包交付 v0.6\n\n- 分包范围：P{start}~P{end}\n- 来源版本：v0.6（16页完整版）\n- 本包包含：大纲 / 逐页文案 / 页面设计 / deck_spec / 最小依赖\n- 说明：页码保持原始页码，不重排。\n',
        encoding='utf-8'
    )
    for sub in ['templates', 'visual_patterns']:
        shutil.copytree(skill / sub, out_dir / 'dependencies' / sub)
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for dp, _, fs in os.walk(out_dir):
            for f in fs:
                ap = Path(dp) / f
                zf.write(ap, ap.relative_to(out_dir.parent).as_posix())
    print(zip_path)
