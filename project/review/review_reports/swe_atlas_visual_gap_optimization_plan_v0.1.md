# SWE Atlas PPT 图片华为风格差距分析与优化方案 v0.1

## 1. 输入与范围

| 类型 | 路径 | 说明 |
|---|---|---|
| SWE Atlas 页面图片 | `project/PPT_image/SWE_Atlas_page_images_v0.1/` | P1-P5 页面图片与总览预览 |
| 华为风格模板 | `tmp/PPTTemplate/0517/` | 147 张华为风格 PPT 模板图片及 contact sheets |
| 当前设计说明 | `project/work/page_design_v0.1.md` | SWE Atlas 页面设计约束 |
| 当前 deck_spec | `project/work/deck_spec_v0.1.json` | Builder 输入结构 |

本轮只输出优化方案，不直接修改 Skill 资产与页面图片。

## 2. 总体判断

SWE Atlas 生成图已经具备“结论先行、红黑灰、模块化、图表化”的基础，但更接近**技术研究报告/咨询稿**，与华为风格模板相比，主要差距在于：

1. **视觉密度偏高**：卡片、边框、红色标签和底部结论条较多，页面压迫感强。
2. **红色强调过量**：多个区域同时用红色，导致焦点分散，不符合“红色只做关键锚点”的华为克制风格。
3. **版式母版不够稳定**：每页都采用不同组合，标题区、主图区、洞察区、底部条的节奏不完全统一。
4. **图表语法需要收敛**：卡片、表格、流程、闭环图都能表达，但节点、箭头、边框、卡片层级缺少统一组件规范。
5. **页脚和来源区一致性不足**：有正式感，但位置、权重、基线稳定性需要固化。
6. **Builder 规则还不够细**：deck_spec 的 visual_notes 已有方向，但没有把“少红、弱边框、统一内边距、底部条克制”等转成可执行约束。

## 3. 与华为模板的关键差距

| 维度 | 华为模板基准 | SWE Atlas 当前表现 | 优化方向 |
|---|---|---|---|
| 版式骨架 | 顶部标题区稳定，正文按网格分区，页脚极轻 | 每页结构完整但变化较多，局部像信息拼贴 | 固化 3 类母版：证据页、问题页、行动页 |
| 标题层级 | 主标题强，副标题弱，层级 2-3 层 | 标题结论化较好，但长标题压缩上方呼吸感 | 增加标题断行、关键词高亮和副标题弱化规则 |
| 红黑灰 | 黑灰为主体，红色 5%-10% 做锚点 | 红框、红条、红标签较多 | 建立“单页红色锚点不超过 1-2 个”的规则 |
| 留白 | 控制型留白，模块间距稳定 | 卡片/表格/底部条偏满 | 增加模块间距、卡片内边距、弱化底部条 |
| 卡片 | 轻边框、浅底、少阴影、等宽网格 | 卡片很多但层级近似，红色标题块偏重 | 建立强/中/弱卡片三级样式 |
| 表格 | 弱化传统表格感，强调结构化汇总 | P3 表格偏数据报告，线条与信息密度较重 | 表格证据化，大数字结论化，减少高亮项 |
| 流程/闭环 | 节点统一、箭头克制、线条轻 | P2/P5 图形元素较杂，箭头/节点样式不够统一 | 统一节点、箭头、连接线、右侧洞察栏规则 |
| 页脚 | 极轻、固定、统一 | 有页脚意识但存在感与位置稳定性不足 | 固化页脚模板与安全区 |

## 4. 逐页优化方案

### P1 核心判断页

问题：左侧长文、右侧卡片、底部流程同时抢焦点，红色强调偏多。  
优化：
- 左侧压缩为“一句主判断 + 3 个短要点”；
- 右侧三卡统一尺寸、内边距、边框；
- 底部箭头改为细线流程，减少红色块面；
- 单页红色焦点只保留“284 tasks”或“Beyond correctness”之一。

资产迭代：`executive_summary_patterns.md`、`visual_rules.md`、`chart_patterns.md:key_findings_cards`。

### P2 方法框架页

问题：三泳道机制表达清楚，但节点/卡片密度偏高，右侧洞察栏和主图区权重略不协调。  
优化：
- 三泳道统一为“任务—检查—判定”三层结构；
- 每列节点高度、间距、箭头一致；
- 右侧 Rubric 洞察保留一句结论 + 3 条短句；
- 红色只用于关键判定节点或标题关键词。

资产迭代：`architecture_page_patterns.md`、`chart_patterns.md:swimlane_process`、`layout_library.md:stack_architecture_with_right_insights`。

### P3 关键结果页

问题：左表和右侧大数字都较强，底部红条过重，偏“宣传页/数据报告混合”。  
优化：
- 表格弱化边框，减少行列线和高亮项；
- 右侧大数字卡统一为“指标名—数值—一句解释”；
- 底部红条改为窄结论条或灰底红字结论；
- 强化“表格是证据、右侧是结论”的阅读路径。

资产迭代：`comparison_page_patterns.md`、`chart_patterns.md:comparison_table`、`visual_rules.md`、`eval/visual_scorecard.md`。

### P4 失败模式页

问题：三卡整齐但同权，红色标题栏过重，底部结论条视觉重量偏大。  
优化：
- 三张卡建立主次：可突出最关键失败模式，其他两张弱化；
- 每卡改为“关键词 + 表现/风险/改进”短结构；
- 底部结论条缩窄，避免压住页面；
- 卡片边框改浅，减少红色块面。

资产迭代：`risk_decision_patterns.md` 或新增 `problem_diagnosis_patterns.md`、`chart_patterns.md:key_findings_cards`、`layout_library.md:three_column_cards`。

### P5 转化启示页

问题：闭环图和右侧建议列表都较重，底部红色横幅压底，图形元素略杂。  
优化：
- 闭环图只保留 5 个节点，每节点“动词+名词”；
- 右侧建议从 5 条压到 3-4 条一级动作；
- 统一节点、箭头、线条、圆角；
- 底部红条改为窄条或页脚上方弱结论。

资产迭代：`chart_patterns.md:value_chain_loop`、`architecture_page_patterns.md`、`layout_library.md:stack_architecture_with_right_insights`、`eval/visual_scorecard.md`。

## 5. 本轮建议迭代的资产清单

### 5.1 必须迭代 P0/P1 资产

| 资产 | 建议动作 | 目标 |
|---|---|---|
| `skills/huawei_ppt_master/templates/visual_rules.md` | 增加“红色锚点预算、留白/内边距、底部结论条克制、页脚安全区”规则 | 解决整体视觉过重、红色过量、留白不足 |
| `skills/huawei_ppt_master/visual_patterns/layout_library.md` | 补充各 layout 的“推荐区域比例、禁用组合、右侧洞察栏宽度、底部条使用条件” | 让 Builder 按稳定母版排版 |
| `skills/huawei_ppt_master/templates/chart_patterns.md` | 补充 `key_findings_cards`、`comparison_table`、`swimlane_process`、`value_chain_loop` 的视觉细则 | 统一卡片/表格/泳道/闭环图语法 |
| `skills/huawei_ppt_master/eval/visual_scorecard.md` | 增加视觉评分项：红色占比、卡片层级、留白、表格密度、页脚一致性 | 让生成后图片可被自动/人工复核 |

### 5.2 建议迭代 P2 资产

| 资产 | 建议动作 | 目标 |
|---|---|---|
| `skills/huawei_ppt_master/visual_patterns/executive_summary_patterns.md` | 增加“左判断 + 右三卡 + 轻流程”的高层总览正例/反例 | 优化 P1 类型页面 |
| `skills/huawei_ppt_master/visual_patterns/architecture_page_patterns.md` | 增加泳道/闭环图节点统一规则 | 优化 P2/P5 类型页面 |
| `skills/huawei_ppt_master/visual_patterns/comparison_page_patterns.md` | 增加“表格证据化 + 右侧指标结论化”模式 | 优化 P3 数据对比页 |
| `skills/huawei_ppt_master/visual_patterns/risk_decision_patterns.md` 或新增 `problem_diagnosis_patterns.md` | 增加三类失败模式页的主次卡片规则 | 优化 P4 问题诊断页 |
| `skills/huawei_ppt_master/prompts/generate_page_design.md` | 在页面设计生成时强制输出：红色使用点、卡片层级、留白策略、页脚规则 | 让设计说明更可执行 |

### 5.3 如存在/后续新增 Builder 资产，建议迭代

当前仓库未见独立 `huawei_ppt_delivery_builder` skill。若后续有 Builder 资产，建议沉淀：

| 资产方向 | 规则 |
|---|---|
| Builder component styles | 卡片三级样式、表格弱边框样式、窄结论条、页脚组件 |
| Builder layout constraints | 标题区固定高度、正文安全边距、右侧洞察栏宽度、底部条最大高度 |
| Builder visual QA | 红色面积阈值、元素数量阈值、最小字号、模块间距检查 |

## 6. 建议的迭代优先级

### 第一轮：先解决“像不像华为”的基础视觉问题

1. `visual_rules.md`：红色克制、留白、页脚、安全区；
2. `layout_library.md`：母版区域比例和禁用组合；
3. `chart_patterns.md`：卡片/表格/泳道/闭环图组件语法；
4. `eval/visual_scorecard.md`：生成图复核评分。

### 第二轮：解决 SWE Atlas 这类技术研究报告页型

1. `comparison_page_patterns.md`：数据表 + 关键指标卡；
2. `architecture_page_patterns.md`：泳道/闭环图；
3. `executive_summary_patterns.md`：高层速读页；
4. `problem_diagnosis_patterns.md`：问题/失败模式三卡页。

### 第三轮：回归验证

- 用 SWE Atlas P1-P5 作为 regression case；
- 重新生成页面图片；
- 以华为模板 contact sheet 为风格参考进行视觉复核；
- 重点检查：红色占比下降、表格变轻、底部条变窄、卡片间距和页脚一致。

## 7. 可执行验收标准

| 验收项 | 标准 |
|---|---|
| 红色使用 | 单页主红色锚点不超过 1-2 个；大面积红条仅用于封面/章节/强收口页 |
| 信息密度 | 正文页 3-5 个主要信息块；P3 数据页可高密但必须有明确主结论 |
| 卡片规范 | 同页卡片圆角、边框、内边距、标题样式一致；重要/次要卡片有层级差 |
| 表格规范 | 弱边框、少高亮、行列线浅灰；表格承担证据，不承担全部结论 |
| 流程/闭环 | 节点统一、箭头克制、每节点短文本；闭环图不做文字容器 |
| 页脚 | 位置、字号、颜色、基线固定；不抢主体 |
| 华为风格一致性 | 白底/浅灰底、黑灰承载信息、红色定锚、低装饰、高结构秩序 |

## 8. 本轮结论

本轮不建议直接改页面图片，而应先迭代规则资产，尤其是 `visual_rules.md`、`layout_library.md`、`chart_patterns.md`、`visual_scorecard.md`。当前 SWE Atlas 的主要问题不是内容逻辑，而是 Builder 视觉约束不够细，导致“结构正确但视觉偏重”。下一轮应先补资产规则，再让角色 A/Builder 基于新规则重生成图片。
