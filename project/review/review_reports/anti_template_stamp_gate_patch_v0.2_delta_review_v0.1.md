# anti_template_stamp_gate_patch_v0.2 差异评审 v0.1

## 1. 结论

`anti_template_stamp_gate_patch_v0.2.md` 已吸收上一轮评审中 P1/P2 的主要问题，适合作为下一轮正式评审对象；但本轮仍不建议直接落地到 `skills/huawei_ppt_master/*`。

## 2. v0.2 已吸收项

| Backlog | v0.2 处理情况 | 评估 |
|---|---|---|
| BL-01 阈值模型 | 从固定 `>=3` 改为混合阈值：N<=3 两两比较；N>=4 使用 `repeat_threshold=max(3,ceil(N*0.5))` | 已处理 |
| BL-02 正反例 | 为 `core_judgement`、`chart_proof_goal`、`chart_visual_boundary` 增加 FAIL/PASS 特征与正反例 | 已处理 |
| BL-03 core_judgement 放宽 | 从“必须动作化”改为“禁止字面复述，允许正当提炼” | 已处理 |
| BL-04 强制后置自检 | 要求生成后执行模板印章检测，并在 self_check 输出统计/复述/骨架/增量/允许重复项 | 已处理 |
| BL-05 单一真相源 | 字段差异化清单只在 `core/field_differentiation_rules.md` 维护，eval 文件引用 | 已处理 |
| BL-06 chart_data 白名单 | 明确 chart_data 键名/列名/结构骨架相似不直接判 FAIL，只判语义内容 | 已处理 |
| BL-07 page_design 兼容 | 增加 `page_design_view(Pn)=global_defaults+overrides(Pn)`，保留每页独立可读视图 | 已处理 |

## 3. 相对 v0.1 的关键改进

1. **阈值更鲁棒**：解决小包漏检和大包误伤。
2. **语义判断更可复现**：从抽象词“骨架填词/伪差异化”变成可判定特征 + 正反例。
3. **不过度差异化**：允许背景页做正当提炼，不强制动作化。
4. **执行触点更明确**：不仅要求读取规则，还要求生成后 self_check 必须执行并输出结果。
5. **规则真相源更清晰**：core 管字段职责，eval 管检测执行。
6. **下游兼容性更好**：page_design 可下沉，但仍保留每页完整可读视图。

## 4. 仍需下一轮评审关注

- few-shot 示例数量是否足够，是否需要扩展到 `speaker_notes` 和 page_copy；
- 混合阈值对 5~6 页短 deck 是否仍过严；
- `visual_notes` 与 page_design overrides 的字段形态是否需要在 output contract 中进一步标准化；
- 如果未来落地，必须同步 README / VERSION / CHANGELOG / INDEX / QUICK_INDEX / PACKAGE_MANIFEST。

## 5. 建议

建议把 v0.2 作为下一轮评审对象。若评审通过，再进入 Phase 1 最小资产落地；当前仍保持“不修改正式 Skill”。
