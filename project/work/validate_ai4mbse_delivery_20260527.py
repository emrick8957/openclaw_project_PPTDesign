import json, zipfile, pathlib
root = pathlib.Path.cwd()
deck = json.loads((root/'project/work/deck_spec_v0.1.json').read_text(encoding='utf-8'))
chart_allowed = {'none','key_findings_cards','quadrant_matrix','comparison_table','capability_radar','capability_map','layered_stack_diagram','architecture_flow_diagram','roadmap_timeline_chart','trend_curve','ecosystem_relationship_map','gap_heatmap','risk_matrix','decision_table','value_chain_loop','swimlane_process','priority_matrix','metric_showcase_grid','case_gallery_cards','hub_spoke_relationship_map'}
layout_allowed = {'executive_summary_dashboard','two_column_comparison','four_quadrant_judgement','three_column_cards','layered_architecture','stack_architecture_with_right_insights','roadmap_timeline','trend_curve_with_strategy','ecosystem_map','insight_panel_with_chart','risk_decision_matrix','multi_module_solution_overview','left_logic_right_proof','hub_spoke_ecosystem_canvas','metric_case_showcase_grid','image_background_section_divider'}
bad=[]
for s in deck['slides']:
    if s['chart_type'] not in chart_allowed:
        bad.append(('chart', s['slide_no'], s['chart_type']))
    if s['layout_pattern'] not in layout_allowed:
        bad.append(('layout', s['slide_no'], s['layout_pattern']))
    for k in ['core_judgement','chart_proof_goal','chart_visual_boundary']:
        if k not in s or not s[k]:
            bad.append((k, s['slide_no']))
    if s['chart_type'] == s['layout_pattern']:
        bad.append(('same', s['slide_no']))
print('slides', len(deck['slides']), 'bad', bad)
for name in ['AI4MBSE_自动化生产系统_论文解读交付包_part1_P1-P7.zip','AI4MBSE_自动化生产系统_论文解读交付包_part2_P8-P14.zip']:
    z=zipfile.ZipFile(root/'deliverables'/name)
    names=z.namelist()
    print(name, 'files', len(names), 'templates', any('templates/' in n for n in names), 'visual_patterns', any('visual_patterns/' in n for n in names), 'has_deck', 'project/work/deck_spec_v0.1.json' in names)
text='\n'.join([(root/'project/work/outline_v0.1.md').read_text(encoding='utf-8'), (root/'project/work/page_copy_v0.1.md').read_text(encoding='utf-8'), (root/'project/work/page_design_v0.1.md').read_text(encoding='utf-8')])
for forbidden in ['英伟达','NVIDIA','CUDA','CANN','昇腾','GPU','NPU']:
    if forbidden in text:
        print('forbidden_found', forbidden)
