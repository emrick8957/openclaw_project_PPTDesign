# issue_log

## 当前评审批次：SWE-ATLAS-VISUAL-ASSET-REVIEW-v1.1

| issue_id | 问题位置 | 问题描述 | 影响 | 问题归因 | 修改建议 | 优先级 | 是否沉淀为 Skill | 是否加入回归测试 |
|---|---|---|---|---|---|---|---|---|
| VIS-SWE-001 | `templates/visual_rules.md` | 缺少单页红色使用预算，SWE Atlas 页面出现红框、红条、红色标签同时抢焦点 | 页面偏重，华为风格克制感不足 | skill_rule_missing | 增加“单页主红色锚点不超过 1-2 个，正文页红色面积 5%-10%”规则 | P1 | 是 | 是 |
| VIS-SWE-002 | `templates/visual_rules.md` / Builder 视觉规则 | 底部红色结论条缺少高度和使用条件约束 | P3/P4/P5 出现压底感，页面视觉重心下沉 | skill_rule_missing | 普通正文页改用窄条或灰底红字，厚红条仅用于强收口页 | P1 | 是 | 是 |
| VIS-SWE-003 | `visual_patterns/layout_library.md` | layout 缺少区域比例、右侧洞察栏宽度、底部条使用条件 | 页面母版节奏不稳 | visual_pattern_gap | 增加标题区/主体区/页脚区比例、右侧洞察栏 25%-32% 规则 | P1 | 是 | 是 |
| VIS-SWE-004 | `chart_patterns.md:key_findings_cards` | 卡片强/中/弱层级缺失 | 三卡/多卡页面同权，主次不清 | visual_pattern_gap | 增加卡片三级样式与同页卡片一致性规则 | P1 | 是 | 是 |
| VIS-SWE-005 | `templates/visual_rules.md` | 页脚安全区和页脚弱化规则不够细 | 页脚正式感和一致性不足 | skill_rule_missing | 固定底部 5% 安全区，来源/页码/保密信息浅灰小字 | P2 | 是 | 是 |
| VIS-SWE-006 | `visual_patterns/layout_library.md` / 页型资产 | SWE Atlas 各页结构正确但母版变化多，像研究稿而非稳定汇报模板 | 降低整套 PPT 的统一性 | visual_pattern_gap | 固化证据页、问题页、行动页三类母版节奏 | P1 | 是 | 是 |
| VIS-SWE-007 | `chart_patterns.md:comparison_table` / `comparison_page_patterns.md` | 表格证据化规则不足，P3 表格偏重 | 数据页阅读压力大 | visual_pattern_gap | 表格弱边框、少高亮，右侧指标卡承担结论 | P1 | 是 | 是 |
| VIS-SWE-008 | `chart_patterns.md:swimlane_process/value_chain_loop` | 泳道/闭环图节点、箭头、连接线规则不足 | P2/P5 图形元素略杂 | visual_pattern_gap | 统一节点尺寸、箭头细线化，红色只标关键节点 | P1 | 是 | 是 |
| VIS-SWE-009 | `eval/visual_scorecard.md` | 现有评分表维度较粗，不能识别红色过量、底部条过重、卡片层级缺失 | 自检容易“结构通过但视觉不够华为” | qa_gate_gap | 增加视觉降噪与华为风格一致性 20 分项 | P1 | 是 | 是 |
| VIS-SWE-010 | `prompts/generate_page_design.md` | 页面设计 prompt 未强制输出红色锚点、卡片层级、留白策略、底部条规则 | Builder 缺少可执行视觉边界 | output_contract_gap | 每页新增 red_anchor/card_hierarchy/spacing_rule/bottom_bar_rule 等字段 | P1 | 是 | 是 |

## 本轮结论

- P0：0
- P1：9
- P2：1
- 当前动作：已输出 patch proposal，不直接修改 Skill
- 建议下一步：人工确认后进入资产迭代
