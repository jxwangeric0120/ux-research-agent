# UX Research Agent

UX Research Agent is an AI-assisted research synthesis tool that transforms raw user research materials into structured UX insights and design deliverables.

It helps designers and researchers analyze interview notes, survey responses, and user feedback, then generate UX artifacts such as affinity maps, user personas, journey maps, service blueprints, theory support, and design directions.

---

## Features

- Paste or upload user research materials
- Generate structured UX insights
- Create affinity maps
- Generate user personas
- Generate user journey maps
- Generate service blueprints
- Search for credible theory support online
- Summarize design directions and recommended features
- Export Word research reports
- Export structured JSON data
- Save and reload previous analysis history
- Support English and Simplified Chinese interface/output

---

## Demo Workflow

```text
User research input
↓
AI structured analysis
↓
UX insights generation
↓
Affinity map / Persona / Journey map / Service blueprint
↓
Theory support search
↓
Design direction summary
↓
Downloadable Word report and JSON data
```

---

## Tech Stack

- Python
- Streamlit
- OpenAI API
- pandas
- python-docx
- python-dotenv

---

## Project Structure

```text
ux-research-agent/
│
├── app.py
├── config.py
├── .env
├── .gitignore
├── requirements.txt
├── README.md
│
├── agents/
│   ├── __init__.py
│   ├── analysis_agent.py
│   └── theory_agent.py
│
├── utils/
│   ├── __init__.py
│   ├── file_utils.py
│   ├── json_utils.py
│   ├── language_utils.py
│   ├── output_utils.py
│   └── doc_generator.py
│
├── ui/
│   ├── __init__.py
│   └── render_tabs.py
│
├── data/
│   ├── sample_inputs/
│   │   └── sample_interview.txt
│   └── uploaded_files/
│       └── .gitkeep
│
└── outputs/
    ├── reports/
    │   └── .gitkeep
    ├── json/
    │   └── .gitkeep
    └── charts/
        └── .gitkeep
```

---

## Folder Responsibilities

### `app.py`

Main Streamlit entry point.

Responsible for:

- Page layout
- Sidebar controls
- File upload
- Language selection
- Output selection
- Main generation workflow
- History loading
- Session state management

---

### `config.py`

Loads environment variables and initializes the OpenAI client.

```python
MODEL_NAME = "gpt-4.1-mini"
```

---

### `agents/`

Contains AI agent logic.

```text
analysis_agent.py
= Generates structured UX research analysis in JSON format

theory_agent.py
= Searches for credible UX theory and research support
```

---

### `utils/`

Contains helper functions.

```text
file_utils.py
= Reads and saves uploaded files

json_utils.py
= Parses JSON and escapes HTML text

language_utils.py
= Handles English / Chinese UI and output language logic

output_utils.py
= Saves generated JSON and Word reports

doc_generator.py
= Generates downloadable Word reports
```

---

### `ui/`

Contains Streamlit rendering components.

```text
render_tabs.py
= Renders Overview, Insights, Affinity Map, Persona, Journey Map, Service Blueprint, Theory Support, Design Directions, and Download tabs
```

---

### `data/`

Stores input-related files.

```text
data/sample_inputs/
= Sample research input for testing

data/uploaded_files/
= User-uploaded files saved locally
```

User-uploaded files are ignored by Git for privacy.

---

### `outputs/`

Stores generated results.

```text
outputs/json/
= Saved structured analysis JSON files

outputs/reports/
= Saved Word research reports

outputs/charts/
= Reserved for future chart/image exports
```

Generated files are ignored by Git for privacy.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ux-research-agent.git
cd ux-research-agent
```

Replace `your-username` with your GitHub username.

---

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

macOS / Linux:

```bash
python3 -m venv venv
```

---

### 3. Activate the Virtual Environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```bat
venv\Scripts\activate.bat
```

macOS / Linux:

```bash
source venv/bin/activate
```

If PowerShell blocks script execution, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again:

```powershell
.\venv\Scripts\Activate.ps1
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Create a `.env` File

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

Do not upload this file to GitHub.

---

### 6. Run the App

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

---

## Usage

### 1. Choose Interface Language

Use the sidebar language selector:

```text
English / 中文
```

If the interface is set to Chinese, the generated output will also be in Chinese.

If the user input contains Chinese, the output will automatically be generated in Simplified Chinese.

---

### 2. Add Research Input

You can either:

- Paste user interview notes directly into the text area
- Upload a `.txt` file

Example input:

```text
I often use second-hand platforms to buy furniture, but I feel unsafe when I need to meet strangers. Sometimes the seller does not reply quickly, and I cannot confirm whether the item is still available. I also worry about scams and fake photos. As an international student, I prefer buying from students from the same school because it feels more trustworthy.
```

---

### 3. Select Outputs

The sidebar allows users to choose which deliverables to generate or display:

- Overview
- Insights
- Affinity Map
- Persona
- Journey Map
- Service Blueprint
- Theory Support
- Design Directions

---

### 4. Generate Report

Click:

```text
Generate UX Research Report
```

The app will generate structured UX research deliverables and display them in tabs.

---

### 5. Download Results

The Download tab provides:

- Word report download
- JSON data download
- Raw JSON preview for debugging

The app also saves generated files locally:

```text
outputs/json/
outputs/reports/
```

---

### 6. Load History

The sidebar History section allows users to reload previous analysis results saved in:

```text
outputs/json/
```

This makes it possible to revisit past analyses without calling the API again.

---

## Language Logic

The app supports English and Simplified Chinese.

Output language follows this logic:

```text
If the user input contains Chinese
→ Output in Simplified Chinese

If the user input is English and UI is set to 中文
→ Output in Simplified Chinese

If the user input is English and UI is set to English
→ Output in English
```

---

## Privacy Notes

The following files are intentionally ignored by Git:

```text
.env
venv/
data/uploaded_files/*
outputs/json/*
outputs/reports/*
outputs/charts/*
__pycache__/
```

This prevents uploading:

- API keys
- Virtual environments
- User-uploaded research data
- Generated reports
- Generated JSON histories
- Python cache files

Before pushing to GitHub, make sure these files are not included:

```text
.env
venv/
outputs/json/*.json
outputs/reports/*.docx
data/uploaded_files/*.txt
```

---

## Recommended `.gitignore`

```gitignore
# Environment variables
.env

# Virtual environment
venv/
.venv/

# Python cache
__pycache__/
*.pyc
*.pyo
*.pyd

# Streamlit secrets
.streamlit/secrets.toml

# User uploaded files
data/uploaded_files/*
!data/uploaded_files/.gitkeep

# Generated outputs
outputs/json/*
!outputs/json/.gitkeep

outputs/reports/*
!outputs/reports/.gitkeep

outputs/charts/*
!outputs/charts/.gitkeep

# OS files
.DS_Store
Thumbs.db

# IDE files
.vscode/
.idea/
```

---

## Sample Input

A sample input file can be stored at:

```text
data/sample_inputs/sample_interview.txt
```

Example:

```text
I often use second-hand platforms to buy furniture, but I feel unsafe when I need to meet strangers. Sometimes the seller does not reply quickly, and I cannot confirm whether the item is still available. I also worry about scams and fake photos. As an international student, I prefer buying from students from the same school because it feels more trustworthy. I also do not want to share my personal phone number or social media account before I know whether the seller is reliable.
```

---

## Current Limitations

- The generated UX artifacts should be reviewed by a human designer or researcher before final use.
- The agent may infer design opportunities from limited data, so users should check whether outputs are sufficiently grounded in the research material.
- Theory support depends on web search availability and API access.
- Historical records currently prioritize saved structured JSON. Theory support may need to be regenerated depending on the workflow.
- Word report formatting is functional but can be further improved for client-facing presentation.

---

## Future Improvements

Potential next steps:

- Export persona, affinity map, journey map, and service blueprint as images
- Add PDF export
- Save theory support together with JSON history
- Add project-level history folders
- Add support for CSV survey responses
- Add support for multiple uploaded files
- Improve Word report visual formatting
- Add authentication for private deployment
- Deploy to Streamlit Community Cloud or another hosting platform

---

## License

This project is for educational and portfolio purposes. Add a license before public or commercial distribution.