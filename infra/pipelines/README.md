# Pipelines

CI/CD definitions (GitHub Actions, optional ArgoCD manifests) live here.

## Planned Workflows
- `ci.yml`: lint + test + smoke runner on PRs.
- `deploy-dev.yml`: build+push containers, deploy to Azure Container Apps.
- `deploy-prod.yml`: promote from staging with manual approval + smoke verification.

Store shared action templates + composite actions alongside workflow files for reuse.
