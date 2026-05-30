# VERSION

Current Version: v0.4.2-relation-roles

Version positioning:

- v0.1: Huawei-style PPT content generation skill with strong AI-compute/Ascend-NVIDIA sample orientation.
- v0.2: General Huawei-style PPT generation core + conditional domain profiles + layout screenshot-derived visual pattern library.
- v0.3: Reference-material learning framework. Supports learning style, structure, expression habits, content套路, executive argument patterns, and industry/framework logic from continuously provided PPTs, PPT screenshots/images, templates, text materials, and data materials, with layered sedimentation and regression gates.
- v0.3.2: Consistency fix for deck_spec trigger conditions, generation workflow precedence wording, and default-general structure interpretation.
- v0.3.3: Visual consistency upgrade based on SWE Atlas page image review and Huawei template comparison. Adds red-anchor budget, layout region ratios, component-level chart visual rules, visual scorecard extensions, page-design visual-noise fields, and regression cases for page image quality.
- v0.3.4: Visual semantics upgrade based on AI_MBSE page image review. Adds red-anchor attention-point checks, engineering card hierarchy, bottom-conclusion increment, valid quadrant coordinates, chart semantic gates, strong-title support, and abstract-concept definition rules.
- v0.3.5: Generated image feedback sedimentation. Adds body-page red-base control, multi-card hierarchy gates, reading-framework/case/decision/roadmap semantic constraints, chart failure conditions, long-title compression, final-definition summary rules, and visual scorecard downgrade items.
- v0.3.6: Visual rules refactor. Rebuilds `templates/visual_rules.md` as a dedicated visual design guidance asset based on visual_rules_v0.2, preserves historical sedimentation, adds negative visual style boundaries, visual optimization priority, default page styles, and synchronizes `visual_boundary` / `page_type_gate` fields.
- v0.3.7: Deck spec proof contract. Adds `core_judgement`, `chart_proof_goal`, and `chart_visual_boundary` to each deck_spec slide, so chart_type must prove the page judgement and obey visual proof boundaries.
- v0.3.8: Deck spec field dictionary formalization. Adds `core/deck_spec_field_dictionary.md` as a formal delivery-support asset with three sections: file positioning, top-level fields, and slide fields. This version terminates the page_render_spec / normalized_render_model exploration and does not add a rendering DSL.
- v0.3.9: Chart semantic mapping. Adds `chart_semantic_mapping` to deck_spec as a semantic proof explanation field, mandatory for `trend_curve` and recommended for high-semantic-risk charts. This is not a rendering DSL.
- v0.4.0: Anti-template-stamp gate. Adds `core/field_differentiation_rules.md` and `eval/template_stamp_detection.md` to detect mechanical field repetition, literal restatement, skeleton filling, and missing per-page design decisions. Uses a mixed threshold model and preserves Huawei-style consistency without reviving page_render_spec / normalized_render_model.
- v0.4.1: Chart data visibility. Clarifies `chart_data` field visibility rules, keeps `group` / `emphasis` / `source_status` logic-only, constrains `edges.label` to short visible action text, routes complex relationship semantics to `chart_semantic_mapping`, and prohibits relation/rendering DSL fields in `chart_data`.
- v0.4.2: Relation roles. Adds optional `correspondence_pairs` (single source of truth for same-level correspondence) and `edge_roles` (directional edge grouping with structured `{from,to}` references) inside `chart_semantic_mapping`, so high-semantic-risk relational charts (V-model and similar) can make correspondence machine-consumable for role C without reviving a rendering DSL or adding relation fields to `chart_data`.

Release date: 2026-05-30
