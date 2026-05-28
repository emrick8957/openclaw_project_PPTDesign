# page_render_spec light/full 触发规则 v0.1

## 1. 默认策略

- 默认不生成 `page_render_spec`；
- 触发后优先生成 `light`；
- 只有当页面存在明确构造风险时升级为 `full`；
- 单个 deck 不建议超过 20% 页面进入 full，除非用户明确要求渲染锁定。

## 2. 不生成条件

满足以下条件时不生成：

1. 标准标题 + 单图/单表/三卡片页面；
2. 文本密度低或中，且不存在右侧洞察/底部结论强约束；
3. `deck_spec` 和 `page_design` 已足以指导 C 端；
4. 页面不是关键判断页、架构页、路线图页、收口页。

## 3. light 触发条件

满足任一条件，生成 `spec_level: light`：

1. 页面有 `bottom_conclusion`，且该结论必须作为底部收口而非正文重复；
2. 页面有 `right_insight_panel`，但内容项不超过 3 条；
3. 页面使用多卡片结构，需明确主次层级，避免等权；
4. 页面标题为强判断句，主图必须证明标题；
5. 页面有轻量红色锚点约束，需防止红色面积外溢；
6. 页面是关键章节页或小结页，但结构不复杂。

light 应包含：`source_trace`、`derived_contract`、核心 `render_units`、简化 `text_fit_policy`、简化 `render_validation`。

## 4. full 触发条件

满足任一条件，生成 `spec_level: full`：

1. 架构页：双 V、数字孪生、自学习闭环、多层系统架构；
2. 生命周期页：阶段多、箭头多、跨层关系多；
3. 决策收口页：需要强标题、主视觉、底部结论、行动建议同时成立；
4. 路线图/时间轴页：多阶段、多里程碑、多责任主体；
5. 四象限/坐标图：坐标语义容易失真；
6. 三列链路/两栏面板：左右或三段因果关系必须锁定；
7. 文本密度高，超过常规卡片承载能力；
8. 历史生成发生过跑版、红底过重、卡片等权、底部结论压迫正文等问题。

full 必须包含完整 `source_trace`、`derived_contract`、`subtype`、关键组件 `render_units`、完整 `text_fit_policy`、`render_unit_policy`、`render_validation` 与 C 端无法满足时的 `manual_review_if`。

## 5. 推荐 Phase 1 试点页

1. P7：双 V 生命周期架构页；
2. P8：自学习数字孪生架构页；
3. P14：决策收口页。

理由：三类页面分别覆盖架构复杂度、闭环语义复杂度、决策收口复杂度，最能验证 `page_render_spec` 是否真正降低构造风险。
