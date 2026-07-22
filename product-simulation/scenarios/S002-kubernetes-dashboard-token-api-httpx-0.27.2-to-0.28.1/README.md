# S002 — HTTPX 0.27.2 → 0.28.1

**Repository:** `Aidan-Wallace/kubernetes-dashboard-token-api`  
**Public event:** PR #20  
**Status:** Complete  
**Manual outcome:** Run targeted checks; merge only if exact-head Python checks pass

## Scenario record

- [`CASE.md`](CASE.md) — complete progressive runtime record, evidence inventory, investigation steps, variants, bounded decision, maintainer report, conceptual machine result, and retrospective.

A separate execution-trace file was not created. `CASE.md` was used as the live progressive primary record and preserves the material state → approach → operation → output → interpretation → outcome → continuation chain.

## Why this case matters

This case materially contrasts with S001:

- direct manifest dependency instead of a transitive lockfile dependency;
- upstream API removal instead of security-advisory interpretation;
- target use through FastAPI/Starlette `TestClient`;
- successful Docker CI that installs/builds but does not run tests;
- a Python workflow that runs the relevant tests but does not trigger for `requirements.txt` changes;
- missing exact dependency-resolution evidence because historical logs expired and FastAPI was unpinned.

## Main finding

A green workflow conclusion cannot receive global decision authority. The system must establish:

1. whether the changed file triggered the relevant workflow;
2. which commands the successful job actually executed;
3. whether those commands exercised the changed dependency path;
4. which exact dependency environment was tested.

For this PR, the public evidence supports likely compatibility but not an unconditional merge recommendation. The smallest sufficient follow-up is to capture resolved versions and run the existing Ruff and pytest checks on the exact PR head.

## Most valuable next contrast

A real dependency-update PR with an actual failing test workflow, where UpgradePilot must distinguish update-caused failure from pre-existing, flaky, environmental, or unrelated failure.
