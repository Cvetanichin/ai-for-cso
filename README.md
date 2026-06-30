# AI at Work for Civil Society

[![CI — Python Tools](https://github.com/Cvetanichin/ai-for-cso/actions/workflows/python-ci.yml/badge.svg)](https://github.com/Cvetanichin/ai-for-cso/actions/workflows/python-ci.yml)

**By Vaska Cvetanoska (Cvetanichin Consultancy)**
**A self-published AI training track for civil society professionals**

A seven-module specialist AI training track for CSO professionals, delivered through [cvetanichin.org](https://cvetanichin.org) and sold as standalone digital products on [Gumroad](https://cvetanichin.gumroad.com/), plus seven matching AI tools. This repo is the source of truth for course content, templates, and AI tools.

## Project Overview

CSOs across the Western Balkans and broader Europe manage EU-funded grants, design M&E frameworks, write donor reports, and run public outreach — without dedicated AI literacy training built for their workflows. This course closes that gap.

This is one of two product lines under the Cvetanichin brand:

| Line | What it is | Sold via |
|---|---|---|
| **AI at Work for Civil Society** (this repo) | Skills training — course + digital products + free AI tools | cvetanichin.org → Gumroad checkout |
| **Intelligence Workspace** | A standalone CSO project management SaaS (proposal drafting, project tracking, funding/open-call monitoring, M&E analysis) | Its own platform — separate repo, separate pricing |

The two are related but independent: this course teaches the skills; Intelligence Workspace is a separate tool sold to the same audience. See [`/docs/platform-architecture.md`](docs/platform-architecture.md) for how cvetanichin.org connects everything.

## Repo Structure

```
Cvetanichin__ai-for-cso/
├── README.md
├── course-content/          # Course materials (scripts, slides, exercises)
│   └── M1-AI-Foundations/
├── templates/                # Standalone sellable digital products
│   └── M1-AI-Literacy-Starter-Kit/
├── ai-tools/                 # AI scripts/web apps for CSO workflows
│   └── M1-Prompt-Optimizer/
└── marketing/                 # Product page copy, launch assets
    └── M1-Product-Page/
```

| Path | Contains | Example |
|---|---|---|
| `/course-content` | Course materials (scripts, slides, exercises) | `M1-AI-Foundations/scripts/M1-Lesson-1.md` |
| `/templates` | Standalone digital products (sellable) | `M1-AI-Literacy-Starter-Kit/files/AI-Prompt-Design-Cheat-Sheet.md` |
| `/ai-tools` | AI scripts/tools for CSO workflows | `M1-Prompt-Optimizer/prompt_optimizer.py` |
| `/marketing` | Product page copy, launch assets | `M1-Product-Page/M1-Starter-Kit-Product-Description.md` |

## Module Status

| Module | Course Content | Digital Product | AI Tool | Status |
|---|---|---|---|---|
| M1 — AI Foundations for CSO Work | ✅ 3 lessons drafted | ✅ Starter Kit **live on Gumroad** | ✅ Prompt Optimizer **live on Gumroad** + [working demo](https://ai-for-cso.vercel.app/) | **Done** |
| M2 — Grant Proposal Writing with AI | ⬜ | ⬜ | ⬜ | Not started |
| M3 — Monitoring & Evaluation with AI | ⬜ | ⬜ | ⬜ | Not started |
| M4 — Donor Reporting & Compliance | ⬜ | ⬜ | ⬜ | Not started |
| M5 — Fundraising & Donor Research | ⬜ | ⬜ | ⬜ | Not started |
| M6 — OD & Internal Communications | ⬜ | ⬜ | ⬜ | Not started |
| M7 — Media Monitoring & Public Outreach | ⬜ | ⬜ | ⬜ | Not started |

## Products

| Product | Description | Price | Sold via | Status |
|---|---|---|---|---|
| AI Literacy for NGOs: Starter Kit | Quick-start guide + templates for CSO AI usage | €29 | [Gumroad](https://cvetanichin.gumroad.com/l/NGOStarterKit) | **Live** |
| Prompt Optimizer Script + Web App | Customisable script + web app for technical users | €69 | [Gumroad](https://cvetanichin.gumroad.com/l/zqvpon) | **Live** |
| M1: AI Foundations for CSO Work | Full course module (3 lessons) | TBD — pricing pending delivery mechanism | cvetanichin.org | Drafted — delivery platform not yet chosen |

## Quick Start

### Try the M1 Prompt Optimizer live
**[ai-for-cso.vercel.app](https://ai-for-cso.vercel.app/)** — no install required.

### Run it locally instead
```bash
cd ai-tools/M1-Prompt-Optimizer
pip install -r requirements.txt
python app.py
# visit http://localhost:5000
```

### For contributors
1. Create a feature branch: `git checkout -b feature/M2-Grant-Templates`
2. Add content to the relevant module folder.
3. Push and open a PR: `git push origin feature/M2-Grant-Templates`

## Continuous Integration

Every push or PR touching `ai-tools/**/*.py` triggers an automated check ([`.github/workflows/python-ci.yml`](.github/workflows/python-ci.yml)) that:

1. **Auto-discovers** every module under `/ai-tools` that has its own `requirements.txt` — no workflow edits needed when M2–M7 are added.
2. **Lints** each module with flake8 (errors only — undefined names, unused imports, syntax issues; not a style guide).
3. **Verifies every `.py` file imports cleanly** — catches the "looks fine, crashes on import" class of bug.
4. **Boots any `app.py`** found and hits `/` and `/healthz` to confirm the Flask app actually serves.
5. **Smoke-tests any CLI entrypoint** (`argparse` + `def main()`) via `--help`.

If a module fails any check, the PR is blocked from merging into `main`. This is meant to catch breakage before a buyer hits it — not to enforce a style guide.

## Tools Used

- **Claude / Claude Code** — content drafting, script generation, tool building.
- **Flask** — web app layer for AI tools.
- **GitHub** — version control for all course content and products, CI via GitHub Actions.
- **WordPress (cvetanichin.org)** — course/product landing pages, blog.
- **Gumroad** — checkout and digital product delivery.
- **Vercel** — hosting for the [consultancy portfolio](https://project-lf54e.vercel.app/) and the separate [Intelligence Workspace](https://figma-projects-zeta.vercel.app/login) SaaS.

## License

Proprietary — © Cvetanichin Consultancy. Not for redistribution without permission.

## Support

Bugs/feature requests: GitHub Issues on this repo.
Questions: vaska@cvetanichin.org
