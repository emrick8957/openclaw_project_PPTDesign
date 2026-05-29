# B_to_A：防机械套版门禁 patch v0.2 交接

## 当前状态

已按用户“OK继续”完成 `anti_template_stamp_gate_patch_v0.2.md`。

本轮仍未修改正式 Skill 资产：`skills/huawei_ppt_master/*` 未改动。

## 新增产出

1. v0.2 patch proposal：
   - `project/review/patch_proposals/anti_template_stamp_gate_patch_v0.2.md`
2. v0.2 差异评审：
   - `project/review/review_reports/anti_template_stamp_gate_patch_v0.2_delta_review_v0.1.md`

## v0.2 吸收内容

已吸收上一轮评审的 P1/P2/P3 关键建议：

- BL-01：阈值从固定 `>=3` 改为混合阈值：
  - N<=3：两两比较；
  - N>=4：`repeat_threshold=max(3,ceil(N*0.5))`。
- BL-02：补充 `core_judgement`、`chart_proof_goal`、`chart_visual_boundary` 的 FAIL/PASS 特征与正反例。
- BL-03：`core_judgement` 放宽为“禁止字面复述，允许正当提炼”。
- BL-04：模板印章检测作为强制后置自检，并要求 self_check 输出检测结果。
- BL-05：字段差异化清单单一真相源：`core/field_differentiation_rules.md`。
- BL-06：`chart_data` 结构骨架相似不误判。
- BL-07：page_design 下沉时保留每页独立可读视图。

## 建议下一步

建议对 v0.2 做一轮正式评审。评审通过后，再决定是否进入 Phase 1 最小资产落地。

不建议直接跳过评审落地。

## 边界

- 不恢复 `page_render_spec`；
- 不恢复 `normalized_render_model`；
- 不新增渲染 DSL；
- 不要求所有字段都差异化；
- 当前仍是 proposal，不是正式 Skill 修改。
