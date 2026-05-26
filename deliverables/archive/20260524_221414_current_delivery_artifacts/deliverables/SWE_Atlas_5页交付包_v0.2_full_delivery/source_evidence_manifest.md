# source_evidence_manifest

> 依据 `SWE_Atlas_5页核心内容与启示.md` 中每页“数据来源”字段整理；不新增事实。

| 页码 | 关键数字 / 结论 | 来源页码 / 表格 |
|---|---|---|
| P1 | SWE Atlas 包含 Codebase Q&A 124 个任务、Test Writing 90 个任务、Refactoring 70 个任务；共 284 个专家编写任务，覆盖 18 个活跃开源仓库 | PDF p1-p3 |
| P1 | 评测从 bug fix / feature implementation 扩展到测试完整性、可维护性、抽象复用、代码库卫生、反模式等工程质量 | PDF p1-p3 |
| P2 | Codebase Q&A、Test Writing、Refactoring 三类任务分别结合 Rubric、Manifest / Mutation、Regression tests 等混合评测机制 | PDF p2-p4 |
| P2 | Rubric 用于捕捉程序化测试难以覆盖的工程质量问题，如代码放置、可维护性、反模式、清理是否彻底 | PDF p2-p4 |
| P3 | Native scaffold 下 GPT 5.4 Pass@1 43.49%、Pass 3 29.2%；Opus 4.7 Pass@1 41.89%、Pass 3 29.2%；GPT 5.3 Codex Pass@1 37.38%；Opus 4.6 Pass@1 34.93%；Gemini 3.1 Pro Pass@1 25.23% | PDF p5，Table 1 |
| P3 | mini-SWE-Agent 脚手架下 Opus 4.7 Pass@1 38.94%、GPT 5.4 Pass@1 38.00%；开源模型 GLM 5 为 24.03% | PDF p5，Table 1 |
| P3 | Pass 3 约 29% 表明“偶尔做对”和“稳定做对”仍有差距 | PDF p5，Table 1 |
| P4 | 失败模式集中在缺少运行时证据、测试断言弱、重构清理不彻底 | PDF p6-p9 |
| P4 | Codebase Q&A 高分模型更多执行代码、启动应用、发送请求并做运行时分析；失败常见于静态解释或覆盖不完整 | PDF p6-p9 |
| P4 | Test Writing 常见问题是 happy path 测试、断言弱，难以区分正常实现和 no-op mutation | PDF p6-p9 |
| P4 | Refactoring 仅看回归测试会高估表现，加入 Rubric 后工程质量短板更明显 | PDF p6-p9 |
| P5 | 建议内部构建 SWE Atlas 类评测集，覆盖任务、证据、质量和稳定性，并接入 CI 做持续回归 | PDF p10，Conclusion；结合 p2-p9 方法与结果 |
| P5 | 启示包括扩展评测对象、分层评测标准、用 mutation / fault injection 检查测试杀伤力、重构强制清理闭环 | PDF p10，Conclusion；结合 p2-p9 方法与结果 |
