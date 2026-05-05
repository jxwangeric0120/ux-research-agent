import streamlit as st

from agents.analysis_agent import analyze_ux_research
from agents.theory_agent import search_theory_support
from utils.file_utils import read_uploaded_file, save_uploaded_file
from utils.output_utils import (
    save_analysis_json,
    list_analysis_history,
    load_analysis_json,
)
from utils.language_utils import get_output_language, get_ui_text
from ui.render_tabs import render_output_tabs


PRIMARY_COLOR = "#2E60FD"


st.set_page_config(
    page_title="UX Research Agent",
    page_icon="UX",
    layout="wide",
)


def inject_theme():
    st.markdown(
        f"""
        <style>
            :root {{
                --primary: {PRIMARY_COLOR};
                --primary-soft: #EAF0FF;
                --primary-muted: #BFD0FF;
                --ink: #111827;
                --muted: #667085;
                --line: #E4E7EC;
                --panel: #FFFFFF;
                --canvas: #F6F8FC;
            }}

            .stApp {{
                background: var(--canvas);
                color: var(--ink);
            }}

            [data-testid="stAppViewContainer"] > .main {{
                background: var(--canvas);
            }}

            [data-testid="stHeader"] {{
                background: rgba(246, 248, 252, 0.86);
                backdrop-filter: blur(10px);
                border-bottom: 1px solid rgba(228, 231, 236, 0.75);
            }}

            [data-testid="stSidebar"] {{
                background: #F0F3F9;
                border-right: 1px solid var(--line);
            }}

            [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
            [data-testid="stSidebar"] label,
            [data-testid="stSidebar"] span {{
                color: var(--ink);
            }}

            .block-container {{
                max-width: 1480px;
                padding-top: 4.25rem;
                padding-bottom: 4rem;
            }}

            h1, h2, h3, h4 {{
                letter-spacing: 0;
                color: var(--ink);
            }}

            div[data-testid="stVerticalBlockBorderWrapper"] {{
                border: 1px solid var(--line);
                border-radius: 8px;
                box-shadow: 0 1px 2px rgba(16, 24, 40, 0.04);
                background: var(--panel);
            }}

            .workspace-hero {{
                border: 1px solid var(--line);
                border-radius: 8px;
                background: var(--panel);
                padding: 28px 30px;
                margin-bottom: 18px;
                box-shadow: 0 1px 2px rgba(16, 24, 40, 0.04);
            }}

            .eyebrow {{
                color: var(--primary);
                font-size: 13px;
                font-weight: 700;
                text-transform: uppercase;
                margin-bottom: 8px;
            }}

            .workspace-hero h1 {{
                font-size: 42px;
                line-height: 1.08;
                margin: 0 0 10px 0;
            }}

            .workspace-hero p {{
                max-width: 760px;
                color: var(--muted);
                font-size: 16px;
                line-height: 1.58;
                margin: 0;
            }}

            .status-row {{
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
                margin-top: 20px;
            }}

            .status-pill {{
                display: inline-flex;
                align-items: center;
                gap: 8px;
                border: 1px solid var(--line);
                border-radius: 999px;
                background: #FFFFFF;
                padding: 8px 12px;
                color: #344054;
                font-size: 13px;
                font-weight: 600;
            }}

            .status-pill strong {{
                color: var(--primary);
            }}

            .panel-title {{
                font-size: 18px;
                font-weight: 750;
                margin-bottom: 4px;
            }}

            .panel-caption {{
                color: var(--muted);
                font-size: 14px;
                line-height: 1.5;
                margin-bottom: 16px;
            }}

            .hint-box {{
                border: 1px solid #D8E2FF;
                border-radius: 8px;
                background: #F8FAFF;
                padding: 14px 16px;
                color: #1D2939;
                margin-top: 12px;
                margin-bottom: 18px;
            }}

            .hint-box strong {{
                display: inline;
                color: var(--primary);
                margin-right: 8px;
            }}

            .upload-strip {{
                border: 1px solid #E4E7EC;
                border-radius: 8px;
                background: #FFFFFF;
                padding: 14px 16px;
                margin: 16px 0 10px 0;
            }}

            .upload-strip-title {{
                color: #101828;
                font-size: 14px;
                font-weight: 750;
                margin-bottom: 2px;
            }}

            .upload-strip-copy {{
                color: #667085;
                font-size: 13px;
                line-height: 1.45;
                margin-bottom: 10px;
            }}

            [data-testid="stFileUploader"] section {{
                background: #F8FAFC;
                border: 1px dashed #C9D3E7;
                border-radius: 8px;
                padding: 10px 12px;
            }}

            [data-testid="stFileUploader"] section > div {{
                padding: 0;
            }}

            [data-testid="stFileUploader"] small {{
                color: #667085;
            }}

            .sidebar-section {{
                border-top: 1px solid #D0D5DD;
                padding-top: 18px;
                margin-top: 18px;
            }}

            .sidebar-heading {{
                color: #101828;
                font-size: 13px;
                font-weight: 750;
                text-transform: uppercase;
                margin-bottom: 10px;
            }}

            .stButton > button,
            .stDownloadButton > button {{
                border-radius: 8px;
                border: 1px solid #C9D3E7;
                font-weight: 700;
                min-height: 42px;
            }}

            .stButton > button[kind="primary"],
            .stDownloadButton > button[kind="primary"] {{
                background: var(--primary);
                border-color: var(--primary);
                color: white;
            }}

            .stButton > button:hover,
            .stDownloadButton > button:hover {{
                border-color: var(--primary);
                color: var(--primary);
            }}

            .stButton > button[kind="primary"]:hover,
            .stDownloadButton > button[kind="primary"]:hover {{
                background: #2555E8;
                color: white;
            }}

            textarea {{
                border-radius: 8px !important;
                border-color: #D0D5DD !important;
                background: #FBFCFE !important;
                min-height: 360px !important;
            }}

            textarea:focus,
            input:focus {{
                border-color: var(--primary) !important;
                box-shadow: 0 0 0 3px rgba(46, 96, 253, 0.12) !important;
            }}

            div[data-baseweb="tab-list"] {{
                gap: 8px;
                border-bottom: 1px solid var(--line);
            }}

            button[data-baseweb="tab"] {{
                border-radius: 8px 8px 0 0;
                color: #475467;
                font-weight: 700;
            }}

            button[data-baseweb="tab"][aria-selected="true"] {{
                color: var(--primary);
                background: var(--primary-soft);
            }}

            div[data-testid="stMetric"] {{
                background: #FFFFFF;
                border: 1px solid var(--line);
                border-radius: 8px;
                padding: 14px;
            }}

            .stAlert {{
                border-radius: 8px;
            }}

            @media (max-width: 768px) {{
                .block-container {{
                    padding-left: 1rem;
                    padding-right: 1rem;
                }}

                .workspace-hero {{
                    padding: 22px;
                }}

                .workspace-hero h1 {{
                    font-size: 32px;
                }}
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def section_heading(text):
    st.markdown(f'<div class="sidebar-heading">{text}</div>', unsafe_allow_html=True)


def build_output_options(ui_text):
    option_definitions = [
        ("Overview", ui_text["overview"]),
        ("Insights", ui_text["insights"]),
        ("Affinity Map", ui_text["affinity_map"]),
        ("Persona", ui_text["persona"]),
        ("Journey Map", ui_text["journey_map"]),
        ("Service Blueprint", ui_text["service_blueprint"]),
        ("Theory Support", ui_text["theory_support"]),
        ("Design Directions", ui_text["design_directions"]),
    ]

    selected = []
    for key, label in option_definitions:
        if st.checkbox(label, value=True, key=f"output_{key}"):
            selected.append(key)

    return selected


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


inject_theme()


with st.sidebar:
    section_heading("UX Research Agent")

    ui_language = st.radio(
        "Language / 语言",
        ["English", "中文"],
        horizontal=True,
        key="ui_language",
    )

    ui_text = get_ui_text(ui_language)

    st.markdown('<div class="sidebar-section"></div>', unsafe_allow_html=True)
    section_heading(ui_text["history"])
    st.caption(ui_text["history_caption"])

    history_files = list_analysis_history()

    if history_files:
        history_display_names = [path.name for path in history_files]

        selected_history_name = st.selectbox(
            ui_text["history_select_label"],
            history_display_names,
            index=0,
        )

        if st.button(ui_text["load_history_button"], use_container_width=True):
            selected_index = history_display_names.index(selected_history_name)
            selected_path = history_files[selected_index]

            loaded_data = load_analysis_json(selected_path)

            st.session_state.analysis_data = loaded_data
            st.session_state.theory_support = (
                "历史记录仅加载了结构化分析 JSON。如需更新理论支持，请重新生成报告。"
                if ui_language == "中文"
                else "History loaded from saved JSON. Theory support was not stored in this history record."
            )
            st.session_state.loaded_history_name = selected_path.name
            st.session_state.last_saved_json_path = selected_path
            st.session_state.current_output_options = None

            st.success(f"{ui_text['history_loaded_text']} {selected_path.name}")
    else:
        st.caption(ui_text["no_history_text"])

    st.markdown('<div class="sidebar-section"></div>', unsafe_allow_html=True)
    section_heading(ui_text["output_options"])
    output_options = build_output_options(ui_text)
    st.caption(f"{ui_text['selected_count']} {len(output_options)} {ui_text['deliverables']}")

    st.markdown('<div class="sidebar-section"></div>', unsafe_allow_html=True)
    section_heading(ui_text["settings"])
    run_web_search = st.checkbox(
        ui_text["search_theory"],
        value=True,
        key="run_web_search",
    )
    st.caption(ui_text["search_caption"])

    st.markdown('<div class="sidebar-section"></div>', unsafe_allow_html=True)
    if st.button(ui_text["clear_current_result"], use_container_width=True):
        st.session_state.analysis_data = None
        st.session_state.theory_support = None
        st.session_state.last_saved_json_path = None
        st.session_state.loaded_history_name = None
        st.session_state.current_output_options = None
        st.success(ui_text["cleared"])


status_label = (
    ui_text["status_has_result"]
    if st.session_state.analysis_data is not None
    else ui_text["status_ready"]
)

output_language_label = (
    "Simplified Chinese"
    if ui_language == "中文"
    else "English"
)

st.markdown(
    f"""
    <section class="workspace-hero">
        <div class="eyebrow">{ui_text["workspace_label"]}</div>
        <h1>{ui_text["page_title"]}</h1>
        <p>{ui_text["page_description"]}</p>
        <div class="status-row">
            <span class="status-pill"><strong>{status_label}</strong></span>
            <span class="status-pill">{ui_text["language"]}: <strong>{output_language_label}</strong></span>
            <span class="status-pill">{ui_text["selected_count"]}: <strong>{len(output_options)}</strong></span>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)


uploaded_file = None
with st.container(border=True):
    st.markdown(f'<div class="panel-title">{ui_text["input"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="panel-caption">{ui_text["workspace_caption"]}</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown(
            f"""
            <div class="upload-strip">
                <div class="upload-strip-title">{ui_text["upload_file"]}</div>
                <div class="upload-strip-copy">{ui_text["upload_caption"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        uploaded_file = st.file_uploader(
            ui_text["upload_file"],
            type=["txt"],
            label_visibility="collapsed",
        )

    if uploaded_file is not None:
        saved_upload_path = save_uploaded_file(uploaded_file)
    else:
        saved_upload_path = None

    file_text = read_uploaded_file(uploaded_file)

    if saved_upload_path is not None:
        st.success(f"{ui_text['saved_upload']} {saved_upload_path.name}")

    research_text = st.text_area(
        ui_text["text_area_label"],
        value=file_text,
        placeholder=ui_text["text_area_placeholder"],
        label_visibility="visible",
    )

    generate_clicked = st.button(
        ui_text["generate_button"],
        type="primary",
        use_container_width=True,
    )

    st.markdown(
        f"""
        <div class="hint-box">
            <strong>{ui_text["input_hint_title"]}</strong>
            {ui_text["input_hint_body"]}
        </div>
        """,
        unsafe_allow_html=True,
    )


output_language = get_output_language(ui_language, research_text)


if generate_clicked:
    if research_text.strip() == "":
        st.warning(ui_text["empty_warning"])

    elif not output_options:
        st.warning(ui_text["option_warning"])

    else:
        with st.spinner(ui_text["analyzing"]):
            analysis_data = analyze_ux_research(
                research_text=research_text,
                output_language=output_language,
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
                        output_language=output_language,
                    )
            else:
                theory_support = (
                    "已跳过理论支持搜索。"
                    if ui_language == "中文"
                    else "Theory search was skipped."
                )

            st.session_state.theory_support = theory_support
            st.success(ui_text["report_success"])


if st.session_state.analysis_data is not None:
    if st.session_state.loaded_history_name:
        st.info(f"{ui_text['current_history']} {st.session_state.loaded_history_name}")

    elif st.session_state.last_saved_json_path is not None:
        st.caption(f"{ui_text['current_json']} {st.session_state.last_saved_json_path}")

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
            "Design Directions",
        ]

    render_output_tabs(
        analysis_data=st.session_state.analysis_data,
        theory_support=st.session_state.theory_support or "",
        output_options=display_output_options,
        ui_language=ui_language,
    )
