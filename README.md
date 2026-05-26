# huawei_ppt_master Skill v0.2

`huawei_ppt_master` 是一个通用华为风格 PPT 生成 Skill，用于生成：

1. PPT 大纲；
2. 逐页文案；
3. 页面设计说明；
4. 后续 PPTX 生成所需的结构化输入。

## v0.2 核心升级

v0.2 不再把“昇腾 vs 英伟达”作为默认主题，而是改为：

> 通用华为风格 PPT 生成内核 + 可条件触发的主题知识包 + 可复用版式库。

因此，当用户输入非 AI 算力主题，例如智慧园区、数据治理、网络安全、客户经营、项目复盘等，Skill 仍应输出大纲、文案和页面设计说明，并且不得无故引入昇腾、英伟达、CUDA、CANN、GPU/NPU、模型迁移等专属概念。

## 推荐安装路径

```text
<workspace>/skills/huawei_ppt_master/
```

## 推荐调用方式

```text
请启用 huawei_ppt_master。
生成《XXX》的华为风格 PPT 大纲。
要求：先输出大纲，不生成 PPTX；每页包含页标题、核心结论、建议图表、页面设计说明。
```

## 与其他角色的关系

```text
角色 A：huawei_ppt_master
负责生成大纲、逐页文案、页面设计说明。

角色 B：huawei_ppt_skill_optimizer
负责评审、回归测试、Skill 优化建议。

角色 C：huawei_pptx_builder
负责把已确认内容生成正式 PPTX。

角色 D：huawei_ppt_qa_reviewer，可选
负责独立验收大纲、文案、版式和 PPTX。
```
