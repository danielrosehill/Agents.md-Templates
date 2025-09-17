# Project Context — Website (Astro + Contentful + Netlify)

This repository is a website built with Astro, using Contentful as the headless CMS backend and deployed on Netlify.

## Environment & Tooling

- Node & package manager: respect the repo's lockfile (`pnpm-lock.yaml`, `yarn.lock`, or `package-lock.json`) when installing.
- Local setup:
  - Install deps: `pnpm install` / `yarn install` / `npm install` (match lockfile).
  - Dev server: `pnpm dev` / `yarn dev` / `npm run dev`.
  - Build: `pnpm build` / `yarn build` / `npm run build`.
- Contentful configuration:
  - Expect env vars: `CONTENTFUL_SPACE_ID`, `CONTENTFUL_ACCESS_TOKEN` (and/or preview token if used).
  - Do not commit secrets. Use `.env` locally and Netlify environment variables in production.
- Netlify deployment:
  - Respect `netlify.toml` if present; otherwise default build command is Astro's build and publish directory typically `dist/`.
  - Do not change deployment settings unless the user requests it.

## Operating Model

- Ask brief clarifying questions if content models, space IDs, or integration points are ambiguous.
- Keep Contentful queries/types aligned with the existing content model; avoid breaking field names or types.
- Prefer small, incremental changes; provide a short plan before multi-step changes.
- Avoid committing large generated assets or secrets.

## Typical Tasks

- Implement Astro components/pages, style updates, performance tweaks.
- Add or adjust Contentful queries, types, and mapping logic while preserving existing data shapes.
- Verify builds locally; ensure Netlify config and env vars are compatible with changes.

