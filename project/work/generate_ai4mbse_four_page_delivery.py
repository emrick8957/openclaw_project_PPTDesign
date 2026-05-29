import json, re, shutil, zipfile
from pathlib import Path

root = Path.cwd()
out = root / 'project/work/AI4MBSE_P4_P7_P8_P14_delivery'
dep = out / 'dependencies'
out.mkdir(parents=True, exist_ok=True)
dep.mkdir(parents=True, exist_ok=True)

pages = [4,7,8,14]
source_deck = json.loads((root/'project/work/deck_spec_v0.1.json').read_text(encoding='utf-8-sig'))
slides_by_no = {s['slide_no']: s for s in source_deck['slides']}
subset = []

def mapping_for(slide):
    no = slide['slide_no']
    if no == 4:
        return {
            'chart_reading_intent': '读者应判断：外部复杂度、竞争和可持续压力正在上升，而孤立 AI 应用不足以支撑系统级工程决策，必须转向工程流程与语义底座重构。',
            'main_visual_logic': '趋势曲线表达从“复杂度压力上升”到“单点 AI 暴露瓶颈”，再到“工程流程重构成为必要动作”的阶段转换；拐点不是收益数字，而是管理认知从工具导入转向系统工程升级。',
            'axis_semantics': {
                'x_axis': '阶段序列：外部压力上升 → 单点 AI 瓶颈暴露 → 工程流程重构，不代表精确年份',
                'y_axis': '系统级工程决策压力/复杂度示意，不代表量化指标'
            },
            'stage_or_node_meaning': {
                '复杂度上升': '客户期望、全球竞争、可持续要求和产业转型共同推高工程复杂度',
                'AI 孤岛': 'AI 有潜力但仍多停留在孤立应用，缺少工程语义上下文和流程闭环',
                '工程流程变革': '需要通过 MBSE、语义模型和治理机制支撑系统级决策'
            },
            'insight_panel_logic': [
                '右侧洞察应解释为什么复杂度压力会暴露单点 AI 的不足',
                '策略建议必须从“单点 AI 不足”推导到“先重构工程过程和语义底座”'
            ],
            'forbidden_visualization': [
                '不得画成无来源的精确增长曲线',
                '不得用大红上升箭头暗示确定收益或市场规模增长',
                '不得让右侧洞察变成与曲线无关的背景备注'
            ]
        }
    if no == 7:
        return {
            'chart_reading_intent': '读者应判断：AI 介入点不是零散工具点，而是覆盖产品与生产双 V 生命周期的系统性工程能力。',
            'main_visual_logic': '主图通过产品/生产双 V 生命周期主线承载七类 AI 介入点，证明 AI+MBSE 必须贯穿设计、验证、运行和回收，而不是停留在局部算法应用。',
            'axis_semantics': {},
            'stage_or_node_meaning': {
                '产品运行': '真实产品运行数据进入生命周期反馈',
                '生产运行': '生产系统运行数据进入工程模型与优化闭环',
                '回收': '生命周期末端信息反哺产品与生产系统设计',
                '产品设计': 'AI 支撑产品模型生成、约束检查和方案探索',
                '生产系统设计': 'AI 支撑产线、工艺和资源配置设计',
                '产品验证': 'AI 与仿真共同支撑产品侧验证',
                '生产系统验证': 'AI 与仿真共同支撑生产系统侧验证'
            },
            'insight_panel_logic': [
                '右侧洞察只解释七类介入点为何要求统一生命周期底座',
                '不得新增与双 V 主图无关的管理口号'
            ],
            'forbidden_visualization': [
                '不得画成七个孤立散点或普通清单',
                '不得把产品 V 和生产 V 画成互不关联的两套图',
                '不得把 AI 节点全部标红导致主线失焦'
            ]
        }
    if no == 8:
        return {
            'chart_reading_intent': '读者应判断：自学习数字孪生的关键不是单个模型，而是真实系统、语义模型、仿真和 AI/XAI 进入同一闭环。',
            'main_visual_logic': '分层架构自下而上展示真实系统层、语义模型层、仿真与 AI 层、治理闭环层，并通过回写关系证明“自学习”来自跨层反馈而非静态堆栈。',
            'axis_semantics': {},
            'stage_or_node_meaning': {
                '真实系统层': '产品、生产系统、传感器/PPS/外部数据提供现实状态输入',
                '语义模型层': '产品模型、生产模型、行为模型和知识图谱提供统一上下文',
                '仿真与 AI 层': 'FMU、共仿真、ML/XAI 承担学习、验证和解释',
                '治理闭环层': '解释、因果/合理性检查和模型回写形成可审查闭环'
            },
            'insight_panel_logic': [
                '如设置洞察栏，只解释各层为何必须闭环连接',
                '底部结论应收口到“同一闭环”，不能重复层级名称'
            ],
            'forbidden_visualization': [
                '不得画成静态四层堆栈而没有反馈/回写语义',
                '不得把 AI/XAI 画成孤立万能模块',
                '不得让每层文字过多导致架构图退化为表格'
            ]
        }
    if no == 14:
        return {
            'chart_reading_intent': '读者应判断：高层需要拍板的是工程体系升级机制，而不是单个 AI 场景试点。',
            'main_visual_logic': '决策表用“拍板事项—推荐方案—资源/责任—阶段产出”证明样板选择、接口机制和 AI 回写治理必须同步定义，形成可执行闭环。',
            'axis_semantics': {},
            'stage_or_node_meaning': {
                '样板场景': '先选择自动化装配/产线样板，形成语义模型 MVP',
                '接口机制': '定义 FMU/工具链接入边界，形成共仿真原型',
                'AI 回写治理': '建立 XAI 审查与责任闭环，形成可审查模型回写机制'
            },
            'insight_panel_logic': [
                '本页优先使用拍板事项卡和执行清单表，不建议另设右侧洞察栏',
                '底部收口应提示需要明确责任、接口和验收产出'
            ],
            'forbidden_visualization': [
                '不得画成全页 Excel 大表',
                '不得让表格吞没拍板事项',
                '不得只列原则而缺少责任、资源和阶段产出'
            ]
        }
    return {}

for no in pages:
    slide = dict(slides_by_no[no])
    slide['chart_semantic_mapping'] = mapping_for(slide)
    # Improve P4 trend chart data wording to avoid fake precision while preserving structure
    if no == 4:
        slide['chart_data'] = {
            'x_axis': ['复杂度压力上升', '单点 AI 瓶颈暴露', '工程流程重构'],
            'series': [{'name': '系统级工程决策压力（示意）', 'values': [1, 2, 3]}],
            'annotations': [{'x': '单点 AI 瓶颈暴露', 'label': 'AI 孤岛难以支撑系统级决策'}]
        }
    subset.append(slide)

out_deck = {
    'deck_title': 'AI 在自动化生产系统 MBSE 中的应用：P4/P7/P8/P14 四页交付物',
    'audience': source_deck['audience'],
    'style': source_deck['style'],
    'source': source_deck.get('source',''),
    'version_note': 'Generated under huawei_ppt_master v0.3.9-chart-semantic-mapping; includes chart_semantic_mapping for the four selected pages.',
    'slides': subset
}
(out/'deck_spec.json').write_text(json.dumps(out_deck, ensure_ascii=False, indent=2), encoding='utf-8')

# Extract page blocks from markdown
def extract_blocks(text, nums, heading_re):
    blocks=[]
    for n in nums:
        pat = re.compile(rf'(^## P{n}\b.*?)(?=^## P\d+\b|\Z)', re.S|re.M)
        m=pat.search(text)
        if m:
            blocks.append(m.group(1).strip())
        else:
            raise SystemExit(f'missing P{n}')
    return '\n\n\n'.join(blocks)+'\n'

copy_src=(root/'project/work/page_copy_v0.1.md').read_text(encoding='utf-8')
design_src=(root/'project/work/page_design_v0.1.md').read_text(encoding='utf-8')
page_copy = '# AI+MBSE 自动化生产系统论文解读逐页文案：P4/P7/P8/P14\n\n' + extract_blocks(copy_src, pages, None)
page_design = '# AI+MBSE 自动化生产系统论文解读页面设计说明：P4/P7/P8/P14\n\n' + extract_blocks(design_src, pages, None)
# Add v0.3.9 note to design
page_design += '\n## v0.3.9 图表语义说明\n\n- P4 `trend_curve` 必须按 deck_spec 中 `chart_semantic_mapping` 解释趋势含义，避免伪精确曲线。\n- P7 `architecture_flow_diagram` 应按语义映射呈现双 V 生命周期和七类 AI 介入点，避免散点清单。\n- P8 `layered_stack_diagram` 应呈现真实系统、语义模型、仿真 AI、治理闭环的层间关系，避免静态堆栈。\n- P14 `decision_table` 应突出拍板事项，避免全页 Excel 大表。\n'
(out/'page_copy.md').write_text(page_copy, encoding='utf-8')
(out/'page_design.md').write_text(page_design, encoding='utf-8')

# Dependencies
for src, name in [
    ('skills/huawei_ppt_master/templates/visual_rules.md','visual_rules.md'),
    ('skills/huawei_ppt_master/templates/chart_patterns.md','chart_patterns.md'),
    ('skills/huawei_ppt_master/templates/wording_rules.md','wording_rules.md'),
    ('skills/huawei_ppt_master/visual_patterns/layout_library.md','layout_library.md'),
    ('skills/huawei_ppt_master/core/deck_spec_field_dictionary.md','deck_spec_field_dictionary.md'),
]:
    shutil.copy2(root/src, dep/name)

readme = '''# P4 / P7 / P8 / P14 四页交付物

## 范围

本交付包仅包含 AI+MBSE 自动化生产系统论文解读材料中的 P4、P7、P8、P14 四页。

## 文件清单

- `deck_spec.json`
- `page_copy.md`
- `page_design.md`
- `dependencies/visual_rules.md`
- `dependencies/chart_patterns.md`
- `dependencies/wording_rules.md`
- `dependencies/layout_library.md`
- `dependencies/deck_spec_field_dictionary.md`
- `self_check.md`

## v0.3.9 说明

本包按 `huawei_ppt_master v0.3.9-chart-semantic-mapping` 生成。`deck_spec.json` 已为四页补充 `chart_semantic_mapping`：P4 为 `trend_curve` 必填；P7/P8 为高语义风险图表建议字段；P14 为决策页语义证明补充。
'''
(out/'README.md').write_text(readme, encoding='utf-8')

# validation
valid_chart_types = {'none','key_findings_cards','quadrant_matrix','comparison_table','capability_radar','capability_map','layered_stack_diagram','architecture_flow_diagram','roadmap_timeline_chart','trend_curve','ecosystem_relationship_map','gap_heatmap','risk_matrix','decision_table','value_chain_loop','swimlane_process','priority_matrix','metric_showcase_grid','case_gallery_cards','hub_spoke_relationship_map'}
valid_layouts = {'executive_summary_dashboard','two_column_comparison','four_quadrant_judgement','three_column_cards','layered_architecture','stack_architecture_with_right_insights','roadmap_timeline','trend_curve_with_strategy','ecosystem_map','insight_panel_with_chart','risk_decision_matrix','multi_module_solution_overview','left_logic_right_proof','hub_spoke_ecosystem_canvas','metric_case_showcase_grid','image_background_section_divider'}
errors=[]
for s in out_deck['slides']:
    if s['chart_type'] not in valid_chart_types: errors.append(f"P{s['slide_no']} bad chart_type")
    if s['layout_pattern'] not in valid_layouts: errors.append(f"P{s['slide_no']} bad layout")
    for k in ['core_judgement','chart_proof_goal','chart_visual_boundary','chart_semantic_mapping']:
        if k not in s or not s[k]: errors.append(f"P{s['slide_no']} missing {k}")
    m=s.get('chart_semantic_mapping',{})
    for k in ['chart_reading_intent','main_visual_logic','axis_semantics','stage_or_node_meaning','insight_panel_logic','forbidden_visualization']:
        if k not in m: errors.append(f"P{s['slide_no']} semantic missing {k}")
if errors:
    raise SystemExit('\n'.join(errors))
json.loads((out/'deck_spec.json').read_text(encoding='utf-8'))
self_check = '# 自检结果\n\n- JSON 解析：通过\n- 页面范围：P4 / P7 / P8 / P14\n- deck_spec v0.3.9 字段：四页均包含 `chart_semantic_mapping`\n- `chart_type` 枚举：通过\n- `layout_pattern` 枚举：通过\n- 依赖文件：5 个依赖均已复制\n- 边界：未生成 PPTX；未使用 page_render_spec / normalized_render_model；未新增渲染 DSL\n'
(out/'self_check.md').write_text(self_check, encoding='utf-8')

# zip
zip_path=root/'deliverables/AI4MBSE_P4_P7_P8_P14_四页交付包.zip'
zip_path.parent.mkdir(exist_ok=True)
if zip_path.exists(): zip_path.unlink()
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as z:
    for p in out.rglob('*'):
        if p.is_file():
            z.write(p, p.relative_to(out.parent))

print('done=true')
print('artifact_dir=project/work/AI4MBSE_P4_P7_P8_P14_delivery')
print('zip=deliverables/AI4MBSE_P4_P7_P8_P14_四页交付包.zip')
print('slides=', [s['slide_no'] for s in out_deck['slides']])
