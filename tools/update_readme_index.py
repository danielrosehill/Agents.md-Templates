#!/usr/bin/env python3
import os
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
README_PATH = REPO_ROOT / "README.md"

MARKER_START = "<!-- TEMPLATE_INDEX_START -->"
MARKER_END = "<!-- TEMPLATE_INDEX_END -->"


def find_templates(root: Path) -> list[tuple[str, Path]]:
    """Find all directories containing an AGENTS.md and return (title, dirpath)."""
    entries: list[tuple[str, Path]] = []
    for agents_path in root.rglob("AGENTS.md"):
        # Skip anything in hidden directories like .git
        if any(part.startswith(".") for part in agents_path.parts):
            continue
        title, _ = parse_agents_md(agents_path)
        if title:
            entries.append((title, agents_path.parent.relative_to(root)))
    # Sort deterministically by directory path
    entries.sort(key=lambda t: str(t[1]))
    return entries


def parse_agents_md(path: Path) -> tuple[str, str]:
    """Return (title, description) from an AGENTS.md file.

    - title: first level-1 heading line (e.g., starting with '# ')
    - description: first non-empty, non-heading paragraph line after the title
    """
    title = ""
    description = ""
    lines = path.read_text(encoding="utf-8").splitlines()

    # Find first H1
    idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith("# "):
            title = line.strip().lstrip("# ").strip()
            idx = i + 1
            break
    if idx is None:
        return title, description

    # Find first non-empty, non-heading line as description
    for j in range(idx, len(lines)):
        s = lines[j].strip()
        if not s:
            continue
        if s.startswith("#"):
            # skip headings
            continue
        description = s
        break
    return title, description


def generate_table(rows: list[tuple[str, Path, str]]) -> str:
    """Generate Markdown table from (title, path, description)."""
    header = "| Template | Directory | Description |\n|----------|-----------|-------------|"
    body_lines = []
    for title, path, desc in rows:
        dir_link = f"[`{path}/`](./{path}/)"
        safe_desc = desc if desc else ""
        body_lines.append(f"| {title} | {dir_link} | {safe_desc} |")
    return "\n".join([header, *body_lines])


def inject_table_into_readme(readme_path: Path, table_md: str) -> None:
    """Replace or insert the template index table in README between markers.

    - If markers exist, replace content between them.
    - Else, locate "## Template Index" section and replace its body with markers + table.
    - If section not found, append a new section at the end.
    """
    content = readme_path.read_text(encoding="utf-8")

    if MARKER_START in content and MARKER_END in content:
        new_content = re.sub(
            rf"{re.escape(MARKER_START)}[\s\S]*?{re.escape(MARKER_END)}",
            f"{MARKER_START}\n\n{table_md}\n\n{MARKER_END}",
            content,
            flags=re.MULTILINE,
        )
        readme_path.write_text(new_content, encoding="utf-8")
        return

    # Try to find existing "## Template Index" section
    lines = content.splitlines()
    out: list[str] = []
    i = 0
    found_header = False
    while i < len(lines):
        line = lines[i]
        out.append(line)
        if not found_header and line.strip().lower() == "## template index":
            found_header = True
            # Skip existing lines until next top-level section (## ) or end
            i += 1
            # Collect and skip until next '## ' at column 0
            while i < len(lines) and not re.match(r"^## ", lines[i]):
                i += 1
            # Insert markers + new table before processing the next section header
            out.append("")
            out.append(MARKER_START)
            out.append("")
            out.extend(table_md.splitlines())
            out.append("")
            out.append(MARKER_END)
            # Continue without incrementing i here to process the next section header normally
            continue
        i += 1

    if found_header:
        readme_path.write_text("\n".join(out) + "\n", encoding="utf-8")
        return

    # Append new section at end
    appended = (
        content.rstrip()
        + "\n\n## Template Index\n\n"
        + MARKER_START
        + "\n\n"
        + table_md
        + "\n\n"
        + MARKER_END
        + "\n"
    )
    readme_path.write_text(appended, encoding="utf-8")


def main() -> None:
    entries = find_templates(REPO_ROOT)
    detailed_rows: list[tuple[str, Path, str]] = []
    for title, rel_dir in entries:
        desc = ""
        agents_md = REPO_ROOT / rel_dir / "AGENTS.md"
        _, desc = parse_agents_md(agents_md)
        detailed_rows.append((title, rel_dir, desc))

    table_md = generate_table(detailed_rows)
    inject_table_into_readme(README_PATH, table_md)
    print(f"Updated {README_PATH} with {len(detailed_rows)} templates.")


if __name__ == "__main__":
    main()

