import json

from config import client, MODEL_NAME


def search_theory_support(analysis_data, output_language="English"):
    project_overview = analysis_data.get("project_overview", {})
    ux_insights = analysis_data.get("ux_insights", {})
    design_directions = analysis_data.get("design_directions", {})

    search_context = {
        "core_problem": project_overview.get("core_problem", ""),
        "pain_points": ux_insights.get("pain_points", []),
        "behavioral_patterns": ux_insights.get("behavioral_patterns", []),
        "design_principles": design_directions.get("design_principles", []),
    }

    prompt = f"""
You are a UX research assistant.

The required output language is: {output_language}.

Based on the UX research analysis below, search the web for credible theories,
research principles, or UX references that can support the design direction.

Prioritize credible sources such as:
- Nielsen Norman Group
- Interaction Design Foundation
- ACM, IEEE, Springer, ScienceDirect, university pages
- Government or institutional usability sources
- Recognized design research publications

Avoid random blogs unless they provide highly relevant practical examples.

Return the result in this structure:

## Theory Support

For each source:
- Source title
- Organization / author if available
- Why it is relevant
- Key idea in simple words
- URL

If the required output language is Simplified Chinese:
- Keep source titles in their original language when appropriate.
- Explain relevance and key ideas in Chinese.
- Use professional but readable UX language.

Research analysis:
{json.dumps(search_context, ensure_ascii=False)}
"""

    response = client.responses.create(
        model=MODEL_NAME,
        tools=[
            {
                "type": "web_search"
            }
        ],
        input=prompt
    )

    return response.output_text