# Agents.md Templates

[![OpenAI Codex](https://img.shields.io/badge/OpenAI-Codex-412991?logo=openai&logoColor=white)](https://openai.com)

This repository contains a collection of `AGENTS.md` templates following the standard suggested by OpenAI for providing rules and context to AI agent codecs. These templates serve as a foundational seeding system for new repositories.

## Purpose

The goal of this repository is to:

1. **Centralize agent rules**: Gather together standardized `AGENTS.md` templates for different project types
2. **Enable quick project setup**: Provide a seeding system where you can select an appropriate template and inject it into a new repository
3. **Maintain consistency**: Ensure consistent agent behavior across different projects by using proven rule sets
4. **Scale over time**: Continuously add new templates as different project patterns emerge

## Template Index

<!-- TEMPLATE_INDEX_START -->

| Template | Directory | Description |
|----------|-----------|-------------|
| Project Context | [`project-type/ha-dashboard/`](./project-type/ha-dashboard/) | The purpose of this repository is iterating upon a Home Assistant Dashboard. |
| Project Context — Resource List Repository | [`project-type/resource-list/`](./project-type/resource-list/) | This repository curates links and references on a specific topic. The primary artifact is a `README.md` organized into sections. The user provides resource items and sectioning guidelines; your job is to create the repo from scratch (if missing) or update an existing one in a clean, consistent, and reproducible way. |
| Project Context — Data Science (Python + uv) | [`purpose-outline/data-science-python/`](./purpose-outline/data-science-python/) | This repository represents a data science project (EDA, notebooks, experiments, and light pipelines). When Python is used, always set up and use a virtual environment managed by `uv`. |
| Project Context — Python (General) | [`purpose-outline/python-general/`](./purpose-outline/python-general/) | This repository is a general Python project. Ensure a virtual environment exists, create it with `uv` if missing, keep `requirements.txt` accurate, and then follow the user's instructions. |
| Project Context — Astro | [`stack-context/astro/`](./stack-context/astro/) | This repository is an Astro project. Use the standard Astro workflow and follow the user's instructions for changes. |
| Project Context — Website (Astro + Contentful + Netlify) | [`stack-context/astro-and-netlify/`](./stack-context/astro-and-netlify/) | This repository is a website built with Astro, using Contentful as the headless CMS backend and deployed on Netlify. |
| System Administration Agent — OPNsense Firewall | [`sysadmin/opnsense/`](./sysadmin/opnsense/) | - Assist with firewall and system administration on an OPNsense appliance. |
| System Administration Agent — Desktop (Ubuntu 25.05) | [`sysadmin/ubuntu-desktop/`](./sysadmin/ubuntu-desktop/) | - Assist the user with day-to-day system administration on a personal desktop running Ubuntu 25.05. |
| System Administration Agent — Ubuntu VM (Proxmox Guest) | [`sysadmin/ubuntu-vm/`](./sysadmin/ubuntu-vm/) | - Assist with system administration inside an Ubuntu virtual machine running as a Proxmox VE guest. |

<!-- TEMPLATE_INDEX_END -->
## Template Structure

Each template directory contains:
- `AGENTS.md` - The main agent rules and context file
- Any additional supporting files specific to that project type

## Codex CLI

- Project: https://github.com/openai/codex
