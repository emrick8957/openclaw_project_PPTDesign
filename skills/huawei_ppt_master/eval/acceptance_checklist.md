# 验收清单

## 1. 内容质量

- 是否有明确汇报对象；
- 是否有总体叙事主线；
- 每页是否有明确核心结论；
- 标题是否为结论型标题；
- 是否有图表建议；
- 是否有页面设计说明；
- 是否有章节分组；
- 是否同时包含问题、判断、路径、风险和建议；
- 是否对高层有决策价值。
- 是否避免空泛口号；

## 2. 华为风格

- 是否克制商务；
- 是否红黑灰白为主；
- 是否工程化表达；
- 是否避免口号化；
- 是否保留页脚、页码、Confidential 等正式元素。
- 是否版式克制
- 是否信息密度可控；
- 是否图表可执行；
- 是否红色使用克制，单页主红色锚点不超过 1-2 个；
- 是否避免正文页厚重红色压底条；
- 是否卡片、表格、流程/闭环图组件风格统一；
- 是否页脚位置、字号、颜色、基线一致。

## 3. 页面设计

- 是否为每页提供可执行版式说明；
- 是否选用了合适的 `visual_patterns`；
- 是否避免满屏文字；
- 是否说明图表承载的信息；
- 是否可转为 deck_spec.json。

## 4. 主题防污染

- 非 AI 算力主题是否无故出现昇腾、英伟达、CUDA、CANN、GPU/NPU 等词；
- 是否把专属主题结构套用到无关主题；
- 是否符合当前主题的业务语境。

## 5. 不合格条件

出现以下任一项，必须重写：

- 页标题只是名词；
- 无故引入不相关主题术语；
- 大量空泛口号；
- 没有图表建议；
- 页面设计说明不可执行；
- 没有风险或决策收口。
- 页面视觉明显偏重：红色过量、卡片同权、表格过密、底部红条压页面，且未在设计说明中给出降噪策略。

## 6 deck_spec 字段失败条件
出现以下任一项，直接判定 deck_spec 不合格，必须重写：

- `chart_type` 不在 `templates/chart_patterns.md` 枚举内；
- `layout_pattern` 不在 `visual_patterns/layout_library.md` 枚举内；
- `chart_type == layout_pattern`；
- 把 layout 名称写入 `chart_type`；
- 把 chart 名称写入 `layout_pattern`；
- 无精确匹配时直接发明新枚举值。

## 7. 高断言页面证据门禁
对于外部格局判断、竞品对比、优势/短板诊断、资源建议等高断言页面：
- 如无公开研究、内部材料或案例支撑，必须使用方向性表述；
- 不得把推测写成已证实事实；
- 必须在 `data_gaps` 中明确缺口；
- 必要时在结论中加入“当前判断”“初步判断”“待补材料后确认”等降级措辞。


## 8. deck_spec 证明契约

- 每页是否包含 `core_judgement`、`chart_proof_goal`、`chart_visual_boundary`；
- `core_judgement` 是否唯一、清晰、可被标题/结论/正文/图表共同支撑；
- `chart_proof_goal` 是否直接服务 `core_judgement`；
- `chart_type` 是否适合证明 `chart_proof_goal`；
- `chart_visual_boundary` 是否具体、可执行，且能防止图表退化为装饰、清单、图片墙、大表格或并列计划。


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


## 10. chart_data 字段可见性门禁

- `chart_data` 中 logic-only 字段是否未作为可见标签上屏，包括 `group`、`emphasis`、`source_status`；
- 若需要可见分组标题，是否使用 `label`、`name`、`headline`、`display_text`、`lane.name`、`layer.name` 或 `stage.name`，而非复用 `group`；
- `edges.label` 是否仅承载短动作词或短关系词；
- 复杂方向、同层对应、层级支撑、闭环回写等关系语义是否进入 `chart_semantic_mapping`；
- `label` / `name` / `headline` / `items` / `edges.label` 是否短语化，长解释是否放入 `description`、`speaker_notes` 或 `chart_semantic_mapping`；
- `chart_data` 内是否未新增 `relation_type`、`edge_style`、`position`、`anchor`、`x/y`、`layer_index` 等关系或渲染 DSL 字段。

出现以下任一项，必须重写：

- `group`、`emphasis`、`source_status` 等 logic-only 字段被字面上屏；
- `edges.label` 被写成长句或复杂关系解释；
- 复杂关系语义只塞进 `label`，未进入 `chart_semantic_mapping`；
- `chart_data` 内出现 `relation_type` 或坐标/shape/edge_style 等 DSL 字段。
