# WildAlert Field Intelligence Prototype

A polished, interactive demonstration of a proposed early-warning and decision-support platform for reducing human–wildlife conflict in Botswana.

## Included
- Dashboard KPIs and filters
- Approximate map view of clearly labelled illustrative reports
- Incident intake form
- Review queue and incident register
- CSV export
- Explainable demonstration risk rules

## Important limitations
This is a working software demonstration, not a validated AI system. It does not use a trained model, live wildlife reports, official data feeds, GPS tracking, or real notification delivery. Sample incidents and coordinates are illustrative; map points are approximate district-level demo locations. Risk categories are not probabilities and are not validated against real incidents.

## Run locally
Requires Python 3.10+.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Deployment
The app can be deployed with Streamlit Community Cloud by connecting the GitHub repository and selecting `app.py` as the main file, subject to platform requirements.

## Next steps
- Validate user needs with communities, farmers, wildlife officers, and conservation partners.
- Identify authorised data sources and establish data-governance safeguards.
- Test the workflow and rules with domain experts.
- Build and evaluate a machine-learning model only if suitable data support it.
- Do not send operational alerts until appropriate validation, safety review, and partner approval are complete.
