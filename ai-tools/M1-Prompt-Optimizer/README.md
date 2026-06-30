# M1 Prompt Optimizer for CSOs

**Script + Web App** — optimize prompts for civil society workflows (grant writing, donor reporting, M&E, stakeholder comms, fundraising research) using a tested four-step formula.

**Live:** [ai-for-cso.vercel.app](https://ai-for-cso.vercel.app/) — try it now, no setup required.

## Quick Start

### Option 0 — Use it live (no install)
Visit [ai-for-cso.vercel.app](https://ai-for-cso.vercel.app/) directly.

### Option 1 — Web App, run locally (no coding)
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
curl -X POST https://ai-for-cso.vercel.app/api/optimize \
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

**Live on Vercel:** [ai-for-cso.vercel.app](https://ai-for-cso.vercel.app/)

Deployed via Vercel's native Flask auto-detection — no `vercel.json`, no custom adapter needed. To redeploy or replicate for a future module:

1. Import the GitHub repo at [vercel.com/new](https://vercel.com/new).
2. Set **Root Directory** to the tool's folder (e.g. `ai-tools/M1-Prompt-Optimizer`) **before** the first deploy — changing it after an initial deploy and clicking "Redeploy" does not reliably re-trigger framework detection; delete and re-import if that happens.
3. Confirm **Framework Preset** shows **Flask** (it auto-detects from the module-level `app = Flask(__name__)` in `app.py`).
4. Deploy. A correct build installs `requirements.txt` and takes several seconds — a build that completes in under 100ms with no pip install means Root Directory wasn't applied; check Settings → General → Root Directory.

Other options, untested but standard for a Flask app:
- **PythonAnywhere:** upload files via the web UI or Git, configure a Flask web app in the dashboard.
- **Render / Railway:** connect the GitHub repo, set the start command to `gunicorn app:app` (already in `requirements.txt` and `Procfile`).

## Integration Ideas

- **WordPress (cvetanichin.org):** call [https://ai-for-cso.vercel.app/api/optimize](https://ai-for-cso.vercel.app/api/optimize) from a custom block or plugin so visitors can try it directly on the site.
- **Embedded demo:** iframe [ai-for-cso.vercel.app](https://ai-for-cso.vercel.app/) into a course/product page on cvetanichin.org for a live, no-signup demo during the lesson walkthrough.
- **Gumroad delivery:** the live demo link is now referenced in both M1 product listings.

## Support

Bugs/feature requests: GitHub Issues on this repo.
Questions: vaska@cvetanichin.org

---
*Cvetanichin Consultancy — cvetanichin.org*
