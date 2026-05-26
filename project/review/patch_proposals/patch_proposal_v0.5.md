# Patch Proposal v0.5

## 1. 基本信息
- 当前任务：华为云竞争力深度洞察
- patch 编号：PP-20260506-05
- 生成时间：2026-05-06
- 目标：给出 `skills/huawei_ppt_master/SKILL.md` 的精简改稿方案、正文草案与旧版映射表

## 2. 改稿原则
1. 不改 Skill 定位，只改信息架构。
2. `SKILL.md` 保留入口控制面，不再承载长示例和大段枚举。
3. 详细契约、长 JSON 示例、读取细节、自检细节分别下沉到 `core/` / `eval/`。
4. 每类规则只保留一个权威定义点。

## 3. 建议替换后的 SKILL.md 目录骨架
```markdown
# huawei_ppt_master

## 0. 最高优先级原则
## 1. Skill 定位
## 2. 适用范围
## 3. 目录职责与读取策略
### 3.1 最小必读 5 件套
### 3.2 条件读取规则
## 4. 任务识别与输出路由
## 5. 主题包隔离与反污染硬规则
## 6. 输出硬门禁
## 7. 默认交付顺序
## 8. 协作边界
## 9. 失败与重写条件
## 10. 最小合格输出标准
```

## 4. 精简版 SKILL.md 正文草案
见：`project/review/drafts/huawei_ppt_master_SKILL_slim_v0.1.md`

## 5. 旧版到新版映射表
见：`project/review/drafts/huawei_ppt_master_SKILL_mapping_v0.1.md`

## 6. 推荐下沉位置
| 旧内容 | 建议去向 |
|---|---|
| outline / page_copy / page_design / deck_spec 详细契约 | `core/output_contracts.md` |
| 长 deck_spec JSON 示例 | `core/output_contracts.md` |
| 全量读取顺序 | `core/generation_workflow.md` |
| 自检清单 | `eval/acceptance_checklist.md` / `eval/visual_scorecard.md` |
| 回归模式细节 | `eval/regression_cases.md` |
| 图表长枚举 | `templates/chart_patterns.md` |
| 版式长枚举 | `visual_patterns/layout_library.md` |

## 7. 合入建议
建议按“先替换主文件，再补回归”的顺序处理：
1. 先用精简版主文件替换旧主文件；
2. 再检查被引用的 `core/` / `eval/` 文件是否承接完整；
3. 最后跑一次非 AI 主题污染回归和 deck_spec 契约回归。
