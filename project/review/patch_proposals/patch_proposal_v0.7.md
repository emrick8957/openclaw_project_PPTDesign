# Patch Proposal v0.7

## 1. 基本信息
- 当前任务: `huawei_ppt_master` 参考材料学习能力升级
- patch 编号: PP-20260509-07
- 生成时间: 2026-05-09
- 类型: 可执行 patch proposal（实施前版本）
- 目标: 将 v0.6 的方向性方案收敛为可按文件实施、可分阶段合入、可回归验证的改造方案

## 2. 变更范围
### 2.1 修改文件
1. `skills/huawei_ppt_master/SKILL.md`
2. `skills/huawei_ppt_master/core/generation_workflow.md`
3. `skills/huawei_ppt_master/prompts/screenshot_analysis.md`
4. `skills/huawei_ppt_master/core/anti_overfit_rules.md`
5. `skills/huawei_ppt_master/core/topic_router.md`

### 2.2 新增文件/目录
1. `skills/huawei_ppt_master/core/reference_ingestion_workflow.md`
2. `skills/huawei_ppt_master/core/reference_material_policy.md`
3. `skills/huawei_ppt_master/methodology_patterns/`
4. `skills/huawei_ppt_master/methodology_patterns/executive_argument_patterns.md`
5. `skills/huawei_ppt_master/methodology_patterns/section_logic_patterns.md`
6. `skills/huawei_ppt_master/methodology_patterns/page_role_patterns.md`
7. `skills/huawei_ppt_master/methodology_patterns/industry_framework_extraction_rules.md`
8. `skills/huawei_ppt_master/eval/reference_learning_regression.md`

## 3. 合入策略
采用三阶段合入，避免一次性改太大。

### Phase 1：流程接入层（必须先做）
目标：先让 Skill 正式“认识到参考材料学习流程”。
- 修改 `SKILL.md`
- 修改 `core/generation_workflow.md`
- 新增 `core/reference_ingestion_workflow.md`
- 新增 `core/reference_material_policy.md`

### Phase 2：内容学习层（第二步）
目标：从只学视觉扩展到学表达与体系。
- 新增 `methodology_patterns/` 全部骨架文件
- 修改 `prompts/screenshot_analysis.md`

### Phase 3：控制与回归层（最后做）
目标：防止越学越乱，并建立长期迭代门禁。
- 修改 `core/anti_overfit_rules.md`
- 修改 `core/topic_router.md`
- 新增 `eval/reference_learning_regression.md`

## 4. 逐文件可执行变更块

### 4.1 `skills/huawei_ppt_master/SKILL.md`
#### 变更类型
- 新增章节
- 新增硬门禁条目
- 新增触发读取规则

#### 建议操作
1. 在 `## 1. Skill 定位` 后新增“参考材料学习与复用”章节；
2. 在“目录职责与读取策略”中新增“参考材料触发读取规则”；
3. 在“输出硬门禁”中增加 4 条与参考材料学习相关的边界规则。

#### 建议插入内容
直接采用：`project/review/drafts/reference_learning_file_level_draft_v0.1.md` 中第 2 节对应正文。

#### 合入判定
满足以下条件视为通过：
- 主文件已显式定义学习能力，而非只在 workflow 中隐含存在；
- 主文件已明确 reference workflow 是条件必读；
- 主文件已明确“图片不能直接当事实依据”等边界。

---

### 4.2 `skills/huawei_ppt_master/core/generation_workflow.md`
#### 变更类型
- 替换 Step 1
- 新增 Step 1.5
- 新增“沉淀结果复用”步骤

#### 建议操作
1. 扩展 Step 1 的输入识别维度；
2. 在 Step 1 后加入参考材料分类；
3. 在正式生成前增加规则复用检查。

#### 建议插入内容
直接采用草案第 3 节正文。

#### 合入判定
- workflow 中已能区分“从零生成”和“参考材料驱动生成”；
- workflow 中已给出 reference workflow 的入口；
- workflow 中已定义先复用沉淀规则、再生成的顺序。

---

### 4.3 新增 `skills/huawei_ppt_master/core/reference_ingestion_workflow.md`
#### 变更类型
- 新增文件

#### 最小必须包含的章节
1. 目标
2. 输入类型分类
3. 证据等级
4. 双通道抽取
5. 沉淀落位规则
6. 升级条件
7. 冲突处理
8. 复用优先级
9. 禁止事项

#### 建议正文来源
直接采用草案第 4 节正文。

#### 合入判定
- 能解释“新材料进来后先做什么”；
- 能解释“抽取后写到哪里”；
- 能解释“什么可以升格为长期规则”。

---

### 4.4 新增 `skills/huawei_ppt_master/core/reference_material_policy.md`
#### 变更类型
- 新增文件

#### 最小必须包含的章节
1. 目的
2. 图片/截图用途边界
3. PPT/PPTX 用途边界
4. 文本材料用途边界
5. 数据表用途边界
6. 输出时的事实降级要求

#### 建议正文来源
直接采用草案第 5 节正文。

#### 合入判定
- 视觉参考与事实依据已被明确分开；
- 未核验事实必须降级表达；
- 不同材料的默认用途清晰。

---

### 4.5 新增 `skills/huawei_ppt_master/methodology_patterns/`
#### 变更类型
- 新增目录与 4 个骨架文件

#### 文件要求
1. `executive_argument_patterns.md`
2. `section_logic_patterns.md`
3. `page_role_patterns.md`
4. `industry_framework_extraction_rules.md`

#### 最小目标
先建骨架，不要求首版内容过满，但必须明确：
- 学什么
- 适用边界
- 何时进入通用层
- 何时只保留为主题层

#### 建议正文来源
直接采用草案第 6 节骨架。

#### 合入判定
- Skill 已有明确的“体系层/内容套路层”承载位置；
- 不再只有 `visual_patterns/` 承接学习结果。

---

### 4.6 `skills/huawei_ppt_master/prompts/screenshot_analysis.md`
#### 变更类型
- 替换提示词正文

#### 建议操作
在保留原视觉抽取的基础上，增加：
- 页面角色
- 标题句式
- 论证结构
- 收口方式
- 通用规则 vs 主题知识的区分

#### 建议正文来源
直接采用草案第 7 节正文。

#### 合入判定
- 提示词不再只抽版式；
- 提示词已能引导输出内容套路层信息；
- 提示词已加入禁止把截图结论直接上升为全局知识的约束。

---

### 4.7 `skills/huawei_ppt_master/core/anti_overfit_rules.md`
#### 变更类型
- 新增章节

#### 建议操作
增加“参考材料学习过拟合控制”章节。

#### 必须覆盖的规则
1. 单份材料默认只能形成候选规则；
2. 至少跨两份材料复现，才考虑进入通用层；
3. 行业专属规律优先去主题层或方法论主题分支；
4. 参考材料增多不能放松事实核验。

#### 建议正文来源
直接采用草案第 8 节正文。

#### 合入判定
- 已覆盖“学习沉淀污染”而非只覆盖术语污染；
- 已定义升级门槛和降级策略。

---

### 4.8 `skills/huawei_ppt_master/core/topic_router.md`
#### 变更类型
- 新增章节

#### 建议操作
增加“主题知识包升级条件”章节。

#### 必须覆盖的规则
1. 不得因单次喂料立即写入 `domain_profiles/`；
2. 主题框架必须跨材料复现；
3. 必须具备跨任务复用价值；
4. 与通用规则冲突时不得强行提升。

#### 建议正文来源
直接采用草案第 9 节正文。

#### 合入判定
- topic_router 已能解释“主题知识从哪里来”；
- topic_router 已能约束持续喂料的升级门槛。

---

### 4.9 新增 `skills/huawei_ppt_master/eval/reference_learning_regression.md`
#### 变更类型
- 新增文件

#### 最小必须包含的章节
1. 目标
2. 视觉学习回归
3. 结构学习回归
4. 表达学习回归
5. 体系学习回归
6. 主题隔离回归
7. 增量稳定性回归
8. 一票否决项

#### 建议正文来源
采用草案第 10 节正文，并与 `project/review/regression_plan.md` 对齐。

#### 合入判定
- R1~R6 六类回归均有明确检查目标；
- 主题污染、事实误用、单客户规则全局化被列为一票否决。

## 5. 文件间依赖关系
1. `SKILL.md` 依赖 `reference_ingestion_workflow.md` 与 `reference_material_policy.md` 存在；
2. `generation_workflow.md` 依赖 reference workflow 存在；
3. `screenshot_analysis.md` 增强版最好在 `methodology_patterns/` 建立后再切换；
4. `anti_overfit_rules.md` 与 `topic_router.md` 应在 regression 文件上线前一并完成。

## 6. 实施顺序建议
### 实施批次 A（低风险）
- `SKILL.md`
- `core/generation_workflow.md`
- `core/reference_ingestion_workflow.md`
- `core/reference_material_policy.md`

### 实施批次 B（中风险）
- `methodology_patterns/` 4 个骨架文件
- `prompts/screenshot_analysis.md`

### 实施批次 C（控制层）
- `core/anti_overfit_rules.md`
- `core/topic_router.md`
- `eval/reference_learning_regression.md`

## 7. 回归执行要求
每个批次完成后最少检查：
- 批次 A：流程是否通，材料边界是否清
- 批次 B：是否真的开始学内容套路，而不只是学版式
- 批次 C：是否能挡住主题污染与单样例过拟合

完整回归维度按 `project/review/regression_plan.md` 执行。

## 8. 风险提醒
1. 最大风险不是改不动，而是“自动沉淀”做得太激进；
2. 首版不建议自动覆盖旧规则，只建议新增规则层和候选规则逻辑；
3. `methodology_patterns/` 首版先骨架化即可，别一口气塞满行业知识；
4. 若没有回归集，不要贸然宣称已具备稳定学习能力。

## 9. 建议结论
**建议按 v0.7 执行。**

理由：
- 已从方向性建议收敛到文件级执行块；
- 已明确分阶段、依赖、门槛与风险；
- 后续如果要真正落地改 Skill，可以直接基于本文件逐项实施。
