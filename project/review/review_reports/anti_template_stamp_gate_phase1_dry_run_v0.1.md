# v0.4.0 anti-template-stamp-gate Phase 1 回归 dry-run

检测对象：`project/work/AI4MBSE_P4_P7_P8_P14_delivery/deck_spec.json`
N=4, repeat_threshold=3

- `page_goal`：unique=1/4，max_duplicate=4，status=ALLOW/WARN
- `core_judgement`：unique=4/4，max_duplicate=1，status=PASS
- `chart_proof_goal`：unique=4/4，max_duplicate=1，status=PASS
- `chart_visual_boundary`：unique=1/4，max_duplicate=4，status=FAIL
- `visual_notes`：unique=1/4，max_duplicate=4，status=FAIL
- `speaker_notes`：unique=1/4，max_duplicate=4，status=WARN
- `P4.core_judgement`：FAIL，字面复述 / 固定前缀 + conclusion
- `P4.chart_proof_goal`：WARN，疑似固定前缀 + 关键词拼接 + 固定后缀
- `P7.core_judgement`：FAIL，字面复述 / 固定前缀 + conclusion
- `P7.chart_proof_goal`：WARN，疑似固定前缀 + 关键词拼接 + 固定后缀
- `P8.core_judgement`：FAIL，字面复述 / 固定前缀 + conclusion
- `P8.chart_proof_goal`：WARN，疑似固定前缀 + 关键词拼接 + 固定后缀
- `P14.core_judgement`：FAIL，字面复述 / 固定前缀 + conclusion
- `P14.chart_proof_goal`：WARN，疑似固定前缀 + 关键词拼接 + 固定后缀

## 结论

- FAIL 项数量：6
- WARN 项数量：5
- ALLOW/WARN 项数量：1
- 旧四页交付包按 v0.4.0 门禁应判为不合格，符合 RT-00 预期。