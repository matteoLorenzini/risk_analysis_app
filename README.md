# risk_analysis_app

Sirius Risk Analysis application package for ResearchSpace.  
This repository contains the templates, configuration, and static assets used to browse cultural heritage entities and run risk-analysis workflows (including scale-based scoring, magnitude, and uncertainty views).

## What this project contains

- `data/templates/`: main UI templates (start page, structured search pages, risk-analysis views, insert forms, and utility pages).
- `ldp/configurations/`: LDP resource configuration files.
- `icons/` and `assets/images/icons/`: custom and platform icon assets used by the UI.
- `file/` and `images/`: optional local/static media used by the runtime.
- `.github/workflows/deploy.yml`: deployment workflow that syncs changed runtime files.

## Application scope

The app is built around semantic data in CIDOC CRM-style models and provides:

- Start and landing pages for navigating Sites, Places, Agents, Events, and Site Types.
- Structured search templates for domain entities.
- Risk analysis interfaces with event-level assessment tables and score ranges.
- Insert/edit templates for creating or enriching risk analysis content in ResearchSpace.

## Research scope (project context)

This ResearchSpace app supports cultural heritage Disaster Risk Management (DRM) by turning fragmented assessment records into interoperable semantic data.

The broader project scope is to:

- Harmonize heterogeneous documentation through an ETL workflow (extract, transform, load).
- Apply semantic enrichment with CIDOC-CRM compliant modelling, controlled vocabularies, and project thesauri (risk agents and heritage typologies).
- Enable integration and querying of resulting knowledge graphs in ResearchSpace for cross-dataset exploration and comparison.
- Support event-centric risk representation (assets, hazards, actors, documentary evidence, and quantitative evaluations) for decision-oriented conservation analysis.

The workflow was validated on cultural heritage sites in Ravenna (Italy), showing operational robustness and scalability for territorial-level risk analysis and prioritization.

## Deployment

On push to `main` (or manual workflow dispatch), GitHub Actions runs `.github/workflows/deploy.yml`, which:

1. Checks out this repository.
2. Copies changed files from `data/`, `ldp/`, and optional `file/` + `images/` into the configured ResearchSpace runtime-data directory.
3. Verifies the local service endpoint (`http://localhost:10214/`) is responding.

The workflow is designed for a self-hosted runner with access to the target runtime path.
