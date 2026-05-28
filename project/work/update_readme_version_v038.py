from pathlib import Path

# Clean and refresh INDEX while preserving original structure/headings
index = Path('skills/huawei_ppt_master/INDEX.md')
index.write_text('''# Skills Index

> huawei_ppt_master Skill 总索引。
> 用途：快速定位 huawei_ppt_master 入口、速查文件和适用场景。
> 更新时间：2026-05-28

## 目录

### 1. huawei_ppt_master
- **路径**：`skills/huawei_ppt_master/`
- **入口文件**：`skills/huawei_ppt_master/SKILL.md`
- **快速索引**：`skills/huawei_ppt_master/QUICK_INDEX.md`
- **路由总表**：`skills/huawei_ppt_master/REFERENCE_ROUTING_TABLE.md`
- **适用场景**：华为风格 PPT 大纲、逐页文案、页面设计说明、deck_spec 生成
- **视觉一致性资产**：`templates/visual_rules.md`、`templates/chart_patterns.md`、`visual_patterns/layout_library.md`、`eval/visual_scorecard.md`、`prompts/generate_page_design.md`
- **生成图片反馈资产**：正文页红色底座控制、多卡片主次层级、案例证明页、决策建议页、路线图阶段门槛、长标题压缩、总结页最终定义、visual_scorecard 一票降级项
- **deck_spec 证明契约资产**：`core/output_contracts.md`、`prompts/deck_spec_generation.md`、`templates/chart_patterns.md`、`eval/visual_scorecard.md`；新增 `core_judgement` / `chart_proof_goal` / `chart_visual_boundary`
- **deck_spec 字段字典**：`core/deck_spec_field_dictionary.md`；说明文件定位、顶层字段和 slide 字段，作为后续正式交付物支持资产
- **视觉规则重构资产**：`templates/visual_rules.md` 专职视觉指导边界、负面视觉风格总表、视觉优化优先级、默认推荐样式、`visual_boundary` / `page_type_gate` 页面设计字段
- **典型主题**：技术方案、战略规划、竞品对比、项目复盘、客户方案、资源申请、运营治理、产品路线图、调研分析

## 推荐调取方式

- 想看某个 Skill 的入口规则：先读对应 `SKILL.md`
- 想快速定位某个 Skill 的常用文件：优先看该 Skill 的 `QUICK_INDEX.md`
- 想看主题路由和术语边界：优先看 `REFERENCE_ROUTING_TABLE.md`
- 想看 `deck_spec.json` 字段含义：读 `core/deck_spec_field_dictionary.md`

## 当前状态

- 当前版本：`v0.3.8-deck-spec-field-dictionary`
- 当前工作区已建总索引：`skills/INDEX.md`
- 当前已收录 Skill：`huawei_ppt_master`
- 后续新增 Skill 时，补充到本页即可

## 文件目录结构

## 关键目录作用


## 文件职责

''', encoding='utf-8')

# Update manifest robustly
manifest = Path('skills/huawei_ppt_master/PACKAGE_MANIFEST.md')
text = manifest.read_text(encoding='utf-8')
text = text.replace('Current package version: v0.3.7-deck-spec-proof-contract', 'Current package version: v0.3.8-deck-spec-field-dictionary')
text = text.replace('Last updated: 2026-05-26', 'Last updated: 2026-05-28')
if '- `core/deck_spec_field_dictionary.md`' not in text:
    text = text.replace('- `core/audience_rules.md`\n', '- `core/audience_rules.md`\n- `core/deck_spec_field_dictionary.md`\n')
if '`core/deck_spec_field_dictionary.md`  \n  定义 `deck_spec.json`' not in text:
    anchor = '- `core/audience_rules.md`  \n  根据汇报对象调整口径，包括华为内部高层、客户高层、市局/分局领导、技术团队等。'
    insert = anchor + '\n\n- `core/deck_spec_field_dictionary.md`  \n  定义 `deck_spec.json` 的文件定位、顶层字段和 slide 字段职责，作为角色 C 理解 deck_spec 的正式交付物支持文档。'
    text = text.replace(anchor, insert)
if '### 3.10 v0.3.8 deck_spec 字段字典资产' not in text:
    text += '''\n\n### 3.10 v0.3.8 deck_spec 字段字典资产\n\n本版本新增以下正式交付物支持资产：\n\n- `core/deck_spec_field_dictionary.md`：说明 `deck_spec.json` 的文件定位、顶层字段和 slide 字段，明确其是页面语义合同，不是 PPTX 或 shape 指令。\n\n边界：本版本不继续推进 `page_render_spec` / `normalized_render_model` 方案，不新增渲染 DSL，不改变默认生成链路。\n'''
manifest.write_text(text, encoding='utf-8')

# Improve QUICK_INDEX with field dictionary link while preserving structure
quick = Path('skills/huawei_ppt_master/QUICK_INDEX.md')
qt = quick.read_text(encoding='utf-8')
if 'deck_spec 字段字典' not in qt:
    qt = qt.replace('- 防污染规则：`skills/huawei_ppt_master/core/anti_overfit_rules.md`\n', '- 防污染规则：`skills/huawei_ppt_master/core/anti_overfit_rules.md`\n- deck_spec 字段字典：`skills/huawei_ppt_master/core/deck_spec_field_dictionary.md`\n')
    qt += '\n- 想看“deck_spec.json 每个字段给角色 C 怎么理解” → 读 `core/deck_spec_field_dictionary.md`\n'
quick.write_text(qt, encoding='utf-8')

# ensure changelog spacing before v0.3.7
ch = Path('skills/huawei_ppt_master/CHANGELOG.md')
ct = ch.read_text(encoding='utf-8').replace('仅补充字段字典说明。\n## v0.3.7', '仅补充字段字典说明。\n\n## v0.3.7')
ch.write_text(ct, encoding='utf-8')
