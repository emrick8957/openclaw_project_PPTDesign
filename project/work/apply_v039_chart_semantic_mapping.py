from pathlib import Path

# 1) output_contracts
p=Path('skills/huawei_ppt_master/core/output_contracts.md')
t=p.read_text(encoding='utf-8')
if '`chart_semantic_mapping`' not in t:
    t=t.replace(
'''- `chart_visual_boundary`：本页主图表的视觉表达边界。通常为 3~5 条短约束，说明不得画偏成什么、必须体现什么、红色/主次/结构应如何控制。''',
'''- `chart_visual_boundary`：本页主图表的视觉表达边界。通常为 3~5 条短约束，说明不得画偏成什么、必须体现什么、红色/主次/结构应如何控制。
- `chart_semantic_mapping`：本页主图表的语义解释映射。用于说明主图表如何证明 `chart_proof_goal`，避免图表沦为装饰、模板或误读。`trend_curve` 必须输出，`quadrant_matrix`、`roadmap_timeline_chart`、`architecture_flow_diagram`、`layered_stack_diagram`、`value_chain_loop`、`swimlane_process`、`ecosystem_relationship_map` 等高语义风险图表建议输出。''')
    t=t.replace(
'''- `chart_visual_boundary` 管“图表不能怎么画 / 视觉表达边界”；
- `chart_type` 仍只允许使用 `templates/chart_patterns.md` 中的合法枚举；''',
'''- `chart_visual_boundary` 管“图表不能怎么画 / 视觉表达边界”；
- `chart_semantic_mapping` 管“图表如何被阅读、如何证明、坐标/阶段/节点/洞察栏分别代表什么”；
- `chart_type` 仍只允许使用 `templates/chart_patterns.md` 中的合法枚举；''')
    t=t.replace(
'''
  "chart_visual_boundary": [
    "不得画成无主次的四张并列卡片",
    "必须突出唯一主判断卡和支撑卡层级",
    "红色只能用于核心判断或关键风险，不能多处抢焦点"
  ],
  "display_text": [''',
'''
  "chart_visual_boundary": [
    "不得画成无主次的四张并列卡片",
    "必须突出唯一主判断卡和支撑卡层级",
    "红色只能用于核心判断或关键风险，不能多处抢焦点"
  ],
  "chart_semantic_mapping": {
    "chart_reading_intent": "读者看完图后应形成的唯一判断",
    "main_visual_logic": "主图通过主次、方向、分层、对比、趋势或闭环证明判断",
    "axis_semantics": {},
    "stage_or_node_meaning": {},
    "insight_panel_logic": [],
    "forbidden_visualization": ["不得把图表画成装饰性模板"]
  },
  "display_text": [''')
    t=t.replace(
'''8. 每页必须包含 `core_judgement`、`chart_proof_goal`、`chart_visual_boundary`。
9. `chart_proof_goal` 必须能直接支撑 `core_judgement`，否则判定该页图表论证目标不成立。
10. `chart_visual_boundary` 必须为数组，建议 3~5 条，不得为空泛口号。''',
'''8. 每页必须包含 `core_judgement`、`chart_proof_goal`、`chart_visual_boundary`。
9. 当 `chart_type=trend_curve` 时，必须包含 `chart_semantic_mapping`；其他高语义风险图表建议包含该字段。
10. `chart_semantic_mapping` 必须服务 `chart_proof_goal`，不得另起一套判断。
11. `chart_proof_goal` 必须能直接支撑 `core_judgement`，否则判定该页图表论证目标不成立。
12. `chart_visual_boundary` 必须为数组，建议 3~5 条，不得为空泛口号。''')
p.write_text(t, encoding='utf-8')

# 2) prompt
p=Path('skills/huawei_ppt_master/prompts/deck_spec_generation.md')
t=p.read_text(encoding='utf-8')
if 'chart_semantic_mapping' not in t:
    t=t.replace(
'''2. 每页包含 slide_no、type、title、conclusion、core_judgement、chart_proof_goal、chart_visual_boundary、body/display_text、chart_type、chart_data、layout_pattern、speaker_notes、need_compression；''',
'''2. 每页包含 slide_no、type、title、conclusion、core_judgement、chart_proof_goal、chart_visual_boundary、chart_semantic_mapping（按触发规则）、body/display_text、chart_type、chart_data、layout_pattern、speaker_notes、need_compression；''')
    t=t.replace(
'''11. `chart_visual_boundary` 必须包含 3~5 条短约束，说明该图表不得退化为什么、必须体现什么、红色和主次如何控制。''',
'''11. `chart_visual_boundary` 必须包含 3~5 条短约束，说明该图表不得退化为什么、必须体现什么、红色和主次如何控制。
12. 当 `chart_type=trend_curve` 时，必须输出 `chart_semantic_mapping`；当图表为四象限、路线图、架构流转、分层架构、闭环、泳道、生态关系等高语义风险图表时，建议输出该字段。
13. `chart_semantic_mapping` 必须包含 6 个核心字段：`chart_reading_intent`、`main_visual_logic`、`axis_semantics`、`stage_or_node_meaning`、`insight_panel_logic`、`forbidden_visualization`。''')
    t=t.replace(
'''- `chart_visual_boundary` 是否具体、可执行，且不与 `visual_notes` 冲突；
- 若图表无法证明本页判断，应优先调整 `chart_type` 或拆页，不得用装饰性图表硬凑。''',
'''- `chart_visual_boundary` 是否具体、可执行，且不与 `visual_notes` 冲突；
- 如已触发 `chart_semantic_mapping`，检查其是否解释了主图如何证明 `chart_proof_goal`，坐标/阶段/节点/洞察栏语义是否成立；
- 若图表无法证明本页判断，应优先调整 `chart_type` 或拆页，不得用装饰性图表硬凑。''')
p.write_text(t, encoding='utf-8')

# 3) field dictionary
p=Path('skills/huawei_ppt_master/core/deck_spec_field_dictionary.md')
t=p.read_text(encoding='utf-8')
if '`chart_semantic_mapping`' not in t:
    t=t.replace(
'''| `chart_visual_boundary` | array[string] | 图表视觉边界 | 用于约束主图不能画偏、红色如何控制、主次如何呈现 |''',
'''| `chart_visual_boundary` | array[string] | 图表视觉边界 | 用于约束主图不能画偏、红色如何控制、主次如何呈现 |
| `chart_semantic_mapping` | object | 图表语义解释映射 | 说明主图表如何证明 `chart_proof_goal`；`trend_curve` 必须输出，其他高语义风险图表建议输出 |''')
p.write_text(t, encoding='utf-8')

# 4) chart_patterns add semantic section before 7.3 failure conditions
p=Path('skills/huawei_ppt_master/templates/chart_patterns.md')
t=p.read_text(encoding='utf-8')
if '### 7.3 chart_semantic_mapping 语义解释映射' not in t:
    block='''### 7.3 chart_semantic_mapping 语义解释映射

`chart_semantic_mapping` 用于说明主图表如何证明 `chart_proof_goal`，避免图表沦为装饰、模板或误读。它不是渲染 DSL，不规定坐标、字号或 shape 参数；它是 deck_spec 中面向角色 C 的图表语义解释层。

#### 7.3.1 触发规则

- `chart_type = trend_curve` 时，必须输出 `chart_semantic_mapping`。
- 以下高语义风险图表建议输出：`quadrant_matrix`、`roadmap_timeline_chart`、`architecture_flow_diagram`、`layered_stack_diagram`、`value_chain_loop`、`swimlane_process`、`ecosystem_relationship_map`。
- 普通 `key_findings_cards`、`comparison_table` 可按页面复杂度选择是否输出。

#### 7.3.2 字段结构

```json
{
  "chart_semantic_mapping": {
    "chart_reading_intent": "读者看完图后必须得出的判断",
    "main_visual_logic": "主图通过什么视觉关系证明判断",
    "axis_semantics": {},
    "stage_or_node_meaning": {},
    "insight_panel_logic": [],
    "forbidden_visualization": []
  }
}
```

#### 7.3.3 六个核心字段

| 字段 | 解决的问题 |
|---|---|
| `chart_reading_intent` | 图表到底要让读者得出什么判断 |
| `main_visual_logic` | 主图应该怎么证明判断 |
| `axis_semantics` | 坐标轴、矩阵、趋势语义是否成立 |
| `stage_or_node_meaning` | 阶段、节点、卡片不是空标签 |
| `insight_panel_logic` | 右侧洞察栏解释主图，而非备注 |
| `forbidden_visualization` | 明确禁止误画、乱画、越界画 |

#### 7.3.4 `trend_curve` 必填语义要求

当 `chart_type=trend_curve` 时，必须说明：

1. 这条趋势到底证明增长、下降、拐点、成熟度变化还是阶段转换；
2. x 轴是否代表时间、阶段、成熟度或其他序列，不能伪造精确年份；
3. y 轴是否有真实度量，若没有真实数据，应标注为趋势/成熟度示意，不得画成精确数值曲线；
4. 拐点、注释和右侧策略解读必须服务同一个 `chart_proof_goal`；
5. 禁止用平滑上升曲线表达未经验证的确定增长。

`trend_curve` 示例：

```json
{
  "chart_type": "trend_curve",
  "chart_semantic_mapping": {
    "chart_reading_intent": "读者应判断：技术演进已从单点工具辅助进入可学习、可解释、可审查的工程闭环阶段。",
    "main_visual_logic": "曲线表达能力成熟度从低到高演进，关键拐点标注语义模型和AI回写机制成为阶段转换条件。",
    "axis_semantics": {
      "x_axis": "阶段序列，不代表精确年份",
      "y_axis": "工程闭环成熟度示意，不代表量化指标"
    },
    "stage_or_node_meaning": {
      "现状": "模型辅助，AI多为孤立应用",
      "转折": "语义模型、仿真和XAI开始接入工程过程",
      "目标态": "模型可学习、可解释、可审查并可回写"
    },
    "insight_panel_logic": [
      "右侧洞察只解释拐点为何成立",
      "策略建议必须从曲线阶段转换推出"
    ],
    "forbidden_visualization": [
      "不得画成无来源的精确增长曲线",
      "不得用大红上升箭头暗示确定收益",
      "不得让右侧洞察变成与曲线无关的备注"
    ]
  }
}
```

'''
    t=t.replace('''### 7.3 失败条件''', block + '### 7.4 失败条件')
    t=t.replace('''## 7. deck_spec 图表证明契约''', '''## 7. deck_spec 图表证明契约''')
p.write_text(t, encoding='utf-8')

# 5) visual_scorecard
p=Path('skills/huawei_ppt_master/eval/visual_scorecard.md')
t=p.read_text(encoding='utf-8')
if 'v0.3.9 chart_semantic_mapping' not in t:
    t += '''

## M. v0.3.9 chart_semantic_mapping 语义映射检查

当 `deck_spec.json` 中出现 `chart_semantic_mapping`，或 `chart_type=trend_curve` 时，必须检查：

- `chart_reading_intent` 是否明确读者看完图后应得出的判断；
- `main_visual_logic` 是否说明主图如何证明 `chart_proof_goal`；
- `axis_semantics` 是否解释坐标轴、矩阵或趋势语义，且没有伪造精确数据；
- `stage_or_node_meaning` 是否说明阶段、节点、卡片的语义，避免空标签；
- `insight_panel_logic` 是否确保右侧洞察解释主图，而不是备注列表；
- `forbidden_visualization` 是否明确禁止误画、乱画、越界画。

### M.1 一票降级项

出现以下任一问题，页面最高 B 档；严重时必须返工：

- `chart_type=trend_curve` 但缺少 `chart_semantic_mapping`；
- 趋势图坐标语义不成立，或把示意趋势画成精确数据；
- `chart_semantic_mapping` 与 `chart_proof_goal` 不一致；
- 阶段、节点或卡片只是空标签，无法支撑页面判断；
- 右侧洞察栏与主图无关，退化为备注列表；
- `forbidden_visualization` 为空或只写泛化口号。
'''
p.write_text(t, encoding='utf-8')

# 6) SKILL version
p=Path('skills/huawei_ppt_master/SKILL.md')
t=p.read_text(encoding='utf-8')
t=t.replace('version: 0.3.8-deck-spec-field-dictionary','version: 0.3.9-chart-semantic-mapping')
p.write_text(t, encoding='utf-8')
