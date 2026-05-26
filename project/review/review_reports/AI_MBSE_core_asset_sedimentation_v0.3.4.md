# AI_MBSE 页面图片评审核心规则沉淀报告 v0.3.4

## 1. 背景

基于 `project/review/review_reports/AI_MBSE_P1-P7_page_image_review_v0.1.md`，将跨主题、可复用、非 AI_MBSE 专属的核心优化规则沉淀到 `huawei_ppt_master` Skill 资产。

## 2. 沉淀原则

- 只沉淀通用视觉/版式/图表/文案/评估规则；
- 不沉淀 AI_MBSE 论文专属事实、案例和术语；
- 不改变默认交付链路；
- 不新增非法 `chart_type` / `layout_pattern` 枚举；
- 优先解决“结构正确但图表没有讲透结论”的问题。

## 3. 已修改文件

1. `skills/huawei_ppt_master/SKILL.md`
   - 版本升级为 `0.3.4-visual-semantics`。

2. `skills/huawei_ppt_master/templates/visual_rules.md`
   - 新增红色锚点注意力判定；
   - 新增工程化卡片层级；
   - 新增底部结论条增量规则。

3. `skills/huawei_ppt_master/visual_patterns/layout_library.md`
   - 新增四象限坐标有效性；
   - 新增右侧洞察栏主图关系约束；
   - 新增三栏并列/链路判断；
   - 新增两列对比表格转面板规则。

4. `skills/huawei_ppt_master/templates/chart_patterns.md`
   - 新增 `quadrant_matrix` 失败条件；
   - 新增 `architecture_flow_diagram` 因果链要求；
   - 新增 `gap_heatmap` 使用边界；
   - 新增图表服务结论检查。

5. `skills/huawei_ppt_master/templates/wording_rules.md`
   - 新增强判断标题支撑规则；
   - 新增抽象概念定义规则。

6. `skills/huawei_ppt_master/eval/visual_scorecard.md`
   - 新增图表论证力加严项；
   - 新增图表语义一票降级项。

7. `skills/huawei_ppt_master/CHANGELOG.md`
   - 新增 `v0.3.4-visual-semantics` 变更记录。

## 4. 预期收益

- 降低红色锚点分散问题；
- 减少咨询模板感和卡片堆叠；
- 防止装饰性四象限、弱流程图、伪 heatmap；
- 强化标题、图表、底部结论之间的论证闭环；
- 提升后续 PPT 图片生成的一致性和返工效率。

## 5. 自检结论

- 未写入 AI_MBSE 专属事实；
- 未新增 chart_type/layout_pattern 枚举；
- 仅增强通用规则和评估门禁；
- 与 v0.3.3 默认交付链路兼容。

更新时间：2026-05-24T23:49:30
