# Temporary Work Package 07 — Final Integration and Cleanup

**Status:** Blocked until Work Package 06 passes  
**Sequence:** 7 of 7  
**Primary repositories:** Canonical `motafegh/Career` and `motafegh/UpgradePilot`  
**Dependency:** Work Packages 01–06  
**Stop boundary:** Complete final review, record final refs, and delete all temporary refactor planning files.

> This package performs no broad redesign. It confirms that the completed edits form one coherent system, fixes only direct integration defects, and removes the temporary planning layer.

## 1. Outcome

After this package:

- canonical Career and UpgradePilot-local controls are coherent;
- accepted technical decisions and capability claims remain accurate;
- the redesigned system passes responsibility, learning, ownership, advanced-system, technical and snapshot checks;
- final commit references are recorded in the completion report;
- the temporary master plan and all temporary work-package files are deleted.

## 2. Inputs required

Before starting, collect:

- final canonical Career refactor commit(s);
- final canonical Career commit used for the snapshot;
- final UpgradePilot technical/entrypoint refactor commit(s);
- final UpgradePilot snapshot refresh commit;
- validation output or evidence from Work Package 06;
- any unresolved deviations from the work-package plans.

Do not start if an earlier work package is only partially complete unless the partial state and reason are explicitly reviewed.

## 3. Final integration review

### 3.1 Mission and technical decisions

Confirm:

- UpgradePilot mission, primary user and supported decision remain unchanged;
- project selection was not reopened;
- ADR-0002 remains accepted unless separate evidence formally changed it;
- current implementation status is not overstated;
- no source or product tests were silently created as part of the governance refactor.

### 3.2 Document responsibility

Confirm:

- each stable file has one clear responsibility;
- Career tracker owns exact current state and capability evidence;
- plans define requirements and gates, not routine result state;
- README files provide orientation, not live session control;
- `AGENTS.md` files contain stable operating rules, not transient project state;
- `MEMORY.md` is a concise continuation pointer;
- working memory preserves session evidence without claiming state authority.

### 3.3 Learning and execution

Confirm:

- lightweight, standard and formal modes are coherent;
- decision, bounded exploration, execution and tangent handling are distinct;
- mode selection uses the least ceremony consistent with risk and evidence;
- AI-assistance fading is explicit;
- Ali receives increasing responsibility for decomposition, tests, diagnosis and evidence selection;
- justified technical challenge is not suppressed by the one-next-action rule.

### 3.4 Capability and ownership

Confirm:

- capability evidence is scoped to specific responsibilities;
- assistance and transfer limits are explicit;
- ownership can be evaluated by dimension;
- D3+ cannot be established by immediate repetition or guided execution alone;
- delayed, changed-case, failure and reduced-assistance evidence is required where appropriate;
- existing claims were not inflated or reduced without evidence.

### 3.5 Operating rules

Confirm:

- the prerequisite limit is a review checkpoint;
- command explanation adapts to novelty and risk;
- governance planning, technical decisions and execution sketches are distinct;
- workload rules include a cognitive-quality stop;
- anti-diversion rules remain effective without blocking normal engineering decomposition.

### 3.6 Advanced systems

Confirm:

- all six areas retain A0 orientation;
- A1 is selected for two or three areas by evidence;
- at least one credible A2 remains targeted;
- second A2 and A3 are conditional;
- reject/defer decisions are valid evidence;
- exposure capacity cannot silently displace core ownership.

### 3.7 Technical specification and ADRs

Confirm:

- requirement strength terminology is defined;
- important invariants have stable IDs;
- proof obligations are traceable;
- specification behavior and ADR implementation choices are separated;
- semantic processing order is explicit;
- M2 raw-input preservation scope is accurate;
- ADR index and accepted ADR statuses are coherent.

### 3.8 Snapshot

Confirm:

- snapshot is point-in-time;
- canonical precedence is explicit;
- source commit and file set are accurate;
- mirrored content matches the selected canonical files;
- routine session changes no longer require snapshot refresh.

## 4. Final change-amplification tests

Answer each scenario with the exact expected files or artifact classes.

### New ADR

Must not normally require README, `AGENTS.md`, roadmap, learning-contract, original-plan or immediate snapshot edits.

### One passing test

Must not modify governance or navigation files.

### Same-milestone next-action change

Must affect only current state/continuation artifacts.

### Milestone transition

May use higher ceremony and one intentional snapshot refresh.

### Technical challenge to an accepted decision

Must permit bounded comparison and only change the ADR/specification when the decision or requirement changes.

### Long prerequisite repair

Must trigger review, not automatic replanning.

### Advanced-system opportunity

Must pass mission, baseline, readiness, capacity and ownership gates.

The refactor fails if these scenarios still produce uncontrolled propagation.

## 5. Integration-fix rule

If a direct contradiction, broken link or responsibility gap is found:

1. identify the authoritative owner;
2. make the smallest correction;
3. do not reopen already settled substantive policy;
4. rerun the affected validation;
5. record the correction in the final report.

Do not use final integration as permission for broad polishing.

## 6. Final acceptance gate

The refactor passes only when:

1. the original strong learning and evidence principles remain authoritative;
2. stable and transient information are separated;
3. accepted technical decisions remain accurate;
4. no capability or implementation claim is inflated;
5. AI control is designed to decrease with demonstrated ability;
6. ownership checks require meaningful evidence;
7. small work can proceed lightly;
8. consequential decisions can compare alternatives;
9. advanced-system breadth is selective beyond orientation;
10. technical requirements are traceable without duplicating framework mechanics;
11. snapshot synchronization is bounded;
12. change-amplification scenarios pass;
13. canonical Career and UpgradePilot controls are coherent;
14. local links and navigation are valid;
15. temporary planning files are no longer needed.

## 7. Completion report

Before deleting the temporary files, prepare a concise completion report containing:

- modified files by repository and work package;
- commit SHAs;
- final Career snapshot source commit;
- major responsibility changes;
- substantive rules preserved;
- substantive rules deliberately changed;
- validation performed and results;
- known limitations or deferred refinements;
- confirmation that product mission, ADR-0002 status and capability claims remain accurate.

The report may be delivered in the conversation or another already-authorized completion artifact. Do not create a new permanent governance document solely for the report.

## 8. Temporary-file removal

After the acceptance gate and completion report:

1. confirm no permanent file depends on the temporary plans as authority;
2. delete:
   - `TEMP_SPECIFICATION_SYSTEM_REFACTOR_PLAN.md`;
   - `TEMP_SPEC_REFACTOR_PLANS/01_DOCUMENT_RESPONSIBILITIES_AND_STATE.md`;
   - `TEMP_SPEC_REFACTOR_PLANS/02_SESSION_EXECUTION_AND_AI_CONTROL.md`;
   - `TEMP_SPEC_REFACTOR_PLANS/03_CAPABILITY_OWNERSHIP_AND_OPERATING_RULES.md`;
   - `TEMP_SPEC_REFACTOR_PLANS/04_ADVANCED_SYSTEMS_REBALANCE.md`;
   - `TEMP_SPEC_REFACTOR_PLANS/05_TECHNICAL_SPEC_AND_ENTRYPOINTS.md`;
   - `TEMP_SPEC_REFACTOR_PLANS/06_SNAPSHOT_AND_CONSISTENCY_VALIDATION.md`;
   - this file.
3. verify the temporary directory is empty/removed;
4. commit the deletion.

Recommended commit message:

`Remove completed specification refactor plans`

Deletion is a required part of completion, not optional cleanup.

## 9. Pass conditions

- [ ] All earlier work packages passed.
- [ ] Final integration review found no unresolved authority conflict.
- [ ] Change-amplification scenarios passed.
- [ ] Final refs and validation results were reported.
- [ ] No permanent artifact links to the temporary plans as controlling authority.
- [ ] All temporary refactor planning files were deleted.
- [ ] The repository returns to its normal product and learning execution flow.