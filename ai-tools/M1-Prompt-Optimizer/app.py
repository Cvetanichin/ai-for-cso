"""
Flask Web Interface for M1 Prompt Optimizer
--------------------------------------------
A simple web app letting CSO professionals optimize prompts without
touching the command line.
"""

from flask import Flask, render_template, request, jsonify
from prompt_optimizer import optimize_prompt, PROMPT_TEMPLATES, DEFAULTS

app = Flask(__name__)


@app.route("/")
def home():
    """Render the homepage with the prompt optimization form."""
    tasks = list(PROMPT_TEMPLATES.keys())
    return render_template("index.html", tasks=tasks, defaults=DEFAULTS)


@app.route("/optimize", methods=["POST"])
def optimize():
    """Optimize a prompt (from the HTML form) and render the result page."""
    data = request.form
    input_prompt = data.get("input_prompt", "").strip()
    task = data.get("task", "").strip()

    if not input_prompt or not task:
        return render_template(
            "index.html",
            tasks=list(PROMPT_TEMPLATES.keys()),
            defaults=DEFAULTS,
            error="Please enter a prompt and select a task.",
        ), 400

    # Everything else in the form becomes optional context (ngo_type, region, etc.)
    context = {k: v for k, v in data.items() if k not in ("input_prompt", "task", "submit") and v}

    try:
        optimized = optimize_prompt(input_prompt, task, **context)
    except ValueError as e:
        return render_template(
            "index.html",
            tasks=list(PROMPT_TEMPLATES.keys()),
            defaults=DEFAULTS,
            error=str(e),
        ), 400

    return render_template("result.html", optimized=optimized, input_prompt=input_prompt, task=task)


@app.route("/api/optimize", methods=["POST"])
def api_optimize():
    """JSON API endpoint for programmatic use (e.g., WordPress integration)."""
    data = request.get_json(silent=True) or {}
    input_prompt = data.get("input_prompt", "")
    task = data.get("task", "")

    if not input_prompt or not task:
        return jsonify({"error": "input_prompt and task are required."}), 400

    context = {k: v for k, v in data.items() if k not in ("input_prompt", "task")}

    try:
        optimized = optimize_prompt(input_prompt, task, **context)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({
        "input_prompt": input_prompt,
        "task": task,
        "optimized_prompt": optimized.split("\n", 1)[1],  # strip header line
        "context": context,
    })


@app.route("/healthz")
def healthz():
    """Lightweight health check for deployment platforms."""
    return jsonify({"status": "ok", "tasks_loaded": len(PROMPT_TEMPLATES)})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
