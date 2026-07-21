# Temporary Specification System Refactor — Coordination Index

**Status:** Active; major non-strategic refactor completed, bounded residual cleanup remains  
**Created:** 2026-07-21  
**Detailed work packages:** [`TEMP_SPEC_REFACTOR_PLANS/`](TEMP_SPEC_REFACTOR_PLANS/)  
**Removal condition:** Delete this index and all work-package files only after residual durable-state cleanup and final validation pass

> This refactor does not change the UpgradePilot mission, primary user, supported decision, accepted technical decisions, current milestone, implementation authorization, product architecture, capability evidence, or Day-90 advanced-systems strategy/capacity/completion requirements.

## 1. Work-package status

| Order | Work package | Status | Result |
|---|---|---|---|
| 1 | [`01_DOCUMENT_RESPONSIBILITIES_AND_STATE.md`](TEMP_SPEC_REFACTOR_PLANS/01_DOCUMENT_RESPONSIBILITIES_AND_STATE.md) | **Partial** | Entry points, core governance, strategy, capability spec, tracker, and session protocol now have explicit owners; residual live-state fields remain in charter/roadmap/milestone/transition artifacts |
| 2 | [`02_SESSION_EXECUTION_AND_AI_CONTROL.md`](TEMP_SPEC_REFACTOR_PLANS/02_SESSION_EXECUTION_AND_AI_CONTROL.md) | **Pass** | Lightweight/standard/formal session modes, decision/exploration/execution/tangent modes, and D-level AI-control transfer are active |
| 3 | [`03_CAPABILITY_OWNERSHIP_AND_OPERATING_RULES.md`](TEMP_SPEC_REFACTOR_PLANS/03_CAPABILITY_OWNERSHIP_AND_OPERATING_RULES.md) | **Pass** | Atomic capability records, ownership vector, delayed/changed/failure evidence, prerequisite checkpoint, adaptive command explanation, planning categories, and cognitive stop are active |
| — | [`04_ADVANCED_SYSTEMS_REBALANCE.md`](TEMP_SPEC_REFACTOR_PLANS/04_ADVANCED_SYSTEMS_REBALANCE.md) | **Excluded by user** | No Day-90 strategy, capacity, A-level target, roadmap allocation, or completion requirement was changed |
| 4 | [`05_TECHNICAL_SPEC_AND_ENTRYPOINTS.md`](TEMP_SPEC_REFACTOR_PLANS/05_TECHNICAL_SPEC_AND_ENTRYPOINTS.md) | **Pass** | Requirement keywords/IDs/proof mapping and lean README/AGENTS/MEMORY/ADR-index responsibilities are active |
| 5 | [`06_SNAPSHOT_AND_CONSISTENCY_VALIDATION.md`](TEMP_SPEC_REFACTOR_PLANS/06_SNAPSHOT_AND_CONSISTENCY_VALIDATION.md) | **Pass with recorded limit** | Point-in-time snapshot policy is active and snapshot is pinned to canonical Career commit `152f4c31bf5bb2fb6af08806a4f16c7408787c49`; final full-repository link scan remains part of WP07 |
| 6 | [`07_FINAL_INTEGRATION_AND_CLEANUP.md`](TEMP_SPEC_REFACTOR_PLANS/07_FINAL_INTEGRATION_AND_CLEANUP.md) | **Blocked** | Waits for residual WP01 cleanup and final integration validation |

## 2. Completed structural outcomes

- Career tracker is the canonical live-state and capability owner.
- README and `AGENTS.md` entrypoints no longer duplicate exact session state.
- Learning/Execution Contract owns mandatory Ali–AI behavior.
- Learning Preferences owns teaching presentation and interaction style.
- Session and Blocker Protocol owns proportional modes and blocker/prerequisite procedure.
- Capability Specification owns D0–D5 evidence, atomic records, ownership dimensions, and claim limits.
- Strategy and Scope owns stable identity, priorities, career targets, evidence expectations, and unchanged advanced-systems strategy.
- UpgradePilot technical specification now uses normative keywords, stable requirement IDs, explicit validation order, M2 raw-scope limits, and proof mapping.
- ADR index separates implementation decisions from requirements and live state.
- UpgradePilot `MEMORY.md` is a concise continuation pointer.
- Career snapshot is a reviewed point-in-time package, not a live per-session mirror.

## 3. Explicitly preserved advanced-systems requirements

The following remain unchanged:

- A1 hands-on exposure for all six named advanced-systems areas;
- A2 project-integrated pilots for at least two areas;
- approved route capacity and scheduling;
- adoption/rejection and baseline-comparison rules;
- Day-90 completion requirements.

Work Package 04 remains excluded and is not a dependency.

## 4. Residual bounded work

Do not perform another broad rewrite. Inspect and correct only direct responsibility violations in:

- canonical Career `UpgradePilot.md` — remove or relabel obsolete activation/next-artifact wording while preserving the full product charter;
- canonical Career `plans/UPGRADEPILOT_90_DAY_MASTER_ROADMAP.md` — make route status descriptive/static or tracker-routed without changing dates, capacity, route sequence, or advanced requirements;
- canonical Career `plans/UPGRADEPILOT_STAGED_MILESTONE_PLAN.md` — remove live-status ownership without changing outcomes, gates, capacities, or completion rules;
- current/historical transition plans or amendments — separate fixed requirements from tracker-owned result/continuation state where direct duplication remains;
- corresponding Career snapshot files after one final reviewed canonical commit.

Do not modify the Advanced Systems Exposure and Adoption Policy or use cleanup as a reason to change its downstream requirements.

## 5. Final acceptance scenarios

Before cleanup, demonstrate:

1. A new ADR normally changes only the ADR/index, directly affected specification, tracker decision, and concise memory when continuation changes.
2. One test result changes source/tests/evidence and only changes tracker/memory when state materially changes.
3. An exact-next-action change does not rewrite README, `AGENTS.md`, charter, contracts, strategy, roadmap, or milestone definitions.
4. A milestone transition may legitimately update the tracker, activation metadata, coarse maturity summary, and one intentional snapshot.
5. A justified technical challenge can enter bounded decision/exploration mode.
6. A prerequisite exceeding 90 minutes triggers review rather than an automatic new roadmap.
7. All local Markdown links and snapshot paths are valid.
8. Canonical and mirrored content match the final selected Career commit.
9. Advanced-systems strategy/capacity/completion requirements remain unchanged.

## 6. Exact next action

Complete only the residual durable-state cleanup listed in Section 4. Then perform WP07 validation and delete this index plus `TEMP_SPEC_REFACTOR_PLANS/`.
