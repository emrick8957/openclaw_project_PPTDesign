# chart_data 字段可见性 v0.4.1 Phase 1 落地报告

## 1. 任务

用户确认 `chart_data_field_rules_and_visibility_patch_v0.2.md` 评审通过，要求进入 Phase 1 小版本落地。

本轮已将 `huawei_ppt_master` 正式升级为：

`v0.4.1-chart-data-visibility`

## 2. 落地范围

正式修改 `skills/huawei_ppt_master/*`，将 v0.2 proposal 中的字段可见性规则落入 Skill 正式资产。

### 2.1 核心规则落地

- `group`、`emphasis`、`source_status` 等 logic-only 字段不得字面上屏；
- 可见分组标题应使用 `label`、`name`、`headline`、`display_text`、`lane.name`、`layer.name`、`stage.name` 等显示内容字段；
- `edges.label` 可见，但只能承载短动作词或短关系词；
- 复杂方向、同层对应、层级支撑、闭环回写等关系语义必须进入 `chart_semantic_mapping`；
- 可见字段需短语化，长解释进入 `description`、`speaker_notes` 或 `chart_semantic_mapping`；
- 禁止在 `chart_data` 内新增 `relation_type`、`edge_style`、`position`、`anchor`、`x/y`、`layer_index` 等关系或渲染 DSL 字段。

## 3. 修改文件

### 3.1 正式规则与生成链路

- `skills/huawei_ppt_master/SKILL.md`
  - 版本升级为 `0.4.1-chart-data-visibility`；
  - 强制读取顺序加入 `core/deck_spec_field_dictionary.md`；
  - deck_spec 硬规则加入 chart_data 字段可见性约束；
  - chart_type 规则加入可见字段短语化与 `edges.label` 边界。

- `skills/huawei_ppt_master/core/deck_spec_field_dictionary.md`
  - 新增 `## 4. chart_data 字段通则与可见性约定`；
  - 定义字段分层、logic-only 字段清单、可见分组标题、`edges.label` 边界、短语化判据和关系语义承载位置。

- `skills/huawei_ppt_master/core/output_contracts.md`
  - deck_spec 强门禁新增第 18~21 条：logic-only 字段不上屏、可见分组字段、`edges.label` 边界、禁止关系/渲染 DSL 字段。

- `skills/huawei_ppt_master/templates/chart_patterns.md`
  - 在 chart_type 与 layout_pattern 边界附近新增 `chart_data 字段可见性边界`。

- `skills/huawei_ppt_master/prompts/deck_spec_generation.md`
  - 生成检查新增 logic-only、可见分组、`edges.label`、短语化和 DSL 禁止项。

### 3.2 验收与回归

- `skills/huawei_ppt_master/eval/acceptance_checklist.md`
  - 新增 `## 10. chart_data 字段可见性门禁`。

- `skills/huawei_ppt_master/eval/regression_cases.md`
  - 新增 Test 8~11：group 不上屏、可见分组不用 group、edges.label 与关系语义归位、section 只弱显示为页眉。

- `skills/huawei_ppt_master/eval/visual_scorecard.md`
  - 新增 `## O. chart_data 字段可见性一票降级项`。

### 3.3 版本同步

- `skills/huawei_ppt_master/README.md`
- `skills/huawei_ppt_master/VERSION.md`
- `skills/huawei_ppt_master/CHANGELOG.md`
- `skills/huawei_ppt_master/INDEX.md`
- `skills/huawei_ppt_master/QUICK_INDEX.md`
- `skills/huawei_ppt_master/PACKAGE_MANIFEST.md`

## 4. 边界确认

本轮没有恢复或新增以下内容：

- 未恢复 `page_render_spec`；
- 未恢复 `normalized_render_model`；
- 未新增 PPTX 渲染 DSL；
- 未新增 shape plan；
- 未把 `deck_spec.json` 变成 C 端渲染协议；
- 未允许 `relation_type`、`edge_style`、`position`、`anchor`、`x/y`、`layer_index` 等字段进入 `chart_data`。

## 5. 验证结果

已执行本地一致性检查：

```text
PASS: v0.4.1 required markers present
PASS: no stale current-version markers in primary metadata
```

检查覆盖：

- `SKILL.md` frontmatter 版本；
- `deck_spec_field_dictionary.md` 新章节；
- `output_contracts.md` 强门禁；
- `chart_patterns.md` 字段可见性边界；
- `deck_spec_generation.md` 生成检查；
- `acceptance_checklist.md`、`regression_cases.md`、`visual_scorecard.md` 验收/回归/降级项；
- `VERSION.md` 与 `PACKAGE_MANIFEST.md` 当前版本标识。

## 6. 结论

Phase 1 小版本落地完成。

`huawei_ppt_master` 当前正式版本：

`v0.4.1-chart-data-visibility`

建议下一步进入 Phase 2：用一份包含 `group`、`edges.label`、`section`、`chart_semantic_mapping` 的小型 deck_spec 样例做 dry-run，验证字段可见性门禁是否能被角色 C 正确消费。
