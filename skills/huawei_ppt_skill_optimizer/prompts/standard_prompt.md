# Skill Optimizer Standard Prompt - Single Task

```text
请启用 huawei_ppt_skill_optimizer。

当前模式：单任务模式。

请读取：
1. PPT大纲：project/work/outline_v0.1.md
2. 逐页文案：project/work/page_copy_v0.1.md
3. 页面设计：project/work/page_design_v0.1.md
4. deck_spec.json：project/work/deck_spec_v0.1.json
5. 交接单：project/handoff/A_to_B.md

请判断哪些问题需要沉淀进 Skill，并输出：
1. review/review_reports/skill_review_v{n}.md
2. review/issue_log.md
3. review/improvement_backlog.md
4. review/patch_proposals/patch_proposal_v{n}.md
5. review/regression_plan.md
6. review/changelog_draft.md
7 .handoff/B_to_A.md

要求：
1. 不直接修改 design_work；
2. 不直接修改任何 SKILL.md；
3. 只输出 patch proposal；
4. 区分 Skill 问题、输入问题、单次偏差；
5. 如当前任务不是 AI 算力主题，必须检查主题污染。
```
