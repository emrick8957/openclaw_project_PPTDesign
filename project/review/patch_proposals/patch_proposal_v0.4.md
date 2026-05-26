# Patch Proposal v0.4

## 1. 基本信息
- 当前任务：华为云竞争力深度洞察
- patch 编号：PP-20260506-04
- 生成时间：2026-05-06
- 目标：降低 `skills/huawei_ppt_master/SKILL.md` 主入口长度，提高规则遵循度与可维护性

## 2. 修改摘要
| 修改文件 | 修改类型 | 对应 issue_id | 优先级 |
|---|---|---|---|
| `skills/huawei_ppt_master/SKILL.md` | 结构重构 / 主入口瘦身 | ISSUE-101, ISSUE-102, ISSUE-103, ISSUE-104, ISSUE-105 | P0 |
| `skills/huawei_ppt_master/core/output_contracts.md` | 契约上收细化 | ISSUE-101, ISSUE-103 | P1 |
| `skills/huawei_ppt_master/core/generation_workflow.md` | 读取路由增强 | ISSUE-105 | P1 |
| `skills/huawei_ppt_master/eval/regression_cases.md` | 回归新增 | ISSUE-102, ISSUE-103, ISSUE-105 | P1 |

## 3. 详细补丁

### 修改文件：`skills/huawei_ppt_master/SKILL.md`

#### 对应问题
- issue_id: ISSUE-101
- backlog_id: HPPT-101
- issue_id: ISSUE-102
- backlog_id: HPPT-102
- issue_id: ISSUE-103
- backlog_id: HPPT-103
- issue_id: ISSUE-104
- backlog_id: HPPT-101
- issue_id: ISSUE-105
- backlog_id: HPPT-104

#### 原规则或缺失点
> 当前主 Skill 同时承担入口说明、知识索引、详细契约、示例库、回归说明、交付规则等职责，导致单文件约 778 行；并存在重复规则、编号漂移、AI 主题示例过重、接近全量必读等问题。

#### 建议新增/修改内容
```markdown
# 结构重构原则
1. `SKILL.md` 只保留入口级规则，不再承载大段示例和长枚举。
2. 主文件目标长度控制在 180~260 行。
3. 每类规则只保留一个“权威定义点”，其他位置只做引用。

# 建议保留在 SKILL.md 的内容
## A. 最高优先级原则
- 用户要求优先
- 本 Skill 为唯一入口
- 禁止编造事实
- 非 AI 主题禁止污染

## B. 最小必读 5 件套
1. `core/generation_workflow.md`
2. `core/topic_router.md`
3. `core/output_contracts.md`
4. `core/anti_overfit_rules.md`
5. `core/audience_rules.md`

## C. 条件读取树
- 命中主题包时才读取对应 `domain_profiles/`
- 仅在需要页面设计/JSON 时读取 `visual_patterns/`
- 仅在输出前读取 `eval/` 自检文件

## D. 输出模式路由
- 只要大纲 → 引用 `core/output_contracts.md` 的 outline 契约
- 逐页文案 → 引用 page_copy 契约
- 页面设计 → 引用 page_design 契约
- deck_spec → 引用 deck_spec 契约

## E. 硬门禁
- 非 AI 主题污染即失败
- 标题不结论化即失败
- 编造数据即失败
- 版式/图表字段混用即失败

## F. 默认输出顺序与交付路径（仅摘要）
- work 区主文件
- handoff 文件
- deliverables 分包规则摘要
- 详细交付规则引用 `core/output_contracts.md`
```

#### 修改理由
把主文件从“全量说明书”改成“控制面”。模型先抓住入口和门禁，再按需读取细节，遵循度通常会更稳。

#### 影响范围
- 主 Skill 首次阅读负担
- 主题路由稳定性
- 后续维护成本
- 规则修改一致性

#### 回归测试
- 主文件缩短后，是否仍能完整生成四类输出
- 非 AI 主题是否仍能稳定避免污染
- 是否仍按条件读取而非全量串读

---

### 修改文件：`skills/huawei_ppt_master/core/output_contracts.md`

#### 对应问题
- issue_id: ISSUE-101
- backlog_id: HPPT-101
- issue_id: ISSUE-103
- backlog_id: HPPT-103

#### 原规则或缺失点
> 当前很多输出契约、长 JSON 示例、字段说明仍停留在主 Skill 中。

#### 建议新增/修改内容
```markdown
## 新增：四类输出契约总表
- outline
- page_copy
- page_design
- deck_spec

## 新增：deck_spec 中性示例
示例主题改为“某行业数字化转型规划”或“云竞争力分析”，避免带入 AI 算力词。

## 新增：字段边界速查表
| 字段 | 含义 | 来源文件 | 是否允许自由扩展 |
|---|---|---|---|
| chart_type | 图表/信息结构类型 | templates/chart_patterns.md | 否 |
| layout_pattern | 页面布局模式 | visual_patterns/layout_library.md | 否 |
| visual_notes | 自由补充说明 | 当前页 | 是 |
```

#### 修改理由
把长示例和细字段说明放回契约文件，更符合职责边界，也能减少主 Skill 被样例“带偏”。

#### 影响范围
- deck_spec 生成
- Builder 输入稳定性
- 非 AI 主题安全性

#### 回归测试
- 非 AI 主题是否仍引用中性示例
- `chart_type` / `layout_pattern` 是否仍边界清晰

---

### 修改文件：`skills/huawei_ppt_master/core/generation_workflow.md`

#### 对应问题
- issue_id: ISSUE-105
- backlog_id: HPPT-104

#### 原规则或缺失点
> 当前主 Skill 给出接近全量读取顺序，但没有把“按需读取”明确画成决策树。

#### 建议新增/修改内容
```markdown
## 读取决策树（新增）
Step 1：先读 5 个必读文件
Step 2：根据 `topic_router` 判断是否加载主题包
Step 3：如果用户只要大纲，则不读 `visual_patterns/` 细文件
Step 4：如果用户要求页面设计或 deck_spec，再读取版式库
Step 5：输出前才读 eval 自检文件
```

#### 修改理由
让最小阅读路径变清晰，减少执行时的无效上下文负担。

#### 影响范围
- 执行效率
- 规则遵循度
- 上下文利用率

#### 回归测试
- 只要大纲任务是否跳过非必要版式文件
- deck_spec 任务是否能补齐所需读取

---

### 修改文件：`skills/huawei_ppt_master/eval/regression_cases.md`

#### 对应问题
- issue_id: ISSUE-102
- backlog_id: HPPT-102
- issue_id: ISSUE-103
- backlog_id: HPPT-103
- issue_id: ISSUE-105
- backlog_id: HPPT-104

#### 原规则或缺失点
> 当前回归没有显式覆盖“主 Skill 缩短后是否降质”“中性示例是否有效”“条件读取是否生效”。

#### 建议新增/修改内容
```markdown
新增回归用例：
1. 主 Skill 瘦身回归
   - 在不读取全部模板的情况下，是否仍能输出合格大纲
2. 非 AI 主题抗污染回归
   - 使用“华为云竞争力深度洞察”题目，检查是否仍被 AI 示例带偏
3. 条件读取回归
   - 只要大纲任务不得强制依赖 `visual_patterns/*` 细文件
4. 契约回归
   - deck_spec 的 `chart_type` / `layout_pattern` 不得混用
```

#### 修改理由
这轮改造的核心风险不是“规则没写”，而是“瘦身后掉质量”；必须把这个风险前置到回归。

#### 影响范围
- Skill 重构后的验收可信度

#### 回归测试
- 新增用例本身即为回归项

## 4. 推荐的新信息架构

### 目标状态
- `SKILL.md`：入口、门禁、路由、摘要
- `core/output_contracts.md`：四类输出契约 + JSON 示例
- `core/generation_workflow.md`：最小读取路径 + 执行决策树
- `eval/regression_cases.md`：瘦身后回归

### 不建议做的事
1. 只删字数，不改职责边界
2. 继续在主 Skill 堆长示例
3. 同一规则在多个章节重复维护
4. 用 AI 专题示例做通用 Skill 默认样例

## 5. 合入建议
**建议合入。**

这是结构优化，不是内容减配。只要回归通过，收益会比较直接：更短、更稳、更不容易跑偏。