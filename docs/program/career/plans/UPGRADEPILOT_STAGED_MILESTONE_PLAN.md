# UpgradePilot Staged Milestone Plan

**Owner:** Ali Rajabi  
**Recorded:** 2026-07-19  
**Execution period:** 2026-07-20 to 2026-10-17  
**Status:** Approved and controlling staged milestone plan  
**Responsibility:** Milestone outcomes, entry requirements, deliverables, evidence and ownership gates, advancement, and stop conditions  
**Live state:** The canonical tracker controls current milestone, gate results, blockers, and next responsibility. This plan does not record current status, completed results, or exact next actions.

## 1. Purpose and authority

This plan converts the 90-day route into bounded product milestones.

A milestone defines:

- user-visible or evaluation outcome;
- minimum entry state;
- deliverables and proof required to pass;
- Ali ownership evidence;
- what may remain weak;
- stop/rejection conditions;
- normative advancement when the gate passes.

It is not a technology curriculum, detailed architecture, framework-selection record, tracker, or substitute for an authorized session/work package.

When instructions conflict, use:

1. safety, legal, privacy, health, credential, cost, and platform constraints;
2. `../governance/90_DAY_EXECUTION_CONTRACT.md`;
3. `../strategy/STRATEGY_AND_SCOPE.md`;
4. `../UpgradePilot.md`;
5. `../strategy/UPGRADEPILOT_CAPABILITY_AND_PREREQUISITE_SPECIFICATION.md`;
6. `../governance/UPGRADEPILOT_LEARNING_AND_EXECUTION_CONTRACT.md`;
7. `UPGRADEPILOT_90_DAY_MASTER_ROADMAP.md`;
8. this plan;
9. the canonical tracker and current authorized session/work package;
10. `../governance/SESSION_AND_BLOCKER_PROTOCOL.md`;
11. current inspected evidence.

A lower-level artifact may divide work but may not weaken a milestone gate, expand the product boundary, or silently adopt technology.

## 2. Milestone law

A milestone passes only when:

- required behavior or decision exists;
- evidence is preserved and linked;
- material limitations are explicit;
- AI assistance is labeled;
- Ali completes the required explanation, modification, test, query, or diagnosis;
- negative or missing evidence is not hidden;
- no unsupported claim is carried forward.

A date or hour ceiling does not create a pass. A rigorous rejection or negative experiment may pass when that is the milestone outcome.

When a milestone passes early, proceed only through its normative advancement rule and the next authorized work artifact. Do not pad time or invent scope.

## 3. Milestone overview

| Milestone | Roadmap route | Required outcome | Maximum route capacity |
|---|---|---|---:|
| M0 — Planning closure | R0 | Execution-control artifacts are approved and technical execution can begin without another planning layer | 4 h |
| M1 — First manual evidence decision | R1 / G1 | One real Dependabot PR becomes a traceable manual evidence package and weak decision report | 8 h |
| M2 — First automated vertical slice | R2 / G2 | One reproducible PR-to-report path with tests and changed-case evidence | 36 h |
| M3 — Reliable evidence and persistence | R3 / G3 | Supported acquisition, validation, provenance, persistence, replay, SQL, failure behavior, and CI | 48 h |
| M4 — Repository-specific dependency context | R4 / G4 | Traceable declaration, path, usage, test, workflow, and limitation evidence | 48 h |
| M5 — Deterministic baseline and evaluation | R5 / G5 | Versioned baseline, staged corpus, adjudication, held-out evaluation, and error analysis | 48 h |
| M6 — Evidence-gated analytical experiments | R6 / G6–G7 | Learned, graph, or grounded-LLM methods are measured or rigorously rejected | 48 h |
| M7 — Advanced-system exposure and pilots | R7 / G7–G9 | A1 exposure across six areas and justified A2 pilots with operational comparisons | 48 direct h |
| M8 — Final ownership and portfolio closure | R8 / G10 | Reproducible supported core, evidence index, ownership defense, portfolio, and market calibration | 24 h |

The tracker records actual milestone status and results.

## 4. M0 — Planning closure

### Outcome

The project can begin evidence work without another governance-planning artifact.

### Must exist

- this milestone plan;
- `../tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md`;
- `UPGRADEPILOT_FIRST_SESSION_PLAN.md`.

### Pass condition

- all required artifacts are approved and mutually consistent;
- the first session names one real public Python Dependabot PR;
- no implementation, architecture build-out, corpus campaign, model experiment, or infrastructure package begins during planning;
- the tracker and session plan can activate M1 without another planning layer.

### Normative advancement

When M0 passes, M1 becomes eligible through the approved first-session plan.

## 5. M1 — First manual evidence decision

### Outcome

> For one real public Python Dependabot PR, produce a traceable evidence package and a weak recommendation to merge after normal review, run targeted checks, investigate or block, defer, or abstain.

### Entry requirements

- D1 recognition of the read-only boundary;
- D1 distinction between observation, inference, missing evidence, and unsupported claims;
- safe public-repository navigation;
- authorized first-session plan.

No standalone prerequisite course is required.

### Must deliver

1. PR identity, URL, base/head revisions, bot/author identity, state, and changed files.
2. Updated package, old/proposed versions, and declaration/lock context.
3. Direct, transitive, optional, development, runtime, or unresolved classification with evidence and uncertainty.
4. Relevant upstream release evidence.
5. Available repository and CI evidence inside the case boundary.
6. Source identity, retrieval time, revision/snapshot, and evidence-state classification.
7. Weak decision report with material claims linked to evidence.
8. Explicit limitations and proof boundaries.
9. Assistance and ownership record.
10. One changed or missing-evidence variant.

### Pass condition

Ali can:

- explain the diff and what it does not establish;
- identify the dependency change and declaration context;
- trace each material factual claim;
- separate observation from interpretation;
- explain why merge status, SemVer, compatibility scores, or passing CI are not safety proof;
- produce or challenge the weak decision;
- respond to changed evidence without inventing certainty.

Minimum depth is narrow D2 guided application for the relevant capability responsibilities.

### What may remain weak

Python implementation, SQL/persistence, automated acquisition, repository-wide context, evaluation corpus, ML, graphs, LLMs, agents, queues, services, Kubernetes, cloud, and MLOps.

### Stop conditions

- the report gate passes;
- the eight-hour ceiling is reached;
- unavailable public evidence requires abstention;
- the selected case is unsuitable, in which case the reason is recorded and one replacement is selected inside the same bounded milestone.

### Normative advancement

When M1 passes, M2 becomes eligible using the same case unless evidence shows it is unsuitable for the minimal automated slice.

## 6. M2 — First automated vertical slice

### Outcome

> One real PR input reaches one reproducible machine-produced evidence report through a bounded interface.

### Entry requirements

- M1 passed;
- relevant Python, contract, testing, provenance, and security capabilities at D1 or teachable D2 scope;
- selected input and report contract preserved.

### Must deliver

- smallest understandable Python package/application structure;
- one bounded input contract;
- raw-input preservation;
- normalized evidence representation;
- explicit missing, invalid, conflicting, accepted, and rejected states as required;
- weak deterministic decision path;
- human-readable and machine-readable output;
- tests for central transformation and decision behavior;
- one malformed, missing, or conflicting case;
- secure configuration with no embedded token;
- reproducible run instructions;
- one Ali-owned central change and one diagnosed changed/failing case.

### Pass condition

A clean run reproduces the vertical slice, central tests pass, degraded evidence remains visible, and Ali can locate, modify, test, diagnose, and explain the central path.

### Forbidden expansion

No database, web service, queue, cloud deployment, ML model, graph model, agent system, or unrelated permanent framework decision is required merely to pass M2.

### Normative advancement

When M2 passes, M3 becomes eligible using only sources and behaviors proven by M2.

## 7. M3 — Reliable evidence and persistence

### Outcome

The supported evidence flow can be acquired or replayed, validated, persisted, queried, diagnosed, and reproduced without hiding source failure.

### Entry requirements

- M2 passed;
- bounded supported-source list;
- acquisition, validation, persistence, SQL, provenance, and reliability capabilities at D2 entry depth or bounded repair scope.

### Must deliver

- lawful GitHub and package/release acquisition for supported fields;
- raw and normalized records with provenance;
- explicit partial-source failure;
- rate-limit, pagination, retry, backoff, caching, or idempotency only when required;
- one relational persistence system;
- reproducible schema setup or migrations;
- SQL queries tracing claims and comparing runs;
- replay/duplicate behavior;
- structured errors and logs;
- unit, integration, failure, and recovery tests;
- CI after the local path is stable;
- Docker only when it measurably improves reproducibility.

### Pass condition

One case can be reacquired or replayed without hidden duplication; claims resolve to persisted evidence; source failures remain explicit; Ali can query and diagnose one persistence or acquisition failure.

### Normative advancement

When M3 passes, M4 becomes eligible after evidence contracts and persistence are stable enough for repository-context records.

## 8. M4 — Repository-specific dependency context

### Outcome

UpgradePilot adds reproducible repository-specific dependency and usage evidence without claiming runtime causality it cannot establish.

### Entry requirements

- M3 passed;
- supported declaration/lock formats selected from real cases;
- relevant dependency, repository-context, and analysis capabilities at required entry depth.

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

Representative cases contain traceable context, limitations remain visible, static reachability is not treated as runtime proof, and Ali can locate evidence and explain one missed path.

### Normative advancement

When M4 passes, freeze the supported context method and make M5 eligible.

## 9. M5 — Deterministic baseline and evaluation

### Outcome

A versioned deterministic baseline and repository-context method can be evaluated honestly on staged cases.

### Entry requirements

- stable M3/M4 evidence contracts;
- evaluation capabilities at D2;
- declared case-acquisition and adjudication process.

### Must deliver

- versioned decision table;
- evidence-sufficiency and abstention rules;
- asymmetric-cost assumptions;
- calibration cases and frozen held-out subset;
- adjudication rubric;
- disagreement and unadjudicable states;
- contamination/leakage controls;
- metrics with denominators and uncertainty;
- error analysis by evidence and recommendation failure type;
- comparison of weak baseline and contextual method;
- label-quality audit.

### Pass condition

Evaluation is reproducible; historical disposition is not ground truth; high-cost errors and label limits are inspectable; Ali can explain the rubric, split, metrics, and main failure classes.

### Normative advancement

When M5 passes, run the analytical-method admission decision. Weak labels may close recommendation-model claims while preserving the core.

## 10. M6 — Evidence-gated analytical experiments

### Outcome

Each admitted learned, graph, or grounded-LLM method has a bounded hypothesis, baseline comparison, reproducible evidence, and adopt/reject/defer decision.

### Entry requirements

- M5 passed;
- target and labels audited;
- measured deterministic baseline;
- relevant prerequisites at D2;
- success and rejection conditions frozen.

### Candidate paths

- recommendation classification;
- investigation-priority ranking;
- selective prediction with abstention;
- dependency-path or structural features;
- grounded report synthesis with citation-entailment checks;
- negative feasibility result.

### Must deliver per admitted path

- hypothesis and observed limitation;
- frozen comparison method;
- data/feature or prompt/context identity;
- leakage-aware split or case separation;
- held-out results;
- high-cost error analysis;
- cost, latency, maintainability, and ownership evidence;
- adopt, retain-as-pilot, reject, or defer decision.

### MLOps rule

MLOps enters only around a defensible learned lifecycle or an explicitly bounded negative lifecycle experiment. It cannot manufacture model success.

### Pass condition

Every attempted method has reproducible evidence and a valid decision. Rigorous rejection passes.

### Normative advancement

When M6 passes, use the supported core as the workload for M7.

## 11. M7 — Advanced-system exposure and pilots

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

Each package satisfies the capability specification and Advanced Systems Exposure and Adoption Policy. Only one major package is active at a time.

### Every package must deliver

- representative UpgradePilot workload;
- simpler baseline;
- A1 or A2 target;
- scope/time ceiling;
- security, credential, privacy, cost, and cleanup boundary;
- observable failure or degraded state;
- inspection, recovery, and cleanup;
- operational-burden comparison;
- Ali teach-back and ownership evidence;
- adopt, retain-as-pilot, reject, or defer decision;
- exact permitted portfolio claim.

### A2 targets

Primary targets remain:

1. distributed queues;
2. advanced MLOps when a defensible learned lifecycle exists.

When MLOps A2 is invalid, a formally recorded fallback may use one microservice extraction or one bounded multi-agent integrated comparison.

### Pass condition

All six areas have valid A1 evidence or a formally documented infeasibility boundary; at least two A2 decisions are completed unless a formal capacity review narrows the requirement; no package weakens the supported core.

### Normative advancement

When M7 passes, M8 becomes eligible with adoption and rejection decisions frozen.

## 12. M8 — Final ownership and portfolio closure

### Outcome

A technical reviewer can reproduce the supported product, inspect evidence and evaluation, understand limitations, and verify Ali's ownership claims.

### Must deliver

- clean supported-core execution;
- declared input/output boundary;
- representative real and failure cases;
- versioned baseline and evaluation results;
- analytical and advanced-system decisions;
- appropriate tests and CI;
- secure configuration and public-safe evidence;
- setup, run, diagnosis, recovery, and cleanup instructions;
- limitations and claim register;
- assistance disclosure;
- capability and ownership evidence;
- architecture/data-flow explanation based on implemented reality;
- concise reviewer demonstration;
- portfolio README and evidence index;
- market calibration against representative roles.

### Pass condition

Final claims match preserved evidence. Ali can explain, modify, test, query, diagnose, and defend the central flow and distinguish core ownership from bounded exposure.

## 13. Weekly direction

| Week | Delivery direction |
|---:|---|
| 1 | Complete M0/M1 requirements and begin M2 |
| 2 | Close M2 requirements; Day-14 workload/ownership review |
| 3–4 | Build and close M3 |
| 5–6 | Build and close M4 |
| 7–8 | Build and close M5 |
| 9–10 | Complete M6 decisions and Day-60 admission review |
| 11–12 | Complete M7 packages |
| 13 | Complete M8 and Day-90 review |

This table is directional and does not record live completion state. Weekly files may assign exact deliverables but may not become strategy documents.

## 14. Blocker, change control, and maintenance

Use the Learning and Execution Contract and Session and Blocker Protocol.

A milestone change requires:

- evidence of infeasibility, external constraint, safety issue, prerequisite overrun, underload/overload, or failed assumption;
- affected milestone and gate;
- smallest necessary correction;
- preserved completed work;
- explicit deadline/downstream consequence;
- confirmation that the mission and frozen boundary remain intact unless formal charter reframe is invoked.

Do not restart the project because one milestone is difficult or one hypothesis fails.

Change this plan only when milestone outcomes, entry requirements, deliverables, gates, advancement, capacities, or stop conditions change.

Do not add current status, gate results, active session, implementation progress, or exact next actions.
