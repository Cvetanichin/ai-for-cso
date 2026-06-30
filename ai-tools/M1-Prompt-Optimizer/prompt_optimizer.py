"""
AI Prompt Optimizer for CSOs
---------------------------------
Optimizes basic prompts for civil society workflows (grant writing, donor
reporting, M&E, stakeholder comms, fundraising research) by adding role,
context, and constraints based on predefined templates.

Usage:
    # CLI Example:
    python prompt_optimizer.py --input "Draft a report" --task "donor_reporting" \
        --ngo_type "human rights" --region "Western Balkans"

    # Programmatic Example:
    from prompt_optimizer import optimize_prompt
    optimized = optimize_prompt(
        input_prompt="Draft a proposal",
        task="grant_writing",
        ngo_type="education",
        region="Albania",
        topic="digital literacy",
        funding_amount="50,000",
    )
    print(optimized)
"""

import argparse
import json
from typing import Dict

# ---------------------------------------------------------------------------
# Predefined prompt templates for CSO tasks
# ---------------------------------------------------------------------------
PROMPT_TEMPLATES: Dict[str, str] = {
    "grant_writing": (
        "You are a **grant writer** for a {ngo_type} NGO working in {region}. "
        "Draft a **{section}** for a **{funding_amount}€ project** on {topic}. "
        "Use **simple language**, avoid jargon, and align with **{donor_name}** priorities. "
        "Base it on this context: {context}. "
        "Keep it under **{word_limit} words**."
    ),
    "donor_reporting": (
        "You are a **project manager** for a {ngo_type} NGO. "
        "Summarize **{num_achievements} key achievements** from our **{time_period} report** "
        "for **{donor_name}**. "
        "Highlight **impact on {target_group}** and use **data from {data_source}**. "
        "Tone: **{tone}**. Length: **{word_limit} words**."
    ),
    "me_analysis": (
        "You are an **M&E specialist** for a {ngo_type} NGO. "
        "Analyze this **{data_type}** (attached: {data_source}) and identify: "
        "**{num_trends} trends**, **{num_gaps} gaps**, and **{num_recommendations} recommendations**. "
        "Focus on **{focus_area}**. Use **bullet points** and **plain language**."
    ),
    "stakeholder_comms": (
        "You are a **communications officer** for a {ngo_type} NGO. "
        "Draft a **{comm_type}** (e.g., email, social post) to **{audience}** about **{topic}**. "
        "Tone: **{tone}**. Length: **{word_limit} words**. "
        "Include: **{key_points}**. "
        "Avoid: **{avoid}**."
    ),
    "fundraising_research": (
        "You are a **fundraising manager** for a {ngo_type} NGO. "
        "Research **{num_donors} potential donors** for a **{topic}** project in **{region}**. "
        "Focus on donors with: **{criteria}**. "
        "Output format: **{output_format}**. "
        "Use these sources: **{sources}**."
    ),
}

# ---------------------------------------------------------------------------
# Default values for placeholders (used when not supplied by the caller)
# ---------------------------------------------------------------------------
DEFAULTS: Dict[str, Dict[str, str]] = {
    "grant_writing": {
        "section": "problem statement",
        "funding_amount": "50,000",
        "topic": "youth employment",
        "donor_name": "EU",
        "word_limit": "200",
        "context": "Our NGO has 10 years of experience in rural development.",
    },
    "donor_reporting": {
        "num_achievements": "3",
        "time_period": "Q2 2024",
        "donor_name": "USAID",
        "target_group": "100+ beneficiaries",
        "data_source": "project database",
        "tone": "professional",
        "word_limit": "150",
    },
    "me_analysis": {
        "data_type": "beneficiary feedback",
        "data_source": "survey responses",
        "num_trends": "2",
        "num_gaps": "1",
        "num_recommendations": "1",
        "focus_area": "project impact",
    },
    "stakeholder_comms": {
        "comm_type": "email",
        "audience": "donor",
        "topic": "project update",
        "tone": "grateful",
        "word_limit": "100",
        "key_points": "impact, next steps, budget status",
        "avoid": "jargon, overly technical terms",
    },
    "fundraising_research": {
        "num_donors": "5",
        "topic": "gender equality",
        "region": "Western Balkans",
        "criteria": "budget > €100K, focus on education, past funding in the region",
        "output_format": "table with columns: Donor, Focus Area, Budget, Contact, Deadline",
        "sources": "EU Grants Portal, Foundation Directory Online",
    },
}


def optimize_prompt(input_prompt: str, task: str, **kwargs) -> str:
    """
    Optimize a basic prompt using a predefined template for the given CSO task.

    Args:
        input_prompt: The user's basic prompt (e.g., "Draft a report"). Kept for
            context/logging; the optimized output is fully template-driven.
        task: The CSO task type (e.g., "grant_writing", "donor_reporting").
        **kwargs: Additional context (e.g., ngo_type="human rights",
            region="North Macedonia"). Anything not supplied falls back to
            DEFAULTS for that task.

    Returns:
        Optimized prompt string with a header line identifying the task.

    Raises:
        ValueError: If the task is unknown or required context is missing
            after merging with defaults.
    """
    if task not in PROMPT_TEMPLATES:
        raise ValueError(
            f"Unknown task: '{task}'. Choose from: {list(PROMPT_TEMPLATES.keys())}"
        )

    # ngo_type and region apply to every template but aren't part of
    # task-specific DEFAULTS, so give them top-level fallbacks here.
    base_context = {"ngo_type": "civil society", "region": "Western Balkans"}
    context = {**base_context, **DEFAULTS.get(task, {}), **kwargs}

    template = PROMPT_TEMPLATES[task]
    try:
        optimized = template.format(**context)
    except KeyError as e:
        missing = str(e).strip("'")
        required = sorted(set(DEFAULTS.get(task, {}).keys()) | {"ngo_type", "region"})
        raise ValueError(
            f"Missing required context for task '{task}': '{missing}'. "
            f"Required fields: {required}"
        )

    return f"--- Optimized Prompt for {task} ---\n{optimized}"


def get_available_tasks() -> str:
    """Return a human-readable, newline-separated list of available tasks."""
    return "\n".join(
        f"- {task}: {PROMPT_TEMPLATES[task].split('.')[0]}" for task in PROMPT_TEMPLATES
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Optimize prompts for CSO workflows (grant writing, donor reporting, etc.)."
    )
    parser.add_argument(
        "--input", type=str, required=True,
        help="Your basic prompt (e.g., 'Draft a report')."
    )
    parser.add_argument(
        "--task", type=str, required=True,
        help=f"CSO task type. Available tasks:\n{get_available_tasks()}"
    )
    parser.add_argument(
        "--ngo_type", type=str, default="civil society",
        help="Type of NGO (e.g., 'human rights', 'education')."
    )
    parser.add_argument(
        "--region", type=str, default="Western Balkans",
        help="Region of operation (e.g., 'North Macedonia', 'Albania')."
    )
    parser.add_argument(
        "--output", type=str, default=None,
        help="Save optimized prompt to a file (e.g., 'optimized_prompt.txt')."
    )
    parser.add_argument(
        "--json", action="store_true",
        help="Output in JSON format (for programmatic use)."
    )

    # Allow arbitrary extra context flags (e.g. --topic, --donor_name) without
    # having to declare every possible placeholder up front.
    args, unknown = parser.parse_known_args()
    extra_context = {}
    key = None
    for tok in unknown:
        if tok.startswith("--"):
            key = tok[2:]
        elif key is not None:
            extra_context[key] = tok
            key = None

    try:
        optimized = optimize_prompt(
            args.input,
            args.task,
            ngo_type=args.ngo_type,
            region=args.region,
            **extra_context,
        )

        if args.json:
            output = {
                "input_prompt": args.input,
                "task": args.task,
                "optimized_prompt": optimized.split("\n", 1)[1],  # strip header
                "context": {"ngo_type": args.ngo_type, "region": args.region, **extra_context},
            }
            optimized = json.dumps(output, indent=2, ensure_ascii=False)

        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(optimized)
            print(f"Optimized prompt saved to {args.output}")

        print(optimized)

    except ValueError as e:
        print(f"Error: {e}")
        print(f"\nAvailable tasks:\n{get_available_tasks()}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
