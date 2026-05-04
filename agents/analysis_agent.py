from config import client, MODEL_NAME
from utils.json_utils import safe_json_loads


def analyze_ux_research(research_text, output_language="English"):
    prompt = f"""
You are a senior UX researcher, service designer, and product strategist.

The required output language is: {output_language}.

Analyze the following user research material and return ONLY valid JSON.
Do not use markdown.
Do not include explanations outside JSON.
Do not invent user data. If something is not directly supported by the research text, keep it conservative and label it as an inference.
Use professional UX language, but keep the content understandable for product designers and stakeholders.

Your analysis should not only summarize the data. It should explain:
- what users are experiencing
- why it matters
- what design implication it creates
- what evidence supports the insight

The JSON must follow this structure exactly:

{{
  "project_overview": {{
    "research_context": "",
    "main_user_group": "",
    "core_problem": "",
    "research_limitations": ""
  }},
  "ux_insights": {{
    "pain_points": [
      {{
        "title": "",
        "what_happens": "",
        "why_it_matters": "",
        "design_implication": "",
        "supporting_quote_or_evidence": ""
      }}
    ],
    "behavioral_patterns": [
      {{
        "title": "",
        "observed_behavior": "",
        "interpretation": "",
        "design_implication": "",
        "supporting_quote_or_evidence": ""
      }}
    ],
    "emotional_needs": [
      {{
        "title": "",
        "emotional_signal": "",
        "underlying_need": "",
        "design_implication": "",
        "supporting_quote_or_evidence": ""
      }}
    ]
  }},
  "affinity_map": [
    {{
      "theme": "",
      "theme_summary": "",
      "insights": ["", "", ""],
      "evidence": ["", ""],
      "design_opportunity": ""
    }}
  ],
  "user_persona": {{
    "name": "",
    "role": "",
    "background": "",
    "primary_goal": "",
    "goals": ["", ""],
    "frustrations": ["", ""],
    "behaviors": ["", ""],
    "needs": ["", ""],
    "trust_barriers": ["", ""],
    "quote": ""
  }},
  "user_journey_map": [
    {{
      "stage": "",
      "user_goal": "",
      "user_actions": "",
      "thoughts": "",
      "emotions": "",
      "pain_points": "",
      "opportunities": "",
      "possible_feature_response": ""
    }}
  ],
  "service_blueprint": [
    {{
      "stage": "",
      "user_actions": "",
      "frontstage_touchpoints": "",
      "backstage_processes": "",
      "support_systems": "",
      "pain_points": "",
      "opportunities": "",
      "design_requirement": ""
    }}
  ],
  "design_directions": {{
    "problem_statement": "",
    "design_principles": ["", "", ""],
    "opportunity_areas": [
      {{
        "title": "",
        "description": "",
        "why_it_matters": ""
      }}
    ],
    "recommended_features": [
      {{
        "feature": "",
        "user_problem_addressed": "",
        "reason": "",
        "priority": "High / Medium / Low"
      }}
    ],
    "final_direction_summary": "",
    "next_research_questions": ["", "", ""]
  }}
}}

Rules for output quality:
- Write all JSON values in {output_language}.
- If output_language is Simplified Chinese, use natural and professional Chinese UX terminology.
- If output_language is English, use clear and professional English UX terminology.
- Pain points should be specific, not generic.
- Persona should be grounded in the input, not fictionalized too much.
- Journey map should include 4 to 6 stages.
- Service blueprint should match the journey stages.
- Recommended features should be concrete and actionable.
- Design principles should be strategic, not generic.
- If the input is too short, still generate a useful structure, but clearly mention limitations in "research_limitations".

User research material:
{research_text}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "You are a senior UX researcher. Return only valid JSON."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_format={"type": "json_object"}
    )

    result_text = response.choices[0].message.content
    return safe_json_loads(result_text)