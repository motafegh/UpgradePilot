# UpgradePilot Staged Milestone Plan

**Owner:** Ali Rajabi  
**Recorded:** 2026-07-19  
**Execution period:** 2026-07-20 to 2026-10-17  
**Status:** Approved and controlling staged milestone plan  
**Authority:** Defines milestone entry, closure, evidence, ownership, and advancement under `../UpgradePilot.md`, the approved capability specification, Learning and Execution Contract, and `UPGRADEPILOT_90_DAY_MASTER_ROADMAP.md`  
**Activation effect:** This plan controls the milestone sequence and gates. Technical execution is active only through approved milestone and session/weekly packages.

## 1. Purpose

This plan converts the approved 90-day route into bounded product milestones.

A milestone describes:

- the user-visible or evaluation outcome;
- the minimum entry state;
- exact evidence required to pass;
- Ali ownership evidence;
- what may remain weak;
- stop and rejection conditions;
- the next authorized milestone.

It is not:

- a technology curriculum;
- a detailed architecture;
- a framework-selection document;
- a substitute for active session plans;
- permission to skip evidence or ownership gates.

## 2. Governing order

When instructions conflict, use:

1. safety, legal, privacy, health, credential, cost, and platform constraints;
2. `../governance/EXECUTION_CONTRACT.md`;
3. `../strategy/STRATEGY_AND_SCOPE.md`;
4. `../UpgradePilot.md`;
5. `../strategy/UPGRADEPILOT_CAPABILITY_AND_PREREQUISITE_SPECIFICATION.md`;
6. `../governance/UPGRADEPILOT_LEARNING_AND_EXECUTION_CONTRACT.md`;
7. `UPGRADEPILOT_90_DAY_MASTER_ROADMAP.md`;
8. this plan;
9. the active evidence/progress tracker and first-session or later weekly/session plan;
10. `../operations/SESSION_PROTOCOL.md`;
11. current inspected evidence.

A lower-level plan may divide work but may not weaken a milestone gate, expand the product boundary, or silently adopt a technology.

## 3. Milestone law

A milestone passes only when:

- its required behavior or decision exists;
- evidence is preserved and linked;
- material limitations are explicit;
- AI assistance is labeled;
- Ali completes the required explanation, modification, test, query, or diagnosis;
- negative or missing evidence is not hidden;
- no unsupported claim is carried forward.

A date or hour ceiling does not create a pass. A rigorous rejection or negative experiment may pass when that is the stated milestone outcome.

When a milestone passes early, proceed to its named advancement item. Do not pad time or invent scope.

## 4. Milestone overview

| Milestone | Roadmap route | Outcome | Maximum route capacity | Current status |
|---|---|---|---:|---|
| M0 — Planning closure | R0 | All execution-control artifacts active; technical execution authorized | 4 h | Pass |
| M1 — First manual evidence decision | R1 / G1 | One real Dependabot PR becomes a traceable manual evidence package and weak decision report | 8 h | Ready |
| M2 — First automated vertical slice | R2 / G2 | One reproducible PR-to-report path with tests and changed-case evidence | 36 h | Not started |
| M3 — Reliable evidence and persistence | R3 / G3 | Supported acquisition, validation, provenance, relational persistence, replay, SQL, failure behavior, and CI | 48 h | Not started |
| M4 — Repository-specific dependency context | R4 / G4 | Traceable declaration, path, usage, test, workflow, and limitation evidence | 48 h | Not started |
| M5 — Deterministic baseline and evaluation | R5 / G5 | Versioned baseline, staged corpus, adjudication rubric, held-out evaluation, and error analysis | 48 h | Not started |
| M6 — Evidence-gated analytical experiments | R6 / G6–G7 | Learned, graph, or grounded-LLM experiments are measured or rigorously rejected | 48 h | Not started |
| M7 — Advanced-system exposure and pilots | R7 / G7–G9 | A1 exposure across six areas and justified A2 pilots with operational comparisons | 48 direct h | Not started |
| M8 — Final ownership and portfolio closure | R8 / G10 | Reproducible supported core, evidence index, ownership defense, portfolio, and market calibration | 24 h | Not started |

## 5. M0 — Planning closure

### Outcome

The project can begin G1 without another planning artifact.

### Must exist

- this staged milestone plan;
- `../tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md`;
- `UPGRADEPILOT_FIRST_SESSION_PLAN.md`;
- repository entry points naming the first session as the next action.

### Pass condition

- all three artifacts are approved and mutually consistent;
- the first session names one real public Python Dependabot PR;
- no implementation, architecture, corpus campaign, model experiment, or infrastructure package was started during planning;
- the tracker records M1 as Ready and the first session as Ready.

### Result

**Pass.** All required artifacts are approved and entry points identify UP-S01 as the next action.

### Next action

Execute `UPGRADEPILOT_FIRST_SESSION_PLAN.md`.

## 6. M1 — First manual evidence decision

### User-visible outcome

> For one real public Python Dependabot pull request, produce a traceable evidence package and a weak recommendation to merge after normal review, run targeted checks, investigate or block, defer, or abstain.

### Entry requirements

- D1 recognition of the read-only boundary;
- D1 distinction between observation, inference, missing evidence, and unsupported claims;
- safe public-repository navigation;
- active first-session plan.

No standalone prerequisite course is required.

### Must deliver

1. PR identity, URL, base/head revisions, author/bot identity, state, and changed files.
2. Updated package, old version, proposed version, and declaration/lock context.
3. Direct, transitive, optional, development, runtime, or unresolved classification with evidence and uncertainty.
4. Relevant upstream release evidence.
5. Available repository and CI evidence within the bounded case.
6. Source identity, retrieval time, revision/snapshot, and evidence-state classification.
7. A weak decision report with material claims linked to evidence.
8. Explicit limitations and what the evidence does not prove.
9. AI-assistance and Ali-ownership record.
10. One changed or missing-evidence variant.

### Pass condition

Ali can:

- explain the diff and what it does not establish;
- identify the dependency change and declaration context;
- trace every material factual claim;
- distinguish observation from interpretation;
- explain why merged status, SemVer, compatibility scores, or passing CI are not objective safety proof;
- produce or challenge the weak recommendation;
- respond to one changed evidence condition without fabricating certainty.

Minimum milestone depth is narrow D2 guided application for C01, C05, C06, C09, C11, and relevant C17 boundaries.

### What may remain weak

- Python implementation;
- SQL and persistence;
- automated acquisition;
- repository-wide context;
- evaluation corpus;
- ML, graph, LLM, agents, queues, services, Kubernetes, cloud, and MLOps.

### Stop conditions

- the report gate passes;
- the eight-hour route ceiling is reached;
- required public evidence is inaccessible and the report must abstain;
- the case proves unsuitable, in which case record why and select one replacement case through the same bounded milestone.

### Advancement

Begin M2 using the same case unless evidence shows it is unsuitable for a minimal automated slice.

## 7. M2 — First automated vertical slice

### User-visible outcome

> One real PR input reaches one reproducible machine-produced evidence report through a bounded interface.

### Entry requirements

- M1 passed;
- C03, C04, C07, C09, and C11 at D1 or teachable D2 scope;
- the selected input and report contract are preserved.

### Must deliver

- the smallest understandable Python application/package structure;
- one bounded input contract;
- raw-input preservation;
- normalized evidence representation;
- explicit missing, invalid, conflicting, accepted, and rejected states as needed;
- a weak deterministic decision path;
- human-readable and machine-readable output;
- tests for central transformation and decision behavior;
- one malformed, missing, or conflicting case;
- secure configuration with no embedded token;
- reproducible run instructions;
- one Ali-owned central change and one diagnosed changed/failing case.

### Pass condition

A clean run reproduces the vertical slice; central tests pass; degraded evidence remains visible; Ali can locate, modify, test, and explain the central path.

### Forbidden expansion

No database, web service, queue, cloud deployment, ML model, graph model, agent system, or permanent framework decision is required merely to pass M2.

### Advancement

Begin M3 with only the supported sources and behaviors proven by M2.

## 8. M3 — Reliable evidence and persistence

### Outcome

The supported evidence flow can be acquired or replayed, validated, persisted, queried, diagnosed, and reproduced without hiding source failure.

### Entry requirements

- M2 passed;
- bounded supported source list;
- C07–C10 and C17 at D2 entry depth or bounded repair scope.

### Must deliver

- lawful GitHub and package/release acquisition for supported fields;
- raw and normalized records with provenance;
- explicit partial-source failure;
- rate-limit, pagination, retry, backoff, caching, or idempotency only where required by supported sources;
- one relational persistence system;
- reproducible schema setup or migrations;
- SQL queries tracing report claims and comparing runs;
- replay/duplicate behavior;
- structured errors and logs;
- unit, integration, failure-path, and recovery tests;
- CI after the local path is stable;
- Docker only when evidence shows it improves reproducibility.

### Pass condition

One case can be reacquired or replayed without hidden duplication; each report claim resolves to persisted evidence; source failures remain explicit; Ali can run central queries and diagnose one persistence or acquisition failure.

### Advancement

Begin M4 only after the evidence contract and persistence path are stable enough to support repository-context records.

## 9. M4 — Repository-specific dependency context

### Outcome

UpgradePilot adds reproducible repository-specific dependency and usage evidence without claiming runtime causality it cannot establish.

### Entry requirements

- M3 passed;
- supported declaration/lock formats selected from actual cases;
- C05, C06, and C13 at D2; C14 at D1.

### Must deliver

- declaration and lock evidence;
- direct/transitive/optional/runtime/development/unresolved classification;
- reproducible dependency paths;
- relevant imports, references, tests, and workflows;
- source locations and revisions;
- explicit dynamic, static, resolver, and reachability limitations;
- comparison with the weaker PR/package-only view;
- representative missing or dynamic-path case.

### Pass condition

Representative cases contain traceable context; limitations remain visible; the system does not convert static reachability into runtime proof; Ali can locate evidence and explain one missed path.

### Advancement

Freeze the supported context method and begin M5 evaluation.

## 10. M5 — Deterministic baseline and evaluation

### Outcome

A versioned, reproducible deterministic baseline and repository-context method can be evaluated honestly on staged cases.

### Entry requirements

- stable M3/M4 evidence contracts;
- C11 and C12 at D2;
- a declared case acquisition and adjudication process.

### Must deliver

- versioned decision table;
- evidence-sufficiency and abstention rules;
- asymmetric-cost assumptions;
- calibration cases and frozen held-out subset;
- adjudication rubric;
- disagreement and unadjudicable states;
- contamination and leakage controls;
- metrics with denominators and uncertainty;
- error analysis by evidence and recommendation failure type;
- comparison of weak baseline and contextual method;
- explicit label-quality audit.

### Pass condition

Evaluation is reproducible; historical disposition is not treated as objective truth; high-cost errors and limitations are inspectable; Ali can explain the rubric, split, metrics, and main failure classes.

### Advancement

Run the analytical-method admission decision. A weak label foundation may close the recommendation-model path while preserving the core product.

## 11. M6 — Evidence-gated analytical experiments

### Outcome

Each attempted learned, graph, or grounded-LLM method has a bounded hypothesis, baseline comparison, reproducible evidence, and adopt/reject/defer decision.

### Entry requirements

- M5 passed;
- target and labels audited;
- measured deterministic baseline;
- relevant capability prerequisites at D2;
- success and rejection conditions frozen.

### Candidate paths

- simple recommendation classification;
- investigation-priority ranking;
- selective prediction and abstention;
- dependency-path or structural features;
- grounded report synthesis with citation-entailment checks;
- negative feasibility result.

### Must deliver for each admitted path

- hypothesis and observed limitation;
- frozen comparison method;
- data/feature or prompt/context identity;
- leakage-aware split or case separation;
- held-out results;
- high-cost error analysis;
- cost, latency, maintainability, and ownership evidence;
- adopt, retain-as-pilot, reject, or defer decision.

### MLOps rule

MLOps work enters only around a defensible learned lifecycle or an explicitly bounded negative lifecycle experiment. It cannot manufacture a model-success claim.

### Pass condition

Every attempted method has reproducible evidence and a valid decision. A rigorous rejection passes.

### Advancement

Use the supported core as the workload for M7 advanced-system packages.

## 12. M7 — Advanced-system exposure and pilots

### Outcome

Ali obtains project-connected hands-on evidence across the six required areas and project-integrated A2 evidence where justified.

### Required areas

- distributed queues;
- advanced MLOps;
- microservices;
- Kubernetes;
- multi-cloud;
- bounded autonomous multi-agent systems.

### Entry requirements

Each package must satisfy the capability specification and Advanced Systems Exposure and Adoption Policy prerequisites. Only one major package is active at a time.

### Every package must deliver

- representative UpgradePilot workload;
- simpler baseline;
- A1 or A2 target;
- scope and time ceiling;
- security, credential, privacy, cost, and cleanup boundary;
- one observable failure or degraded state;
- inspection, recovery, and cleanup;
- operational burden comparison;
- Ali teach-back and ownership evidence;
- adopt, retain-as-pilot, reject, or defer decision;
- exact permitted portfolio claim.

### A2 targets

Primary targets are:

1. distributed queues;
2. advanced MLOps when a defensible learned lifecycle exists.

When MLOps A2 is invalid, a formally recorded fallback may use one microservice extraction comparison or one bounded multi-agent integrated comparison.

### Pass condition

All six areas have valid A1 evidence or a formally documented infeasibility boundary; at least two A2 decisions are completed unless formal capacity review narrows the requirement; no exposure package weakens the supported core.

### Advancement

Begin M8 final closure with all adoption and rejection decisions frozen.

## 13. M8 — Final ownership and portfolio closure

### Outcome

A technical reviewer can reproduce the supported product, inspect its evidence and evaluation, understand its limitations, and verify Ali's ownership claims.

### Must deliver

- clean supported-core execution;
- declared input/output boundary;
- representative real and failure cases;
- versioned baseline and evaluation results;
- analytical and advanced-system decisions;
- tests and CI appropriate to supported behavior;
- secure configuration and public-safe evidence;
- setup, run, diagnosis, recovery, and cleanup instructions;
- limitations and claim register;
- AI-assistance disclosure;
- capability and ownership evidence;
- final architecture and data-flow explanation based on implemented reality;
- concise reviewer demonstration;
- portfolio README and evidence index;
- market calibration against representative target roles.

### Pass condition

All final claims match preserved evidence. Ali can explain, modify, test, query, diagnose, and defend the central flow and accurately distinguish core ownership from bounded exposure.

## 14. Weekly direction

| Week | Delivery direction |
|---:|---|
| 1 | Pass M0 and M1; begin M2 |
| 2 | Close M2; complete Day-14 workload and ownership review |
| 3–4 | Build and close M3 |
| 5–6 | Build and close M4 |
| 7–8 | Build and close M5 |
| 9–10 | Complete M6 decisions and Day-60 admission review |
| 11–12 | Complete M7 packages |
| 13 | Complete M8 and Day-90 review |

Weekly files may assign exact deliverables but may not become additional strategy documents.

## 15. Blocker and change control

Use the approved Learning and Execution Contract and Session Protocol.

A milestone change requires:

- evidence of infeasibility, external constraint, safety issue, prerequisite overrun, underload/overload, or failed assumption;
- affected milestone and gate;
- smallest necessary correction;
- preserved completed work;
- explicit deadline and downstream consequence;
- confirmation that the mission and frozen product boundary remain intact unless the charter's formal reframe rule is invoked.

Do not restart the project because one milestone is difficult or one hypothesis fails.

## 16. Current activation

**Audit result:** Passed.  
**Approval result:** Approved and controlling.  
**Planning route R0:** Pass.  
**Current route/milestone:** R1 / M1 — First manual evidence decision.  
**Active tracker:** `../tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md`.  
**Active session:** `UPGRADEPILOT_FIRST_SESSION_PLAN.md` / UP-S01.  
**Technical execution:** Authorized for the bounded active session.  
**Technical implementation:** Not started; M2 authorization follows M1.  
**Exact next action:** Start UP-S01.  
**No additional planning artifact is authorized before execution.**
