# 防机械套版门禁 Phase 3 发布确认报告 v0.1

## 1. 结论

已进入 Phase 3，并确认 `huawei_ppt_master` 当前正式版本为：

`v0.4.0-anti-template-stamp-gate`

本轮没有重新生成交付物，也没有重复改写已落地规则；只做版本一致性核验、发布状态确认和交接更新。

## 2. 当前版本状态

| 检查项 | 结果 |
|---|---|
| `SKILL.md` 版本 | PASS：`0.4.0-anti-template-stamp-gate` |
| `VERSION.md` 当前版本 | PASS：`v0.4.0-anti-template-stamp-gate` |
| `README.md` v0.4.0 说明 | PASS |
| `CHANGELOG.md` v0.4.0 记录 | PASS |
| `PACKAGE_MANIFEST.md` 包版本 | PASS |
| `core/field_differentiation_rules.md` | PASS，正式资产存在 |
| `eval/template_stamp_detection.md` | PASS，正式资产存在 |
| `eval/acceptance_checklist.md` 防机械套版门禁 | PASS |
| `eval/visual_scorecard.md` 模板印章一票降级项 | PASS |
| manifest 文件存在性 | PASS，无缺失文件 |

## 3. Phase 3 发布定义

Phase 3 的含义是：将前序 Phase 1 已落地能力确认为稳定版本，并作为后续 `huawei_ppt_master` 默认执行规则。

稳定能力包括：

1. 字段差异化规则：`core/field_differentiation_rules.md`；
2. 模板印章检测：`eval/template_stamp_detection.md`；
3. 混合阈值模型：N<=3 两两比较，N>=4 使用 `repeat_threshold=max(3,ceil(N*0.5))`；
4. `core_judgement` 禁止字面复述，但允许正当提炼；
5. `chart_proof_goal` 必须说明主图证明关系；
6. `chart_visual_boundary` 必须结合本页图表风险和 `forbidden_visualization`；
7. page_design 允许下沉为 `global_design_defaults + page_design_overrides`，但必须保留每页独立可读视图。

## 4. 已存在的 Phase 1 验证基线

Phase 1 已完成旧样例 dry-run：

- 报告：`project/review/review_reports/anti_template_stamp_gate_phase1_dry_run_v0.1.md`
- 旧 P4/P7/P8/P14：FAIL 6 / WARN 5 / ALLOW-WARN 1
- 结论：旧样例能被 v0.4.0 门禁识别为不合格，满足 RT-00 预期。

同时，后续 `AI_MBSE v0.4.0` 全链路交付已经通过模板印章检测：

- `project/work/self_check_v0.1.md`
- N=12，threshold=6
- `core_judgement` / `chart_proof_goal` / `chart_visual_boundary` / `visual_notes` / `speaker_notes` 均 PASS

## 5. 边界

Phase 3 不改变以下边界：

- 不恢复 `page_render_spec`；
- 不恢复 `normalized_render_model`；
- 不新增渲染 DSL；
- 不要求所有字段都差异化；
- 不把华为风格一致性误判为机械套版。

## 6. 后续建议

后续所有 `huawei_ppt_master` 全链路执行默认使用 v0.4.0 门禁。

如果角色 C 只做 PPT 图片生成，最小依赖仍建议保持：

- `deck_spec_v0.1.json`
- `page_design_v0.1.md`
- `page_copy_v0.1.md`
- `dependencies/deck_spec_field_dictionary.md`
- `dependencies/templates/chart_patterns.md`
- `dependencies/templates/visual_rules.md`
- `dependencies/visual_patterns/layout_library.md`

如需保留 v0.4.0 防套版检查，再追加：

- `dependencies/field_differentiation_rules.md`
- `dependencies/template_stamp_detection.md`
