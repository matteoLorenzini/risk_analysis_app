# ResearchSpace Runtime Data (risk_analysis_app)

This folder contains the ResearchSpace runtime data for the Risk Analysis app: UI templates, configuration, images, and LDP resources.

## How to use locally (Docker Desktop)

- Ensure the `researchspace/runtime-data` folder in your Docker setup points to this directory.
- Start the stack:
	- In the repo root: `docker compose up -d` (already configured by researchspace-docker-desktop).
- Open ResearchSpace: <http://127.0.0.1:10214/login> (admin/admin).

## Git workflow

This folder is a Git repository (pushed to <https://github.com/matteoLorenzini/risk_analysis_app>).

- Save changes:
	1. Edit templates/config files here.
	2. Commit and push:
		 - `git add -A`
		 - `git commit -m "feat: your change"`
		 - `git push`

- Pull new versions from GitHub:
	- `git pull` (restart the app if templates/config changed and hot-reload doesn’t pick up changes).

## Contents

- `config/*.prop` – ResearchSpace configuration overrides (homepage, namespaces, etc.)
- `data/templates/*` – HTML templates and UI views (structured search, risk analysis, tornado graph, etc.)
- `images/` – Static images used by the UI
- `ldp/` – LDP resource configurations
- `.gitignore` – Excludes ephemeral runtime artifacts

## Deployment options

- Docker bind-mount (current setup): this folder is mounted into the ResearchSpace container, so edits appear immediately.
- Git-based promotion: push changes to `main` and pull on target environments (e.g., a server) into the same `runtime-data` path.

If you want a packaged "App" for installation via the Apps mechanism, we can add a lightweight app descriptor and bundle instructions next.
