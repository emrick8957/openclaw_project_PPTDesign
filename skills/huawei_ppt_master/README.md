# huawei_ppt_master Skill v0.3.8

`huawei_ppt_master` 是一个通用华为风格 PPT 生成 Skill，用于生成：

1. PPT 大纲；
2. 逐页文案；
3. 页面设计说明；
4. `deck_spec.json`；
5. 后续 PPTX 生成所需的结构化输入与字段说明。

## v0.3 核心升级

v0.3 建立“参考材料学习框架”：当用户持续提供 PPT、PPT 图片、模板、文本材料或数据材料时，Skill 可按样式层、结构层、表达层、体系层进行抽取，并通过 `core/reference_ingestion_workflow.md`、`core/reference_material_policy.md`、`methodology_patterns/` 与 `eval/reference_learning_regression.md` 实现分层沉淀、边界控制和回归验证。

学习目标包括：

1. 学样子：配色、字体气质、信息密度、页脚规范；
2. 学结构：版式、图表组合、章节组织、页型分工；
3. 学表达习惯：标题句式、结论收口、判断表达、讲解节奏；
4. 学体系：论证框架、行业套路、章节逻辑、决策链条。

## v0.3.8 deck_spec 字段字典正式化

v0.3.8 将 `deck_spec_field_dictionary` 纳入正式交付物说明资产，解决角色 C 对 `deck_spec.json` 字段职责、消费方式和边界理解不一致的问题。

新增资产：

- `core/deck_spec_field_dictionary.md`

该文档只保留三段核心内容：

1. 文件定位：说明 `deck_spec.json` 是页面语义合同，不是 PPTX 或 shape 指令；
2. 顶层字段：说明 `deck_title`、`audience`、`style`、`source`、`slides` 的作用；
3. slide 字段：说明每页字段的职责，以及角色 C 如何消费。

边界说明：

- 本版本不继续推进 `page_render_spec` / `normalized_render_model` 方案；
- 不新增 PPTX 渲染 DSL；
- 不改变默认生成链路；
- 仅将 `deck_spec.json` 字段说明沉淀为后续正式交付物之一。

## v0.3.7 deck_spec 证明契约

v0.3.7 将 deck_spec 从“告诉 Builder 画什么图”升级为“告诉 Builder 这个图必须证明什么、不能画偏成什么”。

新增每页字段：

1. `core_judgement`：本页唯一核心判断；
2. `chart_proof_goal`：本页主图表必须证明什么；
3. `chart_visual_boundary`：本页主图表的视觉表达边界，约束不得退化为装饰、清单、图片墙、大表格或并列计划。

同步资产：`core/output_contracts.md`、`prompts/deck_spec_generation.md`、`core/generation_workflow.md`、`templates/chart_patterns.md`、`eval/visual_scorecard.md`、`eval/acceptance_checklist.md`。

## v0.3.6 视觉规则重构

v0.3.6 基于用户提供的 `visual_rules_v0.2.md`，将 `templates/visual_rules.md` 重构为“只负责视觉设计指导”的专职资产，并保留 0517 多行业模板、v0.3.3 视觉一致性、v0.3.4 视觉语义、v0.3.5 生成图片反馈门禁的历史沉淀。

核心变化：

1. 明确 `visual_rules.md` 不承担内容事实校验、deck_spec 字段解释、生成流程控制、评分规则、证据溯源和文案改写；
2. 细化色彩、区域比例、字体层级、红色锚点、卡片、图标线条、图表视觉语义、右侧洞察栏、底部结论条、图片素材和特殊页型门禁；
3. 增加互联网发布会风、咨询海报风、卡通插画风、政务宣传风、Excel 报表风、学术论文截图风等负面视觉边界；
4. 同步 `generate_page_design.md`、`output_contracts.md`、`generation_workflow.md`，新增 `visual_boundary` 与 `page_type_gate` 输出字段；
5. 同步 `eval/visual_scorecard.md`，增加 v0.3.6 视觉风格边界扣分/降级项。

## v0.3.5 生成图片反馈沉淀

v0.3.5 基于生成 PPT 图片与华为模板对标结果，补齐“结构正确但视觉语义和论证锋芒不足”的规则：

1. 增强正文页红色底座控制，避免普通正文页大红块成为最大视觉焦点；
2. 增强多卡片主次层级，要求区分主卡、支撑卡、注释卡；
3. 增强阅读框架页、案例证明页、决策建议页、路线图页、总结页的页面角色语义；
4. 增强 `case_gallery_cards`、`decision_table`、`capability_map`、`layered_stack_diagram`、`roadmap_timeline_chart` 的失败条件；
5. 新增长标题压缩规则与总结页最终定义规则；
6. 扩展 visual_scorecard，一票降级正文页红色底座过重、卡片平均主义、案例素材墙、决策表吞没结论等问题。

本版本不沉淀具体主题事实、论文术语、客户/产品/案例名或未经核验数字。

## v0.3.3 视觉一致性升级

v0.3.3 根据 SWE Atlas 页面图片与华为风格 PPT 模板对比结果，补齐视觉资产一致性规则：

1. 增加红色锚点预算，正文页主红色焦点不超过 1-2 个；
2. 增加底部结论条降噪规则，普通页避免厚重红色压底；
3. 增加 layout 区域比例、右侧洞察栏宽度和页脚安全区规则；
4. 增加卡片、表格、泳道、价值闭环图的组件级视觉语法；
5. 扩展页面设计 prompt，要求输出 `red_anchor`、`card_hierarchy`、`spacing_rule`、`bottom_bar_rule`、`visual_simplification`；
6. 扩展 visual_scorecard 与 regression cases，用于检查生成页面图片是否符合华为风格的克制、统一、低装饰要求。

---

## v0.2 核心升级

v0.2 不再把“昇腾 vs 英伟达”作为默认主题，而是改为：

> 通用华为风格 PPT 生成内核 + 可条件触发的主题知识包 + 可复用版式库。

因此，当用户输入非 AI 算力主题，例如智慧园区、数据治理、网络安全、客户经营、项目复盘等，Skill 仍应输出大纲、文案和页面设计说明，并且不得无故引入昇腾、英伟达、CUDA、CANN、GPU/NPU、模型迁移等专属概念。

## 推荐安装路径

```text
<workspace>/skills/huawei_ppt_master/
```

## 推荐调用方式

```text
请启用 huawei_ppt_master。
生成《XXX》的华为风格 PPT 大纲、逐页文案、页面设计说明和 deck_spec.json。
要求：遵循 Skill 全链路；deck_spec 字段含义参照 core/deck_spec_field_dictionary.md。
```

## 与其他角色的关系

```text
角色 A：huawei_ppt_master
负责生成大纲、逐页文案、页面设计说明、deck_spec.json，并提供 deck_spec 字段说明。

角色 B：huawei_ppt_skill_optimizer
负责评审、回归测试、Skill 优化建议。

角色 C：huawei_pptx_builder
负责基于已确认内容和 deck_spec 生成正式 PPTX。C 需要将 deck_spec 语义合同转换为自身可执行的页面结构。

角色 D：huawei_ppt_qa_reviewer，可选
负责独立验收大纲、文案、版式和 PPTX。
```
