# huawei_ppt_master 迭代建议 v0.1

## 0. 目的

基于 `project/PPT_image/AI4MBSE_自动化生产系统/P1-P14.png` 与 `tmp/PPTTemplate/0517` 华为模板对标结果，提出 `huawei_ppt_master` 的可执行迭代建议。

当前用户未授权直接修改 Skill 资产，因此本文件仅作为 patch proposal，不直接覆盖 `skills/huawei_ppt_master/*`。

## 1. 建议迭代范围

建议修改以下文件：

1. `skills/huawei_ppt_master/templates/visual_rules.md`
2. `skills/huawei_ppt_master/visual_patterns/layout_library.md`
3. `skills/huawei_ppt_master/templates/chart_patterns.md`
4. `skills/huawei_ppt_master/templates/wording_rules.md`
5. `skills/huawei_ppt_master/eval/visual_scorecard.md`
6. 如正式落地，需同步更新：`VERSION`、`CHANGELOG.md`、`README.md`、`INDEX.md`、`PACKAGE_MANIFEST.md`

## 2. 问题到规则映射

| 观察问题 | 典型页 | 建议落位 | 规则级别 |
|---|---|---|---|
| 正文页红色横条成为最大视觉块 | P6 | `visual_rules.md` / `visual_scorecard.md` | 通用级 |
| 多卡片同权、平均主义 | P2/P3/P12 | `visual_rules.md` / `layout_library.md` | 通用级 |
| 框架页主链路不足 | P5/P8/P9 | `layout_library.md` / `chart_patterns.md` | 通用级 |
| 案例页素材墙风险 | P10 | `layout_library.md` / `chart_patterns.md` | 通用级 |
| 决策表吞没结论 | P13 | `layout_library.md` / `chart_patterns.md` | 通用级 |
| 标题偏长、判断不够硬 | 多页 | `wording_rules.md` | 通用级 |
| 总结页缺少最终定义感 | P14 | `wording_rules.md` / `layout_library.md` | 通用级 |

## 3. 建议新增/增强规则

### 3.1 `templates/visual_rules.md`

建议新增小节：`正文页红色底座控制规则`

候选内容：

```markdown
### 正文页红色底座控制规则

- 普通正文页不得让红色横条、红色底座或红色大色块成为页面最大视觉块。
- 若红色块面积超过正文主体视觉权重，应降级为窄红线、浅灰底红色关键词或局部节点强调。
- 大面积红色底座仅适用于封面、章节页、强收口页或关键决策页。
- 能力地图、架构图、路线图中，红色只能标记关键节点、路径门槛或最终结论，不得同时作为背景底座和多个模块强调色。
```

建议新增小节：`多卡片主次层级规则`

```markdown
### 多卡片主次层级规则

- 多卡片页必须标注主卡、支撑卡、注释卡，不允许所有卡片同等权重。
- 主卡最多 1 张，承担全页核心判断；支撑卡 2~4 张，承担依据或抓手；注释卡弱化显示。
- 目录页、核心结论页、路线图页的卡片不得只是平均分布，必须体现阅读顺序、优先级或阶段门槛。
```

### 3.2 `visual_patterns/layout_library.md`

建议增强：

```markdown
### 阅读框架页语义约束

目录/阅读框架页不能只做章节导航，必须回答“高层应如何形成判断”。建议使用“为什么—是什么—怎么落地—如何决策”或“判断—证据—路径—拍板”的递进结构，最后一格应承担管理收口。

### 案例证明页语义约束

`left_logic_right_proof` 与 `metric_case_showcase_grid` 不得退化为图片墙。左侧必须给出判断链，右侧图片、截图、案例只证明一个核心判断；若证据不能支撑标题，应降级为待验证样例。

### 决策建议页语义约束

`risk_decision_matrix` 页面中，拍板事项必须独立突出，表格只承载责任、资源、时点、产出和风险闭环。不得让表格吞没全页结论。

### 路线图阶段门槛规则

`roadmap_timeline` 必须表达阶段递进，每阶段至少包含目标、关键动作、验收产出或进入下一阶段的门槛之一。不得只是并列计划。
```

### 3.3 `templates/chart_patterns.md`

建议增强：

```markdown
### `case_gallery_cards` 失败条件

- 图片或案例数量多，但没有证明同一个标题判断；
- 右侧证据与左侧逻辑各讲一套；
- 案例页变成素材墙、Logo 墙或截图墙；
- 没有来源或未经核验的数字被当成事实。

触发时应降级为 `left_logic_right_proof` 中的单案例证明，或标注为待验证样例。

### `decision_table` 失败条件

- 表格占满主体区，拍板事项不突出；
- 表格只有原则，没有责任、资源、时点、产出；
- 高层看完仍不知道需要拍什么。

触发时应将页面改为“拍板事项卡 + 执行清单表”。

### `capability_map` 失败条件

- 只列能力名称，没有连接到场景、机制或闭环；
- 所有能力同权，无法看出主能力和支撑能力；
- 图表无法解释标题中的关键判断。
```

### 3.4 `templates/wording_rules.md`

建议新增：

```markdown
### 长标题压缩规则

当标题超过 28~32 个汉字且包含多个从句时，应优先压缩成强判断句：

- `不是 A，而是 B`
- `核心不在 A，而在 B`
- `要先完成 A，再推进 B`
- `真正瓶颈不是 A，而是 B`
- `从 A 走向 B，关键在 C`

压缩后，副标题或讲解口径再承载背景说明。
```

建议新增：

```markdown
### 总结页最终定义规则

总结页不应复述前文要点，而应形成最终定义或决策框架。推荐句式：

- `X = 对象 + 能力 + 治理边界`
- `X 的本质不是 A，而是 B`
- `最终要形成 A、B、C、D 四类可验收能力`
```

### 3.5 `eval/visual_scorecard.md`

建议新增一票降级项：

```markdown
- 普通正文页红色横条/底座成为页面最大视觉块：最高 B 档；
- 多卡片页所有卡片同权且无主次：最高 B 档；
- 案例页退化为图片墙/素材墙，无法证明标题判断：最高 B 档；
- 决策页表格吞没拍板事项，高层看不出需要决策什么：最高 B 档；
- 总结页只复述前文，没有最终定义或新增管理含义：扣 5~8 分。
```

## 4. 不建议沉淀的内容

以下内容不应写入通用 Skill：

- 本次 AI4MBSE 主题中的具体术语、论文结论、案例名称；
- GBDL、FMU、XAI 等主题专属方法作为通用规则；
- 某一页具体视觉样式，如 P6 的红色底座；
- 未核验数字、客户、系统、产线、产品信息；
- 将本次主题结构作为所有技术汇报默认结构。

## 5. 推荐版本号

如用户确认允许沉淀，建议版本升级为：

```text
0.3.5-generated-image-feedback
```

版本说明：

```text
基于生成PPT图片与华为模板对标结果，增强正文页红色底座控制、多卡片主次层级、案例证明页、决策建议页、路线图阶段门槛、长标题压缩和总结页最终定义规则。
```

## 6. 回归测试建议

正式修改后，至少执行：

1. `eval/reference_learning_regression.md`
2. `eval/visual_scorecard.md`
3. 非 AI 主题污染测试
4. 一套 12~14 页技术高层汇报回归
5. 一套客户方案/解决方案型 PPT 回归

## 7. 结论

建议进入 Skill 资产沉淀，但应先由用户确认。当前最值得沉淀的是视觉语义与评估门禁，而不是本次 AI4MBSE 内容本身。