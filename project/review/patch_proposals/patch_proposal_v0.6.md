# Patch Proposal v0.6

## 1. 基本信息
- 当前任务: `huawei_ppt_master` 参考材料学习能力升级
- patch 编号: PP-20260509-06
- 生成时间: 2026-05-09
- 目标: 将 Skill 从“学样子、学结构、学表达习惯”升级到“学体系、学内容套路、学完自动沉淀并稳定复用”

## 2. 总体改造方向
1. 不改变 `huawei_ppt_master` 的核心定位，仍是 PPT 内容生成 Skill。
2. 新增一套“参考材料学习框架”，专门吸收持续提供的 PPT、PPT 图片、文本材料与数据材料。
3. 采用“双通道学习”：
   - 视觉通道: 配色、版式、图表、信息密度、页面结构
   - 内容通道: 章节逻辑、页型分工、标题句式、论证套路、收口方式、行业框架
4. 所有学习结果必须分层沉淀，避免把局部样例误写成全局规则。

## 3. 建议修改文件

### 3.1 `skills/huawei_ppt_master/SKILL.md`
- 对应 issue_id: ISSUE-201, ISSUE-203
- 原规则或缺失点: 只识别“是否有模板/截图/材料”，没有把持续学习能力作为一级能力定义。
- 新增/修改规则:
  1. 在 Skill 定位中新增“参考材料学习与复用”能力说明；
  2. 在执行流程中新增“若用户提供 PPT / PPT 图片，则先进入参考材料学习流程”；
  3. 明确学习目标分为样式层、结构层、表达层、体系层四层。
- 修改理由: 把学习能力从隐含能力升级为显式能力。
- 影响范围: 全局
- 回归测试建议: R1~R6 全量覆盖

### 3.2 `skills/huawei_ppt_master/core/generation_workflow.md`
- 对应 issue_id: ISSUE-203
- 原规则或缺失点: 缺少材料分类、抽取、沉淀与复用流程。
- 新增/修改规则:
  1. Step 1 后新增“参考材料识别与分类”；
  2. 接入 `reference_ingestion_workflow.md`；
  3. 在生成前优先读取最近沉淀的通用规则、主题规则与方法论规则。
- 修改理由: 让学习与生成形成闭环。
- 影响范围: 主流程
- 回归测试建议: R2, R4, R6

### 3.3 新增 `skills/huawei_ppt_master/core/reference_ingestion_workflow.md`
- 对应 issue_id: ISSUE-201, ISSUE-203, ISSUE-207
- 原规则或缺失点: 不存在
- 新增规则建议:
  1. 输入类型分类: PPT/PPTX、PDF截图、单页图片、多页图片、文本材料、数据表；
  2. 证据等级分类: 风格参考 / 结构参考 / 论证参考 / 事实依据；
  3. 双通道抽取: 视觉抽取 + 内容抽取；
  4. 沉淀落位: `templates/`、`visual_patterns/`、`methodology_patterns/`、`domain_profiles/`；
  5. 冲突处理: 通用规则优先保守，冲突内容降级为主题专属或单次案例；
  6. 复用原则: 生成时优先复用高置信、跨材料重复出现的规则。
- 修改理由: 这是学习能力闭环的核心文件。
- 影响范围: 新增核心流程文件
- 回归测试建议: R1~R6

### 3.4 新增 `skills/huawei_ppt_master/core/reference_material_policy.md`
- 对应 issue_id: ISSUE-207
- 原规则或缺失点: 不同材料类型的证据等级和用途边界不清。
- 新增规则建议:
  1. 图片默认只能作为视觉/结构参考，不可直接作为事实依据；
  2. PPT正文可作为表达与结构参考，涉及事实仍需核验来源；
  3. 数据表与权威文本可进入事实依据层；
  4. 未核验事实必须继续标注“待补材料/需确认”。
- 修改理由: 降低错误引用风险。
- 影响范围: 全局事实规则
- 回归测试建议: R5, R6

### 3.5 新增 `skills/huawei_ppt_master/methodology_patterns/`
- 对应 issue_id: ISSUE-202, ISSUE-206
- 原规则或缺失点: 缺少内容套路与体系层承载目录。
- 新增文件建议:
  - `methodology_patterns/executive_argument_patterns.md`
  - `methodology_patterns/section_logic_patterns.md`
  - `methodology_patterns/page_role_patterns.md`
  - `methodology_patterns/industry_framework_extraction_rules.md`
- 修改理由: 为“学体系、学内容套路”提供明确落点。
- 影响范围: 新增知识层
- 回归测试建议: R3, R4

### 3.6 `skills/huawei_ppt_master/prompts/screenshot_analysis.md`
- 对应 issue_id: ISSUE-202
- 原规则或缺失点: 只要求抽象版式，不要求抽象内容套路。
- 新增/修改规则:
  1. 保留原有视觉抽取项；
  2. 增加页面角色、章节位置、结论句式、论证结构、页面收口方式；
  3. 增加“哪些只能作为主题知识，不可上升为通用规则”的判断。
- 修改理由: 让截图学习从视觉扩展到结构与表达。
- 影响范围: 截图学习入口
- 回归测试建议: R1, R3, R4

### 3.7 `skills/huawei_ppt_master/core/anti_overfit_rules.md`
- 对应 issue_id: ISSUE-204
- 原规则或缺失点: 只防主题术语污染，未覆盖学习沉淀污染。
- 新增/修改规则:
  1. 禁止把单个参考材料的主题内容直接升格为全局规则；
  2. 同一规律至少满足“跨两份以上材料复现”才可进入通用层；
  3. 若只在单行业/单客户反复出现，应优先沉淀到 `domain_profiles/` 或 `methodology_patterns/` 的主题分支。
- 修改理由: 防止越学越偏。
- 影响范围: 全局边界控制
- 回归测试建议: R5, R6

### 3.8 `skills/huawei_ppt_master/core/topic_router.md`
- 对应 issue_id: ISSUE-206
- 原规则或缺失点: 只定义主题触发，不定义主题知识升级来源。
- 新增/修改规则:
  1. 新增“主题知识包升级条件”；
  2. 明确只有当行业框架在多份材料中稳定出现，才允许写入主题包；
  3. 对新材料先走临时参考，再决定是否升级为长期主题知识。
- 修改理由: 让持续喂料能稳定长成主题能力。
- 影响范围: 主题知识管理
- 回归测试建议: R4, R6

### 3.9 新增 `skills/huawei_ppt_master/eval/reference_learning_regression.md`
- 对应 issue_id: ISSUE-205
- 原规则或缺失点: 不存在学习能力专项回归。
- 新增规则建议:
  1. 视觉学习回归
  2. 结构学习回归
  3. 表达学习回归
  4. 体系学习回归
  5. 主题隔离回归
  6. 增量稳定性回归
- 修改理由: 没有回归，就无法安全迭代学习能力。
- 影响范围: 评测体系
- 回归测试建议: 文件本身即测试规范

## 4. 建议新增的最小规则骨架
```markdown
参考材料学习框架
1. 输入分类
2. 证据等级
3. 视觉抽取
4. 内容抽取
5. 沉淀落位
6. 冲突判断
7. 复用优先级
8. 回归验证
```

## 5. 合入建议
**建议合入。**

条件:
1. 先补 workflow 与 policy，再补 methodology 承载层；
2. 学习能力上线前必须补齐专项回归；
3. 不建议把“自动沉淀”理解为无门槛自动写全局规则，必须有分层与冲突控制。
