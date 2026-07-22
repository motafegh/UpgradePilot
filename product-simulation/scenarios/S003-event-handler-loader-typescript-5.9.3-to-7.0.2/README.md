# S003 — event-handler-loader: TypeScript 5.9.3 → 7.0.2

> **Execution status:** Attribution investigated; decision/report construction active.  
> **Artifact-lifecycle status:** Prospective checkpoints 1–3 committed.  
> **Factual review:** Pending.  
> **Ali review:** Pending.  
> **External/behavioral confirmation:** Public CI and source comparison support update-caused attribution; residual limits preserved.

## Frozen case

- Repository: `xayanide/event-handler-loader`
- Pull request: `#341`
- Base SHA: `05df3f80631ec061ee2d55307b7492d200c03faf`
- Proposed head SHA: `f6d6daba48567457018bf6cc171f235d4dda4ef2`
- Observed PR merge ref: `f019e9b25a1476f393a3ecf525871f6990017cb8`
- Dependency: `typescript`
- Transition: `5.9.3` → `7.0.2`
- Run: `s003-20260722T201756Z-r1`

## Current result

The selected PR fails during `npm ci` before ESLint. The proposed root TypeScript `7.0.2` is outside the unchanged `typescript-eslint` 8.65.0 peer range `>=4.8.4 <6.1.0`. An adjacent dependency PR from the exact same base passes `npm ci` and ESLint under a near-comparable environment.

> **Current attribution:** `update_caused` at the dependency-tree/installability layer, strongly supported with explicit limits.

Pending work: decision, reports, follow-up, validation, cross-case synthesis and Ali review.

No target repository mutation or rerun has been performed.
