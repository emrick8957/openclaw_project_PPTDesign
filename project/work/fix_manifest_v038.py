from pathlib import Path
p=Path('skills/huawei_ppt_master/PACKAGE_MANIFEST.md')
text=p.read_text(encoding='utf-8')
# ensure top manifest includes field dictionary after audience
if '- `core/deck_spec_field_dictionary.md`' not in text.split('---',1)[0]:
    text=text.replace('- `core/audience_rules.md`\n', '- `core/audience_rules.md`\n- `core/deck_spec_field_dictionary.md`\n', 1)
# clean duplicate/literal bad section
bad='''- `core/deck_spec_field_dictionary.md`  
  定义 `deck_spec.json` 的文件定位、顶层字段和 slide 字段职责，作为角色 C 理解 deck_spec 的正式交付物支持文档。`r`n`r`n- `core/deck_spec_field_dictionary.md`  `r`n  定义 `deck_spec.json` 的文件定位、顶层字段和 slide 字段职责，作为角色 C 理解 deck_spec 的正式交付物支持文档。
'''
good='''- `core/deck_spec_field_dictionary.md`  
  定义 `deck_spec.json` 的文件定位、顶层字段和 slide 字段职责，作为角色 C 理解 deck_spec 的正式交付物支持文档。
'''
text=text.replace(bad, good)
# If duplicate still exists due literal characters, normalize any adjacent duplicate manually
text=text.replace('`r`n`r`n- `core/deck_spec_field_dictionary.md`  `r`n  定义 `deck_spec.json` 的文件定位、顶层字段和 slide 字段职责，作为角色 C 理解 deck_spec 的正式交付物支持文档。','')
p.write_text(text, encoding='utf-8')
