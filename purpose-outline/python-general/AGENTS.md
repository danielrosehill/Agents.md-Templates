# Project Context — Python (General)

This repository is a general Python project. Ensure a virtual environment exists, create it with `uv` if missing, keep `requirements.txt` accurate, and then follow the user's instructions.

## Environment

- Virtual env: prefer `uv` to manage the venv and installs.
  - Create: `uv venv` (optionally `--python <version>`).
  - Use: activate `.venv` or run commands via `uv run <cmd>`.
- Dependencies:
  - If `requirements.txt` exists: `uv pip install -r requirements.txt`.
  - When packages are added/removed, update `requirements.txt` to stay accurate.
    - Default policy: freeze exact versions unless the user specifies otherwise (e.g., `uv pip freeze > requirements.txt`).

## Operating Model

- Ask quick clarifying questions if versions, entry points, or expected behaviors are ambiguous.
- Prefer small, incremental changes with brief plans for multi-step work.
- Do not commit secrets; avoid committing large build artifacts unless requested.

## Typical Tasks

- Implement features, fix bugs, run tests, and update docs as requested by the user.
- Keep the environment reproducible and synced with the declared requirements.

