# huawei_ppt_master v0.3.5 生成图片反馈沉淀报告

## 1. 背景

用户确认允许将 `project/PPT_image/AI4MBSE_自动化生产系统` 与 `tmp/PPTTemplate/0517` 对标后的通用规则沉淀到 `skills/huawei_ppt_master/*`。

本次沉淀遵循：只沉淀跨主题复用的视觉语义、页面角色、图表失败条件与评估门禁；不沉淀 AI4MBSE 主题事实、论文术语、客户/产品/案例名或未经核验数字。

## 2. 已修改资产

1. `SKILL.md`
   - 版本升级为 `0.3.5-generated-image-feedback`。

2. `templates/visual_rules.md`
   - 新增正文页红色底座控制规则；
   - 新增多卡片主次层级规则。

3. `visual_patterns/layout_library.md`
   - 新增阅读框架页语义约束；
   - 新增案例证明页语义约束；
   - 新增决策建议页语义约束；
   - 新增路线图阶段门槛规则；
   - 新增总结页最终定义规则。

4. `templates/chart_patterns.md`
   - 新增 `case_gallery_cards` 失败条件；
   - 新增 `decision_table` 失败条件；
   - 新增 `capability_map` 失败条件；
   - 新增 `layered_stack_diagram` 失败条件；
   - 新增 `roadmap_timeline_chart` 失败条件。

5. `templates/wording_rules.md`
   - 新增长标题压缩规则；
   - 新增总结页最终定义规则。

6. `eval/visual_scorecard.md`
   - 新增生成图片反馈一票降级项。

7. `README.md`、`INDEX.md`、`PACKAGE_MANIFEST.md`、`VERSION.md`、`CHANGELOG.md`
   - 同步版本、索引、包清单与变更记录。

## 3. 自检结果

- 未新增非法 `chart_type` 或 `layout_pattern` 枚举；
- 未修改默认交付链路；
- 未写入具体主题事实、案例名或未经核验数字；
- 未引入 AI 算力/昇腾/NVIDIA 等无关主题默认污染；
- 新增规则均为跨主题通用视觉/结构/表达/验收规则；
- 与 v0.3.4 视觉语义规则兼容，为增量增强。

## 4. 建议后续回归

下一次生成 PPT 图片后，重点用 `eval/visual_scorecard.md` 检查：

1. 正文页红色底座是否过重；
2. 多卡片页是否有主次层级；
3. 案例页是否退化为素材墙；
4. 决策页是否表格吞没拍板事项；
5. 路线图是否具备阶段门槛和验收产出；
6. 总结页是否形成最终定义或新增管理含义。
