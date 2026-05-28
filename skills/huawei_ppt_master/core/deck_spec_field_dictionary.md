# deck_spec_field_dictionary

## 1. 文件定位

`deck_spec.json` 是 PPT 生成链路中的**页面语义合同**，用于把大纲、逐页文案、页面设计说明转换为角色 C 可理解的结构化输入。

它的核心作用是说明：

- 每页要表达什么判断；
- 每页标题、结论、展示文本和讲解口径是什么；
- 每页主图表要证明什么；
- 每页应使用哪类 `chart_type` 和 `layout_pattern`；
- 每页有哪些视觉强调、文本密度、压缩需求和数据缺口。

边界说明：

- `deck_spec.json` 不是 PPTX 文件；
- 不是像素级 shape 指令；
- 不直接规定坐标、字号、线条、连接线和组件宽高；
- 角色 C 需要基于 `chart_type`、`layout_pattern`、`chart_data` 和视觉规则，将其转换为具体页面渲染结构。

---

## 2. 顶层字段

| 字段 | 类型 | 作用 | 角色 C 使用方式 |
|---|---|---|---|
| `deck_title` | string | 整份 PPT 标题 | 用于封面标题、文件命名或交付物识别 |
| `audience` | string | 汇报对象 | 用于判断表达风格、信息密度和视觉克制程度 |
| `style` | string | 整体风格标识 | 用于选择华为高层汇报风格，如红黑灰白、白底、弱页脚 |
| `source` | string | 主要来源材料 | 用于页脚来源、证据追踪或备注，不应抢占主体视觉 |
| `slides` | array | 页面列表 | 角色 C 按 `slide_no` 顺序逐页消费并生成页面 |

---

## 3. slide 字段

| 字段 | 类型 | 作用 | 角色 C 使用方式 |
|---|---|---|---|
| `slide_no` | integer | 页码 | 决定页面顺序、页码和页面文件名 |
| `section` | string | 所属章节 | 可作为页眉小标签或章节归属，不应抢主标题焦点 |
| `type` | string | 页面类型 | 辅助判断页面角色，如封面、总览、架构、路线图、决策页 |
| `page_goal` | string | 页面目标 | 用于判断页面是否完成高层沟通目的，通常不直接上屏 |
| `title` | string | 页面主标题 | 直接进入标题区，需控制 1–2 行并保持结论型表达 |
| `conclusion` | string | 页面核心结论 | 可作为主卡、底部收口或讲解锚点，是否上屏由版式决定 |
| `core_judgement` | string | 本页唯一核心判断 | 指导全页内容和图表，不一定全文直接上屏 |
| `chart_proof_goal` | string | 主图表证明目标 | 用于约束图表必须证明什么，防止图表变成装饰 |
| `chart_visual_boundary` | array[string] | 图表视觉边界 | 用于约束主图不能画偏、红色如何控制、主次如何呈现 |
| `display_text` | array[string] | 页面展示文本 | 作为卡片、节点、标签、表格等上屏文本候选 |
| `speaker_notes` | string | 讲解口径 | 可进入备注区或讲稿，不应作为主体长段落堆叠 |
| `chart_type` | string | 主图表类型 | 必须来自 `chart_patterns.md`，角色 C 据此选择图表组件 |
| `chart_data` | object | 主图表数据 | 为图表组件提供 rows、cards、nodes、edges、layers、stages 等结构化内容 |
| `layout_pattern` | string | 页面版式模式 | 必须来自 `layout_library.md`，角色 C 据此选择页面布局模板 |
| `visual_notes` | string | 视觉补充说明 | 用于指导配色、留白、主次和页面气质，不是直接上屏文本 |
| `visual_focus` | array[string] | 视觉焦点 | 用于确定页面主视觉关注点和扫读路径 |
| `must_highlight` | array[string] | 必须强调内容 | 用于确定少量强调词或红色锚点，避免多处抢焦点 |
| `text_density` | string | 文本密度 | 用于决定字号、压缩策略、是否需要拆分或弱化说明 |
| `need_compression` | boolean | 是否需要压缩 | 为 true 时，角色 C 应优先压缩辅助文本而非压缩核心判断 |
| `data_gaps` | array[string] | 数据缺口 | 用于标注待补材料或备注，不能伪造成确定事实 |
