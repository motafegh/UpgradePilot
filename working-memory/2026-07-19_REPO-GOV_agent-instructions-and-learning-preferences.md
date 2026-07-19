# Repository Governance — Agent Instructions and Learning Preferences

**Date:** 2026-07-19  
**Step ID:** REPO-GOV  
**Status:** Active  
**Route / milestone:** R2 / M2 — first automated vertical slice

## Authorized objective

Redesign the repository instruction system so `AGENTS.md` contains only stable agent-operating rules, add a project-specific `LEARNING-PREFERENCES.md`, remove duplicated volatile state, and keep repository entry points and memory references consistent.

## Starting state

- `AGENTS.md` said it was stable but contained current route, milestone, next action, and first-session requirements.
- `MEMORY.md` recorded the architecture audit but did not yet reflect the newly approved M2-S01 plan.
- `README.md` had closed the architecture audit but did not route to a learning-preferences file.
- No project-specific `LEARNING-PREFERENCES.md` existed.
- Prior AegisLab, Sentinel, Career, and CyberSecEngineer files contained useful patterns but also project-specific or oversized material that could not be copied blindly.

## Expected output and pass condition

Expected output:

- a durable root `AGENTS.md`;
- a stable UpgradePilot-specific `LEARNING-PREFERENCES.md`;
- approved M2-S01 state and pre-code constraints in `MEMORY.md`;
- corrected routing in `README.md` and `working-memory/README.md`;
- no implementation or architecture adoption.

Pass condition:

- volatile state exists only in state-owning files;
- instruction files have distinct responsibilities and no material conflict;
- current Career snapshot and M2-S01 plan are preserved;
- all links and status statements are consistent;
- `MEMORY.md` remains below 200 lines;
- diff is documentation-only.

## Research and comparison

Consulted:

- OpenAI Codex guidance on `AGENTS.md` scope, nested precedence, validation, and manual review;
- GitHub Copilot guidance on repository-wide and path-specific instructions and avoiding conflicts;
- the open `AGENTS.md` format guidance;
- Anthropic Claude Code project-memory guidance;
- Ali's AegisLab, Sentinel, Career, and CyberSecEngineer instruction files;
- the approved UpgradePilot Learning and Execution Contract;
- the approved `UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md`.

## Design decisions

1. `AGENTS.md` is the single substantive, tool-neutral root agent contract.
2. Current route, milestone, blockers, SHAs, session procedures, and exact next action do not belong in `AGENTS.md`.
3. `LEARNING-PREFERENCES.md` stores Ali-specific teaching refinements without duplicating the canonical contract.
4. `MEMORY.md` stores the current M2-S01 responsibility, restrictions, and pre-code gate.
5. `working-memory/` remains the detailed progressive record system.
6. Future tool-specific files should be thin routing shims unless a real scoped need is demonstrated.
7. Nested `AGENTS.md` files are allowed only for genuinely different subtree conventions.
8. Destructive Git actions, fabricated evidence, silent failure states, and unsupported completion claims are explicitly prohibited.

## Concurrency handling

`main` advanced twice during preparation:

- the architecture audit was closed in README and AGENTS;
- the Career snapshot gained the approved M2-S01 plan.

Direct promotion of the earlier branch was rejected because it was not a fast-forward. The final branch was rebuilt from the latest `main`, preserving all concurrent Career snapshot changes. Temporary M2 requirements were moved from `AGENTS.md` into `MEMORY.md` rather than lost.

## Files changed

- `AGENTS.md`
- `LEARNING-PREFERENCES.md`
- `README.md`
- `MEMORY.md`
- `working-memory/README.md`
- this record

## Assistance and ownership

- Direction and authorization: Ali-directed.
- Research, drafting, integration, and edits: AI-generated / AI-assisted.
- Ali has not yet reviewed every final line or demonstrated practical use of the new instruction system.
- This governance change establishes no implementation capability.

## Pending closure checks

- compare final branch with latest `main`;
- verify documentation-only paths;
- verify no volatile state in `AGENTS.md`;
- verify `MEMORY.md` line limit;
- verify M2-S01 state and exact next action across README, MEMORY, and Career snapshot;
- verify all referenced paths;
- fast-forward `main` without force.
