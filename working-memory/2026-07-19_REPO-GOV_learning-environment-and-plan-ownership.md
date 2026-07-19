# Repository Governance — Learning Environment and Plan Ownership

**Date:** 2026-07-19  
**Step ID:** REPO-GOV  
**Status:** Active  
**Route / milestone:** R2 / M2 — first automated vertical slice

## Objective

Create a simple durable home for learning artifacts, define Career-versus-UpgradePilot planning ownership, and make agent procedure proportional to the size and consequence of the task.

## Starting problem

- Durable learning notes had no dedicated project location.
- A permanent learning branch was being considered even though branches are unsuitable as long-term content categories.
- Detailed technical planning and program-level planning did not have a sufficiently explicit repository boundary.
- Existing agent rules could be interpreted as requiring full working-memory and planning ceremony for small explanations, discussions, or reversible edits.

## Decisions

1. Accepted learning artifacts live on `main` under `learning/`; no permanent learning branch.
2. Short-lived branches isolate unfinished implementation, experiments, or larger session changes.
3. Career owns program-level horizons, capacity, gates, and capability tracking.
4. UpgradePilot owns future detailed technical plans under `plans/`.
5. The current M2-S01 plan remains in Career as a transition artifact and is not moved or duplicated.
6. Agents use the minimum process required by consequence, uncertainty, persistent-state impact, and continuity needs.
7. New folders under `learning/` or `plans/` are created only when a real artifact needs them.

## Expected output

- `learning/README.md`;
- `plans/README.md`;
- proportional-process rules in `AGENTS.md`;
- explicit working-memory create/reuse/skip triggers;
- updated learning-artifact threshold in `LEARNING-PREFERENCES.md`;
- updated README and MEMORY routing;
- synchronized Career README and AGENTS snapshot.

## Stop line

No source code, tests, implementation plan for M2-S01, architecture adoption, route change, or capability claim. The exact M2-S01 next action remains unchanged.

## Assistance and ownership

- Direction and constraints: Ali-directed.
- Design, drafting, and repository edits: AI-generated / AI-assisted.
- Practical ownership will require Ali review and later use of the system.