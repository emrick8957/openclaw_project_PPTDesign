import json
import re
import shutil
import zipfile
from pathlib import Path

root = Path(r"C:\Users\Administrator\cursor\feishu-bot4-workspace")
deliver = root / "deliverables"
deliver.mkdir(exist_ok=True)

outline = (root / "project/work/outline_v0.1.md").read_text(encoding="utf-8")
page_copy = (root / "project/work/page_copy_v0.1.md").read_text(encoding="utf-8")
page_design = (root / "project/work/page_design_v0.1.md").read_text(encoding="utf-8")
deck = json.loads((root / "project/work/deck_spec_v0.1.json").read_text(encoding="utf-8"))

ranges = [(1, 10), (11, 14)]
name_base = "ai4test_insights_2026-05-09_v0.1"

def filter_markdown_sections(text: str):
    parts = re.split(r"\n## (P\d+)\n", text)
    header = parts[0]
    blocks = {}
    for i in range(1, len(parts), 2):
        page = int(parts[i][1:])
        blocks[page] = f"## {parts[i]}\n" + parts[i + 1]
    return header, blocks

outline_lines = outline.splitlines()
outline_header = []
outline_blocks = {}
current = None
buf = []
for line in outline_lines:
    m = re.match(r"^### P(\d+)\s", line)
    if m:
        if current is not None:
            outline_blocks[current] = "\n".join(buf).rstrip() + "\n"
        current = int(m.group(1))
        buf = [line]
    else:
        if current is None:
            outline_header.append(line)
        else:
            buf.append(line)
if current is not None:
    outline_blocks[current] = "\n".join(buf).rstrip() + "\n"
outline_header = "\n".join(outline_header).rstrip() + "\n\n"

copy_header, copy_blocks = filter_markdown_sections(page_copy)
design_header, design_blocks = filter_markdown_sections(page_design)

templates = [
    "chart_patterns.md",
    "huawei_style_reference.md",
    "narrative_patterns.md",
    "page_types.md",
    "visual_rules.md",
    "wording_rules.md",
]
visuals = [
    "architecture_page_patterns.md",
    "comparison_page_patterns.md",
    "executive_summary_patterns.md",
    "layout_library.md",
    "risk_decision_patterns.md",
    "roadmap_page_patterns.md",
    "screenshot_layout_analysis.md",
]

for start, end in ranges:
    pkg = deliver / f"{name_base}_P{start:02d}-P{end:02d}"
    if pkg.exists():
        shutil.rmtree(pkg)
    pkg.mkdir(parents=True)
    selected = list(range(start, end + 1))

    (pkg / "01_outline.md").write_text(
        outline_header + "".join(outline_blocks[p] + "\n" for p in selected if p in outline_blocks),
        encoding="utf-8",
    )
    (pkg / "02_page_copy.md").write_text(
        copy_header + "".join(copy_blocks[p] + "\n" for p in selected if p in copy_blocks),
        encoding="utf-8",
    )
    (pkg / "03_page_design.md").write_text(
        design_header + "".join(design_blocks[p] + "\n" for p in selected if p in design_blocks),
        encoding="utf-8",
    )

    subset = dict(deck)
    subset["slides"] = [s for s in deck["slides"] if start <= s["slide_no"] <= end]
    (pkg / "04_deck_spec.json").write_text(json.dumps(subset, ensure_ascii=False, indent=2), encoding="utf-8")
    (pkg / "README.md").write_text(
        f"# AI4Test洞察 交付分包 P{start:02d}-P{end:02d}\n\n"
        f"- 页码范围：P{start}-P{end}\n"
        f"- 包含：大纲、逐页文案、页面设计说明、deck_spec.json\n"
        f"- 依赖：仅保留 `templates/` 与 `visual_patterns/` 最小依赖文件\n",
        encoding="utf-8",
    )

    dep_t = pkg / "dependencies/templates"
    dep_v = pkg / "dependencies/visual_patterns"
    dep_t.mkdir(parents=True)
    dep_v.mkdir(parents=True)

    for fn in templates:
        shutil.copy2(root / "skills/huawei_ppt_master/templates" / fn, dep_t / fn)
    for fn in visuals:
        shutil.copy2(root / "skills/huawei_ppt_master/visual_patterns" / fn, dep_v / fn)

    zip_path = deliver / f"{name_base}_P{start:02d}-P{end:02d}.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in pkg.rglob("*"):
            zf.write(file, file.relative_to(pkg.parent))
    print(f"built {pkg.name} and {zip_path.name}")
