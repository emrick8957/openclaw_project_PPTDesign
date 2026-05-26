# huawei_ppt_master v0.3.6 视觉规则重构落地报告

## 1. 背景

用户提供 `visual_rules_v0.2.md` 并确认启动落地。此次按“重构合并，不直接丢弃历史沉淀”的方式，将新视觉规则作为 `templates/visual_rules.md` 主干，同时保留 0517 多行业模板、v0.3.3 视觉一致性、v0.3.4 视觉语义、v0.3.5 生成图片反馈规则的兼容说明。

## 2. 已修改资产

1. `SKILL.md`
   - 版本升级为 `0.3.6-visual-rules-refactor`。

2. `templates/visual_rules.md`
   - 以 `visual_rules_v0.2.md` 为主干重构；
   - 明确职责边界：只负责视觉设计指导；
   - 新增完整视觉规则体系：色彩、区域、字体、红色锚点、卡片、图标线条、图表视觉语义、右侧洞察栏、底部结论条、图片素材、特殊页型门禁、负面视觉风格、视觉自检清单、优化优先级、默认推荐样式；
   - 追加历史沉淀兼容说明。

3. `prompts/generate_page_design.md`
   - 新增 `visual_boundary` 字段；
   - 新增 `page_type_gate` 字段；
   - 强化 visual_rules 职责边界，不让视觉规则改写事实或替代 deck_spec。

4. `core/output_contracts.md`
   - 同步页面设计说明输出契约，增加 `visual_boundary` 和 `page_type_gate`。

5. `core/generation_workflow.md`
   - 同步页面设计生成流程字段。

6. `eval/visual_scorecard.md`
   - 新增 v0.3.6 视觉风格边界扣分/降级项；
   - 增加视觉优化优先级。

7. `README.md`、`INDEX.md`、`PACKAGE_MANIFEST.md`、`VERSION.md`、`CHANGELOG.md`
   - 同步版本和资产说明。

## 3. 自检结果

- 未改变 deck_spec 字段枚举；
- 未改变默认完整交付链路；
- 未把视觉规则扩展为事实校验或文案改写；
- 保留了 0517 与 v0.3.5 的关键可复用边界；
- 页面设计字段已同步到 prompt、workflow、output_contracts；
- 视觉评分资产已同步新增负面风格边界。

## 4. 后续使用建议

后续生成页面设计说明时，每页除原有 `red_anchor`、`card_hierarchy`、`spacing_rule`、`bottom_bar_rule`、`visual_simplification` 外，应补充：

- `visual_boundary`：本页需避免的负面视觉风格；
- `page_type_gate`：本页页型门禁，例如案例页不做图片墙、决策页拍板事项独立突出、路线图必须有阶段门槛、总结页必须形成最终定义。

生成页面图片后，视觉自检应同时读取 `templates/visual_rules.md` 与 `eval/visual_scorecard.md`，避免规则和评分职责混用。
