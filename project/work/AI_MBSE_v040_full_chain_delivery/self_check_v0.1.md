# 自检结果 v0.4.0

## 1. 基础校验

- JSON 解析：通过（生成阶段已序列化验证）
- 页面范围：P1-P12，共 12 页
- 四段式结构：Background / Catalyst / Application / Trends 已覆盖
- deck_spec v0.4.0 字段：每页包含 `core_judgement`、`chart_proof_goal`、`chart_visual_boundary`、`chart_semantic_mapping`
- 边界：未生成 PPTX；未使用 page_render_spec / normalized_render_model；未新增渲染 DSL

## 2. 模板印章检测

- N=12，repeat_threshold=max(3,ceil(N*0.5))=6
| 字段 | unique/N | max duplicate | threshold | 结果 |
|---|---:|---:|---:|---|
| `core_judgement` | 12/12 | 1 | 6 | PASS |
| `chart_proof_goal` | 11/12 | 2 | 6 | PASS |
| `chart_visual_boundary` | 12/12 | 1 | 6 | PASS |
| `visual_notes` | 12/12 | 1 | 6 | PASS |
| `speaker_notes` | 12/12 | 1 | 6 | PASS |

- 复述检测：PASS，未发现 core_judgement 等于 conclusion 或固定前缀复述
- 骨架填词检测：PASS，chart_proof_goal 均为关系证明描述
- 设计增量检测：PASS，每页 red_anchor、chart_visual_boundary、chart_semantic_mapping 和 page_design_overrides 均有差异化信号
- 允许重复项：global_design_defaults、页脚来源格式、基础配色、安全边距保留一致

## 3. 枚举校验

- chart_type：使用 chart_patterns.md 已定义枚举；通过
- layout_pattern：使用 layout_library.md 已定义枚举；通过
- chart_type 与 layout_pattern 未混用；通过

## 4. 主题污染检查

- 未引入与本主题无关的 AI 算力专属表达；通过

## 5. 结论

- FAIL 项：0
- 当前交付物可进入 B 侧评审。