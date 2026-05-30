# 防机械套版门禁 Phase 1 落地报告 v0.1

## 1. 背景

用户确认 `anti_template_stamp_gate_patch_v0.2.md` 评审通过，并要求启动 Phase 1 落地。

本次按 v0.2 proposal 将防机械套版门禁正式落入 `skills/huawei_ppt_master`，目标版本：

`v0.4.0-anti-template-stamp-gate`

## 2. 新增正式资产

| 文件 | 作用 |
|---|---|
| `skills/huawei_ppt_master/core/field_differentiation_rules.md` | 字段差异化单一真相源，定义允许重复字段、必须逐页有设计增量字段、可半重复字段，以及 `core_judgement` / `chart_proof_goal` / `chart_visual_boundary` 的 PASS/FAIL 特征和正反例 |
| `skills/huawei_ppt_master/eval/template_stamp_detection.md` | 模板印章检测门禁，定义混合阈值模型、必检字段引用、自检输出格式和 FAIL 处理规则 |

## 3. 修改正式资产

| 文件 | 修改内容 |
|---|---|
| `SKILL.md` | 升级版本到 `0.4.0-anti-template-stamp-gate`；强制读取字段差异化规则和模板印章检测；将模板印章检测纳入自检门禁 |
| `core/output_contracts.md` | 增加字段差异化要求和 deck_spec 强门禁 |
| `core/deck_spec_field_dictionary.md` | 补充 `core_judgement` / `chart_proof_goal` / `chart_visual_boundary` / `visual_notes` 的差异化职责说明 |
| `prompts/deck_spec_generation.md` | 要求生成后执行模板印章检测，并在 self_check 输出检测结果 |
| `eval/acceptance_checklist.md` | 新增防机械套版验收门禁 |
| `eval/visual_scorecard.md` | 新增模板印章一票降级项 |
| `templates/visual_rules.md` | 新增通用视觉规则下沉要求与每页独立可读视图 |
| `templates/wording_rules.md` | 新增防骨架填词规则 |
| `README.md` / `VERSION.md` / `CHANGELOG.md` / `INDEX.md` / `QUICK_INDEX.md` / `PACKAGE_MANIFEST.md` | 同步 v0.4.0 版本、资产说明和包清单 |

## 4. 核心规则落点

### 4.1 混合阈值模型

- N<=3：两两比较；
- N>=4：`repeat_threshold=max(3,ceil(N*0.5))`；
- 达阈值重复：FAIL；
- 未达阈值但重复明显：WARN；
- 页脚、基础配色、安全边距、全局负面风格边界等白名单字段不参与 FAIL 判定。

### 4.2 语义判据

已为以下字段落地 PASS/FAIL 特征与正反例：

- `core_judgement`；
- `chart_proof_goal`；
- `chart_visual_boundary`。

### 4.3 page_design 兼容

允许通用视觉规则下沉为：

```text
global_design_defaults + page_design_overrides
```

但必须保留每页独立可读视图：

```text
page_design_view(Pn) = global_design_defaults + page_design_overrides(Pn)
```

## 5. 验证结果

### 5.1 资产存在性与引用检查

已验证以下内容存在：

- `SKILL.md` 版本为 `0.4.0-anti-template-stamp-gate`；
- `SKILL.md` 引用 `core/field_differentiation_rules.md`；
- `SKILL.md` 引用 `eval/template_stamp_detection.md`；
- `core/output_contracts.md` 包含模板印章检测门禁；
- `prompts/deck_spec_generation.md` 包含生成后模板印章检测要求；
- `eval/acceptance_checklist.md` 包含 `## 9. 防机械套版门禁`；
- `eval/visual_scorecard.md` 包含 `## N. 模板印章一票降级项`；
- `PACKAGE_MANIFEST.md` 包含两个新增资产。

### 5.2 旧四页 dry-run 回归

回归报告：

`project/review/review_reports/anti_template_stamp_gate_phase1_dry_run_v0.1.md`

对象：

`project/work/AI4MBSE_P4_P7_P8_P14_delivery/deck_spec.json`

结果：

- N=4；
- repeat_threshold=3；
- FAIL：6 项；
- WARN：5 项；
- ALLOW/WARN：1 项。

结论：旧四页交付包会被 v0.4.0 门禁识别为不合格，符合 RT-00 预期。

## 6. 边界

- 未恢复 `page_render_spec`；
- 未恢复 `normalized_render_model`；
- 未新增渲染 DSL；
- 未要求所有字段都差异化；
- 保留华为风格一致性，只约束必须承载逐页设计决策的字段。

## 7. 后续建议

建议下一步使用 v0.4.0 规则重生成 P4/P7/P8/P14 作为 Phase 2 对照样例，验证：

- 旧样例 FAIL；
- 新样例 PASS；
- 字段差异化提升；
- 华为风格一致性不被破坏。
