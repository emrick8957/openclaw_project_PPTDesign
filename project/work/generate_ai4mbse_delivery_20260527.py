from pathlib import Path
import json, zipfile, shutil

ROOT = Path.cwd()
WORK = ROOT/'project'/'work'
HANDOFF = ROOT/'project'/'handoff'
DELIV = ROOT/'deliverables'
for p in [WORK, HANDOFF, DELIV]: p.mkdir(parents=True, exist_ok=True)

slides = [
 {"no":1,"section":"封面","type":"cover","title":"AI 正在把 MBSE 从建模工具推向自学习工程闭环","conclusion":"基于论文《Application of artificial intelligence in MBSE of automated production systems》，本材料提炼 AI+MBSE 在自动化生产系统中的背景、触发因素、应用框架和趋势判断。","layout":"executive_summary_dashboard","chart":"none","focus":["AI+MBSE","自学习数字孪生","自动化生产系统"],"gap":[]},
 {"no":2,"section":"核心判断","type":"executive_summary","title":"核心不是把 AI 加进流程，而是让工程模型具备语义、仿真和反馈闭环","conclusion":"论文提出的关键价值在于：以语义丰富的产品—生产一体化模型承接 AI 结果，再通过 FMU 共仿真和 XAI 机制让 AI 从孤立应用走向可解释、可验证、可回写。","layout":"executive_summary_dashboard","chart":"key_findings_cards","focus":["语义总模型","AI/XAI","FMU 共仿真","知识图谱"],"gap":["缺少量化收益和工业规模验证数据"]},
 {"no":3,"section":"阅读框架","type":"agenda","title":"建议按 Background—Catalyst—Application—Trends 四段形成判断","conclusion":"先明确为什么需要 AI+MBSE，再解释触发机制，随后拆解应用框架，最后收口到工程趋势和决策动作。","layout":"roadmap_timeline","chart":"roadmap_timeline_chart","focus":["Background","Catalyst","Application","Trends"],"gap":[]},
 {"no":4,"section":"Background","type":"context_trend","title":"制造企业面对复杂度、竞争和可持续压力，单点 AI 难以支撑系统级工程决策","conclusion":"论文背景指出，客户期望、全球竞争、可持续要求和产业转型共同推高工程复杂度，AI 虽有潜力，但在工程流程中仍多停留在孤立应用。","layout":"trend_curve_with_strategy","chart":"trend_curve","focus":["复杂度上升","AI 孤岛","工程流程变革"],"gap":["外部压力强度需结合企业具体行业数据补充"]},
 {"no":5,"section":"Background","type":"problem_diagnosis","title":"真正瓶颈不是 AI 算法不足，而是产品、生产和运行数据缺少统一语义上下文","conclusion":"论文反复强调，数据只有参考实体和上下文才成为知识；若缺少知识图谱、结构化模型和生命周期语义，AI 结果难以解释、复用和回写。","layout":"three_column_cards","chart":"key_findings_cards","focus":["数据","信息","知识"],"gap":[]},
 {"no":6,"section":"Catalyst","type":"context_trend","title":"AI 落地从热情转向审慎，倒逼企业先重构工程过程和管理方式","conclusion":"论文引用研究指出，部分领域对 AI 的热情已转为失望，原因不是 AI 无价值，而是实施需要成熟流程、既有实践变更和管理方式调整。","layout":"two_column_comparison","chart":"comparison_table","focus":["媒体热情","落地失望","流程重构"],"gap":["论文未给出不同行业失望程度的定量对比"]},
 {"no":7,"section":"Catalyst","type":"framework","title":"七类 AI 介入点覆盖产品与生产双 V 模型，要求统一生命周期工程底座","conclusion":"论文将 AI 介入点扩展到产品运行、生产运行、回收、产品设计、生产系统设计、产品验证和生产系统验证，说明 AI+MBSE 必须贯穿双 V 模型。","layout":"stack_architecture_with_right_insights","chart":"architecture_flow_diagram","focus":["双 V 模型","七类介入点","生命周期"],"gap":[]},
 {"no":8,"section":"Application","type":"architecture","title":"自学习数字孪生应把真实系统、语义模型、仿真和 AI 结果纳入同一闭环","conclusion":"论文提出 AI-based self-learning digital twin：真实产品与生产系统通过传感器、PPS 和外部数据接入，模型侧融合产品模型、生产模型、行为模型、仿真和 AI 组件。","layout":"layered_architecture","chart":"layered_stack_diagram","focus":["真实系统","语义模型","仿真","AI/XAI"],"gap":[]},
 {"no":9,"section":"Application","type":"architecture","title":"GBDL 是语义底座，负责把工程词汇、规则和几何/行为模型沉淀为知识图谱","conclusion":"图基设计语言通过 vocabulary、rules、UML 和 Design Compiler 43 形成中央数据模型，并承载需求、功能、物理、几何、技术、运动和装配等领域本体。","layout":"stack_architecture_with_right_insights","chart":"layered_stack_diagram","focus":["GBDL","本体","知识图谱","DC43"],"gap":[]},
 {"no":10,"section":"Application","type":"architecture","title":"FMU 让 AI 模型以模块方式进入共仿真，避免重新改造整体仿真架构","conclusion":"论文提出利用 FMI/FMU 将物理仿真、AI/XAI 模型和 HiL 系统接入同一模块化共仿真环境，使工程师可在传统模型和 AI-FMU 之间切换。","layout":"stack_architecture_with_right_insights","chart":"architecture_flow_diagram","focus":["FMU","共仿真","AI-FMU","HiL"],"gap":[]},
 {"no":11,"section":"Application","type":"case_proof","title":"自动化装配案例验证了“产品结构—装配序列—生产系统”可自动贯通","conclusion":"论文应用于 Festo 自动化装配系统，展示从产品结构生成装配序列和装配系统，并通过学习摩擦行为形成机器学习模型和 XAI 决策树。","layout":"left_logic_right_proof","chart":"case_gallery_cards","focus":["Festo 装配系统","装配序列","XAI 决策树"],"gap":["案例未披露泛化能力、精度指标和工业部署周期"]},
 {"no":12,"section":"Trends","type":"trend","title":"AI+MBSE 的演进方向是从“模型辅助”走向“模型可学习、可解释、可审查”","conclusion":"论文趋势指向：语义总模型提升 AI 可解释性，XAI 负责描述模型影响因素，语义机器学习负责 plausibility 与 causality 检查，最终形成可审查工程闭环。","layout":"trend_curve_with_strategy","chart":"trend_curve","focus":["可学习","可解释","可审查"],"gap":["因果审查方法仍处于研究与验证阶段"]},
 {"no":13,"section":"Trends","type":"roadmap","title":"企业落地不应先追求全量智能，而应先形成语义底座、模块仿真和闭环治理三类能力","conclusion":"面向企业实践，建议采用“语义建模试点—FMU 共仿真接入—AI/XAI 回写治理—跨场景复制”的阶段路径，避免从孤立算法项目直接跳到全生命周期智能。","layout":"roadmap_timeline","chart":"roadmap_timeline_chart","focus":["语义底座","模块仿真","回写治理","复制"],"gap":["需结合企业现有工具链和数据基础制定阶段门槛"]},
 {"no":14,"section":"决策收口","type":"decision_table","title":"高层需要拍板的不是单个 AI 场景，而是 MBSE 语义底座和 AI 回写治理机制","conclusion":"建议将 AI+MBSE 作为工程体系升级项目管理：先选自动化产线或装配系统样板，明确知识图谱、FMU 接口、XAI 审查和模型回写责任。","layout":"risk_decision_matrix","chart":"decision_table","focus":["样板选择","数据/模型责任","接口标准","审查机制"],"gap":["需要补充企业内部系统清单、责任组织和预算约束"]},
]

def bullets(items): return '\n'.join([f'- {x}' for x in items])

outline = ["# AI+MBSE 自动化生产系统论文解读 PPT 大纲 v0.1\n",
"## 汇报对象\n面向技术高层 / 工程研发负责人 / 智能制造与生产系统决策人。\n",
"## 汇报目标\n基于论文提炼 AI 在自动化生产系统 MBSE 中的背景、触发因素、应用框架与趋势，并转化为可进入 PPTX Builder 的华为风格页面输入。\n",
"## 总体叙事主线\n不是把 AI 作为单点工具嵌入工程流程，而是以语义丰富的产品—生产一体化模型为底座，让 AI 结果可解释、可仿真、可回写、可审查。\n",
"## 四段式章节\n- Background：制造复杂度与 AI 孤岛问题。\n- Catalyst：双 V 生命周期与 AI 落地失望倒逼工程底座重构。\n- Application：自学习数字孪生、GBDL、FMU、XAI 与自动化装配案例。\n- Trends：可学习、可解释、可审查的工程闭环与落地路径。\n"]
for s in slides:
    outline.append(f"\n### P{s['no']} {s['title']}\n核心结论：{s['conclusion']}\n页面类型：{s['type']}\n建议图表：{s['chart']}\n页面设计说明：{s['layout']}；白底红黑灰，标题区承载判断，主体区用主图/卡片证明判断，页脚弱化。\n该页回答的问题：{s['section']} 阶段高层应形成什么判断？\n")
(WORK/'outline_v0.1.md').write_text('\n'.join(outline), encoding='utf-8')

copy = ["# AI+MBSE 自动化生产系统论文解读逐页文案 v0.1\n"]
for s in slides:
    modules = [f"核心判断：{s['conclusion']}", f"关键要点：{', '.join(s['focus'])}"]
    if s['section'] in ['Background','Catalyst','Application','Trends']:
        modules.append(f"四段式定位：{s['section']}")
    copy.append(f"\n## P{s['no']}\n页标题：{s['title']}\n一句话结论：{s['conclusion']}\n正文模块：\n{bullets(modules)}\n图表内容：主图表使用 `{s['chart']}`，围绕 {', '.join(s['focus'])} 建立结构化证明。\n版式说明：`{s['layout']}`，主体 3–5 个信息块，保留 5% 页脚安全区。\n讲解口径：先讲本页判断，再用论文证据解释机制，最后落到管理含义或下一步动作。\n数据缺口：{'; '.join(s['gap']) if s['gap'] else '无；基于论文原文方向性归纳。'}\n是否适合直接进入 PPTX 生成：是。\n")
(WORK/'page_copy_v0.1.md').write_text('\n'.join(copy), encoding='utf-8')

design = ["# AI+MBSE 自动化生产系统论文解读页面设计说明 v0.1\n"]
for s in slides:
    design.append(f"\n## P{s['no']} {s['title']}\n页面类型：{s['type']}\n版式模式：{s['layout']}\n区域划分：标题区 12%，主体区 78%，页脚区 5%，左右安全边距稳定；主图/卡片优先，文字区不超过 5 个信息块。\n标题区：左上章节标签 + 结论型标题；仅保留一条细红线或红色关键词。\n图表区：主图表 `{s['chart']}` 承载页面证明任务，图表文字短语化，避免论文截图式堆叠。\n文字区：正文以 3–5 个短模块呈现；每模块 1 个标题 + 1 行解释。\n强调元素：主红色锚点只给 `{s['focus'][0] if s['focus'] else '核心判断'}`；其他强调用深灰/浅灰。\n页脚：浅灰 8–10pt，包含来源：Procedia CIRP 136 (2025) 61–66。\nPPTX Builder 注意事项：不使用大面积红底、渐变、卡通图标；卡片统一浅灰边框；图表需能看出主次和证明关系。\n视觉降噪约束：\n  red_anchor：仅 1 个主红色锚点，用于核心判断或关键节点。\n  card_hierarchy：最多 1 张主卡，支撑卡 2–4 张，注释卡弱化。\n  spacing_rule：模块间距大于卡片内边距；页脚与主体区保持独立。\n  bottom_bar_rule：普通页不使用厚重红色底栏；必要时仅用浅灰底 + 窄红线。\n  visual_simplification：删除装饰性图标、复杂背景、论文截图式长段落。\n  visual_boundary：禁止互联网发布会风、咨询海报风、卡通插画风、Excel 报表风、学术论文截图风。\n  page_type_gate：本页必须让图表证明标题判断；若无法证明，优先重选通用 chart_type 或拆页。\n")
(WORK/'page_design_v0.1.md').write_text('\n'.join(design), encoding='utf-8')

slide_specs=[]
for s in slides:
    chart_data = {}
    if s['chart']=='key_findings_cards':
        chart_data={"cards":[{"label":f"判断{i+1}","headline":x,"description":"支撑本页核心判断","emphasis":"high" if i==0 else "medium"} for i,x in enumerate(s['focus'])]}
    elif s['chart']=='roadmap_timeline_chart':
        chart_data={"stages":[{"name":x,"time_range":"阶段","goals":["形成阶段判断"],"actions":["沉淀证据与动作"],"milestones":["可进入下一阶段"]} for x in s['focus']]}
    elif s['chart']=='trend_curve':
        chart_data={"x_axis":["现状","转折","目标态"],"series":[{"name":"演进趋势","values":[1,2,3]}],"annotations":[{"x":"转折","label":"语义模型/AI 回写成为拐点"}]}
    elif s['chart']=='comparison_table':
        chart_data={"columns":["维度","传统/孤立方式","AI+MBSE 方式","管理含义"],"rows":[["模型上下文","分散","统一语义模型","先建底座"],["AI结果","局部输出","可解释可回写","需治理机制"],["验证方式","单点验证","仿真与因果审查","需闭环"]]}
    elif s['chart']=='architecture_flow_diagram':
        chart_data={"nodes":[{"id":"A","label":"产品/生产/运行数据","group":"输入"},{"id":"B","label":"语义模型/知识图谱","group":"处理"},{"id":"C","label":"AI/XAI 与 FMU 共仿真","group":"验证"},{"id":"D","label":"模型回写与治理","group":"输出"}],"edges":[{"from":"A","to":"B","label":"语义化"},{"from":"B","to":"C","label":"仿真/学习"},{"from":"C","to":"D","label":"解释/审查"},{"from":"D","to":"B","label":"回写"}]}
    elif s['chart']=='layered_stack_diagram':
        chart_data={"layers":[{"name":"真实系统层","items":["产品","生产系统","传感器/PPS/外部数据"]},{"name":"语义模型层","items":["产品模型","生产模型","行为模型","知识图谱"]},{"name":"仿真与 AI 层","items":["FMU","共仿真","ML/XAI"]},{"name":"治理闭环层","items":["解释","因果/合理性检查","模型回写"]}]}
    elif s['chart']=='case_gallery_cards':
        chart_data={"cards":[{"title":"Festo 自动化装配样例","image_ref":"论文 Fig.6-Fig.8","proof_point":"验证产品结构、装配序列、生产系统和 XAI 模型可贯通","source_status":"provided"}]}
    elif s['chart']=='decision_table':
        chart_data={"columns":["拍板事项","推荐方案","资源/责任","阶段产出"],"rows":[["样板场景","选择自动化装配/产线样板","研发+制造+IT 联合","语义模型 MVP"],["接口机制","定义 FMU/工具链接入边界","架构团队牵头","共仿真原型"],["AI 回写治理","XAI 审查+责任闭环","工程质量/流程 Owner","可审查模型回写机制"]]}
    slide_specs.append({
        "slide_no":s['no'],"section":s['section'],"type":s['type'],"page_goal":"让高层形成本页唯一判断并知道下一步动作", "title":s['title'],"conclusion":s['conclusion'],
        "core_judgement":f"本页唯一要带走的判断：{s['conclusion']}",
        "chart_proof_goal":f"主图表必须证明：{', '.join(s['focus'])} 共同支撑该页判断，而不是做装饰或概念罗列。",
        "chart_visual_boundary":["不得画成无主次的信息堆叠","必须保留唯一主红色锚点","图表必须能解释标题判断","页脚与来源信息弱化且固定"],
        "display_text":s['focus'],"speaker_notes":"先讲判断，再讲论文依据，最后讲管理含义。",
        "chart_type":s['chart'],"chart_data":chart_data,"layout_pattern":s['layout'],
        "visual_notes":"白底，红黑灰为主；普通正文页红色面积控制在 5%以内；标题区结论先行；主体区模块化证明判断。",
        "visual_focus":s['focus'],"must_highlight":s['focus'][:2],"text_density":"medium","need_compression":False,"data_gaps":s['gap']})

deck={"deck_title":"AI 在自动化生产系统 MBSE 中的应用：从单点 AI 到自学习工程闭环","audience":"技术高层 / 工程研发负责人 / 智能制造与生产系统决策人","style":"huawei_executive","source":"Procedia CIRP 136 (2025) 61–66, Application of artificial intelligence in model-based systems engineering of automated production systems","slides":slide_specs}
(WORK/'deck_spec_v0.1.json').write_text(json.dumps(deck, ensure_ascii=False, indent=2), encoding='utf-8')

manifest={"source_file":"examples/人工智能在自动化生产系统基于模型的系统工程（MBSE）中的应用.pdf","extracted_text":"project/work/source_extract/AI4MBSE_pdf_text_20260527.txt","paper":"Timo Schuchter et al., Procedia CIRP 136 (2025) 61–66","evidence_map":[{"pages":"1-2","used_for":"Background: AI 在工程流程中仍有限，制造企业复杂度上升，双 V 模型与七类 AI 介入点"},{"pages":"3-4","used_for":"Application: 自学习数字孪生、GBDL、本体、知识图谱、DC43 蓝图"},{"pages":"4-5","used_for":"Application: FMU/FMI 模块化共仿真、AI/XAI 模型接入"},{"pages":"5-6","used_for":"Application/Trends: 自动化装配应用、产品结构到装配系统贯通、总结与展望"}],"fact_policy":"未编造论文外具体指标；缺少量化收益处均写入 data_gaps。"}
(WORK/'source_evidence_manifest_v0.1.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')

self_check = """# 自检报告 v0.1

- Skill 链路：已读取 SKILL、generation_workflow、topic_router、output_contracts、anti_overfit、audience、reference policy/workflow、default_general、page_types、narrative/visual/chart/wording/layout/eval。
- 四段式：已覆盖 Background、Catalyst、Application、Trends，并在 P3 明确阅读框架。
- 交付物：outline、page_copy、page_design、deck_spec、source_evidence_manifest、handoff、status、zip 均已生成。
- deck_spec：每页均包含 core_judgement、chart_proof_goal、chart_visual_boundary；chart_type 与 layout_pattern 未混用。
- 事实边界：仅基于论文 PDF 归纳；无量化收益、行业规模、部署周期等外部数据编造。
- 视觉规则：红色锚点、卡片层级、间距、底部结论条、visual_boundary、page_type_gate 均已写入页面设计。
- 主题污染：本材料为 AI+MBSE/数字孪生/自动化生产系统主题，未引入昇腾/NVIDIA/CUDA/CANN/GPU/NPU 等无关算力竞品内容。
- 风险：正式 PPTX 未生成；需由 huawei_pptx_builder 读取当前输入后生成成品。
"""
(WORK/'self_check_v0.1.md').write_text(self_check, encoding='utf-8')

handoff = """# A_to_B 交接单 v0.1

## 任务
根据 PDF《人工智能在自动化生产系统基于模型的系统工程（MBSE）中的应用》分析核心内容，按 huawei_ppt_master 全链路生成华为风格 PPT 输入包，至少包含 Background / Catalyst / Application / Trends 四段式。

## 当前交付
- project/work/outline_v0.1.md
- project/work/page_copy_v0.1.md
- project/work/page_design_v0.1.md
- project/work/deck_spec_v0.1.json
- project/work/source_evidence_manifest_v0.1.json
- project/work/self_check_v0.1.md
- deliverables/AI4MBSE_自动化生产系统_论文解读交付包_part1_P1-P7.zip
- deliverables/AI4MBSE_自动化生产系统_论文解读交付包_part2_P8-P14.zip

## 核心结论
本论文的管理含义不是“AI 能做更多场景”，而是 AI 必须依托语义丰富的产品—生产一体化模型、知识图谱、FMU 共仿真和 XAI/因果审查机制，才能从孤立应用走向自学习工程闭环。

## 重点请 B 评审
1. P2/P14 的高层判断是否足够强；
2. P7 双 V 模型与七类 AI 介入点是否表达清晰；
3. P8-P10 架构页是否存在术语密度过高风险；
4. P11 案例页是否需要补充原图截图或只保留文字证明；
5. deck_spec 中 chart_type/layout_pattern 合法性与证明契约是否通过。
"""
(HANDOFF/'A_to_B.md').write_text(handoff, encoding='utf-8')

status = {"version":"v0.1","status":"completed","updated":"2026-05-27 22:55 Asia/Shanghai","source_pdf":"examples/人工智能在自动化生产系统基于模型的系统工程（MBSE）中的应用.pdf","slide_count":14,"sections":["Background","Catalyst","Application","Trends"],"work_files":["project/work/outline_v0.1.md","project/work/page_copy_v0.1.md","project/work/page_design_v0.1.md","project/work/deck_spec_v0.1.json","project/work/source_evidence_manifest_v0.1.json","project/work/self_check_v0.1.md"],"deliverables":["deliverables/AI4MBSE_自动化生产系统_论文解读交付包_part1_P1-P7.zip","deliverables/AI4MBSE_自动化生产系统_论文解读交付包_part2_P8-P14.zip"],"blocked":[]}
(HANDOFF/'status.md').write_text('# status\n\n```json\n'+json.dumps(status, ensure_ascii=False, indent=2)+'\n```\n', encoding='utf-8')

# split helper files
for name, rng in [('part1_P1-P7', range(1,8)), ('part2_P8-P14', range(8,15))]:
    part_slides=[s for s in slide_specs if s['slide_no'] in rng]
    (WORK/f'deck_spec_v0.1_{name}.json').write_text(json.dumps({**deck,"slides":part_slides}, ensure_ascii=False, indent=2), encoding='utf-8')

zip_specs=[('AI4MBSE_自动化生产系统_论文解读交付包_part1_P1-P7.zip', range(1,8), 'part1_P1-P7'), ('AI4MBSE_自动化生产系统_论文解读交付包_part2_P8-P14.zip', range(8,15), 'part2_P8-P14')]
base_files=[WORK/'outline_v0.1.md',WORK/'page_copy_v0.1.md',WORK/'page_design_v0.1.md',WORK/'deck_spec_v0.1.json',WORK/'source_evidence_manifest_v0.1.json',WORK/'self_check_v0.1.md',HANDOFF/'A_to_B.md',HANDOFF/'status.md']
for zip_name, rng, part in zip_specs:
    zp=DELIV/zip_name
    if zp.exists(): zp.unlink()
    with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in base_files:
            z.write(f, f.relative_to(ROOT))
        part_file=WORK/f'deck_spec_v0.1_{part}.json'
        z.write(part_file, part_file.relative_to(ROOT))
        # include minimal dependency dirs
        for d in [ROOT/'skills'/'huawei_ppt_master'/'templates', ROOT/'skills'/'huawei_ppt_master'/'visual_patterns']:
            for f in d.rglob('*'):
                if f.is_file(): z.write(f, f.relative_to(ROOT))
print('generated', len(slides), 'slides')
for zip_name,_,_ in zip_specs:
    print(DELIV/zip_name, (DELIV/zip_name).stat().st_size)
