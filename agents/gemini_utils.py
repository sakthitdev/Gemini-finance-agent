import google.generativeai as genai
import json
from tools.graph_utils import create_graph_base64  # updated import


# Gemini setup
genai.configure(api_key="ADD API HERE")
model = genai.GenerativeModel("gemini-2.5-flash")

def get_structured_explanation(topic):
    prompt = f"""
Explain the topic below in a clean hierarchical structure.

{topic}
    Short Description
        - 2–3 simple lines.
    Key Concepts
        - Bullet points.
    How It Works
        - 3–5 bullets.
    Advantages
        - Bullet list.
    Disadvantages
        - Bullet list.
    Real-World Applications
        - 3 examples.
    Example
        - 2 line example.
    Summary
        - 1–2 lines.

Rules:
- Use '-' bullet points only.
- Respect indentation exactly.
- Do not create new sections.
- Do not write long paragraphs.

Topic: {topic}
"""
    output = model.generate_content(prompt).text
    return output.replace("\n", "<br>")

def check_if_graph_required(topic):
    prompt = f"""
Does the topic require a graph for better understanding?

Topic: {topic}

Respond only with:
yes
no
"""
    txt = model.generate_content(prompt).text.strip().lower()
    return txt == "yes"

def generate_graph_json(topic):
    prompt = f"""
Generate STRICT JSON ONLY.

FORMAT:

{{
  "x": [numbers],
  "y": [numbers],
  "xlabel": "string",
  "ylabel": "string",
  "topic": "string"
}}

Topic: "{topic}"

Rules:
- Only JSON.
- No markdown.
- No backticks.
- No explanation.
"""

    for _ in range(3):

        res = model.generate_content(prompt).text.strip()
        cleaned = res.replace("```json", "").replace("```", "").strip()

        try:
            return json.loads(cleaned)
        except:
            continue

    return None

def analyze_topic(topic):
    explanation = get_structured_explanation(topic)
    graph_needed = check_if_graph_required(topic)

    graph_b64 = None

    if graph_needed:
        graph_data = generate_graph_json(topic)

        if graph_data:
            graph_b64 = create_graph_base64(
                graph_data["x"],
                graph_data["y"],
                graph_data["xlabel"],
                graph_data["ylabel"],
                graph_data["topic"]
            )

    return explanation, graph_needed, graph_b64

