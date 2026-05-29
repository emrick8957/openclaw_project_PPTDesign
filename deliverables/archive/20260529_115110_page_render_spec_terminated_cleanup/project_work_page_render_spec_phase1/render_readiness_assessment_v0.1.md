# Phase 1 渲染就绪度评估 v0.1

## 1. 问题回应

### 问题 1：deck_spec.json 每个字段的作用，角色 C 能理解吗？

当前状态：**字段含义对 A 侧清楚，但对 C 侧不够显式。**

原因：

- 字段有语义，但缺少 C 端字段字典；
- `chart_type`、`layout_pattern` 只是枚举名称，不是组件实现；
- `core_judgement`、`chart_proof_goal`、`chart_visual_boundary` 是论证约束，不是绘图指令；
- C 端需要知道哪些字段上屏、哪些字段只用于校验。

已补充：

- `deck_spec_field_dictionary_for_role_C.md`

结论：补充字段字典后，C 端可以理解字段职责，但仍需要 adapter 转换。

---

### 问题 2：page_render_spec_samples_v0.1.json 每个字段的作用，角色 C 能理解怎么用吗？

当前状态：**比 deck_spec 更接近 C 端，但仍不是直接渲染 DSL。**

原因：

- `render_units` 已经拆到组件级，但 `region_intent` 仍是自然语言区域意图；
- `visual_constraints`、`must_pass`、`manual_review_if` 仍是自然语言规则；
- `unit_type` 需要映射到 C 端组件库；
- 没有 x/y/w/h、字号、颜色 token、z-index、connector path 等 shape 参数。

已补充：

- `page_render_spec_field_dictionary_for_role_C.md`
- `role_C_consumption_guide_v0.1.md`

结论：C 端可以把它作为 render planner 输入，但不能直接当 shape plan 渲染。

---

## 2. 三层协议判断

| 层级 | 当前产物 | 作用 | 是否已有 | 是否可直接渲染 |
|---|---|---|---|---|
| 语义层 | `deck_spec.json` | 页面讲什么、证明什么、用什么图表/版式 | 已有 | 否 |
| 构造约束层 | `page_render_spec_samples_v0.1.json` | 复杂页拆单元、控文本、控层级、控验收 | 已有样例 | 否，需转换 |
| 标准渲染模型层 | `normalized_render_model.json` | region/component/style/constraint 标准化 | 未有 | 接近可渲染 |
| Shape 指令层 | `shape_plan.json` | 坐标、字号、颜色、z-index、连接线 | 未有 | 是 |

---

## 3. 当前缺口

1. 缺少 C 端 adapter 规范；
2. 缺少 `layout_pattern -> region blueprint` 的机器可读映射；
3. 缺少 `chart_type -> component renderer` 的机器可读映射；
4. 缺少 `unit_type -> PPTX component` 的映射；
5. 缺少从自然语言约束到可执行 validation 的规则化表达；
6. 缺少坐标/字号/颜色 token 等 shape plan。

---

## 4. 建议修正方向

### 短期：Phase 1.1

补充两类说明文件，不改 Skill：

1. 字段字典；
2. C 端消费指南；
3. 渲染就绪度评估；
4. 可选：给 P7/P8/P14 各生成一个 `normalized_render_model` 样例。

当前本次已完成 1–3。

### 中期：Phase 2

在不改 Skill 的前提下，扩展：

- `layout_blueprint_map_v0.1.json`
- `chart_component_map_v0.1.json`
- `unit_type_component_map_v0.1.json`
- P7/P8/P14 的 `normalized_render_model` 样例

### 后续：Phase 3

让 C 端基于 `normalized_render_model` 做消费验证，记录：

- 哪些字段 C 可直接使用；
- 哪些字段必须人工解释；
- 哪些规则需要转成机器可执行；
- 哪些页面必须回退 manual_review。

---

## 5. 最终判断

这次发现的问题不是小问题，而是 A→C 协作的关键边界：

- `deck_spec` 不应假装自己是渲染指令；
- `page_render_spec` 也不应直接承担 shape DSL；
- 正确链路应增加一层 C 端可执行的 `normalized_render_model`。

建议下一步不要直接沉淀进 Skill，而是先做 Phase 1.1/Phase 2：把 C 端 adapter 需要的字段映射和标准渲染模型样例补齐。
