from pathlib import Path

# README insert v0.3.9 before v0.3.8 and bump title
p=Path('skills/huawei_ppt_master/README.md')
t=p.read_text(encoding='utf-8')
t=t.replace('# huawei_ppt_master Skill v0.3.8', '# huawei_ppt_master Skill v0.3.9')
if '## v0.3.9 chart_semantic_mapping 图表语义映射' not in t:
    block='''## v0.3.9 chart_semantic_mapping 图表语义映射

v0.3.9 在 deck_spec 证明契约基础上新增 `chart_semantic_mapping`，用于说明主图表如何证明 `chart_proof_goal`，避免图表沦为装饰、模板或误读。

新增字段：

```json
"chart_semantic_mapping": {
  "chart_reading_intent": "",
  "main_visual_logic": "",
  "axis_semantics": {},
  "stage_or_node_meaning": {},
  "insight_panel_logic": [],
  "forbidden_visualization": []
}
```

触发规则：

- `chart_type = trend_curve` 时必须输出；
- `quadrant_matrix`、`roadmap_timeline_chart`、`architecture_flow_diagram`、`layered_stack_diagram`、`value_chain_loop`、`swimlane_process`、`ecosystem_relationship_map` 等高语义风险图表建议输出。

边界说明：

- 本字段是 deck_spec 语义证明增强，不是渲染 DSL；
- 不规定 shape 坐标、字号、线条或连接线；
- 不恢复 `page_render_spec` / `normalized_render_model` 方案。

'''
    t=t.replace('## v0.3.8 deck_spec 字段字典正式化', block + '## v0.3.8 deck_spec 字段字典正式化')
p.write_text(t, encoding='utf-8')

# VERSION
p=Path('skills/huawei_ppt_master/VERSION.md')
t=p.read_text(encoding='utf-8')
t=t.replace('Current Version: v0.3.8-deck-spec-field-dictionary','Current Version: v0.3.9-chart-semantic-mapping')
if '- v0.3.9: Chart semantic mapping.' not in t:
    t=t.replace('- v0.3.8: Deck spec field dictionary formalization. Adds `core/deck_spec_field_dictionary.md` as a formal delivery-support asset with three sections: file positioning, top-level fields, and slide fields. This version terminates the page_render_spec / normalized_render_model exploration and does not add a rendering DSL.',
'''- v0.3.8: Deck spec field dictionary formalization. Adds `core/deck_spec_field_dictionary.md` as a formal delivery-support asset with three sections: file positioning, top-level fields, and slide fields. This version terminates the page_render_spec / normalized_render_model exploration and does not add a rendering DSL.
- v0.3.9: Chart semantic mapping. Adds `chart_semantic_mapping` to deck_spec as a semantic proof explanation field, mandatory for `trend_curve` and recommended for high-semantic-risk charts. This is not a rendering DSL.''')
p.write_text(t, encoding='utf-8')

# CHANGELOG
p=Path('skills/huawei_ppt_master/CHANGELOG.md')
t=p.read_text(encoding='utf-8')
if '## v0.3.9-chart-semantic-mapping' not in t:
    block='''# CHANGELOG

## v0.3.9-chart-semantic-mapping

### 升级目标

新增 `chart_semantic_mapping`，补齐 `chart_type` 与 `chart_proof_goal` 之间的图表语义解释层，尤其解决 `trend_curve` 等图表“看起来有趋势、实际无法证明判断”的问题。

### 新增

1. `core/output_contracts.md`：deck_spec 增加 `chart_semantic_mapping` 字段说明、示例和触发门禁。
2. `prompts/deck_spec_generation.md`：要求 `trend_curve` 必须输出 `chart_semantic_mapping`，高语义风险图表建议输出。
3. `templates/chart_patterns.md`：新增 `chart_semantic_mapping` 语义解释映射规则、六个核心字段和 `trend_curve` 示例。
4. `eval/visual_scorecard.md`：新增 v0.3.9 图表语义映射检查与一票降级项。
5. `core/deck_spec_field_dictionary.md`：补充 `chart_semantic_mapping` 字段说明。

### 修改

1. `SKILL.md` 版本升级为 `0.3.9-chart-semantic-mapping`。
2. `README.md`、`VERSION.md`、`INDEX.md`、`QUICK_INDEX.md`、`PACKAGE_MANIFEST.md` 同步版本与资产说明。

### 边界

1. 本版本只增强 deck_spec 语义证明能力。
2. 不恢复 `page_render_spec` / `normalized_render_model` 方案。
3. 不新增 PPTX 渲染 DSL、shape plan 或 C 端渲染协议。
4. `chart_semantic_mapping` 必须服务 `chart_proof_goal`，不得另起一套判断。

'''
    t=block + t.replace('# CHANGELOG\n\n','')
p.write_text(t, encoding='utf-8')

# INDEX
p=Path('skills/huawei_ppt_master/INDEX.md')
t=p.read_text(encoding='utf-8')
t=t.replace('更新时间：2026-05-28','更新时间：2026-05-28')
t=t.replace('- 当前版本：`v0.3.8-deck-spec-field-dictionary`','- 当前版本：`v0.3.9-chart-semantic-mapping`')
if 'chart_semantic_mapping' not in t:
    t=t.replace('- **deck_spec 字段字典**：`core/deck_spec_field_dictionary.md`；说明文件定位、顶层字段和 slide 字段，作为后续正式交付物支持资产',
'''- **deck_spec 字段字典**：`core/deck_spec_field_dictionary.md`；说明文件定位、顶层字段和 slide 字段，作为后续正式交付物支持资产
- **图表语义映射资产**：`chart_semantic_mapping`；`trend_curve` 必填，高语义风险图表建议输出，用于说明主图如何证明 `chart_proof_goal`''')
p.write_text(t, encoding='utf-8')

# QUICK_INDEX
p=Path('skills/huawei_ppt_master/QUICK_INDEX.md')
t=p.read_text(encoding='utf-8')
if 'chart_semantic_mapping' not in t:
    t=t.replace('- deck_spec 字段字典：`skills/huawei_ppt_master/core/deck_spec_field_dictionary.md`',
'''- deck_spec 字段字典：`skills/huawei_ppt_master/core/deck_spec_field_dictionary.md`
- 图表语义映射规则：`skills/huawei_ppt_master/templates/chart_patterns.md` 中 `chart_semantic_mapping` 章节''')
    t += '\n- 想看“trend_curve 等图表如何证明 chart_proof_goal” → 读 `templates/chart_patterns.md` 的 `chart_semantic_mapping` 章节\n'
p.write_text(t, encoding='utf-8')

# PACKAGE_MANIFEST
p=Path('skills/huawei_ppt_master/PACKAGE_MANIFEST.md')
t=p.read_text(encoding='utf-8')
t=t.replace('Current package version: v0.3.8-deck-spec-field-dictionary','Current package version: v0.3.9-chart-semantic-mapping')
if '### 3.11 v0.3.9 chart_semantic_mapping 图表语义映射资产' not in t:
    t += '''\n\n### 3.11 v0.3.9 chart_semantic_mapping 图表语义映射资产\n\n本版本同步增强以下资产：\n\n- `core/output_contracts.md`：新增 `chart_semantic_mapping` 字段契约、触发规则和示例。\n- `prompts/deck_spec_generation.md`：要求 `trend_curve` 必须输出图表语义映射，高语义风险图表建议输出。\n- `templates/chart_patterns.md`：新增 `chart_semantic_mapping` 章节、六个核心字段和 `trend_curve` 示例。\n- `core/deck_spec_field_dictionary.md`：补充 `chart_semantic_mapping` 字段说明。\n- `eval/visual_scorecard.md`：新增 v0.3.9 图表语义映射检查与一票降级项。\n\n边界：该字段是 deck_spec 语义证明增强，不是渲染 DSL；不恢复 `page_render_spec` / `normalized_render_model` 方案。\n'''
p.write_text(t, encoding='utf-8')
