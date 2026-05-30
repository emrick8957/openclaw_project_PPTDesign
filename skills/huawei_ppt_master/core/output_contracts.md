# 输出契约

## 1. 大纲输出契约

输出必须包含：

1. 汇报对象；
2. 汇报目标；
3. 总体叙事主线；
4. 章节分组；
5. 每页页码；
6. 每页结论型标题；
7. 每页核心结论；
8. 每页建议图表；
9. 每页回答的问题；
10. 后续逐页文案建议。


每页必须包含：

```text
P{n} {页标题}
核心结论：
页面类型：
建议图表：
页面设计说明：
该页回答的问题：
```

超过 12 页必须增加章节分组。

## 2. 逐页文案输出契约

输出必须包含：

1. 页码；
2. 页标题；
3. 一句话结论；
4. 正文模块；
5. 图表内容说明；
6. 版式建议；
7. 讲解口径；
8. 数据缺口或待补材料；
9. 是否适合直接进入 PPTX 生成。

每页必须包含：

```text
页标题：
一句话结论：
正文模块：
图表内容：
版式说明：
讲解口径：
数据缺口：
```

## 3. 页面设计说明输出契约

输出必须包含：

1. 页面类型；
2. 推荐版式模式；
3. 标题区设计；
4. 正文区设计；
5. 图表区设计；
6. 页脚规则；
7. 配色建议；
8. 信息密度控制；
9. PPTX Builder 实现提示；
10. 可能的压缩/拆页建议。
11. 视觉降噪约束，包括红色锚点、卡片层级、间距规则、底部结论条规则、需弱化的装饰元素、负面视觉边界和页型门禁。

必须包含：

```text
版式模式：
区域划分：
标题区：
图表区：
文字区：
强调元素：
页脚：
PPTX Builder 注意事项：
视觉降噪约束：
  red_anchor：
  card_hierarchy：
  spacing_rule：
  bottom_bar_rule：
  visual_simplification：
  visual_boundary：
  page_type_gate：
```

## 4. deck_spec.json 输出契约

当用户要求输出 `deck_spec.json`，或用户未明确限制交付范围且当前任务采用本 Skill 默认全套交付链路时，输出严格 JSON。

### 4.0 deck_spec 证明契约字段

每页必须新增以下字段，用于约束“本页到底要证明什么”：

- `core_judgement`：本页唯一核心判断。它不是展示标题，也不是普通结论句，而是本页所有内容、图表和视觉元素必须共同服务的判断锚点。
- `chart_proof_goal`：本页主图表必须证明什么。用于约束 `chart_type` 的论证任务，防止图表只做装饰或信息罗列。
- `chart_visual_boundary`：本页主图表的视觉表达边界。通常为 3~5 条短约束，说明不得画偏成什么、必须体现什么、红色/主次/结构应如何控制。
- `chart_semantic_mapping`：本页主图表的语义解释映射。用于说明主图表如何证明 `chart_proof_goal`，避免图表沦为装饰、模板或误读。`trend_curve` 必须输出，`quadrant_matrix`、`roadmap_timeline_chart`、`architecture_flow_diagram`、`layered_stack_diagram`、`value_chain_loop`、`swimlane_process`、`ecosystem_relationship_map` 等高语义风险图表建议输出。

字段边界：

- `core_judgement` 管“这一页唯一判断是什么”；
- `chart_proof_goal` 管“图表要证明什么”；
- `chart_visual_boundary` 管“图表不能怎么画 / 视觉表达边界”；
- `chart_semantic_mapping` 管“图表如何被阅读、如何证明、坐标/阶段/节点/洞察栏分别代表什么”；
- `chart_type` 仍只允许使用 `templates/chart_patterns.md` 中的合法枚举；
- `layout_pattern` 仍只允许使用 `visual_patterns/layout_library.md` 中的合法枚举。

### 4.0.1 字段差异化要求

`core_judgement`、`chart_proof_goal`、`chart_visual_boundary` 不只是必填字段，还必须承载逐页设计决策。具体字段职责、允许重复白名单、正反例和下沉规则以 `core/field_differentiation_rules.md` 为准。

关键要求：

- `core_judgement` 不得等于 `conclusion`，也不得只是固定前缀 + `conclusion`；允许对 `conclusion` 做正当提炼或收口；
- `chart_proof_goal` 必须说明主图证明的因果、对比、演进、闭环、分层、决策或权衡关系；
- `chart_visual_boundary` 必须结合本页图表风险和 `chart_semantic_mapping.forbidden_visualization`，不得多页复用同一组泛化边界；
- 通用视觉规范应下沉为全局默认，不得逐页重复伪装成页面设计。

输出严格 JSON：

```json
{
  "deck_title": "",
  "audience": "",
  "style": "huawei_executive",
  "slides": [
    {
  "slide_no": 1,
  "section": "第一章 核心判断",
  "type": "executive_summary",
  "page_goal": "让高层在1分钟内看懂整体结论",
  "title": "当前竞争焦点不是“哪张卡更强”，而是“谁能形成可持续算力体系”",
  "conclusion": "英伟达整体领先，但昇腾在国产化、安全可控和重点行业适配上具备战略价值。",
  "core_judgement": "本页唯一要让高层带走的判断：竞争焦点从单卡性能转向可持续体系能力。",
  "chart_proof_goal": "主图表必须证明：领先、差距、风险和建议共同指向体系化竞争，而不是单点能力比较。",
  "chart_visual_boundary": [
    "不得画成无主次的四张并列卡片",
    "必须突出唯一主判断卡和支撑卡层级",
    "红色只能用于核心判断或关键风险，不能多处抢焦点"
  ],
  "chart_semantic_mapping": {
    "chart_reading_intent": "读者看完图后应形成的唯一判断",
    "main_visual_logic": "主图通过主次、方向、分层、对比、趋势或闭环证明判断",
    "axis_semantics": {},
    "stage_or_node_meaning": {},
    "insight_panel_logic": [],
    "forbidden_visualization": ["不得把图表画成装饰性模板"]
  },
  "display_text": [
    "英伟达领先在通用生态、开发者心智和训练体系",
    "昇腾具备国产化、安全可控和供应连续性优势",
    "核心短板在生态成熟度、迁移效率和复制能力",
    "建议以样板场景牵引补齐算力—模型—工具—运营闭环"
  ],
  "speaker_notes": "先讲总体判断，再讲差距和动作建议",
  "chart_type": "key_findings_cards",
  "chart_data": {},
  "layout_pattern": "executive_summary_dashboard",
  "visual_notes": "白底，红色强调结论，四象限卡片式布局",
  "visual_focus": [
    "领先",
    "差距",
    "风险",
    "建议"
  ],
  "must_highlight": [
    "体系竞争",
    "国产化",
    "生态成熟度"
  ],
  "text_density": "medium",
  "need_compression": false,
  "data_gaps": []
}
  ]
}
```

### 4.1 deck_spec 契约检查
- `chart_type` 是否描述图表/信息结构，而非页面版式；
- `layout_pattern` 是否为版式模式，且可在版式库中找到；
- 若同名同时出现在 `chart_type` 与 `layout_pattern`，应判定为需复核；
- Builder 是否可直接据此生成 page_images / pptx。

### 4.2 deck_spec 字段边界补充
- `chart_type` 表示图表或信息结构类型；
- `layout_pattern` 表示页面布局模式；
- 两者不得混用。

#### 生成deck_spec.json 时，`chart_type` 字段必须从 `templates/chart_patterns.md` 文件中选择图表
推荐 `chart_type` 常用图表包括：


#### 生成deck_spec.json时，`layout_pattern`字段必须从 `visual_patterns/layout_library.md` 文件中选择模式，或`visual_patterns/` 目录下的相关版式文件中选择。





### 4.3 deck_spec 强门禁
生成 `deck_spec.json` 时，必须先完成以下检查：

1. `chart_type` 必须严格取自 `templates/chart_patterns.md` 已定义枚举；
2. `layout_pattern` 必须严格取自 `visual_patterns/layout_library.md` 已定义枚举；
3. 若 `chart_type == layout_pattern`，直接判定失败，必须重选；
4. 若 `chart_type` 命中 layout 黑名单，直接判定失败；
5. 若 `layout_pattern` 命中 chart 黑名单，直接判定失败；
6. 若字段不在合法枚举内，不得输出最终 `deck_spec.json`；
7. 必须先确定 `chart_type`，再确定 `layout_pattern`，不得反向从版式名推导图表名并直接复用同名值。
8. 每页必须包含 `core_judgement`、`chart_proof_goal`、`chart_visual_boundary`。
9. 当 `chart_type=trend_curve` 时，必须包含 `chart_semantic_mapping`；其他高语义风险图表建议包含该字段。
10. `chart_semantic_mapping` 必须服务 `chart_proof_goal`，不得另起一套判断。
11. `chart_proof_goal` 必须能直接支撑 `core_judgement`，否则判定该页图表论证目标不成立。
12. `chart_visual_boundary` 必须为数组，建议 3~5 条，不得为空泛口号。
13. 必须通过 `eval/template_stamp_detection.md` 的模板印章检测。
14. 重复判定必须使用混合阈值模型：N<=3 两两比较，N>=4 使用 `repeat_threshold=max(3,ceil(N*0.5))`。
15. `core_judgement` 不得等于 `conclusion` 或固定前缀 + `conclusion`。
16. `chart_visual_boundary`、`visual_notes` / page_design overrides 若在混合阈值模型下触发重复 FAIL，必须返工；如为通用规则，必须拆入 `global_design_defaults`。
17. `chart_data` 的键名、列名、节点结构相似不判 FAIL，只判语义内容是否机械重复。
18. `chart_data` 中 logic-only 字段不得作为可见标签上屏，包括但不限于 `group`、`emphasis`、`source_status`；
19. 若需要可见分组标题，必须使用 `label`、`name`、`headline`、`display_text`、`lane.name`、`layer.name` 或 `stage.name` 等显示内容字段，不得复用 `group`；
20. `edges.label` 只能承载短动作词或短关系词，不得承载复杂关系语义；复杂关系语义必须进入 `chart_semantic_mapping`；
21. 不得在 `chart_data` 内新增 `relation_type`、`edge_style`、`position`、`anchor`、`x/y`、`layer_index` 等渲染或关系 DSL 字段。
22. 高语义风险关系图（双分支 / 同层对应 / 层级支撑 / 闭环）若需声明关系角色：同层对应只能由 `chart_semantic_mapping.correspondence_pairs` 承载，`edge_roles` 不得出现 `same_level_correspondence` 角色（单一事实源）。
23. `chart_semantic_mapping.edge_roles` 的边引用必须为结构化 `{"from":<id>,"to":<id>}`，不得使用 `"from->to"` 字符串；`edge_roles` 引用的边必须命中 `chart_data.edges` 已存在的边，`correspondence_pairs` 引用的 id 必须命中 `chart_data` 已存在的节点，不得引入影子边/影子节点。


### 4.4 无精确匹配时的唯一合法处理
如果设想的图表或版式没有精确匹配项，必须按以下顺序处理：

1. 优先选择最接近的通用 `chart_type`；
2. 再选择最接近的通用 `layout_pattern`；
3. 将差异、特化要求、视觉补充说明写入 `visual_notes`；
4. 不得自造新的 `chart_type` 或 `layout_pattern` 枚举值；
5. 如确实需要新增模式，只能在评审/优化环节输出 patch proposal，不得直接写入正式交付物。

