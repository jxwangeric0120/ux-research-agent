import json

import pandas as pd
import streamlit as st

from utils.doc_generator import generate_docx_report
from utils.output_utils import save_docx_report
from utils.json_utils import html_escape


PRIMARY_COLOR = "#2E60FD"


def get_render_labels(ui_language="English"):
    if ui_language == "中文":
        return {
            "Overview": "项目概览",
            "Insights": "UX 洞察",
            "Affinity Map": "亲和图",
            "Persona": "用户画像",
            "Journey Map": "用户旅程图",
            "Service Blueprint": "服务蓝图",
            "Theory Support": "理论支持",
            "Design Directions": "设计方向",
            "Download": "下载",
            "project_overview": "项目概览",
            "research_context": "研究背景",
            "main_user_group": "主要用户群体",
            "core_problem": "核心问题",
            "research_limitations": "研究限制",
            "ux_insights": "UX 洞察",
            "pain_points": "痛点",
            "behavioral_patterns": "行为模式",
            "emotional_needs": "情绪需求",
            "what_happens": "发生了什么",
            "why_it_matters": "为什么重要",
            "design_implication": "设计启示",
            "observed_behavior": "观察到的行为",
            "interpretation": "研究解读",
            "emotional_signal": "情绪信号",
            "underlying_need": "底层需求",
            "evidence": "证据",
            "affinity_caption": "基于主题的研究综合墙，用于归纳用户证据、重复洞察与设计机会。",
            "insight_notes": "洞察便签",
            "supporting_evidence": "支持证据",
            "design_opportunity": "设计机会",
            "theme_summary": "主题总结",
            "user_persona": "用户画像",
            "primary_goal": "核心目标",
            "quote": "用户引语",
            "persona_details": "画像详情",
            "goals": "目标",
            "frustrations": "挫败点",
            "needs": "需求",
            "behaviors": "行为",
            "trust_barriers": "信任障碍",
            "journey_caption": "基于阶段的用户旅程视图，展示目标、行为、情绪、痛点与机会。",
            "user_goal": "用户目标",
            "actions": "行为",
            "thoughts": "想法",
            "emotions": "情绪",
            "opportunities": "机会",
            "feature_response": "可能的功能回应",
            "blueprint_caption": "分层服务视图，展示用户行为如何与前台触点、后台流程和支持系统连接。",
            "layer": "层级",
            "user_actions": "用户行为",
            "frontstage_touchpoints": "前台触点",
            "backstage_processes": "后台流程",
            "support_systems": "支持系统",
            "design_requirement": "设计需求",
            "problem_statement": "问题陈述",
            "design_principles": "设计原则",
            "opportunity_areas": "机会区域",
            "recommended_features": "推荐功能",
            "user_problem_addressed": "对应的用户问题",
            "priority": "优先级",
            "final_direction_summary": "最终设计方向总结",
            "next_research_questions": "下一步研究问题",
            "download_report": "下载报告",
            "download_word": "下载 Word 报告",
            "download_json": "下载 JSON 数据",
            "raw_json": "查看原始 JSON 数据用于调试",
            "report_saved": "报告已保存到：",
            "no_data": "暂无生成内容。",
            "no_research_context": "暂无研究背景。",
            "no_user_group": "暂无主要用户群体。",
            "no_core_problem": "暂无核心问题。",
            "no_limitations": "暂无研究限制。",
            "overview_caption": "研究范围、目标用户、核心问题与限制的快速摘要。",
            "download_caption": "导出可交付文档或结构化数据，便于复盘、汇报和继续加工。",
        }

    return {
        "Overview": "Overview",
        "Insights": "Insights",
        "Affinity Map": "Affinity Map",
        "Persona": "Persona",
        "Journey Map": "Journey Map",
        "Service Blueprint": "Service Blueprint",
        "Theory Support": "Theory Support",
        "Design Directions": "Design Directions",
        "Download": "Download",
        "project_overview": "Project Overview",
        "research_context": "Research Context",
        "main_user_group": "Main User Group",
        "core_problem": "Core Problem",
        "research_limitations": "Research Limitations",
        "ux_insights": "UX Insights",
        "pain_points": "Pain Points",
        "behavioral_patterns": "Behavioral Patterns",
        "emotional_needs": "Emotional Needs",
        "what_happens": "What happens",
        "why_it_matters": "Why it matters",
        "design_implication": "Design implication",
        "observed_behavior": "Observed behavior",
        "interpretation": "Interpretation",
        "emotional_signal": "Emotional signal",
        "underlying_need": "Underlying need",
        "evidence": "Evidence",
        "affinity_caption": "A theme-based synthesis wall that groups user evidence, recurring insights, and design opportunities.",
        "insight_notes": "Insight Notes",
        "supporting_evidence": "Supporting Evidence",
        "design_opportunity": "Design Opportunity",
        "theme_summary": "Theme Summary",
        "user_persona": "User Persona",
        "primary_goal": "Primary Goal",
        "quote": "Quote",
        "persona_details": "Persona Details",
        "goals": "Goals",
        "frustrations": "Frustrations",
        "needs": "Needs",
        "behaviors": "Behaviors",
        "trust_barriers": "Trust Barriers",
        "journey_caption": "A stage-based view of the user's goals, actions, emotions, pain points, and design opportunities.",
        "user_goal": "User Goal",
        "actions": "Actions",
        "thoughts": "Thoughts",
        "emotions": "Emotions",
        "opportunities": "Opportunities",
        "feature_response": "Feature Response",
        "blueprint_caption": "A layered service view showing how user actions connect with frontstage, backstage, and support systems.",
        "layer": "Layer",
        "user_actions": "User Actions",
        "frontstage_touchpoints": "Frontstage Touchpoints",
        "backstage_processes": "Backstage Processes",
        "support_systems": "Support Systems",
        "design_requirement": "Design Requirement",
        "problem_statement": "Problem Statement",
        "design_principles": "Design Principles",
        "opportunity_areas": "Opportunity Areas",
        "recommended_features": "Recommended Features",
        "user_problem_addressed": "User problem addressed",
        "priority": "Priority",
        "final_direction_summary": "Final Direction Summary",
        "next_research_questions": "Next Research Questions",
        "download_report": "Download Report",
        "download_word": "Download Word Report",
        "download_json": "Download JSON Data",
        "raw_json": "View raw JSON data for debugging",
        "report_saved": "Report saved to:",
        "no_data": "No data generated.",
        "no_research_context": "No research context generated.",
        "no_user_group": "No main user group generated.",
        "no_core_problem": "No core problem generated.",
        "no_limitations": "No research limitations generated.",
        "overview_caption": "A quick summary of research context, target users, core problem, and limitations.",
        "download_caption": "Export client-ready documents or structured data for review, reporting, and further iteration.",
    }


def inject_result_styles():
    st.markdown(
        f"""
        <style>
            .result-shell {{
                margin-top: 26px;
            }}

            .section-header {{
                margin: 24px 0 14px 0;
            }}

            .section-kicker {{
                color: {PRIMARY_COLOR};
                font-size: 12px;
                font-weight: 800;
                letter-spacing: 0;
                text-transform: uppercase;
                margin-bottom: 5px;
            }}

            .section-title {{
                color: #101828;
                font-size: 24px;
                font-weight: 800;
                line-height: 1.2;
                margin: 0;
            }}

            .section-copy {{
                color: #667085;
                font-size: 14px;
                line-height: 1.55;
                margin-top: 6px;
            }}

            .ux-card {{
                background: #FFFFFF;
                border: 1px solid #E4E7EC;
                border-radius: 8px;
                padding: 18px;
                min-height: 100%;
                box-shadow: 0 1px 2px rgba(16, 24, 40, 0.04);
                margin-bottom: 14px;
            }}

            .ux-card-title {{
                color: #101828;
                font-size: 17px;
                font-weight: 780;
                line-height: 1.35;
                margin-bottom: 10px;
            }}

            .ux-card-label {{
                color: #475467;
                font-size: 12px;
                font-weight: 800;
                text-transform: uppercase;
                margin: 14px 0 5px 0;
            }}

            .ux-card-body {{
                color: #344054;
                font-size: 14px;
                line-height: 1.58;
            }}

            .accent-card {{
                border-left: 4px solid {PRIMARY_COLOR};
                background: #FFFFFF;
            }}

            .soft-callout {{
                border: 1px solid #D8E2FF;
                border-radius: 8px;
                background: #EAF0FF;
                color: #1D2939;
                padding: 14px;
                margin-top: 12px;
                line-height: 1.56;
            }}

            .evidence-box {{
                border-left: 3px solid #98A2B3;
                background: #F8FAFC;
                padding: 12px;
                border-radius: 8px;
                color: #475467;
                font-size: 13px;
                line-height: 1.5;
                margin-top: 12px;
            }}

            .note-card {{
                background: #FFFAEB;
                border: 1px solid #FEDF89;
                border-radius: 8px;
                padding: 14px;
                min-height: 126px;
                color: #3F2E00;
                font-size: 14px;
                line-height: 1.52;
                margin-bottom: 12px;
            }}

            .persona-header {{
                background: #FFFFFF;
                border: 1px solid #E4E7EC;
                border-radius: 8px;
                padding: 22px;
                box-shadow: 0 1px 2px rgba(16, 24, 40, 0.04);
                margin-bottom: 16px;
            }}

            .persona-row {{
                display: flex;
                align-items: flex-start;
                gap: 16px;
            }}

            .avatar {{
                width: 64px;
                height: 64px;
                border-radius: 8px;
                background: {PRIMARY_COLOR};
                color: #FFFFFF;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 22px;
                font-weight: 800;
                flex: 0 0 auto;
            }}

            .persona-name {{
                color: #101828;
                font-size: 27px;
                font-weight: 850;
                line-height: 1.15;
            }}

            .persona-role {{
                color: {PRIMARY_COLOR};
                font-size: 14px;
                font-weight: 750;
                margin-top: 4px;
            }}

            .quote-box {{
                background: #F8FAFC;
                border: 1px solid #E4E7EC;
                border-radius: 8px;
                padding: 16px;
                color: #344054;
                font-size: 15px;
                line-height: 1.58;
            }}

            .journey-stage {{
                border-top: 4px solid {PRIMARY_COLOR};
            }}

            .badge {{
                display: inline-flex;
                align-items: center;
                border-radius: 999px;
                padding: 5px 9px;
                background: #EAF0FF;
                color: {PRIMARY_COLOR};
                font-size: 12px;
                font-weight: 800;
                margin-bottom: 10px;
            }}

            .download-panel {{
                background: #FFFFFF;
                border: 1px solid #E4E7EC;
                border-radius: 8px;
                padding: 22px;
                box-shadow: 0 1px 2px rgba(16, 24, 40, 0.04);
            }}

            .dataframe {{
                border-radius: 8px;
            }}

            @media (max-width: 768px) {{
                .persona-row {{
                    display: block;
                }}

                .avatar {{
                    margin-bottom: 12px;
                }}
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def section_header(title, caption=None, kicker=None):
    kicker_html = f'<div class="section-kicker">{html_escape(kicker)}</div>' if kicker else ""
    caption_html = f'<div class="section-copy">{html_escape(caption)}</div>' if caption else ""
    st.markdown(
        f"""
        <div class="section-header">
            {kicker_html}
            <h2 class="section-title">{html_escape(title)}</h2>
            {caption_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_info_card(title, body, label=None, accent=False):
    accent_class = " accent-card" if accent else ""
    label_html = f'<div class="badge">{html_escape(label)}</div>' if label else ""
    st.markdown(
        f"""
        <div class="ux-card{accent_class}">
            {label_html}
            <div class="ux-card-title">{html_escape(title)}</div>
            <div class="ux-card-body">{html_escape(body)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_labeled_block(label, body, callout=False):
    if not body:
        return

    class_name = "soft-callout" if callout else "ux-card-body"
    st.markdown(
        f"""
        <div class="ux-card-label">{html_escape(label)}</div>
        <div class="{class_name}">{html_escape(body)}</div>
        """,
        unsafe_allow_html=True,
    )


def render_list_card(title, items):
    items = items or []
    body = "".join(f"<li>{html_escape(item)}</li>" for item in items)
    if not body:
        body = "<li>No data generated.</li>"

    st.markdown(
        f"""
        <div class="ux-card">
            <div class="ux-card-title">{html_escape(title)}</div>
            <ul class="ux-card-body" style="padding-left:18px; margin:0;">{body}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_insight_item(item, labels, fields):
    title = item.get("title", labels["no_data"])
    blocks = [f'<div class="ux-card-title">{html_escape(title)}</div>']

    for label_key, data_key, is_callout in fields:
        body = item.get(data_key, "")
        if body:
            class_name = "soft-callout" if is_callout else "ux-card-body"
            blocks.append(
                f"""
                <div class="ux-card-label">{html_escape(labels[label_key])}</div>
                <div class="{class_name}">{html_escape(body)}</div>
                """
            )

    evidence = item.get("supporting_quote_or_evidence", "")
    if evidence:
        blocks.append(
            f'<div class="evidence-box"><strong>{html_escape(labels["evidence"])}:</strong> {html_escape(evidence)}</div>'
        )

    st.markdown(
        f'<div class="ux-card">{"".join(blocks)}</div>',
        unsafe_allow_html=True,
    )


def render_output_tabs(analysis_data, theory_support, output_options, ui_language="English"):
    labels = get_render_labels(ui_language)
    inject_result_styles()

    tab_keys = output_options.copy()
    tab_keys.append("Download")

    tab_display_names = [labels.get(key, key) for key in tab_keys]
    tabs = st.tabs(tab_display_names)
    tab_map = dict(zip(tab_keys, tabs))

    st.markdown('<div class="result-shell"></div>', unsafe_allow_html=True)

    if "Overview" in tab_map:
        with tab_map["Overview"]:
            section_header(labels["project_overview"], labels["overview_caption"], labels["Overview"])
            overview = analysis_data.get("project_overview", {})

            overview_cards = [
                (labels["research_context"], overview.get("research_context", labels["no_research_context"]), True),
                (labels["main_user_group"], overview.get("main_user_group", labels["no_user_group"]), False),
                (labels["core_problem"], overview.get("core_problem", labels["no_core_problem"]), True),
                (labels["research_limitations"], overview.get("research_limitations", labels["no_limitations"]), False),
            ]

            cols = st.columns(2)
            for index, (title, body, accent) in enumerate(overview_cards):
                with cols[index % 2]:
                    render_info_card(title, body, accent=accent)

    if "Insights" in tab_map:
        with tab_map["Insights"]:
            section_header(labels["ux_insights"], None, labels["Insights"])
            ux_insights = analysis_data.get("ux_insights", {})

            insight_groups = [
                (
                    labels["pain_points"],
                    ux_insights.get("pain_points", []),
                    [
                        ("what_happens", "what_happens", False),
                        ("why_it_matters", "why_it_matters", False),
                        ("design_implication", "design_implication", True),
                    ],
                ),
                (
                    labels["behavioral_patterns"],
                    ux_insights.get("behavioral_patterns", []),
                    [
                        ("observed_behavior", "observed_behavior", False),
                        ("interpretation", "interpretation", False),
                        ("design_implication", "design_implication", True),
                    ],
                ),
                (
                    labels["emotional_needs"],
                    ux_insights.get("emotional_needs", []),
                    [
                        ("emotional_signal", "emotional_signal", False),
                        ("underlying_need", "underlying_need", False),
                        ("design_implication", "design_implication", True),
                    ],
                ),
            ]

            for group_title, items, fields in insight_groups:
                section_header(group_title)
                if items:
                    cols = st.columns(2)
                    for index, item in enumerate(items):
                        with cols[index % 2]:
                            render_insight_item(item, labels, fields)
                else:
                    st.write(labels["no_data"])

    if "Affinity Map" in tab_map:
        with tab_map["Affinity Map"]:
            section_header(labels["Affinity Map"], labels["affinity_caption"], labels["Affinity Map"])
            affinity_map = analysis_data.get("affinity_map", [])

            if affinity_map:
                for group in affinity_map:
                    theme = group.get("theme", labels["no_data"])
                    theme_summary = group.get("theme_summary", "")
                    design_opportunity = group.get("design_opportunity", "")

                    with st.container(border=True):
                        st.markdown(f"### {theme}")

                        if theme_summary:
                            render_labeled_block(labels["theme_summary"], theme_summary)

                        st.markdown(f"#### {labels['insight_notes']}")
                        insights = group.get("insights", [])
                        if insights:
                            note_cols = st.columns(3)
                            for index, insight in enumerate(insights):
                                with note_cols[index % 3]:
                                    st.markdown(
                                        f'<div class="note-card">{html_escape(insight)}</div>',
                                        unsafe_allow_html=True,
                                    )
                        else:
                            st.write(labels["no_data"])

                        evidence_list = group.get("evidence", [])
                        if evidence_list:
                            st.markdown(f"#### {labels['supporting_evidence']}")
                            evidence_cols = st.columns(2)
                            for index, evidence in enumerate(evidence_list):
                                with evidence_cols[index % 2]:
                                    st.markdown(
                                        f'<div class="evidence-box">{html_escape(evidence)}</div>',
                                        unsafe_allow_html=True,
                                    )

                        if design_opportunity:
                            render_labeled_block(labels["design_opportunity"], design_opportunity, callout=True)
            else:
                st.write(labels["no_data"])

    if "Persona" in tab_map:
        with tab_map["Persona"]:
            section_header(labels["user_persona"], None, labels["Persona"])
            persona = analysis_data.get("user_persona", {})

            name = persona.get("name", "Unnamed Persona")
            role = persona.get("role", "")
            background = persona.get("background", "")
            primary_goal = persona.get("primary_goal", "")
            quote = persona.get("quote", "")
            initials = "".join([part[0].upper() for part in name.split()[:2]]) if name else "U"

            st.markdown(
                f"""
                <div class="persona-header">
                    <div class="persona-row">
                        <div class="avatar">{html_escape(initials)}</div>
                        <div>
                            <div class="persona-name">{html_escape(name)}</div>
                            <div class="persona-role">{html_escape(role)}</div>
                            <div class="ux-card-body" style="margin-top:10px;">{html_escape(background)}</div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            goal_col, quote_col = st.columns([1.1, 1])
            with goal_col:
                render_info_card(labels["primary_goal"], primary_goal or labels["no_data"], accent=True)
            with quote_col:
                quote_text = f'"{quote}"' if quote else labels["no_data"]
                st.markdown(f'<div class="quote-box">{html_escape(quote_text)}</div>', unsafe_allow_html=True)

            section_header(labels["persona_details"])
            persona_sections = [
                (labels["goals"], persona.get("goals", [])),
                (labels["frustrations"], persona.get("frustrations", [])),
                (labels["needs"], persona.get("needs", [])),
                (labels["behaviors"], persona.get("behaviors", [])),
                (labels["trust_barriers"], persona.get("trust_barriers", [])),
            ]

            cols = st.columns(3)
            for index, (title, items) in enumerate(persona_sections):
                with cols[index % 3]:
                    render_list_card(title, items)

    if "Journey Map" in tab_map:
        with tab_map["Journey Map"]:
            section_header(labels["Journey Map"], labels["journey_caption"], labels["Journey Map"])
            journey = analysis_data.get("user_journey_map", [])

            if journey:
                cols = st.columns(3)
                for index, stage in enumerate(journey):
                    with cols[index % 3]:
                        blocks = [
                            f'<div class="badge">{html_escape(stage.get("stage", labels["no_data"]))}</div>'
                        ]
                        stage_fields = [
                            (labels["user_goal"], stage.get("user_goal", ""), False),
                            (labels["actions"], stage.get("user_actions", ""), False),
                            (labels["thoughts"], stage.get("thoughts", ""), False),
                            (labels["emotions"], stage.get("emotions", ""), False),
                            (labels["pain_points"], stage.get("pain_points", ""), True),
                            (labels["opportunities"], stage.get("opportunities", ""), True),
                            (labels["feature_response"], stage.get("possible_feature_response", ""), False),
                        ]
                        for label, body, is_callout in stage_fields:
                            if body:
                                class_name = "soft-callout" if is_callout else "ux-card-body"
                                blocks.append(
                                    f"""
                                    <div class="ux-card-label">{html_escape(label)}</div>
                                    <div class="{class_name}">{html_escape(body)}</div>
                                    """
                                )
                        st.markdown(
                            f'<div class="ux-card journey-stage">{"".join(blocks)}</div>',
                            unsafe_allow_html=True,
                        )
            else:
                st.write(labels["no_data"])

    if "Service Blueprint" in tab_map:
        with tab_map["Service Blueprint"]:
            section_header(labels["Service Blueprint"], labels["blueprint_caption"], labels["Service Blueprint"])
            blueprint = analysis_data.get("service_blueprint", [])

            if blueprint:
                stages = [
                    item.get("stage", f"Stage {i + 1}")
                    for i, item in enumerate(blueprint)
                ]

                blueprint_layers = [
                    {
                        labels["layer"]: labels["user_actions"],
                        **{
                            stage: blueprint[index].get("user_actions", "")
                            for index, stage in enumerate(stages)
                        },
                    },
                    {
                        labels["layer"]: labels["frontstage_touchpoints"],
                        **{
                            stage: blueprint[index].get("frontstage_touchpoints", "")
                            for index, stage in enumerate(stages)
                        },
                    },
                    {
                        labels["layer"]: labels["backstage_processes"],
                        **{
                            stage: blueprint[index].get("backstage_processes", "")
                            for index, stage in enumerate(stages)
                        },
                    },
                    {
                        labels["layer"]: labels["support_systems"],
                        **{
                            stage: blueprint[index].get("support_systems", "")
                            for index, stage in enumerate(stages)
                        },
                    },
                    {
                        labels["layer"]: labels["pain_points"],
                        **{
                            stage: blueprint[index].get("pain_points", "")
                            for index, stage in enumerate(stages)
                        },
                    },
                    {
                        labels["layer"]: labels["opportunities"],
                        **{
                            stage: blueprint[index].get("opportunities", "")
                            for index, stage in enumerate(stages)
                        },
                    },
                    {
                        labels["layer"]: labels["design_requirement"],
                        **{
                            stage: blueprint[index].get("design_requirement", "")
                            for index, stage in enumerate(stages)
                        },
                    },
                ]

                blueprint_df = pd.DataFrame(blueprint_layers)

                with st.container(border=True):
                    st.dataframe(
                        blueprint_df,
                        use_container_width=True,
                        hide_index=True,
                    )
            else:
                st.write(labels["no_data"])

    if "Theory Support" in tab_map:
        with tab_map["Theory Support"]:
            section_header(labels["Theory Support"], None, labels["Theory Support"])

            if theory_support:
                with st.container(border=True):
                    st.markdown(theory_support)
            else:
                st.write(labels["no_data"])

    if "Design Directions" in tab_map:
        with tab_map["Design Directions"]:
            section_header(labels["Design Directions"], None, labels["Design Directions"])
            directions = analysis_data.get("design_directions", {})

            render_info_card(
                labels["problem_statement"],
                directions.get("problem_statement", labels["no_data"]),
                accent=True,
            )

            principles = directions.get("design_principles", [])
            section_header(labels["design_principles"])
            cols = st.columns(3)
            for index, principle in enumerate(principles or [labels["no_data"]]):
                with cols[index % 3]:
                    render_info_card(f"{labels['design_principles']} {index + 1}", principle)

            section_header(labels["opportunity_areas"])
            opportunity_areas = directions.get("opportunity_areas", [])
            if opportunity_areas:
                cols = st.columns(2)
                for index, area in enumerate(opportunity_areas):
                    with cols[index % 2]:
                        blocks = [
                            f'<div class="ux-card-title">{html_escape(area.get("title", labels["no_data"]))}</div>',
                            f'<div class="ux-card-body">{html_escape(area.get("description", ""))}</div>',
                        ]
                        why = area.get("why_it_matters", "")
                        if why:
                            blocks.append(
                                f'<div class="evidence-box"><strong>{html_escape(labels["why_it_matters"])}:</strong> {html_escape(why)}</div>'
                            )
                        st.markdown(
                            f'<div class="ux-card">{"".join(blocks)}</div>',
                            unsafe_allow_html=True,
                        )
            else:
                st.write(labels["no_data"])

            section_header(labels["recommended_features"])
            recommended_features = directions.get("recommended_features", [])
            if recommended_features:
                for feature in recommended_features:
                    with st.container(border=True):
                        col1, col2 = st.columns([2.4, 0.8])

                        with col1:
                            st.markdown(f"### {feature.get('feature', labels['no_data'])}")
                            st.write(feature.get("reason", ""))

                            problem_addressed = feature.get("user_problem_addressed", "")
                            if problem_addressed:
                                st.caption(f"{labels['user_problem_addressed']}: {problem_addressed}")

                        with col2:
                            priority = feature.get("priority", "Medium")
                            st.metric(labels["priority"], priority)
            else:
                st.write(labels["no_data"])

            section_header(labels["final_direction_summary"])
            st.markdown(
                f'<div class="soft-callout">{html_escape(directions.get("final_direction_summary", labels["no_data"]))}</div>',
                unsafe_allow_html=True,
            )

            section_header(labels["next_research_questions"])
            render_list_card(labels["next_research_questions"], directions.get("next_research_questions", []))

    with tab_map["Download"]:
        section_header(labels["download_report"], labels["download_caption"], labels["Download"])

        docx_file = generate_docx_report(analysis_data, theory_support)
        saved_report_path = save_docx_report(docx_file)
        json_file = json.dumps(analysis_data, ensure_ascii=False, indent=2)

        with st.container(border=True):
            st.caption(f"{labels['report_saved']} {saved_report_path}")

            col1, col2 = st.columns(2)
            with col1:
                st.download_button(
                    label=labels["download_word"],
                    data=docx_file,
                    file_name="ux_research_report.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    key="download_word_report",
                    type="primary",
                    use_container_width=True,
                )

            with col2:
                st.download_button(
                    label=labels["download_json"],
                    data=json_file,
                    file_name="ux_research_data.json",
                    mime="application/json",
                    key="download_json_data",
                    use_container_width=True,
                )

            with st.expander(labels["raw_json"]):
                st.json(analysis_data)
