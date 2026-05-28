# deck_spec.json 字段字典与角色 C 消费说明 v0.1

## 1. 文件定位

`deck_spec.json` 是 **页面语义合同**，不是像素级渲染指令。

它告诉角色 C：

- 每页要表达什么判断；
- 主图表要证明什么；
- 应使用哪类图表结构；
- 应使用哪类页面版式；
- 哪些文字必须展示、哪些元素需要强调；
- 哪些地方需要压缩或人工补充。

它不直接告诉角色 C：

- 每个 shape 的绝对坐标；
- 每个文本框的宽高；
- 每条线、箭头、卡片的具体绘制参数；
- 字号、间距、颜色的最终数值。

因此：**C 端不能只读 deck_spec 就零理解渲染出稳定 PPT；必须先把 deck_spec 映射为 C 端内部 layout/component/shape 指令。**

---

## 2. 顶层字段

| 字段 | 类型 | 角色 C 用法 | 是否可直接渲染 | 说明 |
|---|---|---|---|---|
| `deck_title` | string | 作为文件标题、封面标题候选、导出命名依据 | 部分可直用 | 封面仍需结合 slide 1 判断 |
| `audience` | string | 决定整体风格密度与表达克制程度 | 不直接渲染 | 用于渲染策略，如高层汇报少装饰、强结论 |
| `style` | string | 选择主题样式包 | 需转换 | 如 `huawei_executive` 映射到红黑灰白、页脚、安全区等 |
| `source` | string | 页脚来源或证据说明候选 | 部分可直用 | 建议弱化展示，不进入主体视觉焦点 |
| `slides` | array | 每页渲染输入列表 | 需逐页转换 | C 端核心消费对象 |

---

## 3. slide 字段

| 字段 | 类型 | 角色 C 用法 | 是否可直接渲染 | 说明 |
|---|---|---|---|---|
| `slide_no` | integer | 页码、排序、文件命名 | 可直用 | 直接决定页面顺序 |
| `section` | string | 章节标签、页眉小标签 | 部分可直用 | 不应抢主标题焦点 |
| `type` | string | 页型策略参考 | 需转换 | 如 `architecture`、`decision_table`，用于选择渲染策略 |
| `page_goal` | string | 渲染目标提示 | 不直接渲染 | 用于判断页面是否达成目的 |
| `title` | string | 主标题文本 | 可直用但需适配 | 需做行数、字号、压缩判断 |
| `conclusion` | string | 一句话结论、底部收口、主卡内容候选 | 部分可直用 | 不一定每页都要完整展示，需按版式决定位置 |
| `core_judgement` | string | 页面唯一判断锚点 | 不建议直接全文渲染 | 应指导标题、主图、强调元素，不一定原文上屏 |
| `chart_proof_goal` | string | 主图表论证任务 | 不直接渲染 | C 端用它校验图表是否只是装饰 |
| `chart_visual_boundary` | array[string] | 主图视觉禁区/约束 | 不直接渲染 | 用于渲染前检查和失败降级 |
| `display_text` | array[string] | 页面上屏关键词/短句候选 | 可直用但需编排 | 常用于卡片、节点、标签 |
| `speaker_notes` | string | 备注/讲稿 | 不进入主体 | 可放 speaker notes，不应作为页面正文 |
| `chart_type` | string | 选择主图表组件类型 | 需转换 | 必须映射到 C 端组件，如 cards/table/layered_stack/flow |
| `chart_data` | object | 主图表数据源 | 需转换 | C 端据此生成节点、表格、层级、时间轴等 |
| `layout_pattern` | string | 选择页面布局模板 | 需转换 | 映射到 C 端布局蓝图，如标题区/主体区/右侧洞察/底部条 |
| `visual_notes` | string | 风格与补充说明 | 不直接渲染 | 转换为颜色、密度、边界策略 |
| `visual_focus` | array[string] | 主视觉焦点候选 | 需转换 | 决定红色锚点或视觉优先级 |
| `must_highlight` | array[string] | 必须强调的关键词 | 需转换 | 只能少量强调，防止红色过多 |
| `text_density` | string | 文本密度策略 | 需转换 | `medium/high` 影响字号、压缩、拆页 |
| `need_compression` | boolean | 是否需要压缩 | 需转换 | true 时触发文本压缩策略 |
| `data_gaps` | array[string] | 数据缺口提示 | 不直接渲染或弱展示 | 可作为备注/风险提示，不应伪造成事实 |

---

## 4. C 端推荐转换流程

```text
for slide in deck_spec.slides:
  1. 读取 layout_pattern → 选择页面布局蓝图
  2. 读取 chart_type → 选择主图表组件
  3. 读取 chart_data/display_text → 生成组件内容
  4. 读取 title/conclusion/core_judgement → 确定标题、主卡、底部收口
  5. 读取 visual_focus/must_highlight → 分配唯一红色锚点
  6. 读取 chart_visual_boundary/visual_notes → 执行视觉禁区检查
  7. 读取 text_density/need_compression → 做文本压缩或人工评审
```

---

## 5. 直接渲染能力判断

| 能力层级 | deck_spec 是否满足 | 说明 |
|---|---|---|
| 页面顺序 | 满足 | `slide_no` 可直用 |
| 标题与主要文字 | 基本满足 | 需文本适配 |
| 主图表类型 | 满足 | 但需 C 端有组件映射 |
| 主图表数据 | 部分满足 | 简单表格/卡片较直接，架构图需解释转换 |
| 页面布局 | 部分满足 | `layout_pattern` 是模板名，不是坐标 |
| 视觉风格 | 部分满足 | 需 C 端将规则映射为样式 token |
| 精确坐标/shape | 不满足 | 需要 C 端生成 |
| 渲染失败判断 | 部分满足 | 需结合 page_render_spec 的 `render_validation` 更完整 |

结论：`deck_spec.json` **不是直接渲染协议**，而是 C 端渲染前的语义输入。C 端必须有一层 `deck_spec_adapter` 把它转换为内部 render model。
