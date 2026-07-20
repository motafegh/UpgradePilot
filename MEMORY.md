# UpgradePilot Current Memory

**Last updated:** 2026-07-20  
**Purpose:** Compact current-state memory for a newly started AI assistant. Keep this file below 200 lines.

## Current control state

- Primary project: UpgradePilot.
- Program window: 2026-07-20 through 2026-10-17.
- Current route: R2 — Automated vertical slice.
- Current milestone: M2 — First automated vertical slice.
- M1 / UP-S01: Passed on `pydantic/pydantic#13432`.
- M1 recommendation: run targeted checks for semantic correctness of generated Algolia search records.
- Architecture-status audit `M2-ENTRY-01`: Passed.
- `docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md` is approved and controlling.
- M2-S01 status: approved, not started.
- Exact start condition: use the required start message and answer the five pre-code questions before any source file is created.

## Repository state

- Repository role: documentation, memory, learning, planning, and authorized implementation home.
- Accepted source implementation before M2-S01 execution: none.
- Accepted tests, package configuration, executable examples, or CI: none.
- Accepted architecture: none.
- `docs/architecture/ARCHITECTURE.md` is retained as an unreviewed prior AI proposal, non-controlling and not Ali-owned.
- `docs/architecture/DECISIONS.md` is retained as an unreviewed proposal register; none of its entries is accepted.
- The premature AI-generated scaffold was removed from the active tree and remains available only through Git history.
- Do not restore, repair, continue, or use the removed scaffold as an implementation baseline automatically.
- Root responsibilities:
  - `README.md` — human-facing entry point and concise responsibility map;
  - `AGENTS.md` — durable repository-wide agent behavior;
  - `LEARNING-PREFERENCES.md` — durable project-specific teaching and assessment preferences;
  - `MEMORY.md` — current state;
  - `working-memory/` — detailed records for formal sessions and material work;
  - `learning/` — durable educational artifacts;
  - `plans/` — future detailed project-local technical plans;
  - Career tracker — canonical general product-progress and capability state.

## Completed evidence

- Repository correction: `working-memory/2026-07-19_REPO-AUDIT_premature-scaffold-correction.md`.
- M1 investigation: `working-memory/2026-07-19_UP-S01_manual-evidence-investigation.md`.
- Architecture-status audit: `working-memory/2026-07-19_M2-ENTRY_architecture-status-audit.md`.
- Agent-instruction redesign: `working-memory/2026-07-19_REPO-GOV_agent-instructions-and-learning-preferences.md`.
- Learning/planning environment: `working-memory/2026-07-19_REPO-GOV_learning-environment-and-plan-ownership.md`.
- Responsibility map and tracker ownership: `working-memory/2026-07-20_REPO-GOV_readme-responsibility-map-and-tracker.md`.

## M1 demonstrated depth

- Public evidence retrieval and report assembly were substantially AI-generated / AI-assisted.
- Ali correctly challenged an uninformed prediction request and redirected instructional pace when the session became confusing.
- Ali demonstrated narrow guided understanding of:
  - direct versus transitive dependency;
  - repository-specific relevance;
  - observed versus inferred versus unresolved versus unsupported evidence;
  - why passing CI is scope-limited;
  - silent output regression;
  - proportional targeted-check selection;
  - changed-evidence reasoning.
- Ali's silent-failure explanation used a strong prior ML analogy involving offline/online graph-extractor mismatch.
- Independent end-to-end repository investigation, GitHub API operation, and implementation ownership were not demonstrated.

## Architecture audit result

- `ARCH-001` is resolved.
- False `Accepted`, `Active`, and Ali-decision-owner claims were removed or superseded.
- Retained technical material is historical proposal content only.
- The audit did not adopt a package layout, CLI, JSON contract, deterministic policy, database, adapter structure, test strategy, or CI approach.

## Current decisions

1. Learning and ownership must precede accepted implementation.
2. AI-generated code does not become project progress merely because it exists or passes tests.
3. The M1 report action is `run targeted checks`, not a safety certification.
4. M1 passes at narrow D2 guided depth; broad capability mastery is not claimed.
5. Retained architecture ideas are candidates only; each must be rederived and explicitly decided when a real responsibility requires it.
6. Build future responsibilities through: teach → predict → execute/direct → inspect → modify/test/diagnose → record evidence.
7. Current state must not be stored in `AGENTS.md` or `LEARNING-PREFERENCES.md`.
8. Accepted learning artifacts live under `learning/` on `main`; there is no permanent learning branch.
9. Career owns program-level planning; UpgradePilot owns future detailed technical plans under `plans/`.
10. The current M2-S01 plan remains the Career-owned transition artifact and is not moved or duplicated.
11. Agents use the minimum process justified by consequence, uncertainty, state impact, and continuity; lightweight interactions do not create unnecessary plans or working-memory files.
12. New directory structure is created only when a real artifact requires it.
13. `README.md` contains the concise repository responsibility map; no separate map file is needed now.
14. `Career/tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md` is the single general product-progress and capability tracker; UpgradePilot must not duplicate it.
15. A project-local technical inventory is allowed only for a distinct engineering concern and must not duplicate the canonical tracker.

## M2-S01 authorized responsibility

Given manually supplied identity fields for `pydantic/pydantic#13432`, validate and normalize them into one deterministic Python record without mutating the raw input.

Required behavior and evidence:

1. use a manually created plain Python dictionary from the M1 report;
2. validate required identity fields and normalize text values;
3. require a positive PR number and 40-character hexadecimal base/head SHAs;
4. require non-empty dependency, version, and changed-file values;
5. require old and new versions to differ;
6. return a new normalized dictionary while leaving raw input unchanged;
7. include one valid unit test, one malformed-head-SHA test, and a raw-input non-mutation assertion;
8. preserve one Ali-directed change and update working memory and the canonical tracker.

Not authorized in M2-S01:

- restoration of prior JSON, CLI, policy, package layout, or tests;
- live network acquisition;
- persistence or databases;
- recommendation-policy breadth;
- services, containers, cloud, models, agents, or broader architecture adoption.

## Pre-code gate

Before any source file is created, Ali must explain:

1. why case identity is separate from release, CI, and recommendation evidence;
2. which fields identify the exact PR snapshot;
3. what should happen when the head SHA is malformed;
4. why normalization returns a new dictionary instead of mutating the raw one;
5. what the valid test proves and does not prove.

## Proportional operating model

- Lightweight explanation, clarification, idea discussion, or small reversible edit: no new plan or working-memory file unless persistent state changes.
- Bounded continuation inside M2-S01: reuse its plan and one active working-memory record.
- New formal responsibility or multi-step investigation: one project-local plan when justified and one working-memory record.
- High-consequence work: full authority, risk, rollback, and validation checks.
- Read `MEMORY.md`, the active plan/record, and directly relevant files; do not scan all history.

## Exact next authorized action

Start M2-S01 using its required start message, then answer the five pre-code questions above. Do not create source files before the pre-code gate passes.

## Canonical references

- `README.md`
- `docs/program/SOURCE.md`
- `docs/program/career/README.md`
- `docs/program/career/AGENTS.md`
- `docs/program/career/governance/EXECUTION_CONTRACT.md`
- `docs/program/career/strategy/STRATEGY_AND_SCOPE.md`
- `docs/program/career/UpgradePilot.md`
- `docs/program/career/strategy/UPGRADEPILOT_CAPABILITY_AND_PREREQUISITE_SPECIFICATION.md`
- `docs/program/career/governance/UPGRADEPILOT_LEARNING_AND_EXECUTION_CONTRACT.md`
- `docs/program/career/plans/UPGRADEPILOT_90_DAY_MASTER_ROADMAP.md`
- `docs/program/career/plans/UPGRADEPILOT_STAGED_MILESTONE_PLAN.md`
- `docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md`
- `docs/program/career/tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md`
