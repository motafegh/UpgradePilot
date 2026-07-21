# UpgradePilot Evidence and Progress Tracker

**Owner:** Ali Rajabi  
**Status:** Approved and active canonical state/evidence tracker  
**Responsibility:** Current milestone/gate state, controlled responsibility, blockers, decisions, capability evidence, assistance, ownership, and limitations  
**Not responsible for:** Full session transcripts, stable governance rules, technical requirements, or detailed ADR rationale

## 1. Recording rules

1. Record observed state, not optimistic interpretation.
2. Link commits, files, commands, outputs, tests, queries, or public evidence where available.
3. Distinguish product progress from capability progress.
4. Use atomic responsibility records; do not mark a broad topic complete because one narrow task passed.
5. Record actual assistance and ownership dimensions.
6. Preserve failures, corrections, negative experiments, rejected methods, and superseded assumptions.
7. Update this tracker when a gate, blocker, material decision, capability claim, assistance assessment, or controlled responsibility changes.
8. Do not update it merely to transcribe every command or conversation.
9. Keep entries public-safe.
10. Accepted documentation, specifications, or ADRs do not establish executable behavior or capability ownership.
11. Source, tests, commands, outputs, and inspected environment state remain the authority for actual implementation behavior.

## 2. Current control state

| Field | Current state |
|---|---|
| Primary project | UpgradePilot |
| Governing charter | `../UpgradePilot.md` |
| Capability control | `../strategy/UPGRADEPILOT_CAPABILITY_AND_PREREQUISITE_SPECIFICATION.md` |
| Learning/execution control | `../governance/UPGRADEPILOT_LEARNING_AND_EXECUTION_CONTRACT.md` |
| Workload/capacity control | `../governance/90_DAY_EXECUTION_CONTRACT.md` |
| Session/blocker protocol | `../governance/SESSION_AND_BLOCKER_PROTOCOL.md` |
| Master roadmap | `../plans/UPGRADEPILOT_90_DAY_MASTER_ROADMAP.md` |
| Milestone plan | `../plans/UPGRADEPILOT_STAGED_MILESTONE_PLAN.md` |
| Active M2 transition plan | `../plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md` |
| Controlling M2 amendment | `../plans/UPGRADEPILOT_M2_S01_TECHNICAL_CONTRACT_AMENDMENT.md` |
| Core technical specification | UpgradePilot `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md` |
| Source-layout decision | UpgradePilot `docs/architecture/ADR-0001-initial-python-source-layout.md` |
| Runtime-contract decision | UpgradePilot `docs/architecture/ADR-0002-pydantic-runtime-contract-models.md` |
| Current route/milestone | R2 / M2 — Active |
| Current controlled responsibility | M2-S01 — Pydantic implementation onboarding for the initial trusted case transformation |
| Active PR case | `pydantic/pydantic#13432` |
| Current implementation truth | No accepted package metadata, installed runtime dependency, source implementation, tests, editable-install/import proof, or executable product behavior exists yet |
| Architecture boundary | Accepted source/package boundary and bounded Pydantic runtime-contract policy; complete internal architecture remains open |
| Active project working record | UpgradePilot `working-memory/2026-07-20_M2-S01_case-identity-implementation-start.md` |
| Next controlled responsibility | Teach the minimum Pydantic v2 concepts required for the first models; then create reviewed package metadata/dependency, verify editable installation/import resolution, and write the valid nested-contract test first |
| AegisLab | Deferred historical evidence; non-controlling |
| Sentinel | Research archive; non-controlling |

The exact next command belongs in the current project/session context, not in this tracker.

## 3. Route and milestone status

| Route | Milestone | Status | Primary evidence | Gate decision | Updated |
|---|---|---|---|---|---|
| R0 — Planning closure | M0 | Pass | Charter, controls, roadmap, milestone plan, tracker, first plan | G1 authorized | 2026-07-19 |
| R1 — Manual evidence reality | M1 | Pass | M1 report and working record | Narrow D2 guided; advance | 2026-07-19 |
| R2 — First automated vertical slice | M2 | Active | M1 report, audit, ADR-0001, core specification, amendment, ADR-0002, working record | Begin Pydantic package/test-first implementation | 2026-07-21 |
| R3 — Reliable evidence system | M3 | Not started | — | Depends on M2 | 2026-07-19 |
| R4 — Repository-specific context | M4 | Not started | — | Depends on M3 | 2026-07-19 |
| R5 — Deterministic baseline/evaluation | M5 | Not started | — | Depends on M4 | 2026-07-19 |
| R6 — Analytical experiments | M6 | Not started | — | Depends on M5 admission | 2026-07-19 |
| R7 — Advanced-system pilots | M7 | Not started | — | Existing approved strategy/capacity/gates remain controlling | 2026-07-19 |
| R8 — Final closure | M8 | Not started | — | Depends on prior gates | 2026-07-19 |

Status values: `Not started | Ready | Active | Partial | Blocked | Pass | Failed | Rejected | Deferred`.

## 4. Active deliverable register

| ID | Milestone | Deliverable | Status | Evidence | Pass requirement | Assistance/ownership conclusion |
|---|---|---|---|---|---|---|
| UP-S01-D1 | M1 | Manual evidence report | Pass | M1 report | Claims trace; limitations explicit | Substantial AI generation/assistance; Ali guided |
| UP-S01-D2 | M1 | Changed/missing-evidence variant | Pass | M1 report Section 10 | Recommendation changes without invention | AI-assisted; Ali guided |
| M2-ENTRY-01 | M2 | Prior architecture/state audit | Pass | UpgradePilot audit | False authority removed; scaffold absent | AI-generated under Ali direction; no technical capability claim |
| M2-LAYOUT-01 | M2 | Initial source-layout baseline | Pass — decision only | ADR-0001 | Professional boundary; no speculative layers | AI-recommended; Ali challenged/approved |
| M2-CONTRACT-01 | M2 | Core pipeline/information-contract baseline | Pass — specification only | Core specification and amendment | Correct boundaries, states, invariants, M2 activation | Substantially AI-generated after Ali identified gap |
| M2-METHOD-01 | M2 | Representation/runtime-validation method | Pass — decision only | ADR-0002 | Baselines compared; costs/reversal recorded; Ali approved | Substantially AI-generated; Ali-directed; no implementation ownership claim |
| M2-S01 | M2 | Initial trusted case transformation | Active — implementation not started | Active plan/amendment/working record | Installable package; nested contract; invalid/non-mutation tests; Ali change and diagnosed failure | AI teaching/review permitted; implementation/ownership pending |

## 5. Material decision and evidence ledger

| ID | Date | Artifact/decision | Supports | Does not prove | State |
|---|---|---|---|---|---|
| GOV-001 | 2026-07-19 | Charter and controls | Mission, route, evidence/learning controls | Implementation or ownership | Accepted |
| CASE-001 | 2026-07-19 | `pydantic/pydantic#13432` | Selected case/update context | Objective safety | Accepted for current work |
| CASE-002 | 2026-07-19 | M1 evidence report | Evidence matrix, weak decision, limitations | Independent ownership | Accepted |
| REPO-003 | 2026-07-19 | M2-entry audit | Corrected authority and absent scaffold | Implementation capability | Accepted |
| ARCH-DEC-001 | 2026-07-20 | ADR-0001 | Source/package boundary | Working imports or complete architecture | Accepted |
| SPEC-001 | 2026-07-21 | Core technical specification | Pipeline, contracts, invariants, evidence states | Executable behavior | Accepted |
| PLAN-002 | 2026-07-21 | M2 technical-contract amendment | Corrected M2 authorization/gates | Executable behavior | Accepted |
| ARCH-DEC-002 | 2026-07-21 | ADR-0002 | Pydantic v2 runtime-contract method and reassessment triggers | Installed dependency, models, tests, practical ownership | Accepted |

## 6. Atomic capability records

The capability specification controls interpretation. Current records are deliberately narrow.

### CAP-MAINT-001

```text
Capability family: Maintainer/Dependabot reasoning
Specific responsibility: Interpret one Dependabot PR evidence set and produce a weak bounded recommendation
Depth: D2 guided
Context: pydantic/pydantic#13432 M1 report
Evidence: M1 report and changed/missing-evidence variant
Assistance level: Substantial AI retrieval, explanation, and wording
Ownership dimensions: problem understanding guided; evidence interpretation guided; decision explanation guided
Changed-case evidence: One changed/missing-evidence variant
Failure evidence: None independently diagnosed
Delayed evidence: Not established
Last demonstrated: 2026-07-19
Breadth: One case
Confidence: Medium
Transfer limit: Does not establish independent maintainer review or repeated case handling
Reassessment trigger: A second case with reduced prompting
```

### CAP-GIT-001

```text
Capability family: Git/GitHub evidence
Specific responsibility: Explain PR number, repository, base/head revisions, and diff/history limits
Depth: D2 guided
Context: M1/M2 conceptual work
Evidence: Explanations and accepted contract correction
Assistance level: AI retrieved and explained evidence
Ownership dimensions: interpretation guided; operation not independently demonstrated
Changed-case evidence: Limited
Failure evidence: None
Delayed evidence: Not established
Last demonstrated: 2026-07-21
Breadth: One PR case
Confidence: Medium-low
Transfer limit: Does not establish branch/review workflow ownership or independent tool use
Reassessment trigger: Ali independently inspects and explains another PR snapshot
```

### CAP-PYSTRUCT-001

```text
Capability family: Python application structure
Specific responsibility: Distinguish distribution/import package, source root, tests, and package metadata boundary
Depth: D1 introduced with D2 guided design participation
Context: ADR-0001 and M2 preparation
Evidence: Ali challenged and approved the source-layout decision
Assistance level: Substantial AI recommendation and wording
Ownership dimensions: problem/design participation present; implementation/testing absent
Changed-case evidence: None
Failure evidence: None
Delayed evidence: Not established
Last demonstrated: 2026-07-20
Breadth: One planned package
Confidence: Medium
Transfer limit: No package creation, editable installation, import resolution, or blank-page application structure
Reassessment trigger: Create and explain the minimum package boundary and repair one import/install issue
```

### CAP-CONTRACT-001

```text
Capability family: Data contracts and transformation
Specific responsibility: Separate raw input, boundary validation, trusted nested data, persistence, and report roles
Depth: D2 guided conceptual design
Context: M2 core contract and ADR-0002
Evidence: Ali identified the missing contract layer, challenged premature method rejection, and approved the corrected boundaries
Assistance level: Substantial AI analysis and drafting
Ownership dimensions: problem framing/directing partial; design guided; implementation/testing/diagnosis absent
Changed-case evidence: Conceptual variants only
Failure evidence: Design-gap identification, not runtime diagnosis
Delayed evidence: Not established
Last demonstrated: 2026-07-21
Breadth: Initial M2 contract only
Confidence: Medium
Transfer limit: Does not establish executable validation/transformation ownership
Reassessment trigger: Implement, test, modify, and diagnose the initial trusted-case transformation
```

### CAP-PYDANTIC-001

```text
Capability family: Pydantic runtime contracts
Specific responsibility: Explain why Pydantic v2 is used for strict trusted application contracts and its major policy boundaries
Depth: D1 introduced / decision participation
Context: ADR-0002
Evidence: Method comparison and explicit approval
Assistance level: Substantial AI explanation/recommendation
Ownership dimensions: design participation limited; syntax/implementation/testing/diagnosis absent
Changed-case evidence: None
Failure evidence: None
Delayed evidence: Not established
Last demonstrated: 2026-07-21
Breadth: One decision
Confidence: Medium
Transfer limit: No model, validator, error, serialization, installation, or test execution
Reassessment trigger: First valid/invalid tests, implementation, changed case, and intentional failure repair
```

### CAP-TEST-001

```text
Capability family: Python testing/debugging
Specific responsibility: Design and diagnose strict boundary-model tests for the initial trusted case
Depth: D0–D1 mixed; not yet demonstrated
Context: M2-S01
Evidence: Concepts discussed only
Assistance level: AI-assisted discussion
Ownership dimensions: not established
Changed-case evidence: None
Failure evidence: None
Delayed evidence: None
Last demonstrated: Not established
Breadth: None
Confidence: High that D2 is absent
Transfer limit: No test-first implementation or failure diagnosis
Reassessment trigger: Valid, invalid, boundary, non-mutation, changed-case, and repair evidence
```

### CAP-PACKAGE-001

```text
Capability family: Packaging/dependency adoption
Specific responsibility: Declare Pydantic v2 compatibly, create package metadata, install editable, and verify imports
Depth: D0 practical / D1 conceptual
Context: M2-S01 onboarding
Evidence: Dependency decision only
Assistance level: Substantial guidance
Ownership dimensions: design decision participated; implementation/operation/diagnosis absent
Changed-case evidence: None
Failure evidence: None
Delayed evidence: None
Last demonstrated: 2026-07-21 conceptual only
Breadth: None practical
Confidence: High that practical capability is absent
Transfer limit: No metadata/install/import proof
Reassessment trigger: Complete onboarding and diagnose one relevant environment/import failure
```

### CAP-PROVENANCE-001

```text
Capability family: Provenance/evidence states
Specific responsibility: Distinguish raw/trusted data and missing, inaccessible, stale, conflicting, invalid, rejected, and accepted evidence
Depth: D2 guided conceptual
Context: M1 report and M2 contract
Evidence: Evidence matrix and contract taxonomy
Assistance level: AI-assisted
Ownership dimensions: interpretation guided; executable representation absent
Changed-case evidence: M1 missing-evidence variant
Failure evidence: Limited
Delayed evidence: Not established
Last demonstrated: 2026-07-21
Breadth: One case/contract
Confidence: Medium
Transfer limit: No executable provenance pipeline
Reassessment trigger: Implement and query/trace evidence through later milestones
```

### CAP-SQL-001

```text
Capability family: SQL/persistence
Specific responsibility: Not yet activated
Depth: D0
Context: Later milestone
Evidence: None
Assistance level: None
Ownership dimensions: None
Last demonstrated: Not established
Breadth: None
Confidence: High
Transfer limit: No practical SQL/persistence capability established
Reassessment trigger: Persistence milestone activation
```

### CAP-SECURE-001

```text
Capability family: Secure/reliable engineering
Specific responsibility: Reason about strict boundaries, explicit failure, raw/trusted separation, and untrusted-code limits
Depth: D2 guided provisional
Context: Governance, M1 evidence, M2 contracts
Evidence: Guided decisions and explanations
Assistance level: AI-assisted with Ali challenge/directing
Ownership dimensions: reasoning partial; implementation/testing/operation absent
Changed-case evidence: Limited
Failure evidence: Limited
Delayed evidence: Not established
Last demonstrated: 2026-07-21
Breadth: Several conceptual controls, no executable path
Confidence: Medium
Transfer limit: Does not establish implementation or operational security ownership
Reassessment trigger: Implement and diagnose boundary/failure behavior
```

### CAP-ADV-001

```text
Capability family: ML/graphs/LLM/agents/cloud/distributed/MLOps
Specific responsibility: Governed by existing advanced-systems strategy and later route gates
Depth: D0–D1 exposure mix; unchanged
Context: Prior repositories and conceptual exposure
Evidence: No UpgradePilot implementation evidence
Assistance level: Mixed historical AI assistance
Ownership dimensions: Not established for UpgradePilot
Changed-case evidence: Not established
Failure evidence: Not established
Delayed evidence: Not established
Last demonstrated: Historical exposure only
Breadth: Mixed exposure
Confidence: High that ownership is absent
Transfer limit: No professional or project ownership claim
Reassessment trigger: Existing approved exposure/pilot gates
```

## 7. Ownership-vector register for central artifacts

| Artifact/responsibility | Problem | Design | Implementation | Testing | Operation | Diagnosis | Explanation | Reproduction | Current conclusion |
|---|---|---|---|---|---|---|---|---|---|
| Governing planning documents | Ali-directed with AI support | Substantially AI-generated | N/A | N/A | N/A | N/A | Reviewed | Not applicable | Governance evidence only |
| M1 evidence report | Guided | Guided | N/A | Variant guided | Evidence retrieved largely by AI | Limited | Guided | Not established | Narrow D2 only |
| ADR-0001 source layout | Ali challenged/approved | AI-recommended | Absent | Absent | Absent | Absent | Guided | Absent | Decision participation only |
| Core contract specification | Ali identified gap | Substantially AI-generated | Absent | Absent | Absent | Design-gap identification | Guided | Absent | Specification evidence only |
| ADR-0002 Pydantic method | Ali proposed/challenged/approved | Substantially AI-generated | Absent | Absent | Absent | Absent | Conceptual acceptance | Absent | Decision participation only |
| UpgradePilot implementation | Pending | Pending | None accepted | None accepted | None accepted | None accepted | Pending | Pending | No implementation ownership claim |

## 8. Assistance labels

- **AI-generated** — AI produced substantive artifact, implementation, or central reasoning.
- **AI-assisted** — Ali performed meaningful work with substantial explanation/generation/repair.
- **Ali-directed** — Ali materially defined the responsibility, approach, constraint, or decision.
- **Ali-verified** — Ali independently checked behavior/evidence and correctly explained proof and limits.
- **Ali-owned** — Ali can explain, locate, modify, test, diagnose, reconnect, and reproduce with limited assistance at the stated scope.

Do not label a complete artifact “Ali-owned” when required ownership dimensions remain guided or absent.

## 9. Blockers and limitations

| ID | State | Description | Effect | Next evidence needed |
|---|---|---|---|---|
| BLK-M2-IMPLEMENTATION | Active prerequisite/implementation gap | Package metadata, dependency installation, source, tests, and import proof do not exist | M2 executable behavior and capability cannot advance | Complete reviewed onboarding and first test-first contract implementation |
| LIM-ONE-CASE | Active limitation | Most evidence comes from one PR case | Generalization is weak | Repeat on changed/second cases in later authorized work |
| LIM-AI-DIRECTION | Active limitation | Major specifications and decisions were substantially AI-generated | Ownership claims remain narrow | Ali-selected decomposition, tests, modifications, diagnosis, and delayed reconstruction |

## 10. State-update rule

Update this tracker when:

- a milestone/deliverable status changes;
- a blocker is added, materially changes, or closes;
- a technical decision is accepted/reversed;
- a capability depth, assistance level, ownership dimension, or transfer limit changes;
- the next controlled responsibility changes.

Do not update stable governance, README, `AGENTS.md`, roadmap, or milestone definitions merely because this tracker changes.

## 11. Immediate continuation

The current controlled responsibility remains M2-S01 Pydantic implementation onboarding.

The project-local current context should select the next exact action. The broader sequence is:

1. teach the minimum Pydantic v2 model/config/validation/error concepts;
2. establish reviewed package metadata and dependency range;
3. verify editable installation and import resolution;
4. write the valid nested-contract test first;
5. implement only the activated models/adapter;
6. add invalid, malformed SHA, non-mutation, and immutable-path cases;
7. require one Ali-directed central change and one diagnosed intentional failure;
8. update this tracker only when evidence changes a gate or capability conclusion.

No Day-90 advanced-systems strategy, capacity, exposure target, or completion requirement was changed by this tracker refactor.