# 角色 C 消费指南 v0.1

## 1. 核心结论

当前 Phase 1 交付物分两层：

1. `deck_spec.json`：页面语义合同；
2. `page_render_spec_samples_v0.1.json`：复杂页构造约束。

二者都不是最终 PPTX shape 指令。

角色 C 不能简单地把 JSON 字段逐个画出来，而应经过一层转换：

```text
deck_spec + page_design + page_copy
        ↓
page_render_spec（复杂页才有）
        ↓
角色 C adapter / render planner
        ↓
内部 normalized render model
        ↓
PPTX shapes / page image
```

---

## 2. 两个 JSON 的职责边界

| 文件 | 核心职责 | C 端如何用 | 是否直接渲染 |
|---|---|---|---|
| `deck_spec.json` | 告诉 C 每页讲什么、用什么图表、用什么版式 | 作为所有页面的语义输入 | 不能直接渲染，需要转换 |
| `page_render_spec_samples_v0.1.json` | 告诉 C 高风险页怎么拆组件、怎么控文本、怎么验收 | 作为 P7/P8/P14 的额外构造约束 | 接近渲染，但仍需转换 |
| `page_copy_v0.1.md` | 提供逐页文案和讲解口径 | 内容回查/备注来源 | 不直接渲染全部内容 |
| `page_design_v0.1.md` | 提供版式和视觉说明 | 渲染风格和区域策略参考 | 需转换 |
| 依赖文件 | 提供视觉、图表、文案、版式规则 | C 端规则库/校验依据 | 不直接渲染 |

---

## 3. 推荐 C 端 adapter 流程

### Step 1：加载基础规则

```text
load visual_rules.md
load chart_patterns.md
load wording_rules.md
load layout_library.md
```

将其转换为 C 端内部 token / enum / rule：

- style tokens：颜色、字号、页脚、安全区；
- layout templates：`layout_pattern` → 区域蓝图；
- chart components：`chart_type` → 图表组件；
- text policies：标题行数、卡片行数、压缩策略。

### Step 2：读取 deck_spec

```text
for slide in deck_spec.slides:
  create semantic_page_model
```

最小字段映射：

```json
{
  "page_no": "slide_no",
  "title": "title",
  "core_judgement": "core_judgement",
  "layout_template": "layout_pattern",
  "chart_component": "chart_type",
  "chart_payload": "chart_data",
  "display_text": "display_text",
  "highlight_terms": "must_highlight",
  "visual_constraints": "chart_visual_boundary"
}
```

### Step 3：检查是否存在 page_render_spec

```text
if slide_no in page_render_spec.samples:
  merge complex_page_constraints
else:
  use default layout/chart adapter
```

合并原则：

```text
content semantics: deck_spec 优先
visual/design intent: page_design 优先
complex construction constraints: page_render_spec 补充
conflict: 不静默覆盖，返回 manual_review
```

### Step 4：生成 normalized render model

建议角色 C 内部生成一个更接近绘制的模型，例如：

```json
{
  "page_no": 7,
  "canvas": {"ratio": "16:9"},
  "regions": [
    {"id": "title_region", "role": "title", "bounds_policy": "top_12_percent"},
    {"id": "main_region", "role": "chart", "bounds_policy": "body_left_70_percent"},
    {"id": "insight_region", "role": "right_insight", "bounds_policy": "right_28_percent"},
    {"id": "footer_region", "role": "footer", "bounds_policy": "bottom_5_percent"}
  ],
  "components": [
    {"id": "title", "component": "text_box", "source": "title", "max_lines": 2},
    {"id": "main_chart", "component": "architecture_flow", "source": "chart_data"}
  ],
  "validation": ["red_anchor_count <= 1", "footer_not_overlap"]
}
```

这个 `normalized render model` 才是更适合直接进入 PPTX shape 生成的一层。

---

## 4. 当前字段可用性分级

### A 类：C 可直接使用

- `slide_no`
- `page_id`
- `title`，但需文本适配
- `display_text`，但需布局编排
- `chart_data` 中的表格 rows/columns、layers、nodes/edges
- `max_text_lines`
- `overflow_action`

### B 类：C 需映射后使用

- `layout_pattern`
- `chart_type`
- `type`
- `spec_level`
- `subtype.subtype_enum`
- `visual_focus`
- `must_highlight`
- `red_anchor`
- `card_hierarchy`
- `spacing_rule`
- `bottom_bar_rule`
- `right_insight_rule`

### C 类：C 用于校验/决策，不直接画

- `page_goal`
- `core_judgement`
- `chart_proof_goal`
- `chart_visual_boundary`
- `trigger_reason`
- `page_risk_level`
- `forbidden_patterns`
- `must_pass`
- `manual_review_if`
- `expected_builder_behavior`
- `data_gaps`

---

## 5. 三页样例的 C 端使用方式

### P7 双 V 生命周期架构

C 端应：

1. 用 `subtype=dual_v_lifecycle_architecture` 选择双 V/生命周期 planner；
2. 用 `render_units.dual_v_main` 生成主图；
3. 用 `ai_touchpoints` 生成七类介入点标签；
4. 用 `right_insight` 生成右侧洞察栏；
5. 用 `render_validation` 检查是否退化成散点图或普通流程图。

若 C 端没有双 V planner：返回 `manual_review`，不要静默改成四卡片。

### P8 自学习数字孪生架构

C 端应：

1. 用 `subtype=self_learning_digital_twin_architecture` 选择分层架构 + 闭环 planner；
2. 用 `chart_data.layers` 生成四层结构；
3. 用 `feedback_loop` 生成唯一红色闭环箭头；
4. 用 `bottom_conclusion` 生成浅灰底部收口；
5. 检查是否退化为静态堆栈。

若无法表达闭环箭头：返回 `manual_review`。

### P14 决策收口页

C 端应：

1. 用 `subtype=decision_closeout` 选择拍板页 planner；
2. 用 `decision_card` 生成主拍板卡；
3. 用 `decision_table` 生成 3 行 4 列执行清单；
4. 用 `bottom_conclusion` 生成最终收口；
5. 检查表格是否吞没决策结论。

若只能生成 Excel 大表：返回 `manual_review`。

---

## 6. 需要补的下一层协议

如果目标是让角色 C “更少理解、更多执行”，建议 Phase 2/3 增加一层：

```text
normalized_render_model.json
```

它应包含：

- 标准 canvas；
- region 列表；
- component 列表；
- component 到内容源的绑定；
- style token；
- layout constraints；
- validation rules；
- fallback/manual_review 行为。

再往下，如果目标是“完全直接渲染”，还需要：

```text
shape_plan.json
```

它才应包含：

- x/y/w/h；
- font size；
- fill/stroke；
- z-index；
- connector path；
- table cell style；
- text box bounds。

---

## 7. 当前结论

当前 Phase 1 交付物对 C 端是 **可理解、可转换、可评审**，但不是 **零转换、可直接绘制**。

更准确的定位是：

> `deck_spec` 决定“画什么和为什么画”；`page_render_spec` 决定“复杂页应该拆成哪些渲染单元、受哪些约束”；角色 C 仍需要 adapter/render planner 把它们转换成内部渲染模型，再生成 PPTX。
