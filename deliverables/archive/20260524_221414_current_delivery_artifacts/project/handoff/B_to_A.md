# B_to_A 交接单

## 1. 基本信息

| 字段 | 内容 |
|---|---|
| task_id | SWE-ATLAS-VISUAL-CONSISTENCY-20260522-01 |
| 任务名称 | SWE Atlas 页面图片视觉资产一致性同步 |
| 当前阶段 | B_asset_sync_done_ready_for_A_regeneration |
| 交接方向 | 角色 B：huawei_ppt_skill_optimizer → 角色 A：huawei_ppt_master / Builder |
| Skill 版本 | v0.3.3-visual-consistency |
| 同步报告 | `project/review/review_reports/visual_asset_consistency_sync_v0.3.3.md` |

## 2. B 已完成

已根据用户要求，同步检查并修改与视觉迭代资产存在关联的文档，避免只改单点资产导致系统不一致。

核心修改包括：

1. 视觉规则：`templates/visual_rules.md`
2. 版式库：`visual_patterns/layout_library.md`
3. 图表模式：`templates/chart_patterns.md`
4. 视觉评分：`eval/visual_scorecard.md`
5. 页面设计 prompt：`prompts/generate_page_design.md`
6. 输出契约与生成流程：`core/output_contracts.md`、`core/generation_workflow.md`
7. deck_spec/self-review prompt：`prompts/deck_spec_generation.md`、`prompts/self_review.md`
8. 页型专项资产：总览、架构、对比、风险/问题诊断页
9. 验收、回归、README、INDEX、VERSION、CHANGELOG 等关联文档

## 3. 角色 A 下一步建议

请基于 v0.3.3 规则重新生成 SWE Atlas 页面设计与图片：

1. 重新生成 `page_design_v0.2.md`，每页必须包含：
   - `red_anchor`
   - `card_hierarchy`
   - `spacing_rule`
   - `bottom_bar_rule`
   - `visual_simplification`
2. 更新或重新生成 deck_spec，将视觉降噪要求同步进 `visual_notes`。
3. 交给 Builder 重新生成 P1-P5 页面图片。
4. 使用 `eval/visual_scorecard.md` 和 `eval/regression_cases.md` 执行视觉回归。

## 4. 回归重点

- P1：红色锚点减少，三卡统一，底部流程细线化；
- P2：泳道节点统一，右侧洞察栏压缩；
- P3：表格弱化，右侧指标卡承担结论；
- P4：三卡有主次，底部结论条降权；
- P5：闭环 4-5 节点，右侧行动 3-4 条，底部不压页面。

## 5. 阻塞项

无。
