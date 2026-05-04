import streamlit as st

from agents.analysis_agent import analyze_ux_research
from agents.theory_agent import search_theory_support
from utils.file_utils import read_uploaded_file, save_uploaded_file
from utils.output_utils import (
    save_analysis_json,
    list_analysis_history,
    load_analysis_json
)
from utils.language_utils import get_output_language, get_ui_text
from ui.render_tabs import render_output_tabs


# ====================
# Page Config
# Must be the first Streamlit command
# ====================

st.set_page_config(
    page_title="UX Research Agent",
    page_icon="🧠",
    layout="wide"
)


# ====================
# Session State
# ====================

if "analysis_data" not in st.session_state:
    st.session_state.analysis_data = None

if "theory_support" not in st.session_state:
    st.session_state.theory_support = None

if "last_saved_json_path" not in st.session_state:
    st.session_state.last_saved_json_path = None

if "loaded_history_name" not in st.session_state:
    st.session_state.loaded_history_name = None

if "current_output_options" not in st.session_state:
    st.session_state.current_output_options = None


# ====================
# Language Setting
# ====================

ui_language = st.sidebar.radio(
    "Language / 语言",
    ["English", "中文"],
    horizontal=True
)

ui_text = get_ui_text(ui_language)


# ====================
# Page Header
# ====================

st.title(ui_text["page_title"])
st.write(ui_text["page_description"])


# ====================
# Sidebar
# ====================

with st.sidebar:
    st.header(ui_text["input"])

    uploaded_file = st.file_uploader(
        ui_text["upload_file"],
        type=["txt"]
    )

    st.divider()

    # ====================
    # History
    # ====================

    if ui_language == "中文":
        st.write("**历史记录**")
        history_caption = "从 outputs/json/ 中读取过去生成的分析结果。"
        history_select_label = "选择历史记录"
        load_history_button = "加载历史记录"
        no_history_text = "暂无历史记录。"
        history_loaded_text = "已加载历史记录："
    else:
        st.write("**History**")
        history_caption = "Load previous analysis results from outputs/json/."
        history_select_label = "Select history"
        load_history_button = "Load History"
        no_history_text = "No history yet."
        history_loaded_text = "Loaded history:"

    st.caption(history_caption)

    history_files = list_analysis_history()

    if history_files:
        history_display_names = [path.name for path in history_files]

        selected_history_name = st.selectbox(
            history_select_label,
            history_display_names,
            index=0
        )

        if st.button(load_history_button):
            selected_index = history_display_names.index(selected_history_name)
            selected_path = history_files[selected_index]

            loaded_data = load_analysis_json(selected_path)

            st.session_state.analysis_data = loaded_data
            st.session_state.theory_support = (
                "历史记录仅加载了结构化分析 JSON。理论支持如需更新，请重新生成报告。"
                if ui_language == "中文"
                else "History loaded from saved JSON. Theory support was not stored in this history record."
            )
            st.session_state.loaded_history_name = selected_path.name
            st.session_state.last_saved_json_path = selected_path
            st.session_state.current_output_options = None

            st.success(f"{history_loaded_text} {selected_path.name}")
    else:
        st.caption(no_history_text)

    st.divider()

    # ====================
    # Output Options
    # ====================

    st.write(f"**{ui_text['output_options']}**")

    include_overview = st.checkbox(ui_text["overview"], value=True)
    include_insights = st.checkbox(ui_text["insights"], value=True)
    include_affinity_map = st.checkbox(ui_text["affinity_map"], value=True)
    include_persona = st.checkbox(ui_text["persona"], value=True)
    include_journey_map = st.checkbox(ui_text["journey_map"], value=True)
    include_service_blueprint = st.checkbox(ui_text["service_blueprint"], value=True)
    include_theory_support = st.checkbox(ui_text["theory_support"], value=True)
    include_design_directions = st.checkbox(ui_text["design_directions"], value=True)

    output_options = []

    # Internal option keys remain English.
    # Only UI labels are translated.
    if include_overview:
        output_options.append("Overview")
    if include_insights:
        output_options.append("Insights")
    if include_affinity_map:
        output_options.append("Affinity Map")
    if include_persona:
        output_options.append("Persona")
    if include_journey_map:
        output_options.append("Journey Map")
    if include_service_blueprint:
        output_options.append("Service Blueprint")
    if include_theory_support:
        output_options.append("Theory Support")
    if include_design_directions:
        output_options.append("Design Directions")

    st.divider()

    run_web_search = st.checkbox(
        ui_text["search_theory"],
        value=True
    )

    st.caption(ui_text["search_caption"])

    st.divider()

    if ui_language == "中文":
        clear_label = "清除当前结果"
    else:
        clear_label = "Clear Current Result"

    if st.button(clear_label):
        st.session_state.analysis_data = None
        st.session_state.theory_support = None
        st.session_state.last_saved_json_path = None
        st.session_state.loaded_history_name = None
        st.session_state.current_output_options = None
        st.success("Cleared." if ui_language == "English" else "已清除。")


# ====================
# File Input Handling
# ====================

if uploaded_file is not None:
    saved_upload_path = save_uploaded_file(uploaded_file)
else:
    saved_upload_path = None

file_text = read_uploaded_file(uploaded_file)

if saved_upload_path is not None:
    if ui_language == "中文":
        st.sidebar.success(f"上传文件已保存：{saved_upload_path.name}")
    else:
        st.sidebar.success(f"Saved upload: {saved_upload_path.name}")


# ====================
# Main Text Input
# ====================

research_text = st.text_area(
    ui_text["text_area_label"],
    value=file_text,
    height=300,
    placeholder=ui_text["text_area_placeholder"]
)

output_language = get_output_language(ui_language, research_text)


# ====================
# Main Workflow
# ====================

if st.button(ui_text["generate_button"]):
    if research_text.strip() == "":
        st.warning(ui_text["empty_warning"])

    elif not output_options:
        st.warning(ui_text["option_warning"])

    else:
        with st.spinner(ui_text["analyzing"]):
            analysis_data = analyze_ux_research(
                research_text=research_text,
                output_language=output_language
            )

        if analysis_data is not None:
            saved_json_path = save_analysis_json(analysis_data)

            st.session_state.analysis_data = analysis_data
            st.session_state.last_saved_json_path = saved_json_path
            st.session_state.loaded_history_name = None
            st.session_state.current_output_options = output_options.copy()

            st.success(ui_text["analysis_success"])
            st.caption(f"{ui_text['json_saved']} {saved_json_path}")

            if "Theory Support" in output_options and run_web_search:
                with st.spinner(ui_text["searching"]):
                    theory_support = search_theory_support(
                        analysis_data=analysis_data,
                        output_language=output_language
                    )
            else:
                if ui_language == "中文":
                    theory_support = "已跳过理论支持搜索。"
                else:
                    theory_support = "Theory search was skipped."

            st.session_state.theory_support = theory_support

            st.success(ui_text["report_success"])


# ====================
# Persistent Results Display
# ====================

if st.session_state.analysis_data is not None:
    if st.session_state.loaded_history_name:
        if ui_language == "中文":
            st.info(f"当前显示历史记录：{st.session_state.loaded_history_name}")
        else:
            st.info(f"Currently viewing history: {st.session_state.loaded_history_name}")

    elif st.session_state.last_saved_json_path is not None:
        if ui_language == "中文":
            st.caption(f"当前分析 JSON：{st.session_state.last_saved_json_path}")
        else:
            st.caption(f"Current analysis JSON: {st.session_state.last_saved_json_path}")

    display_output_options = output_options

    if not display_output_options:
        display_output_options = st.session_state.current_output_options

    if not display_output_options:
        display_output_options = [
            "Overview",
            "Insights",
            "Affinity Map",
            "Persona",
            "Journey Map",
            "Service Blueprint",
            "Theory Support",
            "Design Directions"
        ]

    render_output_tabs(
        analysis_data=st.session_state.analysis_data,
        theory_support=st.session_state.theory_support or "",
        output_options=display_output_options,
        ui_language=ui_language
    )