import re


def contains_chinese(text):
    """Check whether the input text contains Chinese characters."""
    if not text:
        return False

    return bool(re.search(r"[\u4e00-\u9fff]", text))


def get_output_language(ui_language, research_text):
    """
    Decide the AI output language.

    Rules:
    1. If user input contains Chinese, output Chinese.
    2. Otherwise, follow the selected UI language.
    """
    if contains_chinese(research_text):
        return "Simplified Chinese"

    if ui_language == "中文":
        return "Simplified Chinese"

    return "English"


def get_ui_text(ui_language):
    """Return UI text dictionary based on selected language."""
    if ui_language == "中文":
        return {
            "page_title": "UX Research Agent",
            "page_description": "把访谈、问卷开放题和用户反馈转化为清晰的 UX 洞察、研究产物和可下载报告。",
            "workspace_label": "研究工作台",
            "workspace_caption": "粘贴或上传研究资料，选择需要的产物，然后生成结构化报告。",
            "input": "输入",
            "upload_file": "上传 .txt 文件",
            "upload_caption": "支持 TXT 文件，也可以直接粘贴文本。",
            "output_options": "输出选项",
            "overview": "项目概览",
            "insights": "UX 洞察",
            "affinity_map": "亲和图",
            "persona": "用户画像",
            "journey_map": "用户旅程图",
            "service_blueprint": "服务蓝图",
            "theory_support": "理论支持",
            "design_directions": "设计方向",
            "search_theory": "联网搜索理论支持",
            "search_caption": "关闭后会跳过理论搜索，只生成基础 UX 分析。",
            "text_area_label": "研究资料",
            "text_area_placeholder": "例如：我在买二手家具时会担心安全问题，也不想和陌生人交换联系方式……",
            "generate_button": "生成 UX 研究报告",
            "empty_warning": "请先粘贴或上传一些研究资料。",
            "option_warning": "请至少选择一个输出内容。",
            "analyzing": "正在分析 UX 研究资料……",
            "searching": "正在联网搜索理论支持……",
            "analysis_success": "UX 研究分析已生成。",
            "report_success": "报告已生成。",
            "json_saved": "分析 JSON 已保存到：",
            "language": "语言",
            "settings": "设置",
            "history": "历史记录",
            "history_caption": "从 outputs/json/ 读取过去生成的分析结果。",
            "history_select_label": "选择历史记录",
            "load_history_button": "加载历史记录",
            "no_history_text": "暂无历史记录。",
            "history_loaded_text": "已加载历史记录：",
            "clear_current_result": "清除当前结果",
            "cleared": "已清除。",
            "saved_upload": "上传文件已保存：",
            "current_history": "当前显示历史记录：",
            "current_json": "当前分析 JSON：",
            "selected_count": "已选择",
            "deliverables": "个产物",
            "input_hint_title": "输入建议",
            "input_hint_body": "可以放入多段访谈笔记、问卷开放题、客服反馈或可用性测试观察。资料越具体，生成结果越有依据。",
            "status_ready": "准备分析",
            "status_has_result": "已有结果",
        }

    return {
        "page_title": "UX Research Agent",
        "page_description": "Transform interview notes, survey responses, and user feedback into clear UX insights, artifacts, and downloadable reports.",
        "workspace_label": "Research Workspace",
        "workspace_caption": "Paste or upload research material, choose deliverables, and generate a structured report.",
        "input": "Input",
        "upload_file": "Upload a .txt file",
        "upload_caption": "Use a TXT file or paste the material directly.",
        "output_options": "Output Options",
        "overview": "Overview",
        "insights": "UX Insights",
        "affinity_map": "Affinity Map",
        "persona": "Persona",
        "journey_map": "Journey Map",
        "service_blueprint": "Service Blueprint",
        "theory_support": "Theory Support",
        "design_directions": "Design Directions",
        "search_theory": "Search theory support online",
        "search_caption": "Turn this off to skip theory search and test the core analysis first.",
        "text_area_label": "Research material",
        "text_area_placeholder": "Example: I feel unsafe when buying second-hand furniture from strangers...",
        "generate_button": "Generate UX Research Report",
        "empty_warning": "Please paste or upload some research material first.",
        "option_warning": "Please select at least one output option.",
        "analyzing": "Analyzing UX research...",
        "searching": "Searching theory support online...",
        "analysis_success": "UX research analysis generated successfully.",
        "report_success": "Report generated successfully.",
        "json_saved": "Analysis JSON saved to:",
        "language": "Language",
        "settings": "Settings",
        "history": "History",
        "history_caption": "Load previous analysis results from outputs/json/.",
        "history_select_label": "Select history",
        "load_history_button": "Load History",
        "no_history_text": "No history yet.",
        "history_loaded_text": "Loaded history:",
        "clear_current_result": "Clear Current Result",
        "cleared": "Cleared.",
        "saved_upload": "Saved upload:",
        "current_history": "Currently viewing history:",
        "current_json": "Current analysis JSON:",
        "selected_count": "Selected",
        "deliverables": "deliverables",
        "input_hint_title": "Input Guidance",
        "input_hint_body": "Use interview notes, open-ended survey answers, support feedback, or usability observations. More specific evidence leads to stronger outputs.",
        "status_ready": "Ready to analyze",
        "status_has_result": "Result available",
    }
