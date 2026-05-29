# AI4MBSE 四页交付物“防机械套版”可行性评审 v0.1

## 1. 结论

用户提出的诊断成立：当前四页交付物的结构稳定性，很大一部分来自重复字段与通用模板句，而不是逐页真实设计决策。

建议启动一个小版本能力迭代：`v0.4.0-anti-template-stamp-gate`。

目标不是推翻 `deck_spec.json`，而是在现有 `deck_spec` 证明契约之上增加“字段差异化 / 设计增量 / 模板印章检测”门禁，防止交付物看似完整、实际误导下游生图或 PPTX Builder。

## 2. 证据核验

对 `project/work/AI4MBSE_P4_P7_P8_P14_delivery/` 抽查结果：

| 字段 | 唯一值数量 | 评估 |
|---|---:|---|
| `page_goal` | 1 / 4 | 四页完全相同，属于通用目标 |
| `chart_visual_boundary` | 1 / 4 | 四页完全相同，未承载逐页视觉边界 |
| `visual_notes` | 1 / 4 | 四页完全相同，无法指导差异化生成 |
| `speaker_notes` | 1 / 4 | 四页完全相同，讲解动作没有分化 |
| `core_judgement` | 4 / 4 | 表面不同，但四页均为 `本页唯一要带走的判断：` + `conclusion`，增量不足 |
| `chart_proof_goal` | 4 / 4 | 表面不同，但句式高度模板化 |

逐页内容中真正有效的差异化信号主要来自：

1. `title` / `conclusion`；
2. `chart_data`；
3. `chart_semantic_mapping`；
4. 少量 `must_highlight` / `visual_focus`。

## 3. 可行性判断

### 3.1 技术可行性：高

三条建议均可落地为规则和自检，不需要恢复 `page_render_spec`，也不需要新增渲染 DSL。

- “模板印章检测”可通过字段相似度 / 重复计数实现；
- `core_judgement != conclusion` 可作为确定性规则；
- `chart_visual_boundary` 可要求吸收 `chart_semantic_mapping.forbidden_visualization` 的逐页差异；
- `page_design` 可拆为全局默认 + 单页偏离项，减少重复噪声。

### 3.2 对现有 Skill 影响：中等

会影响输出契约、deck_spec 生成提示词、自检门禁和页面设计说明模板。风险可控，但必须避免一刀切：

- `page_goal`、页脚、安全边距、基础配色等字段允许跨页相同；
- 不能要求所有字段都差异化，否则会破坏风格一致性；
- 门禁应区分“允许重复的全局规范”和“必须逐页承载决策的字段”。

### 3.3 对下游价值：高

该改动能减少下游生图/PPTX Builder 接收到的重复噪声，让每页的设计输入更聚焦：

- 哪个字段是全局风格默认；
- 哪个字段是本页独有图表边界；
- 哪个字段必须决定主图、主次、红色锚点和阅读路径。

## 4. 建议落地资产

### 4.1 新增资产

| 资产 | 建议路径 | 作用 |
|---|---|---|
| 防机械套版规则 | `skills/huawei_ppt_master/eval/template_stamp_detection.md` | 定义字段重复阈值、允许重复白名单、FAIL/WARN 规则 |
| 字段差异化规则 | `skills/huawei_ppt_master/core/field_differentiation_rules.md` | 定义哪些字段必须逐页有增量、哪些字段应下沉为全局默认 |
| 自检脚本/提示模板 | `skills/huawei_ppt_master/prompts/self_check_generation.md` 或扩展现有提示 | 要求自检输出重复字段统计和失败项 |

### 4.2 修改资产

| 资产 | 修改点 |
|---|---|
| `core/output_contracts.md` | 增加 `core_judgement`、`chart_proof_goal`、`chart_visual_boundary` 的差异化要求 |
| `prompts/deck_spec_generation.md` | 增加生成前后字段去重检查；禁止 `core_judgement = conclusion` |
| `eval/visual_scorecard.md` | 增加“模板印章一票降级项” |
| `eval/acceptance_checklist.md` | 若存在则加入交付门禁；若不存在建议新增 |
| `templates/visual_rules.md` | 明确通用视觉约束应作为全局默认，不要逐页机械复写 |
| `templates/wording_rules.md` | 增加禁止“骨架填词式”口径 |
| `README.md` / `VERSION.md` / `CHANGELOG.md` / `INDEX.md` / `PACKAGE_MANIFEST.md` | 版本和资产同步 |

### 4.3 可选修改资产

| 资产 | 修改点 |
|---|---|
| `core/deck_spec_field_dictionary.md` | 补充字段职责：哪些字段必须承载逐页设计决策 |
| `templates/page_types.md` | 为常见页型提供差异化 page_design 要点 |
| `visual_patterns/layout_library.md` | 为不同 layout_pattern 增加区域比例建议区间，避免固定 12/78/5 |

## 5. 建议门禁规则

### 5.1 字段重复门禁

- 对同一 deck 内的以下字段执行重复检测：
  - `core_judgement`
  - `chart_proof_goal`
  - `chart_visual_boundary`
  - `visual_notes`
  - `speaker_notes`
  - page_copy 中“图表内容 / 版式说明 / 讲解口径”
  - page_design 中“区域划分 / 图表区 / 视觉降噪约束”
- 规则：
  - 同一字段在 ≥3 页逐字相同：FAIL，除非字段在允许重复白名单中；
  - 高相似骨架填词：WARN 或 FAIL，视字段职责而定；
  - `chart_visual_boundary` 在 ≥3 页相同：FAIL；
  - `visual_notes` 在 ≥3 页相同：FAIL，除非拆为全局默认。

### 5.2 字段去重规则

- `core_judgement` 不得等于 `conclusion`，也不得只是加前缀复述；
- `core_judgement` 必须增加“动作指向 / 取舍判断 / 管理含义”之一；
- `chart_proof_goal` 必须说明主图要证明的因果、对比、演进、闭环或决策关系，而不是只拼接 `display_text`；
- `chart_visual_boundary` 必须引用本页图表风险，优先吸收 `chart_semantic_mapping.forbidden_visualization`；
- `speaker_notes` 必须至少体现本页讲解顺序差异，例如“先解释趋势拐点 / 先解释双 V 覆盖 / 先解释闭环反馈 / 先解释拍板项”。

### 5.3 page_design 下沉规则

建议将 page_design 拆成：

1. `global_design_defaults`：全局共性约束，只写一次；
2. `page_design_overrides`：每页只写本页偏离项和独有设计决策。

每页必须至少包含：

- 本页主视觉结构；
- 本页红色锚点原因；
- 本页区域比例或主图占比；
- 本页图表不得退化的具体形态；
- 本页与其他页不同的设计动作。

## 6. 建议阶段

### Phase 0：评审与规则冻结

产出：

- `project/review/review_reports/AI4MBSE_four_page_template_stamp_feasibility_review_v0.1.md`
- `project/review/patch_proposals/anti_template_stamp_gate_patch_v0.1.md`

目标：冻结规则，不直接改 Skill。

### Phase 1：最小资产落地

修改范围控制在 eval/prompts/core：

- 新增 `eval/template_stamp_detection.md`；
- 新增或扩展 acceptance checklist；
- 修改 `prompts/deck_spec_generation.md`；
- 修改 `core/output_contracts.md`；
- 修改 `eval/visual_scorecard.md`。

验收：用 P4/P7/P8/P14 旧交付包回归，必须能检出当前问题。

### Phase 2：重生成四页对照样例

基于新规则重新生成 P4/P7/P8/P14：

- `core_judgement` 必须有增量；
- `chart_visual_boundary` 每页不同；
- `visual_notes` 拆为全局默认 + 页面偏离项；
- `page_design` 不再重复 7 段固定模板。

验收：生成前后对比报告，确认字段差异化提升且不破坏华为风格一致性。

### Phase 3：沉淀为稳定版本

若 Phase 2 通过：

- 升级版本到 `v0.4.0-anti-template-stamp-gate`；
- 同步 README / CHANGELOG / VERSION / INDEX / PACKAGE_MANIFEST；
- 记录回归测试结果。

## 7. 风险与边界

- 不应把所有重复都判失败。页脚、基础色彩、安全边距、通用负面风格边界可以重复。
- 不应让差异化变成“为了不同而不同”。字段差异必须来自页面论证任务、图表类型、风险边界和受众动作。
- 不应恢复 `page_render_spec` 或 `normalized_render_model`。本次是内容/设计契约质量门禁，不是渲染中间层。

## 8. 推荐动作

建议先进入 Phase 0 + Phase 1：生成 patch proposal，并在不修改正式 Skill 的前提下设计最小规则；待确认后再实际落地到 `skills/huawei_ppt_master`。
