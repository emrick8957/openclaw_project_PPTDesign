# patch proposal：防机械套版门禁 v0.2

> 状态：Phase 0 revised proposal，仅供人工确认；未修改 `skills/huawei_ppt_master/*`。  
> 基于：`anti_template_stamp_gate_patch_v0.1.md`、`skill_review_anti_template_stamp_gate_v0.1.md`、`anti_template_stamp_gate_phase0_review_response_v0.1.md`。  
> 本版重点：吸收 P1/P2 评审意见，优先修正阈值鲁棒性与语义判据可复现性。

## 1. 目标版本

建议版本：`v0.4.0-anti-template-stamp-gate`

目标不变：在现有 `deck_spec` 证明契约和 `chart_semantic_mapping` 基础上，增加“字段差异化 / 模板印章检测 / page_design 下沉”门禁，防止交付物通过结构校验但缺少逐页设计决策。

本版相对 v0.1 的关键修正：

1. 将绝对阈值 `≥3 页重复` 改为混合阈值模型；
2. 为 `core_judgement`、`chart_proof_goal`、`chart_visual_boundary` 增加可执行判据与正反例；
3. 放宽 `core_judgement`，禁止字面复述，但允许正当提炼；
4. 明确模板印章检测必须作为强制后置自检步骤；
5. 字段差异化清单只在 `core/field_differentiation_rules.md` 维护，`eval/template_stamp_detection.md` 只引用；
6. 补充 `chart_data` 结构骨架豁免与 page_design 独立可读视图。

## 2. 建议新增文件

### 2.1 `skills/huawei_ppt_master/core/field_differentiation_rules.md`

定位：字段差异化的单一真相源。`eval/template_stamp_detection.md` 不再复制字段清单，只引用本文件。

建议内容：

```md
# 字段差异化规则

## 1. 定位

本文件定义 deck_spec、page_copy、page_design 中哪些字段必须承载逐页设计决策，哪些字段应作为全局默认下沉，避免机械套版。

本文件是字段差异化清单的唯一真相源；`eval/template_stamp_detection.md` 只引用本文件，不重复维护清单。

## 2. 字段分层

### 2.1 允许重复 / 建议下沉为全局默认

- 基础配色：白底、红黑灰白、红色克制；
- 字体气质；
- 页脚来源格式、页码、Confidential 等正式元素；
- 左右安全边距；
- 全局负面视觉边界；
- 输出格式说明；
- `chart_data` 的结构骨架、键名、列名、节点字段名：允许相似，仅判断语义内容是否机械重复。

### 2.2 必须逐页有设计增量

- `core_judgement`；
- `chart_proof_goal`；
- `chart_visual_boundary`；
- `visual_notes` 或 page_design overrides；
- `speaker_notes`；
- page_copy 中的图表内容、版式说明、讲解口径；
- page_design 中的区域划分、图表区、强调元素、PPTX Builder 注意事项、page_type_gate。

### 2.3 可半重复但必须带差异项

- `page_goal`：可有统一受众目标，但应加入本页特定动作；
- `visual_notes`：可引用全局默认，但必须给出本页主图、主红锚点、布局偏离项；
- `speaker_notes`：可统一“先判断、再证据、后动作”，但必须写明本页先解释什么机制或图形关系。

## 3. core_judgement

### 3.1 规则

- 不得等于 `conclusion`；
- 不得只是固定前缀 + `conclusion`；
- 允许是对 `conclusion` 的提炼、收口或管理化表达，但必须是不同表述，并承载本页唯一带走点；
- 背景页、上下文页不强制增加动作建议，避免为了差异化制造冗余。

### 3.2 FAIL 特征

- 与 `conclusion` 完全相同；
- 仅增加固定前缀，如“本页唯一要带走的判断：”；
- 未形成唯一带走点，只是复述背景信息。

### 3.3 PASS 特征

- 可从 `conclusion` 提炼，但措辞不同；
- 明确高层应该带走的判断；
- 可包含动作、取舍、风险边界或管理含义，但不强制所有页都动作化。

### 3.4 反例

```text
conclusion：复杂度上升导致单点 AI 难以支撑系统级工程决策。
core_judgement：本页唯一要带走的判断：复杂度上升导致单点 AI 难以支撑系统级工程决策。
```

### 3.5 正例

```text
core_judgement：本页要让高层判断，AI 试点不能继续按工具点推进，必须先补工程语义和流程闭环。
```

```text
core_judgement：本页核心判断不是“AI 可用”，而是现有工程流程缺少可被 AI 读取、验证和回写的系统语义底座。
```

## 4. chart_proof_goal

### 4.1 规则

- 必须回答主图证明什么关系；
- 至少命中一类：因果、对比、演进、闭环、分层、决策、权衡；
- 不得只是 `display_text` 的拼接；
- 应与 `chart_semantic_mapping.main_visual_logic` 一致。

### 4.2 FAIL 特征

- 固定前缀 + `display_text` 拼接 + 固定后缀；
- 只说“共同支撑判断”，没有说明支撑关系；
- 看不出主图为什么必须选当前 `chart_type`。

### 4.3 PASS 特征

- 明确图表证明的关系类型；
- 能解释为什么图表不是装饰；
- 能约束主图结构选择。

### 4.4 反例

```text
主图表必须证明：真实系统、语义模型、仿真、AI/XAI 共同支撑该页判断，而不是做装饰。
```

```text
主图表必须证明：样板选择、数据/模型责任、接口标准、审查机制共同支撑该页判断。
```

### 4.5 正例

```text
主图必须证明真实系统数据进入语义模型，经仿真与 AI/XAI 审查后再回写治理，形成自学习闭环；否则该页会退化为静态架构堆栈。
```

```text
主图必须证明四类拍板事项之间存在先后依赖：先定样板边界，再定数据/模型责任，最后固化接口和审查机制；否则会退化为普通任务清单。
```

## 5. chart_visual_boundary

### 5.1 规则

- 必须结合本页 `chart_type` 和 `chart_semantic_mapping.forbidden_visualization`；
- 至少 2 条来自本页图表风险；
- 必须说明该图表不得退化成什么形态；
- 不得多页复用同一组泛化约束。

### 5.2 FAIL 特征

- 多页完全同一组泛化禁令；
- 只写“不得无主次、保留红色锚点”等通用规则；
- 未吸收 `forbidden_visualization` 中的本页专属风险。

### 5.3 PASS 特征

- 明确 chart_type 最容易画偏的形态；
- 能约束红色、主次、方向、箭头、层级、表格吞没等问题；
- 与本页标题判断和 `chart_semantic_mapping` 一致。

### 5.4 反例

```text
不得画成无主次的信息堆叠；必须保留唯一主红色锚点；图表必须能解释标题判断。
```

```text
不得做装饰；不得信息过多；必须突出重点。
```

### 5.5 正例

```text
不得把七类 AI 介入点画成七个孤立散点；不得把产品 V 与生产 V 画成互不关联的两套图；红色只用于贯穿双 V 的生命周期主线。
```

```text
不得把自学习数字孪生画成静态三层架构；必须表现真实系统→语义模型→仿真/AI审查→模型回写的闭环箭头；AI/XAI 不得被画成孤立装饰节点。
```

## 6. visual_notes / page_design

- 通用视觉规范应下沉为 `global_design_defaults`；
- 每页 `visual_notes` / page_design overrides 只写本页主图、红色锚点、布局偏离、主次策略、压缩策略；
- 必须保留每页独立可读视图：

```text
page_design_view(Pn) = global_design_defaults + page_design_overrides(Pn)
```

若下游外部模型按“每页完整段落”消费，则输出时应把 `page_design_view(Pn)` 展开为该页完整提示，避免丢失上下文。
```

### 2.2 `skills/huawei_ppt_master/eval/template_stamp_detection.md`

定位：检测执行规则。字段清单引用 `core/field_differentiation_rules.md`，不重复维护。

建议内容：

```md
# 模板印章检测

## 1. 检测目标

识别 deck_spec、page_copy、page_design 中因机械套版导致的重复字段、骨架填词和伪差异化。

字段职责与分层以 `core/field_differentiation_rules.md` 为唯一真相源。

## 2. 混合阈值模型

设：

```text
N = deck 页数
repeat_threshold = max(3, ceil(N * 0.5))
```

### 2.1 N <= 3 小包规则

- 对关键差异化字段做两两比较；
- 任意关键差异化字段全同：WARN；
- 两个及以上关键差异化字段全同：FAIL；
- `chart_visual_boundary` 或 `visual_notes` / page_design overrides 全同：FAIL；
- 若字段已下沉为 `global_design_defaults`，且每页 overrides 有足够差异，则不判 FAIL。

### 2.2 N >= 4 通用规则

- 关键差异化字段重复页数 >= `repeat_threshold`：FAIL；
- 关键差异化字段重复页数 >= 3 且 < `repeat_threshold`：WARN；
- 若字段已下沉为 `global_design_defaults`，且每页 overrides 有足够差异，则不判 FAIL；
- 页脚、基础配色、安全边距、全局负面风格边界等白名单字段不参与 FAIL 判定。

## 3. 必检字段

必检字段引用 `core/field_differentiation_rules.md` 的“必须逐页有设计增量”与“可半重复但必须带差异项”章节。

## 4. 语义检测

必须使用 `core/field_differentiation_rules.md` 中 `core_judgement`、`chart_proof_goal`、`chart_visual_boundary` 的 FAIL/PASS 特征与正反例进行判断。

## 5. 自检输出格式

每次生成交付物时，自检必须包含：

| 检查项 | 结果 | 证据 | 处理建议 |
|---|---|---|---|
| 重复字段统计 | PASS/WARN/FAIL | 字段名 + 重复页数 + 阈值 | 下沉全局默认 / 重写逐页字段 |
| 复述检测 | PASS/WARN/FAIL | 字段与来源文本 | 改为正当提炼或补充唯一带走点 |
| 骨架填词检测 | PASS/WARN/FAIL | 固定前后缀/关键词拼接证据 | 补充因果/对比/演进/闭环/决策关系 |
| 设计增量检测 | PASS/WARN/FAIL | 每页差异信号数量 | 补充主图/锚点/边界/讲解差异 |
| 允许重复项 | PASS | 白名单字段 | 保留或下沉全局默认 |

## 6. 失败处理

出现 FAIL 时，不得输出最终交付包；必须重写对应字段或将通用规则下沉为全局默认并补齐每页 overrides。
```

## 3. 建议修改文件

### 3.1 `skills/huawei_ppt_master/SKILL.md`

#### 3.1.1 强制读取顺序

在 `core/output_contracts.md` 之后新增：

```md
读取 `core/field_differentiation_rules.md`。
```

在 `eval/visual_scorecard.md` / `eval/acceptance_checklist.md` 附近新增：

```md
读取 `eval/template_stamp_detection.md`。
```

#### 3.1.2 强制后置自检

在自检或输出前检查章节新增：

```md
生成 deck_spec/page_copy/page_design/self_check 后，必须执行 `eval/template_stamp_detection.md` 的模板印章检测，输出重复字段统计、复述检测、骨架填词检测、设计增量检测和允许重复项。若出现 FAIL，不得输出最终交付包，必须返工对应字段。
```

说明：v0.3.9 已有 `visual_notes`、`chart_visual_boundary` 生成要求，但未强制后置统计，因此未能阻止旧四页套版问题。本次补的是执行触点，不是新增渲染层。

### 3.2 `skills/huawei_ppt_master/core/output_contracts.md`

建议在 `4.0 deck_spec 证明契约字段` 后追加：

```md
### 4.0.1 字段差异化要求

`core_judgement`、`chart_proof_goal`、`chart_visual_boundary` 不只是必填字段，还必须承载逐页设计决策。具体字段职责、允许重复白名单、正反例和下沉规则以 `core/field_differentiation_rules.md` 为准。

关键要求：

- `core_judgement` 不得等于 `conclusion`，也不得只是固定前缀 + `conclusion`；允许对 `conclusion` 做正当提炼或收口；
- `chart_proof_goal` 必须说明主图证明的因果、对比、演进、闭环、分层、决策或权衡关系；
- `chart_visual_boundary` 必须结合本页图表风险和 `chart_semantic_mapping.forbidden_visualization`，不得多页复用同一组泛化边界；
- 通用视觉规范应下沉为全局默认，不得逐页重复伪装成页面设计。
```

建议在 `4.3 deck_spec 强门禁` 追加：

```md
13. 必须通过 `eval/template_stamp_detection.md` 的模板印章检测；
14. 重复判定必须使用混合阈值模型：N<=3 两两比较，N>=4 使用 `repeat_threshold=max(3,ceil(N*0.5))`；
15. `core_judgement` 不得等于 `conclusion` 或固定前缀 + `conclusion`；
16. `chart_visual_boundary`、`visual_notes` / page_design overrides 的重复不得触发模板印章 FAIL；如为通用规则，必须拆入 global_design_defaults；
17. `chart_data` 的键名、列名、节点结构相似不判 FAIL，只判语义内容是否机械重复。
```

### 3.3 `skills/huawei_ppt_master/prompts/deck_spec_generation.md`

建议在“生成时必须检查”中追加：

```md
- 生成后必须执行模板印章检测，并在 self_check 中输出：重复字段统计、复述检测、骨架填词检测、设计增量检测、允许重复项；
- 重复字段统计必须使用混合阈值模型：N<=3 两两比较，N>=4 使用 `repeat_threshold=max(3,ceil(N*0.5))`；
- `core_judgement` 不能等于 `conclusion`，也不能只是固定前缀 + `conclusion`；但允许对 `conclusion` 做不同表述的正当提炼；
- `chart_proof_goal` 必须说明主图证明的关系类型，不能只是关键词拼接；
- `chart_visual_boundary` 必须优先吸收 `chart_semantic_mapping.forbidden_visualization` 中的本页专属风险；
- `speaker_notes` 必须体现本页讲解顺序差异；
- 如 `visual_notes` 或 page_design 包含通用规范，应拆为 `global_design_defaults + page_design_overrides`，并保留每页独立可读视图。
```

### 3.4 `skills/huawei_ppt_master/eval/acceptance_checklist.md`

建议新增章节：

```md
## 9. 防机械套版门禁

- 是否执行了 `eval/template_stamp_detection.md`；
- 是否在 self_check 中输出重复字段统计、复述检测、骨架填词检测、设计增量检测和允许重复项；
- 是否使用混合阈值模型，而不是固定 `>=3 页`；
- `core_judgement` 是否避免字面复述 `conclusion`，同时允许正当提炼；
- `chart_proof_goal` 是否说明主图证明关系，而非关键词拼接；
- `chart_visual_boundary` 是否逐页结合图表风险和 `forbidden_visualization`；
- `visual_notes` 和 page_design 是否将通用规则下沉为全局默认，并提供每页 overrides；
- `chart_data` 是否只检查语义内容，不因结构键名相似而误判。

出现以下任一项，必须重写：

- 模板印章检测出现 FAIL；
- `core_judgement` 等于 `conclusion` 或固定前缀 + `conclusion`；
- `chart_proof_goal` 只是固定前缀 + 关键词拼接 + 固定后缀，未说明关系；
- `chart_visual_boundary` 在混合阈值模型下触发重复 FAIL；
- page_design 的本页红色锚点、图表区、page_type_gate 在混合阈值模型下触发重复 FAIL。
```

### 3.5 `skills/huawei_ppt_master/eval/visual_scorecard.md`

建议新增章节：

```md
## N. 模板印章一票降级项

出现以下任一问题，页面最高 B 档；若在混合阈值模型下触发 FAIL，整套交付必须返工：

- 逐页设计字段大面积重复，导致下游无法判断每页独有设计动作；
- `core_judgement` 只是字面复述 `conclusion`；
- `chart_proof_goal` 只是关键词拼接，未说明因果、对比、演进、闭环、分层、决策或权衡关系；
- `chart_visual_boundary` 未结合本页 `chart_type` 和 `forbidden_visualization`；
- page_design 重复通用约束但缺少本页主图结构、红色锚点原因、区域比例和退化边界；
- `speaker_notes` 全 deck 使用同一句话，无法指导讲解节奏。
```

### 3.6 `skills/huawei_ppt_master/templates/visual_rules.md`

建议新增：

```md
## 通用视觉规则下沉要求

通用视觉规则用于定义全局默认，不应在每页 page_design 中逐字重复并伪装成页面独有设计。

逐页 page_design 应只写：

- 本页主视觉结构；
- 本页红色锚点原因；
- 本页主图占比或区域偏离；
- 本页图表不得退化形态；
- 本页独有设计动作。

面向下游外部模型时，必须保留每页独立可读视图：

```text
page_design_view(Pn) = global_design_defaults + page_design_overrides(Pn)
```
```

### 3.7 `skills/huawei_ppt_master/templates/wording_rules.md`

建议新增：

```md
## 防骨架填词规则

禁止把固定句式作为字段生成器直接套用：

- 不得把 `core_judgement` 写成固定前缀 + `conclusion`；
- 不得把 `chart_proof_goal` 写成固定前缀 + 关键词拼接 + 固定后缀；
- 不得让 page_copy 的“核心判断”原样复制“一句话结论”；
- 不得让所有页面使用同一句讲解口径。

允许统一表达风格，也允许背景页对结论进行正当提炼，但每页必须形成独立带走点或图表证明关系。
```

### 3.8 版本同步文件

若 Phase 1 确认落地，需要同步：

- `README.md`
- `VERSION.md`
- `CHANGELOG.md`
- `INDEX.md`
- `QUICK_INDEX.md`
- `PACKAGE_MANIFEST.md`

新增资产必须写入 manifest，避免包清单遗漏。

## 4. 回归用例

### 4.1 RT-00：旧四页交付包必须 FAIL

对象：

`project/work/AI4MBSE_P4_P7_P8_P14_delivery/`

预期：

- `chart_visual_boundary` 四页完全相同：N=4，threshold=3 → FAIL；
- `visual_notes` 四页完全相同：N=4，threshold=3 → FAIL；
- `speaker_notes` 四页完全相同：WARN；若缺少逐页讲解顺序 → FAIL；
- `core_judgement` = 固定前缀 + `conclusion` → FAIL；
- `chart_proof_goal` 疑似骨架填词 → WARN；若未说明关系 → FAIL。

### 4.2 RT-01：3 页小包退化规则

构造 3 页样例，其中：

- `chart_visual_boundary` 三页完全相同；
- `core_judgement` 各页只是固定前缀 + `conclusion`。

预期：

- N<=3 两两比较命中；
- `chart_visual_boundary` 全同 → FAIL；
- `core_judgement` 复述 → FAIL。

### 4.3 RT-02：14 页大包不误伤

构造 14 页样例，其中仅 3 页 `visual_notes` 相同，且已拆为 `global_design_defaults`，每页 overrides 不同。

预期：

- N=14，threshold=7；
- 3 页相同未达 threshold；
- 已拆全局默认 + overrides 不同 → PASS 或最多 WARN，不得 FAIL。

### 4.4 RT-03：core_judgement 正当提炼不误伤

背景页样例：

```text
conclusion：复杂度上升使单点 AI 难以支撑系统级工程决策。
core_judgement：本页核心判断不是 AI 是否可用，而是工程流程缺少支撑系统级决策的语义闭环。
```

预期：PASS。

### 4.5 RT-04：chart_data 结构骨架相似不误伤

构造多页同 `chart_type=layered_stack_diagram`，`chart_data.layers/items` 键名相似，但层级语义、节点内容、证明目标不同。

预期：PASS。

### 4.6 RT-05：新四页样例必须 PASS

重生成 P4/P7/P8/P14 后，预期：

- `core_judgement` 各页不是字面复述；
- `chart_proof_goal` 各页说明关系；
- `chart_visual_boundary` 各页至少 2 条本页专属风险；
- `visual_notes` / page_design 拆为全局默认 + 每页偏离项；
- self_check 输出模板印章检测结果。

## 5. 不做事项

- 不恢复 `page_render_spec`；
- 不恢复 `normalized_render_model`；
- 不新增渲染 DSL；
- 不要求所有字段都差异化；
- 不把华为风格一致性误判为机械套版；
- 不因 `chart_data` 键名/列名/节点结构相似直接判 FAIL。

## 6. 合入建议

v0.2 已吸收 P1/P2 主要评审意见，建议作为下一轮评审对象。

是否进入 Phase 1 落地，应在 v0.2 评审后决定；本 proposal 本身不执行正式 Skill 修改。
