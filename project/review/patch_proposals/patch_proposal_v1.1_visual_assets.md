# patch_proposal_v1.1_visual_assets

## 1. 背景

来源：`project/review/review_reports/swe_atlas_visual_gap_optimization_plan_v0.1.md`。

本轮针对 SWE Atlas 页面图片与华为风格 PPT 模板的差距，提出视觉资产迭代 proposal。按角色 B 边界，本文件**不直接修改** `skills/huawei_ppt_master/*`，仅给出可人工确认的 patch 方案。

## 2. 总体判断

SWE Atlas 页面图片的问题不是内容逻辑，而是视觉约束不够细：红色强调过多、卡片/表格/流程组件偏重、底部结论条偏大、页脚一致性不足、母版区域比例不够稳定。

建议本轮优先补齐 4 类基础资产：

1. `templates/visual_rules.md`
2. `visual_patterns/layout_library.md`
3. `templates/chart_patterns.md`
4. `eval/visual_scorecard.md`

然后补充 5 类页型资产：

1. `visual_patterns/executive_summary_patterns.md`
2. `visual_patterns/architecture_page_patterns.md`
3. `visual_patterns/comparison_page_patterns.md`
4. `visual_patterns/risk_decision_patterns.md` 或新增 `visual_patterns/problem_diagnosis_patterns.md`
5. `prompts/generate_page_design.md`

## 3. Patch Proposal 明细

### 3.1 `templates/visual_rules.md`

| 字段 | 内容 |
|---|---|
| 对应 issue_id | VIS-SWE-001, VIS-SWE-002, VIS-SWE-005 |
| 原规则或缺失点 | 现有规则说明红色用于标题/关键结论/箭头/重点数字，但缺少红色使用预算、底部结论条高度、卡片内边距、页脚安全区等可执行阈值 |
| 新增规则 | 增加“华为式视觉降噪规则”：单页主红色锚点不超过 1-2 个；正文页红色面积建议控制在 5%-10%；底部红色结论条仅用于强收口页，普通页使用窄条或灰底红字；卡片边框用浅灰细线，避免重红框；页脚固定底部 5% 安全区 |
| 修改理由 | SWE Atlas P1/P3/P4/P5 均出现红色偏重、底部条压迫、卡片边框偏强的问题 |
| 影响范围 | 全局视觉生成规则；会让页面更克制、更接近华为模板 |
| 回归测试 | 重新生成 SWE Atlas P1-P5，检查红色面积、底部条高度、卡片边框权重、页脚一致性 |

建议新增文本：

```markdown
## 华为式视觉降噪规则

- 单页只允许 1 个主红色视觉锚点，最多 2 个辅助红色强调点；不要让红框、红条、红色数字、红色标签同时抢焦点。
- 正文页红色面积建议控制在 5%-10%；大面积红色横条仅用于封面、章节页或强收口页。
- 普通正文页底部结论优先使用“窄红线 + 黑/灰文字”或“浅灰底 + 红色关键词”，避免厚重红色压底。
- 卡片默认使用白底/浅灰底、浅灰细边框、弱阴影或无阴影；红色只用于卡片编号、关键词或单个重点数字。
- 同页卡片必须统一圆角、边框、内边距、标题样式；重要卡片可强化，次要卡片必须降噪。
- 页脚固定在底部安全区，包含来源/保密/页码时应使用浅灰小字，不得与正文抢视觉。
```

---

### 3.2 `visual_patterns/layout_library.md`

| 字段 | 内容 |
|---|---|
| 对应 issue_id | VIS-SWE-003, VIS-SWE-006 |
| 原规则或缺失点 | layout 只定义结构，缺少区域比例、右侧洞察栏宽度、底部结论条使用条件、禁用组合 |
| 新增规则 | 为关键 layout 增加区域比例与禁用项：`executive_summary_dashboard`、`stack_architecture_with_right_insights`、`insight_panel_with_chart`、`three_column_cards` |
| 修改理由 | SWE Atlas 每页结构都正确，但母版节奏不够稳定，导致“像研究稿，不像稳定企业汇报模板” |
| 影响范围 | 页面设计说明与 Builder 布局选择 |
| 回归测试 | 检查 P1-P5 是否使用稳定标题区、主体区、页脚区；右侧洞察栏宽度是否一致 |

建议新增规则：

```markdown
## layout 通用区域比例

- 标题区：10%-15%，承载章节标签、主标题、副标题；长标题需断为 1-2 行，避免压缩正文。
- 主体区：75%-80%，必须有清晰网格；同页模块间距不得小于卡片内边距。
- 页脚区：约 5%，位置固定，弱化显示。
- 右侧洞察栏：通常占页面宽度 25%-32%，只承载 1 句结论 + 3-4 条短要点。
- 底部结论条：仅当页面需要强收口时使用；普通页优先用窄条，不使用厚重红色横幅。

## 禁用组合

- 不要在同一页同时使用厚重红色底部条、多个红色卡片标题、多个红色大数字。
- `insight_panel_with_chart` 中，表格承担证据，右侧指标卡承担结论；二者不得同等强视觉。
- `three_column_cards` 中，三卡可同构但必须通过编号、关键词或轻量图标建立扫读路径。
```

---

### 3.3 `templates/chart_patterns.md`

| 字段 | 内容 |
|---|---|
| 对应 issue_id | VIS-SWE-004, VIS-SWE-007, VIS-SWE-008 |
| 原规则或缺失点 | chart_type 定义了数据结构和场景，但对具体视觉组件约束不足 |
| 新增规则 | 为 `key_findings_cards`、`comparison_table`、`swimlane_process`、`value_chain_loop` 增加视觉语法 |
| 修改理由 | SWE Atlas 的卡片、表格、泳道、闭环图均存在“结构正确但视觉偏重/不统一”的问题 |
| 影响范围 | deck_spec 生成与 Builder 图表绘制 |
| 回归测试 | P1/P4 卡片、P3 表格、P2 泳道、P5 闭环图重生成后逐项检查 |

建议新增规则：

```markdown
### key_findings_cards 视觉规则
- 同页卡片等宽等高，内边距一致。
- 强卡片最多 1 张；其余卡片用弱边框/浅灰底降权。
- 红色只用于编号、核心数字或关键词，不使用整块红色标题栏铺满多张卡片。

### comparison_table 视觉规则
- 表格是证据区，不承担全部结论；必须配独立结论区或关键指标卡。
- 行列线使用浅灰细线；高亮项不超过 2-3 个。
- 表头可加粗或红色关键词，但避免大面积深色底。

### swimlane_process 视觉规则
- 泳道节点高度、宽度、间距统一；箭头细线化。
- 每个节点控制为短语，不写长句。
- 红色只标记关键判定节点或终点，不标满所有节点。

### value_chain_loop 视觉规则
- 闭环节点建议 4-5 个，每个节点使用“动词 + 名词”短语。
- 闭环图是概念锚点，不是文字容器；详细说明放到右侧洞察栏。
- 箭头和连接线用浅灰/深灰，红色只用于闭环起点、关键节点或中心结论。
```

---

### 3.4 `eval/visual_scorecard.md`

| 字段 | 内容 |
|---|---|
| 对应 issue_id | VIS-SWE-009 |
| 原规则或缺失点 | 评分表维度较粗，不能识别红色过量、底部条过重、卡片层级缺失、表格密度偏高等问题 |
| 新增规则 | 增加可执行评分子项和扣分项 |
| 修改理由 | 当前 SWE Atlas 自检显示“遵循设计说明”，但视觉上仍偏重，说明现有 scorecard 不够细 |
| 影响范围 | 页面图片生成后 QA / B 复核 |
| 回归测试 | 用 SWE Atlas P1-P5 做 visual regression，目标分数 ≥ 85 |

建议新增评分项：

```markdown
## F. 视觉降噪与华为风格一致性 20分

- 红色锚点克制：4分。单页主红色焦点不超过 1-2 个，无多处抢焦点。
- 卡片层级清晰：4分。同页卡片样式统一，强/中/弱层级明确。
- 图表组件统一：4分。表格、泳道、闭环图节点/线条/箭头样式一致。
- 留白与安全区：4分。标题、正文、页脚之间有稳定呼吸感。
- 底部结论条克制：4分。无厚重压底，普通页使用窄条或弱结论区。

## 一票降级项

- 正文页出现大面积红色横幅且非强收口页：最高 B 档。
- 表格页无独立结论区，全部信息压在表格内：最高 B 档。
- 页脚位置/字号/颜色每页不一致：扣 3-5 分。
```

---

### 3.5 `prompts/generate_page_design.md`

| 字段 | 内容 |
|---|---|
| 对应 issue_id | VIS-SWE-010 |
| 原规则或缺失点 | 当前 prompt 要求说明区域和 Builder 实现，但没有强制输出红色使用点、卡片层级、留白策略、页脚规则 |
| 新增规则 | 页面设计说明必须包含“视觉降噪约束”字段 |
| 修改理由 | 让 Builder 在生成前就拿到可执行视觉边界 |
| 影响范围 | 角色 A 页面设计说明生成 |
| 回归测试 | 新生成 `page_design.md` 每页必须包含 visual_noise_control / red_anchor / spacing / footer_rule |

建议新增要求：

```markdown
7. 每页必须输出视觉降噪约束：
   - red_anchor：本页唯一主红色强调点；
   - card_hierarchy：卡片强/中/弱层级；
   - spacing_rule：模块间距、卡片内边距和页脚安全区；
   - bottom_bar_rule：是否允许底部结论条，若允许需说明高度和颜色强度；
   - visual_simplification：需要弱化或删除的装饰元素。
```

---

### 3.6 页型专项资产

#### `visual_patterns/executive_summary_patterns.md`

- 增加“左主判断 + 右三卡 + 轻流程”的总览页模式。
- 要求左侧判断不超过 3 要点；右侧三卡同规格；底部流程仅用细线箭头。

#### `visual_patterns/architecture_page_patterns.md`

- 增加“泳道流程 + 右侧洞察栏”和“价值闭环 + 右侧行动栏”两类模式。
- 要求节点统一、箭头克制、红色只标关键节点。

#### `visual_patterns/comparison_page_patterns.md`

- 增加“表格证据区 + 指标结论卡”模式。
- 要求表格弱化边框，右侧指标卡统一结构。

#### `visual_patterns/risk_decision_patterns.md` 或新增 `visual_patterns/problem_diagnosis_patterns.md`

- 增加“三类失败模式诊断页”模式。
- 要求三卡可同构，但必须建立主次；底部结论条降权。

## 4. 新增问题清单

| issue_id | 问题 | 归因 | 优先级 | 是否沉淀 |
|---|---|---|---|---|
| VIS-SWE-001 | 红色使用预算缺失 | skill_rule_missing | P1 | 是 |
| VIS-SWE-002 | 底部结论条过重缺少约束 | skill_rule_missing | P1 | 是 |
| VIS-SWE-003 | layout 区域比例与右侧洞察栏规则不足 | visual_pattern_gap | P1 | 是 |
| VIS-SWE-004 | 卡片强/中/弱层级缺失 | visual_pattern_gap | P1 | 是 |
| VIS-SWE-005 | 页脚安全区规则不足 | skill_rule_missing | P2 | 是 |
| VIS-SWE-006 | 母版节奏不够稳定 | visual_pattern_gap | P1 | 是 |
| VIS-SWE-007 | 表格证据化规则不足 | visual_pattern_gap | P1 | 是 |
| VIS-SWE-008 | 泳道/闭环图组件语法不足 | visual_pattern_gap | P1 | 是 |
| VIS-SWE-009 | visual_scorecard 不能识别视觉偏重问题 | qa_gate_gap | P1 | 是 |
| VIS-SWE-010 | page_design prompt 缺少视觉降噪字段 | output_contract_gap | P1 | 是 |

## 5. 合入建议

**建议有条件合入。**

条件：
1. 人工确认本 proposal 的视觉规则阈值；
2. 先合入 P1 资产：`visual_rules.md`、`layout_library.md`、`chart_patterns.md`、`visual_scorecard.md`、`generate_page_design.md`；
3. 再合入页型专项资产；
4. 使用 SWE Atlas P1-P5 重生成页面图片并完成视觉回归。

当前不建议直接修改页面图片，应先修规则资产，再让 A/Builder 重跑。
