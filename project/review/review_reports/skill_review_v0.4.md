# Skill 优化评审报告

## 1. 基本信息
- 任务名称：华为云竞争力深度洞察
- task_id：HC-20260504-06
- 评审角色：B / huawei_ppt_skill_optimizer
- 评审对象：`skills/huawei_ppt_master/SKILL.md`
- 评审目标：判断 700+ 行主 Skill 是否存在可压缩、可拆分、可提遵循度的优化空间

## 2. 被评审对象
### 已读取文件
1. `skills/huawei_ppt_master/SKILL.md`
2. `project/handoff/A_to_B.md`
3. `project/handoff/status.md`

### 当前观察
- 主文件总行数：约 778 行
- 当前问题不是“规则太少”，而是“主入口过重、重复、混杂”
- 已出现维护漂移迹象：章节编号不连续、角色章节编号异常、同类规则多处重复

## 3. 总体结论
**有明显优化空间，且值得做结构性瘦身。**

我不建议简单删规则；更合理的方向是：
1. 保留 `SKILL.md` 作为唯一入口；
2. 把重复规则、枚举细节、回归/交付细节下沉到专门文件；
3. 让 `SKILL.md` 只保留“必读原则 + 最小读图 + 触发路由 + 硬门禁 + 输出顺序”。

目标不是把内容变少，而是把**首屏决策负担**降下来。

## 4. 问题清单

### ISSUE-101
- 问题位置：`skills/huawei_ppt_master/SKILL.md`
- 问题描述：单文件承载入口说明、读取顺序、主题路由、输出契约、风格规则、图表规则、自检门禁、协作边界、交付打包、回归模式等多类职责。
- 影响：主 Skill 变成“大而全操作手册”，执行时不易抓住最关键约束，遵循度下降。
- 问题归因：`output_contract_gap`
- 修改建议：把主文件收敛为“控制面”，把细则下沉到 `core/`、`templates/`、`eval/`。
- 优先级：P0
- 是否沉淀为 Skill：是
- 是否加入回归测试：是

### ISSUE-102
- 问题位置：主题污染、自检、失败重写、回归测试相关章节
- 问题描述：同一约束在多个章节反复出现，尤其 AI 主题污染规则、自检门禁、失败条件、分包规则存在重复表述。
- 影响：修改一处容易漏改其他处，长期会造成规则漂移。
- 问题归因：`skill_rule_conflict`
- 修改建议：每类规则只保留一个权威定义点，其他位置改成引用。
- 优先级：P1
- 是否沉淀为 Skill：是
- 是否加入回归测试：是

### ISSUE-103
- 问题位置：`7.4 deck_spec.json` 示例
- 问题描述：示例内容使用 AI 算力/昇腾/NVIDIA 主题，且样例过长。
- 影响：对非 AI 主题形成错误锚点，提升主题污染概率，也拉长主文件长度。
- 问题归因：`domain_profile_issue`
- 修改建议：改为通用中性示例，详细字段示例移入 `core/output_contracts.md`。
- 优先级：P1
- 是否沉淀为 Skill：是
- 是否加入回归测试：是

### ISSUE-104
- 问题位置：章节结构
- 问题描述：存在编号异常（如 `14.4` 出现在 `14` 之前、缺少 `18`），说明维护成本已经上升。
- 影响：降低可维护性，也会削弱模型对主文件结构的稳定理解。
- 问题归因：`single_run_deviation`
- 修改建议：重排目录并控制章节层级深度。
- 优先级：P1
- 是否沉淀为 Skill：是
- 是否加入回归测试：否

### ISSUE-105
- 问题位置：强制读取顺序
- 问题描述：当前把大量模板、图表、版式、评测文件写成接近全量必读。
- 影响：前置读取成本过高，容易让执行过程从“按需调用”退化成“机械串读”。
- 问题归因：`skill_rule_missing`
- 修改建议：改成“必读 5 件套 + 条件读取树 + 按需补充”。
- 优先级：P0
- 是否沉淀为 Skill：是
- 是否加入回归测试：是

## 5. 问题归因
- `output_contract_gap`：1 项
- `skill_rule_conflict`：1 项
- `domain_profile_issue`：1 项
- `single_run_deviation`：1 项
- `skill_rule_missing`：1 项

## 6. improvement_backlog
- HPPT-101：主 Skill 控制面瘦身
- HPPT-102：重复规则单点收口
- HPPT-103：示例去主题污染化
- HPPT-104：读取顺序改为最小必读 + 条件路由

## 7. patch proposal 摘要
建议修改以下文件（仅 patch proposal，不直接改 Skill）：
1. `skills/huawei_ppt_master/SKILL.md`
2. `skills/huawei_ppt_master/core/output_contracts.md`
3. `skills/huawei_ppt_master/core/generation_workflow.md`
4. `skills/huawei_ppt_master/eval/regression_cases.md`

## 8. 回归测试建议
1. 非 AI 主题是否仍被 AI 示例带偏
2. 执行时是否只读取最小必读文件
3. 主题污染规则是否仍只保留单点权威定义
4. 输出质量是否因主 Skill 缩短而下降
5. 超过 10 页交付时，交付规则是否仍能正确执行

## 9. 合入判断
**建议合入。**

前提：不是“删内容”，而是“重构信息架构”。如果只是压缩字数、不调整职责边界，收益会很有限。

## 10. B_to_A 交接摘要
当前主 Skill 过长的根因不是信息量本身，而是控制面与知识面没有分层。建议把 `SKILL.md` 从 778 行压到约 180~260 行，只保留入口级规则；把长示例、枚举、交付细节、自检细节下沉到对应文件。