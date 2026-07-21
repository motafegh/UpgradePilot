# UpgradePilot — Governing Project Charter

**Owner:** Ali Rajabi  
**Recorded:** 2026-07-19  
**Status:** Formally selected and final primary 90-day flagship project  
**Execution period:** 2026-07-20 to 2026-10-17  
**Authority:** Primary-project charter under [`governance/90_DAY_EXECUTION_CONTRACT.md`](governance/90_DAY_EXECUTION_CONTRACT.md)  
**Responsibility:** Mission, user, supported decision, product boundary, outcome classes, evidence doctrine, technology-admission rules, termination conditions, and claim limits  
**Live state:** The canonical tracker controls current route, milestone, gate, blocker, capability state, and next responsibility. This charter does not record session-level activation or exact next actions.  
**Working identity:** **AI-augmented Python/data/ML engineer developing secure engineering capability.**

## 1. Decision and authority

UpgradePilot is the selected primary project for the 90-day execution period. Broad project comparison is closed.

- UpgradePilot receives the primary technical focus.
- AegisLab execution plans, daily routes, weekly packages, milestone sequences, and implementation orders are deferred and non-controlling.
- AegisLab remains historical technical evidence and may contribute only a bounded lesson or component through explicit later admission.
- Sentinel remains a research archive and source of selectively reusable lessons. It does not dictate the mission, architecture, modules, or route.
- No prior project, architecture, task, or repository becomes active merely because it already exists.

Reopening primary-project selection requires the formal change evidence defined in this charter and the canonical 90-day execution contract.

## 2. Governing controls

This charter operates with:

1. [`governance/90_DAY_EXECUTION_CONTRACT.md`](governance/90_DAY_EXECUTION_CONTRACT.md);
2. [`strategy/STRATEGY_AND_SCOPE.md`](strategy/STRATEGY_AND_SCOPE.md);
3. [`strategy/LEARNING_AND_PROJECT_DESIGN_PROFILE.md`](strategy/LEARNING_AND_PROJECT_DESIGN_PROFILE.md);
4. [`strategy/PROJECT_SELECTION_AND_CAPABILITY_SPECIFICATION.md`](strategy/PROJECT_SELECTION_AND_CAPABILITY_SPECIFICATION.md);
5. [`strategy/ADVANCED_SYSTEMS_EXPOSURE_AND_ADOPTION_POLICY.md`](strategy/ADVANCED_SYSTEMS_EXPOSURE_AND_ADOPTION_POLICY.md);
6. [`strategy/UPGRADEPILOT_CAPABILITY_AND_PREREQUISITE_SPECIFICATION.md`](strategy/UPGRADEPILOT_CAPABILITY_AND_PREREQUISITE_SPECIFICATION.md);
7. [`governance/UPGRADEPILOT_LEARNING_AND_EXECUTION_CONTRACT.md`](governance/UPGRADEPILOT_LEARNING_AND_EXECUTION_CONTRACT.md).

`governance/EXECUTION_CONTRACT.md` is a compatibility path only and has no independent authority.

Older AegisLab-specific or candidate-comparison documents cannot override this selected-project decision. Higher-level safety, legal, privacy, workload, evidence, and ownership requirements remain controlling.

## 3. Working definition

UpgradePilot is an evidence-backed dependency-update decision system for maintainers of public Python repositories.

> For an open-source Python maintainer reviewing an automated dependency-update pull request, UpgradePilot produces a provenance-backed, uncertainty-aware recommendation to **merge after normal review, run targeted checks, investigate or block, defer, or abstain**. It uses pull-request change evidence, upstream release evidence, repository-specific dependency context, dependency relationships, and available Continuous Integration evidence because the signals are fragmented and a passing build, version number, compatibility score, or generated changelog alone does not establish that an update is appropriate for the repository.

UpgradePilot is decision support. It is not an automatic merge bot, generic vulnerability scanner, universal dependency platform, or substitute for maintainer judgment.

## 4. Selection basis and personal fit

UpgradePilot passed selection because:

- the problem exists independently of the learning plan;
- the primary user and supported decision are specific;
- lawful public but imperfect inputs are available;
- a weak end-to-end flow is feasible early;
- usefulness and quality can be evaluated beyond visual appearance;
- the project contains a nontrivial evidence and context thesis;
- the mission has sufficient curiosity and technical runway for 90 days;
- the product can remain bounded to one user, workflow, input family, and output family;
- the core can be implemented and progressively owned by Ali;
- the mission supports Python, data, SQL, testing, security, CI, ML, AI, and production-oriented engineering;
- it supports project-connected advanced-system exposure without requiring permanent adoption;
- no known external dependency makes the complete project impossible.

The personal-fit requirement is passed. The mission repeatedly asks questions aligned with Ali's learning and reasoning style:

- How can a change propagate through a repository or dependency relationship?
- Which relationships are direct, transitive, structural, or only apparent?
- Which evidence is trustworthy, incomplete, stale, unavailable, or conflicting?
- How deeply should this update be investigated?
- When is broad investigation disproportionate?
- What does the simple baseline miss?
- Does contextual, structural, historical, learned, or AI-assisted evidence materially improve the decision?
- What should the maintainer do next, and why?

Selection does not guarantee that every technical hypothesis will succeed. Evidence may justify narrowing, reclassification, or termination.

## 5. Primary user, problem, and supported decision

### 5.1 Primary user

A maintainer of a public Python open-source repository receiving an automated Dependabot dependency-update pull request.

### 5.2 Central problem

The maintainer must decide how to handle an update using evidence distributed across the pull request, dependency declarations, repository code and configuration, upstream releases, package metadata, dependency relationships, CI runs, and repository history.

The evidence may be incomplete, inconsistent, stale, inaccessible, or non-project-specific. Existing automation proposes the update and exposes signals, but the maintainer still chooses the appropriate investigation depth and next action.

### 5.3 Bounded actions

1. **Merge after normal review** — available evidence identifies no need beyond the repository's normal process.
2. **Run targeted checks** — specific missing or risk-bearing evidence justifies a named check or review step.
3. **Investigate or block** — observed evidence identifies a material compatibility, support, behavior, security, or reliability concern.
4. **Defer** — policy, timing, supersession, unresolved evidence, or disproportionate investigation cost means the update should not proceed now.
5. **Abstain** — evidence is too incomplete, inaccessible, or conflicting for a defensible recommendation.

These actions do not authorize repository mutation.

## 6. Mission and technical thesis

Build a production-oriented system that turns a real dependency-update pull request into a reproducible, provenance-backed, uncertainty-aware decision report, then determine whether repository context, structural relationships, learned methods, and grounded AI assistance improve the maintainer decision over a transparent deterministic baseline.

Primary thesis:

> Combining repository-specific usage context, dependency-path evidence, upstream behavioral changes, and available CI history will produce more useful and better-calibrated decisions than a baseline using only version-change category, current CI conclusion, dependency directness, and release-note keywords.

Supporting investigations include whether:

- explicit provenance and source-quality states reduce unsupported conclusions;
- abstention and proportional investigation depth outperform forced recommendations;
- structural or graph representations capture context missed by flat features;
- learned ranking or recommendation improves decision utility;
- grounded LLM synthesis improves evidence comprehension without unacceptable unsupported claims;
- bounded multi-agent investigation improves coverage or review quality over deterministic and single-agent workflows;
- asynchronous work, service boundaries, orchestration, and MLOps solve observed needs or remain unjustified complexity.

A technology label is not a thesis. Every experiment requires:

1. an observed product or evaluation limitation;
2. a simpler baseline;
3. a bounded hypothesis;
4. measurable success and rejection conditions;
5. documented costs and new failure modes;
6. an adopt, retain-as-pilot, reject, or defer decision.

## 7. Outcome classification

### 7.1 Core required outcome

A successful flagship core requires:

- one public Python Dependabot PR through the complete product flow;
- lawful source acquisition with time or revision context;
- explicit raw, normalized, accepted, rejected, missing, inaccessible, stale, invalid, and conflicting evidence states;
- tested central contracts and transformations;
- a deterministic baseline producing one bounded recommendation or abstention;
- traceability from every material factual claim to preserved evidence;
- separation of observation from inference;
- uncertainty, degraded output, or abstention under insufficient evidence;
- persisted runs, inputs, transformations, recommendations, and versions;
- clean-setup reproducibility;
- unit, integration, failure-path, and recovery tests;
- CI for the supported core;
- secure configuration, untrusted-input handling, dependency-risk controls, and claim boundaries;
- a CLI and/or API exposing the user-visible flow;
- a staged-corpus evaluation of the deterministic baseline;
- an explicit truth and label audit;
- Ali's ability to explain, modify, test, query, and diagnose the central path;
- portfolio language distinguishing implemented, measured, degraded, experimental, rejected, and future behavior.

The core does not require a successful learned model, permanent graph architecture, permanent LLM or agent component, microservices, queue, Kubernetes, or multi-cloud operation.

### 7.2 Serious 90-day targets

The following retain their approved target status and must receive planned investigation when prerequisites and core progress permit:

- a defensible adjudication and label process;
- at least one learned ranking or recommendation experiment;
- an advanced MLOps lifecycle around the real model or a bounded negative lifecycle experiment when labels reject the model path;
- comparison of flat features with dependency-path, structural, temporal, or graph-derived representations;
- grounded LLM evidence synthesis compared with a deterministic report;
- bounded multi-agent investigation compared with deterministic and single-agent baselines;
- a project-integrated distributed-queue pilot for a representative long-running or rate-limited job;
- one bounded service-extraction comparison against the modular-monolith baseline;
- representative Kubernetes deployment;
- bounded multi-cloud portability or deployment exposure;
- A1 hands-on exposure for all six advanced-system areas required by policy;
- at least two A2 project-integrated pilots, provisionally distributed queues and advanced MLOps.

A target may end in adoption, retained pilot status, rejection, or documented inability to evaluate. A rigorous negative result satisfies the experimental responsibility without creating a success claim.

### 7.3 Stretch outcomes

Stretch outcomes include measurable improvement from learned, graph, LLM, or multi-agent methods; useful confidence calibration; external maintainer validation; A3 permanent adoption; larger trustworthy corpora; temporal generalization; broader package-format support; and evidence supporting claims beyond a bounded learning/portfolio environment.

Failure to reach a stretch outcome does not weaken the core when the experiment and decision are rigorous.

## 8. Frozen 90-day product boundary

Included:

- one primary user: public Python open-source maintainer;
- one workflow: review of an automated Dependabot update PR;
- one input family: associated public repository, PR, package, release, dependency, and CI evidence;
- one output family: dependency-update decision reports;
- Python as primary implementation language;
- one main persistence system;
- one application repository;
- one deployment model for the supported core;
- one analytical question: whether contextual evidence improves the maintainer decision over a transparent baseline;
- one continuous product flow.

Initial ecosystem:

- GitHub-hosted public repositories;
- Dependabot pull requests;
- Python projects;
- PyPI metadata and public upstream release evidence;
- public repository files and public CI metadata through authorized interfaces.

Additional Python declaration formats enter only when actual cases demonstrate need.

Outside the frozen core:

- private repositories or private Dependabot alert details;
- automatic merging, commenting, approval, or repository mutation;
- universal language, package-manager, update-bot, or hosting-provider support;
- generic vulnerability scanning or exploitability prediction;
- a separate general CI repair, code-review, agent, or MLOps platform;
- enterprise authentication, multi-tenancy, multiple databases, or an unjustified vector database;
- autonomous external actions;
- high-availability or multi-region production operation;
- claims that an update is objectively safe.

## 9. Input family and feasibility realities

The product may use PR metadata and diffs; base/head revisions; comments and disposition; dependency declarations and lockfiles; repository source, tests, configuration, and workflows; package metadata; upstream releases, changelogs, commits, advisories, and support statements; reproducible dependency relationships; available public CI metadata and logs; prior public update PRs; and lawful user-supplied preserved evidence.

Required limitations:

- historical CI logs may expire;
- private alert details may be inaccessible;
- release notes and metadata may be incomplete, delayed, inconsistent, or wrong;
- static repository files may not reveal dynamic, generated, optional, or deployment-specific behavior;
- merged or closed status is supporting evidence, not ground truth;
- a large trustworthy action-label set is not guaranteed;
- external maintainer review is desirable but not mandatory;
- sources may disappear, rate-limit, change schema, or conflict;
- missing, inaccessible, stale, or conflicting evidence remains visible and may require abstention.

The product must not replace these realities with synthetic certainty.

## 10. End-to-end flow and report contract

```text
public Dependabot PR
→ acquire source records
→ preserve raw evidence and source context
→ validate, classify, and normalize evidence
→ expose missing, inaccessible, stale, invalid, and conflicting states
→ construct repository and dependency context
→ run deterministic baseline
→ optionally run admitted contextual, structural, learned, or AI-assisted methods
→ compare evidence and method outputs
→ produce provenance-backed recommendation, targeted checks, defer decision, investigation/block decision, or abstention
→ persist run, versions, evidence state, decision, and evaluation result
→ compare repeated runs and changed evidence
```

Not every responsibility requires a separate service or module.

Each report must include:

- repository, PR, dependency, and version identity;
- analysis time and input snapshot identifiers;
- recommended action or abstention;
- confidence or uncertainty appropriate to the method;
- observed evidence and inferred conclusions;
- missing, inaccessible, stale, and conflicting evidence;
- material risk or compatibility signals;
- justified targeted checks;
- provenance for every material factual claim;
- rules, model, prompt, configuration, and data versions used;
- known limitations, degraded-state indicator, claim boundary, and reproducibility information.

A report must never imply guaranteed compatibility, security, absence of regressions, or maintainer intent.

## 11. Transparent deterministic baseline

The first baseline uses inspectable signals such as:

- version-change category;
- direct versus transitive status when reproducible;
- CI conclusion and evidence availability;
- breaking, support, deprecation, security, or behavior indicators in upstream evidence;
- runtime, Python, platform, or toolchain support changes;
- repository declaration and lockfile context;
- basic repository-specific usage evidence;
- known missing or conflicting source states;
- explicit abstention rules.

This baseline must be measured before learned, graph-heavy, LLM, or agentic methods can be claimed as improvements.

## 12. Evidence doctrine

Evidence may support only claims inside its observed scope:

- PR metadata and diffs show the declared change, revisions, files, comments, checks, and disposition—not universal safety or maintainer intent.
- Declarations and lockfiles show declared/resolved relationships for a snapshot—not actual runtime reachability or exploitability.
- Source, tests, and workflows show observable static references and configured checks—not complete dynamic behavior or sufficiency.
- Package metadata and upstream records show published statements and changes—not project-specific compatibility or completeness.
- Dependency graphs show captured structural paths—not runtime execution, causality, or value from graph complexity.
- CI shows recorded outcomes for identified commits and environments—not universal compatibility or absence of untested regressions.
- Historical PR outcomes show actions taken—not the objectively correct action.
- Adjudicated labels show interpretation under a declared rubric—not universal maintainer preference or objective safety.
- Model metrics show performance on a declared corpus, split, labels, and metrics—not production safety or broad generalization.
- LLM or multi-agent outputs show candidate synthesis or investigation traces only when grounded and evaluated; agreement among agents is not reliability proof.
- External review supports perceived usefulness for reviewed cases—not general correctness or market demand.

A passing CI result is evidence, not a safety certificate.

## 13. Corpus and evaluation requirements

Corpus construction must:

- use lawful public cases;
- preserve evidence snapshot and acquisition time;
- group or split by repository/dependency to reduce leakage;
- prefer temporal separation when possible;
- distinguish evidence-complete from evidence-degraded cases;
- record exclusions;
- avoid using final PR disposition as the sole label;
- freeze held-out cases before final comparison;
- permit an explicit unadjudicable state.

Targets:

- **Calibration:** 20–30 cases.
- **Held-out acquisition:** at least 50, target 75–100 when lawful acquisition and adjudication quality permit.
- **Defensibly adjudicable held-out recommendations:** at least 30, preferred 50+.
- **External-review subset:** desirable 5–15 cases, but optional.

When fewer than 30 held-out cases are defensibly adjudicable:

- no strong learned-recommendation claim is permitted;
- model work may remain a bounded feasibility experiment;
- label limitations are recorded as a negative result;
- evaluation may shift to evidence quality, selective prediction, investigation ranking, or another approved measurable framing.

Before final evaluation, corpus membership, splits, rubric, adjudication version, baseline, candidate versions, and contamination controls must be frozen and versioned.

## 14. Metrics

Metrics must include scope, denominators, uncertainty, exclusions, and label limitations. Evaluate as applicable:

- extraction correctness and silent-drop/false-acceptance counts;
- material-claim provenance coverage and resolvability;
- evidence-source coverage and evidence-state correctness;
- abstention quality, coverage-risk trade-offs, and false-confidence counts;
- clean-checkout and rerun reproducibility;
- contextual improvement over baseline using paired case analysis and cost-weighted utility;
- class-wise precision/recall/F1, macro-F1, confusion matrix, high-cost false-safe rate, unnecessary-investigation rate, ranking metrics, calibration, and subgroup performance;
- grounded LLM citation coverage, entailment, unsupported claims, omissions, structured-output validity, review effort, latency, and cost;
- multi-agent completion, coverage, unsupported claims, recommendation quality, reproducibility, cost, latency, authorization violations, termination failures, conflict handling, and recovery.

Complexity, report length, model training completion, citation emission, or agent count is not a quality metric.

## 15. Production-oriented quality and ownership

The supported core should include, when justified:

- explicit Python package/application structure;
- explicit central contracts;
- configuration boundaries;
- structured errors and logs;
- raw-input preservation;
- validation and degraded/quarantine behavior;
- one persistence system and reproducible schema setup;
- replay/idempotency behavior;
- CLI and/or API;
- unit, integration, failure, and recovery tests;
- secret, credential, untrusted-content, and supply-chain controls;
- Docker or another runtime only when justified;
- CI;
- operational setup and cleanup documentation;
- limitations and claim register;
- versioned evaluation evidence;
- AI-assistance disclosure.

The default claim is **production-oriented**, not production-ready.

For central responsibilities, Ali must increasingly:

```text
understand the maintainer need
→ predict behavior
→ make or challenge the design decision
→ implement or materially modify a bounded responsibility
→ test it
→ run it on real evidence
→ interpret result or failure
→ explain its effect on the complete flow
```

Required ownership includes at least one substantial Ali-owned central change each week, ability to locate responsible code/data, explain central schemas and queries, add or repair tests, diagnose failures, reject unjustified complexity, and reproduce representative behavior with progressively reduced prompting.

Repository size, service count, model complexity, cloud count, cluster size, agent count, and tool count do not establish ownership.

## 16. Advanced-system exposure and adoption

The existing approved advanced-system strategy remains unchanged.

Advanced packages use the working UpgradePilot mission and representative workload and do not precede the first working core flow. Approximately 20–30% of focused technical capacity is reserved later, with only one major package normally active.

| Area | Minimum required path | Planned target |
|---|---|---|
| Kubernetes | A1 deployment with resource, rollout/failure, recovery, and cleanup evidence | A1; A2 only when orchestration needs justify it |
| Microservices | A1 bounded service boundary and failure path | A1; possible A2 comparison against modular monolith |
| Distributed queues | A1 producer-consumer workflow with state, failure/retry, and idempotency evidence | **A2 target** for a real asynchronous limitation |
| Multi-cloud | A1 executable comparison of the same bounded workload in two environments | A1; A2 only when portability/provider behavior is mission-relevant |
| Autonomous multi-agent systems | A1 bounded roles, tools, shared state, termination, traceability, and failure inspection | A1; A2 only with measured improvement over simpler workflows |
| Advanced MLOps | A1 reproducible lifecycle with experiment tracking, artifact identity, evaluation, and controlled inference | **A2 target** around a real learned lifecycle or bounded negative lifecycle experiment |

Primary provisional A2 pilots remain distributed queues and advanced MLOps. When MLOps A2 is invalid, a formal decision may use a microservice or multi-agent fallback. No fallback may manufacture success or weaken the core.

Every package records representative workload, simpler baseline, target exposure, time/scope ceiling, safety/cost/privacy/credential/cleanup boundaries, observed behavior and failure, comparison, operational burden, Ali ownership, adoption decision, and exact permitted claim.

## 17. Technology and source admission

A new technology, source, model family, representation, service, or major module enters only when:

1. a user-visible or evaluation limitation is observed;
2. simpler behavior is inadequate;
3. success and rejection conditions exist;
4. the smallest viable experiment is defined;
5. maintenance and delayed work are recorded;
6. Ali can explain and modify the responsibility;
7. the core remains runnable;
8. permanent adoption follows baseline comparison.

Additional rules:

- Learned methods require real target, label audit, defensible cases, baseline, leakage-aware split, utility/failure metrics, and rejection rule.
- Graph work requires meaningful entities/relationships, reproducible construction, simpler baseline, information-loss hypothesis, leakage/temporal analysis, and measurable benefit.
- Grounded LLM synthesis requires a specific unmet task, source-constrained context, bounded output, abstention/review behavior, unsupported-claim evaluation, and non-LLM comparison.
- Multi-agent work requires separable roles, tool/authorization limits, shared-state and termination rules, conflict handling, simpler comparison, and safety/recovery tests.
- Additional sources require evidence of inadequate coverage or decision quality and must be lawful, accessible, maintainable, and measurable.

## 18. Reframe and termination conditions

A formal review must reframe, narrow, or terminate when evidence shows that:

- public evidence cannot support output more useful than a simple PR summary;
- repository context cannot be acquired or interpreted inside the boundary;
- defensible evaluation or adjudication cannot be constructed;
- recommendations depend mainly on undocumented intuition;
- useful operation requires private data, unavailable logs, or inaccessible infrastructure;
- value requires multi-language, multi-hosting, or multi-bot scope first;
- the product becomes a generic scanner, CI, code-review, agent, or MLOps platform;
- missing evidence is hidden;
- model, graph, LLM, or agent work proceeds without baseline and rejection gates;
- advanced exposure prevents core completion or ownership;
- Ali cannot increasingly modify, test, query, and diagnose the central flow;
- material cost, credential, legal, privacy, or safety constraints appear;
- the mission no longer sustains product pursuit;
- the deterministic baseline already solves the decision sufficiently.

Prefer the smallest necessary change. A failed hypothesis revises or terminates that hypothesis, component, representation, or adoption claim—not automatically the mission.

## 19. Historical activation sequence

Before initial technical execution was authorized, the following artifacts were required and approved:

1. Capability and Prerequisite Specification;
2. Learning and Execution Contract;
3. 90-Day Master Roadmap;
4. Staged Milestone Plan;
5. First-Session Plan;
6. Evidence and Progress Tracker.

This section records the original governance activation sequence. It does **not** control current state, implementation authorization, or the next action. Current state is recorded only in the canonical tracker and current authorized work artifact.

## 20. AegisLab and Sentinel preservation

AegisLab may contribute bounded safety, assistance, failure-diagnosis, validation, reproducibility, scenario, and cleanup lessons. Its environment-first route, security-lab prerequisites, module structure, roadmap, and architecture do not transfer automatically.

Sentinel may contribute lessons from external acquisition, raw/normalized separation, provenance, source-failure handling, visible flow, evaluation, representation experiments, graphs, and scope/ownership failures. Its mission, repositories, module count, blockchain scope, or AI-generated complexity do not transfer automatically.

## 21. Claim standard

Permitted claims must match evidence:

- **selected primary project** — this charter;
- **implemented** — behavior exists and is verified;
- **evaluated** — measured on a declared corpus and metric;
- **production-oriented** — realistic engineering practices exist with explicit limitations;
- **hands-on exposure** — A1 evidence;
- **project-integrated pilot** — A2 comparison evidence;
- **adopted product responsibility** — A3 evidence;
- **independent capability** — repeated low-assistance design, operation, diagnosis, and modification evidence.

Do not claim objective update safety, correctness from merged status, model success from training, grounding from emitted citations, reliability from agent agreement, mastery from advanced-system exposure, or production readiness without evidence beyond the 90-day environment.

## 22. Selection closure and maintenance

The primary-project selection decision is closed. UpgradePilot is the single primary flagship mission. Broad candidate comparison, automatic AegisLab continuation, and architecture-first redesign remain unauthorized.

This charter must change only when the mission, user, supported decision, frozen boundary, outcome classes, evidence doctrine, target requirements, admission rules, termination conditions, or claim limits change.

Do not add current milestone, session, implementation, method, blocker, or exact-next-action state to this charter.
