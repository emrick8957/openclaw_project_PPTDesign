# Skill 优化评审报告：防机械套版门禁 patch v0.1

## 1. 基本信息

- 评审角色：B（huawei_ppt_skill_optimizer）
- 评审对象：`project/review/patch_proposals/anti_template_stamp_gate_patch_v0.1.md`
- 关联交付物证据：`project/work/AI4MBSE_P4_P7_P8_P14_delivery/`（deck_spec.json / page_copy.md / page_design.md / self_check.md）
- 目标版本：`v0.4.0-anti-template-stamp-gate`
- 评审日期：2026-05-29
- 当前 Skill 版本：v0.3.9-chart-semantic-mapping

## 2. 被评审对象

patch 主张：在现有证明契约（`core_judgement`/`chart_proof_goal`/`chart_visual_boundary`/`chart_semantic_mapping`）之上，新增"字段差异化 + 模板印章检测 + page_design 下沉"门禁，防止交付物**通过结构校验但缺少逐页设计决策**。

新增文件 2 个（`core/field_differentiation_rules.md`、`eval/template_stamp_detection.md`），修改文件 7 个，版本同步文件 6 个，含回归用例与"不做事项"边界。

## 3. 总体结论

- 结论：**有条件合入**（conditional merge）。
- 评分：**88 / 100**（≥85，可合入；无 P0）。
- 一句话判断：问题识别与归因准确、证据扎实、边界克制，是真问题真修；但**门禁判据偏主观、阈值对非 4 页交付不鲁棒、与既有未被执行的契约规则未做根因对齐**，需在落地前补齐 4 项条件，否则门禁本身会变得"时灵时不灵"，反而引入新的不稳定。

## 4. 问题清单（针对 patch 本身）

| ID | 严重度 | 位置 | 问题 |
|---|---|---|---|
| R-01 | P1 | FAIL/WARN 规则、回归用例 | "≥3 页逐字相同"为**绝对页数阈值**，对 ≤3 页交付永远漏检，对大 deck（如 14 页）又可能误伤；缺少按比例/小包的处理规则 |
| R-02 | P1 | template_stamp_detection 全文 | "骨架填词""伪差异化""未说明因果/对比/演进关系"等为**语义判断**，但未给可操作判据或正反例，自检（由 LLM 执行）难以一致复现 → 门禁结果不稳定 |
| R-03 | P2 | field_differentiation_rules §2 | `core_judgement` 强制"不得等于 conclusion 且必须加动作/取舍/管理含义"可能**过度差异化**：背景/上下文页（如 P4）的判断本就≈结论，硬加动作会制造冗余，违反 patch 自身"不把一致性误判为套版"的边界 |
| R-04 | P2 | 与 deck_spec_generation.md 既有规则 | 现有 rule 8（visual_notes 须逐页吸收红锚/层级/间距）与 rule 11（chart_visual_boundary 3–5 条）**本应阻止雷同却未生效**；patch 只加检测未做根因对齐，未把检测设为 §12 自检门禁的强制步骤，可能像旧规则一样被跳过 |
| R-05 | P2 | 新增 2 文件内容重叠 | `field_differentiation_rules.md`（core）与 `template_stamp_detection.md`（eval）各自列"必须差异化字段清单 + FAIL 条件"，两份清单将来易漂移、不一致 |
| R-06 | P3 | 允许重复白名单 §2.1 | 未豁免 `chart_data` 的**结构性骨架重复**（如多页 layered_stack_diagram 的层级键名、decision_table 列名相似），可能误判 |
| R-07 | P3 | page_design 下沉结构 | `global_design_defaults` + `page_design_overrides` 改变了 page_design 形态，而下游是"外部模型读 page_design 生图"；若提示词流程按"每页完整段落"消费，下沉后会丢失每页上下文 |

## 5. 问题归因

| ID | 归因 |
|---|---|
| R-01 | `qa_gate_gap`：门禁阈值设计不完整 |
| R-02 | `qa_gate_gap`：缺少可执行判据与样例，检测可复现性不足 |
| R-03 | `output_contract_gap`：字段语义边界定义偏激进 |
| R-04 | `qa_gate_gap` + `skill_rule_conflict`：新门禁与既有未执行规则未对齐，执行触点不明确 |
| R-05 | `output_contract_gap`：规则真相源未单一化 |
| R-06 | `qa_gate_gap`：白名单覆盖不全 |
| R-07 | 下游消费兼容性风险（A→外部生图边界） |

## 6. improvement_backlog（合入前必须处理）

- BL-01（对应 R-01）：阈值改为 `判定页数 = max(3, ceil(N×0.5))`；并显式定义 N≤3 时退化为"逐页两两比对，任意字段全同即 WARN，关键差异化字段全同即 FAIL"。
- BL-02（对应 R-02）：在 `template_stamp_detection.md` 为每个关键字段补 2 正 2 反例（尤其 `core_judgement`、`chart_proof_goal`），作为自检 few-shot 锚点。
- BL-03（对应 R-03）：将 `core_judgement` 规则从"必须加动作含义"放宽为"不得为 `前缀+conclusion` 的字面复述；允许是对 conclusion 的提炼/收口，但须是不同表述且承载唯一带走点"。区分"复述"与"正当提炼"。
- BL-04（对应 R-04）：把模板印章检测写入 `SKILL.md` §12 自检门禁作为**强制后置步骤**（不仅放进强制读取顺序）；并在 patch 中说明既有 rule 8/11 未生效的根因＝缺执行触点，本次一并补。
- BL-05（对应 R-05）：字段差异化清单**只在 `core/field_differentiation_rules.md` 维护一份**，`eval/template_stamp_detection.md` 仅引用不复制。
- BL-06（对应 R-06）：白名单补充"`chart_data` 结构骨架（键名/列名）允许相似，仅判语义内容"。
- BL-07（对应 R-07）：保留"每页可被独立完整读取"的渲染视图，或确认外部生图提示词模板兼容"全局默认+偏离项"结构后再下沉。

## 7. patch proposal 摘要评价

- 新增/修改文件的插入点经核对**全部真实存在**（`output_contracts.md` 4.0/4.3、`deck_spec_generation.md`「生成时必须检查」、`acceptance_checklist.md` §1–8 后接 §9、`visual_scorecard.md`、`visual_rules.md`、`wording_rules.md`），可直接落地。
- 版本同步文件清单完整（README/VERSION/CHANGELOG/INDEX/QUICK_INDEX/PACKAGE_MANIFEST），符合既往版本管理纪律。
- "不做事项"明确（不复活 page_render_spec / normalized_render_model / 渲染 DSL；不要求全字段差异化），边界克制，安全。

## 8. 回归测试建议

- 保留 patch 的 4.1（旧样例必须 FAIL）/4.2（新样例必须 PASS），但补充：
  - RT-01：构造 1 个 **3 页**交付样例，验证 BL-01 小包退化规则能命中 FAIL。
  - RT-02：构造 1 个 **14 页**样例，其中仅 3 页 visual_notes 相同但已拆全局默认，验证不误判（PASS）。
  - RT-03：背景页 `core_judgement` 为 conclusion 的正当提炼（非字面复制），验证 BL-03 不误伤（PASS）。
  - RT-04：多页同 `chart_type` 但 `chart_data` 键名结构相似、语义不同，验证 BL-06 白名单（PASS）。

## 9. 合入判断

- 判断：**有条件合入**。
- 合入条件：完成 BL-01 ~ BL-05（P1/P2 全部）后方可合入；BL-06/BL-07（P3）可在合入同批或紧随其后处理。
- 风险等级：中低。无 P0、无主题污染、无安全边界破坏。主要风险是"门禁可复现性"，由 BL-01/BL-02 化解。

## 10. B_to_A 交接摘要

- 本次评审针对"防机械套版门禁 patch v0.1"，结论为**有条件合入（88/100）**。
- A 侧落地前需吸收 5 条 P1/P2 改造：阈值按比例化、补字段正反例、放宽 core_judgement、把检测设为强制自检步骤、字段清单单一真相源。
- 落地后必须用 `AI4MBSE_P4_P7_P8_P14_delivery` 作为"必须 FAIL"回归基线，并新增小包/大包/正当提炼/结构骨架四类用例。
- 不得借本次改造复活 page_render_spec / normalized_render_model 或新增渲染 DSL。
