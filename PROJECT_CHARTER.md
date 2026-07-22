# UpgradePilot Project Charter

**Status:** Controlling stable project charter  
**Owner:** Ali Rajabi  
**Execution period:** 2026-07-20 to 2026-10-17  
**Responsibility:** Mission, user, supported decision, product boundary, outcome classes, evidence doctrine, admission rules, termination conditions, and claim limits

## 1. Project decision

UpgradePilot is the selected primary learning-by-building flagship for the current 90-day execution period.

It is a production-oriented evidence-backed dependency-update decision system for maintainers of public Python repositories.

## 2. Primary user and decision

### User

A maintainer of a public Python open-source repository receiving an automated Dependabot dependency-update pull request.

### Supported decision

UpgradePilot supports a bounded recommendation to:

1. merge after normal review;
2. run targeted checks;
3. investigate or block;
4. defer; or
5. abstain.

It does not mutate repositories or replace maintainer judgment.

## 3. Product definition

> Given a public Python Dependabot pull request, UpgradePilot assembles and preserves relevant pull-request, package, upstream-release, repository-context, dependency-relationship, and available CI evidence; separates observation from inference and missing evidence; and produces a provenance-backed, uncertainty-aware decision report.

A passing build, version number, compatibility score, merged status, generated changelog, model output, or agent conclusion alone does not establish that an update is appropriate or safe.

## 4. Technical thesis

Primary thesis:

> Repository-specific usage context, dependency-path evidence, upstream behavioral changes, and available CI history can produce more useful and better-calibrated decisions than a transparent baseline using only version-change category, current CI conclusion, dependency directness, and release-note keywords.

That keyword baseline is a comparative decision baseline, not the accepted
architecture for interpreting natural-language evidence.

Later experiments may test whether structural/graph features, learned ranking, grounded LLM synthesis, or bounded multi-agent investigation materially improve decision quality over simpler baselines.

Every admitted experiment requires:

- an observed limitation;
- a simpler baseline;
- a bounded hypothesis;
- measurable success and rejection conditions;
- explicit cost and new failure modes;
- an adopt, retain-as-pilot, reject, or defer decision.

Incremental experiments may begin with one evidence type or semantic category,
but selected product methods must be evaluated against the complete owning
responsibility. A fixture-sized, phrase-enumerating, or category-by-category
handcrafted solution remains a baseline or disposable experiment unless it has a
credible generalization path across that responsibility. The controlling
acceptance rules are in
`docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`.

## 5. Frozen 90-day product boundary

Included:

- public GitHub-hosted Python repositories;
- Dependabot pull requests;
- PyPI and lawful public upstream evidence;
- public repository files and available public CI metadata through authorized interfaces;
- one primary workflow: dependency-update review;
- one output family: evidence-backed decision reports;
- Python as the primary implementation language;
- one application repository;
- one main persistence system when justified;
- one supported core deployment model;
- deterministic baseline and evidence evaluation;
- bounded later experiments admitted by evidence.

Outside the frozen core:

- private repositories or private alert details;
- automatic merge, approval, commenting, or external mutation;
- universal language/package-manager/update-bot support;
- generic vulnerability scanning or exploitability prediction;
- a separate generic CI, code-review, agent, or MLOps platform;
- enterprise authentication, multi-tenancy, multiple databases, or unjustified vector infrastructure;
- autonomous external actions;
- high-availability or multi-region production operation;
- claims that an update is objectively safe.

## 6. Required core outcome

The supported core must eventually demonstrate:

- one real public Dependabot PR through the complete product flow;
- lawful evidence acquisition with time/revision context;
- explicit raw, trusted, missing, inaccessible, stale, invalid, conflicting, rejected, unsupported, and not-applicable behavior where relevant;
- tested central contracts and transformations;
- deterministic bounded recommendation or abstention;
- traceability from material factual claims to evidence;
- uncertainty, degradation, or abstention under insufficient evidence;
- persisted/replayable runs when that milestone activates;
- clean-setup reproducibility;
- appropriate unit, integration, failure, and recovery tests;
- CI and secure configuration for supported behavior;
- a CLI and/or API exposing the supported user flow when justified;
- staged-corpus evaluation of the deterministic baseline;
- explicit truth/label limitations;
- Ali's ability to explain, modify, test, query, and diagnose the central path;
- accurate portfolio language distinguishing implemented, measured, experimental, rejected, and future behavior.

The core does not require a successful learned model or permanent adoption of graph, LLM, agent, service, queue, Kubernetes, or multi-cloud architecture.

## 7. Advanced-system obligations

The existing approved career strategy remains unchanged:

- A1 hands-on exposure for distributed queues, advanced MLOps, microservices, Kubernetes, multi-cloud, and bounded autonomous multi-agent systems;
- at least two A2 project-integrated pilots unless an explicit strategic review changes the requirement;
- A3 permanent adoption only when project evidence justifies it.

These obligations are implemented through the project plan and evidence-gated packages. They do not authorize premature architecture.

## 8. Evidence doctrine

- Preserve source identity, time/revision, and transformation context for material evidence.
- Keep observation, inference, uncertainty, and decision distinct.
- Represent missing or degraded evidence explicitly rather than inventing certainty.
- Prefer reproducible commands, tests, outputs, and preserved artifacts over prose claims.
- Freeze evaluation cases, labels/rubrics, versions, and contamination controls before final comparison.
- A negative experiment or rejection decision is valid when method and evidence are rigorous.
- AI assistance must be disclosed; generated artifacts do not establish Ali-owned capability.

## 9. Technology admission

A new technology, model family, representation, service, or major module enters only when:

1. an observable product or evaluation limitation exists;
2. a simpler credible baseline is inadequate;
3. success and rejection conditions are defined;
4. the smallest viable experiment is bounded;
5. security, maintenance, cost, and cleanup are explicit;
6. Ali can increasingly explain and modify the responsibility;
7. the supported core remains runnable;
8. permanent adoption follows comparative evidence.

## 10. Reframe or termination

Formally narrow, reframe, or terminate a responsibility when evidence shows:

- public evidence cannot support output more useful than a simple PR summary;
- repository context cannot be acquired or interpreted within the boundary;
- defensible evaluation cannot be constructed;
- recommendations depend mainly on undocumented intuition;
- useful operation requires private or inaccessible evidence;
- the product becomes a generic scanner, CI, code-review, agent, or MLOps platform;
- missing evidence is hidden;
- experiments proceed without baseline and rejection gates;
- advanced exposure prevents core completion or ownership;
- Ali cannot increasingly modify, test, query, and diagnose the central flow;
- legal, privacy, credential, safety, or material cost constraints appear;
- the deterministic baseline already solves the decision sufficiently.

Use the smallest necessary correction. A failed hypothesis does not automatically terminate the mission.

## 11. Claim limits

Default language is **production-oriented**, not production-ready.

Do not claim:

- update safety;
- professional mastery from project exposure;
- production scale or reliability without evidence;
- independent ownership of AI-generated work;
- successful technology adoption merely because a pilot ran;
- implemented behavior from plans, specifications, or ADRs alone.

## 12. Change control

Change this charter only when the mission, user, supported decision, frozen boundary, required outcomes, evidence doctrine, admission rules, termination conditions, or claim limits change.

Do not update it for ordinary project progress, tests, commits, current plans, exact next actions, or Career review state.
