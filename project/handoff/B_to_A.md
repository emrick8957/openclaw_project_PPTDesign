# B_to_A：v0.4.1-chart-data-visibility Phase 1 落地完成

## 当前状态

用户确认 `chart_data_field_rules_and_visibility_patch_v0.2.md` 评审通过，并要求进入 Phase 1 小版本落地。

已完成正式 Skill 修改，当前版本：

`v0.4.1-chart-data-visibility`

## 落地报告

- `project/review/review_reports/chart_data_visibility_phase1_landing_report_v0.1.md`

## 正式修改文件

- `skills/huawei_ppt_master/SKILL.md`
- `skills/huawei_ppt_master/core/deck_spec_field_dictionary.md`
- `skills/huawei_ppt_master/core/output_contracts.md`
- `skills/huawei_ppt_master/templates/chart_patterns.md`
- `skills/huawei_ppt_master/prompts/deck_spec_generation.md`
- `skills/huawei_ppt_master/eval/acceptance_checklist.md`
- `skills/huawei_ppt_master/eval/regression_cases.md`
- `skills/huawei_ppt_master/eval/visual_scorecard.md`
- `skills/huawei_ppt_master/README.md`
- `skills/huawei_ppt_master/VERSION.md`
- `skills/huawei_ppt_master/CHANGELOG.md`
- `skills/huawei_ppt_master/INDEX.md`
- `skills/huawei_ppt_master/QUICK_INDEX.md`
- `skills/huawei_ppt_master/PACKAGE_MANIFEST.md`

## 核心规则

- logic-only 字段：`group`、`emphasis`、`source_status` 不得字面上屏；
- 可见分组标题使用 `label/name/headline/display_text/lane.name/layer.name/stage.name`；
- `edges.label` 只能承载短动作词或短关系词；
- 复杂关系语义进入 `chart_semantic_mapping`；
- 禁止 `relation_type`、`edge_style`、`position`、`anchor`、`x/y`、`layer_index` 等关系/渲染 DSL 字段进入 `chart_data`。

## 验证

```text
PASS: v0.4.1 required markers present
PASS: no stale current-version markers in primary metadata
```

## 建议下一步

进入 Phase 2 dry-run：构造一个包含 `group`、`edges.label`、`section`、`chart_semantic_mapping` 的小型 deck_spec 样例，验证角色 C 消费边界。
