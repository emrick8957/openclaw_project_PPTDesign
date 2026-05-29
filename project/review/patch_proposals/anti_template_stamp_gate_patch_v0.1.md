# patch proposal：防机械套版门禁 v0.1

> 状态：Phase 0 proposal，仅供人工确认；未修改 `skills/huawei_ppt_master/*`。

## 1. 目标版本

建议版本：`v0.4.0-anti-template-stamp-gate`

目标：在现有 `deck_spec` 证明契约和 `chart_semantic_mapping` 基础上，增加“字段差异化 / 模板印章检测 / page_design 下沉”门禁，防止交付物通过结构校验但缺少逐页设计决策。

## 2. 建议新增文件

### 2.1 `skills/huawei_ppt_master/eval/template_stamp_detection.md`

建议内容：

```md
# 模板印章检测

## 1. 检测目标

识别 deck_spec、page_copy、page_design 中因机械套版导致的重复字段、骨架填词和伪差异化。

## 2. 字段分层

### 2.1 允许重复白名单

- 基础配色：白底、红黑灰白、红色克制；
- 页脚来源格式、页码、Confidential 等正式元素；
- 左右安全边距；
- 全局负面视觉边界；
- 输出格式字段名。

### 2.2 必须逐页差异化字段

- `core_judgement`；
- `chart_proof_goal`；
- `chart_visual_boundary`；
- `visual_notes`；
- `speaker_notes`；
- page_copy 的图表内容、版式说明、讲解口径；
- page_design 的区域划分、图表区、强调元素、PPTX Builder 注意事项、page_type_gate。

## 3. FAIL 规则

- `chart_visual_boundary` 在 ≥3 页逐字相同；
- `visual_notes` 在 ≥3 页逐字相同，且未拆为全局默认；
- `core_judgement` 等于 `conclusion`，或只是固定前缀 + `conclusion`；
- `chart_proof_goal` 只是固定前缀 + `display_text` 拼接 + 固定后缀，且未说明因果/对比/演进/闭环/决策关系；
- page_design 中本应逐页变化的 `red_anchor`、`page_type_gate`、图表退化边界在 ≥3 页相同。

## 4. WARN 规则

- `speaker_notes` 在 ≥3 页逐字相同；
- page_copy 的核心判断原样复制一句话结论；
- page_design 的通用视觉降噪约束逐页重复，但未影响本页关键设计判断；
- `page_goal` 完全相同但不影响后续生成。

## 5. 自检输出格式

每次生成交付物时，自检应包含：

| 检查项 | 结果 | 证据 | 处理建议 |
|---|---|---|---|
| 重复字段统计 | PASS/WARN/FAIL | 字段名 + 重复页数 | 下沉全局默认 / 重写逐页字段 |
| 复述检测 | PASS/WARN/FAIL | 字段与来源文本 | 补充动作指向或取舍判断 |
| 设计增量检测 | PASS/WARN/FAIL | 每页差异信号数量 | 补充主图/锚点/边界/讲解差异 |
```

### 2.2 `skills/huawei_ppt_master/core/field_differentiation_rules.md`

建议内容：

```md
# 字段差异化规则

## 1. 定位

本文件定义 deck_spec、page_copy、page_design 中哪些字段必须承载逐页设计决策，哪些字段应作为全局默认下沉，避免机械套版。

## 2. core_judgement

- 不得等于 `conclusion`；
- 不得只是“本页唯一要带走的判断：” + `conclusion`；
- 必须增加至少一类增量：动作指向、取舍判断、管理含义、风险边界、验收口径。

## 3. chart_proof_goal

- 必须回答主图证明什么关系；
- 至少命中一类：因果、对比、演进、闭环、分层、决策、权衡；
- 不得只是 `display_text` 的拼接。

## 4. chart_visual_boundary

- 必须结合本页 `chart_type` 和 `chart_semantic_mapping.forbidden_visualization`；
- 必须包含本页专属退化风险；
- 不得多页复用同一组泛化约束。

## 5. visual_notes

- 通用视觉规范应下沉为 `global_design_defaults`；
- 每页 `visual_notes` 只写本页主图、红色锚点、布局偏离、主次策略、压缩策略。

## 6. page_design

推荐输出结构：

- `global_design_defaults`：全局共性规则；
- `page_design_overrides`：逐页独有设计动作。

每页 overrides 至少包含：主视觉结构、红色锚点原因、区域比例或主图占比、图表不得退化形态、本页讲解路径。
```

## 3. 建议修改文件

### 3.1 `skills/huawei_ppt_master/SKILL.md`

在强制读取顺序中，建议新增：

```md
- 读取 `core/field_differentiation_rules.md`；
- 读取 `eval/template_stamp_detection.md`；
```

建议位置：

- `core/field_differentiation_rules.md` 放在 `core/output_contracts.md` 之后；
- `eval/template_stamp_detection.md` 放在 `eval/visual_scorecard.md` 或验收检查附近。

### 3.2 `skills/huawei_ppt_master/core/output_contracts.md`

建议在 `4.0 deck_spec 证明契约字段` 后追加：

```md
### 4.0.1 字段差异化要求

`core_judgement`、`chart_proof_goal`、`chart_visual_boundary` 不只是必填字段，还必须承载逐页设计决策：

- `core_judgement` 不得等于 `conclusion`，也不得只是固定前缀 + `conclusion`；
- `chart_proof_goal` 必须说明主图证明的因果、对比、演进、闭环、分层或决策关系；
- `chart_visual_boundary` 必须结合本页图表风险，不得多页复用同一组泛化边界；
- 通用视觉规范应下沉为全局默认，不得逐页重复伪装成页面设计。
```

建议在 `4.3 deck_spec 强门禁` 追加：

```md
13. 必须通过 `eval/template_stamp_detection.md` 的模板印章检测；
14. `core_judgement` 不得等于 `conclusion` 或固定前缀 + `conclusion`；
15. `chart_visual_boundary` 在同一 deck 内不得 ≥3 页逐字相同，除非明确拆为全局默认且每页另有 overrides；
16. `visual_notes` 在同一 deck 内不得 ≥3 页逐字相同，除非明确拆为全局默认。
```

### 3.3 `skills/huawei_ppt_master/prompts/deck_spec_generation.md`

建议在“生成时必须检查”中追加：

```md
- 生成后必须执行模板印章检测：统计 `core_judgement`、`chart_proof_goal`、`chart_visual_boundary`、`visual_notes`、`speaker_notes` 的重复页数；
- `core_judgement` 不能等于 `conclusion`，也不能只是固定前缀 + `conclusion`；
- `chart_visual_boundary` 必须优先吸收 `chart_semantic_mapping.forbidden_visualization` 中的本页专属风险；
- `speaker_notes` 必须体现本页讲解顺序差异；
- 如 `visual_notes` 包含通用规范，应拆为全局默认 + 页面差异项。
```

### 3.4 `skills/huawei_ppt_master/eval/acceptance_checklist.md`

建议新增章节：

```md
## 9. 防机械套版门禁

- 是否统计了关键字段跨页重复情况；
- `core_judgement` 是否避免复述 `conclusion`；
- `chart_proof_goal` 是否说明主图证明关系，而非关键词拼接；
- `chart_visual_boundary` 是否逐页结合图表风险；
- `visual_notes` 和 page_design 是否将通用规则下沉为全局默认；
- 自检是否输出 FAIL / WARN / 允许重复项。

出现以下任一项，必须重写：

- `chart_visual_boundary` 在 ≥3 页逐字相同；
- `visual_notes` 在 ≥3 页逐字相同且没有全局默认拆分；
- `core_judgement` 等于 `conclusion` 或固定前缀 + `conclusion`；
- page_design 的本页红色锚点、图表区、page_type_gate 在 ≥3 页机械重复。
```

### 3.5 `skills/huawei_ppt_master/eval/visual_scorecard.md`

建议新增章节：

```md
## N. 模板印章一票降级项

出现以下任一问题，页面最高 B 档；若影响同一 deck 内 ≥3 页，整套交付必须返工：

- 逐页设计字段大面积重复，导致下游无法判断每页独有设计动作；
- `core_judgement` 只是复述 `conclusion`；
- `chart_visual_boundary` 未结合本页 `chart_type` 和 `forbidden_visualization`；
- page_design 重复通用约束但缺少本页主图结构、红色锚点原因、区域比例和退化边界；
- `speaker_notes` 全 deck 使用同一句话，无法指导讲解节奏。
```

### 3.6 `skills/huawei_ppt_master/templates/visual_rules.md`

建议在“页面区域与版式骨架”或末尾增加：

```md
## 通用视觉规则下沉要求

通用视觉规则用于定义全局默认，不应在每页 page_design 中逐字重复。

逐页 page_design 应只写：

- 本页主视觉结构；
- 本页红色锚点原因；
- 本页主图占比或区域偏离；
- 本页图表不得退化形态；
- 本页独有设计动作。
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

允许统一表达风格，但每页必须增加动作指向、取舍判断、机制解释或管理含义。
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

### 4.1 必须失败的旧样例

使用：

`project/work/AI4MBSE_P4_P7_P8_P14_delivery/`

预期：

- `chart_visual_boundary` 四页完全相同 → FAIL；
- `visual_notes` 四页完全相同 → FAIL；
- `speaker_notes` 四页完全相同 → WARN/FAIL；
- `core_judgement` = 固定前缀 + `conclusion` → FAIL；
- page_design 多段通用约束逐页重复 → WARN；若红色锚点与 page_type_gate 缺少逐页差异，则 FAIL。

### 4.2 必须通过的新样例

重生成 P4/P7/P8/P14 后，预期：

- `core_judgement` 各页包含动作指向或管理含义；
- `chart_visual_boundary` 各页至少 2 条本页专属风险；
- `visual_notes` 拆为全局默认 + 每页偏离项；
- `speaker_notes` 体现 P4/P7/P8/P14 不同讲解顺序；
- 自检报告输出重复字段统计。

## 5. 不做事项

- 不恢复 `page_render_spec`；
- 不恢复 `normalized_render_model`；
- 不新增渲染 DSL；
- 不要求所有字段都差异化；
- 不把华为风格一致性误判为机械套版。
