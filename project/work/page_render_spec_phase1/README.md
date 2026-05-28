# page_render_spec Phase 1 交付包

## 范围

本目录为 Phase 1 手工样例交付，不修改 `skills/huawei_ppt_master/*`，不接入默认生成链路。

## 本次包含

### 三页样例 page_render_spec

- `page_render_specs/P07_page_render_spec_v0.1.json`
- `page_render_specs/P08_page_render_spec_v0.1.json`
- `page_render_specs/P14_page_render_spec_v0.1.json`
- `page_render_spec_samples_v0.1.json`：三页合并索引

### 上游交付物

- `deck_spec.json`
- `page_copy_v0.1.md`
- `page_design_v0.1.md`

### 依赖文件

- `dependencies/visual_rules.md`
- `dependencies/chart_patterns.md`
- `dependencies/wording_rules.md`
- `dependencies/layout_library.md`

## 样例页选择理由

- P7：双 V 生命周期架构，验证复杂关系与右侧洞察栏约束；
- P8：自学习数字孪生架构，验证分层架构 + 闭环箭头 + 底部结论；
- P14：决策收口页，验证拍板事项卡 + 执行表格 + 管理收口。

## 边界

- `page_render_spec` 只继承/约束 `deck_spec/page_design/page_copy`，不新增事实判断；
- `layout_pattern`、`chart_type`、`bottom_conclusion`、`right_insight_panel` 均为派生字段；
- C 端无法满足约束时应返回 `manual_review`，不得静默改写内容。
