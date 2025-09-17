# Project Context — Resource List Repository

This repository curates links and references on a specific topic. The primary artifact is a `README.md` organized into sections. The user provides resource items and sectioning guidelines; your job is to create the repo from scratch (if missing) or update an existing one in a clean, consistent, and reproducible way.

## Inputs You Expect

- Topic scope: the focus of the resource list and any exclusions.
- Section guidelines: desired section names, ordering, and grouping rules; any required subsections.
- Resource items: title, URL, optional 1–2 line description, and optional tags.
- Style preferences: naming, tone, sorting (alpha/date/popularity), badges, license, and contribution rules.

## Operating Model

- Propose a short plan before large edits; summarize changes after.
- Prefer non-destructive, incremental updates; keep diffs easy to review.
- Idempotent behavior: re-running your process should keep formatting stable (sorting, spacing, headings).
- Validate links and flag dead or redirected links; suggest replacements when possible.

## Repository Layout

- `README.md`: the curated list and project overview (single source of truth).
- `CONTRIBUTING.md` (optional): how to add resources and formatting rules.
- `.github/workflows/link-check.yml` (optional): CI for link checking.
- `LICENSE` (recommended): as provided or requested by the user.

## README Structure (Suggested)

1. Title and short overview paragraph (what the list covers, who it’s for).
2. Badges (optional): license, CI status, link-checker.
3. Table of Contents (optional but recommended for long lists).
4. Sections (as per guidelines), each with concise descriptions.
5. Contribution guidelines link and style summary.
6. License and acknowledgments.

## Entry Format Rules

- One bullet per resource: `- [Title](URL) — short description (≤ 140 chars).`
- Keep titles human-friendly; don’t duplicate site names unless ambiguous.
- Prefer the canonical URL; follow one redirect to normalize.
- Sorting: alphabetical by title within each section unless user requests otherwise.
- Deduplicate by URL (case-insensitive) and title; consolidate duplicates.
- Use tags sparingly; prefer section placement over tag sprawl.
- If a resource has a notable status (archived, paywalled), note it succinctly.

## Section Design

- Use the provided section list and order. If unspecified, propose common groupings such as: Getting Started, Tutorials, Articles, Videos, Tools, Libraries, Datasets, Papers, Community.
- Keep section intros to one sentence where helpful.
- Create subsections only when a section exceeds ~20 items.

## Creating From Scratch

1. Initialize minimal structure with the sections above (or user-provided ones).
2. Ingest the provided resource list; normalize entries; sort per rules.
3. Generate a simple ToC if the file is long; avoid heavy tooling.
4. Add contribution and license sections if specified.

## Updating Existing Repos

1. Parse current `README.md`; preserve existing sections and ordering.
2. Normalize existing entries to the Entry Format Rules (without changing meaning).
3. Merge new resources; dedupe; sort; keep changes minimal and well-scoped.
4. Validate links; update obvious redirects; mark or move dead links to a small "Archive" subsection if requested.

## Safety & Review

- Do not remove sections or large blocks without explicit approval.
- Avoid promotional or spammy additions; prefer authoritative, educational, or widely-used resources.
- Call out potential licensing or access issues (paywalls, TOS restrictions).
- When guidelines conflict (e.g., sorting vs. grouping), confirm preference with the user.

## Automation (Optional)

- Add a lightweight link-check workflow (e.g., weekly) when desired by the user.
- Provide a small script to validate entry format and detect duplicates as the list grows.

