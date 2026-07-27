# UpgradePilot Evidence-Derived Learning and Building Plan

**Status:** Controlling project-local route and gate plan  
**Owner:** Ali Rajabi  
**Activated:** 2026-07-23  
**D1 acceptance record:** [`D1_ACCEPTANCE_AND_B1_ACTIVATION.md`](D1_ACCEPTANCE_AND_B1_ACTIVATION.md)  
**Clean reset decision:** [`../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md`](../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md)

## 1. Authority and state separation

This file is the single owner of UpgradePilot's stage sequence, gate definitions, and required
outcomes. It replaces the historical M0–M8 decomposition and the superseded M2-S03
report-first path.

This file does **not** record which stage is selected, passed, active, pending, blocked, or
next. [`../MEMORY.md`](../MEMORY.md) is the sole owner of that live position and of the exact
continuation.

Other authority owners retain bounded responsibilities:

- [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md) — mission, user, supported boundary,
  evidence doctrine, and claim limits;
- [`../OPERATING_GUIDE.md`](../OPERATING_GUIDE.md) — ordinary learning and execution;
- applicable specifications — stable framework-independent behavior;
- accepted ADRs — durable consequential methods;
- bounded plans — scope, sequence, proof, and stop conditions for one responsibility;
- source, tests, commands, outputs, and environment — implemented truth;
- dated acceptance and working records — historical evidence only.

The supported core remains a Python implementation for maintainers of public Python
repositories receiving Dependabot dependency-update pull requests.

## 2. Evidence-derived product flow

S001–S005 exposed the responsibilities below. Implementation must follow the real
user-visible flow rather than begin from an artificial replay-only interface:

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
→ captured evidence for reproducibility, testing, rerun, and replay
→ review, ownership, and validation
```

Replay is a supporting reproducibility and testing capability. It must not replace the real
PR-to-decision path as the primary product interface.

The discovery cases established that:

- CI colour lacks authority without dependency identity, trigger, job, step, command,
  revision, environment, scope, and result;
- dependency role and path may include lock, transitive, development/test, adapter,
  framework, deployment-installation, and peer-support relationships;
- missing, expired, inaccessible, conflicting, stale, and failed-method evidence can change
  the action;
- advisory, compatibility, repeated-execution, attribution, dynamic-execution, platform,
  and similar work are conditional;
- the transparent baseline may be sufficient or wrong;
- upstream caution requires mapping to target activation conditions;
- non-activation and justified stopping are product states;
- simulation artifacts are discovery evidence, not approved production schemas.

## 3. Route principles

1. Evidence gates control advancement; dates, hours, case counts, and artifact counts do not.
2. One route exists; `MEMORY.md` selects the live position on it.
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
11. Stop when further work has no material decision, uncertainty, actionability, learning,
    or product value.
12. Historical implementation does not control new design merely because it exists or once
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

| Stage | Required outcome |
|---|---|
| D0 — Initial evidence base | Expose initial runtime and artifact responsibilities through real-case evidence. |
| D1 — Contrast closure | Synthesize contrasting cases sufficiently to freeze the first implementation responsibility. |
| B1 — Implementation responsibility freeze | Establish the real PR-first boundary, clean source baseline, minimum acquisition/error model, first interface, tests, and ownership direction required for B2 entry. |
| B2 — Public PR vertical slice | Carry one public Python Dependabot PR locator through minimum read-only acquisition, exact identity, bounded evidence evaluation, recommendation or abstention, concise output, tests, and one central owner-controlled change. |
| B3 — Acquisition and replay robustness | Add raw preservation, changed-head handling, source failures, rate limits, recovery, deterministic replay, and broader required public-source acquisition. |
| B4 — Deterministic context and decision support | Expand supported dependency, CI-authority, target-relevance, conditional-stage, stopping, targeted-check, and action-change behavior. |
| B5 — Persistence, diagnosis, and evaluation | Add justified storage, diagnostics, corpus evaluation, cost, and stopping evidence. |
| X1 — Evidence-gated experiments | Measure and adopt, pilot, reject, or defer advanced methods against simpler baselines. |
| C1 — Hardening, ownership, and portfolio closure | Demonstrate a reproducible supported core and evidence-indexed ownership proof. |

Stages are evidence gates, not calendar promises. Their live state belongs only in
`MEMORY.md`.

## 6. D0 — Initial evidence base

Produce enough real-case and manual evidence to reveal the product's decision, evidence,
reporting, stopping, and artifact responsibilities. Do not treat one case as representative.

## 7. D1 — Contrast closure

Use materially contrasting cases to determine:

- which responsibilities are universal;
- which responsibilities are conditional;
- when the baseline is sufficient;
- when target-specific evidence changes the action;
- which uncertainties must remain visible;
- where implementation should begin.

D1 completion requires an accepted synthesis and an explicit implementation-entry decision.

## 8. B1 — Implementation responsibility freeze

Before product implementation expands, establish:

- the smallest complete real user-visible responsibility;
- the public read-only permission boundary;
- exact identity and evidence-authority requirements;
- the clean active source boundary;
- the simplest credible dependencies and methods;
- acceptance tests, claim limits, and stop lines;
- the ownership-bearing work required before stage advancement.

B1 must not inherit archived method choices automatically.

## 9. B2 — Public PR vertical slice

One clean command accepts a public GitHub repository and PR number and grows toward a bounded
recommendation or abstention from newly acquired public evidence.

Minimum complete B2 behavior:

- validate the public repository and PR locator;
- acquire PR metadata read-only from GitHub;
- freeze exact repository, PR, base, head, and changed-file identity;
- identify one supported Python dependency-version change without repository-specific
  hardcoding;
- acquire the minimum relevant exact-head check or workflow evidence available through the
  authorized interface;
- acquire the minimum public package or upstream evidence required by the supported case;
- preserve source, revision/time context, evidence state, and acquisition failure;
- execute a transparent baseline and bounded evidence-authority checks;
- activate or decline only conditional work required by the case;
- produce a bounded recommendation or abstention with reasons, uncertainty, and claim limits;
- produce one concise human-readable result and the minimum machine-readable state needed
  for testing and traceability;
- capture acquired responses or normalized evidence for deterministic tests and replay;
- perform no target mutation and require no private repository access.

For each bounded increment:

```text
real next responsibility
→ identify the minimum blocking concepts and decisions
→ implement one bounded capability
→ run deterministic evidence and a safe real example where applicable
→ inspect success or failure
→ perform the required owner-controlled explanation, modification, test, or diagnosis
→ record live continuation only in MEMORY.md
```

The first slice does not require persistence, services, queues, agents, models, deployment
infrastructure, exhaustive repository analysis, or a complete future artifact family.

## 10. B3 — Acquisition and replay robustness

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

## 11. B4 — Deterministic context and decision support

Expand supported Python behavior for dependency declarations and locks, direct and
transitive relationships, role/path evidence, repository usage, CI dependency identity and
responsibility, version and constraint comparisons, upstream activation-condition mapping,
targeted checks, action changes, stopping, abstention, and conditionally activated analysis.

Acceptance must be demonstrated on supported Python cases.

## 12. B5 — Persistence, diagnosis, and evaluation

Select durable infrastructure only after real run, replay, query, diagnosis, and evaluation
needs exist.

Required outcomes include idempotent storage, supersession, useful queries, diagnostics,
setup and cleanup, staged corpus identity, baseline/full comparisons, coverage, abstention,
cost/stopping analysis, and explicit truth/adjudication limits.

Do not select a database, queue, or service because a historical milestone named it.

## 13. X1 — Evidence-gated experiments

Any model, graph, LLM, agentic, distributed, MLOps, microservice, Kubernetes, or multi-cloud
experiment requires an observed limitation, bounded hypothesis, simpler baseline,
measurable acceptance and rejection rules, security/cost controls, cleanup, and an
adopt/pilot/reject/defer decision.

## 14. C1 — Hardening and ownership

Closure requires reproducible supported-core execution, representative normal/failure/
changed/early-stop cases, secure configuration, tests and CI, run/diagnosis/recovery
instructions, limitations and claim register, assistance disclosure, implemented
architecture explanation, reviewer demonstration, portfolio evidence, and Ali's ability to
modify, test, diagnose, and defend the central flow.

## 15. Capacity and scope

Standard planning capacity remains up to 24 focused hours per week as a ceiling, not a
quota. Preserve core behavior, evidence integrity, and ownership work first. Defer optional
breadth and experiments before weakening evaluation.

Do not restore archived M2 source, resume M2-S03, select another simulation merely to
continue, require a fixed case count, hardcode a known PR result, or select permanent
architecture before its evidence gate.

## 16. Route maintenance

Change this file only when stage order, gate definitions, required outcomes, route principles,
or the stable product flow changes.

Do not update it for:

- stage activation or completion;
- a latest commit or test result;
- an immediate blocker or continuation;
- selection of a bounded plan;
- ordinary implementation progress.

Those live facts belong only in `MEMORY.md`.