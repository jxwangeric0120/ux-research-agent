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
            "page_description": "分析用户研究资料，生成 UX 洞察、用户画像、旅程图、服务蓝图，并导出研究报告。",
            "input": "输入",
            "upload_file": "上传 .txt 文件",
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
            "search_caption": "如果联网搜索导致 API 报错，可以先关闭它测试基础分析功能。",
            "text_area_label": "在这里粘贴用户访谈、问卷开放题或用户反馈：",
            "text_area_placeholder": "例如：我在买二手家具时会担心安全问题，也不想和陌生人交换联系方式……",
            "generate_button": "生成 UX 研究报告",
            "empty_warning": "请先粘贴或上传一些研究材料。",
            "option_warning": "请至少选择一个输出内容。",
            "analyzing": "正在分析 UX 研究材料……",
            "searching": "正在联网搜索理论支持……",
            "analysis_success": "UX 研究分析已生成。",
            "report_success": "报告已生成。",
            "json_saved": "分析 JSON 已保存到：",
        }

    return {
        "page_title": "UX Research Agent",
        "page_description": "Analyze user research, search theory support, generate UX artifacts, and export a research report.",
        "input": "Input",
        "upload_file": "Upload a .txt file",
        "output_options": "Output Options",
        "overview": "Overview",
        "insights": "Insights",
        "affinity_map": "Affinity Map",
        "persona": "Persona",
        "journey_map": "Journey Map",
        "service_blueprint": "Service Blueprint",
        "theory_support": "Theory Support",
        "design_directions": "Design Directions",
        "search_theory": "Search theory support online",
        "search_caption": "If web search causes an API error, turn this off and test the analysis first.",
        "text_area_label": "Paste user interview notes, survey responses, or user feedback here:",
        "text_area_placeholder": "Example: I feel unsafe when buying second-hand furniture from strangers...",
        "generate_button": "Generate UX Research Report",
        "empty_warning": "Please paste or upload some research material first.",
        "option_warning": "Please select at least one output option.",
        "analyzing": "Analyzing UX research...",
        "searching": "Searching theory support online...",
        "analysis_success": "UX research analysis generated successfully.",
        "report_success": "Report generated successfully.",
        "json_saved": "Analysis JSON saved to:",
    }