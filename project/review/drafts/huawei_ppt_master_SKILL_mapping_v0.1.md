# huawei_ppt_master SKILL 映射表 v0.1

## 目标
说明旧版 700+ 行主文件内容，在精简版中如何保留、合并或下沉。

| 旧版章节 | 处理方式 | 新位置 | 说明 |
|---|---|---|---|
| 0. 最高优先级原则 | 保留 | 新版 0 | 作为入口级强约束，必须保留 |
| 1. Skill 定位 | 保留 | 新版 1 | 基本不变，做压缩 |
| 2. 适用范围 | 保留 | 新版 2 | 保留核心范围，删长尾说明 |
| 3. 文件职责说明 | 合并压缩 | 新版 3 | 只保留目录职责和读取策略 |
| 4. 强制读取顺序 | 重构 | 新版 3.1 / 3.2 + `core/generation_workflow.md` | 由全量顺序改为最小必读 + 条件读取 |
| 5. 主题包隔离规则 | 保留压缩 | 新版 5 | 保留硬规则，触发细节留给 `topic_router` |
| 6. 任务类型识别 | 保留压缩 | 新版 4 | 保留任务路由 |
| 7. 输出模式 | 摘要保留 | 新版 4 + `core/output_contracts.md` | 详细字段契约下沉 |
| 7.4 deck_spec JSON 长示例 | 下沉 | `core/output_contracts.md` | 主文件不保留长示例 |
| 8. 华为风格总原则 | 合并 | 新版 6 / 10 + `templates/wording_rules.md` | 主文件只保留硬门禁 |
| 9. 版式选择规则 | 下沉 | `visual_patterns/layout_library.md` / `core/output_contracts.md` | 避免主文件堆枚举 |
| 10. 通用图表选择规则 | 下沉 | `templates/chart_patterns.md` / `core/output_contracts.md` | 同上 |
| 11. 事实与数据规则 | 保留压缩 | 新版 1 / 6 / 9 | 作为通用硬门禁 |
| 12. 自检门禁 | 摘要保留 | 新版 6 + `eval/*` | 详细检查项下沉 |
| 13. 与其他角色协同边界 | 保留压缩 | 新版 8 | 修复编号与层级 |
| 14. 包自检模式 | 下沉 | `core/generation_workflow.md` 或单独文档 | 非主路径任务，不必放主文件展开 |
| 15. 回归测试模式 | 下沉 | `eval/regression_cases.md` | 回归细节不占入口 |
| 16. 默认输出顺序 | 保留压缩 | 新版 7 | 保留交付摘要 |
| 17. 失败与重写规则 | 保留压缩 | 新版 9 | 保留为硬失败条件 |
| 19. 最小合格输出标准 | 保留 | 新版 10 | 作为出口门槛 |

## 进一步建议
1. 精简版替换后，先补 `core/output_contracts.md` 的中性 `deck_spec` 示例；
2. 再补 `core/generation_workflow.md` 的条件读取决策树；
3. 最后补 `eval/regression_cases.md` 的瘦身回归项。
