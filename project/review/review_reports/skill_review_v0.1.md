# Skill 优化评审报告

## 1. 基本信息
- 任务名称：华为云竞争力深度洞察
- task_id：HC-20260504-01
- 评审角色：B / huawei_ppt_skill_optimizer
- 评审对象：角色 A 当前 v0.1 交付物
- 评审范围：`project/work/outline_v0.1.md`、`project/work/page_copy_v0.1.md`、`project/work/page_design_v0.1.md`、`project/work/deck_spec_v0.1.json`、`project/handoff/A_to_B.md`

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
- Builder 输入可用性：基本可用，但存在字段规范风险

## 3. 总体结论
本次 A 交付整体完成度较高，华为高层汇报风格明确，结构完整，结论链较清晰，且已较好控制非 AI 主题污染。

但从 Skill 优化视角看，当前暴露出两类值得沉淀的问题：
1. **输出契约层问题**：`deck_spec.json` 中 `chart_type` 与 `layout_pattern` 的边界不够稳定，存在把版式名写入图表类型的情况，后续容易影响 Builder 兼容性。
2. **门禁层问题**：对高判断强度页面，当前 Skill 缺少“证据强度/措辞强度”约束，导致在缺少权威数据时仍容易输出较强判断。

结论：
- 对本次 A 输出：**建议 A 轻量返工后进入角色 C**。
- 对本 Skill：**建议有条件合入优化项**。

## 4. 问题清单

### ISSUE-001
- 问题位置：`project/work/deck_spec_v0.1.json`
- 问题描述：`chart_type` 与 `layout_pattern` 存在命名边界不清。部分页面的 `chart_type` 实际填写为版式模式，如 `executive_summary_dashboard`、`roadmap_timeline`、`three_column_cards`、`trend_curve_with_strategy`。
- 影响：会削弱 `deck_spec` 作为中间契约的稳定性；增加 Builder 对隐式映射的依赖。
- 问题归因：`output_contract_gap`
- 修改建议：在 Skill 中新增 `chart_type` 与 `layout_pattern` 的标准枚举边界，并在验收清单中增加一致性检查。
- 优先级：P1
- 是否沉淀为 Skill：是
- 是否加入回归测试：是

### ISSUE-002
- 问题位置：P4 / P5 / P8 / P9 / P10 文案与结论页
- 问题描述：多处页面结论判断较强，但支撑材料仍以 `data_gaps` 方式后置标注，缺少对“判断强度是否应降级”的硬约束。
- 影响：在缺少外部研究或内部证据时，易形成“结构正确但事实支撑偏弱”的输出。
- 问题归因：`qa_gate_gap`
- 修改建议：在 Skill 中增加“高断言页面证据门禁”：若缺少材料，必须采用方向性、框架性表述，不得写成已证实判断。
- 优先级：P1
- 是否沉淀为 Skill：是
- 是否加入回归测试：是

### ISSUE-003
- 问题位置：P13 / P14 / P15
- 问题描述：资源投入、责任主体、时间节点、验收口径仍缺实参，现阶段多为框架建议。
- 影响：影响落地性，但不构成当前 Skill 通用规则缺陷。
- 问题归因：`input_material_missing`
- 修改建议：补充内部专项、预算口径、组织归口、阶段节点信息。
- 优先级：P1
- 是否沉淀为 Skill：否
- 是否加入回归测试：否

### ISSUE-004
- 问题位置：P4 / P5 / P8 / P9 / P10
- 问题描述：外部格局、竞争短板与优势判断仍偏框架化，缺少案例、公开研究或内部证据托底。
- 影响：影响说服力，但更偏单次任务资料不足。
- 问题归因：`input_material_missing`
- 修改建议：按 A_to_B 中待补材料清单补证据，再决定措辞强度。
- 优先级：P1
- 是否沉淀为 Skill：否
- 是否加入回归测试：否

## 5. 问题归因
- Skill 规则缺口：2 项（ISSUE-001、ISSUE-002）
- 输入材料不足：2 项（ISSUE-003、ISSUE-004）
- 单次执行偏差：0 项
- 主题污染：0 项
- 安全边界问题：0 项

## 6. improvement_backlog
建议沉淀以下 backlog：
- HPPT-001：标准化 `deck_spec` 的 `chart_type` / `layout_pattern` 契约
- HPPT-002：为高断言页面增加证据强度门禁和措辞降级规则

## 7. patch proposal 摘要
建议修改以下文件（仅 patch proposal，不直接改 Skill）：
1. `skills/huawei_ppt_master/core/output_contracts.md`
2. `skills/huawei_ppt_master/eval/acceptance_checklist.md`
3. `skills/huawei_ppt_master/templates/wording_rules.md`
4. `skills/huawei_ppt_master/eval/regression_cases.md`

## 8. 回归测试建议
1. 非 AI 主题污染测试：华为云/数据治理/安全主题不得出现算力专属术语
2. `deck_spec` 契约测试：`chart_type` 必须为图表类型，`layout_pattern` 必须为版式类型
3. 高断言页面证据测试：缺证据时是否自动降级为方向性表述
4. Builder 可执行性测试：以当前云竞争力题目验证 `page_images/pptx` 输入可执行

## 9. 合入判断
### 对 A 输出
- 是否建议进入角色 C：**有条件进入**
- 是否需要 A 返工：**需要轻量返工**
- 返工重点：
  1. 统一 `deck_spec` 中 `chart_type` 命名
  2. 对证据不足页面适度降低断言强度或补材料

### 对 Skill 优化建议
- 合入判断：**有条件合入**
- 理由：总分达到可合入区间；无 P0；问题具备通用价值；但需通过回归测试后再正式合入。

## 10. B_to_A 交接摘要
A 当前交付完整，主线清晰，主题控制良好。
建议优先轻量修正两点：
1. `deck_spec` 的 `chart_type` 命名规范；
2. P4/P5/P8/P9/P10 在证据不足时的措辞强度。
修正后即可更稳地进入角色 C。

## 评分
| 维度 | 分值 | 得分 |
|---|---:|---:|
| 问题识别准确性 | 15 | 13 |
| 问题归因准确性 | 15 | 13 |
| Skill 优化价值 | 15 | 14 |
| patch proposal 可执行性 | 15 | 13 |
| 对现有能力的兼容性 | 10 | 9 |
| 回归测试完整性 | 10 | 8 |
| 主题污染控制 | 10 | 10 |
| 安全边界保持 | 10 | 10 |
| **总分** | **100** | **90** |
