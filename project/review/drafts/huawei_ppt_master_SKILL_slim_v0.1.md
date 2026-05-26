---
name: huawei_ppt_master
version: 0.2.2-draft
description: 通用华为风格 PPT 生成 Skill。根据用户输入生成 PPT 大纲、逐页文案、页面设计说明与 deck_spec.json；适用于技术方案、战略规划、竞品对比、项目复盘、客户方案、资源申请、运营治理、产品路线图、调研分析等高层汇报场景。
---

# huawei_ppt_master

## 0. 最高优先级原则
本 Skill 的唯一入口是 `SKILL.md`。

执行任何任务时，按以下优先级处理：
1. 用户当前明确要求；
2. 本 `SKILL.md` 的强制规则；
3. `core/` 通用执行内核；
4. `eval/` 验收与回归测试；
5. `templates/` 通用模板库；
6. `visual_patterns/` 版式库；
7. `domain_profiles/` 条件触发主题包；
8. `prompts/` 提示词素材。

如规则冲突，以本文件和 `core/anti_overfit_rules.md` 为准。

## 1. Skill 定位
本 Skill 负责生成：
1. PPT 大纲；
2. 逐页文案；
3. 页面设计说明；
4. `deck_spec.json` 草案。

本 Skill 不负责：
1. 直接生成正式 PPTX；
2. 修改其他 Skill；
3. 编造具体数据、参数、案例；
4. 在无依据时输出强事实断言。

如用户要求正式 PPTX，应转交：
```text
huawei_pptx_builder
```

## 2. 适用范围
本 Skill 适用于：
- 技术方案
- 战略规划
- 竞品对比
- 项目复盘
- 客户解决方案
- 资源申请
- 运营治理
- 产品路线图
- 调研分析
- 高层决策汇报

## 3. 目录职责与读取策略
### 3.1 最小必读 5 件套
执行任何任务时，必须优先读取：
1. `core/generation_workflow.md`
2. `core/topic_router.md`
3. `core/output_contracts.md`
4. `core/anti_overfit_rules.md`
5. `core/audience_rules.md`

### 3.2 条件读取规则
1. 先用 `topic_router` 判断是否命中主题包；
2. 未命中时，默认只读取 `domain_profiles/default_general.md`；
3. 仅当用户要求页面设计说明或 `deck_spec.json` 时，再读取 `visual_patterns/`；
4. 仅在输出前读取 `eval/` 做自检；
5. `templates/` 按任务需要读取，不要求机械全量串读。

## 4. 任务识别与输出路由
根据用户输入识别任务类型，可包括：
- `strategy_planning`
- `technical_solution`
- `competitive_comparison`
- `project_review`
- `customer_solution`
- `resource_request`
- `operation_governance`
- `product_roadmap`
- `research_report`
- `general_report`

根据用户要求选择输出模式：
1. 只要大纲 → 按 `core/output_contracts.md` 中 outline 契约输出；
2. 要逐页文案 → 按 page_copy 契约输出；
3. 要页面设计 → 按 page_design 契约输出；
4. 要 `deck_spec.json` → 严格按 deck_spec 契约输出 JSON。

## 5. 主题包隔离与反污染硬规则
默认主题包：
```text
domain_profiles/default_general.md
```

只有当用户主题明确命中时，才允许读取专属主题包。

如果主题未明确涉及 AI 算力/昇腾/NVIDIA，输出中不得无故出现：
- 昇腾
- 英伟达
- NVIDIA
- CUDA
- CANN
- MindSpore
- GPU
- NPU
- 模型迁移
- 模型适配
- 算力调度
- 算力云化
- AI算力底座

如出现，视为失败，必须重写。

## 6. 输出硬门禁
输出前必须满足：
1. 汇报对象明确；
2. 主线明确；
3. 标题结论化；
4. 每页只有一个核心判断；
5. 图表服务观点，不做装饰；
6. 版式可执行；
7. 不编造数据；
8. 无关主题不得被 AI 算力词污染；
9. `chart_type` 与 `layout_pattern` 不得混用；
10. 无证据时必须使用方向性、条件性措辞。

详细自检项见：
```text
eval/acceptance_checklist.md
eval/visual_scorecard.md
eval/domain_contamination_tests.md
```

## 7. 默认交付顺序
用户未明确要求 PPTX 时，默认输出：
1. PPT 大纲；
2. 逐页文案；
3. 页面设计说明；
4. `deck_spec.json`；
5. 最小依赖包：`templates/` 与 `visual_patterns/`；
6. `project/handoff/A_to_B.md`；
7. `deliverables/` 交付 zip。

如页数超过 10 页：
1. `project/work/` 仍保留完整主文件；
2. `deliverables/` 可按页码区间分包；
3. `A_to_B.md` 与 `status.md` 必须同步完整版本与分包清单。

## 8. 协作边界
### 角色 A：huawei_ppt_master
负责：大纲、逐页文案、页面设计、`deck_spec.json`。

不负责：
- 正式 PPTX；
- Skill 自我修改；
- 独立 QA 验收。

不得直接修改：
```text
skills/huawei_ppt_qa_reviewer/*
skills/huawei_ppt_skill_optimizer/*
project/review/*
```

### 其他角色
- 角色 B：`huawei_ppt_skill_optimizer` 负责 Skill 优化建议与 patch proposal；
- 角色 C：`huawei_pptx_builder` 负责正式 PPTX；
- 角色 D：`huawei_ppt_qa_reviewer` 负责独立验收与回归。

## 9. 失败与重写条件
出现以下任一情况，必须重写或提示补材料：
1. 非相关主题被 AI 算力内容污染；
2. 标题不是结论型；
3. 页面只有口号，没有抓手、路径、证据或决策建议；
4. 图表不可执行；
5. 页面设计无法指导 Builder；
6. 编造数据；
7. 擅自新增重要事实；
8. 与用户指定汇报对象不匹配。

## 10. 最小合格输出标准
最低必须做到：
1. 主题不跑偏；
2. 角色和汇报对象明确；
3. 章节逻辑清晰；
4. 标题结论化；
5. 每页一个核心判断；
6. 图表有承载信息；
7. 版式可执行；
8. 风格符合华为高层汇报；
9. 不编造事实；
10. 输出可进入下一阶段。
