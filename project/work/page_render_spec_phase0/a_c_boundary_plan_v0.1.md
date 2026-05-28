# page_render_spec A/C 边界计划 v0.1

## 1. 角色定义

| 角色 | 职责 | 不做 |
|---|---|---|
| A：huawei_ppt_master / 内容设计侧 | 生成页面判断、文案、设计说明、deck_spec；按需生成 page_render_spec 约束 | 不生成正式 PPTX；不写 C 端实现代码；不根据渲染便利性改事实和结论 |
| C：huawei_pptx_builder / 渲染构建侧 | 消费 deck_spec/page_design/page_render_spec，生成 PPTX 或页面图 | 不创造新内容；不擅自改结论；不把视觉实现反向污染 A 侧规则 |
| 人工评审 | 判断复杂页约束是否合理、是否需要沉淀 | 不要求所有页面强制 full |

## 2. A → C 输入合同

A 侧可向 C 侧提供：

1. `deck_spec.json`：页面语义合同；
2. `page_design.md`：页面设计说明；
3. `page_copy.md`：文案与讲稿；
4. `page_render_spec.json`：仅复杂/高风险页面的构造约束补丁。

其中 `page_render_spec` 只能引用/继承上述内容，不得新增事实判断。

## 3. C 侧消费要求

1. 若字段与 `deck_spec/page_design` 冲突，以 `deck_spec/page_design` 的内容语义为准；
2. `page_render_spec` 只决定构造约束、组件边界、文本适配和验收阈值；
3. 无法满足约束时，应返回 `manual_review`，而不是静默降级；
4. 不得把 `custom_subtype_note` 当作新版式白名单直接固化；
5. 不得因布局困难删除 `core_judgement`、`chart_proof_goal`、`bottom_conclusion` 等关键语义。

## 4. 冲突处理

| 冲突类型 | 处理原则 |
|---|---|
| page_render_spec 与 deck_spec 语义冲突 | deck_spec 优先，page_render_spec 回退修正 |
| page_render_spec 与 page_design 视觉冲突 | page_design 优先，除非 page_render_spec 明确是跑版修复约束 |
| C 端模板无法满足约束 | 标记 manual_review，不静默替换为无关版式 |
| 文本超出可承载范围 | 按 text_fit_policy 压缩；超过阈值进入人工评审 |
| subtype_enum 不覆盖实际页面 | 使用 custom，但必须写 custom_subtype_note；不得立即沉淀为长期枚举 |

## 5. Phase 路线

### Phase 0：方案冻结，不接入
- 输出定位说明、v0.1 schema 草案、light/full 触发规则、A/C 边界计划；
- 不修改 Skill；
- 不生成样例页。

### Phase 1：三页样例，不默认集成
- 选择 P7/P8/P14 三个复杂页；
- 手工生成样例 `page_render_spec`；
- 验证字段是否足够支撑 C 端消费；
- 不接入默认链路。

### Phase 2：人工样本扩展
- 基于更多历史跑版页补充样例；
- 观察 light/full 触发边界是否稳定；
- 暂不沉淀进 Skill。

### Phase 3：C 端消费验证
- 让 PPTX builder 或构建脚本读取样例；
- 对比有/无 page_render_spec 的页面稳定性；
- 记录不可满足约束。

### Phase 4：是否沉淀决策
- 决定是否进入 `huawei_ppt_master` / `huawei_pptx_builder`；
- 决定 subtype 白名单；
- 决定是否加入默认可选交付，而非强制交付。

## 6. 当前建议

Phase 0 结束后不要立刻改 Skill。建议先进入 Phase 1，用 P7/P8/P14 三页验证 schema 是否过重、是否缺字段、C 端是否能消费，再决定是否沉淀。
