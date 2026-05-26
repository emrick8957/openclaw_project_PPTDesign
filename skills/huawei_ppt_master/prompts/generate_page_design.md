# 生成页面设计说明提示词

请基于已确认大纲和逐页文案，为每页生成页面设计说明。

要求：

1. 从 `visual_patterns/layout_library.md` 中选择版式模式；
2. 说明标题区、图表区、正文区、强调区、页脚区；
3. 说明图表承载的信息；
4. 说明 PPTX Builder 应如何实现；
5. 如内容过长，标记 need_compression=true；
6. 不改写核心观点。`n7. 必须遵守 `templates/visual_rules.md` 的职责边界：视觉规则只管视觉，不改写事实、不解释 deck_spec 字段、不替代评分规则。`n8. 每页必须输出视觉降噪约束：
   - `red_anchor`：本页唯一主红色强调点；
   - `card_hierarchy`：卡片强/中/弱层级安排；
   - `spacing_rule`：模块间距、卡片内边距和页脚安全区；
   - `bottom_bar_rule`：是否允许底部结论条，若允许需说明高度和颜色强度；
   - `visual_simplification`：需要弱化或删除的装饰元素；`n   - `visual_boundary`：本页需避免的负面视觉风格，如互联网发布会风、咨询海报风、卡通插画风、Excel 报表风；`n   - `page_type_gate`：本页页型门禁，如案例页不做图片墙、决策页拍板事项独立突出、路线图必须有阶段门槛、总结页必须形成最终定义。

输出页面设计说明时，每页至少包含以下字段：

```text
版式模式：
区域划分：
标题区：
图表区：
文字区：
强调元素：
页脚：
视觉降噪约束：
  red_anchor：
  card_hierarchy：
  spacing_rule：
  bottom_bar_rule：
  visual_simplification：`n  visual_boundary：`n  page_type_gate：`nPPTX Builder 注意事项：
```

