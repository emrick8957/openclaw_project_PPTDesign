# patch_proposal_v1.0

## 1. 背景

本 proposal 来自 `SWE-ATLAS-B-REVIEW-v1.0-second-round`。角色 A 已完成 v0.2 full_delivery 打包，当前交付物可进入 PPTX Builder。本 proposal 仅沉淀后续 Skill 优化建议，不要求当前交付物返工。

## 2. 建议修改文件与规则

### 2.1 多版本交付优先级规则

| 字段 | 内容 |
|---|---|
| 建议修改文件 | `skills/huawei_ppt_master/templates/` 下 README/交付契约模板，或 `core/generation_workflow.md` |
| 对应 issue_id | SWE-B2-001 |
| 原规则或缺失点 | 当 deliverables 中同时存在 v0.1、v0.2 等多个交付包时，缺少“最终推荐版本”显式标识 |
| 新增规则 | 最新 `README.md` 与 `status.md` 必须标注 recommended package；旧包如保留，应在状态或 README 中标记 superseded |
| 修改理由 | 避免 Builder 或人工审阅误取旧包 |
| 影响范围 | 仅影响交付物可追溯性，不影响内容生成 |
| 回归测试建议 | 构造多版本包目录，检查 status 是否明确推荐版本 |

### 2.2 主题污染扫描范围分层

| 字段 | 内容 |
|---|---|
| 建议修改文件 | `skills/huawei_ppt_master/eval/domain_contamination_tests.md` |
| 对应 issue_id | SWE-B2-002 |
| 原规则或缺失点 | 全文 grep 会把依赖模板中的禁用词清单误判为主题污染 |
| 新增规则 | 对内容文件严格扫描：outline/page_copy/page_design/deck_spec 的 title、conclusion、display_text、speaker_notes、visual_notes；对 `dependencies/templates/wording_rules.md` 等规则文件，禁用词清单可豁免，但不得出现在页面内容字段 |
| 修改理由 | 降低误报，同时保持页面内容污染拦截能力 |
| 影响范围 | 影响 QA/eval 扫描逻辑，不放宽页面文案要求 |
| 回归测试建议 | 依赖规则文件含“昇腾/NVIDIA”禁用词清单时不报错；page_copy 或 deck_spec 页面字段出现时必须报错 |

## 3. 合入建议

**建议后续合入，不阻塞当前 SWE Atlas 交付。**

优先级：P2。可与下一轮交付契约/QA gate 优化一起处理。
