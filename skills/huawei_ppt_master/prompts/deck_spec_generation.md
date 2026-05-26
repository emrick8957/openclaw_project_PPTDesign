# deck_spec.json 生成提示词

请把已确认的大纲、逐页文案和页面设计说明转换为 `deck_spec.json`。

要求：

1. 输出严格 JSON；
2. 每页包含 slide_no、type、title、conclusion、core_judgement、chart_proof_goal、chart_visual_boundary、body/display_text、chart_type、chart_data、layout_pattern、speaker_notes、need_compression；
3. 不新增事实；
4. 不改写结论；
5. 版式模式必须来自 `visual_patterns/layout_library.md`；
6. 图表类型必须来自 `templates/chart_patterns.md`，不得与 `layout_pattern` 混用；
7. 如果页面内容过长，标记 need_compression=true；
8. `visual_notes` 必须吸收页面设计说明中的视觉降噪约束，至少体现：
   - 本页主红色锚点；
   - 卡片强/中/弱层级；
   - 模块间距与页脚安全区；
   - 底部结论条是否允许以及强度；
   - 需要弱化或删除的装饰元素。
9. 每页必须先生成 `core_judgement`，再生成 `chart_proof_goal`，最后选择 `chart_type` 和 `layout_pattern`。
10. `chart_proof_goal` 必须回答“这个主图表要证明本页唯一核心判断中的哪一部分”。
11. `chart_visual_boundary` 必须包含 3~5 条短约束，说明该图表不得退化为什么、必须体现什么、红色和主次如何控制。

生成时必须检查：

- 正文页不得默认使用厚重红色压底条；
- `comparison_table` 页面必须让表格承担证据，结论通过标题、右侧指标卡或弱结论区呈现；
- `swimlane_process` 与 `value_chain_loop` 的节点、箭头、连接线必须在 `visual_notes` 中说明统一规则；
- 单页主红色视觉锚点不超过 1-2 个。


## 图表证明契约检查

生成 `deck_spec.json` 前必须检查：

- `core_judgement` 是否为本页唯一判断，不能是多个判断拼接；
- `chart_proof_goal` 是否直接服务 `core_judgement`；
- `chart_type` 是否适合证明 `chart_proof_goal`；
- `chart_visual_boundary` 是否具体、可执行，且不与 `visual_notes` 冲突；
- 若图表无法证明本页判断，应优先调整 `chart_type` 或拆页，不得用装饰性图表硬凑。
