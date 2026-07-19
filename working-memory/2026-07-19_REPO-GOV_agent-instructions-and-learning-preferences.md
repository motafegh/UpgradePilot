# Repository Governance — Agent Instructions and Learning Preferences

**Date:** 2026-07-19  
**Step ID:** REPO-GOV  
**Status:** Completed  
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

`main` advanced repeatedly during preparation with valid Career snapshot synchronization for M2-S01.

- Earlier direct fast-forward promotion was rejected because `main` had advanced.
- The final branch was rebuilt from the latest known `main`.
- A pull request was used so later snapshot commits could merge without being overwritten.
- GitHub confirmed the PR was mergeable.
- Pull request `#1` merged successfully as `662e1e9e0435ca250ffced31af240891449d908b`.

Temporary M2 requirements were moved from `AGENTS.md` into `MEMORY.md` rather than discarded.

## Files changed

- `AGENTS.md`
- `LEARNING-PREFERENCES.md`
- `README.md`
- `MEMORY.md`
- `working-memory/README.md`
- this record

## Validation

- PR `#1` changed only the six documentation paths listed above.
- No source code, tests, package metadata, executable example, CI, architecture file, or Career snapshot file was changed by this work.
- `AGENTS.md` is 147 content lines and contains no current route, milestone, active blocker, commit SHA, active session procedure, or exact next action.
- `LEARNING-PREFERENCES.md` is explicitly subordinate to the canonical Learning and Execution Contract and stores project-specific refinements only.
- `MEMORY.md` is 132 content lines, below the 200-line hard limit.
- `README.md`, `MEMORY.md`, the Career README snapshot, and the M2-S01 plan agree that M2-S01 is approved and not started.
- The exact next action is to start M2-S01 and pass its five-question pre-code gate before creating source files.
- All referenced instruction, memory, audit, and M2-S01 plan paths exist.

## Assistance and ownership

- Direction and authorization: Ali-directed.
- Research, drafting, integration, and edits: AI-generated / AI-assisted.
- Ali has not yet reviewed every final line or demonstrated practical use of the new instruction system.
- This governance change establishes no implementation capability.

## Result and continuation

**Pass condition:** Passed.

`MEMORY.md` was updated. No canonical tracker update was required by this governance-only change because M2-S01 authorization, capability depth, and technical next action were not changed.

**Exact next authorized action:** Start M2-S01 using its required start message and answer the five pre-code questions before creating any source file.
