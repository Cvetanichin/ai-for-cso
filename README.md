# AI at Work for Civil Society

**By Vaska Cvetanoska (Cvetanichin Consultancy)**
**Phase 1 — AI Training Track for Civil Society Professionals**

A seven-module specialist AI training track for CSO professionals, delivered as a Brainster LMS course plus seven standalone sellable digital products. This repo is the source of truth for course content, templates, and AI tools.

## Project Overview

CSOs across the Western Balkans and broader Europe manage EU-funded grants, design M&E frameworks, write donor reports, and run public outreach — without dedicated AI literacy training built for their workflows. This course closes that gap.

## Repo Structure

```
Cvetanichin__ai-for-cso/
├── README.md
├── course-content/          # Course materials (scripts, slides, exercises) — Brainster LMS
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
| M1 — AI Foundations for CSO Work | ✅ 3 lessons drafted | ✅ Starter Kit drafted | ✅ Prompt Optimizer (CLI + web app) built and tested | **Done** |
| M2 — Grant Proposal Writing with AI | ⬜ | ⬜ | ⬜ | Not started |
| M3 — Monitoring & Evaluation with AI | ⬜ | ⬜ | ⬜ | Not started |
| M4 — Donor Reporting & Compliance | ⬜ | ⬜ | ⬜ | Not started |
| M5 — Fundraising & Donor Research | ⬜ | ⬜ | ⬜ | Not started |
| M6 — OD & Internal Communications | ⬜ | ⬜ | ⬜ | Not started |
| M7 — Media Monitoring & Public Outreach | ⬜ | ⬜ | ⬜ | Not started |

## Products

| Product | Description | Price | Status |
|---|---|---|---|
| AI Literacy for NGOs: Starter Kit | Quick-start guide + templates for CSO AI usage | $29 | Drafted |
| Prompt Optimizer Script + Web App | Customisable script + web app for technical users | $49 | Built, tested |
| M1: AI Foundations for CSO Work | Full course module (3 lessons) | Included in full course | Drafted |

## Quick Start

### Run the M1 Prompt Optimizer locally
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

## Tools Used

- **Claude / Claude Code** — content drafting, script generation, tool building.
- **Flask** — web app layer for AI tools.
- **GitHub** — version control for all course content and products.
- **WordPress (cvetanichin.org)** — digital product sales pages.
- **Brainster LMS** — course delivery and certification.

## License

Proprietary — © Cvetanichin Consultancy. Not for redistribution without permission.

## Support

Bugs/feature requests: GitHub Issues on this repo.
Questions: vaska@cvetanichin.org
