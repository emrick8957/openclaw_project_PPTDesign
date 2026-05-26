# Regression Rules

单任务模式下，回归测试不再使用 task_id，而使用当前工作区的 input/topic.md 或用户指定题目。

## 必跑测试建议

1. 当前任务题目；
2. 一个非当前主题的通用题目；
3. 一个非 AI 算力主题污染测试；
4. deck_spec 字段完整性测试；
5. 页面设计说明可执行性测试；
6. page_images / pptx 输入可用性测试。

## 通过标准

- 每项得分不低于 85；
- 非 AI 主题不得出现污染词；
- deck_spec 必须可解析；
- 页面设计说明必须能指导 page_images / pptx。
