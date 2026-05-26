# Skill 优化评审报告

## 1. 基本信息
- 任务名称：华为云竞争力深度洞察
- task_id：HC-20260504-02
- 评审角色：B / huawei_ppt_skill_optimizer
- 评审对象：角色 A 当前 v0.2 交付物
- 评审范围：`project/work/outline_v0.2.md`、`project/work/page_copy_v0.2.md`、`project/work/page_design_v0.2.md`、`project/work/deck_spec_v0.2.json`、`project/handoff/A_to_B.md`

## 2. 被评审对象
### 已读取交付物
1. PPT 大纲：已完成
2. 逐页文案：已完成
3. 页面设计说明：已完成
4. deck_spec.json：已完成，且可解析
5. A_to_B 交接单：已完成
6. 交付包：已完成

### 交付完整性判断
- 结构完整：是
- 章节结构完整：是
- 高层汇报主线明确：是
- 主题污染：未发现
- Builder 输入可用性：较 v0.1 提升，但仍有命名契约问题

## 3. 总体结论
v0.2 相比 v0.1 有明确改进：
1. 页数从 16 页压缩到 15 页，结构更紧；
2. 高断言页面已普遍加入“当前判断看 / 初步看 / 若后续材料验证成立”等降级措辞；
3. 高层视角更稳定，体系化经营主线更集中。

但仍存在一个需要优先修正的问题：`deck_spec.json` 中 `chart_type` 与 `layout_pattern` 的边界仍未完全统一，部分页面仍把版式模式写入 `chart_type`。

结论：
- 对本次 A 输出：**建议轻量修正后进入角色 C**。
- 对本 Skill：**继续建议有条件合入优化项**。

## 4. 问题清单

### ISSUE-001
- 问题位置：`project/work/deck_spec_v0.2.json`
- 问题描述：`chart_type` 与 `layout_pattern` 仍存在混用。典型页面包括：P2、P4、P6、P7、P11，其中 `chart_type` 分别写成 `executive_summary_dashboard`、`trend_curve_with_strategy`、`four_quadrant_judgement`、`three_column_cards`、`roadmap_timeline`，这些更像版式模式而非图表类型。
- 影响：削弱 deck_spec 作为 Builder 中间契约的稳定性，后续实现需要做隐式映射。
- 问题归因：`output_contract_gap`
- 修改建议：统一 `chart_type` 为图表/信息结构类型，保留 `layout_pattern` 承载版式模式。
- 优先级：P1
- 是否沉淀为 Skill：是
- 是否加入回归测试：是

### ISSUE-002
- 问题位置：P4 / P5 / P7 / P8 / P9 / P13-P15
- 问题描述：措辞强度已较 v0.1 明显收敛，但外部格局、优势短板、资源拍板页仍主要依赖框架判断，证据仍不足。
- 影响：事实风险已下降，但说服力仍受限。
- 问题归因：`input_material_missing`
- 修改建议：按 A_to_B 待补材料补外部研究、案例、内部经营数据与责任归口信息。
- 优先级：P1
- 是否沉淀为 Skill：否
- 是否加入回归测试：否

### ISSUE-003
- 问题位置：P13 / P14 / P15
- 问题描述：资源投入、责任方向、阶段时点与验收标准仍偏框架化，未绑定真实组织口径。
- 影响：影响决策页的落地性与执行性。
- 问题归因：`input_material_missing`
- 修改建议：补充牵头单位、阶段指标、评估时点、资源口径。
- 优先级：P1
- 是否沉淀为 Skill：否
- 是否加入回归测试：否

## 5. 问题归因
- Skill 规则缺口：1 项（ISSUE-001）
- 输入材料不足：2 项（ISSUE-002、ISSUE-003）
- 单次执行偏差：0 项
- 主题污染：0 项
- 安全边界问题：0 项

## 6. improvement_backlog
建议保留并继续推进以下 backlog：
- HPPT-001：标准化 `deck_spec` 的 `chart_type` / `layout_pattern` 契约
- HPPT-002：高断言页面证据强度门禁

其中 HPPT-002 在 v0.2 已看到明显改进，说明方向正确；HPPT-001 仍未闭环。

## 7. patch proposal 摘要
建议修改以下文件（仅 patch proposal，不直接改 Skill）：
1. `skills/huawei_ppt_master/core/output_contracts.md`
2. `skills/huawei_ppt_master/eval/acceptance_checklist.md`
3. `skills/huawei_ppt_master/eval/regression_cases.md`

## 8. 回归测试建议
1. 非 AI 主题污染测试：当前题目及非云主题题目均不得出现算力专属术语
2. `deck_spec` 契约测试：`chart_type` 不得填写版式模式
3. 高断言页面测试：无证据时必须自动降级为方向性表达
4. Builder 可执行性测试：抽检 P2、P4、P6、P7、P11 的字段一致性

## 9. 合入判断
### 对 A 输出
- 是否建议进入角色 C：**有条件进入**
- 是否需要 A 返工：**需要极轻量返工**
- 返工重点：
  1. 修正 `deck_spec` 中 P2/P4/P6/P7/P11 的 `chart_type`
  2. 如时间允许，继续补 P13-P15 的责任与验收实参

### 对 Skill 优化建议
- 合入判断：**有条件合入**
- 理由：无 P0；v0.2 已验证证据门禁方向有效；但 `deck_spec` 契约问题仍需用规则和回归测试彻底钉住。

## 10. B_to_A 交接摘要
v0.2 已较 v0.1 明显收敛并变稳，主线和措辞控制都有进步。当前最需要修的是 `deck_spec` 命名契约，不是重做内容。修正后即可更稳地进入角色 C。

## 评分
| 维度 | 分值 | 得分 |
|---|---:|---:|
| 问题识别准确性 | 15 | 14 |
| 问题归因准确性 | 15 | 14 |
| Skill 优化价值 | 15 | 14 |
| patch proposal 可执行性 | 15 | 14 |
| 对现有能力的兼容性 | 10 | 9 |
| 回归测试完整性 | 10 | 9 |
| 主题污染控制 | 10 | 10 |
| 安全边界保持 | 10 | 10 |
| **总分** | **100** | **94** |
