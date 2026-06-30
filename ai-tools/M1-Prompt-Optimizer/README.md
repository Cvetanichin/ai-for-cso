# M1 Prompt Optimizer for CSOs

**Script + Web App** — optimize prompts for civil society workflows (grant writing, donor reporting, M&E, stakeholder comms, fundraising research) using a tested four-step formula.

## Quick Start

### Option 1 — Web App (no coding)
```bash
pip install -r requirements.txt
python app.py
```
Open `http://localhost:5000`, enter your prompt, pick a task, click "Optimize Prompt."

### Option 2 — CLI (for developers)
```bash
python prompt_optimizer.py --input "Draft a report" --task "donor_reporting" --ngo_type "health" --region "North Macedonia"
```

### Option 3 — API (for integration, e.g. WordPress)
```bash
curl -X POST http://localhost:5000/api/optimize \
  -H "Content-Type: application/json" \
  -d '{"input_prompt": "Draft a proposal", "task": "grant_writing", "ngo_type": "education"}'
```

## Features

| Feature | Description |
|---|---|
| Web interface | Form-based UI for non-technical users |
| CLI tool | Optimize prompts from the command line, with `--json` and `--output` flags |
| API endpoint | `/api/optimize` — integrate with WordPress, Gumroad product pages, or other platforms |
| 5 CSO task templates | grant_writing, donor_reporting, me_analysis, stakeholder_comms, fundraising_research |
| Sensible defaults | Works out of the box; override any field via form, CLI flag, or API payload |
| Copy to clipboard | One-click copy on the results page |

## Files

| File | Purpose |
|---|---|
| `prompt_optimizer.py` | Core logic — templates, defaults, optimize_prompt(), CLI |
| `app.py` | Flask web app and JSON API |
| `requirements.txt` | Dependencies (Flask) |
| `templates/index.html` | Web app homepage |
| `templates/result.html` | Results page |
| `static/style.css` | Styling |

## Adding a New Task Template

Edit `PROMPT_TEMPLATES` and `DEFAULTS` in `prompt_optimizer.py`:

```python
PROMPT_TEMPLATES["budget_narrative"] = (
    "You are a finance officer for a {ngo_type} NGO. "
    "Draft a budget narrative for a {funding_amount}€ project on {topic}. "
    "Explain {num_line_items} line items in plain language. "
    "Align with {donor_name} requirements."
)

DEFAULTS["budget_narrative"] = {
    "num_line_items": "5",
    "funding_amount": "50,000",
    "topic": "education",
    "donor_name": "EU",
}
```

Restart the app and the new task appears automatically in the dropdown — no other code changes needed.

## Deployment

- **Vercel:** `npm install -g vercel && vercel` (use a Python/Flask adapter, e.g. `vercel-python`, or deploy as a serverless function).
- **PythonAnywhere:** upload files via the web UI or Git, configure a Flask web app in the dashboard.
- **Render / Railway:** connect the GitHub repo, set the start command to `gunicorn app:app`, and add `gunicorn` to `requirements.txt` for production use (the Flask dev server is not production-safe).

## Integration Ideas

- **WordPress (cvetanichin.org):** call `/api/optimize` from a custom block or plugin so visitors can try it directly on the site.
- **Embedded demo:** iframe the deployed web app into a course/product page on cvetanichin.org for a live, no-signup demo during the lesson walkthrough.
- **Gumroad delivery:** link to the deployed app URL as a bonus resource in the Starter Kit and Prompt Optimizer product files.

## Support

Bugs/feature requests: GitHub Issues on this repo.
Questions: vaska@cvetanichin.org

---
*Cvetanichin Consultancy — cvetanichin.org*
