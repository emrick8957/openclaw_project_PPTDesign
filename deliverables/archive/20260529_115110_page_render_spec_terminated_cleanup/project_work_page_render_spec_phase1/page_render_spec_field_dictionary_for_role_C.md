# page_render_spec_samples_v0.1.json 字段字典与角色 C 消费说明 v0.1

## 1. 文件定位

`page_render_spec_samples_v0.1.json` 是 **复杂页构造约束样例集合**。

它比 `deck_spec.json` 更接近渲染，但仍不是最终像素级绘图指令。

它告诉角色 C：

- 哪些页面是复杂/高风险页面；
- 为什么需要额外约束；
- 每个页面应拆成哪些可渲染单元；
- 每个单元的语义角色、内容来源、优先级和溢出处理；
- 文本适配、红色锚点、卡片层级、底部结论、右侧洞察等约束；
- 渲染完成后必须通过哪些检查。

它不直接告诉角色 C：

- 每个 render_unit 的绝对坐标；
- 具体字体字号；
- 每个 shape 的 SVG/PPTX primitive；
- 箭头路径、卡片尺寸、层级间距的最终数值。

因此：**page_render_spec 不是“直接拿来画”的最终指令，而是 C 端 adapter/render planner 的输入。C 端需要理解字段含义并转换为内部渲染模型。**

---

## 2. 顶层字段

| 字段 | 类型 | 角色 C 用法 | 是否可直接渲染 | 说明 |
|---|---|---|---|---|
| `schema_version` | string | 判断协议版本 | 可直用 | 版本不匹配应拒绝或降级 |
| `deck_id` | string | 绑定交付包/渲染任务 | 可直用 | 用于日志、文件名、追踪 |
| `positioning` | string | 文件定位说明 | 不渲染 | 告诉 C 这是约束层，不是内容源 |
| `samples` | array | 样例页列表 | 需逐页转换 | 每个元素是一页 page_render_spec |

---

## 3. 单页 page_render_spec 字段

| 字段 | 类型 | 角色 C 用法 | 是否可直接渲染 | 说明 |
|---|---|---|---|---|
| `schema_version` | string | 版本检查 | 可直用 | 当前为 `0.1` |
| `deck_id` | string | 任务绑定 | 可直用 | 与上游 deck 对齐 |
| `slide_no` | integer | 匹配 deck_spec 第几页 | 可直用 | C 端必须据此找到对应 slide |
| `page_id` | string | 稳定页 ID | 可直用 | 用于缓存、日志、人工评审 |
| `spec_level` | string | 决定约束强度 | 需转换 | `light/full` 影响 C 端是否启用完整检查 |
| `page_risk_level` | string | 风险提示 | 不直接渲染 | 决定失败时是否 manual_review |
| `trigger_reason` | array[string] | 触发原因 | 不直接渲染 | 帮 C 判断为何不能走普通模板 |
| `source_trace` | object | 源字段追踪 | 不直接渲染 | C 端用来回查 deck_spec/page_copy/page_design |
| `derived_contract` | object | 从上游继承的语义合同 | 部分可直用 | C 端必须以此为准，不可新增内容 |
| `subtype` | object | 复杂页子类型 | 需转换 | 决定选择哪种复杂页渲染 planner |
| `render_units` | array | 可渲染单元列表 | 需转换 | 最接近渲染的核心字段，但仍需布局求解 |
| `text_fit_policy` | object | 文本适配策略 | 需转换 | 控制压缩、截断、拆分、人工评审 |
| `render_unit_policy` | object | 页面级视觉/组件策略 | 需转换 | 控制红色预算、主焦点、层级、禁用模式 |
| `render_validation` | object | 渲染验收规则 | 不直接渲染 | 渲染后检查；失败则 manual_review |

---

## 4. source_trace 字段

| 字段 | 角色 C 用法 |
|---|---|
| `deck_spec_ref` | 找到该页原始语义合同 |
| `page_design_ref` | 找到该页设计说明 |
| `page_copy_ref` | 找到该页文案来源 |
| `source_evidence_ref` | 找到证据清单，避免新增事实 |
| `inherited_fields` | 告诉 C 哪些字段是从上游继承，不允许擅自改写 |

C 端使用原则：

```text
如果 page_render_spec 与 deck_spec/page_design 语义冲突：
  deck_spec/page_design 优先；
  page_render_spec 只作为构造约束修正。
```

---

## 5. derived_contract 字段

| 字段 | 角色 C 用法 |
|---|---|
| `title` | 页面标题，直接进入标题区，但需文本适配 |
| `core_judgement` | 页面唯一判断，不一定全文上屏，但必须指导主图和强调 |
| `layout_pattern` | 选择页面布局蓝图 |
| `chart_type` | 选择主图表组件 |
| `chart_proof_goal` | 校验主图是否证明标题判断 |
| `chart_visual_boundary` | 渲染禁区与视觉约束 |
| `bottom_conclusion` | 底部收口文本候选 |
| `right_insight_panel` | 右侧洞察栏内容与限制 |
| `red_anchor` | 唯一红色锚点目标与预算 |
| `card_hierarchy` | 组件主次层级 |
| `spacing_rule` | 区域间距与安全区 |
| `visual_simplification` | 需要删除/弱化的装饰项 |

---

## 6. render_units 字段

`render_units` 是 page_render_spec 中最接近 C 端渲染的数据，但仍不是 shape 指令。

| 字段 | 角色 C 用法 | 是否可直接渲染 |
|---|---|---|
| `unit_id` | 渲染单元唯一 ID | 可直用 |
| `unit_type` | 选择组件类型，如 title/chart/card/table/footer | 需映射 |
| `semantic_role` | 解释该单元为何存在 | 不直接渲染 |
| `content_source` | 指向内容来源 | 需解析 |
| `priority` | 决定视觉层级与压缩顺序 | 需转换 |
| `region_intent` | 区域意图描述 | 需布局求解 |
| `max_text_lines` | 文本行数限制 | 可转约束 |
| `overflow_action` | 溢出处理方式 | 可转策略 |
| `visual_constraints` | 单元视觉约束 | 需解释转换 |

C 端推荐处理：

```text
for unit in render_units:
  1. 按 unit_type 选择组件类
  2. 按 content_source 拉取文本/数据
  3. 按 priority 分配视觉权重
  4. 按 region_intent + layout_pattern 求解区域
  5. 按 max_text_lines/overflow_action 做文本适配
  6. 按 visual_constraints 做局部检查
```

---

## 7. text_fit_policy 字段

| 字段 | 用法 |
|---|---|
| `title_max_lines` | 标题最大行数 |
| `card_title_max_lines` | 卡片标题最大行数 |
| `card_body_max_lines` | 卡片正文最大行数 |
| `bottom_conclusion_max_lines` | 底部结论最大行数 |
| `right_insight_max_items` | 右侧洞察最大条数 |
| `compression_order` | 文本压缩顺序 |
| `manual_review_threshold` | 超过阈值时不能静默压缩，必须人工评审 |

---

## 8. render_unit_policy 字段

| 字段 | 用法 |
|---|---|
| `red_anchor_budget` | 控制红色面积和红色使用对象 |
| `primary_focus_count` | 主视觉焦点数量，通常为 1 |
| `card_hierarchy_rule` | 卡片/组件强弱层级 |
| `bottom_bar_rule` | 底部结论条是否允许、颜色强度、高度限制 |
| `right_insight_rule` | 右侧洞察栏条数和角色限制 |
| `spacing_rule` | 模块间距、安全区、页脚间距 |
| `forbidden_patterns` | 禁止渲染成的错误形态 |

---

## 9. render_validation 字段

| 字段 | 用法 |
|---|---|
| `must_pass` | 渲染后必须满足的检查项 |
| `manual_review_if` | 触发人工评审的条件 |
| `expected_builder_behavior` | C 端预期行为，尤其是失败时不能静默改版 |

C 端应实现为：

```text
render_result = render(page_render_spec)
validation_result = validate(render_result, render_validation)
if validation_result.failed or manual_review_if_triggered:
  return manual_review
```

---

## 10. 直接渲染能力判断

| 能力层级 | page_render_spec 是否满足 | 说明 |
|---|---|---|
| 找到目标页 | 满足 | `slide_no/page_id` 可直用 |
| 找到内容来源 | 满足 | `source_trace/content_source` 可定位 |
| 拆分渲染单元 | 基本满足 | `render_units` 给出组件级单元 |
| 选择组件类型 | 部分满足 | `unit_type/chart_type/subtype` 需映射到 C 端组件库 |
| 文本适配 | 基本满足 | 有行数和溢出策略 |
| 视觉约束 | 基本满足 | 有红色、层级、禁用模式 |
| 坐标和 shape | 不满足 | 需 C 端布局求解 |
| 自动验收 | 部分满足 | 规则是自然语言，需 C 端实现检查器或人工评审 |

结论：`page_render_spec_samples_v0.1.json` **可以作为 C 端 render planner 的输入，但不能直接等同于可绘制 shape DSL**。若目标是“零理解直接渲染”，后续还需要新增 `normalized_render_model` 或 `shape_plan` 层。
