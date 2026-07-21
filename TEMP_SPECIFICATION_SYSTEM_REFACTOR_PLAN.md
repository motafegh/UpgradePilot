# Temporary Specification System Refactor — Coordination Index

**Status:** Temporary controlling index for the specification-system refactor only  
**Created:** 2026-07-21  
**Detailed work packages:** [`TEMP_SPEC_REFACTOR_PLANS/`](TEMP_SPEC_REFACTOR_PLANS/)  
**Removal condition:** Delete this index and all work-package files after final validation and completion reporting

> This temporary plan does not change the UpgradePilot mission, primary user, supported decision, accepted technical decisions, current milestone, implementation authorization, product architecture, capability evidence, progress state, or Day-90 advanced-systems strategy. It controls only the bounded refactor of specifications, governance, instructions, state ownership, entrypoints, and snapshot behavior.

## 1. Active scope

The refactor will reduce:

- excessive ceremony;
- state duplication and change amplification;
- mixed document responsibilities;
- AI over-direction;
- performative ownership evidence;
- suppression of legitimate technical exploration;
- unnecessary Career snapshot synchronization.

It must preserve rigor, safety, continuity, honest evidence, product focus, and all existing advanced-systems strategy/capacity/completion requirements.

## 2. Shared rules

1. One authoritative owner per fact or rule.
2. Reference rather than repeat.
3. Stable rules and live state remain separate.
4. Plans/specifications define requirements; trackers/evidence record results.
5. Procedure is proportional to consequence, novelty, risk, and learning importance.
6. AI control decreases as demonstrated capability grows.
7. Evidence quality matters more than checklist completion.
8. Simplification must not weaken safety, reasoning, testing, or evidence.
9. Do not create another permanent governance layer.
10. Do not modify advanced-systems strategy, capacity, targets, or completion requirements.

## 3. Active work-package sequence

The active packages are sequential. Work Package 04 is excluded and is not a dependency.

| Order | Work package | Main outcome | Status |
|---|---|---|---|
| 1 | [`01_DOCUMENT_RESPONSIBILITIES_AND_STATE.md`](TEMP_SPEC_REFACTOR_PLANS/01_DOCUMENT_RESPONSIBILITIES_AND_STATE.md) | One document responsibility and one canonical state owner | Active |
| 2 | [`02_SESSION_EXECUTION_AND_AI_CONTROL.md`](TEMP_SPEC_REFACTOR_PLANS/02_SESSION_EXECUTION_AND_AI_CONTROL.md) | Proportional session modes, operating modes, and fading AI control | Blocked by 01 |
| 3 | [`03_CAPABILITY_OWNERSHIP_AND_OPERATING_RULES.md`](TEMP_SPEC_REFACTOR_PLANS/03_CAPABILITY_OWNERSHIP_AND_OPERATING_RULES.md) | Atomic capability evidence, ownership vector, and refined operating controls | Blocked by 02 |
| — | [`04_ADVANCED_SYSTEMS_REBALANCE.md`](TEMP_SPEC_REFACTOR_PLANS/04_ADVANCED_SYSTEMS_REBALANCE.md) | Day-90 strategy/capacity/completion changes | **Excluded by user** |
| 4 | [`05_TECHNICAL_SPEC_AND_ENTRYPOINTS.md`](TEMP_SPEC_REFACTOR_PLANS/05_TECHNICAL_SPEC_AND_ENTRYPOINTS.md) | Requirement traceability and lean UpgradePilot entrypoints | Blocked by 03 |
| 5 | [`06_SNAPSHOT_AND_CONSISTENCY_VALIDATION.md`](TEMP_SPEC_REFACTOR_PLANS/06_SNAPSHOT_AND_CONSISTENCY_VALIDATION.md) | Point-in-time snapshot and bounded structural validation | Blocked by 05 |
| 6 | [`07_FINAL_INTEGRATION_AND_CLEANUP.md`](TEMP_SPEC_REFACTOR_PLANS/07_FINAL_INTEGRATION_AND_CLEANUP.md) | Final coherence review, report, and deletion of temporary plans | Blocked by 06 |

## 4. Repository order

1. Modify and validate canonical `motafegh/Career` controls through Work Packages 01–03.
2. Do not execute Work Package 04 and do not alter its governed strategy.
3. Modify UpgradePilot-local technical and entrypoint files in Work Package 05.
4. Select one final reviewed Career commit and refresh the local snapshot once in Work Package 06.
5. Perform final integration and remove all temporary planning files in Work Package 07.

Do not refresh `docs/program/career/**` after each Career commit.

## 5. Global non-goals

This refactor must not:

- change the UpgradePilot mission, primary user, supported decision, or product boundary;
- reopen project selection or reverse ADR-0002;
- alter the current milestone or implementation order without a discovered direct contradiction;
- change Day-90 advanced-systems strategy, capacity, A-level targets, adoption requirements, roadmap allocation, or completion gates;
- create product architecture, source code, tests, corpus, models, or advanced-system implementations;
- inflate or reduce capability claims without evidence;
- erase historical evidence;
- weaken safety, privacy, legal, cost, credential, or untrusted-code controls;
- weaken the distinction between AI-generated work and Ali-owned capability;
- become another permanent planning system.

## 6. Execution discipline

For each active work package:

1. Read the latest affected files before editing.
2. Follow only that package’s scope.
3. Preserve unrelated substantive content.
4. Validate the package’s scenarios and pass conditions.
5. Report files, commits, deliberate rule changes, preserved controls, and unresolved limits.
6. Stop at the package boundary before proceeding.

## 7. Global acceptance conditions

The active refactor passes only when:

- stable and transient information are separated;
- accepted technical decisions and capability claims remain accurate;
- AI control decreases with demonstrated ability;
- ownership evidence cannot be satisfied through immediate repetition or guided execution alone;
- small work can use lightweight execution;
- consequential decisions can compare alternatives;
- technical requirements are traceable without duplicating framework mechanics;
- the Career snapshot no longer requires routine synchronization;
- future ADRs, test results, and next-action changes have small predictable update sets;
- canonical Career and UpgradePilot-local controls are coherent;
- all advanced-systems strategy/capacity/completion requirements remain unchanged;
- links and navigation are valid;
- all temporary refactor planning files are deleted.

## 8. Exact next action

Complete Work Package 01, then continue through Packages 02, 03, 05, 06, and 07. Work Package 04 remains excluded.