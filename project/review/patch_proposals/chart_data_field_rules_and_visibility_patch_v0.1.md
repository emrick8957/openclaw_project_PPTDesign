# mini patch proposal：chart_data 字段通则与字段可见性 v0.1

> 状态：Phase 0 proposal，仅供人工确认；未修改 `skills/huawei_ppt_master/*`。
> 来源：本次系统工程 V 模型单页交付的角色 C 渲染偏差复盘（group 字面泄漏、关系语义无处安放）。
> 合并两条讨论结论：(1) group 等逻辑字段 logic-only 不上图；(2) chart_data 字段按"风险×价值"分层，关系语义归 chart_semantic_mapping，不在 chart_data 内发明 relation 字段。

## 1. 目标版本

建议版本：`v0.4.x-chart-data-field-rules`（可与防套版门禁合并为同一 minor 版本落地）

目标：在不把 deck_spec 变成渲染 DSL 的前提下，明确 chart_data 各字段"要不要规则、谁来消费"，堵住两类问题：
- 逻辑字段（如 `group`）被角色 C 字面渲染为可见标签；
- 关系语义（方向、同层对应、层级、闭环）无处安放，被迫塞进 `label` 字符串或 `chart_visual_boundary` 散文，导致渲染多解。

## 2. 设计原则（本 patch 的判定内核）

### 2.1 字段规则判据

一个 chart_data 字段，**仅当满足以下任一条**才需要写规则：

1. 会被字面渲染且可能泄漏/误导 → 写"可见性规则"；
2. 内容质量影响论证、可能编造 → 写"内容规则"；
3. 承载关系语义且角色 C 可能渲染偏离 → **不在 chart_data 内解决，交 `chart_semantic_mapping`**。

否则（纯拓扑/管道字段、行业通用图结构语法）→ **不写规则**，避免契约膨胀。

### 2.2 边界

- chart_data 只承载"拓扑 + 内容"；
- 关系语义（方向/对应/层级/闭环）归 `chart_semantic_mapping`；
- 禁止在 edges/nodes 内发明 `relation_type` 等结构化关系字段（这会复辟 page_render_spec / 渲染 DSL）；
- 本 patch 不规定坐标、字号、线宽、连接线样式等 shape 参数。

## 3. 建议修改文件

### 3.1 `skills/huawei_ppt_master/core/deck_spec_field_dictionary.md`

在现有 `## 3. slide 字段` 之后，新增一节：

建议新增内容（注意：落地时若内层出现代码块，请用缩进或 ~~~ 包裹，避免围栏嵌套破损）：

---

## 4. chart_data 字段通则与可见性约定

### 4.1 字段分层

不同 `chart_type` 的 `chart_data` 结构不同（cards / columns+rows / nodes+edges / layers+items / stages 等），但其字段可统一归为三类，规则跨所有 chart_type 通用：

| 类别 | 典型字段 | 是否需要规则 | 规则 |
|---|---|---|---|
| 拓扑/管道字段 | `nodes`、`edges`、`id`、`from`、`to`、`rows`、`columns`、`layers`、`stages` 等结构键 | 否 | 通用图/表结构语法，角色 C 按标准结构消费，无需额外语义规则 |
| 显示内容字段 | `label`、`name`、`headline`、`items`、`description`、单元格文本等 | 是 | 短语化、控制长度、避免长句；不得编造未提供的数字/案例；遵守 `wording_rules.md` 与 `visual_rules.md` 的节点短语化要求 |
| 逻辑字段 | `group`、`emphasis`、`source_status` 等仅用于分组/标记 | 是 | **logic-only：仅供逻辑分组或渲染判断，不得被字面渲染为节点/卡片可见标签** |

### 4.2 logic-only 字段清单（不得直接上屏）

以下字段仅用于逻辑、约束或讲解，角色 C **不得**将其原文渲染为页面可见文本：

- slide 级：`page_goal`、`core_judgement`、`chart_proof_goal`、`section`（仅作页眉小标签时除外）；
- chart_data 级：`group`、`emphasis`、`source_status`。

若需要可见的分组标题，应由 `display_text`、`label` 或专门的可见字段承载，而不是复用逻辑字段。

### 4.3 关系语义的承载位置

方向（自顶向下/自底向上）、同层对应、层级支撑、闭环回写等**关系语义**，统一由 `chart_semantic_mapping` 承载：

- `main_visual_logic`：说明主图通过什么关系（方向/对应/层级/闭环）证明判断；
- `stage_or_node_meaning`：说明每个节点/阶段的含义；
- `forbidden_visualization`：说明禁止的退化形态（如禁线性化、禁错层、禁单向）。

**禁止**在 `chart_data` 的 nodes/edges 内新增 `relation_type` 等结构化关系字段；关系语义不进 chart_data。

---

### 3.2 `skills/huawei_ppt_master/templates/chart_patterns.md`

在 `## 5. 图表使用规则` 或 `## 0. chart_type 与 layout_pattern 的边界` 附近，增加一条指引：

- chart_data 字段规则与可见性约定见 `core/deck_spec_field_dictionary.md` 的"chart_data 字段通则"；关系语义由 `chart_semantic_mapping` 承载，不在 chart_data 内发明关系字段。

### 3.3 `skills/huawei_ppt_master/prompts/deck_spec_generation.md`

在"生成时必须检查"中追加：

- `chart_data` 内逻辑字段（如 `group`）不得作为可见标签上屏；
- 方向、同层对应、层级、闭环等关系语义必须写入 `chart_semantic_mapping`，不得仅塞进 `label` 文本或新增关系字段。

### 3.4 版本同步文件（落地后）

- `README.md`、`VERSION.md`、`CHANGELOG.md`、`INDEX.md`、`QUICK_INDEX.md`、`PACKAGE_MANIFEST.md`

字典若新增章节，需在 manifest/index 中体现章节更新（文件路径不变，无需新增文件）。

## 4. 回归用例

### 4.1 RT-01：group 不上屏（必须通过）

构造 architecture_flow_diagram 页，`group="左支-定义"`。预期：角色 C 渲染结果中不出现"左支-定义"字面标签；分组仅影响布局归类。

### 4.2 RT-02：关系语义归位（必须通过）

构造 V 模型类页面，方向/同层对应写入 `chart_semantic_mapping.main_visual_logic` 与 `forbidden_visualization`。预期：deck_spec 的 chart_data 内无 `relation_type` 等字段；语义检查通过。

### 4.3 RT-03：管道字段不被过度文档化（防膨胀）

检查字典与提示词：`id/from/to/nodes/edges` 未被逐字段写消费规则。预期：通过（保持轻量）。

### 4.4 RT-04：label 内容规则（必须通过）

构造节点 `label` 为长句的页面。预期：自检提示 label 应短语化，触发 WARN。

## 5. 不做事项

- 不恢复 `page_render_spec` / `normalized_render_model`；
- 不在 chart_data 内新增 `relation_type` 等关系字段；
- 不规定坐标、字号、线宽、shape 参数；
- 不给纯拓扑/管道字段逐字段写消费规则；
- 不把字段通则按 17 个 chart_type 逐一展开（保持单一通则，跨类型复用）。

## 6. 合入建议

本 patch 轻量、零新增文件、确定性高、与 DSL 边界清晰，建议作为下一轮评审对象；可与 `anti_template_stamp_gate` 合并为同一 minor 版本落地，减少版本碎片。
