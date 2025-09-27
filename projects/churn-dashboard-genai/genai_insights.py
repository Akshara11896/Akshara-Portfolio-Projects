# genai_insights.py
# Example function to build a prompt and call an LLM (replace with your library/client)

def build_kpi_prompt(kpi_summary: dict) -> str:
    lines = [f"{k}: {v}" for k, v in kpi_summary.items()]
    prompt = "Please summarise these KPIs for a business stakeholder in 3 short bullets:\n" + "\n".join(lines)
    return prompt

# PSEUDO-code for calling an LLM (do not include API keys in repo)
# response = llm_client.generate(prompt)
# print(response.text)
