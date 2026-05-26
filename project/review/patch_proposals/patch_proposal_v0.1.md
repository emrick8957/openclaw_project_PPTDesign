# Patch Proposal v0.1

## 1. 基本信息
- 当前任务: 华为云竞争力深度洞察
- patch 编号: PP-20260504-01
- 生成时间: 2026-05-04

## 2. 修改摘要
| 修改文件 | 修改类型 | 对应 issue_id | 优先级 |
|---|---|---|---|
| `skills/huawei_ppt_master/core/output_contracts.md` | 规则增强 | ISSUE-001 | P1 |
| `skills/huawei_ppt_master/eval/acceptance_checklist.md` | 门禁增强 | ISSUE-001, ISSUE-002 | P1 |
| `skills/huawei_ppt_master/templates/wording_rules.md` | 规则增强 | ISSUE-002 | P1 |
| `skills/huawei_ppt_master/eval/regression_cases.md` | 回归补充 | ISSUE-001, ISSUE-002 | P1 |

## 3. 详细补丁

### 修改文件：`skills/huawei_ppt_master/core/output_contracts.md`

#### 对应问题
- issue_id: ISSUE-001
- backlog_id: HPPT-001

#### 原规则或缺失点
> 当前仅要求 `deck_spec.json` 包含 `chart_type`、`layout_pattern`，但未明确两者的命名边界与标准类型，易产生混用。

#### 建议新增/修改内容
```markdown
### 4.1 deck_spec 字段边界补充
- `chart_type` 表示图表/信息结构类型，不得直接填写版式模式名。
- `layout_pattern` 表示页面布局模式，必须来自 `visual_patterns/layout_library.md` 或已登记的版式库。

推荐 `chart_type` 示例：
- executive_summary
- comparison_matrix
- capability_map
- gap_heatmap
- decision_table
- risk_matrix
- roadmap
- timeline
- value_closure_loop
- ecosystem_map
- layered_architecture
- none

推荐 `layout_pattern` 示例：
- executive_summary_dashboard
- two_column_comparison
- four_quadrant_judgement
- three_column_cards
- insight_panel_with_chart
- roadmap_timeline
- trend_curve_with_strategy
- risk_decision_matrix
- stack_architecture_with_right_insights
- cover
```

#### 修改理由
明确中间契约边界，降低 Builder 隐式适配风险。

#### 影响范围
- deck_spec 生成
- Builder 输入稳定性
- 回归测试口径

#### 回归测试
- 检查 `chart_type` 是否误填为 `layout_pattern`
- 检查 `layout_pattern` 是否来自版式库

### 修改文件：`skills/huawei_ppt_master/eval/acceptance_checklist.md`

#### 对应问题
- issue_id: ISSUE-001
- backlog_id: HPPT-001
- issue_id: ISSUE-002
- backlog_id: HPPT-002

#### 原规则或缺失点
> 当前验收清单未覆盖字段边界一致性，也未覆盖高断言页面的证据强度门禁。

#### 建议新增/修改内容
```markdown
## 6. deck_spec 契约检查
- `chart_type` 是否为图表类型，而非版式模式；
- `layout_pattern` 是否为版式模式，且可在版式库中找到；
- 图表类型与版式模式是否匹配；
- Builder 是否可直接据此生成 page_images / pptx。

## 7. 高断言页面证据门禁
对于外部格局判断、竞品对比、优势/短板诊断、资源建议等高断言页面：
- 如无公开研究、内部材料或案例支撑，必须使用方向性表述；
- 不得把推测写成已证实事实；
- 必须在 `data_gaps` 中明确缺口；
- 必要时在结论中加入“当前判断”“初步判断”“待补材料后确认”等降级措辞。
```

#### 修改理由
把隐性经验变成显式门禁。

#### 影响范围
- A 自检质量
- B 归因效率
- 事实风险控制

#### 回归测试
- 无证据题目下是否自动降级措辞
- deck_spec 契约检查是否能识别混用

### 修改文件：`skills/huawei_ppt_master/templates/wording_rules.md`

#### 对应问题
- issue_id: ISSUE-002
- backlog_id: HPPT-002

#### 原规则或缺失点
> 当前文案规则强调“强判断”，但缺少“证据不足时应如何降级”的配套规则。

#### 建议新增/修改内容
```markdown
## 6. 证据不足时的措辞规则
当用户未提供充分数据、公开研究或内部材料时：
- 可以输出判断框架、方向性结论、待验证假设；
- 不得把推测写成确定事实；
- 推荐使用：
  - 当前判断是……
  - 初步看……
  - 现阶段更可能的核心矛盾是……
  - 若后续材料验证成立，建议……
- 避免使用：
  - 已经证明……
  - 明确表明……（若无证据）
  - 核心原因就是……（若无证据）
```

#### 修改理由
避免“强判断”被误用为“强断言”。

#### 影响范围
- 所有高层汇报主题
- 竞品对比与战略判断类题目尤为重要

#### 回归测试
- 无证据题目是否自动切到方向性表达

### 修改文件：`skills/huawei_ppt_master/eval/regression_cases.md`

#### 对应问题
- issue_id: ISSUE-001
- backlog_id: HPPT-001
- issue_id: ISSUE-002
- backlog_id: HPPT-002

#### 原规则或缺失点
> 当前回归未专门覆盖 deck_spec 字段边界与证据强度控制。

#### 建议新增/修改内容
```markdown
新增回归用例：
1. 华为云竞争力深度洞察（无外部数据版）
   - 观察是否自动使用方向性表达；
   - 观察 `data_gaps` 是否完整。
2. deck_spec 契约一致性测试
   - 检查 `chart_type` 与 `layout_pattern` 是否混用；
   - 检查 Builder 是否可执行。
```

#### 修改理由
让本次暴露问题能被持续防回归。

#### 影响范围
- Skill 升级后验收

#### 回归测试
- 新增用例本身即为回归项

## 4. 合入建议
有条件合入
