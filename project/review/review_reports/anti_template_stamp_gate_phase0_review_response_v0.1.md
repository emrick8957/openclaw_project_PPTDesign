# 防机械套版门禁 Phase 0 评审意见续评 v0.1

## 1. 输入

评审意见文件：

`project/review/review_reports/skill_review_anti_template_stamp_gate_v0.1.md`

关联 proposal：

`project/review/patch_proposals/anti_template_stamp_gate_patch_v0.1.md`

本轮用户约束：

- 继续评审；
- 个人建议 P1 优先；
- 本轮暂不启动落地。

## 2. 总体判断

我接受该评审报告的主要结论：**有条件合入**是合理判断，但当前不宜直接进入 Skill 落地。

尤其 P1 问题必须优先处理：

1. R-01：绝对阈值 `≥3 页` 不鲁棒；
2. R-02：语义类判据缺少可执行锚点，LLM 自检复现性不足。

这两个问题如果不先修，Phase 1 落地会把“检测机械套版”变成另一个不稳定判断源。

## 3. 对评审问题的采纳情况

| ID | 严重度 | 是否采纳 | 处理优先级 | 续评判断 |
|---|---|---|---|---|
| R-01 | P1 | 采纳 | 最高 | 必须先改阈值模型，否则小包漏检、大 deck 误伤 |
| R-02 | P1 | 采纳 | 最高 | 必须补正反例和可判定特征，否则自检不稳定 |
| R-03 | P2 | 采纳 | 次高 | `core_judgement` 规则确实偏硬，应从“必须动作化”改成“禁止字面复述，允许正当提炼” |
| R-04 | P2 | 采纳 | 次高 | 需要把检测放入强制后置自检，否则可能重演旧规则未执行问题 |
| R-05 | P2 | 采纳 | 次高 | 字段清单应单一真相源，避免 core/eval 双写漂移 |
| R-06 | P3 | 采纳 | 后续 | `chart_data` 结构骨架相似应豁免，只判语义内容 |
| R-07 | P3 | 部分采纳 | 后续 | page_design 下沉方向正确，但必须保留每页独立可读视图 |

## 4. P1 优先修订建议

### 4.1 P1-A：阈值模型从绝对页数改为混合阈值

原规则：

```text
同一字段在 ≥3 页逐字相同 → FAIL/WARN
```

问题：

- N≤3 的交付包可能永远漏检；
- N 很大时，仅 3 页重复可能不应全局 FAIL；
- 不区分字段职责，容易误伤。

建议改为：

```text
N = deck 页数
重复阈值 repeat_threshold = max(3, ceil(N * 0.5))

当 N <= 3：
- 对关键差异化字段做两两比较；
- 任意关键字段全同：WARN；
- 两个及以上关键字段全同，或 chart_visual_boundary/visual_notes 全同：FAIL。

当 N >= 4：
- 关键差异化字段重复页数 >= repeat_threshold：FAIL；
- 关键差异化字段重复页数 >= 3 但未达 repeat_threshold：WARN；
- 若字段已下沉为 global_design_defaults，且每页 overrides 有足够差异，则不判 FAIL。
```

关键差异化字段建议限定为：

- `core_judgement`；
- `chart_proof_goal`；
- `chart_visual_boundary`；
- `visual_notes` / page_design overrides；
- `speaker_notes`。

### 4.2 P1-B：语义判断补充可操作判据与 few-shot 锚点

R-02 的判断很关键。建议给每个高风险字段补“可判定特征 + 正反例”，优先覆盖 3 个字段：

#### core_judgement

FAIL 特征：

- 与 `conclusion` 完全相同；
- 仅增加固定前缀，如“本页唯一要带走的判断：”；
- 未形成“唯一带走点”，只是复述背景信息。

PASS 特征：

- 可从 conclusion 提炼，但措辞不同；
- 明确本页要让高层形成的判断；
- 可包含动作、取舍、风险边界或管理含义，但不是强制所有页都动作化。

反例：

```text
conclusion：复杂度上升导致单点 AI 难以支撑系统级工程决策。
core_judgement：本页唯一要带走的判断：复杂度上升导致单点 AI 难以支撑系统级工程决策。
```

正例：

```text
core_judgement：本页要让高层判断，AI 试点不能继续按工具点推进，必须先补工程语义和流程闭环。
```

#### chart_proof_goal

FAIL 特征：

- 固定前缀 + `display_text` 拼接 + 固定后缀；
- 只说“共同支撑判断”，没说明支撑关系；
- 看不出主图为什么必须选当前 `chart_type`。

PASS 特征：

- 明确主图证明的关系类型：因果、对比、演进、闭环、分层、决策、权衡；
- 能解释为什么图表不是装饰；
- 与 `chart_semantic_mapping.main_visual_logic` 一致。

反例：

```text
主图表必须证明：真实系统、语义模型、仿真、AI/XAI 共同支撑该页判断，而不是做装饰。
```

正例：

```text
主图必须证明真实系统数据进入语义模型，经仿真与 AI/XAI 审查后再回写治理，形成自学习闭环；否则该页会退化为静态架构堆栈。
```

#### chart_visual_boundary

FAIL 特征：

- 多页完全同一组泛化禁令；
- 只写“不得无主次、保留红色锚点”等通用规则；
- 未吸收 `forbidden_visualization` 中的本页专属风险。

PASS 特征：

- 至少 2 条来自本页图表风险；
- 明确该 chart_type 最容易画偏的形态；
- 能约束红色、主次、方向、箭头、层级或表格吞没问题。

反例：

```text
不得画成无主次的信息堆叠；必须保留唯一主红色锚点；图表必须能解释标题判断。
```

正例：

```text
不得把七类 AI 介入点画成七个孤立散点；不得把产品 V 与生产 V 画成互不关联的两套图；红色只用于贯穿双 V 的生命周期主线。
```

## 5. P2 配套修订建议

P1 修完后，再处理 P2：

1. `core_judgement` 从“必须增加动作/取舍/管理含义”改为：
   - 禁止字面复述；
   - 允许正当提炼；
   - 背景页可以是判断收口，不强制动作化。
2. `template_stamp_detection` 必须写入强制后置自检，而不仅是读取文件。
3. 字段差异化清单只维护在 `core/field_differentiation_rules.md`：
   - `eval/template_stamp_detection.md` 引用该清单；
   - 不重复维护字段列表。
4. 对旧规则未生效做根因解释：
   - 旧规则停留在生成要求；
   - 缺少生成后重复统计；
   - 缺少 FAIL/WARN 输出格式；
   - 缺少回归样例。

## 6. P3 后续处理建议

P3 不阻断下一版 proposal，但建议记录：

- `chart_data` 的键名、列名、节点结构允许相似；只判语义内容是否逐页不同；
- page_design 可以下沉为全局默认 + 偏离项，但必须保留“每页独立可读视图”：

```text
每页最终给下游的 page_design_view = global_design_defaults + current_page_overrides
```

这样既减少重复，又避免外部生图模型拿不到上下文。

## 7. 建议下一步，不落地

本轮不启动正式 Skill 落地。建议下一步只做一个修订版 proposal：

`project/review/patch_proposals/anti_template_stamp_gate_patch_v0.2.md`

v0.2 应吸收：

- BL-01 阈值模型；
- BL-02 正反例；
- BL-03 core_judgement 放宽；
- BL-04 强制后置自检触点；
- BL-05 单一真相源；
- BL-06/BL-07 作为附加兼容项。

确认 v0.2 后，再决定是否进入 Phase 1 落地。

## 8. 当前结论

- P1 优先是正确策略；
- 当前 v0.1 proposal 不建议直接合入；
- 本轮只完成续评，不改正式 Skill；
- 建议下一轮先产出 v0.2 patch proposal，再评审是否落地。
