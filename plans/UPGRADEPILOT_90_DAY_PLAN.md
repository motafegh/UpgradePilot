# UpgradePilot Evidence-Derived Learning and Building Plan

**Status:** Controlling project-local route and gate plan  
**Owner:** Ali Rajabi  
**Activated:** 2026-07-23  
**Current stage:** B2 — Public PR vertical slice  
**D1 acceptance:** [`D1_ACCEPTANCE_AND_B1_ACTIVATION.md`](D1_ACCEPTANCE_AND_B1_ACTIVATION.md)  
**Clean reset:** [`../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md`](../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md)

## 1. Authority

This file is the single owner of UpgradePilot's project route. It replaces the historical
M0–M8 decomposition and the superseded M2-S03 report-first path.

Other authority owners retain bounded responsibilities:

- [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md) — mission, user, supported boundary,
  evidence doctrine, and claim limits;
- [`../OPERATING_GUIDE.md`](../OPERATING_GUIDE.md) — ordinary learning and execution,
  including post-run learning-depth and ownership review;
- [`B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md`](B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md)
  — completed B1 boundary and B2 entry requirements;
- [`B1_CURRENT_SOURCE_AND_TEST_RECONCILIATION.md`](B1_CURRENT_SOURCE_AND_TEST_RECONCILIATION.md)
  — completed source inspection and clean-reset consequence;
- [`../MEMORY.md`](../MEMORY.md) — exact continuation;
- active source, tests, commands, outputs, and environment — implemented truth;
- [`../archive/2026-07-23_PRE_B2_M2_IMPLEMENTATION.md`](../archive/2026-07-23_PRE_B2_M2_IMPLEMENTATION.md)
  — historical pre-reset implementation only.

The supported core remains a Python implementation for maintainers of public Python
repositories receiving Dependabot dependency-update pull requests.

## 2. Evidence-derived product flow

S001–S005 exposed the responsibilities below. Implementation and learning must follow the
real user-visible flow rather than begin from an artificial replay-only interface:

```text
public repository and Dependabot PR locator
→ read-only public acquisition
→ exact base, head, changed-file, dependency, and version identity
→ relevant repository, CI, package, and upstream evidence
→ explicit evidence states and provenance
→ observations, interpretations, and findings
→ transparent baseline and bounded context evaluation
→ conditional-stage activation or non-activation
→ bounded decision or abstention
→ concise human and machine output
→ captured evidence for reproducibility, testing, rerun, and later replay
→ review, ownership, and validation
```

Replay is a supporting reproducibility and testing capability. It must not replace the real
PR-to-decision path as the primary product interface or learning sequence.

The cases established that:

- CI color lacks authority without dependency identity, trigger, job, step, command,
  revision, environment, scope, and result;
- dependency role and path may include lock, transitive, development/test, adapter,
  framework, deployment-installation, and peer-support relationships;
- missing, expired, inaccessible, conflicting, stale, and failed-method evidence can change
  the action;
- advisory, compatibility, repeated-execution, attribution, dynamic-execution, platform,
  and similar work are conditional;
- the transparent baseline may be sufficient or wrong;
- upstream caution requires mapping to target activation conditions;
- non-activation and justified stopping are product state;
- simulation artifacts are discovery evidence, not approved production schemas.

## 3. Route principles

1. Evidence gates control advancement; dates, hours, case counts, and artifact counts do
   not.
2. One active route exists.
3. Learn and build through the real end-to-end product responsibility.
4. Build the thinnest complete credible vertical slice before isolated internal subsystems.
5. Use captured responses and replay to test and reproduce real behavior, not to substitute
   for the real product flow.
6. Separate universal and conditional work.
7. Preserve identity, provenance, uncertainty, and degraded evidence states.
8. Prefer deterministic trust controls before semantic automation.
9. Admit dependencies, models, graphs, agents, services, databases, queues, and
   infrastructure only through observed need and comparative evidence.
10. Increase Ali's control through prediction, implementation, testing, diagnosis, and
    explanation.
11. After each meaningful real run, review only career- and responsibility-relevant learning
    as must-master, operational, deliberately deferred, and Ali-owned practice under the
    operating guide.
12. Stop when further work has no material decision, uncertainty, actionability, learning,
    or product value.
13. Historical implementation does not control new design merely because it exists or once
    passed tests.

## 4. Discovery evidence

| Case | Contrast | Baseline/full relationship | Full action |
|---|---|---|---|
| S001 | transitive docs/advisory path and relevant green CI | same action; stronger authority and calibration | merge after normal review |
| S002 | adapter path and skipped relevant tests | same action; exact missing authority and checks | run targeted checks |
| S003 | failing install, peer conflict, causal comparison | same broad action; cause and recovery added | block current proposal as-is |
| S004 | exact relevant green control and early stop | baseline sufficient | merge after normal review |
| S005 | exact lock-backed matrix and target-scoped caution | baseline wrong action | merge after normal review |

Controlling discovery records:

- [`../product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](../product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md)
- [`D1_ACCEPTANCE_AND_B1_ACTIVATION.md`](D1_ACCEPTANCE_AND_B1_ACTIVATION.md)

The evidence is contrasting, not representative. It does not prove target safety,
universal correctness, or automated semantic reliability.

## 5. Route overview

| Stage | State | Required outcome |
|---|---|---|
| D0 — Initial evidence base | Complete | Initial runtime and artifact responsibilities exposed |
| D1 — Contrast closure | **Passed** | S001–S005 synthesized and accepted by Ali |
| B1 — Implementation responsibility freeze | **Passed for B2 entry** | Real PR-first boundary, clean source baseline, minimum acquisition/error model, first interface, tests, and ownership direction accepted |
| B2 — Public PR vertical slice | **Active** | One public Python Dependabot PR locator through minimum read-only acquisition, exact identity, bounded evidence evaluation, recommendation or abstention, concise output, tests, and Ali-owned change |
| B3 — Acquisition and replay robustness | Pending | Raw preservation, changed-head handling, source failures, rate limits, recovery, deterministic replay, and broader required public-source acquisition |
| B4 — Deterministic context and decision support | Pending | Supported Python dependency, CI-authority, target-relevance, conditional-stage, stopping, targeted-check, and action-change behavior |
| B5 — Persistence, diagnosis, and evaluation | Pending | Justified storage, diagnostics, corpus evaluation, cost, and stopping evidence |
| X1 — Evidence-gated experiments | Pending | Measured adoption or rejection of advanced methods |
| C1 — Hardening, ownership, and portfolio closure | Pending | Reproducible supported core and evidence-indexed ownership proof |

Stages are evidence gates, not calendar promises.

## 6. D1 and B1 closure

D1 is complete because:

- the technical evidence gate was satisfied by five contrasting cases;
- stable and conditional responsibilities can be stated at the useful current depth;
- Ali accepted the synthesis and limitations;
- no named discovery uncertainty requires S006 before B1.

D1 acceptance did not permanently fix implementation order. During B1, Ali identified that
a replay-first learning and implementation sequence obscured the real product workflow. The
route now starts B2 with the thinnest real public PR-to-decision vertical slice while keeping
replay as supporting test and reproducibility behavior.

B1 passed for B2 entry because:

- the active source was reset independently of archived M2 implementation;
- the first interface begins with a public repository and PR number;
- the no-target-mutation and public read-only boundary is explicit;
- the initial HTTP, timeout, ambiguous `404`, response-validation, and test boundaries were
  understood and accepted;
- `Requests` was selected as the smallest adequate current HTTP dependency;
- Ali explicitly authorized the first increment, installed it, ran its tests, and completed
  the live S004 identity request in WSL.

B1 closure does not claim that the whole B2 responsibility is implemented or independently
owned.

## 7. B2 — Active public PR vertical slice

One clean command accepts a public GitHub repository and PR number and incrementally grows
toward a bounded recommendation or abstention from newly acquired public evidence.

Minimum complete B2 behavior remains:

- validate the public repository and PR locator;
- acquire PR metadata read-only from GitHub;
- freeze exact repository, PR, base, head, and changed-file identity;
- identify one supported Python dependency-version change without repository-specific
  hardcoding;
- acquire the minimum relevant exact-head check or workflow evidence available through the
  authorized interface;
- acquire the minimum public upstream or package evidence required by the selected slice;
- preserve source, revision/time context, evidence state, and acquisition failure;
- execute a transparent baseline and the bounded evidence-authority check;
- activate or decline only the conditional work required by the case;
- produce a bounded recommendation or abstention with reasons, uncertainty, and claim
  limits;
- produce one concise human-readable result and the minimum machine-readable state needed
  for testing and traceability;
- capture acquired responses or normalized evidence for deterministic tests and later
  replay;
- perform no target mutation and require no private repository access.

### Implemented increment 1

```text
repository + PR number
→ read-only GitHub PR request
→ exact base/head identity validation
→ concise identity output
```

This increment is validated by active unit tests and Ali's successful live WSL run against
`googlefonts/glyphsLib#1145`. It does not yet establish changed-file extraction, CI
authority, dependency recommendation, or independent Ali ownership.

### B2 implementation rhythm

For each bounded increment:

```text
real next responsibility
→ teach the minimum blocking concepts
→ Ali predicts or challenges
→ implement one bounded capability
→ run unit/integration evidence and a safe real example where applicable
→ inspect success or failure
→ classify must-master, operational, deferred, and Ali-owned learning
→ Ali explains, modifies, tests, or diagnoses one central boundary
→ record only material continuation and evidence
```

Do not study all source lines equally. Deepen syntax, code, frameworks, or internals only
when they are central to the active responsibility, diagnosis, safety, target career, or
ownership transfer.

The first slice does not require persistence, services, queues, agents, models, deployment
infrastructure, exhaustive repository analysis, or a complete future artifact family.

Ali must progressively trace the real request and evidence path, implement or materially
modify central behavior, add or change meaningful tests, diagnose acquisition/identity/
evaluation failures, and explain evidence authority and claim limits.

## 8. B3 — Acquisition and replay robustness

Strengthen the real acquisition path after the first vertical slice exists.

Required behavior includes:

- raw response preservation or durable references where justified;
- explicit inaccessible, missing, expired, stale, invalid, conflicting, and failed-source
  states;
- changed-head detection and clean new-analysis boundaries;
- rate-limit, timeout, network, malformed-response, and partial-source handling;
- secure optional credential handling if evidence justifies authenticated public access;
- deterministic replay independent of live availability;
- acquisition failure and recovery tests;
- broader GitHub, PyPI, repository, and upstream acquisition required by the supported
  product boundary.

## 9. B4 — Deterministic context and decision support

Expand supported Python behavior for dependency declarations and locks, direct and
transitive relationships, role/path evidence, repository usage, CI dependency identity and
responsibility, version and constraint comparisons, upstream activation-condition mapping,
targeted checks, action changes, stopping, abstention, and conditionally activated analysis.

Acceptance must be demonstrated on supported Python cases.

## 10. B5 — Persistence, diagnosis, and evaluation

Select durable infrastructure only after real run, replay, query, diagnosis, and evaluation
needs exist.

Required outcomes include idempotent storage, supersession, useful queries, diagnostics,
setup and cleanup, staged corpus identity, baseline/full comparisons, coverage, abstention,
cost/stopping analysis, and explicit truth/adjudication limits.

Do not select a database, queue, or service because a historical milestone named it.

## 11. X1 — Evidence-gated experiments

Any model, graph, LLM, agentic, distributed, MLOps, microservice, Kubernetes, or multi-cloud
experiment requires an observed limitation, bounded hypothesis, simpler baseline,
measurable acceptance and rejection rules, security/cost controls, cleanup, and an
adopt/pilot/reject/defer decision.

## 12. C1 — Hardening and ownership

Closure requires reproducible supported-core execution, representative normal/failure/
changed/early-stop cases, secure configuration, tests and CI, run/diagnosis/recovery
instructions, limitations and claim register, assistance disclosure, implemented
architecture explanation, reviewer demonstration, portfolio evidence, and Ali's ability to
modify, test, diagnose, and defend the central flow.

## 13. Learning-by-building cycle

```text
real user-visible responsibility
→ minimum blocking concept
→ Ali predicts or challenges
→ one bounded implementation or investigation action
→ inspect actual source, response, test, or failure evidence
→ diagnose and correct
→ classify required learning depth
→ Ali modifies or tests a central part
→ Ali explains the path, authority, and limits
→ record demonstrated depth only when material
```

Internal terminology and artifacts are introduced only when the implemented responsibility
creates the need for them. The detailed operating rule is owned by
[`../OPERATING_GUIDE.md`](../OPERATING_GUIDE.md), especially its post-run learning and
ownership review.

## 14. Capacity and scope

Standard planning capacity remains up to 24 focused hours per week as a ceiling, not a
quota. Preserve core behavior, evidence integrity, and ownership work first. Defer optional
breadth and experiments before weakening evaluation.

## 15. Current authorized sequence

1. Continue B2 from the validated public PR identity increment.
2. Trace and understand the central request-to-validated-identity path to the depth required
   for modification and diagnosis; do not study all lines equally.
3. Add changed-file acquisition and one supported pinned Python dependency-change
   extraction.
4. Add deterministic tests, run them in WSL, and run the safe real S004 path.
5. Perform the post-run learning-depth and ownership review.
6. Require one Ali-owned explanation, modification, test, or diagnosis before moving beyond
   the increment.
7. Then add exact-head workflow evidence and continue toward the first bounded recommendation
   or abstention.

Do not restore archived M2 source, resume M2-S03, select S006 without a named blocker,
require a fixed case count, hardcode a known PR result, or select permanent architecture
before its evidence gate.