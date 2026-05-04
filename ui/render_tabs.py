import json

import pandas as pd
import streamlit as st

from utils.doc_generator import generate_docx_report
from utils.output_utils import save_docx_report
from utils.json_utils import html_escape


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
            "insight_notes": "洞察便利贴",
            "supporting_evidence": "支持证据",
            "design_opportunity": "设计机会",
            "theme_summary": "主题总结",

            "user_persona": "用户画像",
            "primary_goal": "核心目标",
            "quote": "用户引语",
            "persona_details": "用户画像详情",
            "goals": "目标",
            "frustrations": "挫败点",
            "needs": "需求",
            "behaviors": "行为",
            "trust_barriers": "信任障碍",

            "journey_caption": "基于阶段的用户旅程视图，展示用户目标、行为、情绪、痛点与设计机会。",
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
    }


def render_output_tabs(analysis_data, theory_support, output_options, ui_language="English"):
    labels = get_render_labels(ui_language)

    tab_keys = output_options.copy()
    tab_keys.append("Download")

    tab_display_names = [labels.get(key, key) for key in tab_keys]

    tabs = st.tabs(tab_display_names)
    tab_map = dict(zip(tab_keys, tabs))

    # ====================
    # Overview Tab
    # ====================

    if "Overview" in tab_map:
        with tab_map["Overview"]:
            st.subheader(labels["project_overview"])
            overview = analysis_data.get("project_overview", {})

            with st.container(border=True):
                st.markdown(f"### {labels['research_context']}")
                st.write(overview.get("research_context", labels["no_research_context"]))

                st.markdown(f"### {labels['main_user_group']}")
                st.write(overview.get("main_user_group", labels["no_user_group"]))

                st.markdown(f"### {labels['core_problem']}")
                st.info(overview.get("core_problem", labels["no_core_problem"]))

                st.markdown(f"### {labels['research_limitations']}")
                st.warning(overview.get("research_limitations", labels["no_limitations"]))

    # ====================
    # Insights Tab
    # ====================

    if "Insights" in tab_map:
        with tab_map["Insights"]:
            st.subheader(labels["ux_insights"])
            ux_insights = analysis_data.get("ux_insights", {})

            st.markdown(f"### {labels['pain_points']}")
            pain_points = ux_insights.get("pain_points", [])

            if pain_points:
                for item in pain_points:
                    with st.container(border=True):
                        st.markdown(f"#### {item.get('title', labels['no_data'])}")

                        st.markdown(f"**{labels['what_happens']}**")
                        st.write(item.get("what_happens", ""))

                        st.markdown(f"**{labels['why_it_matters']}**")
                        st.write(item.get("why_it_matters", ""))

                        st.markdown(f"**{labels['design_implication']}**")
                        st.info(item.get("design_implication", ""))

                        evidence = item.get("supporting_quote_or_evidence", "")
                        if evidence:
                            st.caption(f"{labels['evidence']}: {evidence}")
            else:
                st.write(labels["no_data"])

            st.markdown(f"### {labels['behavioral_patterns']}")
            behavioral_patterns = ux_insights.get("behavioral_patterns", [])

            if behavioral_patterns:
                for item in behavioral_patterns:
                    with st.container(border=True):
                        st.markdown(f"#### {item.get('title', labels['no_data'])}")

                        st.markdown(f"**{labels['observed_behavior']}**")
                        st.write(item.get("observed_behavior", ""))

                        st.markdown(f"**{labels['interpretation']}**")
                        st.write(item.get("interpretation", ""))

                        st.markdown(f"**{labels['design_implication']}**")
                        st.info(item.get("design_implication", ""))

                        evidence = item.get("supporting_quote_or_evidence", "")
                        if evidence:
                            st.caption(f"{labels['evidence']}: {evidence}")
            else:
                st.write(labels["no_data"])

            st.markdown(f"### {labels['emotional_needs']}")
            emotional_needs = ux_insights.get("emotional_needs", [])

            if emotional_needs:
                for item in emotional_needs:
                    with st.container(border=True):
                        st.markdown(f"#### {item.get('title', labels['no_data'])}")

                        st.markdown(f"**{labels['emotional_signal']}**")
                        st.write(item.get("emotional_signal", ""))

                        st.markdown(f"**{labels['underlying_need']}**")
                        st.write(item.get("underlying_need", ""))

                        st.markdown(f"**{labels['design_implication']}**")
                        st.info(item.get("design_implication", ""))

                        evidence = item.get("supporting_quote_or_evidence", "")
                        if evidence:
                            st.caption(f"{labels['evidence']}: {evidence}")
            else:
                st.write(labels["no_data"])

    # ====================
    # Affinity Map Tab
    # ====================

    if "Affinity Map" in tab_map:
        with tab_map["Affinity Map"]:
            st.subheader(labels["Affinity Map"])
            affinity_map = analysis_data.get("affinity_map", [])

            st.caption(labels["affinity_caption"])

            if affinity_map:
                for group in affinity_map:
                    with st.container(border=True):
                        theme = group.get("theme", labels["no_data"])
                        theme_summary = group.get("theme_summary", "")
                        design_opportunity = group.get("design_opportunity", "")

                        st.markdown(f"## {theme}")

                        if theme_summary:
                            st.markdown(f"**{labels['theme_summary']}**")
                            st.write(theme_summary)

                        st.markdown(f"### {labels['insight_notes']}")

                        insights = group.get("insights", [])

                        if insights:
                            notes_per_row = 3

                            for i in range(0, len(insights), notes_per_row):
                                row_notes = insights[i:i + notes_per_row]
                                cols = st.columns(len(row_notes))

                                for col, insight in zip(cols, row_notes):
                                    with col:
                                        st.markdown(
                                            f"""
                                            <div style="
                                                background: #FFF4B8;
                                                padding: 16px;
                                                border-radius: 12px;
                                                min-height: 130px;
                                                box-shadow: 0 2px 8px rgba(0,0,0,0.08);
                                                border: 1px solid rgba(0,0,0,0.06);
                                                margin-bottom: 12px;
                                            ">
                                                <div style="
                                                    font-size: 13px;
                                                    font-weight: 700;
                                                    margin-bottom: 8px;
                                                    color: #5B4A00;
                                                ">
                                                    Insight
                                                </div>
                                                <div style="
                                                    font-size: 15px;
                                                    line-height: 1.45;
                                                    color: #222222;
                                                ">
                                                    {html_escape(insight)}
                                                </div>
                                            </div>
                                            """,
                                            unsafe_allow_html=True
                                        )
                        else:
                            st.write(labels["no_data"])

                        st.markdown(f"### {labels['supporting_evidence']}")

                        evidence_list = group.get("evidence", [])

                        if evidence_list:
                            evidence_cols = st.columns(2)

                            for index, evidence in enumerate(evidence_list):
                                with evidence_cols[index % 2]:
                                    st.markdown(
                                        f"""
                                        <div style="
                                            background: #F3F4F6;
                                            padding: 14px;
                                            border-radius: 10px;
                                            border-left: 4px solid #9CA3AF;
                                            margin-bottom: 10px;
                                        ">
                                            <div style="
                                                font-size: 13px;
                                                font-weight: 700;
                                                margin-bottom: 6px;
                                                color: #4B5563;
                                            ">
                                                {html_escape(labels["evidence"])}
                                            </div>
                                            <div style="
                                                font-size: 14px;
                                                line-height: 1.45;
                                                color: #374151;
                                            ">
                                                {html_escape(evidence)}
                                            </div>
                                        </div>
                                        """,
                                        unsafe_allow_html=True
                                    )
                        else:
                            st.write(labels["no_data"])

                        st.markdown(f"### {labels['design_opportunity']}")

                        if design_opportunity:
                            st.markdown(
                                f"""
                                <div style="
                                    background: #E8F1FF;
                                    padding: 16px;
                                    border-radius: 12px;
                                    border: 1px solid #BFD7FF;
                                    margin-top: 8px;
                                ">
                                    <div style="
                                        font-size: 14px;
                                        font-weight: 700;
                                        margin-bottom: 6px;
                                        color: #1D4ED8;
                                    ">
                                        {html_escape(labels["opportunities"])}
                                    </div>
                                    <div style="
                                        font-size: 15px;
                                        line-height: 1.5;
                                        color: #1F2937;
                                    ">
                                        {html_escape(design_opportunity)}
                                    </div>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )
                        else:
                            st.write(labels["no_data"])

                        st.divider()
            else:
                st.write(labels["no_data"])

    # ====================
    # Persona Tab
    # ====================

    if "Persona" in tab_map:
        with tab_map["Persona"]:
            st.subheader(labels["user_persona"])
            persona = analysis_data.get("user_persona", {})

            name = persona.get("name", "Unnamed Persona")
            role = persona.get("role", "")
            background = persona.get("background", "")
            primary_goal = persona.get("primary_goal", "")
            quote = persona.get("quote", "")

            initials = "".join([part[0].upper() for part in name.split()[:2]]) if name else "U"

            # Header card
            st.markdown(
                f"""
                <div style="background:linear-gradient(135deg,#F8FAFC 0%,#EEF2FF 100%);
                            padding:24px;
                            border-radius:18px;
                            border:1px solid #E5E7EB;
                            box-shadow:0 4px 16px rgba(0,0,0,0.05);
                            margin-bottom:18px;">
                    <div style="display:flex; align-items:center; gap:18px;">
                        <div style="width:72px;
                                    height:72px;
                                    border-radius:50%;
                                    background:#4F46E5;
                                    color:white;
                                    display:flex;
                                    align-items:center;
                                    justify-content:center;
                                    font-size:24px;
                                    font-weight:700;
                                    flex-shrink:0;">
                            {html_escape(initials)}
                        </div>
                        <div>
                            <div style="font-size:28px;
                                        font-weight:800;
                                        color:#111827;
                                        margin-bottom:4px;">
                                {html_escape(name)}
                            </div>
                            <div style="font-size:15px;
                                        color:#4B5563;
                                        margin-bottom:6px;">
                                {html_escape(role)}
                            </div>
                            <div style="font-size:14px;
                                        color:#6B7280;
                                        line-height:1.5;">
                                {html_escape(background)}
                            </div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            col1, col2 = st.columns([1.2, 1])

            with col1:
                st.markdown(f"### {labels['primary_goal']}")
                st.info(primary_goal if primary_goal else labels["no_data"])

            with col2:
                st.markdown(f"### {labels['quote']}")
                if quote:
                    st.warning(f"“{quote}”")
                else:
                    st.write(labels["no_data"])

            st.markdown(f"### {labels['persona_details']}")

            persona_sections = [
                {
                    "title": labels["goals"],
                    "items": persona.get("goals", []),
                    "icon": "🎯"
                },
                {
                    "title": labels["frustrations"],
                    "items": persona.get("frustrations", []),
                    "icon": "⚠️"
                },
                {
                    "title": labels["needs"],
                    "items": persona.get("needs", []),
                    "icon": "💡"
                },
                {
                    "title": labels["behaviors"],
                    "items": persona.get("behaviors", []),
                    "icon": "🔁"
                },
                {
                    "title": labels["trust_barriers"],
                    "items": persona.get("trust_barriers", []),
                    "icon": "🔒"
                }
            ]

            cards_per_row = 3

            for i in range(0, len(persona_sections), cards_per_row):
                row_sections = persona_sections[i:i + cards_per_row]
                cols = st.columns(len(row_sections))

                for col, section in zip(cols, row_sections):
                    with col:
                        with st.container(border=True):
                            st.markdown(f"#### {section['icon']} {section['title']}")

                            items = section.get("items", [])

                            if items:
                                for item in items:
                                    st.markdown(f"- {item}")
                            else:
                                st.write(labels["no_data"])

    # ====================
    # Journey Map Tab
    # ====================

    if "Journey Map" in tab_map:
        with tab_map["Journey Map"]:
            st.subheader(labels["Journey Map"])
            journey = analysis_data.get("user_journey_map", [])

            if journey:
                st.caption(labels["journey_caption"])

                stages_per_row = 3

                for i in range(0, len(journey), stages_per_row):
                    row_stages = journey[i:i + stages_per_row]
                    cols = st.columns(len(row_stages))

                    for col, stage in zip(cols, row_stages):
                        with col:
                            with st.container(border=True):
                                st.markdown(f"### {stage.get('stage', labels['no_data'])}")

                                st.markdown(f"**{labels['user_goal']}**")
                                st.write(stage.get("user_goal", ""))

                                st.markdown(f"**{labels['actions']}**")
                                st.write(stage.get("user_actions", ""))

                                st.markdown(f"**{labels['thoughts']}**")
                                st.write(stage.get("thoughts", ""))

                                st.markdown(f"**{labels['emotions']}**")
                                st.write(stage.get("emotions", ""))

                                st.markdown(f"**{labels['pain_points']}**")
                                st.warning(stage.get("pain_points", ""))

                                st.markdown(f"**{labels['opportunities']}**")
                                st.info(stage.get("opportunities", ""))

                                st.markdown(f"**{labels['feature_response']}**")
                                st.write(stage.get("possible_feature_response", ""))
            else:
                st.write(labels["no_data"])

    # ====================
    # Service Blueprint Tab
    # ====================

    if "Service Blueprint" in tab_map:
        with tab_map["Service Blueprint"]:
            st.subheader(labels["Service Blueprint"])
            blueprint = analysis_data.get("service_blueprint", [])

            if blueprint:
                st.caption(labels["blueprint_caption"])

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
                        }
                    },
                    {
                        labels["layer"]: labels["frontstage_touchpoints"],
                        **{
                            stage: blueprint[index].get("frontstage_touchpoints", "")
                            for index, stage in enumerate(stages)
                        }
                    },
                    {
                        labels["layer"]: labels["backstage_processes"],
                        **{
                            stage: blueprint[index].get("backstage_processes", "")
                            for index, stage in enumerate(stages)
                        }
                    },
                    {
                        labels["layer"]: labels["support_systems"],
                        **{
                            stage: blueprint[index].get("support_systems", "")
                            for index, stage in enumerate(stages)
                        }
                    },
                    {
                        labels["layer"]: labels["pain_points"],
                        **{
                            stage: blueprint[index].get("pain_points", "")
                            for index, stage in enumerate(stages)
                        }
                    },
                    {
                        labels["layer"]: labels["opportunities"],
                        **{
                            stage: blueprint[index].get("opportunities", "")
                            for index, stage in enumerate(stages)
                        }
                    },
                    {
                        labels["layer"]: labels["design_requirement"],
                        **{
                            stage: blueprint[index].get("design_requirement", "")
                            for index, stage in enumerate(stages)
                        }
                    }
                ]

                blueprint_df = pd.DataFrame(blueprint_layers)

                st.dataframe(
                    blueprint_df,
                    use_container_width=True,
                    hide_index=True
                )

            else:
                st.write(labels["no_data"])

    # ====================
    # Theory Support Tab
    # ====================

    if "Theory Support" in tab_map:
        with tab_map["Theory Support"]:
            st.subheader(labels["Theory Support"])

            if theory_support:
                st.markdown(theory_support)
            else:
                st.write(labels["no_data"])

    # ====================
    # Design Directions Tab
    # ====================

    if "Design Directions" in tab_map:
        with tab_map["Design Directions"]:
            st.subheader(labels["Design Directions"])
            directions = analysis_data.get("design_directions", {})

            st.markdown(f"### {labels['problem_statement']}")
            st.info(directions.get("problem_statement", labels["no_data"]))

            st.markdown(f"### {labels['design_principles']}")
            design_principles = directions.get("design_principles", [])

            if design_principles:
                for item in design_principles:
                    st.markdown(f"- {item}")
            else:
                st.write(labels["no_data"])

            st.markdown(f"### {labels['opportunity_areas']}")
            opportunity_areas = directions.get("opportunity_areas", [])

            if opportunity_areas:
                for area in opportunity_areas:
                    with st.container(border=True):
                        st.markdown(f"#### {area.get('title', labels['no_data'])}")
                        st.write(area.get("description", ""))

                        why_it_matters = area.get("why_it_matters", "")
                        if why_it_matters:
                            st.caption(f"{labels['why_it_matters']}: {why_it_matters}")
            else:
                st.write(labels["no_data"])

            st.markdown(f"### {labels['recommended_features']}")
            recommended_features = directions.get("recommended_features", [])

            if recommended_features:
                for feature in recommended_features:
                    with st.container(border=True):
                        col1, col2 = st.columns([2, 1])

                        with col1:
                            st.markdown(f"#### {feature.get('feature', labels['no_data'])}")
                            st.write(feature.get("reason", ""))

                            problem_addressed = feature.get("user_problem_addressed", "")
                            if problem_addressed:
                                st.caption(f"{labels['user_problem_addressed']}: {problem_addressed}")

                        with col2:
                            priority = feature.get("priority", "Medium")
                            st.metric(labels["priority"], priority)
            else:
                st.write(labels["no_data"])

            st.markdown(f"### {labels['final_direction_summary']}")
            st.write(directions.get("final_direction_summary", labels["no_data"]))

            st.markdown(f"### {labels['next_research_questions']}")
            next_questions = directions.get("next_research_questions", [])

            if next_questions:
                for question in next_questions:
                    st.markdown(f"- {question}")
            else:
                st.write(labels["no_data"])

    # ====================
    # Download Tab
    # ====================

    with tab_map["Download"]:
        st.subheader(labels["download_report"])

        docx_file = generate_docx_report(analysis_data, theory_support)
        saved_report_path = save_docx_report(docx_file)

        st.caption(f"{labels['report_saved']} {saved_report_path}")

        st.download_button(
            label=labels["download_word"],
            data=docx_file,
            file_name="ux_research_report.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            key="download_word_report"
        )

        json_file = json.dumps(analysis_data, ensure_ascii=False, indent=2)

        st.download_button(
            label=labels["download_json"],
            data=json_file,
            file_name="ux_research_data.json",
            mime="application/json",
            key="download_json_data"
        )

        with st.expander(labels["raw_json"]):
            st.json(analysis_data)