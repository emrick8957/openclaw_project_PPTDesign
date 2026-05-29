# page_render_spec / normalized_render_model 相关文件梳理 v0.1

## 0. 本轮边界

- 用户确认：`page_render_spec` 方案已终止。
- 本轮只做文件梳理，不清理、不删除、不移动、不改写历史产物。
- 现行正式方向：仅保留简洁版 `deck_spec_field_dictionary` 作为后续正式交付支持资产；不恢复 `page_render_spec` / `normalized_render_model` / 渲染 DSL。

## 1. 可归档候选：page_render_spec Phase 0 方案冻结产物

目录：`project/work/page_render_spec_phase0/`

| 文件 | 性质 | 备注 |
|---|---|---|
| `README.md` | Phase 0 交付索引 | 历史方案索引 |
| `positioning_note_v0.1.md` | 定位说明 | 已被“方案终止”覆盖 |
| `page_render_spec_schema_draft_v0.1.json` | schema 草案 | 已终止，不应进入正式链路 |
| `light_full_trigger_rules_v0.1.md` | light/full 触发规则 | 已终止 |
| `a_c_boundary_plan_v0.1.md` | A/C 边界计划 | 历史方案材料 |

统计：5 个文件，约 15 KB。

## 2. 可归档候选：page_render_spec Phase 1 样例与 C 端消费说明

目录：`project/work/page_render_spec_phase1/`

### 2.1 核心样例

| 文件 | 性质 | 备注 |
|---|---|---|
| `page_render_specs/P07_page_render_spec_v0.1.json` | P7 样例 | 历史样例 |
| `page_render_specs/P08_page_render_spec_v0.1.json` | P8 样例 | 历史样例 |
| `page_render_specs/P14_page_render_spec_v0.1.json` | P14 样例 | 历史样例 |
| `page_render_spec_samples_v0.1.json` | 三页合并索引 | 历史样例集合 |

### 2.2 上游复制件 / 依赖复制件

| 文件 | 性质 | 备注 |
|---|---|---|
| `deck_spec.json` | 当时上游交付复制件 | 可随 Phase 1 一并归档 |
| `page_copy_v0.1.md` | 当时上游交付复制件 | 可随 Phase 1 一并归档 |
| `page_design_v0.1.md` | 当时上游交付复制件 | 可随 Phase 1 一并归档 |
| `dependencies/visual_rules.md` | 依赖复制件 | 源文件仍在 Skill 正式资产中 |
| `dependencies/chart_patterns.md` | 依赖复制件 | 源文件仍在 Skill 正式资产中 |
| `dependencies/wording_rules.md` | 依赖复制件 | 源文件仍在 Skill 正式资产中 |
| `dependencies/layout_library.md` | 依赖复制件 | 源文件仍在 Skill 正式资产中 |

### 2.3 角色 C 消费评估材料

| 文件 | 性质 | 备注 |
|---|---|---|
| `deck_spec_field_dictionary_for_role_C.md` | 临时 C 端字段说明 | 已被正式 `core/deck_spec_field_dictionary.md` 精简替代 |
| `page_render_spec_field_dictionary_for_role_C.md` | page_render_spec 字段说明 | 方案已终止 |
| `role_C_consumption_guide_v0.1.md` | C 端消费指南 | 含 normalized_render_model 后续方向，已终止 |
| `render_readiness_assessment_v0.1.md` | 可渲染性评估 | 记录终止原因，有历史价值 |

### 2.4 索引 / 自检

| 文件 | 性质 | 备注 |
|---|---|---|
| `README.md` | Phase 1 交付包说明 | 历史索引 |
| `self_check_v0.1.md` | JSON / 边界自检 | 历史记录 |

统计：17 个文件，约 222 KB。

## 3. 可归档候选：生成脚本与交付包

| 路径 | 性质 | 建议 |
|---|---|---|
| `project/work/generate_page_render_spec_phase1.py` | Phase 1 一次性生成脚本 | 可随 Phase 1 归档，避免误用 |
| `deliverables/page_render_spec_phase1_delivery.zip` | Phase 1 对外交付 zip | 可保留为历史交付包或移入 archive；本轮不处理 |

## 4. 需要更新但本轮不改：handoff 当前状态文件

| 路径 | 当前问题 | 建议 |
|---|---|---|
| `project/handoff/A_to_B.md` | 仍指向 `page_render_spec Phase 1`，并建议后续 `normalized_render_model` | 下轮可改为“方案已终止 / 历史交付归档 / 当前正式方向为 deck_spec_field_dictionary” |
| `project/handoff/status.md` | 仍记录 `next_recommended_phase: Phase 1.1 normalized_render_model...` | 下轮可改为终止状态，避免继续误触发 |

## 5. 正式 Skill 中的保留项：不是清理目标

这些文件包含“方案已终止、不恢复”的边界声明，或包含正式 `deck_spec_field_dictionary` 资产引用；建议保留。

| 文件 | 处理建议 |
|---|---|
| `skills/huawei_ppt_master/core/deck_spec_field_dictionary.md` | 正式保留 |
| `skills/huawei_ppt_master/README.md` | 保留，其中关于终止 page_render_spec 的说明是有效边界 |
| `skills/huawei_ppt_master/VERSION.md` | 保留版本记录 |
| `skills/huawei_ppt_master/CHANGELOG.md` | 保留变更记录 |
| `skills/huawei_ppt_master/INDEX.md` | 保留正式索引 |
| `skills/huawei_ppt_master/QUICK_INDEX.md` | 保留正式索引 |
| `skills/huawei_ppt_master/PACKAGE_MANIFEST.md` | 保留包清单 |
| `skills/huawei_ppt_master/SKILL.md` | 保留；当前只出现正式交付要求中的 `deck_spec_field_dictionary.md` |

## 6. 其他相关但非清理目标

| 路径 | 说明 |
|---|---|
| `project/work/update_readme_version_v038.py` | v0.3.8 文档同步脚本，记录终止边界 |
| `project/work/sync_v039_docs.py` | v0.3.9 文档同步脚本，记录“不恢复 page_render_spec / normalized_render_model” |
| `project/work/fix_manifest_v038.py` | v0.3.8 manifest 修复脚本，涉及 `deck_spec_field_dictionary` |
| `project/work/apply_v039_chart_semantic_mapping.py` | v0.3.9 字段增强脚本，涉及正式字段字典 |
| `project/work/generate_ai4mbse_four_page_delivery.py` | 四页交付生成脚本，明确未使用 page_render_spec / normalized_render_model |
| `project/work/AI4MBSE_P4_P7_P8_P14_delivery/` | 正式四页交付目录，其中依赖包含 `deck_spec_field_dictionary.md`；不是 page_render_spec 方案目录 |

## 7. 后续如需清理，建议顺序

> 本轮不执行，仅记录建议。

1. 先更新 `project/handoff/A_to_B.md` 与 `project/handoff/status.md`，把状态改为“page_render_spec / normalized_render_model 已终止”。
2. 将 `project/work/page_render_spec_phase0/`、`project/work/page_render_spec_phase1/`、`project/work/generate_page_render_spec_phase1.py`、`deliverables/page_render_spec_phase1_delivery.zip` 移入 archive 或打包留存。
3. 不动 `skills/huawei_ppt_master/core/deck_spec_field_dictionary.md` 及 v0.3.8/v0.3.9 版本记录。
4. 清理后再跑一次全文检索，确认仅剩“终止声明 / 正式字段字典 / 历史 changelog”类引用。
