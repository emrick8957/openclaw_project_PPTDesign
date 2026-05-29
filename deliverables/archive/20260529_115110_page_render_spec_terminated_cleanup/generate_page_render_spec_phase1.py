import json, shutil, zipfile
from pathlib import Path

root = Path.cwd()
out = root / 'project/work/page_render_spec_phase1'
spec_dir = out / 'page_render_specs'
dep_dir = out / 'dependencies'
for d in [out, spec_dir, dep_dir]:
    d.mkdir(parents=True, exist_ok=True)

# Copy requested upstream deliverables
copy_map = {
    root/'project/work/deck_spec_v0.1.json': out/'deck_spec.json',
    root/'project/work/page_copy_v0.1.md': out/'page_copy_v0.1.md',
    root/'project/work/page_design_v0.1.md': out/'page_design_v0.1.md',
    root/'skills/huawei_ppt_master/templates/visual_rules.md': dep_dir/'visual_rules.md',
    root/'skills/huawei_ppt_master/templates/chart_patterns.md': dep_dir/'chart_patterns.md',
    root/'skills/huawei_ppt_master/templates/wording_rules.md': dep_dir/'wording_rules.md',
    root/'skills/huawei_ppt_master/visual_patterns/layout_library.md': dep_dir/'layout_library.md',
}
for src, dst in copy_map.items():
    shutil.copy2(src, dst)

deck = json.loads((root/'project/work/deck_spec_v0.1.json').read_text(encoding='utf-8-sig'))
slides = {s['slide_no']: s for s in deck['slides']}

def derived(s, *, bottom=None, right=None, red=None, hierarchy=None, spacing=None, simplify=None):
    d = {
        'title': s['title'],
        'core_judgement': s['core_judgement'],
        'layout_pattern': s['layout_pattern'],
        'chart_type': s['chart_type'],
        'chart_proof_goal': s['chart_proof_goal'],
        'chart_visual_boundary': s['chart_visual_boundary'],
        'bottom_conclusion': bottom or s.get('conclusion',''),
        'right_insight_panel': right or {},
        'red_anchor': red or {'target': (s.get('must_highlight') or s.get('visual_focus') or ['核心判断'])[0], 'budget': '普通正文页红色面积≤5%，仅保留一个主红色锚点'},
        'card_hierarchy': hierarchy or '主图优先，辅助说明弱化；不得所有组件等权',
        'spacing_rule': spacing or '标题区约12%，主体区约78%，页脚区约5%；模块间距大于卡片内边距',
        'visual_simplification': simplify or '删除装饰性图标、复杂背景、论文截图式长段落；保留白底、浅灰边框、红黑灰层级'
    }
    return d

def source_trace(slide_no):
    return {
        'deck_spec_ref': f'project/work/deck_spec_v0.1.json#/slides/{slide_no}',
        'page_design_ref': f'project/work/page_design_v0.1.md#P{slide_no}',
        'page_copy_ref': f'project/work/page_copy_v0.1.md#P{slide_no}',
        'source_evidence_ref': 'project/work/source_evidence_manifest_v0.1.json',
        'inherited_fields': ['title','core_judgement','layout_pattern','chart_type','chart_proof_goal','chart_visual_boundary','conclusion','display_text','visual_focus','must_highlight','text_density','data_gaps']
    }

base_validation = [
    '标题不超过2行，不能挤压主体区',
    '主红色锚点只有1个，普通正文页红色面积控制在5%以内',
    '主图必须能解释标题判断和chart_proof_goal',
    '页脚固定在底部约5%安全区，来源信息弱化',
    '不得新增deck_spec/page_copy/page_design之外的新事实或新判断'
]

p7 = slides[7]
spec7 = {
    'schema_version': '0.1',
    'deck_id': 'AI4MBSE_自动化生产系统_论文解读',
    'slide_no': 7,
    'page_id': 'P07_dual_v_lifecycle_architecture',
    'spec_level': 'full',
    'page_risk_level': 'complex',
    'trigger_reason': ['complex_layout','strict_chart_semantics','right_insight_panel','architecture_or_lifecycle'],
    'source_trace': source_trace(7),
    'derived_contract': derived(
        p7,
        right={'headline':'统一生命周期工程底座', 'items':['七类 AI 介入点必须映射到产品/生产双 V 生命周期','右侧洞察只解释主图，不另起一套管理建议','AI 介入点不得画成孤立散点']},
        hierarchy='双V生命周期主图为primary；七类介入点为secondary标签；右侧洞察为supporting，不得抢主图焦点'
    ),
    'subtype': {'subtype_enum':'dual_v_lifecycle_architecture'},
    'render_units': [
        {'unit_id':'title','unit_type':'title','semantic_role':'页面唯一判断','content_source':{'from':'deck_spec','field':'title','no_new_content':True},'priority':'primary','region_intent':'顶部12%标题区，左对齐，1–2行','max_text_lines':2,'overflow_action':'compress','visual_constraints':['仅允许标题关键词轻量红色强调']},
        {'unit_id':'dual_v_main','unit_type':'chart','semantic_role':'表达产品V与生产V的生命周期映射关系','content_source':{'from':'deck_spec','field':'chart_data.nodes/edges','no_new_content':True},'priority':'primary','region_intent':'主体左中部约68%宽度，形成双V/闭环主图','max_text_lines':0,'overflow_action':'manual_review','visual_constraints':['双V两侧对称但不等权堆叠','箭头必须表示生命周期流向','七类介入点围绕对应阶段贴标，不得散点漂浮']},
        {'unit_id':'ai_touchpoints','unit_type':'icon_label','semantic_role':'七类AI介入点标签','content_source':{'from':'page_copy','field':'P7 正文模块/关键要点','no_new_content':True},'priority':'secondary','region_intent':'贴附于双V阶段节点，短标签化','max_text_lines':1,'overflow_action':'compress','visual_constraints':['标签统一灰底细边框，仅关键介入点用红色细线连接']},
        {'unit_id':'right_insight','unit_type':'right_insight','semantic_role':'解释主图的管理含义','content_source':{'from':'deck_spec','field':'conclusion','no_new_content':True},'priority':'supporting','region_intent':'右侧洞察栏25%–30%宽度，1句结论+3条短要点','max_text_lines':5,'overflow_action':'truncate_with_review','visual_constraints':['右侧栏不得变成长段文字','只解释主图，不新增事实']},
        {'unit_id':'footer','unit_type':'footer','semantic_role':'来源和页码','content_source':{'from':'page_design','field':'P7 页脚','no_new_content':True},'priority':'tertiary','region_intent':'底部5%安全区','max_text_lines':1,'overflow_action':'compress','visual_constraints':['浅灰8–10pt，不进入主体区']}
    ],
    'text_fit_policy': {'title_max_lines':2,'card_title_max_lines':1,'card_body_max_lines':2,'bottom_conclusion_max_lines':2,'right_insight_max_items':3,'compression_order':['右侧洞察说明','介入点标签说明','标题副句'],'manual_review_threshold':'双V节点标签超过7个或右侧洞察超过3条时进入人工评审'},
    'render_unit_policy': {'red_anchor_budget':'≤5%；仅“双 V 模型”或生命周期主线使用红色','primary_focus_count':1,'card_hierarchy_rule':'主图>介入点标签>右侧洞察>页脚','bottom_bar_rule':'不使用厚重底部红条；如需收口仅浅灰底+细红线','right_insight_rule':'1句判断+最多3条短要点，宽度25%–30%','spacing_rule':'主图与洞察栏间距≥卡片内边距1.5倍；页脚独立','forbidden_patterns':['散点式AI标签','双V左右各讲一套','红色箭头过多','论文截图式长段落']},
    'render_validation': {'must_pass': base_validation + ['七类AI介入点能映射到生命周期阶段','右侧洞察解释主图而非新增内容'], 'manual_review_if':['节点/标签遮挡导致生命周期不可读','C端无法画出双V关系而退化为普通流程图','红色连接线超过主图注意力预算'], 'expected_builder_behavior':['优先生成双V生命周期主图','无法实现时返回manual_review，不静默改成普通四卡片']}
}

p8 = slides[8]
spec8 = {
    'schema_version': '0.1',
    'deck_id': 'AI4MBSE_自动化生产系统_论文解读',
    'slide_no': 8,
    'page_id': 'P08_self_learning_digital_twin_architecture',
    'spec_level': 'full',
    'page_risk_level': 'high_risk',
    'trigger_reason': ['complex_layout','strict_chart_semantics','architecture_or_lifecycle','bottom_conclusion_sensitive'],
    'source_trace': source_trace(8),
    'derived_contract': derived(
        p8,
        bottom=p8['conclusion'],
        hierarchy='四层架构自下而上；真实系统层与治理闭环层形成回路；不得退化为静态堆栈',
        red={'target':'真实系统—语义模型—AI/XAI 闭环主线','budget':'红色仅用于闭环回写箭头或唯一核心节点，面积≤5%'}
    ),
    'subtype': {'subtype_enum':'self_learning_digital_twin_architecture'},
    'render_units': [
        {'unit_id':'title','unit_type':'title','semantic_role':'页面唯一判断','content_source':{'from':'deck_spec','field':'title','no_new_content':True},'priority':'primary','region_intent':'顶部12%标题区','max_text_lines':2,'overflow_action':'compress','visual_constraints':['标题保持强判断，不改写为名词标题']},
        {'unit_id':'layer_stack','unit_type':'chart','semantic_role':'真实系统、语义模型、仿真AI、治理闭环的分层架构','content_source':{'from':'deck_spec','field':'chart_data.layers','no_new_content':True},'priority':'primary','region_intent':'主体中部，四层横向堆栈，占宽70%–80%','max_text_lines':0,'overflow_action':'manual_review','visual_constraints':['层级顺序清晰','每层最多4个短标签','不得把层级画成等权卡片墙']},
        {'unit_id':'feedback_loop','unit_type':'arrow','semantic_role':'表达自学习回写闭环','content_source':{'from':'deck_spec','field':'chart_proof_goal','no_new_content':True},'priority':'primary','region_intent':'从治理闭环层回指语义模型层/真实系统层的细红闭环箭头','max_text_lines':1,'overflow_action':'compress','visual_constraints':['闭环箭头是唯一红色主锚点','箭头不穿越正文文字']},
        {'unit_id':'bottom_conclusion','unit_type':'bottom_conclusion','semantic_role':'页面底部收口','content_source':{'from':'deck_spec','field':'conclusion','no_new_content':True},'priority':'secondary','region_intent':'主体底部浅灰结论区，不超过页面高度8%','max_text_lines':2,'overflow_action':'compress','visual_constraints':['浅灰底+窄红线，不用厚重红底','不得重复标题全文']},
        {'unit_id':'footer','unit_type':'footer','semantic_role':'来源和页码','content_source':{'from':'page_design','field':'P8 页脚','no_new_content':True},'priority':'tertiary','region_intent':'底部5%安全区','max_text_lines':1,'overflow_action':'compress','visual_constraints':['浅灰8–10pt']}
    ],
    'text_fit_policy': {'title_max_lines':2,'card_title_max_lines':1,'card_body_max_lines':2,'bottom_conclusion_max_lines':2,'right_insight_max_items':0,'compression_order':['层内item说明','底部结论','标题副句'],'manual_review_threshold':'任一层超过4个item或底部结论超过2行时进入人工评审'},
    'render_unit_policy': {'red_anchor_budget':'≤5%；仅闭环箭头或核心节点可用红色','primary_focus_count':1,'card_hierarchy_rule':'四层架构主图为唯一主体；底部结论弱收口','bottom_bar_rule':'允许浅灰底部结论区，高度≤8%，禁止红底横幅','right_insight_rule':'本页不设右侧洞察栏，避免压缩架构主体','spacing_rule':'层间距稳定，层内标签对齐；页脚与底部结论区分离','forbidden_patterns':['静态四层堆叠无闭环','满屏节点','多条红色箭头抢焦点','把AI/XAI画成孤立模块']},
    'render_validation': {'must_pass': base_validation + ['必须看出真实系统、语义模型、仿真AI、治理闭环四层关系','必须看出自学习回写闭环'], 'manual_review_if':['闭环箭头不可读','层级标签溢出','底部结论条压迫主体区'], 'expected_builder_behavior':['优先生成分层架构+闭环箭头','无法表达闭环时返回manual_review']}
}

p14 = slides[14]
spec14 = {
    'schema_version': '0.1',
    'deck_id': 'AI4MBSE_自动化生产系统_论文解读',
    'slide_no': 14,
    'page_id': 'P14_decision_closeout',
    'spec_level': 'full',
    'page_risk_level': 'high_risk',
    'trigger_reason': ['strict_chart_semantics','bottom_conclusion_sensitive','decision_closeout','high_text_density'],
    'source_trace': source_trace(14),
    'derived_contract': derived(
        p14,
        bottom='高层拍板重点：样板场景、接口机制、AI回写治理三项必须同步定义责任与验收产出。',
        red={'target':'拍板事项卡','budget':'红色只用于拍板事项主卡或关键风险标记，面积≤5%'},
        hierarchy='拍板事项卡为primary；执行清单表为secondary；风险/责任收口为supporting'
    ),
    'subtype': {'subtype_enum':'decision_closeout'},
    'render_units': [
        {'unit_id':'title','unit_type':'title','semantic_role':'最终决策判断','content_source':{'from':'deck_spec','field':'title','no_new_content':True},'priority':'primary','region_intent':'顶部12%标题区','max_text_lines':2,'overflow_action':'compress','visual_constraints':['标题必须保留“不是单个AI场景，而是机制”判断结构']},
        {'unit_id':'decision_card','unit_type':'card','semantic_role':'高层拍板事项主卡','content_source':{'from':'deck_spec','field':'conclusion','no_new_content':True},'priority':'primary','region_intent':'主体左上或顶部主卡，占主体高度20%–25%','max_text_lines':3,'overflow_action':'compress','visual_constraints':['唯一红色锚点','不得与表格等权']},
        {'unit_id':'decision_table','unit_type':'table','semantic_role':'资源、责任、阶段产出执行清单','content_source':{'from':'deck_spec','field':'chart_data.rows','no_new_content':True},'priority':'secondary','region_intent':'主体中部表格，3行4列，浅灰线框','max_text_lines':2,'overflow_action':'truncate_with_review','visual_constraints':['表格不做Excel重网格','首列可轻强调，其他列灰黑层级','每格短语化']},
        {'unit_id':'bottom_conclusion','unit_type':'bottom_conclusion','semantic_role':'最终收口和下一步动作','content_source':{'from':'page_render_spec','field':'derived_contract.bottom_conclusion','no_new_content':True},'priority':'secondary','region_intent':'底部浅灰收口区，高度≤8%','max_text_lines':2,'overflow_action':'compress','visual_constraints':['浅灰底+窄红线','不使用厚红条']},
        {'unit_id':'footer','unit_type':'footer','semantic_role':'来源和页码','content_source':{'from':'page_design','field':'P14 页脚','no_new_content':True},'priority':'tertiary','region_intent':'底部5%安全区','max_text_lines':1,'overflow_action':'compress','visual_constraints':['浅灰8–10pt']}
    ],
    'text_fit_policy': {'title_max_lines':2,'card_title_max_lines':1,'card_body_max_lines':3,'bottom_conclusion_max_lines':2,'right_insight_max_items':0,'compression_order':['表格单元格说明','拍板主卡说明','底部收口句'],'manual_review_threshold':'表格超过3行4列、单元格超过2行或拍板卡超过3行时进入人工评审'},
    'render_unit_policy': {'red_anchor_budget':'≤5%；只给拍板事项主卡/关键风险，不给整表红底','primary_focus_count':1,'card_hierarchy_rule':'拍板事项卡>执行清单表>底部收口>页脚','bottom_bar_rule':'允许浅灰底部收口区，高度≤8%，禁止厚重红底条','right_insight_rule':'本页不设右侧洞察栏，避免表格和洞察双焦点','spacing_rule':'主卡与表格间距≥卡片内边距1.5倍；底部收口与页脚分离','forbidden_patterns':['整页Excel表格','表格吞没决策结论','多个红色表头','只罗列事项无拍板动作']},
    'render_validation': {'must_pass': base_validation + ['拍板事项必须独立突出','表格只承载责任/资源/时点/产出，不吞没结论','底部形成明确管理收口'], 'manual_review_if':['表格视觉强于拍板卡','底部结论超过2行','C端将本页退化为普通风险矩阵'], 'expected_builder_behavior':['生成拍板主卡+执行清单表+底部收口结构','无法突出拍板卡时返回manual_review']}
}

for no, spec in [(7,spec7),(8,spec8),(14,spec14)]:
    (spec_dir/f'P{no:02d}_page_render_spec_v0.1.json').write_text(json.dumps(spec, ensure_ascii=False, indent=2), encoding='utf-8')

# Combined index JSON
combined = {
    'schema_version': '0.1',
    'deck_id': 'AI4MBSE_自动化生产系统_论文解读',
    'positioning': 'Phase 1 manual pilot samples only; not integrated into default chain.',
    'samples': [json.loads((spec_dir/f'P{no:02d}_page_render_spec_v0.1.json').read_text(encoding='utf-8')) for no in [7,8,14]]
}
(out/'page_render_spec_samples_v0.1.json').write_text(json.dumps(combined, ensure_ascii=False, indent=2), encoding='utf-8')

readme = '''# page_render_spec Phase 1 交付包

## 范围

本目录为 Phase 1 手工样例交付，不修改 `skills/huawei_ppt_master/*`，不接入默认生成链路。

## 本次包含

### 三页样例 page_render_spec

- `page_render_specs/P07_page_render_spec_v0.1.json`
- `page_render_specs/P08_page_render_spec_v0.1.json`
- `page_render_specs/P14_page_render_spec_v0.1.json`
- `page_render_spec_samples_v0.1.json`：三页合并索引

### 上游交付物

- `deck_spec.json`
- `page_copy_v0.1.md`
- `page_design_v0.1.md`

### 依赖文件

- `dependencies/visual_rules.md`
- `dependencies/chart_patterns.md`
- `dependencies/wording_rules.md`
- `dependencies/layout_library.md`

## 样例页选择理由

- P7：双 V 生命周期架构，验证复杂关系与右侧洞察栏约束；
- P8：自学习数字孪生架构，验证分层架构 + 闭环箭头 + 底部结论；
- P14：决策收口页，验证拍板事项卡 + 执行表格 + 管理收口。

## 边界

- `page_render_spec` 只继承/约束 `deck_spec/page_design/page_copy`，不新增事实判断；
- `layout_pattern`、`chart_type`、`bottom_conclusion`、`right_insight_panel` 均为派生字段；
- C 端无法满足约束时应返回 `manual_review`，不得静默改写内容。
'''
(out/'README.md').write_text(readme, encoding='utf-8')

self_check = '''# page_render_spec Phase 1 自检 v0.1

## JSON 校验

- 三个单页 `page_render_spec`：已通过 JSON 解析；
- 合并 `page_render_spec_samples_v0.1.json`：已通过 JSON 解析。

## 边界校验

- 未修改 `skills/huawei_ppt_master/*`；
- 未把 `page_render_spec` 接入默认交付链；
- 三页样例均只引用/继承 `deck_spec/page_copy/page_design`；
- 未新增论文之外的新事实；
- `chart_type` 与 `layout_pattern` 均沿用既有合法枚举。

## 关键风险

- P7 双 V 关系对 C 端绘图能力要求较高，若无法稳定表达，应进入 `manual_review`；
- P8 需要验证闭环箭头是否会造成红色面积超标；
- P14 需防止被渲染成 Excel 式大表，拍板事项必须独立突出。
'''
(out/'self_check_v0.1.md').write_text(self_check, encoding='utf-8')

# Validate JSON
for p in list(spec_dir.glob('*.json')) + [out/'page_render_spec_samples_v0.1.json', out/'deck_spec.json']:
    json.loads(p.read_text(encoding='utf-8-sig'))

# Handoff/status
handoff = '''# A_to_B handoff：page_render_spec Phase 1

## 本次交付

已完成 Phase 1 手工样例与配套交付物，目录：

`project/work/page_render_spec_phase1/`

## 文件清单

- 三页样例：`page_render_specs/P07_page_render_spec_v0.1.json`、`P08_page_render_spec_v0.1.json`、`P14_page_render_spec_v0.1.json`
- 合并索引：`page_render_spec_samples_v0.1.json`
- 上游交付物：`deck_spec.json`、`page_copy_v0.1.md`、`page_design_v0.1.md`
- 依赖：`dependencies/visual_rules.md`、`chart_patterns.md`、`wording_rules.md`、`layout_library.md`
- 自检：`self_check_v0.1.md`

## 边界声明

- 未修改 `skills/huawei_ppt_master/*`；
- 未接入默认链路；
- 本次是 Phase 1 手工样例，用于评审 schema 字段是否可被 C 端消费；
- C 端无法满足约束时应返回 `manual_review`，不得静默改写页面判断。

## 建议评审点

1. P7 双 V 生命周期结构是否足够明确；
2. P8 分层架构 + 闭环箭头是否能稳定渲染；
3. P14 决策收口是否避免退化为 Excel 表格；
4. `text_fit_policy` 和 `render_validation` 是否可执行；
5. 是否进入 Phase 2 扩展更多人工样本。
'''
(root/'project/handoff/A_to_B.md').write_text(handoff, encoding='utf-8')
(root/'project/handoff/status.md').write_text('# status\n\n- task: page_render_spec Phase 1\n- status: completed\n- skill_modified: false\n- default_chain_integrated: false\n- artifacts_dir: project/work/page_render_spec_phase1\n- sample_pages: P7, P8, P14\n- included_upstream_artifacts: deck_spec.json, page_copy_v0.1.md, page_design_v0.1.md\n- included_dependencies: visual_rules.md, chart_patterns.md, wording_rules.md, layout_library.md\n- next_recommended_phase: Phase 2 manual samples or Phase 3 C-consumption validation\n', encoding='utf-8')

# Zip deliverable
zip_path = root/'deliverables/page_render_spec_phase1_delivery.zip'
zip_path.parent.mkdir(parents=True, exist_ok=True)
if zip_path.exists():
    zip_path.unlink()
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for p in out.rglob('*'):
        if p.is_file():
            z.write(p, p.relative_to(out.parent))

print('phase1_done=true')
print('artifact_dir=project/work/page_render_spec_phase1')
print('zip=deliverables/page_render_spec_phase1_delivery.zip')
print('json_files_valid=', len(list(spec_dir.glob('*.json'))) + 2)
