# page_render_spec Phase 0 定位冻结说明 v0.1

## 1. 一句话定位

`page_render_spec.json` 不是新的 PPT 内容源，也不是 `huawei_ppt_master` 的默认交付物；它是 **A→C 之间的复杂页面构造约束层**，用于把高风险页面的版式、文本适配、组件边界和渲染验收条件提前锁住，降低 C 端 PPTX 构建时的跑版、误读和语义漂移。

## 2. 适用对象

仅适用于以下页面：

1. 复杂结构页：多区域、多链路、多层级、多组件嵌套；
2. 高风险页：标题强判断、图表需严格证明结论、文本密度高；
3. 历史跑版页：过往生成中发生过文本溢出、红色锚点过重、卡片等权、底部结论失控等问题；
4. 需要渲染锁定页：关键汇报页、架构页、决策页、路线图页、收口页。

普通页面默认不生成 `page_render_spec.json`。

## 3. 非目标

Phase 0 明确不做以下事项：

- 不修改 `skills/huawei_ppt_master/*`；
- 不把 `page_render_spec.json` 加入默认全链路交付；
- 不新增事实、观点或业务结论；
- 不替代 `deck_spec.json`、`page_design.md`、`page_copy.md`；
- 不要求所有页面都具备 full 级约束；
- 不引入 PPTX 构建器实现细节作为内容规则。

## 4. 与既有产物关系

| 产物 | 职责 | page_render_spec 关系 |
|---|---|---|
| outline | 章节与叙事骨架 | 不继承，不反向修改 |
| page_copy | 页面文案与讲稿 | 只引用必要文本，不生成新内容 |
| page_design | 页面设计说明 | 继承视觉与版式意图 |
| deck_spec | 机器可读页面语义合同 | 继承 `layout_pattern`、`chart_type`、`bottom_conclusion`、`right_insight_panel` 等派生字段 |
| page_render_spec | 构造约束层 | 锁定复杂页的渲染单元、文本适配、边界与验收 |
| PPTX builder / C端 | 执行渲染 | 消费 page_render_spec，不反向创造内容 |

## 5. 核心原则

1. **派生不原创**：不得产生新结论、新事实、新图表含义；
2. **只约束高风险**：默认轻量，必要时 full；
3. **服务渲染确定性**：重点解决跑版、密度、层级、红色锚点、底部结论、右侧洞察等问题；
4. **保持 A/C 边界**：A 给约束，C 负责实现；C 不改内容判断；
5. **可回退**：没有 page_render_spec 时，现有 `deck_spec + page_design` 链路仍可工作。

## 6. Phase 0 冻结结论

`page_render_spec.json` v0.1 的正确位置是：

> 面向复杂/高风险页面的“页面构造约束补丁”，由 A 侧按需生成，供 C 侧渲染时消费；它不进入默认 PPT 内容生产链，不承担内容创作职责。
