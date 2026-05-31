# 自检报告 v0.1

## 1. 内容质量
- PASS：已按 Background / Catalyst / Application / Trends 四段式组织，共 14 页，包含总览、背景、机制、应用、趋势与决策建议。
- PASS：每页标题均为结论型标题，未使用“建设背景/总体架构”等名词式标题。
- PASS：每页均有核心判断、图表建议、页面设计说明和高层回答问题。

## 2. deck_spec 合法性
- PASS：`chart_type` 均来自 `templates/chart_patterns.md`：none、key_findings_cards、comparison_table、architecture_flow_diagram、layered_stack_diagram、value_chain_loop、capability_map、swimlane_process、trend_curve、decision_table。
- PASS：`layout_pattern` 均来自 `visual_patterns/layout_library.md`：image_background_section_divider、executive_summary_dashboard、multi_module_solution_overview、two_column_comparison、stack_architecture_with_right_insights、layered_architecture、ecosystem_map、insight_panel_with_chart、roadmap_timeline、left_logic_right_proof、trend_curve_with_strategy、risk_decision_matrix。
- PASS：无 `chart_type == layout_pattern`，无自造枚举。
- PASS：每页包含 `core_judgement`、`chart_proof_goal`、`chart_visual_boundary`、`chart_semantic_mapping`。

## 3. 模板印章检测
| 检查项 | 结果 | 证据 | 处理建议 |
|---|---|---|---|
| 重复字段统计 | PASS | N=14，repeat_threshold=max(3,ceil(14*0.5))=7；关键字段未出现 7 页及以上相同 | 保留 global_design_defaults，逐页 overrides 已差异化 |
| 复述检测 | PASS | `core_judgement` 对 `conclusion` 做管理化转译，未逐字相等 | 后续 PPTX 生成仍需保留差异 |
| 骨架填词检测 | PASS | `chart_proof_goal` 分别说明对比、流转、层级、闭环、趋势、决策关系 | 无需返工 |
| 设计增量检测 | PASS | 每页 chart_type/layout_pattern/视觉边界/讲解口径按页面角色变化 | 无需返工 |
| 允许重复项 | PASS | 页脚、配色、安全区已下沉为全局默认 | 下游 Builder 可复用 |

## 4. chart_data 字段可见性
- PASS：未在 `chart_data` 中使用 `relation_type`、`edge_style`、`position`、`anchor`、`x/y`、`layer_index` 等 DSL 字段。
- PASS：`edges.label` 均为短动作词：验证、交付、回收、协同、生成、训练、解释、封装、输出、引用、赋义、关联、沉淀、映射等。
- PASS：复杂流转、闭环与阶段语义进入 `chart_semantic_mapping`。

## 5. 主题污染与事实边界
- PASS：主题为 AI in MBSE，不是 AI 算力主题；未引入昇腾、NVIDIA、CUDA、CANN、GPU/NPU、模型迁移等无关专属内容。
- PASS：未编造论文外部数字、市场份额或企业案例。
- WARN：若用于组织正式立项，需要补充内部系统边界、样板场景、责任人和验收指标。

## 6. 视觉评分预估
- 页面结构：23/25；华为风格：23/25；图表可执行性：19/20；高层阅读效率：18/20；风险项：9/10；合计约 92/100。
- 无一票降级项：未设计大面积红底、图片墙、Excel 满表、咨询海报风或学术论文截图风。
