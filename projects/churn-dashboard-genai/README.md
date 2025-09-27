# Customer Churn Dashboard (with GenAI)


## Business problem
Predict customers at high risk of churn and provide stakeholder-ready summaries + sample retention messages.


## Tools
Python (Pandas, scikit-learn), Power BI (dashboard), Generative AI (example integration file `genai_insights.py` — uses a generic LLM call pattern).


## Approach
1. Data cleaning and feature engineering in `churn_model.ipynb`.
2. Train simple models (logistic regression / random forest) and store predictions.
3. Publish visualisations in Power BI (screenshots or `.pbix` file linked in README).
4. Use `genai_insights.py` to:
- Summarise high-level churn drivers.
- Translate model outputs into plain-language recommendations.
- Generate sample personalised retention emails for a small number of customers (synthetic examples).


## Notes on GenAI usage
- The GenAI code included is an example demonstrating prompt structure and how to connect model outputs to plain-language text.
- Do not include real customer PII when using GenAI. Always test on synthetic or anonymised records.
