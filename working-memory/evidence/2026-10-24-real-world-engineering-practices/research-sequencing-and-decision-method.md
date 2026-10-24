# Real-world engineering practices — research sequencing and decision method

**Status:** active research guidance, non-controlling  
**Branch:** `research/real-world-engineering-practices-2026-10-24`  
**Purpose:** define how to continue the project-fit study without turning it into an unbounded glossary or premature architecture rewrite.

## Research objective

The objective is not to collect industry terminology. It is to determine, with transferable engineering understanding and current UpgradePilot evidence, which practices/patterns/mechanisms:

- already exist and should simply be recognized/named accurately;
- are partially present and deserve clearer ownership or boundaries;
- solve a real current or foreseeable UpgradePilot problem and may merit later adoption;
- are useful learning but currently unnecessary;
- should be explicitly rejected for this product boundary.

No concept is admitted because it is common, fashionable, or impressive in a portfolio.

## Unit of research

Do not study every term in isolation. Prefer **pressure-centered clusters**. A cluster groups concepts that address the same real engineering concern and lets us compare alternatives rather than accidentally adopting several overlapping mechanisms.

For each selected concept use three passes:

1. **Learn** — precise professional meaning, nearby terms, common misuse, and a concrete real-world failure/pressure it addresses.
2. **Map** — inspect UpgradePilot's current source/tests/specifications/ADRs/history to determine whether the responsibility already exists, partially exists, or is genuinely absent.
3. **Decide** — benefit, cost, failure modes, evidence trigger and disposition candidate. Record whether any later product/design responsibility is actually warranted.

External real-world references should be consulted when the professional term, standard practice, or trade-off needs grounding. UpgradePilot's own implementation claims must come from repository evidence, not from external descriptions.

## Recommended sequencing

### Track 1 — Project understanding and documentation architecture

Start here because we have already found a concrete gap and it improves every later research track.

Study together:

- Project Engineering Guide;
- handbook vs guide vs playbook vs runbook;
- documentation taxonomy and information architecture;
- architecture/system diagrams;
- glossary/ubiquitous terminology where useful;
- working-memory as engineering-history/provenance layer;
- decision log / ADR / specification / plan boundaries;
- onboarding and contributor-facing documentation.

Expected result: a defensible documentation model and a refined Engineering Guide template, without yet promoting it to `main`.

### Track 2 — Architecture and responsibility boundaries

Study the concepts most likely to accurately describe or challenge the current architecture:

- modular monolith;
- layered architecture;
- Dependency Injection and Inversion of Control;
- Ports and Adapters / Hexagonal architecture;
- Clean Architecture;
- Domain-Driven Design and bounded contexts;
- adapters / anti-corruption layers / facades / strategies;
- state machines;
- Strangler migration;
- repository pattern;
- explicit contrasts with microservices, CQRS, event sourcing and plugin architecture.

Primary question: **what architecture do we actually have, and which standard vocabulary improves reasoning without forcing a rewrite?**

Expected result: an evidence-backed architecture terminology map suitable for the future Engineering Guide and possibly later architecture documentation cleanup.

### Track 3 — State, persistence, concurrency and reproducibility

This cluster maps directly to Workspace and report/recovery responsibilities:

- immutable revisions and snapshots;
- checkpointing;
- transactions / ACID boundaries;
- optimistic concurrency / compare-and-swap;
- idempotency;
- Unit of Work;
- schema evolution and migrations;
- backward compatibility;
- reconstruction vs recovery vs deterministic replay;
- content-addressing / integrity hashes;
- caching and cache invalidation only if a real need appears.

Primary question: **which established distributed/state-management concepts accurately explain Workspace, and where are real correctness gaps versus terminology gaps?**

### Track 4 — Verification, testing and evidence quality

Study together:

- unit/integration/E2E/acceptance distinctions;
- contract testing and Consumer-Driven Contracts;
- property-based testing;
- fuzzing;
- fault injection;
- differential testing;
- metamorphic testing;
- golden/snapshot testing;
- mutation testing;
- hermetic/reproducible fixtures;
- independent evaluation vs regression proof.

Primary question: **which verification techniques would actually find classes of UpgradePilot defects our current test strategy can miss?**

Do not add a technique solely for test-count or portfolio value.

### Track 5 — Security and trust engineering

High-value because UpgradePilot consumes untrusted public evidence and may involve models, credentials, storage and future execution boundaries.

Study together:

- threat modeling;
- trust boundaries;
- least privilege;
- secure-by-default / fail-closed behavior;
- input validation;
- secret management;
- sandboxing if target execution expands;
- software-supply-chain practices such as SBOM/SLSA only against a concrete release/distribution need;
- SSDLC as an umbrella practice.

Primary question: **what threats and trust transitions are real for UpgradePilot today, and which controls are missing or merely unnamed?**

### Track 6 — Reliability, operations and observability

Study only to the depth justified by the current local/CLI deployment model:

- timeouts;
- retries/backoff/jitter;
- rate limits;
- graceful degradation;
- structured logging;
- metrics;
- observability;
- health/readiness checks;
- circuit breakers/bulkheads;
- OpenTelemetry/distributed tracing;
- SLI/SLO/SLA/error budgets.

Primary question: **what operational evidence would we actually need to diagnose and support the product we currently run?**

Expect some concepts to be deliberately deferred until a persistent service/deployment exists.

### Track 7 — Delivery, compatibility and release engineering

Study:

- CI vs Continuous Delivery vs Continuous Deployment;
- release engineering;
- packaging and clean-install proof;
- Semantic Versioning;
- API/schema/version compatibility;
- deprecation policy;
- migration policy;
- release provenance and distribution controls.

Primary question: **what does UpgradePilot need before it can make stronger public/portfolio distribution and production-oriented engineering claims?**

### Track 8 — AI/agent engineering

Study last enough that ordinary software-engineering fundamentals remain the reference frame:

- human-in-the-loop;
- offline/online evals;
- grounded generation;
- entailment/claim validation;
- model/prompt/version tracing;
- guardrails;
- LLM-as-judge;
- red teaming;
- model governance;
- multi-agent architecture.

Primary question: **which AI-specific mechanisms add evidence-backed capability beyond deterministic owners, and which merely add orchestration complexity?**

This track should reuse UpgradePilot's existing semantic-failure evidence rather than assuming more agent roles or prompts solve it.

## Research cadence

For each cluster:

```text
orientation to professional concepts
→ select 2–5 most relevant terms
→ inspect current UpgradePilot owners/source/tests/history
→ compare mechanisms and boundaries
→ record per-term dispositions
→ write a short cluster synthesis
→ decide whether any concept needs deeper experiment/design
→ continue to next cluster
```

Avoid researching every inventory item at equal depth. Terms may be closed quickly when clearly irrelevant or already understood.

## Decision gates

A concept can produce one of three broad outcomes:

### Learning-only outcome

No project mutation needed. Preserve the accurate term, mapping and rejection/defer rationale.

### Documentation/terminology outcome

The project already has the mechanism, but future documentation could name or explain it more clearly. Candidate material may feed the Engineering Guide or existing canonical documentation after final reconciliation.

### Engineering-change candidate

A real gap exists. Record:

- exact product/engineering problem;
- current evidence;
- candidate mechanism and alternatives;
- expected benefit;
- complexity/failure modes;
- trigger and proof required;
- correct future owner (plan/specification/ADR/security/operations/etc.).

Do not implement it on this research branch unless Ali explicitly changes the branch responsibility.

## Cross-cluster synthesis

Maintain a final matrix containing at least:

- concept;
- professional meaning;
- current UpgradePilot mapping;
- present/partial/absent status;
- evidence anchors;
- disposition;
- project pressure solved;
- adoption trigger;
- expected cost/risk;
- future owner if promoted;
- Engineering Guide relevance;
- transferable learning value.

Also produce a smaller **recommended action set** grouped into:

1. no change — already good / terminology learned;
2. documentation improvements;
3. low-risk engineering improvements;
4. bounded experiments/designs worth considering;
5. deferred until a named maturity/deployment trigger;
6. explicit rejections.

## Relationship to the engineering journey

`working-memory/` remains the broad engineering evidence trail. During each cluster, use historical records selectively to understand how current mechanisms emerged, including failed assumptions, corrections, experiments, rejected approaches and proof transitions.

Do not treat historical working-memory as current authority. Current source/tests and canonical accepted owners define present truth; history explains the engineering path to that truth.

The future Engineering Guide should consume only the historically important transitions that materially improve understanding. It should not reproduce this entire research record or the whole project chronology.

## Recommended immediate next step

Complete **Track 1 — Project understanding and documentation architecture** first, because it is already active and will give us the structure for recording and communicating every later result. Then move to **Track 2 — Architecture and responsibility boundaries**, where the highest-value first concepts are likely:

1. modular monolith;
2. layered architecture;
3. Dependency Injection vs Inversion of Control;
4. Ports and Adapters / Hexagonal architecture;
5. DDD / bounded context only after the simpler architecture mapping is clear.

This order intentionally starts from observable structure and moves toward stronger architectural labels, reducing the risk of forcing UpgradePilot into a fashionable pattern.