# patch_proposal_v0.9

## 1. 背景

本 proposal 来自 `SWE-ATLAS-B-REVIEW-v0.9`。本次不直接修改 `huawei_ppt_master`，仅提出可人工确认的规则补丁建议。

## 2. 建议修改文件与规则

### 2.1 交付流程 / 生成工作流

| 字段 | 内容 |
|---|---|
| 建议修改文件 | `skills/huawei_ppt_master/core/generation_workflow.md` 或等价交付流程文件 |
| 对应 issue_id | SWE-B-001, SWE-B-002 |
| 原规则或缺失点 | 缺少“评审前/打包前检查 handoff/status 是否指向当前任务”的硬性门禁；缺少“B 评审通过后 A 执行正式打包”的明确动作 |
| 新增规则 | 在交付前执行 handoff freshness check：任务名、版本、交付物路径、当前阶段必须与最新 deliverables 一致；B 评审通过后，A 根据 B_to_A 生成正式 zip 包 |
| 修改理由 | 避免旧任务交接单污染当前交付链路 |
| 影响范围 | 仅影响交付闭环，不改变内容生成逻辑 |
| 回归测试建议 | 构造 status 指向旧任务的样例，要求评审/打包前拦截 |

### 2.2 论文/报告类交付证据清单

| 字段 | 内容 |
|---|---|
| 建议修改文件 | `skills/huawei_ppt_master/templates/` 下新增或扩展 delivery README 模板；`skills/huawei_ppt_master/eval/` 增加事实追溯检查 |
| 对应 issue_id | SWE-B-003 |
| 原规则或缺失点 | 内容稿内有页码标注，但正式交付包未强制包含 source evidence manifest |
| 新增规则 | 对论文、白皮书、报告解读类材料，交付包必须包含 README 或 source_evidence_manifest，列出关键数字、表格、页码、来源文件；启示类内容需标注为“基于来源推导” |
| 修改理由 | 降低事实追溯风险，方便高层材料复核 |
| 影响范围 | 仅影响含外部来源/研究报告的交付包 |
| 回归测试建议 | 检查关键数字是否在 evidence manifest 中有来源记录 |

### 2.3 视觉模式命名边界

| 字段 | 内容 |
|---|---|
| 建议修改文件 | `skills/huawei_ppt_master/visual_patterns/layout_library.md` |
| 对应 issue_id | SWE-B-004 |
| 原规则或缺失点 | `ecosystem_map` 容易被泛化用于所有闭环图 |
| 新增规则 | `ecosystem_map` 仅用于生态、伙伴、多主体协同关系；评测/治理/能力建设闭环优先使用 `closed_loop`、`value_chain_loop` 或 `process_cycle` |
| 修改理由 | 降低 Builder 图形误解概率 |
| 影响范围 | 视觉模式选择，不影响文案 |
| 回归测试建议 | 给出“评测闭环”样例，验证不会路由到 ecosystem_map |

## 3. 合入建议

**有条件合入。**  
建议优先合入 2.1 和 2.2；2.3 可随视觉模式库统一整理。
