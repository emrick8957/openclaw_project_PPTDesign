# huawei_ppt_master v0.3.7 deck_spec 证明契约落地报告

## 1. 背景

用户确认启动 deck_spec.json 优化落地，目标是新增字段明确：本页唯一核心判断是什么、主图表必须证明什么、chart_type 的视觉表达边界是什么。

此次升级将 deck_spec 从“页面内容和图表类型描述”增强为“页面判断 + 图表证明目标 + 图表视觉边界”的证明契约。

## 2. 已修改资产

1. `SKILL.md`
   - 版本升级为 `0.3.7-deck-spec-proof-contract`。

2. `core/output_contracts.md`
   - deck_spec 每页新增：
     - `core_judgement`
     - `chart_proof_goal`
     - `chart_visual_boundary`
   - 增加字段边界和强门禁。

3. `prompts/deck_spec_generation.md`
   - 要求先生成 `core_judgement`，再生成 `chart_proof_goal`，最后选择 `chart_type` / `layout_pattern`。
   - 新增图表证明契约检查。

4. `core/generation_workflow.md`
   - 同步 Step 6.5 deck_spec 字段映射检查顺序。

5. `templates/chart_patterns.md`
   - 新增 deck_spec 图表证明契约；
   - 为常见 `chart_type` 增加 proof_goal 和 visual_boundary 示例；
   - 增加图表证明失败条件。

6. `eval/visual_scorecard.md`
   - 新增 v0.3.7 deck_spec 证明契约检查；
   - 新增一票降级项：无唯一 core_judgement、图表未证明 chart_proof_goal、chart_type 与证明目标不匹配、违反 chart_visual_boundary。

7. `eval/acceptance_checklist.md`
   - 新增 deck_spec 证明契约验收项。

8. `README.md`、`INDEX.md`、`PACKAGE_MANIFEST.md`、`VERSION.md`、`CHANGELOG.md`
   - 同步版本与资产说明。

## 3. 新字段定义

```json
{
  "core_judgement": "本页唯一核心判断",
  "chart_proof_goal": "本页主图表必须证明什么",
  "chart_visual_boundary": [
    "不得退化为什么",
    "必须体现什么",
    "红色/主次/结构如何控制"
  ]
}
```

## 4. 自检结果

- 未新增 `chart_type` 枚举；
- 未新增 `layout_pattern` 枚举；
- 未改变默认完整交付链路；
- 新字段只增强 deck_spec 证明约束，不替代页面设计说明；
- 与 v0.3.6 的 `visual_boundary` / `page_type_gate` 兼容；
- 视觉自检和验收清单已同步。

## 5. 后续使用建议

后续生成 deck_spec 时，每页必须先写 `core_judgement`，再写 `chart_proof_goal`，再选 `chart_type`。如果某个 chart_type 无法证明该目标，应换图表或拆页，不允许用装饰性图表硬凑。
