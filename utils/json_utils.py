import json
import html
import streamlit as st


def safe_json_loads(text):
    """Safely parse JSON returned by the model."""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        st.error("The model did not return valid JSON. Please run again.")
        st.code(text)
        return None


def html_escape(value):
    """Escape text before rendering it inside custom HTML."""
    if value is None:
        return ""
    return html.escape(str(value))