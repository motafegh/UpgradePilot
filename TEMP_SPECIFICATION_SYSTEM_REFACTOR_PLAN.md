# Temporary Specification System Refactor — Coordination Index

**Status:** Temporary controlling index for the specification-system refactor only  
**Created:** 2026-07-21  
**Detailed work packages:** [`TEMP_SPEC_REFACTOR_PLANS/`](TEMP_SPEC_REFACTOR_PLANS/)  
**Removal condition:** Delete this index and all work-package files after final validation and completion reporting

> This temporary plan does not change the UpgradePilot mission, primary user, supported decision, accepted technical decisions, current milestone, implementation authorization, product architecture, capability evidence, or progress state. It controls only the bounded refactor of specifications, governance, instructions, state ownership, entrypoints, and snapshot behavior.

## 1. Why this refactor exists

The UpgradePilot/Career system contains strong controls for:

- mission-driven learning;
- real-input and failure-led engineering;
- just-in-time prerequisites;
- accurate mental models;
- conservative capability claims;
- explicit AI assistance;
- learner ownership;
- evidence-based technical decisions;
- narrow product boundaries;
- resistance to planning and architecture expansion.

The problem is structural rather than philosophical. Stable rules, live state, technical requirements, decisions, session evidence, navigation, and mirrored program files are mixed or duplicated. One logical decision can therefore trigger many administrative edits.

This refactor must reduce:

- excessive ceremony;
- state duplication;
- change amplification;
- temporal coupling;
- mixed document responsibilities;
- AI over-direction;
- performative ownership evidence;
- suppression of legitimate technical exploration;
- shallow technology-checklist exposure.

It must preserve rigor, safety, continuity, honest evidence, and product focus.

## 2. Shared design principles

Every work package must follow these rules:

1. **One authoritative owner per fact or rule.**
2. **Reference rather than repeat.**
3. **Stable rules and live state remain separate.**
4. **Plans/specifications define requirements; trackers/evidence record results.**
5. **Procedure is proportional to consequence, novelty, risk and learning importance.**
6. **AI control decreases as demonstrated capability grows.**
7. **Evidence quality matters more than checklist completion.**
8. **The product mission remains visible.**
9. **Simplification must not weaken safety, reasoning, testing or evidence.**
10. **Do not create another permanent governance layer.**

## 3. Work-package sequence

The packages are sequential. Do not execute later packages before earlier pass conditions are satisfied.

| Order | Work package | Main outcome | Status |
|---|---|---|---|
| 1 | [`01_DOCUMENT_RESPONSIBILITIES_AND_STATE.md`](TEMP_SPEC_REFACTOR_PLANS/01_DOCUMENT_RESPONSIBILITIES_AND_STATE.md) | One document responsibility and one canonical state owner | Ready |
| 2 | [`02_SESSION_EXECUTION_AND_AI_CONTROL.md`](TEMP_SPEC_REFACTOR_PLANS/02_SESSION_EXECUTION_AND_AI_CONTROL.md) | Proportional session modes, operating modes and fading AI control | Blocked by 01 |
| 3 | [`03_CAPABILITY_OWNERSHIP_AND_OPERATING_RULES.md`](TEMP_SPEC_REFACTOR_PLANS/03_CAPABILITY_OWNERSHIP_AND_OPERATING_RULES.md) | Atomic capability evidence, ownership vector and refined operating controls | Blocked by 02 |
| 4 | [`04_ADVANCED_SYSTEMS_REBALANCE.md`](TEMP_SPEC_REFACTOR_PLANS/04_ADVANCED_SYSTEMS_REBALANCE.md) | A0 breadth with evidence-selected A1/A2 depth | Blocked by 03 |
| 5 | [`05_TECHNICAL_SPEC_AND_ENTRYPOINTS.md`](TEMP_SPEC_REFACTOR_PLANS/05_TECHNICAL_SPEC_AND_ENTRYPOINTS.md) | Requirement traceability and lean UpgradePilot entrypoints | Blocked by 04 |
| 6 | [`06_SNAPSHOT_AND_CONSISTENCY_VALIDATION.md`](TEMP_SPEC_REFACTOR_PLANS/06_SNAPSHOT_AND_CONSISTENCY_VALIDATION.md) | Point-in-time snapshot and bounded structural validation | Blocked by 05 |
| 7 | [`07_FINAL_INTEGRATION_AND_CLEANUP.md`](TEMP_SPEC_REFACTOR_PLANS/07_FINAL_INTEGRATION_AND_CLEANUP.md) | Final coherence review, report and deletion of temporary plans | Blocked by 06 |

## 4. Repository order

1. Modify and validate canonical `motafegh/Career` controls through Work Packages 01–04.
2. Modify UpgradePilot-local technical and entrypoint files in Work Package 05.
3. Select one final reviewed Career commit and refresh the local snapshot once in Work Package 06.
4. Perform final integration and remove all temporary planning files in Work Package 07.

Do not refresh `docs/program/career/**` after each Career commit.

## 5. Global non-goals

This refactor must not, by itself:

- change the UpgradePilot mission, primary user, supported decision, or product boundary;
- reopen project selection;
- reverse ADR-0002;
- alter the current milestone or implementation order without a discovered direct contradiction;
- create product architecture, source code, tests, corpus, models, or advanced-system implementations;
- inflate or reduce capability claims without evidence;
- erase historical evidence;
- weaken safety, privacy, legal, cost, credential, or untrusted-code controls;
- weaken the distinction between AI-generated work and Ali-owned capability;
- become another permanent planning system.

## 6. Execution discipline

For each work package:

1. Read the latest affected files before editing.
2. Follow only that package’s scope.
3. Preserve unrelated substantive content.
4. Make changes in focused commits.
5. Validate the package’s scenarios and pass conditions.
6. Report files, commits, deliberate rule changes, preserved controls and unresolved limits.
7. Stop at the package boundary.
8. Mark the next package ready only after the current package passes.

Do not perform the entire refactor as one opaque rewrite.

## 7. Expected commit groups

The work packages recommend the following logical commit groups:

1. Career document responsibilities and state ownership.
2. Career session execution and AI-control transfer.
3. Career capability/ownership evidence and operating-rule refinement.
4. Career advanced-system exposure rebalance.
5. UpgradePilot technical specification traceability.
6. UpgradePilot README, `AGENTS.md`, `MEMORY.md`, and working-memory roles.
7. Bounded Career snapshot policy and one final refresh.
8. Validation fixes, if required.
9. Removal of temporary refactor plans.

## 8. Global acceptance conditions

The complete refactor passes only when:

- strong original learning and evidence principles remain authoritative;
- stable and transient information are separated;
- accepted technical decisions remain accurate;
- no capability or implementation claim is inflated;
- AI control is explicitly designed to decrease with demonstrated ability;
- ownership evidence cannot be satisfied through immediate repetition or guided execution alone;
- small work can use lightweight execution;
- consequential decisions can compare alternatives;
- advanced-system exposure is broad at orientation level and selective at hands-on/integrated depth;
- technical requirements are traceable without duplicating framework mechanics;
- the Career snapshot no longer requires routine synchronization;
- future ADRs, test results and next-action changes have small predictable update sets;
- canonical Career and UpgradePilot-local controls are coherent;
- links and navigation are valid;
- all temporary refactor planning files are deleted.

## 9. Exact next action

Begin:

[`TEMP_SPEC_REFACTOR_PLANS/01_DOCUMENT_RESPONSIBILITIES_AND_STATE.md`](TEMP_SPEC_REFACTOR_PLANS/01_DOCUMENT_RESPONSIBILITIES_AND_STATE.md)

Complete only its inventory, responsibility-boundary, transient-state, normative/result separation, and duplicate-rule consolidation work. Do not begin Work Package 02 or refresh the Career snapshot until Work Package 01 passes.