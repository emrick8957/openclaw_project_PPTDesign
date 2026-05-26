# CHANGELOG

## v0.3.7-deck-spec-proof-contract

### 升级目标

将 deck_spec 从“描述页面内容与图表类型”升级为“明确本页唯一判断、图表证明目标和图表视觉边界”的证明契约，解决 chart_type 合法但图表论证无力的问题。

### 新增

1. `core/output_contracts.md`：deck_spec 每页新增 `core_judgement`、`chart_proof_goal`、`chart_visual_boundary` 字段与检查规则。
2. `prompts/deck_spec_generation.md`：要求先生成 `core_judgement`，再生成 `chart_proof_goal`，最后选择 `chart_type` / `layout_pattern`。
3. `core/generation_workflow.md`：同步 Step 6.5 deck_spec 字段映射检查顺序。
4. `templates/chart_patterns.md`：新增 deck_spec 图表证明契约，给出常见 chart_type 的 proof_goal 示例与 visual_boundary 示例。
5. `eval/visual_scorecard.md`：新增 v0.3.7 deck_spec 证明契约检查与一票降级项。
6. `eval/acceptance_checklist.md`：新增 deck_spec 证明契约验收项。

### 修改

1. `SKILL.md` 版本升级为 `0.3.7-deck-spec-proof-contract`。
2. `README.md`、`INDEX.md`、`PACKAGE_MANIFEST.md`、`VERSION.md` 同步版本与资产说明。

### 兼容性

v0.3.7 不新增 chart_type 或 layout_pattern 枚举，不改变默认交付链路；仅新增 deck_spec 证明字段和图表论证门禁。

## v0.3.6-visual-rules-refactor

### 升级目标

基于用户提供的 `visual_rules_v0.2.md`，将 `templates/visual_rules.md` 从增量规则堆叠重构为“专职视觉设计指导资产”，明确职责边界，并保留 0517 多行业模板、v0.3.3 视觉一致性、v0.3.4 视觉语义、v0.3.5 生成图片反馈规则的历史沉淀。

### 新增

1. `templates/visual_rules.md` 新增明确职责边界：只管视觉风格、色彩、版式、字体、间距、卡片、图表形态、红色锚点、页脚、安全区和负面视觉禁止项；不承担事实校验、deck_spec 字段解释、生成流程控制、评分规则、证据溯源、文案改写。
2. `templates/visual_rules.md` 新增完整视觉规则主干：总体视觉定位、色彩角色、页面区域、字体层级、红色纠偏、卡片模块、图标线条、图表视觉语义、右侧洞察栏、底部结论条、图片素材、特殊页型门禁、负面视觉风格总表、视觉自检清单、优化优先级和默认推荐样式。
3. `templates/visual_rules.md` 新增历史沉淀兼容说明，保留 0517 与 v0.3.5 核心边界。
4. `prompts/generate_page_design.md` 新增 `visual_boundary` 与 `page_type_gate` 字段要求。
5. `core/output_contracts.md`、`core/generation_workflow.md` 同步页面设计说明输出字段。
6. `eval/visual_scorecard.md` 新增 v0.3.6 视觉风格边界扣分/降级项。

### 修改

1. `SKILL.md` 版本升级为 `0.3.6-visual-rules-refactor`。
2. `README.md`、`INDEX.md`、`PACKAGE_MANIFEST.md`、`VERSION.md` 同步版本与资产说明。

### 兼容性

v0.3.6 不改变 deck_spec 字段枚举、不改变默认交付链路、不改写事实与文案规则；仅强化视觉资产边界、页面设计字段和视觉自检门禁。

## v0.3.5-generated-image-feedback

### 升级目标

基于生成 PPT 图片 `project/PPT_image/AI4MBSE_自动化生产系统` 与华为模板 `tmp/PPTTemplate/0517` 的对标结果，沉淀“生成图片反馈 → Skill 资产迭代”的通用规则，解决正文页红色底座过重、卡片平均主义、框架/案例/决策页论证力不足等问题。

### 新增

1. `templates/visual_rules.md` 新增正文页红色底座控制规则、多卡片主次层级规则。
2. `visual_patterns/layout_library.md` 新增阅读框架页、案例证明页、决策建议页、路线图阶段门槛、总结页最终定义等页面角色语义约束。
3. `templates/chart_patterns.md` 新增 `case_gallery_cards`、`decision_table`、`capability_map`、`layered_stack_diagram`、`roadmap_timeline_chart` 的失败条件与降级建议。
4. `templates/wording_rules.md` 新增长标题压缩规则、总结页最终定义规则。
5. `eval/visual_scorecard.md` 新增生成图片反馈一票降级项。

### 修改

1. `SKILL.md` 版本升级为 `0.3.5-generated-image-feedback`。
2. `README.md`、`INDEX.md`、`PACKAGE_MANIFEST.md`、`VERSION.md` 同步版本与资产说明。

### 边界

不沉淀 AI4MBSE 主题事实、论文术语、客户/产品/案例名、未经核验数字；仅沉淀跨主题复用的视觉语义、页面角色、图表失败条件与评估门禁。

## v0.3.4-visual-semantics

### 升级目标

基于 AI_MBSE P1-P7 页面图片评审，将“页面结构正确但图表没有讲透结论”的共性问题沉淀为核心可复用规则，强化红色锚点语义、卡片工程化层级、版式语义有效性、图表论证力和强判断标题支撑。

### 新增

1. `templates/visual_rules.md` 新增页面图片生成后的红色锚点判定、工程化卡片层级、底部结论条增量规则。
2. `visual_patterns/layout_library.md` 新增关键版式语义约束：四象限坐标有效性、右侧洞察栏约束、三栏并列/链路判断、两列对比表格转面板规则。
3. `templates/chart_patterns.md` 新增图表语义失败条件与降级规则，覆盖 `quadrant_matrix`、`architecture_flow_diagram`、`gap_heatmap`。
4. `templates/wording_rules.md` 新增强判断标题支撑规则与抽象概念定义规则。
5. `eval/visual_scorecard.md` 新增图表论证力加严项与图表语义一票降级项。

### 兼容性

v0.3.4 不改变默认交付链路和 deck_spec 字段，仅增强页面图片/PPTX 生成后的视觉语义与论证质量门禁。

## v0.3.3-visual-consistency

### 升级目标

根据 SWE Atlas 页面图片与华为风格 PPT 模板对比结果，补齐视觉资产之间的一致性规则，解决“结构正确但视觉偏重”的问题。

### 新增

1. `templates/visual_rules.md` 增加华为式视觉降噪规则：红色锚点预算、底部结论条克制、卡片层级、留白安全区、页脚一致性。
2. `visual_patterns/layout_library.md` 增加 layout 通用区域比例、右侧洞察栏宽度、底部结论条使用条件和禁用组合。
3. `templates/chart_patterns.md` 增加 `key_findings_cards`、`comparison_table`、`swimlane_process`、`value_chain_loop` 的组件级视觉约束。
4. `eval/visual_scorecard.md` 增加视觉降噪与华为风格一致性评分项和一票降级项。
5. `prompts/generate_page_design.md` 增加 `red_anchor`、`card_hierarchy`、`spacing_rule`、`bottom_bar_rule`、`visual_simplification` 输出要求。
6. `eval/regression_cases.md` 增加 SWE Atlas 页面图片视觉一致性回归用例。

### 修改

1. `SKILL.md` 升级到 v0.3.3，并增加视觉一致性硬规则。
2. `core/output_contracts.md` 与 `core/generation_workflow.md` 同步页面设计视觉降噪字段，保证输出契约与生成流程一致。
3. `visual_patterns/executive_summary_patterns.md`、`architecture_page_patterns.md`、`comparison_page_patterns.md`、`risk_decision_patterns.md` 同步增加 SWE Atlas 类页面优化模式。
4. `eval/acceptance_checklist.md`、`README.md`、`QUICK_INDEX.md`、`INDEX.md`、`PACKAGE_MANIFEST.md`、`VERSION.md` 同步更新，保证系统资产一致性。

### 兼容性

v0.3.3 不改变内容生成链路与交付物类型，只增强页面设计说明、deck_spec/Builder 输入和生成图片的视觉一致性约束。

## v0.3.2-consistency-fix

### 修复目标

修复剩余的 deck_spec 输出触发条件歧义、生成流程优先级表述不完整，以及 default_general 默认结构易被误读的问题。

### 修复

1. 调整 `core/output_contracts.md`，明确默认全套交付链路下也应输出 `deck_spec.json`。
2. 调整 `core/generation_workflow.md`，明确用户当前明确偏好优先于沉淀规则复用。
3. 调整 `domain_profiles/default_general.md`，明确默认结构块不等于固定页数，实际页数遵循 `SKILL.md`。

### 兼容性

v0.3.2 不改变 Skill 的核心能力与交付物类型，仅消除剩余规则歧义并增强执行一致性。

## v0.3.1-conflict-fix

### 修复目标

修复当前 Skill 包内已识别的优先级冲突、任务路由歧义与交付规则不一致问题，并同步放宽角色 A 的工作区写权限边界。

### 修复

1. 调整 `core/reference_ingestion_workflow.md` 的复用优先级，确保“用户当前明确指定偏好”高于已沉淀规则。
2. 调整 `SKILL.md` 的默认说明，明确用户未限制交付范围时默认走全套交付链路。
3. 调整 `SKILL.md` 页面设计默认要求，移除“备选版式”要求，仅保留主版式。
4. 调整 `core/topic_router.md` 与 `domain_profiles/project_operation.md`，移除 `project_operation` 对“项目复盘”的误吸收，避免与 `project_review` 任务类型冲突。

### 兼容性

v0.3.1 保持 v0.3 的参考材料学习能力与全套交付能力，仅修复规则冲突，不改变核心产物类型。

## v0.3.0-reference-learning

### 升级目标

把 `huawei_ppt_master` 从“参考材料辅助生成”升级为“参考材料学习框架”：不仅学习样式、结构、表达习惯，也学习体系、内容套路、论证框架，并通过分层沉淀和专项回归稳定复用。

### 新增

1. 新增 `core/reference_ingestion_workflow.md`，定义 PPT、PPT 图片、模板、文本材料、数据材料的接入、分类、双通道抽取、沉淀落位与冲突处理流程。
2. 新增 `core/reference_material_policy.md`，区分风格参考、结构参考、论证参考与事实依据，防止把截图或样张直接当成事实来源。
3. 新增 `methodology_patterns/`，承载高层论证套路、章节逻辑、页面角色和行业框架抽取规则。
4. 新增 `eval/reference_learning_regression.md`，覆盖视觉学习、结构学习、表达学习、体系学习、主题隔离和增量稳定性回归。

### 修改

1. 修改 `SKILL.md`：新增“参考材料学习与复用”能力定义、触发读取规则和学习自检门禁。
2. 修改 `core/generation_workflow.md`：新增 Step 1.5 参考材料识别与分类，以及 Step 3.5 沉淀结果复用。
3. 修改 `prompts/screenshot_analysis.md`：从只抽取版式扩展为同时抽取页面角色、标题句式、论证结构和页面收口方式。
4. 修改 `core/anti_overfit_rules.md`：新增参考材料学习过拟合控制。
5. 修改 `core/topic_router.md`：新增主题知识包升级条件。

### 兼容性

v0.3 保持 v0.2 的通用华为风格生成能力与主题包隔离规则，同时新增参考材料学习流程。若无参考材料输入，原有生成流程仍可正常使用。

## v0.2

### 升级目标

把 v0.1 从“AI算力/昇腾-NVIDIA 强场景 Skill”升级为“通用华为风格 PPT Skill + 条件触发主题知识包 + 版式截图沉淀库”。

### 新增

1. 新增 `core/` 通用生成内核。
2. 新增 `core/topic_router.md`，用于主题识别和主题知识包条件触发。
3. 新增 `core/anti_overfit_rules.md`，用于避免昇腾/NVIDIA 主题污染其他主题。
4. 新增 `domain_profiles/`，将昇腾/NVIDIA、公安政务、AI平台、持续运营等主题知识拆成可选模块。
5. 新增 `visual_patterns/`，将用户提供的版式截图抽象为可复用页面模式。
6. 新增 `eval/domain_contamination_tests.md`，测试非昇腾主题是否被 AI 算力概念污染。
7. 新增 `prompts/generate_page_design.md`，专门生成页面设计说明。
8. 新增 `prompts/deck_spec_generation.md`，用于生成 PPTX Builder 的结构化输入。

### 修改

1. 修改 `SKILL.md`：将 Skill 定位改为通用华为风格 PPT 生成 Skill。
2. 修改 `templates/wording_rules.md`：移除全局昇腾/NVIDIA 专属表达，只保留通用文案规则。
3. 修改 `templates/narrative_patterns.md`：增加通用战略、技术方案、客户方案、项目复盘、运营治理、数据治理、安全运营等叙事模式。
4. 修改 `templates/chart_patterns.md`：将 AI 算力图表从全局默认迁移到主题包中。
5. 修改 `eval/regression_cases.md`：新增非 AI 算力主题测试用例。

### 保留

1. 保留华为红、黑、灰、白的视觉风格。
2. 保留 Huawei Confidential、页码、封面、目录、Thank you 等正式汇报要素。
3. 保留“结论先行、问题导向、工程化表达、克制商务”的基本原则。

### 移动

1. 将 v0.1 中“昇腾 vs 英伟达默认 18 页大纲”移动到 `domain_profiles/ai_compute_ascend_nvidia.md`。
2. 将 v0.1 中“政务公安、算力调度、持续运营”相关表达拆分到独立主题包。

### 兼容性

v0.2 仍支持《昇腾 vs 英伟达：全方位对比与深度洞察》，但该能力由主题包触发，不再污染通用主题。


