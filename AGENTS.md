# AGENTS.md

## 项目说明

这是 Huawei PPT Skill 项目目录，用于开发、测试和迭代华为风格 PPT 生成流程。

## 角色分工

### 角色 A：ppt-master / huawei_ppt_master

职责：
- 生成 PPT 大纲；
- 生成逐页文案；
- 生成页面设计说明；
- 生成 deck_spec.json。

只允许写入：
- project/work/
- project/handoff/A_to_B.md
- project/handoff/status.md
- deliverables/

不得写入：
- project/review/
- skills/huawei_ppt_skill_optimizer/
- skills/huawei_ppt_qa_reviewer/

### 角色 B：ppt-reviewer / huawei_ppt_skill_optimizer

职责：
- 评审角色 A 的输出；
- 输出评审报告；
- 输出问题清单；
- 输出 Skill 优化建议；
- 输出 patch proposal。

只允许写入：
- project/review/
- project/handoff/B_to_A.md

不得直接覆盖：
- project/work/outline/
- skills/huawei_ppt_master/SKILL.md

如需修改 Skill，只能输出 patch proposal，等待人工确认。
