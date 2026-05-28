# Package Manifest

Current package version: v0.3.8-deck-spec-field-dictionary
Last updated: 2026-05-28

- `CHANGELOG.md`
- `README.md`
- `SKILL.md`
- `UPGRADE_FILE_LIST_v0.2.md`
- `VERSION.md`
- `core/anti_overfit_rules.md`
- `core/audience_rules.md`
- `core/deck_spec_field_dictionary.md`
- `core/generation_workflow.md`
- `core/output_contracts.md`
- `core/reference_ingestion_workflow.md`
- `core/reference_material_policy.md`
- `core/topic_router.md`
- `domain_profiles/ai_compute_ascend_nvidia.md`
- `domain_profiles/ai_platform.md`
- `domain_profiles/customer_solution.md`
- `domain_profiles/cybersecurity.md`
- `domain_profiles/data_governance.md`
- `domain_profiles/default_general.md`
- `domain_profiles/gov_public_security.md`
- `domain_profiles/project_operation.md`
- `eval/acceptance_checklist.md`
- `eval/domain_contamination_tests.md`
- `eval/reference_learning_regression.md`
- `eval/regression_cases.md`
- `eval/visual_scorecard.md`
- `prompts/deck_spec_generation.md`
- `prompts/generate_outline.md`
- `prompts/generate_page_copy.md`
- `prompts/generate_page_design.md`
- `prompts/screenshot_analysis.md`
- `prompts/self_review.md`
- `methodology_patterns/executive_argument_patterns.md`
- `methodology_patterns/industry_framework_extraction_rules.md`
- `methodology_patterns/page_role_patterns.md`
- `methodology_patterns/section_logic_patterns.md`
- `templates/chart_patterns.md`
- `templates/huawei_style_reference.md`
- `templates/narrative_patterns.md`
- `templates/page_types.md`
- `templates/visual_rules.md`
- `templates/wording_rules.md`
- `visual_patterns/architecture_page_patterns.md`
- `visual_patterns/comparison_page_patterns.md`
- `visual_patterns/executive_summary_patterns.md`
- `visual_patterns/layout_library.md`
- `visual_patterns/risk_decision_patterns.md`
- `visual_patterns/roadmap_page_patterns.md`
- `visual_patterns/screenshot_layout_analysis.md`
- `visual_patterns/solution_showcase_patterns.md`


---

## 3. 文件职责说明

### 3.1 `core/`：通用执行内核，任何任务都必须优先读取

- `core/generation_workflow.md`  
  定义从主题识别、章节规划、大纲生成、逐页文案、页面设计、deck_spec 到自检的完整流程。

- `core/topic_router.md`  
  判断用户主题类型，并决定是否加载 `domain_profiles/` 下的主题包。

- `core/output_contracts.md`  
  定义大纲、逐页文案、页面设计说明、deck_spec.json 的标准输出格式。

- `core/anti_overfit_rules.md`  
  防止昇腾/NVIDIA/AI算力等主题内容污染其他主题。该文件为强约束文件。

- `core/audience_rules.md`  
  根据汇报对象调整口径，包括华为内部高层、客户高层、市局/分局领导、技术团队等。

- `core/deck_spec_field_dictionary.md`  
  定义 `deck_spec.json` 的文件定位、顶层字段和 slide 字段职责，作为角色 C 理解 deck_spec 的正式交付物支持文档。

- `core/reference_ingestion_workflow.md`  
  定义持续提供 PPT、PPT 图片、模板、文本材料和数据材料时的分类、抽取、沉淀、冲突处理和复用流程。

- `core/reference_material_policy.md`  
  定义不同参考材料的证据等级与使用边界，避免把视觉参考误当事实依据。

### 3.2 `templates/`：通用华为风格模板库，所有主题均可使用

- `templates/page_types.md`  
  定义封面、目录、总览、对比、架构、路线图、风险、决策、Thank you 等页型。

- `templates/narrative_patterns.md`  
  定义高层汇报、客户汇报、技术方案、项目复盘、竞品对比等叙事结构。

- `templates/visual_rules.md`  
  定义华为风格配色、字体、页脚、留白、图表视觉规则。

- `templates/chart_patterns.md`  
  定义矩阵、架构图、路线图、风险表、决策表、生态图、能力地图等图表模式。

- `templates/wording_rules.md`  
  定义通用华为式文案表达，禁止空泛口号，不包含具体行业事实。

- `templates/huawei_style_reference.md`  
  记录用户提供的华为模板风格要点，包括白底、红黑灰、Huawei Confidential、正式页脚等。

### 3.3 `domain_profiles/`：主题知识包，必须由 topic_router 条件触发

- `domain_profiles/default_general.md`  
  默认主题包。任何无法明确归类的主题都使用该包。

- `domain_profiles/ai_compute_ascend_nvidia.md`  
  仅当用户主题明确涉及昇腾、英伟达、NVIDIA、AI算力、GPU/NPU、算力调度、模型适配、CUDA、CANN、MindSpore 等内容时允许读取。

- `domain_profiles/gov_public_security.md`  
  仅当用户主题明确涉及公安、政务、市局、分局、区县、安平、视频解析、警情研判等内容时允许读取。

- `domain_profiles/ai_platform.md`  
  仅当用户主题明确涉及 AI 平台、模型平台、应用平台、模型服务、MLOps 等内容时允许读取。

- `domain_profiles/project_operation.md`  
  仅当用户主题明确涉及持续运营、项目运营、运维治理、运营机制、服务保障等内容时允许读取。

- `domain_profiles/customer_solution.md`  
  仅当用户明确要求客户版、客户汇报、解决方案、售前方案时允许读取。

- `domain_profiles/data_governance.md`  
  仅当用户主题明确涉及数据治理、数据资产、数据中台、数据质量、数据目录等内容时允许读取。

- `domain_profiles/cybersecurity.md`  
  仅当用户主题明确涉及网络安全、安全运营、主机安全、攻防、合规、安全测试等内容时允许读取。

### 3.4 `visual_patterns/`：版式库，用于页面设计说明与 PPTX 生成输入

- `visual_patterns/layout_library.md`  
  通用页面布局模式库。

- `visual_patterns/screenshot_layout_analysis.md`  
  基于用户提供版式截图提取的布局规律。

- `visual_patterns/executive_summary_patterns.md`  
  总览页、仪表盘页、四象限判断页模式。

- `visual_patterns/comparison_page_patterns.md`  
  对比页、矩阵页、左右对照页模式。

- `visual_patterns/architecture_page_patterns.md`  
  架构图、分层图、链路图、生态图模式。

- `visual_patterns/roadmap_page_patterns.md`  
  时间轴、三阶段路线图、里程碑图模式。

- `visual_patterns/risk_decision_patterns.md`  
  风险矩阵、决策清单、行动闭环页模式。

### 3.5 `methodology_patterns/`：方法论与内容套路库

- `methodology_patterns/executive_argument_patterns.md`  
  沉淀高层汇报中的“判断—依据—动作—风险—决策”等论证套路。

- `methodology_patterns/section_logic_patterns.md`  
  沉淀战略、方案、对比、复盘、客户方案、资源申请等章节逻辑。

- `methodology_patterns/page_role_patterns.md`  
  沉淀总览页、诊断页、对比页、方案页、路径页、风险页、拍板页等页面角色模式。

- `methodology_patterns/industry_framework_extraction_rules.md`  
  定义如何从持续投喂的行业 PPT / 图片中抽取可复用行业方法论。

### 3.6 `eval/`：验收与回归测试

- `eval/acceptance_checklist.md`  
  通用质量验收清单。

- `eval/visual_scorecard.md`  
  页面设计说明、版式质量、视觉降噪和华为风格一致性评分表。

- `eval/regression_cases.md`  
  Skill 升级后的回归测试题。

- `eval/domain_contamination_tests.md`  
  检查非 AI 算力主题是否被昇腾/NVIDIA/GPU/NPU 等术语污染。

- `eval/reference_learning_regression.md`  
  检查参考材料学习后的视觉、结构、表达、体系、主题隔离和增量稳定性。

### 3.7 `prompts/`：可复用提示词

`prompts/` 仅作为提示词素材库，不得覆盖本 `SKILL.md` 中的强制规则。

### 3.7 v0.3.5 生成图片反馈沉淀资产

本版本同步增强以下资产：

- `templates/visual_rules.md`：正文页红色底座控制、多卡片主次层级。
- `visual_patterns/layout_library.md`：阅读框架页、案例证明页、决策建议页、路线图页、总结页语义约束。
- `templates/chart_patterns.md`：案例图卡、决策表、能力地图、分层堆栈、路线图时间轴失败条件。
- `templates/wording_rules.md`：长标题压缩、总结页最终定义。
- `eval/visual_scorecard.md`：生成图片反馈一票降级项。

### 3.8 v0.3.6 视觉规则重构资产

本版本同步增强以下资产：

- `templates/visual_rules.md`：以 `visual_rules_v0.2.md` 为主干重构为专职视觉设计指导资产，并保留历史沉淀兼容说明。
- `prompts/generate_page_design.md`：新增 `visual_boundary` 与 `page_type_gate` 输出要求。
- `core/output_contracts.md`：同步页面设计说明输出契约。
- `core/generation_workflow.md`：同步页面设计生成流程字段。
- `eval/visual_scorecard.md`：新增 v0.3.6 视觉风格边界扣分/降级项。
- `README.md`、`INDEX.md`、`VERSION.md`、`CHANGELOG.md`：同步版本与资产说明。


### 3.9 v0.3.7 deck_spec 证明契约资产

本版本同步增强以下资产：

- `core/output_contracts.md`：deck_spec 每页新增 `core_judgement`、`chart_proof_goal`、`chart_visual_boundary` 字段。
- `prompts/deck_spec_generation.md`：要求先生成唯一核心判断和图表证明目标，再选择 `chart_type` / `layout_pattern`。
- `core/generation_workflow.md`：同步 Step 6.5 字段映射检查顺序。
- `templates/chart_patterns.md`：新增各类 `chart_type` 的 proof_goal 示例与 visual_boundary 边界。
- `eval/visual_scorecard.md`：新增 v0.3.7 deck_spec 证明契约检查与一票降级项。
- `eval/acceptance_checklist.md`：新增 deck_spec 证明契约验收项。

### 3.10 v0.3.8 deck_spec 字段字典资产

本版本新增以下正式交付物支持资产：

- `core/deck_spec_field_dictionary.md`：说明 `deck_spec.json` 的文件定位、顶层字段和 slide 字段，明确其是页面语义合同，不是 PPTX 或 shape 指令。

边界：本版本不继续推进 `page_render_spec` / `normalized_render_model` 方案，不新增渲染 DSL，不改变默认生成链路。
