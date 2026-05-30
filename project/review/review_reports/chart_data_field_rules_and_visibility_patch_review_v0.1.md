# chart_data 字段通则与字段可见性 patch v0.1 可行性评审

## 1. 评审对象

- Patch proposal：`project/review/patch_proposals/chart_data_field_rules_and_visibility_patch_v0.1.md`
- 当前 Skill 版本：`v0.4.0-anti-template-stamp-gate`
- 评审范围：方案可行性、与 v0.4.0 规则兼容性、角色 C 生成 PPT 图片的落地价值、是否存在 DSL / page_render_spec 复活风险。

## 2. 总体结论

结论：**建议有条件合入**。

评分：**91 / 100**。

一句话判断：这是一个轻量但必要的补丁，问题真实、边界清晰、落点准确，能解决角色 C 把 `group` 等逻辑字段误渲染为页面可见标签的问题；但落地前建议补齐 4 个小修订，避免“logic-only 字段”与“可见分组标题 / edge label / swimlane lane name”等字段边界再次混淆。

## 3. 可行性判断

### 3.1 技术可行性：高

本 patch 不新增文件，只修改已有字段说明、图表规则和 deck_spec 生成提示词，实施成本低。

建议修改点均真实存在：

- `skills/huawei_ppt_master/core/deck_spec_field_dictionary.md`
- `skills/huawei_ppt_master/templates/chart_patterns.md`
- `skills/huawei_ppt_master/prompts/deck_spec_generation.md`
- 版本同步文件

### 3.2 与 v0.4.0 的兼容性：高

v0.4.0 已明确 `chart_data` 结构骨架允许相似，仅判断语义内容是否机械重复；本 patch 进一步补充字段可见性与关系语义归位，属于 v0.4.0 的自然延伸。

兼容点：

- 不改变 `deck_spec.json` 顶层结构；
- 不新增 `chart_type` 或 `layout_pattern`；
- 不新增 `relation_type`、坐标、shape、线宽等 DSL 字段；
- 继续把关系语义放在 `chart_semantic_mapping`；
- 与 `field_differentiation_rules.md` 中“chart_data 结构骨架允许相似”的边界一致。

### 3.3 对角色 C 的价值：高

当前 `AI_MBSE_v040` 交付物里已实际出现 `group` 字段，例如：

- `group: 生命周期`
- `group: AI介入`
- `group: 输入`
- `group: 语义底座`
- `group: 生成`
- `group: 仿真`
- `group: AI`

这些字段对 C 来说有分组价值，但如果被原样渲染为节点标签，会造成“逻辑字段泄漏”。patch 的 `logic-only` 约定能直接降低这类渲染偏差。

## 4. 主要优点

1. **问题定义准确**  
   抓住了角色 C 的真实问题：字段能消费，不代表字段都该上屏。

2. **边界克制**  
   明确 chart_data 只承载“拓扑 + 内容”，关系语义交给 `chart_semantic_mapping`，避免把 deck_spec 推向渲染 DSL。

3. **规则轻量**  
   不是给 17 个 chart_type 分别写字段规则，而是抽象成三类：拓扑/管道字段、显示内容字段、逻辑字段。

4. **与 v0.4.0 可衔接**  
   v0.4.0 解决“字段机械套版”，本 patch 解决“字段可见性与关系语义归位”，二者互补。

5. **回归用例方向正确**  
   RT-01 group 不上屏、RT-02 关系语义归位、RT-03 防契约膨胀、RT-04 label 短语化，覆盖了核心风险。

## 5. 需修订问题清单

| ID | 严重度 | 问题 | 建议 |
|---|---|---|---|
| R-01 | P1 | `group` 一律 logic-only 是正确方向，但需要说明“若需要可见分组标题，应使用什么字段”。proposal 有提到 display_text/label，但不够具体 | 增加规则：可见分组标题优先用 `label/name/headline` 或 `display_text`，不得复用 `group`；若是泳道图，`lane.name` 可见，`node.group` 不可见 |
| R-02 | P1 | `edges.label` 与“关系语义不进 chart_data”容易被误读。边上短标签本身是可见内容，但方向/层级/闭环等语义应在 `chart_semantic_mapping` | 增加区分：`edges.label` 可承载短动作词，如“回写/验证/编译”；不得承载复杂关系解释；复杂关系写入 `chart_semantic_mapping.main_visual_logic` |
| R-03 | P2 | 只改 `deck_spec_field_dictionary.md`、`chart_patterns.md`、`deck_spec_generation.md` 可能还不够，`output_contracts.md` 也应有一句强门禁，否则执行触点偏弱 | 在 `core/output_contracts.md` 的 4.3 deck_spec 强门禁增加一条：logic-only 字段不得上屏，关系语义不得新增 chart_data 字段 |
| R-04 | P2 | 版本号建议不再用泛化 `v0.4.x`，当前 v0.4.0 已稳定发布，落地应明确为小版本 | 建议目标版本设为 `v0.4.1-chart-data-visibility` |
| R-05 | P3 | RT-04 只说 label 长句 WARN，但没有给长度或判据 | 建议加轻量判据：节点 `label/name` 建议 ≤12 汉字或 ≤2 个短语；长解释放 `description` / `speaker_notes` / `chart_semantic_mapping` |
| R-06 | P3 | `section` 被列为 logic-only，但又允许页眉小标签例外；这个例外需要更明确 | 说明 `section` 只可作为页眉/章节标签弱显示，不得作为主体节点或卡片标题渲染 |

## 6. 建议修订后的最小落点

### 6.1 必改文件

1. `core/deck_spec_field_dictionary.md`  
   新增 `chart_data 字段通则与可见性约定`，但需吸收 R-01/R-02/R-06。

2. `templates/chart_patterns.md`  
   在 chart_type 与 layout_pattern 边界附近增加引用说明：字段可见性看字段字典；关系语义看 `chart_semantic_mapping`。

3. `prompts/deck_spec_generation.md`  
   在生成检查中增加 logic-only 与关系语义归位检查。

4. `core/output_contracts.md`  
   增加一条 deck_spec 强门禁：`chart_data` 逻辑字段不得作为可见标签；不得新增 `relation_type` 等关系字段。

### 6.2 建议同步文件

- `README.md`
- `VERSION.md`
- `CHANGELOG.md`
- `INDEX.md`
- `QUICK_INDEX.md`
- `PACKAGE_MANIFEST.md`

## 7. 与 page_render_spec / normalized_render_model 的边界

本 patch 没有复活二者，原因：

- 不定义坐标、字号、线宽、shape 参数；
- 不引入中间渲染模型；
- 不要求 C 按像素级规则执行；
- 只定义字段语义、字段可见性和关系语义归属。

但要警惕：如果后续继续增加 `relation_type`、`edge_style`、`position`、`anchor`、`x/y`、`layer_index` 等字段，就会重新滑向渲染 DSL。当前 proposal 明确禁止 `relation_type`，这是对的。

## 8. 回归用例建议补强

在原有 RT-01~RT-04 基础上，建议新增：

### RT-05：edge label 可见但不承载复杂关系

构造：

```json
{"from":"A","to":"B","label":"回写"}
```

预期：

- `label=回写` 可上屏作为短箭头标签；
- “为什么回写、回写形成什么闭环”必须在 `chart_semantic_mapping.main_visual_logic` 中说明。

### RT-06：swimlane lane.name 可见，node.group 不可见

预期：

- `lane.name` 可作为泳道标题；
- `node.group` 只用于内部归类，不直接上屏。

### RT-07：section 只弱显示为页眉

预期：

- `section` 可在页眉弱显示；
- 不得作为主体卡片标题或节点标签。

## 9. 合入建议

建议：**有条件合入**。

合入前建议先产出 `chart_data_field_rules_and_visibility_patch_v0.2.md`，吸收：

1. 明确可见分组字段与 logic-only `group` 的差异；
2. 明确 `edges.label` 是可见短动作词，不是复杂关系语义；
3. 增加 `core/output_contracts.md` 强门禁落点；
4. 目标版本明确为 `v0.4.1-chart-data-visibility`；
5. 补充 label 长度/短语化轻量判据。

若 v0.2 修订完成，可进入 Phase 1 小版本落地；不建议直接按 v0.1 落地。
