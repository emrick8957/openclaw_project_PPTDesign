# Skill 优化评审报告

## 1. 基本信息
- 任务名称: `huawei_ppt_master` 参考材料学习能力升级
- 评审角色: B / `huawei_ppt_skill_optimizer`
- 评审对象: `skills/huawei_ppt_master/` 中与参考材料学习相关的规则层设计
- 评审目标: 判断当前 Skill 是否具备“持续喂 PPT / PPT 图片后，自动沉淀并稳定复用”的能力基础，以及应如何升级

## 2. 被评审对象
### 已读取文件
1. `skills/huawei_ppt_master/SKILL.md`
2. `skills/huawei_ppt_master/core/generation_workflow.md`
3. `skills/huawei_ppt_master/core/anti_overfit_rules.md`
4. `skills/huawei_ppt_master/prompts/screenshot_analysis.md`
5. `skills/huawei_ppt_master/templates/huawei_style_reference.md`
6. `skills/huawei_ppt_master/templates/visual_rules.md`
7. `skills/huawei_ppt_master/visual_patterns/screenshot_layout_analysis.md`

### 当前观察
- 已存在“从用户提供模板/截图提炼视觉规则与版式模式”的能力雏形。
- 已有历史沉淀证据，说明这部分不是空白能力。
- 但整体仍偏“视觉抽取”，尚未形成完整的“持续输入 → 双通道抽取 → 分层沉淀 → 回归复用”闭环。

## 3. 总体结论
**当前能力可作为基础，但距离你的目标还有一段明显差距。**

更准确地说：
- 现在已经能学: 样子、结构、表达习惯的一部分；
- 现在还不够能学: 体系、内容套路、行业框架、稳定增量沉淀；
- 最关键缺口不是素材不够，而是规则架构还没把“学习”定义成一级流程。

## 4. 问题清单
详见 `project/review/issue_log.md`，本次核心问题共 7 项：
- P0: 5 项
- P1: 2 项

其中最关键的 3 个是：
1. 缺少统一的参考材料学习框架；
2. 缺少内容/方法论抽取承载层；
3. 缺少增量学习冲突控制与专项回归。

## 5. 问题归因
- `skill_rule_missing`: 2 项
- `output_contract_gap`: 2 项
- `domain_profile_issue`: 2 项
- `qa_gate_gap`: 1 项

## 6. improvement_backlog
详见 `project/review/improvement_backlog.md`。

优先级建议：
1. 先做 HPPT-201 / HPPT-203 / HPPT-204；
2. 再做 HPPT-202；
3. 最后补 HPPT-205。

## 7. patch proposal 摘要
详见 `project/review/patch_proposals/patch_proposal_v0.6.md`。

本次建议不是小修小补，而是增加一层“参考材料学习框架”，核心新增包括：
- `core/reference_ingestion_workflow.md`
- `core/reference_material_policy.md`
- `methodology_patterns/`
- `eval/reference_learning_regression.md`

## 8. 回归测试建议
详见 `project/review/regression_plan.md`。

必须重点盯住：
1. 学完后是否只是更像截图表面；
2. 是否真的学到了章节逻辑与论证套路；
3. 是否因持续喂料造成主题污染或过拟合。

## 9. 合入判断
**有条件合入。**

条件是：
1. 不把“自动沉淀”做成无门槛自动写规则；
2. 先补分层管理和冲突判定；
3. 先有回归，再放大学习能力。

## 10. B_to_A 交接摘要
这次最值得改的不是某一句提示词，而是 Skill 的学习架构。当前它已经有视觉学习基础，但还缺内容方法论学习、增量沉淀分层与专项回归。建议按 patch v0.6 分阶段升级，先把参考材料学习流程立起来，再逐步增强主题知识沉淀。