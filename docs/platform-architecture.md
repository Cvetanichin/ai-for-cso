# Platform Architecture

How cvetanichin.org, Gumroad, and Intelligence Workspace fit together — and what's still undecided.

## Current state (as of M1)

| Property | URL | Status |
|---|---|---|
| Consultancy portfolio | [project-lf54e.vercel.app](https://project-lf54e.vercel.app/) | Deployed |
| Intelligence Workspace (SaaS prototype) | [figma-projects-zeta.vercel.app](https://figma-projects-zeta.vercel.app/login) | Deployed, has a login screen |
| cvetanichin.org | WordPress, Astra theme | Fresh install — unconfigured, no branding applied yet |
| Gumroad | [cvetanichin.gumroad.com](https://cvetanichin.gumroad.com/) | 2 products live: [Starter Kit](https://cvetanichin.gumroad.com/l/NGOStarterKit) (€29), [Prompt Optimizer](https://cvetanichin.gumroad.com/l/zqvpon) (€69) |

## The two product lines

This repo (`ai-for-cso`) covers **one** of two separate revenue lines under the Cvetanichin brand. They are related but should not be conflated in pricing, roadmap, or positioning.

### Line 1 — AI at Work for Civil Society (this repo)
Skills training for individual CSO professionals: course + standalone digital products (Starter Kit, Prompt Optimizer) + free-to-try AI tools per module.

- **Audience:** individual grant writers, M&E specialists, project managers, NGO leaders.
- **Sold via:** cvetanichin.org (landing/sales pages) → Gumroad (checkout, delivery).
- **Build pattern per module:** course scripts + sellable template product + AI tool, all in this repo.

### Line 2 — Intelligence Workspace
A standalone CSO project management SaaS — proposal drafting, client/project progress tracking, funding opportunity and open-call monitoring, M&E data analysis and reporting, eventually an embedded LMS.

- **Audience:** CSOs and consultants who want an operating system for their project work, not just AI skills training.
- **Sold via:** its own platform (currently the Vercel prototype at figma-projects-zeta.vercel.app), independent of Gumroad.
- **Relationship to this repo:** none directly at the code level. Conceptually, it's the productized version of the workflows this course teaches.

## cvetanichin.org's job

cvetanichin.org is the connective hub across both lines, with two phases:

**Phase A — now (sales/landing layer)**
- Course and product landing pages.
- Blog.
- Routes traffic out to Gumroad for checkout (Line 1) and to Intelligence Workspace for SaaS signup (Line 2).
- No embedded LMS, no custom checkout, no client portal yet.

**Phase B — later (ambitious practice OS)**
Vas's own internal practice tool, separate from both product lines above: draft proposals, track client project progress, monitor funding opportunities and open calls, run M&E data analysis and reporting, eventually an embedded LMS for delivering the course directly rather than through Gumroad.

## Open tension — flagged, not yet resolved

Phase B's feature list (proposal drafting, project tracking, funding monitoring, M&E analysis) is functionally close to Intelligence Workspace's feature list. Two ways this could resolve, and it doesn't need deciding now:

1. **Build them separately** — Phase B stays a lightweight internal tool (e.g. Notion + cvetanichin.org), Intelligence Workspace stays the sellable SaaS, no shared code.
2. **Collapse into one** — Vas eventually just uses Intelligence Workspace as her own practice tool (perhaps on a free/internal tier), and Phase B as a separate build is dropped.

Revisit this once Intelligence Workspace's feature set is further along — premature to commit either way while it's still a login-screen prototype.

## What this means for `ai-for-cso` going forward

- Course/product copy in this repo should reference **cvetanichin.org + Gumroad** as the real delivery mechanism, not a third-party LMS.
- Don't reference Intelligence Workspace as part of *this* product's bundle/upsell unless a deliberate cross-sell decision is made later — keep the lines distinct in marketing copy until that's confirmed.
- Pricing for the course module itself (M1: AI Foundations) is **not yet finalised** — the original $199/$299 figures were priced against Brainster's LMS/certification value, which no longer applies. Needs a fresh pricing pass once the delivery mechanism (Gumroad-hosted video vs. something else) is chosen.
