import json
from pathlib import Path
from datetime import datetime


JSON_OUTPUT_DIR = Path("outputs/json")
REPORT_OUTPUT_DIR = Path("outputs/reports")


def save_analysis_json(analysis_data):
    """Save generated analysis JSON to outputs/json."""
    JSON_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_path = JSON_OUTPUT_DIR / f"ux_research_data_{timestamp}.json"

    with open(save_path, "w", encoding="utf-8") as file:
        json.dump(analysis_data, file, ensure_ascii=False, indent=2)

    return save_path


def save_docx_report(docx_file):
    """Save generated docx report to outputs/reports."""
    REPORT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_path = REPORT_OUTPUT_DIR / f"ux_research_report_{timestamp}.docx"

    docx_file.seek(0)
    save_path.write_bytes(docx_file.read())
    docx_file.seek(0)

    return save_path


def list_analysis_history():
    """List saved JSON analysis history from outputs/json."""
    JSON_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    history_files = sorted(
        JSON_OUTPUT_DIR.glob("ux_research_data_*.json"),
        key=lambda path: path.stat().st_mtime,
        reverse=True
    )

    return history_files


def load_analysis_json(file_path):
    """Load a saved analysis JSON file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)