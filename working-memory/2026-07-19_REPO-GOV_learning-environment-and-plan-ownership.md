# Repository Governance — Learning Environment and Plan Ownership

**Date:** 2026-07-19  
**Step ID:** REPO-GOV  
**Status:** Completed  
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
8. Learning-note creation thresholds live in `learning/README.md` and are referenced by `AGENTS.md`; they are not duplicated into `LEARNING-PREFERENCES.md`.

## Files changed

### Career

- `AGENTS.md`
- `README.md`

Career merge commit: `da884f7669ed8abc737c9315ca682eed021060b0`.

### UpgradePilot

- `AGENTS.md`
- `MEMORY.md`
- `README.md`
- `learning/README.md`
- `plans/README.md`
- `working-memory/README.md`
- this record
- `docs/program/SOURCE.md`
- `docs/program/career/AGENTS.md`
- `docs/program/career/README.md`

## Validation

- Change set is documentation and governance only.
- No source code, tests, package metadata, executable examples, CI, architecture adoption, or M2-S01 implementation plan was created.
- `AGENTS.md` contains explicit lightweight, bounded, formal, and high-consequence thresholds.
- `AGENTS.md` directs agents not to scan all historical working-memory files.
- `working-memory/README.md` defines create, reuse, and skip conditions and prohibits one record per concept, command, or chat.
- `learning/README.md` defines durable-note thresholds and rejects a permanent learning branch.
- `plans/README.md` defines Career-versus-UpgradePilot ownership and preserves M2-S01 as the transition artifact.
- Only the root guide exists under each new area; no empty hierarchy was created.
- `AGENTS.md` is 175 content lines.
- `MEMORY.md` is 140 content lines, below the 200-line limit.
- Mirrored Career `AGENTS.md` and `README.md` have the same content SHAs as canonical Career.
- Snapshot provenance points to Career commit `da884f7669ed8abc737c9315ca682eed021060b0`.
- README, MEMORY, Career controls, and the M2-S01 plan still agree that M2-S01 is approved but not started.
- Exact technical next action remains unchanged.

## Assistance and ownership

- Direction and constraints: Ali-directed.
- Design, drafting, integration, and repository edits: AI-generated / AI-assisted.
- Ali has not yet reviewed every final line or demonstrated practical use of the new structure.
- This governance change establishes no implementation capability.

## Result

**Pass condition:** Passed.

The repository now separates durable learning, detailed technical planning, current state, and working history without requiring formal ceremony for lightweight interactions.

## Exact next authorized action

Start M2-S01 using its required start message, then answer the five pre-code questions before creating any source file.