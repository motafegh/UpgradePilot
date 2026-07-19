# UpgradePilot 90-Day Master Roadmap

**Owner:** Ali Rajabi  
**Recorded:** 2026-07-19  
**Execution period:** 2026-07-20 to 2026-10-17  
**Status:** Approved and controlling master roadmap  
**Authority:** Schedules the UpgradePilot route under `../UpgradePilot.md`, the approved capability specification, and the approved Learning and Execution Contract  
**Activation effect:** Controls stage order, capacity, reviews, fallbacks, and Day-90 outcomes. Technical execution is active only through approved milestone and session/weekly packages.

## 1. Purpose

This roadmap converts the approved UpgradePilot charter into one bounded 90-day route.

It controls:

- the order in which product capability develops;
- the maximum planning hold before real evidence work begins;
- stage-level outcomes and hard gates;
- capacity allocated to the supported core, evaluation, learned methods, advanced-systems exposure, and closure;
- formal review points and fallback decisions;
- what must exist by Day 90;
- what remains forbidden.

This roadmap does not select permanent frameworks, database products, cloud providers, model families, queue products, orchestration tools, or implementation architecture. Those decisions require observed need and the admission rules in the governing charter and Learning and Execution Contract.

## 2. Governing authorities

Read conflicts in this order:

1. safety, legal, privacy, credential, health, cost, and platform constraints;
2. `../governance/EXECUTION_CONTRACT.md`;
3. `../strategy/STRATEGY_AND_SCOPE.md`;
4. `../UpgradePilot.md`;
5. `../strategy/UPGRADEPILOT_CAPABILITY_AND_PREREQUISITE_SPECIFICATION.md`;
6. `../governance/UPGRADEPILOT_LEARNING_AND_EXECUTION_CONTRACT.md`;
7. this roadmap;
8. `UPGRADEPILOT_STAGED_MILESTONE_PLAN.md` and the active weekly/session package;
9. `../tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md`;
10. `../operations/SESSION_PROTOCOL.md`;
11. current inspected evidence and technical state.

A later milestone or weekly file may add exact deliverables but may not reorder the route, weaken a gate, expand the frozen product boundary, or silently adopt a technology.

## 3. Fixed execution principles

The route follows these rules:

- one primary mission: evidence-backed dependency-update decisions for maintainers of public Python repositories reviewing Dependabot pull requests;
- one continuous flow from real PR evidence to a traceable recommendation or abstention;
- deterministic and provenance-backed behavior before learned or agentic methods;
- a modular single-application baseline before service extraction;
- one main persistence system when persistence becomes necessary;
- real public evidence, explicit missing states, and no manufactured certainty;
- teaching around active product needs rather than detached courses;
- increasing Ali ownership of central behavior;
- one major advanced-systems package at a time;
- negative experiments may pass when the method and rejection decision are rigorous;
- documentation ends when it is sufficient to execute, reproduce, evaluate, or defend the work.

## 4. Capacity model

### 4.1 Standard capacity

- Monday–Saturday: 4 focused hours per Green day.
- Standard full week: 24 focused hours.
- Final partial week: 24 focused hours across 2026-10-12 to 2026-10-17.
- Standard 90-day technical and planning capacity: approximately **312 focused hours** before approved capacity adjustments.

Hours are containers and ceilings. Stage gates, not elapsed hours, determine advancement.

### 4.2 Capacity allocation

| Allocation | Planned capacity | Purpose |
|---|---:|---|
| Planning closure and first manual evidence flow | 12 hours | Close remaining authorized artifacts and complete G1 quickly |
| First automated flow and core engineering | 84 hours | G2 and G3: runnable slice, acquisition, validation, provenance, persistence, tests |
| Repository-specific context | 48 hours | G4: dependency declarations, paths, usage, tests, workflows, limitations |
| Deterministic baseline and evaluation | 48 hours | G5: corpus, rubric, held-out evaluation, error analysis |
| Learned, graph, LLM, and advanced-lifecycle decisions | 48 hours | G6 and admitted portions of G7; includes conditional MLOps work |
| Advanced-systems exposure packages | 48 direct hours plus up to 24 embedded hours | A1 across six areas and A2 targets without displacing the core |
| Final hardening, portfolio, ownership, and market closure | 24 hours | G10 and Day-90 evidence package |

Advanced-systems work therefore receives approximately **64–72 hours**, about 20–23% of standard capacity, including MLOps or agent work embedded in the analytical stages.

### 4.3 Capacity protection

When time is lost or a stage overruns:

1. preserve the supported core and evidence integrity;
2. reduce optional polish;
3. narrow experimental breadth before weakening evaluation;
4. retain A1 exposure through smaller representative workloads;
5. reduce an A2 target to A1 only through an explicit review decision;
6. do not hide missed gates by relabeling partial work as complete.

## 5. Route overview

| Route | Dates | Maximum focused capacity | Governing capability gate | Primary outcome | Current status |
|---|---|---:|---|---|---|
| R0 — Planning closure | Jul 20 | 4 h | Pre-execution authorization | Remaining execution artifacts approved; no further planning hold | Pass |
| R1 — Manual evidence reality | Jul 20–22 | 8 h | G1 | One real Dependabot PR becomes a traceable manual evidence package and weak decision report | Ready |
| R2 — First automated vertical slice | Jul 23–Aug 2 | 36 h | G2 | One reproducible input-to-report path with tests and an Ali-owned changed case | Not started |
| R3 — Reliable evidence system | Aug 3–16 | 48 h | G3 | Reliable acquisition, validation, provenance, replay behavior, relational persistence, and diagnostics | Not started |
| R4 — Repository-specific context | Aug 17–30 | 48 h | G4 | Dependency declaration, path, usage, test, workflow, and explicit reachability evidence | Not started |
| R5 — Deterministic baseline and evaluation | Aug 31–Sep 13 | 48 h | G5 | Versioned baseline, staged corpus, adjudication rules, held-out evaluation, error analysis | Not started |
| R6 — Contextual, learned, graph, and grounded-AI decisions | Sep 14–27 | 48 h | G6 and admitted G7 work | Measured experiments or rigorous rejection decisions against the baseline | Not started |
| R7 — Advanced-systems pilots and operational comparison | Sep 28–Oct 11 | 48 h | G7–G9 | Required A1 exposures, targeted A2 pilots, failure/recovery evidence, adoption decisions | Not started |
| R8 — Final ownership and portfolio closure | Oct 12–17 | 24 h | G10 | Reproducible final system, evidence package, limitations, ownership defense, portfolio and market calibration | Not started |

The staged milestone plan may split these route blocks into smaller milestones but may not create a longer planning preface before R1.

## 6. R0 — Planning closure

**Date:** 2026-07-20  
**Maximum:** 4 focused hours

Required closure artifacts:

- approved staged milestone plan;
- approved UpgradePilot evidence and progress tracker;
- approved first-session plan.

Gate R0 passes when:

- each artifact exists and agrees with the charter, capability specification, contract, and this roadmap;
- the first session names one real public Python Dependabot PR and one exact manual evidence output;
- no implementation architecture, corpus campaign, model experiment, or infrastructure package has been started;
- technical execution can begin without another planning document.

**Result:** Pass. The three artifacts are approved, repository entry points are synchronized, and UP-S01 is ready.

**Hard stop:** Planning has stopped. G1 begins with the active first-session plan. New planning files require explicit authority.

## 7. R1 — Manual evidence reality

**Dates:** 2026-07-20 to 2026-07-22  
**Maximum:** 8 focused hours  
**Gate:** G1

User-visible outcome:

> Given one real public Python Dependabot pull request, produce a traceable evidence package and a weak manual recommendation, targeted-check request, defer decision, investigation/block decision, or abstention.

Required evidence categories:

- PR identity, base/head revisions, and changed files;
- package, previous version, proposed version, and declaration or lock context;
- direct, transitive, optional, or unresolved status;
- available package and release evidence;
- available CI and repository evidence within the case boundary;
- source identity, retrieval time, and snapshot/revision;
- observed, inferred, missing, inaccessible, stale, conflicting, invalid, accepted, and rejected states where applicable;
- recommendation and limitations;
- AI-assistance and Ali-ownership record.

Gate R1 passes when Ali can explain the change, trace each material claim to evidence, state what the evidence does not prove, and respond correctly to one changed or missing-evidence variant.

Not required:

- implementation repository;
- database or SQL;
- automated multi-source acquisition;
- corpus construction;
- repository-wide static analysis;
- ML, graphs, LLMs, agents, queues, microservices, Kubernetes, cloud, or MLOps.

## 8. R2 — First automated vertical slice

**Dates:** 2026-07-23 to 2026-08-02  
**Maximum:** 36 focused hours  
**Gate:** G2

User-visible outcome:

> One real PR input reaches one reproducible machine-produced evidence report through a bounded interface.

The stage must establish only the smallest application structure needed for:

- input identity;
- bounded acquisition or accepted manual input;
- raw preservation;
- normalized evidence contracts;
- explicit evidence states;
- a weak deterministic decision path;
- a human-readable and machine-readable report;
- central tests and changed-case behavior;
- secure configuration and no embedded credentials.

Gate R2 passes when:

- one clean execution reproduces the vertical slice;
- central transformation and decision behavior have tests;
- one malformed, missing, or conflicting case degrades explicitly;
- Ali materially modifies a central responsibility and diagnoses one changed or failing case;
- assistance and limitations are recorded.

No permanent framework, database, service, queue, cloud, or model decision is required here.

## 9. R3 — Reliable evidence system

**Dates:** 2026-08-03 to 2026-08-16  
**Maximum:** 48 focused hours  
**Gate:** G3

Primary outcomes:

- lawful, bounded acquisition for supported GitHub and package/release evidence;
- raw and normalized records with provenance;
- explicit partial-source failure;
- pagination, rate-limit, retry, backoff, caching, and idempotency behavior only where real supported sources require them;
- one relational persistence system and reproducible schema setup;
- central SQL queries for traceability and run comparison;
- replay or duplicate behavior;
- structured errors and logs;
- unit, integration, failure-path, and recovery tests;
- CI after the local supported slice is stable.

Gate R3 passes when one case can be reacquired or replayed without hidden duplication, each report claim resolves to persisted evidence, source failure remains visible, and Ali can query and diagnose the central path.

Docker may enter when it measurably improves reproducibility. It is not mandatory merely because the stage is operational.

## 10. R4 — Repository-specific context

**Dates:** 2026-08-17 to 2026-08-30  
**Maximum:** 48 focused hours  
**Gate:** G4

Primary outcomes:

- identify supported Python dependency declaration and lockfile formats from real cases;
- distinguish direct, transitive, optional, runtime, development, and unresolved relationships;
- construct reproducible dependency paths within declared limits;
- inspect repository imports, references, tests, and workflows relevant to the updated package;
- preserve evidence locations and revisions;
- state static-analysis and reachability limitations explicitly;
- compare repository-context evidence with the weaker PR/package-only view.

Gate R4 passes when representative cases show traceable repository-specific context, missing or dynamic paths remain explicit, and the system does not claim runtime causality from static evidence.

Whole-program static analysis, universal resolver support, dynamic execution of untrusted repositories, and graph neural networks remain deferred.

## 11. R5 — Deterministic baseline and evaluation

**Dates:** 2026-08-31 to 2026-09-13  
**Maximum:** 48 focused hours  
**Gate:** G5

Primary outcomes:

- versioned deterministic decision table;
- explicit evidence-sufficiency and abstention rules;
- asymmetric decision-cost assumptions;
- staged case corpus built from public evidence;
- calibration cases and a frozen held-out subset;
- documented adjudication rubric;
- disagreement and unadjudicable states;
- contamination and leakage controls;
- metrics with denominators and confidence limitations;
- error analysis by evidence and recommendation failure type;
- comparison between weak baseline and repository-context method.

Gate R5 passes when the baseline and contextual method can be reproduced on the frozen evaluation set, errors are inspectable, label limitations are explicit, and no historical PR outcome is treated as objective truth.

A learned method is not admitted merely because R5 exists. The label and target audit decides admission.

## 12. R6 — Contextual, learned, graph, and grounded-AI decisions

**Dates:** 2026-09-14 to 2026-09-27  
**Maximum:** 48 focused hours  
**Gate:** G6 and admitted portions of G7

### 12.1 Required decision sequence

1. identify the strongest remaining baseline failure;
2. define the smallest contextual, learned, structural, or synthesis hypothesis;
3. freeze success and rejection conditions;
4. compare against the deterministic baseline on held-out evidence;
5. inspect high-cost errors, calibration or selective behavior, latency, cost, and maintainability;
6. adopt, retain as pilot, reject, or defer.

### 12.2 Learned-method path

A model may be fitted only when the target, labels, split, and sample support a defensible experiment.

Possible bounded outcomes:

- recommendation classification;
- investigation-priority ranking;
- selective prediction with abstention;
- a negative feasibility result.

A weak or invalid label foundation closes the recommendation-model path. It does not trigger manufactured labels or optimistic metrics.

### 12.3 Graph path

A graph experiment requires a reproducible structural representation and a measured limitation of flat features. Basic dependency-path features precede advanced graph learning.

### 12.4 Grounded LLM path

Grounded synthesis requires a specific report-comprehension limitation, source-constrained context, structured output, citation-entailment checks, unsupported-claim measurement, and comparison with a deterministic template.

### 12.5 MLOps embedding

When a defensible learned experiment exists, this stage may include up to 16–24 hours of MLOps A1/A2 work covering reproducible runs, data/code/model identity, experiment tracking, evaluation gates, controlled inference, and replacement or rejection.

When a model is not defensible, the MLOps requirement becomes a bounded negative lifecycle experiment or shifts through formal review to the approved fallback A2 area. No success claim is manufactured.

Gate R6 passes when every attempted method has reproducible evidence and an explicit adoption decision. A rigorous rejection may be the correct result.

## 13. R7 — Advanced-systems pilots and operational comparison

**Dates:** 2026-09-28 to 2026-10-11  
**Maximum direct capacity:** 48 focused hours  
**Gate:** G7–G9

The supported core remains the workload. Only one major package is active at a time.

### 13.1 Required exposure objectives

| Area | Minimum | Target |
|---|---|---|
| Distributed queues | A1 | A2 target if synchronous acquisition or analysis shows a real limitation |
| Advanced MLOps | A1 | A2 target when a defensible model/lifecycle question exists; otherwise approved fallback |
| Microservices | A1 | A2 only if independent lifecycle or isolation value is measurable |
| Kubernetes | A1 | A2 only when the representative workload creates an orchestration question |
| Multi-cloud | A1 | A2 only when portability or provider behavior becomes mission-relevant |
| Autonomous multi-agent systems | A1 | A2 only when separable investigation roles improve measured quality over simpler flows |

### 13.2 Package contract

Every package requires:

- representative UpgradePilot workload;
- simpler baseline;
- A1 or A2 target;
- prerequisite depth;
- time and scope ceiling;
- security, credential, privacy, cost, and cleanup boundary;
- one observable failure or degraded state;
- inspection, recovery, and cleanup;
- operational burden measurement;
- Ali teach-back and ownership evidence;
- adopt, retain-as-pilot, reject, or defer decision;
- exact permitted portfolio claim.

### 13.3 Provisional sequence

1. distributed queue A1 and possible A2;
2. microservice-boundary A1 comparison;
3. Kubernetes A1 deployment of a representative workload;
4. multi-cloud A1 executable portability comparison;
5. bounded multi-agent A1 investigation;
6. remaining MLOps A1/A2 closure or approved fallback A2.

The staged milestone plan may reorder packages when prerequisites or real evidence require it, but it may not run several major packages simultaneously.

### 13.4 Fallback A2 rule

Primary A2 targets are distributed queues and advanced MLOps.

When MLOps A2 is invalid because no defensible learned lifecycle exists, the replacement A2 may be:

- one microservice extraction comparison; or
- one bounded multi-agent integrated comparison.

The replacement requires a formal recorded decision and may not weaken the core.

## 14. R8 — Final ownership and portfolio closure

**Dates:** 2026-10-12 to 2026-10-17  
**Maximum:** 24 focused hours  
**Gate:** G10

Required Day-90 package:

- clean reproducible supported-core execution;
- declared supported input and output boundary;
- representative real cases and failure cases;
- versioned deterministic baseline and evaluation results;
- contextual, learned, graph, LLM, and advanced-system adoption decisions;
- tests and CI appropriate to the supported behavior;
- secure configuration and public-safe evidence;
- operational setup, run, diagnosis, recovery, and cleanup instructions;
- limitations and claim register;
- AI-assistance disclosure;
- capability and ownership evidence;
- architecture and data-flow explanation based on the final system, not speculative design;
- concise demonstration for a technical reviewer;
- portfolio README and evidence index;
- market calibration against representative target roles;
- final review of what Ali can explain, modify, test, query, diagnose, and reject.

Gate R8 passes only when the final claims match the evidence. “Production-oriented” is allowed when supported; “production-ready,” “safe,” “enterprise-grade,” or “expert” requires evidence beyond this roadmap.

## 15. Weekly delivery map

This table communicates direction, not daily implementation detail.

| Week | Dates | Controlling delivery direction |
|---:|---|---|
| 1 | Jul 20–26 | Close planning, complete G1, begin first automated vertical slice |
| 2 | Jul 27–Aug 2 | Close G2; Day-14 workload and ownership review |
| 3 | Aug 3–9 | Reliable acquisition, raw/normalized evidence, validation, provenance |
| 4 | Aug 10–16 | Persistence, SQL diagnostics, replay, failure paths, CI; close G3 |
| 5 | Aug 17–23 | Dependency declarations, paths, repository usage, tests, workflows |
| 6 | Aug 24–30 | Context quality, static limitations, changed cases; close G4 |
| 7 | Aug 31–Sep 6 | Deterministic baseline, evidence sufficiency, corpus and rubric |
| 8 | Sep 7–13 | Held-out evaluation, leakage controls, metrics, error analysis; close G5 |
| 9 | Sep 14–20 | Learned/graph admission decisions and first bounded experiment; Day-60 review |
| 10 | Sep 21–27 | Experiment comparison, grounded synthesis, MLOps lifecycle decision; close G6 |
| 11 | Sep 28–Oct 4 | Queue A1/A2 and microservice A1 packages |
| 12 | Oct 5–11 | Kubernetes, multi-cloud, multi-agent, and remaining MLOps/fallback exposure closure |
| 13 | Oct 12–17 | Hardening, reproducibility, ownership defense, portfolio and Day-90 closure |

## 16. Formal review points

### 16.1 Day 14 — 2026-08-02

Review:

- whether G1 passed quickly;
- whether G2 has a real reproducible output;
- delivery density and workload realism;
- whether AI assistance is outrunning ownership;
- whether planning has actually stopped.

Allowed corrections: narrow G2, rebalance workload, repair a prerequisite, or clarify evidence. Do not reopen project selection casually.

### 16.2 Day 30 — 2026-08-18

Review:

- reliable evidence acquisition and preservation;
- data contracts and explicit degraded states;
- persistence and SQL progress;
- test and diagnosis quality;
- readiness for repository-context work.

A missing central G3 responsibility must be repaired before contextual complexity grows.

### 16.3 Day 60 — 2026-09-17

Review:

- whether G4 and G5 evidence are defensible;
- baseline quality and main error classes;
- label and target sufficiency for learned methods;
- which graph, LLM, MLOps, and advanced-system experiments are admitted;
- whether advanced capacity remains feasible without weakening the core.

This is the formal ML/MLOps admission or rejection point.

### 16.4 Day 90 — 2026-10-17

Review:

- supported product behavior;
- evaluation honesty;
- reliability and reproducibility;
- Ali ownership and capability depth;
- advanced exposure and adoption decisions;
- portfolio claims;
- market calibration;
- next 90-day direction based on evidence.

## 17. Fallback and reframe rules

### 17.1 Evidence availability

When historical CI logs or upstream evidence are unavailable:

- preserve the missing state;
- prefer recent cases;
- narrow claims;
- request targeted checks or abstain;
- do not replace evidence with retrospective assumptions.

### 17.2 Label insufficiency

When labels are not defensible:

- stop recommendation-model claims;
- preserve a deterministic product;
- consider ranking, selective prediction, or feasibility-only experiments;
- keep negative results;
- use the approved MLOps fallback rule.

### 17.3 External review unavailable

External maintainer review is valuable but not required for core completion. Use a declared internal rubric, separated calibration and held-out cases, independent second-pass review where possible, and explicit limitation language.

### 17.4 Capability gap larger than expected

Use the smallest prerequisite repair. When the gap exceeds the allowed repair and affects the active gate, narrow the responsibility or adjust sequence at a formal review. Do not replace the project with a general course.

### 17.5 Advanced-system overload

When advanced exposure threatens core completion or ownership:

- reduce package breadth;
- retain smaller A1 workloads;
- drop optional A2 expansion;
- preserve the two A2 target decisions through formal review;
- do not mislabel orientation as project-integrated capability.

### 17.6 Mission or feasibility failure

Apply the reframe and termination conditions in `../UpgradePilot.md`. Prefer the smallest necessary change. A failed technical hypothesis does not automatically terminate the mission.

## 18. Forbidden scope

This roadmap does not authorize:

- multiple programming ecosystems;
- non-GitHub hosting platforms;
- dependency bots other than Dependabot;
- private repository data as a core requirement;
- automatic merge, mutation, or repository write actions;
- generic vulnerability scanning;
- full CI diagnosis as a separate product;
- universal package-manager and lockfile support;
- executing arbitrary untrusted repository code;
- generalized static-analysis, agent, MLOps, queue, cloud, or platform products;
- multiple primary databases;
- service fleets or permanent multi-cloud architecture;
- production-readiness or safety claims without evidence;
- planning artifacts beyond approved active weekly/session packages and evidence-derived operational documentation.

## 19. Advancement and completion law

A route block advances only when:

- its user-visible or evaluation outcome exists;
- required evidence is preserved;
- limitations and assistance are explicit;
- Ali completes the required ownership check;
- no hidden failure is carried into the next dependency;
- the next route block does not rely on an unsupported claim.

When a gate passes early, continue to a named advancement item from the staged milestone plan. Do not pad time or invent scope.

When a gate does not pass by its ceiling, record Partial or Blocked, identify the smallest repair, and use the next formal review or explicit change-control process. Do not silently declare success.

## 20. Current activation

**Audit result:** Passed.  
**Approval result:** Approved and controlling master roadmap.  
**Planning route R0:** Pass.  
**Current route:** R1 — Manual evidence reality.  
**Current milestone:** M1 — First manual evidence decision.  
**Active session:** `UPGRADEPILOT_FIRST_SESSION_PLAN.md` / UP-S01.  
**Technical execution:** Authorized for the bounded active session.  
**Technical implementation:** Not started; M2 authorization follows M1.  
**Exact next action:** Start UP-S01.  
**No additional planning artifact is authorized before execution.**
