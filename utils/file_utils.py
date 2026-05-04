from pathlib import Path
from datetime import datetime


UPLOAD_DIR = Path("data/uploaded_files")


def read_uploaded_file(uploaded_file):
    """Read uploaded txt file."""
    if uploaded_file is None:
        return ""

    try:
        return uploaded_file.read().decode("utf-8")
    except UnicodeDecodeError:
        uploaded_file.seek(0)
        return uploaded_file.read().decode("latin-1")


def save_uploaded_file(uploaded_file):
    """Save uploaded file to data/uploaded_files."""
    if uploaded_file is None:
        return None

    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = uploaded_file.name.replace(" ", "_")
    save_path = UPLOAD_DIR / f"{timestamp}_{safe_name}"

    uploaded_file.seek(0)
    save_path.write_bytes(uploaded_file.read())
    uploaded_file.seek(0)

    return save_path