# Patch Proposal v0.3

## 1. 基本信息
- 当前任务: 华为云竞争力深度洞察
- patch 编号: PP-20260504-03
- 生成时间: 2026-05-04

## 2. 修改摘要
| 修改文件 | 修改类型 | 对应 issue_id | 优先级 |
|---|---|---|---|
| `skills/huawei_ppt_master/core/output_contracts.md` | 规则增强 | ISSUE-001, ISSUE-002 | P1 |
| `skills/huawei_ppt_master/eval/acceptance_checklist.md` | 门禁增强 | ISSUE-001, ISSUE-003 | P1 |
| `skills/huawei_ppt_master/eval/regression_cases.md` | 回归补充 | ISSUE-001, ISSUE-002, ISSUE-003 | P1 |
| `skills/huawei_ppt_master/SKILL.md` | 交付规则补强 | ISSUE-002 | P1 |

## 3. 详细补丁

### 修改文件：`skills/huawei_ppt_master/core/output_contracts.md`

#### 对应问题
- issue_id: ISSUE-001
- backlog_id: HPPT-001
- issue_id: ISSUE-002
- backlog_id: HPPT-003

#### 原规则或缺失点
> 当前对 `deck_spec.json` 的 `chart_type` / `layout_pattern` 边界定义不够强；对超过 10 页后的分包交付规则也未做明确说明。

#### 建议新增/修改内容
```markdown
### 4.1 deck_spec 字段边界补充
- `chart_type` 表示图表或信息结构类型；
- `layout_pattern` 表示页面布局模式；
- 两者不得混用。

推荐 `chart_type` 示例：
- chapter_agenda
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
- cover
- three_column_cards
- executive_summary_dashboard
- trend_curve_with_strategy
- insight_panel_with_chart
- four_quadrant_judgement
- stack_architecture_with_right_insights
- roadmap_timeline
- risk_decision_matrix

### 4.2 分包交付补充
- 当页面数超过 10 页时，deliverables 可按页码区间分包；
- `project/work/` 必须始终保留完整版本主文件；
- `project/handoff/A_to_B.md` 与 `project/handoff/status.md` 必须同时声明完整版本与所有分包文件清单；
- 分包命名应包含版本号和页码范围。
```

#### 修改理由
同时修复中间契约不稳和交付状态不清两个问题。

#### 影响范围
- deck_spec 生成
- Builder 输入解析
- 交付打包与交接一致性

#### 回归测试
- 检查 `chart_type` 是否误填为 `layout_pattern`
- 检查分包时 work / deliverables / handoff 是否一致

### 修改文件：`skills/huawei_ppt_master/eval/acceptance_checklist.md`

#### 对应问题
- issue_id: ISSUE-001
- backlog_id: HPPT-001
- issue_id: ISSUE-003
- backlog_id: HPPT-002

#### 原规则或缺失点
> 当前虽已有契约与证据门禁，但对“同名混用”和“方向性措辞是否持续保持”仍不够细。

#### 建议新增/修改内容
```markdown
## 6. deck_spec 契约检查（补强）
- `chart_type` 是否描述图表/信息结构，而非页面版式；
- `layout_pattern` 是否描述布局模式；
- 若同名同时出现在 `chart_type` 与 `layout_pattern`，应判定为需复核；
- 对总览页、趋势页、四象限页、三栏卡片页、路线图页等，需明确“图表类型”和“版式模式”分别是什么。

## 7. 高断言页面证据门禁（固化）
- 外部竞争变化、竞品框架、优势/短板诊断、资源建议等页面，在缺少证据时必须降级措辞；
- 推荐使用：当前判断看、初步看、若后续材料验证成立；
- 如仍使用强断言，应在 `data_gaps` 中明确支撑材料来源。
```

#### 修改理由
把本轮有效做法固化成显式门禁。

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
- backlog_id: HPPT-003
- issue_id: ISSUE-003
- backlog_id: HPPT-002

#### 原规则或缺失点
> 当前回归未把 v0.3 中的分包交付与契约混用作为显式测试点。

#### 建议新增/修改内容
```markdown
新增回归用例：
1. 华为云竞争力深度洞察 v0.3
   - 检查 P3/P5/P7/P8/P12 的 `chart_type` 是否仍误写为版式模式；
   - 检查高断言页面是否保持方向性表达。
2. 超过 10 页的打包一致性测试
   - 检查 `project/work` 是否仍保留完整主文件；
   - 检查 deliverables 分包命名是否规范；
   - 检查 handoff/status 是否同步完整版本与分包清单。
```

#### 修改理由
让本轮暴露问题可稳定防回归。

#### 影响范围
- Skill 升级后验收

#### 回归测试
- 新增用例本身即为回归项

### 修改文件：`skills/huawei_ppt_master/SKILL.md`

#### 对应问题
- issue_id: ISSUE-002
- backlog_id: HPPT-003

#### 原规则或缺失点
> 当前默认输出顺序与交付路径未明确说明“超过 10 页时的分包交付规则”。

#### 建议新增/修改内容
```markdown
### 分包交付规则补充
当最终交付页数超过 10 页时：
1. `project/work/` 仍输出完整版本主文件；
2. `deliverables/` 可按页码区间拆分为多个 zip；
3. `A_to_B.md` 必须列出完整版本文件与全部分包文件；
4. `status.md` 必须同步最新版本号与分包清单；
5. 分包仅影响交付包，不影响 B 评审读取 work 区完整主文件。
```

#### 修改理由
避免交接层和文件层口径分裂。

#### 影响范围
- 交付打包规范
- A/B 协作效率

#### 回归测试
- 超过 10 页题目下是否稳定执行

## 4. 合入建议
有条件合入
