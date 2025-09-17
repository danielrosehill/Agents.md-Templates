# Project Context — Data Science (Python + uv)

This repository represents a data science project (EDA, notebooks, experiments, and light pipelines). When Python is used, always set up and use a virtual environment managed by `uv`.

## Environment

- Virtual env: create and use a `uv` venv for all Python tasks.
  - Create: `uv venv` (optionally specify Python version with `--python 3.11`).
  - Use: either activate `.venv` or prefer `uv run <cmd>` to run inside the env without activation.
- Dependencies: if a `requirements.txt` or `pyproject.toml` exists, install with `uv` before running code.
  - `uv pip install -r requirements.txt`
  - or `uv sync` when using `pyproject.toml` with dependency sections.

## Working Model

- Ask brief clarifying questions when datasets, paths, or objectives are ambiguous.
- Keep notebooks in `notebooks/`, data in `data/` (e.g., `raw/`, `processed/`), and outputs in `outputs/` or `reports/` when applicable.
- Be reproducible: set seeds when relevant; record important package versions.
- Avoid committing large data or generated artifacts unless explicitly requested. Do not commit secrets.

## Typical Tasks

- EDA and visualization, lightweight feature engineering, model baselines, and experiment tracking.
- Script and notebook refactoring into small, reusable modules.
- Environment hygiene: ensure `uv` venv exists and dependencies are installed before executing.

