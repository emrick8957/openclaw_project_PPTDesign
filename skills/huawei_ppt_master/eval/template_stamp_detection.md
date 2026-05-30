# 模板印章检测

## 1. 检测目标

识别 `deck_spec.json`、逐页文案和页面设计说明中因机械套版导致的重复字段、骨架填词和伪差异化。

字段职责与分层以 `core/field_differentiation_rules.md` 为唯一真相源。

## 2. 混合阈值模型

设：

```text
N = deck 页数
repeat_threshold = max(3, ceil(N * 0.5))
```

### 2.1 N <= 3 小包规则

- 对关键差异化字段做两两比较；
- 任意关键差异化字段全同：WARN；
- 两个及以上关键差异化字段全同：FAIL；
- `chart_visual_boundary` 或 `visual_notes` / page_design overrides 全同：FAIL；
- 若字段已下沉为 `global_design_defaults`，且每页 overrides 有足够差异，则不判 FAIL。

### 2.2 N >= 4 通用规则

- 关键差异化字段重复页数 >= `repeat_threshold`：FAIL；
- 关键差异化字段重复页数 >= 3 且 < `repeat_threshold`：WARN；
- 若字段已下沉为 `global_design_defaults`，且每页 overrides 有足够差异，则不判 FAIL；
- 页脚、基础配色、安全边距、全局负面风格边界等白名单字段不参与 FAIL 判定。

## 3. 必检字段

必检字段引用 `core/field_differentiation_rules.md` 的“必须逐页有设计增量”与“可半重复但必须带差异项”章节。

## 4. 语义检测

必须使用 `core/field_differentiation_rules.md` 中 `core_judgement`、`chart_proof_goal`、`chart_visual_boundary` 的 FAIL/PASS 特征与正反例进行判断。

## 5. 自检输出格式

每次生成交付物时，自检必须包含：

| 检查项 | 结果 | 证据 | 处理建议 |
|---|---|---|---|
| 重复字段统计 | PASS/WARN/FAIL | 字段名 + 重复页数 + 阈值 | 下沉全局默认 / 重写逐页字段 |
| 复述检测 | PASS/WARN/FAIL | 字段与来源文本 | 改为正当提炼或补充唯一带走点 |
| 骨架填词检测 | PASS/WARN/FAIL | 固定前后缀/关键词拼接证据 | 补充因果/对比/演进/闭环/决策关系 |
| 设计增量检测 | PASS/WARN/FAIL | 每页差异信号数量 | 补充主图/锚点/边界/讲解差异 |
| 允许重复项 | PASS | 白名单字段 | 保留或下沉全局默认 |

## 6. 失败处理

出现 FAIL 时，不得输出最终交付包；必须重写对应字段或将通用规则下沉为全局默认并补齐每页 overrides。
