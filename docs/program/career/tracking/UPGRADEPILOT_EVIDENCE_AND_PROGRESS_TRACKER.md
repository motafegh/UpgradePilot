# UpgradePilot Evidence and Progress Tracker

**Owner:** Ali Rajabi  
**Recorded:** 2026-07-20  
**Status:** Approved and active evidence/progress tracker  
**Authority:** Records current state, milestone evidence, capability depth, assistance, ownership, blockers, and decisions under the UpgradePilot charter, capability specification, Learning and Execution Contract, master roadmap, and staged milestone plan  
**Activation effect:** M1 and the M2-entry architecture-status audit have passed. M2-S01 is active. The initial Python source-layout baseline is accepted and synchronized into UpgradePilot; no source, package metadata, installation evidence, or tests exist yet, and the integrated behavior gate remains open.

## 1. Recording rules

1. Record observed state, not optimistic interpretation.
2. Link commits, files, commands, outputs, tests, queries, screenshots, or public evidence where available.
3. Distinguish product progress from capability progress.
4. Distinguish exposure from guided application, independent bounded application, ownership, and advanced capability.
5. Record AI assistance using approved labels.
6. Do not mark a broad topic complete because one narrow task passed.
7. Preserve failures, corrections, negative experiments, and rejected technologies.
8. Update the exact next action after every session or governance change.
9. Keep all entries public-safe.
10. A missing entry does not imply success.

## 2. Current control state

| Field | Current state |
|---|---|
| Primary project | UpgradePilot |
| Governing charter | `../UpgradePilot.md` |
| Capability control | `../strategy/UPGRADEPILOT_CAPABILITY_AND_PREREQUISITE_SPECIFICATION.md` |
| Learning/execution control | `../governance/UPGRADEPILOT_LEARNING_AND_EXECUTION_CONTRACT.md` |
| Master roadmap | `../plans/UPGRADEPILOT_90_DAY_MASTER_ROADMAP.md` |
| Milestone plan | `../plans/UPGRADEPILOT_STAGED_MILESTONE_PLAN.md` |
| Completed M1 session plan | `../plans/UPGRADEPILOT_FIRST_SESSION_PLAN.md` |
| Active session plan | `../plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md` |
| Current route | R2 — Automated vertical slice |
| Current milestone | M2 — First automated vertical slice — Active |
| Current session | M2-S01 — Active; pre-code onboarding in progress |
| M1 result | Pass — manual evidence report and changed-evidence variant complete |
| M2-entry audit | Pass — prior AI architecture invalidated; no former AI decision controls current work |
| Session mode | Green |
| Focused minutes | Not recorded |
| Implementation status | No source, package metadata, installation output, or tests yet; integrated behavior gate remains open |
| Initial source-layout baseline | Accepted and synchronized: repository `UpgradePilot`; distribution/import package `upgradepilot`; source root `src/upgradepilot/`; tests under `tests/`; minimal `pyproject.toml` only when implementation begins |
| Architecture scope | Source/package boundary accepted; complete internal architecture remains intentionally undecided |
| Implementation repository | `motafegh/UpgradePilot` |
| UpgradePilot synchronization | Merge `6fa34eaa273e381637917080fdb66989bd077f97` |
| Active working record | `UpgradePilot/working-memory/2026-07-20_M2-S01_case-identity-normalization.md` |
| Accepted decision record | `UpgradePilot/docs/architecture/ADR-0001-initial-python-source-layout.md` |
| Active PR case | `pydantic/pydantic#13432` |
| Exact next action | Close the integrated behavior gate, then create the minimal installable package boundary and write the valid test first |
| AegisLab | Deferred historical evidence; non-controlling |
| Sentinel | Research archive; non-controlling |

## 3. Route and milestone status

| Route | Milestone | Status | Primary evidence | Gate decision | Updated |
|---|---|---|---|---|---|
| R0 — Planning closure | M0 | Pass | Charter, capability specification, contract, roadmap, milestone plan, tracker, first-session plan | Technical G1 session authorized | 2026-07-19 |
| R1 — Manual evidence reality | M1 | Pass | `evidence/UP-S01_pydantic-13432_manual-evidence-report.md`; UpgradePilot working-memory record | Narrow D2 guided application accepted; advance to M2 | 2026-07-19 |
| R2 — Automated vertical slice | M2 | Active | M1 report; architecture-status audit; active M2-S01 plan and working record; accepted ADR-0001 | Close M2-S01 behavior gate, create minimal package boundary, then write the valid test first | 2026-07-20 |
| R3 — Reliable evidence system | M3 | Not started | — | Depends on M2 | 2026-07-19 |
| R4 — Repository-specific context | M4 | Not started | — | Depends on M3 | 2026-07-19 |
| R5 — Deterministic baseline and evaluation | M5 | Not started | — | Depends on M4 | 2026-07-19 |
| R6 — Analytical experiments | M6 | Not started | — | Depends on M5 admission | 2026-07-19 |
| R7 — Advanced-system pilots | M7 | Not started | — | Depends on supported core and prerequisites | 2026-07-19 |
| R8 — Final closure | M8 | Not started | — | Depends on prior gates | 2026-07-19 |

Status values: `Not started | Ready | Active | Partial | Blocked | Pass | Failed | Rejected | Deferred`.

## 4. Active deliverable register

| ID | Milestone | Deliverable | Status | Evidence path/link | Pass requirement | Assistance | Owner |
|---|---|---|---|---|---|---|---|
| UP-S01-D1 | M1 | Manual evidence report for `pydantic/pydantic#13432` | Pass | `evidence/UP-S01_pydantic-13432_manual-evidence-report.md` | Material claims trace to evidence; limitations explicit | AI-generated / AI-assisted; Ali reviewed reasoning incrementally | Ali with substantial AI teaching and evidence retrieval |
| UP-S01-D2 | M1 | Changed or missing-evidence variant | Pass | Same evidence report, Section 10 | Recommendation changes without invented certainty | AI-assisted; Ali followed and accepted changed-risk logic | Ali at guided depth |
| UP-S01-D3 | M1 | Session evidence and ownership record | Pass | Report Sections 12–14; UpgradePilot UP-S01 working memory | Assistance and demonstrated depth recorded accurately | Joint record; conservative ownership | Ali and AI |
| M2-ENTRY-01 | M2 | Prior architecture and repository-state audit | Pass | UpgradePilot M2-entry working memory | False accepted/owned claims removed; no prior architecture controls current work; active scaffold absent | AI-generated under Ali-directed boundary | Ali-directed; no technical ownership claim |
| M2-LAYOUT-01 | M2 | Initial Python source-layout baseline | Pass — decision only | Career plan merge `ab1a68e...`; UpgradePilot ADR and alignment merge `6fa34eaa...` | Professional source/package boundary selected and synchronized without speculative internal layers or implementation claims | AI-recommended; Ali explicitly agreed and directed synchronization | Ali-directed; not Ali-owned packaging capability |
| M2-S01 | M2 | Case-identity normalization | Active | `../plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md`; UpgradePilot active working record | Installable package boundary; real case normalizes; malformed SHA rejected; raw input unchanged; one Ali-directed change and diagnosed failure | AI-assisted; implementation evidence pending | Ali with AI teaching/review |

## 5. Session and audit ledger

| Session / step | Date | Mode | Focused minutes | Deliverable | Result | Evidence/commit | Assistance | Capability evidence | Exact next action |
|---|---|---|---:|---|---|---|---|---|---|
| UP-S01 | 2026-07-19 | Read-only evidence session | Not reliably measured | First manual evidence decision | Pass | Career report commit `3519a8aa651073eec1ed2ca14c82a07f624b7158`; UpgradePilot closure `a9006506...` | Substantial AI retrieval/teaching; Ali-directed challenges and guided verification | Narrow D2 guided application | M2 entry audit |
| M2-ENTRY-01 | 2026-07-19 | Documentation/ownership audit | Not separately timed | Invalidate prior AI architecture and verify active tree | Pass | Architecture audit closure `5999bed2...` | AI inspection/edits under Ali-directed ownership boundary | No architecture or implementation capability created | Define M2-S01 |
| M2-LAYOUT-01 | 2026-07-20 | Architecture-boundary review | Not recorded | Select and synchronize initial Python source/package boundary | Pass — decision only | Career merge `ab1a68e...`; UpgradePilot merge `6fa34eaa...` | Technical recommendation substantially AI-generated; Ali challenged assumptions, required a production-grade review, agreed, and directed alignment | Guided understanding of repository versus import-package distinction; no installation or packaging execution | Close behavior gate |
| M2-S01 | 2026-07-20 | Green | Not recorded | Case-identity normalization | Active — orientation and teaching substantially completed; layout synchronized; behavior gate open | UpgradePilot merge `6fa34eaa...` includes ADR, active record, learning note, and project-state alignment | AI-assisted; Ali directed assessment-method and source-layout corrections | Guided conceptual reasoning only; no code, install, import, test execution, or implementation ownership | Close integrated behavior gate, create minimum package boundary, write valid test first |

UP-S01 summary:

```text
Recommendation: Run targeted checks; no material incompatibility found in inspected scope; semantic correctness of generated Algolia records remains unresolved.
Changed case: Active Python 3.8 support without CI coverage changes the action to investigate or block.
Ali can explain: dependency path, evidence-versus-inference, scope limits of green CI, silent-output risk, and proportional checking.
Limitation: independent end-to-end investigation and implementation ownership not demonstrated.
```

M2-entry audit summary:

```text
Starting conflict: prior AI-generated files claimed accepted/active architecture and Ali ownership.
Correction: false authority and ownership were removed; the generated scaffold was removed from the active tree.
Final disposition: the former architecture files were removed from the active tree after fresh ADR-0001 replaced the only currently required boundary.
Validation: package metadata, source, tests, executable examples, and CI remain absent.
```

M2 source-layout decision summary:

```text
Repository/product workspace: UpgradePilot
Distribution and import package: upgradepilot
Source root: src/upgradepilot/
Test root: tests/
Project metadata: minimal pyproject.toml when implementation begins
Accepted scope: source/package boundary only
Deferred: internal layering, CLI, adapters, services, persistence, frameworks, and publication automation
Reassessment trigger: observed import, packaging, distribution, interface, or module-cohesion limitation
```

M2-S01 active summary:

```text
Current responsibility: validate and normalize the manually supplied identity of pydantic/pydantic#13432 without mutating raw input.
Teaching covered: exact snapshot identity, raw versus normalized data, validation, deterministic transformation, ValueError, Python data/function/module mechanics, bounded test claims, and source/package naming distinctions.
Instructional correction: replace fragmented micro-questions with meaningful chunks followed by one integrated reasoning or practical assessment.
Current boundary: no package metadata, source, tests, installation, imports, or accepted behavior exist; the integrated behavior gate remains open.
```

## 6. Capability depth ledger

The M1 increases remain narrow. The layout decision records guided design participation, not practical packaging or application ownership.

| Capability | Initial state | Current state | Latest demonstrated evidence | Assistance | Confidence | Limitation | Updated |
|---|---|---|---|---|---|---|---|
| Maintainer workflow and Dependabot reasoning | D1 provisional | **D2 guided — narrow M1 case** | One weak next-action recommendation and changed-evidence response | Substantial AI teaching | Medium | Not independently reproduced on a second case | 2026-07-19 |
| Git/GitHub PR, diff, history, review evidence | D1 provisional | **D2 guided — interpretation only** | Explains PR purpose, changed file, base/head role, and why merged status is not truth | AI retrieved most evidence | Medium-low | Tool/API execution not independently demonstrated | 2026-07-19 |
| Python application structure | D1 provisional | D1 provisional — guided layout decision | Distinguished repository, distribution, import package, module, and source-root roles; accepted `src/upgradepilot/` after challenge and comparison | Substantial AI recommendation; Ali-directed challenge and agreement | Medium | No `pyproject.toml`, package creation, installation, import, implementation, modification, or execution evidence | 2026-07-20 |
| Testing, debugging, types, exceptions, CLI/config | D0–D1 mixed | D0–D1 mixed | `unittest`, assertions, `ValueError`, type hints, and bounded test claims taught; no test execution or diagnosis | AI-assisted | High that D2 implementation is absent | M2-S01 still requires test-first work, failure interpretation, and Ali-directed modification | 2026-07-20 |
| Python packaging metadata and dependency semantics | D0 | D0–D1 mixed | Lockfile interpretation at D2 guided; repository/distribution/import-package and editable-install concepts introduced | Substantial guidance | High that practical packaging capability is absent | No metadata authored, build backend configured, editable install run, or import verified | 2026-07-20 |
| Dependency semantics and SemVer limits | D0 | **D2 guided — narrow dependency path** | Classified Soup Sieve as transitive and rejected version-number certainty | AI-assisted | Medium | One bounded path only | 2026-07-19 |
| HTTP/JSON/API acquisition | D1 overall; HTTP D2 guided | Unchanged | AI used read-only interfaces; Ali did not independently operate acquisition | Substantial guidance | Medium | Deferred from M2-S01 | 2026-07-19 |
| Evidence contracts, provenance, and quality states | D1 provisional | **D2 guided — narrow evidence matrix** | Distinguished observed, inferred, unresolved, unsupported, and historical context | AI-assisted | Medium | Full claim tracing not independently reproduced | 2026-07-19 |
| SQL and relational persistence | D0 | D0 | None at required depth | — | High | Assessed at M3 | 2026-07-19 |
| Deterministic decision and abstention | D1 provisional | **D2 guided — one recommendation** | Applied action-class rule and changed outcome when evidence changed | AI-assisted | Medium | Policy code deferred from M2-S01 | 2026-07-19 |
| Evaluation, labels, leakage, calibration | D0–D1 provisional | Unchanged | Existing-tool comparison discussed conceptually | Assisted | High that ownership absent | Assessed at M5 | 2026-07-19 |
| Static analysis and repository context | D1 provisional | **D2 guided — narrow source relevance** | Reasoned about docs/HTML usage and direct versus indirect API relevance | AI performed searches | Medium-low | Repository-wide context absent | 2026-07-19 |
| Graph methods | D0 | D0 | Exposure only | — | High | Evidence-gated M6 only | 2026-07-19 |
| Machine learning | D0 provisional | D0 provisional | Prior-experience analogy to offline/online feature mismatch | Ali-generated explanation | High | No UpgradePilot ML responsibility | 2026-07-19 |
| Secure/reliable engineering | D2 guided provisional | D2 guided provisional | Reasoned about fail-fast versus silent output corruption | AI-assisted with strong Ali transfer | Medium | Implementation evidence pending | 2026-07-19 |
| CI and Docker | D1 provisional | **CI D2 guided concept; Docker unchanged** | Explains that passing CI proves only executed scope | AI retrieved CI | Medium | CI forbidden in M2-S01 | 2026-07-19 |
| Grounded LLM evaluation | D0 | D0 | No preserved entailment evaluation | — | High | Evidence-gated M6 | 2026-07-19 |
| Agents, queues, microservices | D0 | D0 | No capability evidence | — | High | M7 only | 2026-07-19 |
| Kubernetes and cloud/multi-cloud | D0 | D0 | No execution evidence | — | High | M7 only | 2026-07-19 |
| MLOps | D0 | D0 | No lifecycle ownership evidence | — | High | M6/M7 after admission | 2026-07-19 |

## 7. Assistance and ownership evidence

Approved labels:

- **AI-generated** — AI produced the substantive artifact or implementation.
- **AI-assisted** — Ali performed meaningful work with substantial explanation, generation, correction, or repair.
- **Ali-directed** — Ali materially defined the responsibility, approach, constraint, or decision.
- **Ali-verified** — Ali inspected checks and correctly explained what they prove and do not prove.
- **Ali-owned** — Ali can explain, locate, modify, test, diagnose, reconnect, and reproduce the responsibility with limited assistance.

| Artifact/responsibility | AI-generated | AI-assisted | Ali-directed | Ali-verified | Ali-owned | Evidence |
|---|---|---|---|---|---|---|
| Governing planning documents | Yes, substantially | Yes | Yes, through requirements and review direction | Governance consistency reviewed with Ali | No technical ownership claim | Repository commits and conversation record |
| UP-S01 evidence retrieval | Yes, substantially | Yes | Ali redirected pace and challenged unsupported prediction | Selected interpretations verified with teaching | No | Report and working memory |
| UP-S01 report | Yes, assembly and much wording | Yes | Ali directed honesty, scope, and repository synchronization | Core dependency/risk/check logic verified at guided depth | No independent end-to-end ownership | M1 report |
| Silent-failure reasoning | No substantive generation beyond context | Light assistance | Yes, through Ali's ML analogy | Yes | Narrow conceptual ownership | M1 report and work record |
| M2-S01 pre-code onboarding | Teaching and notes substantially AI-generated | Yes | Ali corrected pacing, assessment method, source-layout framing, and repository-alignment requirement | Selected concepts reasoned with guidance; behavior gate remains open | No | UpgradePilot active working record and learning note |
| Initial source-layout baseline | Technical recommendation and wording substantially AI-generated | Yes | Ali challenged the duplicate-name explanation, required a production-grade project-wide decision, accepted the recommendation, and directed synchronization | Conceptual distinction reviewed; no practical execution | No | Career merge `ab1a68e...`; UpgradePilot merge `6fa34eaa...`; ADR-0001 |
| UpgradePilot implementation | No accepted implementation | — | Ali rejected premature scaffold | Active-tree absence verified | No | Repository state |

## 8. Evidence register

| Evidence ID | Date | Source/artifact | Revision/snapshot | What it supports | What it does not prove | State | Link/path |
|---|---|---|---|---|---|---|---|
| GOV-001 | 2026-07-19 | UpgradePilot charter and approved controls | Current `main` | Mission, boundary, route, learning and evidence controls | Product implementation or capability ownership | Accepted | Repository governing files |
| CASE-001 | 2026-07-19 | `pydantic/pydantic#13432` | Base `652a61c`; head `aa2dc02` | Selected real case and visible lockfile update | Correct recommendation or objective safety | Accepted for session input | Public PR |
| CASE-002 | 2026-07-19 | UP-S01 manual evidence report | Career commit `3519a8aa651073eec1ed2ca14c82a07f624b7158` | M1 evidence matrix, weak decision, limitations, changed variant, assistance | Independent ownership or universal compatibility | Accepted | `evidence/UP-S01_pydantic-13432_manual-evidence-report.md` |
| REPO-001 | 2026-07-19 | UP-S01 working memory | UpgradePilot closure `a9006506...` | Actual session sequence and instructional correction | Canonical gate status by itself | Accepted | UpgradePilot working memory |
| REPO-002 | 2026-07-19 | Former AI architecture files | Preserved in Git history and audit commits; removed from active tree by UpgradePilot merge `6fa34eaa...` | Evidence of premature unowned design and later correction | Current architecture, implementation authority, or Ali ownership | Historical evidence only | Git history; UpgradePilot M2-entry audit |
| REPO-003 | 2026-07-19 | M2-entry architecture-status audit | UpgradePilot closure `5999bed2...` | Correction of false status/ownership and implementation-free active tree | M2 implementation capability | Accepted | UpgradePilot M2-entry working memory |
| PLAN-001 | 2026-07-20 | M2-S01 plan | Career merge `ab1a68e02e8c348d2a766c9dc8d7c1d55af464d3` | Active bounded responsibility, accepted source boundary, teaching sequence, tests, ownership gate, forbidden scope | Completed implementation or complete architecture | Accepted and controlling active session | `../plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md` |
| ARCH-DEC-001 | 2026-07-20 | Initial Python source-layout decision | UpgradePilot merge `6fa34eaa273e381637917080fdb66989bd077f97` | Selected repository/distribution/import-package names, `src` boundary, minimal metadata, deferred architecture, reassessment triggers | Practical packaging capability, working imports, or permanent architecture | Accepted decision; implementation unproven | UpgradePilot `docs/architecture/ADR-0001-initial-python-source-layout.md` |
| REPO-004 | 2026-07-20 | M2-S01 active working record | UpgradePilot merge `6fa34eaa273e381637917080fdb66989bd077f97` | Actual session activation, progress, source-layout challenge, stop line, and exact continuation | Passed behavior gate or implementation behavior | Active | UpgradePilot `working-memory/2026-07-20_M2-S01_case-identity-normalization.md` |
| LEARN-001 | 2026-07-20 | Case identity, validation, normalization, and source-boundary review note | UpgradePilot merge `6fa34eaa273e381637917080fdb66989bd077f97` | Concise durable mental model for later review | Mastery, accepted code, or passed tests | Accepted as learning aid | UpgradePilot `learning/concepts/case-identity-validation-and-normalization.md` |

## 9. Decision register

| Decision ID | Date | Decision | Evidence/rationale | Status | Revisit trigger |
|---|---|---|---|---|---|
| DEC-001 | 2026-07-19 | UpgradePilot selected | Governing charter and formal project audit | Adopted | Charter reframe criteria only |
| DEC-002 | 2026-07-19 | Deterministic-first, manual evidence before automation | Capability readiness and ownership risk | Adopted | M1 pass enables M2 |
| DEC-003 | 2026-07-19 | Use `pydantic/pydantic#13432` for UP-S01 | Bounded case with release and CI evidence | Adopted for M1 | Public evidence unavailable or case unsuitable |
| DEC-004 | 2026-07-19 | UP-S01 recommendation is `run targeted checks` | No material conflict; bounded silent Algolia-output uncertainty | Adopted for M1 report only | New evidence or support-policy change |
| DEC-005 | 2026-07-19 | Pass M1 and prepare M2 using the same case | Report gate and conservative guided evidence complete | Adopted | M2 evidence shows case unsuitable |
| DEC-006 | 2026-07-19 | Former AI architecture has no authority and is not an implementation baseline | Prior scaffold was AI-generated and unowned; audit removed false claims | Adopted | None; later decisions must be derived fresh |
| DEC-007 | 2026-07-19 | Start M2 with case-identity normalization | Identity fields are stable M1 inputs and provide a small validation/testing responsibility | Adopted for M2-S01 | Session diagnostic shows prerequisite or representation scope is unsuitable |
| DEC-008 | 2026-07-20 | Adopt `src/upgradepilot/` as the initial source-layout baseline | Provides a professional namespace and installed-package boundary for a growing Python project while avoiding speculative internal layers | Adopted for M2 and subsequent growth | Observed import, packaging, distribution, interface, or module-cohesion limitation |
| DEC-009 | 2026-07-20 | Keep product/repository name `UpgradePilot` and use `upgradepilot` for distribution/import naming | Branding/workspace and Python namespace are distinct layers; renaming the repository or inventing another package name adds no technical value | Adopted | External distribution-name conflict or product identity change |

Technology decisions must use `adopt | retain as pilot | reject | defer` and include a simpler baseline and rejection condition.

## 10. Blocker register

| Blocker ID | Date | Milestone | Type | Expected | Actual | Evidence | Smallest next action | Status |
|---|---|---|---|---|---|---|---|---|
| ARCH-001 | 2026-07-19 | M2 entry | Scope/ownership failure | No architecture accepted before Ali learns, directs, reviews, and owns bounded responsibilities | Prior AI files falsely claimed accepted/active/Ali-owned status | Corrected files and M2-entry audit | Invalidate prior decisions and verify active tree | Resolved 2026-07-19 |
| ARCH-002 | 2026-07-20 | M2-S01 | Source-boundary ambiguity | Select a professional initial package boundary without pre-creating the full system | Temporary-layout framing obscured long-term repository growth and import namespace requirements | Ali challenge, technical comparison, Career merge `ab1a68e...`, UpgradePilot merge `6fa34eaa...` | Close the behavior gate and begin bounded implementation | Resolved 2026-07-20 |

## 11. Evaluation and corpus register

This section remains inactive until M5.

| Evaluation version | Corpus version | Calibration cases | Held-out cases | Adjudication method | Baseline | Metrics | Main limitations | Status |
|---|---|---:|---:|---|---|---|---|---|
| — | — | 0 | 0 | — | — | — | No corpus yet | Not started |

Do not use merged/closed status as direct ground truth.

## 12. Advanced-systems exposure register

A0–A4 is separate from D0–D5.

| Area | Current exposure | Target | Representative workload | Baseline | Failure/recovery evidence | Decision | Permitted claim |
|---|---|---|---|---|---|---|---|
| Distributed queues | A0 | A1; A2 target if justified | Not selected | Synchronous core | — | Not started | None |
| Advanced MLOps | A0 | A1; A2 target when valid | Not selected | Reproducible local experiment | — | Not started | None |
| Microservices | A0 | A1 | Not selected | Modular single application | — | Not started | None |
| Kubernetes | A0 | A1 | Not selected | Local/container runtime | — | Not started | None |
| Multi-cloud | A0 | A1 | Not selected | One local/provider path | — | Not started | None |
| Multi-agent systems | A0 | A1 | Not selected | Deterministic/single-agent investigation | — | Not started | None |

## 13. Weekly review register

| Week | Dates | Planned direction | Focused hours | Gate result | Primary evidence | Ownership evidence | Carry item |
|---:|---|---|---:|---|---|---|---|
| 1 | Jul 20–26 | Pass M1 and begin M2 | Not reliably measured yet | M1 Pass; architecture audit Pass; M2-S01 Active; source layout accepted and synchronized | M1 report, audits, active plan/record, ADR-0001 | Guided pre-code reasoning and design participation; independent implementation absent | Close behavior gate and begin package/test-first implementation |
| 2 | Jul 27–Aug 2 | Close M2 and Day-14 review | 0 | Not started | — | — | — |
| 3–4 | Aug 3–16 | M3 | 0 | Not started | — | — | — |
| 5–6 | Aug 17–30 | M4 | 0 | Not started | — | — | — |
| 7–8 | Aug 31–Sep 13 | M5 | 0 | Not started | — | — | — |
| 9–10 | Sep 14–27 | M6 | 0 | Not started | — | — | — |
| 11–12 | Sep 28–Oct 11 | M7 | 0 | Not started | — | — | — |
| 13 | Oct 12–17 | M8 | 0 | Not started | — | — | — |

## 14. Formal review register

| Review | Date | Status | Required decision evidence |
|---|---|---|---|
| Planning closure | 2026-07-19 | Pass | Required artifacts approved; first session ready |
| M1 gate review | 2026-07-19 | Pass | Manual report, evidence states, changed case, limitations, conservative assistance/ownership |
| M2-entry architecture review | 2026-07-19 | Pass | False status/ownership invalidated; active implementation absent; no former AI decision controls current work |
| M2 initial source-layout review | 2026-07-20 | Pass — decision only | Professional source/package boundary, synchronized ADR, deferred internal architecture, explicit reassessment triggers, conservative ownership |
| Day 14 | 2026-08-02 | Not started | G1/G2 delivery density, ownership, workload, planning-stop evidence |
| Day 30 | 2026-08-18 | Not started | Evidence system, persistence, SQL, testing, diagnosis |
| Day 60 | 2026-09-17 | Not started | Context/evaluation validity; ML, graph, LLM, MLOps admission decisions |
| Day 90 | 2026-10-17 | Not started | Supported product, ownership, evaluation, exposure, portfolio claims |

## 15. Current activation decision

**M1:** Pass with narrow D2 guided evidence and substantial AI assistance.  
**M2-entry architecture audit:** Pass; former AI-generated architecture has no current authority and has been removed from the active UpgradePilot tree.  
**Initial source-layout baseline:** Accepted and synchronized as `src/upgradepilot/` with a minimal future root `pyproject.toml` and `tests/`; no complete internal architecture is claimed.  
**M2-S01:** Active; pre-code onboarding is in progress.  
**Technical implementation authorization:** Limited to the behavior and stop lines in `UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md`; source/package creation remains blocked only until the integrated behavior gate passes.  
**Accepted implementation:** None.  
**Accepted architecture:** Initial source/package boundary only; internal architecture undecided.  
**Exact next action:** Close the integrated behavior gate, then create the minimal installable package boundary and write the valid test first.