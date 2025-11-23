# risk_analysis_app

Repository for the Sirius risk analysis application templates and configuration.

## CI/CD

This repo now uses GitHub-hosted runners (no committed `actions-runner` binaries). A workflow at `.github/workflows/deploy.yml` can optionally build and push a Docker image to GHCR when a `Dockerfile` is present.

### Adding a Dockerfile

If you want the image build to run, add a `Dockerfile` at the repository root. Example minimal placeholder:

```dockerfile
FROM nginx:1.27-alpine
COPY data/templates /usr/share/nginx/html/templates
```

Commit the file; the next push to `main` will build and push `ghcr.io/<OWNER>/risk-analysis-app:<SHA>`.

### Registry Authentication & Permissions

The workflow uses the built-in `GITHUB_TOKEN` for GHCR (packages: write). If you target another registry, add appropriate secrets (`REGISTRY_USERNAME`, `REGISTRY_PASSWORD`) and update the login step.

### Ignore Local Runner Artifacts

If you recreate a local self-hosted runner directory on your machine, ensure it is ignored. Add (or update) `.gitignore` with:

```gitignore
actions-runner/
```

### Manual Dispatch Inputs

You can manually trigger the workflow with:

* `build_image` (true/false) – skip or run image build/push
* `image_tag` – override default SHA tag
* `registry` – change container registry host (default `ghcr.io`)

### Post-Deployment Health (Future)

Health checks from the prior self-hosted workflow were removed. Reintroduce them once a remote deployment target is defined (e.g., SSH to a host, `docker pull` + `docker compose up -d`).

## Next Steps

1. Add a real Dockerfile aligned with ResearchSpace runtime.
2. Introduce deployment job (e.g., `deploy` needs host credentials / environment secrets).
3. Add basic automated tests for SPARQL template integrity (placeholder script).

---

Generated cleanup: removed previously committed self-hosted runner artifacts.
