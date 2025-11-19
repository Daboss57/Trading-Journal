# Frontend App (Next.js)

This package hosts the trading journal UI described in the wireframes. It ships as a Next.js 15 app using the `app/` router so we can mix SSR + client components.

## Quickstart

```bash
pnpm install
pnpm dev --filter @trading-journal/frontend
```

## Next Steps
- Wire Clerk/NextAuth for authentication.
- Add shared component library + charting primitives.
- Integrate GraphQL/REST clients pointed at the FastAPI gateway.
