# improvement_backlog

## SWE Atlas 视觉资产迭代 backlog v1.1

| backlog_id | 对应 issue_id | 改进项 | 优先级 | 类型 | 建议落点 | 验收标准 |
|---|---|---|---|---|---|---|
| BL-VIS-001 | VIS-SWE-001 | 增加红色锚点预算与红色面积约束 | P1 | visual_rule | `skills/huawei_ppt_master/templates/visual_rules.md` | 单页主红色锚点不超过 1-2 个；正文页红色面积约 5%-10% |
| BL-VIS-002 | VIS-SWE-002 | 增加底部结论条使用条件与高度规则 | P1 | visual_rule | `visual_rules.md` / Builder 规则 | 普通页不再使用厚重压底红条 |
| BL-VIS-003 | VIS-SWE-003 | 补充 layout 区域比例与右侧洞察栏宽度 | P1 | layout_pattern | `visual_patterns/layout_library.md` | 标题区/主体区/页脚区比例稳定；右侧洞察栏 25%-32% |
| BL-VIS-004 | VIS-SWE-004 | 建立卡片强/中/弱三级视觉样式 | P1 | chart_pattern | `templates/chart_patterns.md` | P1/P4 卡片主次清晰，边框和内边距统一 |
| BL-VIS-005 | VIS-SWE-005 | 固化页脚安全区和来源/页码/保密信息样式 | P2 | visual_rule | `visual_rules.md` | 页脚位置、字号、颜色、基线一致 |
| BL-VIS-006 | VIS-SWE-006 | 固化证据页、问题页、行动页三类母版节奏 | P1 | layout_pattern | `layout_library.md` + 页型资产 | SWE Atlas P1-P5 页面节奏更统一 |
| BL-VIS-007 | VIS-SWE-007 | 增加“表格证据区 + 指标结论卡”模式 | P1 | page_pattern | `visual_patterns/comparison_page_patterns.md` | P3 表格变轻，右侧指标卡承担结论 |
| BL-VIS-008 | VIS-SWE-008 | 增加泳道/闭环图组件语法 | P1 | chart_pattern | `chart_patterns.md` + `architecture_page_patterns.md` | P2/P5 节点、箭头、连接线统一 |
| BL-VIS-009 | VIS-SWE-009 | 扩展 visual_scorecard，增加视觉降噪评分项 | P1 | qa_gate | `eval/visual_scorecard.md` | 可识别红色过量、底部条过重、卡片层级缺失 |
| BL-VIS-010 | VIS-SWE-010 | 扩展 page_design prompt，强制输出视觉降噪约束 | P1 | output_contract | `prompts/generate_page_design.md` | 每页设计说明含 red_anchor/card_hierarchy/spacing_rule/bottom_bar_rule |

## 迭代分批建议

### Batch 1：基础视觉约束

- BL-VIS-001
- BL-VIS-002
- BL-VIS-003
- BL-VIS-004
- BL-VIS-009
- BL-VIS-010

### Batch 2：页型专项增强

- BL-VIS-006
- BL-VIS-007
- BL-VIS-008
- BL-VIS-005

## 当前建议

先由人工确认 `patch_proposal_v1.1_visual_assets.md`，确认后再允许直接修改 `skills/huawei_ppt_master/*`。
