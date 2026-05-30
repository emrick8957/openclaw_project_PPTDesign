# mini patch proposal：chart_data 字段通则与字段可见性 v0.2

> 状态：Phase 0 revised proposal，仅供人工确认；未修改 `skills/huawei_ppt_master/*`。  
> 来源：角色 C 渲染偏差复盘与 `chart_data_field_rules_and_visibility_patch_review_v0.1.md`。  
> 本版重点：吸收 v0.1 评审意见，明确 logic-only 字段、可见字段、edge label、section 弱显示、output_contracts 强门禁和目标版本。

## 1. 目标版本

建议版本：`v0.4.1-chart-data-visibility`

目标：在不把 `deck_spec.json` 变成渲染 DSL 的前提下，明确 `chart_data` 各字段“是否可见、谁来消费、关系语义放哪里”，堵住两类问题：

1. 逻辑字段（如 `group`）被角色 C 字面渲染为页面可见标签；
2. 方向、同层对应、层级支撑、闭环回写等关系语义无处安放，被迫塞进 `label` 字符串或散落在 `chart_visual_boundary` 中，导致渲染多解。

## 2. 设计原则

### 2.1 字段规则判据

一个 `chart_data` 字段，仅当满足以下任一条才需要写规则：

1. 会被字面渲染且可能泄漏/误导 → 写“可见性规则”；
2. 内容质量影响论证、可能编造 → 写“内容规则”；
3. 承载复杂关系语义且角色 C 可能渲染偏离 → 不在 `chart_data` 内解决，交给 `chart_semantic_mapping`。

否则：纯拓扑/管道字段、行业通用图结构语法，不逐字段写消费规则，避免契约膨胀。

### 2.2 边界

- `chart_data` 只承载“拓扑 + 内容”；
- 复杂关系语义归 `chart_semantic_mapping`；
- 禁止在 `nodes` / `edges` 内新增 `relation_type` 等结构化关系字段；
- 不规定坐标、字号、线宽、连接线样式、shape 参数；
- 不恢复 `page_render_spec` / `normalized_render_model`。

## 3. 建议修改文件

### 3.1 `skills/huawei_ppt_master/core/deck_spec_field_dictionary.md`

在现有 `## 3. slide 字段` 之后，新增：

---

## 4. chart_data 字段通则与可见性约定

### 4.1 字段分层

不同 `chart_type` 的 `chart_data` 结构不同（cards / columns+rows / nodes+edges / layers+items / stages / lanes 等），但字段可统一归为三类：

| 类别 | 典型字段 | 是否需要规则 | 规则 |
|---|---|---|---|
| 拓扑/管道字段 | `nodes`、`edges`、`id`、`from`、`to`、`rows`、`columns`、`layers`、`stages`、`lanes` 等结构键 | 否 | 通用图/表结构语法，角色 C 按标准结构消费；不逐字段写渲染规则 |
| 显示内容字段 | `label`、`name`、`headline`、`items`、`description`、单元格文本、`edges.label`、`lane.name` 等 | 是 | 可上屏，但必须短语化、控制长度、避免长句；不得编造未提供的数字/案例；遵守 `wording_rules.md` 与 `visual_rules.md` 的节点短语化要求 |
| 逻辑字段 | `group`、`emphasis`、`source_status` 等仅用于分组/标记 | 是 | **logic-only：仅供逻辑分组、样式强弱或渲染判断，不得被字面渲染为节点/卡片/泳道可见标签** |

### 4.2 logic-only 字段清单（不得直接上屏）

以下字段仅用于逻辑、约束、分组或讲解，角色 C 不得将其原文渲染为页面主体可见文本：

- slide 级：
  - `page_goal`：只用于判断页面沟通目标，不直接上屏；
  - `core_judgement`：指导全页判断，是否转写上屏由标题、结论、主卡承担；
  - `chart_proof_goal`：指导主图证明任务，不直接作为图中说明文字；
  - `section`：只可作为页眉/章节弱标签显示，不得作为主体节点、卡片标题或图表标签。
- chart_data 级：
  - `group`：仅用于内部归类、布局分组或样式分组，不得字面上屏；
  - `emphasis`：仅用于强弱层级或视觉强调判断，不得字面上屏；
  - `source_status`：仅用于来源状态判断，不得字面上屏。

### 4.3 可见分组标题应使用什么字段

如果页面需要可见分组标题，不得复用 logic-only 的 `group` 字段，应使用以下可见字段：

- 节点/卡片标题：`label`、`name`、`headline`；
- 页面展示候选：`display_text`；
- 泳道图标题：`lane.name` 可见，`node.group` 不可见；
- 分层图标题：`layer.name` 可见，层内节点的 `group` 不可见；
- 路线图阶段标题：`stage.name` 可见。

判断原则：

- 字段名表达的是“显示文本” → 可以上屏；
- 字段名表达的是“分组/状态/强弱/来源判断” → logic-only，不直接上屏。

### 4.4 edges.label 的可见性边界

`edges.label` 是可见内容字段，但只能承载短动作词或短关系词，例如：

- `回写`
- `验证`
- `编译`
- `生成`
- `仿真`
- `审查`

`edges.label` 不得承载复杂关系解释，例如：

- 为什么回写；
- 回写形成什么闭环；
- 两条 V 模型如何同层对应；
- 层级支撑关系如何证明页面判断。

复杂关系语义必须写入：

- `chart_semantic_mapping.main_visual_logic`；
- `chart_semantic_mapping.stage_or_node_meaning`；
- `chart_semantic_mapping.forbidden_visualization`。

### 4.5 显示内容字段短语化判据

可见字段应短语化，避免长句撑爆节点或卡片：

- `label` / `name`：建议 ≤12 个汉字，或 ≤2 个短语；
- `headline`：建议 ≤16 个汉字；
- `items`：每项建议 ≤14 个汉字；
- `edges.label`：建议 2~6 个汉字，优先动词或动宾短语；
- 长解释应放入 `description`、`speaker_notes`、`chart_semantic_mapping` 或页面洞察区。

若可见字段过长，自检应 WARN；若导致图表变成文字容器，应返工。

### 4.6 关系语义的承载位置

方向（自顶向下 / 自底向上）、同层对应、层级支撑、闭环回写等复杂关系语义，统一由 `chart_semantic_mapping` 承载：

- `main_visual_logic`：说明主图通过什么关系证明判断；
- `stage_or_node_meaning`：说明节点、阶段、层级、泳道的语义；
- `forbidden_visualization`：说明禁止的退化形态，如禁线性化、禁错层、禁单向、禁散点化。

禁止在 `chart_data.nodes` / `chart_data.edges` 内新增 `relation_type`、`edge_style`、`position`、`anchor`、`x/y`、`layer_index` 等渲染或关系 DSL 字段。

---

### 3.2 `skills/huawei_ppt_master/core/output_contracts.md`

在 `### 4.3 deck_spec 强门禁` 中追加：

```md
18. `chart_data` 中 logic-only 字段不得作为可见标签上屏，包括但不限于 `group`、`emphasis`、`source_status`；
19. 若需要可见分组标题，必须使用 `label`、`name`、`headline`、`display_text`、`lane.name`、`layer.name` 或 `stage.name` 等显示内容字段，不得复用 `group`；
20. `edges.label` 只能承载短动作词或短关系词，不得承载复杂关系语义；复杂关系语义必须进入 `chart_semantic_mapping`；
21. 不得在 `chart_data` 内新增 `relation_type`、`edge_style`、`position`、`anchor`、`x/y`、`layer_index` 等渲染或关系 DSL 字段。
```

### 3.3 `skills/huawei_ppt_master/templates/chart_patterns.md`

在 `## 0. chart_type 与 layout_pattern 的边界` 附近增加：

```md
### 0.x chart_data 字段可见性边界

`chart_data` 字段规则与可见性约定见 `core/deck_spec_field_dictionary.md` 的“chart_data 字段通则与可见性约定”。

原则：

- `chart_data` 承载拓扑和可见内容；
- `group`、`emphasis`、`source_status` 等 logic-only 字段不得字面上屏；
- `edges.label` 可作为短动作词上屏，但复杂方向、对应、层级、闭环语义必须写入 `chart_semantic_mapping`；
- 不得在 `chart_data` 内发明 `relation_type` 等关系字段。
```

### 3.4 `skills/huawei_ppt_master/prompts/deck_spec_generation.md`

在“生成时必须检查”中追加：

```md
- `chart_data` 内 logic-only 字段（如 `group`、`emphasis`、`source_status`）不得作为可见标签上屏；
- 若需要可见分组标题，应使用 `label` / `name` / `headline` / `display_text` / `lane.name` / `layer.name` / `stage.name`，不得复用 `group`；
- `edges.label` 只能写短动作词或短关系词，复杂方向、同层对应、层级、闭环语义必须写入 `chart_semantic_mapping`；
- 不得在 `chart_data` 内新增 `relation_type`、`edge_style`、`position`、`anchor`、`x/y`、`layer_index` 等渲染或关系 DSL 字段；
- `label` / `name` / `headline` / `items` / `edges.label` 应短语化，过长时放入 `description`、`speaker_notes` 或 `chart_semantic_mapping`。
```

### 3.5 版本同步文件（落地后）

若进入 Phase 1 落地，需要同步：

- `README.md`
- `VERSION.md`
- `CHANGELOG.md`
- `INDEX.md`
- `QUICK_INDEX.md`
- `PACKAGE_MANIFEST.md`

文件路径不新增，但 `deck_spec_field_dictionary.md` 的章节职责发生扩展，应在 README/CHANGELOG/INDEX 中说明。

## 4. 回归用例

### RT-01：group 不上屏

构造 `architecture_flow_diagram`：

```json
{
  "nodes": [
    {"id": "A", "label": "产品 V 模型", "group": "左支-定义"}
  ]
}
```

预期：

- 渲染结果中可见 `产品 V 模型`；
- 不出现 `左支-定义` 字面标签；
- `group` 只影响布局归类或样式分组。

### RT-02：可见分组标题不用 group

构造需要可见分组标题的页面：

```json
{
  "nodes": [
    {"id": "A", "label": "语义模型", "group": "model_cluster"}
  ],
  "display_text": ["模型底座"]
}
```

预期：

- 可见分组标题使用 `display_text=模型底座` 或专门 `label/name/headline`；
- 不显示 `model_cluster`。

### RT-03：关系语义归位

构造 V 模型类页面，方向 / 同层对应 / 闭环写入：

- `chart_semantic_mapping.main_visual_logic`
- `chart_semantic_mapping.stage_or_node_meaning`
- `chart_semantic_mapping.forbidden_visualization`

预期：

- `chart_data` 内无 `relation_type`；
- `chart_data` 内无 `edge_style` / `position` / `x/y` / `anchor`；
- 语义检查通过。

### RT-04：管道字段不被过度文档化

检查字典与提示词：

- `id`、`from`、`to`、`nodes`、`edges` 仅作为拓扑/管道字段；
- 不逐字段写 C 端 shape 消费规则。

预期：PASS，保持轻量。

### RT-05：label 内容短语化

构造节点：

```json
{"id":"A", "label":"真实系统数据进入语义模型并经过仿真与XAI审查后再回写治理"}
```

预期：

- 自检 WARN：`label` 过长；
- 建议改为 `label="模型回写"`，长解释放入 `description` 或 `chart_semantic_mapping`。

### RT-06：edge label 可见但不承载复杂关系

构造：

```json
{"from":"A", "to":"B", "label":"回写"}
```

预期：

- `label=回写` 可上屏作为短箭头标签；
- “为什么回写、回写形成什么闭环”必须在 `chart_semantic_mapping.main_visual_logic` 中说明。

### RT-07：swimlane lane.name 可见，node.group 不可见

预期：

- `lane.name` 可作为泳道标题；
- `node.group` 只用于内部归类，不直接上屏。

### RT-08：section 只弱显示为页眉

预期：

- `section` 可在页眉弱显示；
- 不得作为主体卡片标题、节点标签或图表标签。

## 5. 不做事项

- 不恢复 `page_render_spec`；
- 不恢复 `normalized_render_model`；
- 不在 `chart_data` 内新增 `relation_type` 等关系字段；
- 不规定坐标、字号、线宽、shape 参数；
- 不给纯拓扑/管道字段逐字段写消费规则；
- 不按所有 chart_type 分别展开字段通则；
- 不把 `deck_spec.json` 变成角色 C 的渲染 DSL。

## 6. 合入建议

v0.2 已吸收 v0.1 评审意见，建议作为下一轮正式评审对象。

若评审通过，可进入 Phase 1 小版本落地，目标版本：

`v0.4.1-chart-data-visibility`
