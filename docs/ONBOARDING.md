# Engineering Onboarding Checklist

1. Install prerequisites
   - Python 3.12+
   - Node.js 20+
   - pnpm 9+
   - uv (https://docs.astral.sh/uv/)
   - Docker Desktop
2. Clone repo and bootstrap tools
   ```bash
   pnpm install
   uv sync
   ```
3. Copy `.env.example` → `.env` (pending Key Vault hookup) and populate API keys (see `api_validation/README` once added).
4. Run the validation smoke suite to verify data provider access:
   ```bash
   python api_validation/run_smoke.py --ws-duration 3
   ```
5. Launch local stack (placeholder until Docker Compose lands).
6. Read `docs/TECHNICAL_SETUP.md` and the PRD to understand architecture + milestones.
