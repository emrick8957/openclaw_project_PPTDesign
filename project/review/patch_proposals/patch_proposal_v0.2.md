# Patch Proposal v0.2

## 1. 基本信息
- 当前任务: 华为云竞争力深度洞察
- patch 编号: PP-20260504-02
- 生成时间: 2026-05-04

## 2. 修改摘要
| 修改文件 | 修改类型 | 对应 issue_id | 优先级 |
|---|---|---|---|
| `skills/huawei_ppt_master/core/output_contracts.md` | 规则增强 | ISSUE-001 | P1 |
| `skills/huawei_ppt_master/eval/acceptance_checklist.md` | 门禁增强 | ISSUE-001, ISSUE-002 | P1 |
| `skills/huawei_ppt_master/eval/regression_cases.md` | 回归补充 | ISSUE-001, ISSUE-002 | P1 |

## 3. 详细补丁

### 修改文件：`skills/huawei_ppt_master/core/output_contracts.md`

#### 对应问题
- issue_id: ISSUE-001
- backlog_id: HPPT-001

#### 原规则或缺失点
> 当前仅要求 `deck_spec.json` 包含 `chart_type`、`layout_pattern`，但未严格限定两者边界，导致 v0.2 中仍出现版式模式写入 `chart_type` 的情况。

#### 建议新增/修改内容
```markdown
### 4.1 deck_spec 字段边界补充
- `chart_type` 表示图表或信息结构类型；
- `layout_pattern` 表示页面布局模式；
- 两者不得混用。

推荐 `chart_type` 示例：
- executive_summary
- comparison_matrix
- decision_table
- gap_heatmap
- value_closure_loop
- roadmap
- trend_timeline
- risk_matrix
- closure_architecture
- four_quadrant_analysis
- three_column_comparison
- none

推荐 `layout_pattern` 示例：
- executive_summary_dashboard
- trend_curve_with_strategy
- four_quadrant_judgement
- three_column_cards
- insight_panel_with_chart
- roadmap_timeline
- risk_decision_matrix
- stack_architecture_with_right_insights
- cover
```

#### 修改理由
减少 Builder 侧隐式映射，增强中间契约稳定性。

#### 影响范围
- deck_spec 生成
- Builder 输入解析
- 回归测试口径

#### 回归测试
- 检查 `chart_type` 是否误填为 `layout_pattern`
- 抽检 P2/P4/P6/P7/P11 类型映射

### 修改文件：`skills/huawei_ppt_master/eval/acceptance_checklist.md`

#### 对应问题
- issue_id: ISSUE-001
- backlog_id: HPPT-001
- issue_id: ISSUE-002
- backlog_id: HPPT-002

#### 原规则或缺失点
> 当前已增加门禁，但仍需把 deck_spec 契约检查和证据降级规则做得更具体、可执行。

#### 建议新增/修改内容
```markdown
## 6. deck_spec 契约检查（补强）
- `chart_type` 是否描述图表/信息结构，而非页面版式；
- `layout_pattern` 是否描述布局模式；
- 若同名同时出现在 `chart_type` 与 `layout_pattern`，应判定为需复核；
- 对总览页、路线图页、四象限页、三栏卡片页等，需明确“图表类型”和“版式模式”分别是什么。

## 7. 高断言页面证据门禁（固化）
- 外部竞争变化、竞品框架、优势/短板诊断、资源建议等页面，在缺少证据时必须降级措辞；
- 推荐使用：当前判断看、初步看、若后续材料验证成立；
- 如仍使用强断言，应在 `data_gaps` 中明确支撑材料来源。
```

#### 修改理由
把本轮有效改进固化为显式规则。

#### 影响范围
- A 自检质量
- B 归因效率
- 事实风险控制

#### 回归测试
- 缺证据题目下是否自动降级措辞
- 契约检查是否能识别同名混用

### 修改文件：`skills/huawei_ppt_master/eval/regression_cases.md`

#### 对应问题
- issue_id: ISSUE-001
- backlog_id: HPPT-001
- issue_id: ISSUE-002
- backlog_id: HPPT-002

#### 原规则或缺失点
> 当前回归未把“v0.2 命名混用残留”作为显式测试点。

#### 建议新增/修改内容
```markdown
新增回归用例：
1. 华为云竞争力深度洞察 v0.2
   - 检查 P2/P4/P6/P7/P11 的 `chart_type` 是否仍误写为版式模式；
   - 检查高断言页面是否保持方向性表达。
2. 无外部数据的竞品判断题
   - 检查是否自动降级为框架性判断；
   - 检查 `data_gaps` 是否完整。
```

#### 修改理由
让本轮问题可稳定防回归。

#### 影响范围
- Skill 升级后验收

#### 回归测试
- 新增用例本身即为回归项

## 4. 合入建议
有条件合入
