# P4/P7/P8/P14 旧交付包模板印章检测 dry-run v0.1

检测对象：`project/work/AI4MBSE_P4_P7_P8_P14_delivery/deck_spec.json`

- `page_goal`：unique=1/4，max_duplicate=4，status=ALLOW/WARN
- `core_judgement`：unique=4/4，max_duplicate=1，status=PASS
- `chart_proof_goal`：unique=4/4，max_duplicate=1，status=PASS
- `chart_visual_boundary`：unique=1/4，max_duplicate=4，status=FAIL
- `visual_notes`：unique=1/4，max_duplicate=4，status=FAIL
- `speaker_notes`：unique=1/4，max_duplicate=4，status=WARN
- `P4.core_judgement`：FAIL，固定前缀 + conclusion
- `P4.chart_proof_goal`：WARN，疑似骨架填词
- `P7.core_judgement`：FAIL，固定前缀 + conclusion
- `P7.chart_proof_goal`：WARN，疑似骨架填词
- `P8.core_judgement`：FAIL，固定前缀 + conclusion
- `P8.chart_proof_goal`：WARN，疑似骨架填词
- `P14.core_judgement`：FAIL，固定前缀 + conclusion
- `P14.chart_proof_goal`：WARN，疑似骨架填词

## 结论

- FAIL 项数量：6
- WARN 项数量：6
- 预期：该旧交付包应被 Phase 1 门禁检出，不能只因 JSON/枚举合法而通过。