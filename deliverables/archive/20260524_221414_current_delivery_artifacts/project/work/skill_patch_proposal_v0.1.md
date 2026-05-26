# Huawei PPT Skill Patch Proposal v0.1

目标：强化 `chart_type` / `layout_pattern` 字段边界，确保后续稳定遵循：
1. 有匹配时必须优先使用已定义枚举；
2. 无精确匹配时必须按统一降级规则处理；
3. deck_spec 生成前必须经过字段门禁检查。

---

## 一、建议修改文件

1. `skills/huawei_ppt_master/core/output_contracts.md`
2. `skills/huawei_ppt_master/core/generation_workflow.md`
3. `skills/huawei_ppt_master/SKILL.md`
4. `skills/huawei_ppt_master/eval/acceptance_checklist.md`
5. （可选增强）`skills/huawei_ppt_master/templates/chart_patterns.md`

---

## 二、核心问题

### 问题 1：示例仍会误导字段混用
当前 `output_contracts.md` 和 `SKILL.md` 中 deck_spec 示例里，`chart_type` 仍出现过非标准图表枚举写法，容易让生成阶段把版式名或历史错误名写进 `chart_type`。

### 问题 2：规则存在，但还是偏“说明型”
当前 skill 已说明：
- `chart_type` 和 `layout_pattern` 不得混用；
- `chart_type` 应来自 `templates/chart_patterns.md`；
- `layout_pattern` 应来自版式库。

但这些规则仍缺少“强门禁”和“无匹配时唯一合法处理路径”。

### 问题 3：生成流程未前置字段合法性检查
当前检查更多放在验收阶段，没有在生成 `deck_spec.json` 的当下强制阻断非法值。

---

## 三、建议改法

### Patch A：修正 `core/output_contracts.md`

#### A1. 替换 deck_spec 示例中的错误 `chart_type`
把示例中的：
- `chart_type: "chapter_agenda"`

改为：
- `chart_type: "key_findings_cards"`（若示例为总览卡片页）

#### A2. 新增强门禁规则
建议在 `4.2 deck_spec 字段边界补充` 后追加：

```md
### 4.3 deck_spec 强门禁
生成 `deck_spec.json` 时，必须先完成以下检查：

1. `chart_type` 必须严格取自 `templates/chart_patterns.md` 已定义枚举；
2. `layout_pattern` 必须严格取自 `visual_patterns/layout_library.md` 已定义枚举；
3. 若 `chart_type == layout_pattern`，直接判定失败，必须重选；
4. 若 `chart_type` 命中 layout 黑名单，直接判定失败；
5. 若 `layout_pattern` 命中 chart 黑名单，直接判定失败；
6. 若字段不在合法枚举内，不得输出最终 `deck_spec.json`；
7. 必须先确定 `chart_type`，再确定 `layout_pattern`，不得反向从版式名推导图表名并直接复用同名值。
```

#### A3. 明确“无精确匹配时”的唯一合法处理
把当前：
- 选择最接近的通用 chart_type
- 选择最接近的通用 layout_pattern
- 差异写入 visual_notes
- 不得自造新枚举值

加强为：

```md
#### 4.4 无精确匹配时的唯一合法处理
如果设想的图表或版式没有精确匹配项，必须按以下顺序处理：

1. 优先选择最接近的通用 `chart_type`；
2. 再选择最接近的通用 `layout_pattern`；
3. 将差异、特化要求、视觉补充说明写入 `visual_notes`；
4. 不得自造新的 `chart_type` 或 `layout_pattern` 枚举值；
5. 如确实需要新增模式，只能在评审/优化环节输出 patch proposal，不得直接写入正式交付物。
```

---

### Patch B：加强 `core/generation_workflow.md`

在 Step 6 和 Step 7 之间新增一个独立步骤：

```md
## Step 6.5：deck_spec 字段映射检查
在输出 `deck_spec.json` 前，必须完成以下动作：

1. 先判断该页主信息表达方式，确定 `chart_type`；
2. 再判断页面区域组织方式，确定 `layout_pattern`；
3. 对照 `templates/chart_patterns.md` 检查 `chart_type` 是否为合法枚举；
4. 对照 `visual_patterns/layout_library.md` 检查 `layout_pattern` 是否为合法枚举；
5. 若两者同名或字段越界，必须重写该页 deck_spec；
6. 若无精确匹配，按“最接近通用类型 + visual_notes 补充”的规则处理，不得自造新值。
```

这样可以把检查前置，不要等到最后才发现字段混用。

---

### Patch C：加强 `SKILL.md`

建议在“强制读取顺序”后，或者“deck_spec.json”章节后，追加一个明确约束段：

```md
### deck_spec 字段选择硬规则
生成 `deck_spec.json` 时，必须遵守：

1. `chart_type` 先选，`layout_pattern` 后选；
2. `chart_type` 只允许来自 `templates/chart_patterns.md`；
3. `layout_pattern` 只允许来自 `visual_patterns/layout_library.md`；
4. 不允许把页面版式名写入 `chart_type`；
5. 不允许把图表类型名写入 `layout_pattern`；
6. 如果设想的表达方式没有精确匹配，必须降级到最接近的通用类型，并在 `visual_notes` 中补充，不得创造新枚举；
7. 若字段边界不清，优先保证合法枚举和值域正确，再通过 `visual_notes` 补细节。
```

---

### Patch D：加强 `eval/acceptance_checklist.md`

当前已有检查项，但建议再补一条“必须重写”的硬条件：

```md
## 6.1 deck_spec 字段失败条件
出现以下任一项，直接判定 deck_spec 不合格，必须重写：

- `chart_type` 不在 `templates/chart_patterns.md` 枚举内；
- `layout_pattern` 不在 `visual_patterns/layout_library.md` 枚举内；
- `chart_type == layout_pattern`；
- 把 layout 名称写入 `chart_type`；
- 把 chart 名称写入 `layout_pattern`；
- 无精确匹配时直接发明新枚举值。
```

---

### Patch E（可选增强）：补“推荐映射速查表”

建议在 `templates/chart_patterns.md` 末尾再补一个“常用页型 → 推荐 chart_type / layout_pattern”速查表，降低后续误选概率。

建议新增内容：

```md
## 7. 常用页型推荐映射速查表

| 页面意图 | 推荐 chart_type | 推荐 layout_pattern |
|---|---|---|
| 高层总判断页 | `key_findings_cards` | `executive_summary_dashboard` |
| 四象限优先级页 | `priority_matrix` / `quadrant_matrix` | `four_quadrant_judgement` |
| 多维竞品对比页 | `comparison_table` | `insight_panel_with_chart` / `two_column_comparison` |
| 趋势判断页 | `trend_curve` | `trend_curve_with_strategy` |
| 闭环诊断页 | `value_chain_loop` | `insight_panel_with_chart` / `stack_architecture_with_right_insights` |
| 路线图页 | `roadmap_timeline_chart` | `roadmap_timeline` |
| 风险页 | `risk_matrix` | `risk_decision_matrix` |
| 决策页 | `decision_table` | `risk_decision_matrix` |
| 架构流转页 | `architecture_flow_diagram` | `stack_architecture_with_right_insights` |
```

---

## 四、优先级建议

### P0（必须马上改）
1. 修 `output_contracts.md` / `SKILL.md` 中的旧示例；
2. 在 `generation_workflow.md` 增加生成前字段门禁；
3. 在 `acceptance_checklist.md` 增加 deck_spec 失败条件。

### P1（强烈建议）
4. 在 `SKILL.md` 增加 deck_spec 硬规则；
5. 在 `chart_patterns.md` 补充速查表。

---

## 五、预期收益

改完后，Skill 会更稳定满足：

1. **有匹配时必须遵循已定义枚举**，不再把版式名误写到 `chart_type`；
2. **无匹配时有唯一合法处理路径**，统一降级到最接近通用类型并写入 `visual_notes`；
3. 生成阶段就能拦截字段越界，而不是等到用户指出问题；
4. 后续 deck_spec 可执行性更高，更利于 builder 稳定消费。

---

## 六、当前结论

Skill **有明确优化空间**，而且优先级很高。  
这不是补充说明的问题，而是要把“字段边界”从软规则提升为**生成门禁 + 验收门禁**。