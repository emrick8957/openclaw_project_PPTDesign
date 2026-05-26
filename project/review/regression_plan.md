# regression_plan

## SWE Atlas 视觉资产迭代回归计划 v1.1

## 1. 回归对象

| 对象 | 路径 |
|---|---|
| 当前 SWE Atlas 图片 | `project/PPT_image/SWE_Atlas_page_images_v0.1/` |
| 华为模板参考 | `tmp/PPTTemplate/0517/` |
| 视觉优化方案 | `project/review/review_reports/swe_atlas_visual_gap_optimization_plan_v0.1.md` |
| patch proposal | `project/review/patch_proposals/patch_proposal_v1.1_visual_assets.md` |

## 2. 回归步骤

1. 合入视觉资产规则后，由角色 A 重新生成 `page_design.md`，要求每页包含：
   - `red_anchor`
   - `card_hierarchy`
   - `spacing_rule`
   - `bottom_bar_rule`
   - `visual_simplification`
2. Builder 基于新 `page_design.md` 与 `deck_spec.json` 重新生成 P1-P5 图片。
3. 对比旧版 `project/PPT_image/SWE_Atlas_page_images_v0.1/` 与新版图片。
4. 使用 `eval/visual_scorecard.md` 新评分项打分。
5. 与 `tmp/PPTTemplate/0517/_analysis/contact_sheets/` 做风格对照。

## 3. 页面级验收标准

| 页面 | 回归重点 | 通过标准 |
|---|---|---|
| P1 | 高层总览、三卡、底部流程 | 左侧压缩为主判断+3要点；三卡统一；底部流程细线化；红色焦点 ≤2 |
| P2 | 三泳道、右侧 Rubric 洞察 | 节点等高等宽；箭头细线；右侧洞察 1 句结论 + 3 条短句 |
| P3 | 对比表、指标卡、底部结论 | 表格弱边框；高亮项 ≤3；右侧指标卡同结构；无厚重压底红条 |
| P4 | 三类失败模式卡片 | 三卡统一但有主次；列表短语化；底部结论条弱化 |
| P5 | 价值闭环、行动建议 | 闭环 4-5 节点；节点为短语；右侧建议 3-4 条；底部条不压页面 |

## 4. 全局验收标准

| 项 | 标准 |
|---|---|
| 红色使用 | 单页主红色锚点不超过 1-2 个；正文页红色面积约 5%-10% |
| 留白 | 标题区、主图区、页脚区有稳定安全距离 |
| 卡片 | 同页卡片圆角、边框、内边距一致；强弱层级明确 |
| 表格 | 弱边框、浅灰线、少高亮；表格承担证据，结论单独呈现 |
| 流程/闭环 | 节点、箭头、连接线统一；红色只标关键节点 |
| 页脚 | 位置、字号、颜色、基线一致 |
| 得分 | visual_scorecard ≥ 85；任一页面低于 80 必须返工 |

## 5. 一票降级项

- 正文页出现厚重红色压底条且非强收口页；
- 同页出现 3 个以上互相抢焦点的红色强调区；
- 表格无独立结论区且文字/数据过密；
- 页脚每页位置或样式明显漂移；
- 闭环图/泳道图节点文本过长，变成文字容器。
