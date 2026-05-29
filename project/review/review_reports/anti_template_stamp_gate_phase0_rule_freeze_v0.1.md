# 防机械套版门禁 Phase 0 规则冻结 v0.1

## 1. 背景

在 `AI4MBSE_P4_P7_P8_P14_delivery` 四页交付物评审中发现：

- `deck_spec.json` 结构合法；
- `chart_type` / `layout_pattern` 枚举合法；
- `chart_semantic_mapping` 逐页质量较高；
- 但多个设计字段存在跨页重复和骨架填词，导致“看似稳定、实际缺少逐页设计决策”。

因此，本阶段冻结一组“防机械套版”规则，用于后续 patch proposal。Phase 0 不修改正式 Skill。

## 2. 原则

### 2.1 不反对风格一致

华为风格需要稳定的全局规范，例如：

- 白底、红黑灰白；
- 页脚弱化；
- 安全边距；
- 红色克制；
- 不使用互联网发布会风、咨询海报风、卡通插画风等负面边界。

这些可以重复，但应尽量下沉为全局默认，不应伪装成每页独有设计。

### 2.2 反对机械套版

以下问题应被识别：

- 同一字段跨 ≥3 页逐字相同，且字段职责本应承载逐页设计决策；
- 字段只是对 `title`、`conclusion`、`display_text` 的加前缀复述；
- `chart_proof_goal` 只把关键词拼成一句“共同支撑判断”；
- `chart_visual_boundary` 没有吸收本页图表风险，四页使用同一套泛化禁令；
- page_design 把通用视觉规范逐页重复，导致下游模型以为每页设计策略相同。

## 3. 字段分层

### 3.1 允许重复字段 / 内容

允许重复，但建议下沉为全局默认：

- 基础色彩规则；
- 字体气质；
- 页脚位置和来源格式；
- 左右安全边距；
- 全局负面风格边界；
- “红色锚点克制”等通用视觉原则；
- 输出格式说明。

### 3.2 必须逐页有设计增量的字段

以下字段必须体现本页论证任务、图表类型或风险边界差异：

- `core_judgement`；
- `chart_proof_goal`；
- `chart_visual_boundary`；
- `visual_notes`；
- `speaker_notes`；
- page_copy 中的“图表内容 / 版式说明 / 讲解口径”；
- page_design 中的“区域划分 / 图表区 / 强调元素 / PPTX Builder 注意事项 / page_type_gate”。

### 3.3 可半重复字段

这些字段可包含统一骨架，但必须带本页差异项：

- `page_goal`：可有统一受众目标，但应加入本页特定动作；
- `visual_notes`：可引用全局默认，但必须给出本页主图、主红锚点、布局偏离项；
- `speaker_notes`：可统一“先判断、再证据、后动作”，但必须写明本页先解释什么机制。

## 4. 强门禁

### 4.1 重复门禁

同一 deck 内：

- `chart_visual_boundary` 在 ≥3 页逐字相同：FAIL；
- `visual_notes` 在 ≥3 页逐字相同，且未拆为全局默认：FAIL；
- `speaker_notes` 在 ≥3 页逐字相同：WARN；若同时缺少逐页讲解顺序，则 FAIL；
- page_design 的“视觉降噪约束”在 ≥3 页逐字相同：WARN；若其中包含本应逐页变化的 `red_anchor`、`page_type_gate`，则 FAIL。

### 4.2 复述门禁

- `core_judgement == conclusion`：FAIL；
- `core_judgement == 固定前缀 + conclusion`：FAIL；
- `chart_proof_goal == 固定前缀 + display_text 拼接 + 固定后缀`：WARN；若未说明因果/对比/演进/闭环/决策关系，则 FAIL；
- page_copy 的“核心判断”原样复制“一句话结论”：WARN；若全 deck 多页如此，则 FAIL。

### 4.3 逐页设计决策门禁

每页至少应包含 3 类逐页差异信号：

1. 本页主图证明逻辑：因果、对比、演进、闭环、决策或分层关系；
2. 本页视觉风险边界：不得退化为什么；
3. 本页红色锚点和主次策略：为什么只强调该节点；
4. 本页区域比例或主图占比：应与页型匹配；
5. 本页讲解顺序：先解释哪一个关键机制或图形关系。

少于 3 类：WARN；少于 2 类：FAIL。

## 5. page_design 下沉规则

建议后续输出从：

```text
每页重复完整通用设计说明
```

调整为：

```text
## global_design_defaults
- 全局色彩 / 页脚 / 安全区 / 字体 / 禁止风格

## page_design_overrides
### Pn
- 主视觉结构
- 本页红色锚点原因
- 区域比例或主图占比
- 图表不得退化形态
- 本页独有设计动作
```

这样既保留华为风格一致性，又减少机械重复对下游模型的误导。

## 6. 与既有能力的关系

- 不替代 `chart_semantic_mapping`，而是要求 `chart_visual_boundary`、`visual_notes`、`page_design` 从中吸收逐页风险；
- 不恢复 `page_render_spec` / `normalized_render_model`；
- 不新增渲染 DSL；
- 只增强内容与设计交付物的质量门禁。

## 7. Phase 1 验收标准

后续若进入 Phase 1，必须满足：

- 新增或修改后的规则能检出旧 P4/P7/P8/P14 交付包中的重复问题；
- 不把页脚、基础配色、安全边距等合理共性误判为 FAIL；
- `chart_semantic_mapping` 已有优点不被削弱；
- 自检报告必须输出“重复字段统计 / FAIL 项 / WARN 项 / 允许重复项”。
