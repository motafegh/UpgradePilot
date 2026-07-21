# UpgradePilot 90-Day Master Roadmap

**Owner:** Ali Rajabi  
**Recorded:** 2026-07-19  
**Execution period:** 2026-07-20 to 2026-10-17  
**Status:** Approved and controlling master roadmap  
**Responsibility:** Route order, capacity, stage outcomes, reviews, fallback rules, forbidden scope, and Day-90 requirements  
**Live state:** The canonical tracker controls current route, milestone, gate result, blocker, and next responsibility. This roadmap does not record live status or exact next actions.

## 1. Purpose and authority

This roadmap converts the approved UpgradePilot charter into one bounded 90-day route.

It controls:

- product-capability order;
- maximum planning hold before evidence work;
- stage outcomes and hard gates;
- capacity for the supported core, evaluation, learned methods, advanced-system exposure, and closure;
- formal review points and fallback decisions;
- Day-90 required outputs;
- forbidden expansion.

It does not select permanent frameworks, database products, cloud providers, model families, queue products, orchestration tools, or internal architecture. Those choices require observed need and the admission rules in the charter and Learning and Execution Contract.

When instructions conflict, use:

1. safety, legal, privacy, credential, health, cost, and platform constraints;
2. `../governance/90_DAY_EXECUTION_CONTRACT.md`;
3. `../strategy/STRATEGY_AND_SCOPE.md`;
4. `../UpgradePilot.md`;
5. `../strategy/UPGRADEPILOT_CAPABILITY_AND_PREREQUISITE_SPECIFICATION.md`;
6. `../governance/UPGRADEPILOT_LEARNING_AND_EXECUTION_CONTRACT.md`;
7. this roadmap;
8. `UPGRADEPILOT_STAGED_MILESTONE_PLAN.md` and the current authorized session/work package;
9. `../tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md` for actual state;
10. `../governance/SESSION_AND_BLOCKER_PROTOCOL.md`;
11. current inspected technical evidence.

A lower-level artifact may add exact deliverables but may not reorder the route, weaken a gate, expand the frozen boundary, or silently adopt technology.

## 2. Fixed execution principles

- One primary mission: evidence-backed dependency-update decisions for maintainers of public Python repositories reviewing Dependabot pull requests.
- One continuous flow from real PR evidence to a traceable recommendation or abstention.
- Deterministic, provenance-backed behavior before learned or agentic methods.
- A modular single-application baseline before service extraction.
- One main persistence system when persistence becomes necessary.
- Real public evidence, explicit missing states, and no manufactured certainty.
- Teaching around active product needs rather than detached courses.
- Increasing Ali ownership of central behavior.
- One major advanced-system package at a time.
- Rigorous negative experiments may pass.
- Documentation ends when sufficient to execute, reproduce, evaluate, or defend the work.

## 3. Capacity model

### 3.1 Standard capacity

- Monday–Saturday: 4 focused hours per Green day.
- Standard full week: 24 focused hours.
- Final partial week: 24 focused hours across 2026-10-12 to 2026-10-17.
- Approximate total capacity: **312 focused hours** before approved adjustments.

Hours are containers and ceilings. Gates, not elapsed time, determine advancement.

### 3.2 Allocation

| Allocation | Planned capacity | Purpose |
|---|---:|---|
| Planning closure and first manual evidence flow | 12 h | Close controls and complete G1 quickly |
| First automated flow and core engineering | 84 h | G2–G3: runnable slice, acquisition, validation, provenance, persistence, tests |
| Repository-specific context | 48 h | G4: declarations, dependency paths, usage, tests, workflows, limitations |
| Deterministic baseline and evaluation | 48 h | G5: corpus, rubric, held-out evaluation, error analysis |
| Learned, graph, LLM, and advanced-lifecycle decisions | 48 h | G6 and admitted G7 work, including conditional MLOps |
| Advanced-system exposure packages | 48 direct h plus up to 24 embedded h | A1 across six areas and A2 targets without displacing the core |
| Final hardening, ownership, portfolio, and market closure | 24 h | G10 and Day-90 package |

Advanced-system work remains approximately **64–72 hours**, about 20–23% of standard capacity, including embedded MLOps or agent work.

### 3.3 Capacity protection

When time is lost or a stage overruns:

1. preserve the supported core and evidence integrity;
2. reduce optional polish;
3. narrow experimental breadth before weakening evaluation;
4. retain A1 exposure through smaller representative workloads;
5. reduce an A2 target to A1 only through explicit review;
6. never relabel partial work as complete.

## 4. Route overview

| Route | Dates | Maximum focused capacity | Gate | Required outcome |
|---|---|---:|---|---|
| R0 — Planning closure | Jul 20 | 4 h | Pre-execution authorization | Required execution controls approved; no further planning hold |
| R1 — Manual evidence reality | Jul 20–22 | 8 h | G1 | One real Dependabot PR becomes a traceable manual evidence package and weak decision report |
| R2 — First automated vertical slice | Jul 23–Aug 2 | 36 h | G2 | One reproducible input-to-report path with tests and an Ali-owned changed case |
| R3 — Reliable evidence system | Aug 3–16 | 48 h | G3 | Acquisition, validation, provenance, replay, relational persistence, SQL, diagnostics, and CI |
| R4 — Repository-specific context | Aug 17–30 | 48 h | G4 | Declaration, path, usage, test, workflow, and explicit limitation evidence |
| R5 — Deterministic baseline and evaluation | Aug 31–Sep 13 | 48 h | G5 | Versioned baseline, staged corpus, adjudication, held-out evaluation, and error analysis |
| R6 — Contextual, learned, graph, and grounded-AI decisions | Sep 14–27 | 48 h | G6 and admitted G7 | Measured experiments or rigorous rejection decisions against the baseline |
| R7 — Advanced-system pilots and operational comparison | Sep 28–Oct 11 | 48 h direct | G7–G9 | Required A1 exposures, targeted A2 pilots, failure/recovery evidence, and adoption decisions |
| R8 — Final ownership and portfolio closure | Oct 12–17 | 24 h | G10 | Reproducible final system, evidence package, limitations, ownership defense, portfolio, and market calibration |

The staged milestone plan may divide route blocks but may not add another broad planning phase.

## 5. R0 — Planning closure

**Date:** 2026-07-20  
**Maximum:** 4 h

Required artifacts:

- staged milestone plan;
- evidence and progress tracker;
- first-session plan.

Gate criteria:

- artifacts exist and agree with the charter, capability specification, learning contract, and roadmap;
- the first session names one real public Python Dependabot PR and one exact manual evidence output;
- no implementation architecture, corpus campaign, model experiment, or infrastructure package begins during planning;
- execution can start without another planning document.

The tracker records the actual R0 result.

## 6. R1 — Manual evidence reality

**Dates:** 2026-07-20 to 2026-07-22  
**Maximum:** 8 h  
**Gate:** G1

Outcome:

> Given one real public Python Dependabot PR, produce a traceable evidence package and a weak recommendation, targeted-check request, investigation/block decision, defer decision, or abstention.

Required evidence:

- PR identity, base/head revisions, and changed files;
- package, old/proposed versions, and declaration/lock context;
- direct, transitive, optional, or unresolved status;
- available package, release, CI, and repository evidence;
- source identity, retrieval time, and snapshot/revision;
- explicit observed, inferred, missing, inaccessible, stale, conflicting, invalid, accepted, and rejected states where applicable;
- recommendation and limitations;
- assistance and ownership record.

Pass when Ali can explain the change, trace material claims, state proof limits, and respond correctly to one changed/missing-evidence case.

Not required: implementation repository, persistence, automated acquisition, corpus, ML, graphs, LLMs, agents, queues, services, Kubernetes, cloud, or MLOps.

## 7. R2 — First automated vertical slice

**Dates:** 2026-07-23 to 2026-08-02  
**Maximum:** 36 h  
**Gate:** G2

Outcome:

> One real PR input reaches one reproducible machine-produced evidence report through a bounded interface.

Required scope:

- smallest understandable Python package/application structure;
- bounded input identity and acquisition/manual-input path;
- raw preservation and normalized evidence contracts;
- explicit evidence states;
- weak deterministic decision path;
- human-readable and machine-readable report;
- central tests and changed-case behavior;
- secure configuration with no embedded credentials.

Pass when one clean execution reproduces the slice, central behavior is tested, degraded evidence remains explicit, and Ali materially modifies and diagnoses the central path.

No database, service, queue, cloud, model, or permanent framework decision is required merely to pass R2.

## 8. R3 — Reliable evidence system

**Dates:** 2026-08-03 to 2026-08-16  
**Maximum:** 48 h  
**Gate:** G3

Required outcomes:

- lawful bounded acquisition for supported GitHub and package/release evidence;
- raw and normalized records with provenance;
- explicit partial-source failure;
- pagination, rate-limit, retry, backoff, cache, and idempotency only where required;
- one relational persistence system and reproducible schema setup;
- SQL queries for traceability and run comparison;
- replay/duplicate behavior;
- structured errors and logs;
- unit, integration, failure, and recovery tests;
- CI after the local path is stable.

Pass when a case can be reacquired or replayed without hidden duplication, report claims resolve to persisted evidence, source failure remains visible, and Ali can query and diagnose the central path.

Docker enters only when it improves reproducibility.

## 9. R4 — Repository-specific context

**Dates:** 2026-08-17 to 2026-08-30  
**Maximum:** 48 h  
**Gate:** G4

Required outcomes:

- supported declaration/lock formats selected from real cases;
- direct, transitive, optional, runtime, development, and unresolved relationships;
- reproducible dependency paths;
- relevant imports, references, tests, and workflows;
- evidence locations and revisions;
- explicit static, dynamic, resolver, and reachability limits;
- comparison with the weaker PR/package-only view.

Pass when representative cases contain traceable context and the system does not claim runtime causality from static evidence.

Universal resolver support, dynamic execution of untrusted repositories, whole-program static analysis, and graph neural networks remain deferred.

## 10. R5 — Deterministic baseline and evaluation

**Dates:** 2026-08-31 to 2026-09-13  
**Maximum:** 48 h  
**Gate:** G5

Required outcomes:

- versioned deterministic decision table;
- evidence-sufficiency and abstention rules;
- asymmetric decision-cost assumptions;
- staged public corpus;
- calibration cases and frozen held-out subset;
- documented adjudication rubric;
- disagreement and unadjudicable states;
- contamination and leakage controls;
- metrics with denominators and confidence limitations;
- error analysis by evidence and recommendation failure type;
- comparison between weak baseline and repository-context method.

Pass when evaluation is reproducible, historical PR outcome is not ground truth, errors and label limits are inspectable, and Ali can explain the rubric, split, metrics, and main failure classes.

Learned methods enter only after label and target admission.

## 11. R6 — Contextual, learned, graph, and grounded-AI decisions

**Dates:** 2026-09-14 to 2026-09-27  
**Maximum:** 48 h  
**Gate:** G6 and admitted portions of G7

Decision sequence:

1. identify the strongest remaining baseline failure;
2. define the smallest contextual, learned, structural, or synthesis hypothesis;
3. freeze success and rejection conditions;
4. compare with the deterministic baseline on held-out evidence;
5. inspect high-cost errors, calibration/selective behavior, latency, cost, and maintainability;
6. adopt, retain as pilot, reject, or defer.

A learned model requires defensible target, labels, split, and sample. Possible bounded outcomes include classification, investigation ranking, selective prediction with abstention, or a negative feasibility result.

Graph work requires reproducible structure and a measured limitation of flat features. Grounded LLM work requires a specific comprehension limitation, source-constrained context, structured output, entailment/unsupported-claim checks, and deterministic comparison.

When a defensible learned lifecycle exists, up to 16–24 hours may support MLOps A1/A2. Otherwise the MLOps responsibility becomes a bounded negative lifecycle experiment or approved fallback. No success claim is manufactured.

Pass when every attempted method has reproducible evidence and an explicit decision.

## 12. R7 — Advanced-system pilots and operational comparison

**Dates:** 2026-09-28 to 2026-10-11  
**Maximum direct capacity:** 48 h  
**Gate:** G7–G9

The supported core remains the workload. Only one major package is active.

| Area | Minimum | Target |
|---|---|---|
| Distributed queues | A1 | A2 target when synchronous work shows a real limitation |
| Advanced MLOps | A1 | A2 target for a defensible learned lifecycle; otherwise approved fallback |
| Microservices | A1 | A2 only when lifecycle or isolation value is measurable |
| Kubernetes | A1 | A2 only when orchestration creates a real question |
| Multi-cloud | A1 | A2 only when portability/provider behavior is mission-relevant |
| Autonomous multi-agent systems | A1 | A2 only when separable roles improve measured quality over simpler flows |

Each package requires representative workload, simpler baseline, A-level target, prerequisites, time/scope ceiling, safety/privacy/credential/cost/cleanup boundary, failure/degraded-state evidence, recovery/cleanup, operational-burden comparison, Ali ownership, adoption decision, and exact permitted claim.

Primary A2 targets remain distributed queues and advanced MLOps. If MLOps A2 is invalid, a formal decision may use one microservice or bounded multi-agent integrated comparison. The fallback must not weaken the core.

## 13. R8 — Final ownership and portfolio closure

**Dates:** 2026-10-12 to 2026-10-17  
**Maximum:** 24 h  
**Gate:** G10

Required Day-90 package:

- clean reproducible supported-core execution;
- declared input/output boundary;
- representative real and failure cases;
- versioned baseline and evaluation results;
- analytical and advanced-system decisions;
- appropriate tests and CI;
- secure configuration and public-safe evidence;
- setup, run, diagnosis, recovery, and cleanup instructions;
- limitations and claim register;
- AI-assistance disclosure;
- capability and ownership evidence;
- architecture and data-flow explanation based on implemented reality;
- concise technical-reviewer demonstration;
- portfolio README and evidence index;
- market calibration against representative roles.

Pass only when final claims match evidence. “Production-oriented” may be used when supported; “production-ready,” “safe,” “enterprise-grade,” or “expert” requires evidence beyond this route.

## 14. Weekly direction

| Week | Dates | Direction |
|---:|---|---|
| 1 | Jul 20–26 | Close planning, complete G1, begin R2 |
| 2 | Jul 27–Aug 2 | Close G2; Day-14 workload/ownership review |
| 3 | Aug 3–9 | Acquisition, raw/normalized evidence, validation, provenance |
| 4 | Aug 10–16 | Persistence, SQL, replay, failures, CI; close G3 |
| 5 | Aug 17–23 | Declarations, dependency paths, repository usage, tests, workflows |
| 6 | Aug 24–30 | Context quality, static limitations, changed cases; close G4 |
| 7 | Aug 31–Sep 6 | Baseline, evidence sufficiency, corpus, rubric |
| 8 | Sep 7–13 | Held-out evaluation, leakage controls, metrics, error analysis; close G5 |
| 9 | Sep 14–20 | Learned/graph admission and first bounded experiment; Day-60 review |
| 10 | Sep 21–27 | Comparisons, grounded synthesis, MLOps lifecycle decision; close G6 |
| 11 | Sep 28–Oct 4 | Queue A1/A2 and microservice A1 |
| 12 | Oct 5–11 | Kubernetes, multi-cloud, multi-agent, and remaining MLOps/fallback closure |
| 13 | Oct 12–17 | Hardening, reproducibility, ownership defense, portfolio, Day-90 closure |

This map communicates direction, not current completion state or daily instructions.

## 15. Formal review points

### Day 14 — 2026-08-02

Review G1/G2 evidence, delivery density, workload realism, ownership, and whether planning has stopped. Allowed corrections include narrowing G2, rebalancing workload, repairing a prerequisite, or clarifying evidence.

### Day 30 — 2026-08-18

Review reliable acquisition, evidence contracts, degraded states, persistence/SQL, testing/diagnosis, and readiness for repository context. Missing central G3 responsibilities must be repaired before complexity grows.

### Day 60 — 2026-09-17

Review G4/G5 evidence, baseline quality, error classes, label/target sufficiency, experiment admission, and advanced-capacity feasibility. This is the formal ML/MLOps admission or rejection point.

### Day 90 — 2026-10-17

Review supported behavior, evaluation honesty, reliability, reproducibility, Ali ownership, advanced exposure/adoption decisions, portfolio claims, market calibration, and the next evidence-based direction.

## 16. Fallback and reframe rules

- Missing historical CI/upstream evidence remains explicit; prefer recent cases, narrow claims, request checks, or abstain.
- Weak labels stop recommendation-model claims; preserve deterministic product and consider ranking, selective prediction, or feasibility-only experiments.
- External maintainer review is useful but not required; use a declared rubric, held-out separation, independent second pass where possible, and explicit limits.
- Large prerequisite gaps trigger the smallest repair, responsibility narrowing, or formal sequence adjustment—not a general course or project restart.
- Advanced-system overload reduces package breadth, preserves smaller A1 workloads, and changes A2 only through formal review.
- Mission/feasibility failure follows the charter’s reframe and termination conditions.

## 17. Forbidden scope

This roadmap does not authorize:

- multiple programming ecosystems or non-GitHub hosts;
- update bots other than Dependabot;
- private repository data as a core requirement;
- automatic repository mutation;
- generic vulnerability scanning or a separate CI-diagnosis product;
- universal package-manager/lockfile support;
- arbitrary execution of untrusted repository code;
- generalized static-analysis, agent, MLOps, queue, cloud, or platform products;
- multiple primary databases;
- service fleets or permanent multi-cloud architecture;
- unsupported production-readiness or safety claims;
- additional governance planning beyond approved active packages and evidence-derived operational documentation.

## 18. Advancement law and maintenance

A route advances only when its required outcome exists, evidence is preserved, limitations and assistance are explicit, Ali completes the ownership check, no hidden failure is carried forward, and the next block does not depend on an unsupported claim.

When a gate passes early, continue only to a named advancement item. When a gate misses its ceiling, record Partial or Blocked, identify the smallest repair, and use formal review/change control. Never silently declare success.

Change this roadmap only when route order, dates, capacity, stage outcomes, reviews, fallback rules, forbidden scope, or Day-90 requirements change.

Do not add current route, milestone, gate result, session, implementation state, or exact next action.
