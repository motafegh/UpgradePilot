# UpgradePilot Evidence-Derived Learning and Building Plan

**Status:** Controlling project-local route and gate plan  
**Owner:** Ali Rajabi  
**Activated:** 2026-07-23  
**Current stage:** B1 — Implementation responsibility freeze  
**D1 acceptance:** [`D1_ACCEPTANCE_AND_B1_ACTIVATION.md`](D1_ACCEPTANCE_AND_B1_ACTIVATION.md)  
**Clean reset:** [`../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md`](../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md)

## 1. Authority

This file is the single owner of UpgradePilot's project route. It replaces the historical
M0–M8 decomposition and the superseded M2-S03 report-first path.

Other authority owners retain bounded responsibilities:

- [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md) — mission, user, supported boundary,
  evidence doctrine, and claim limits;
- [`../OPERATING_GUIDE.md`](../OPERATING_GUIDE.md) — ordinary learning and execution;
- [`B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md`](B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md)
  — active B1 procedure;
- [`B1_CURRENT_SOURCE_AND_TEST_RECONCILIATION.md`](B1_CURRENT_SOURCE_AND_TEST_RECONCILIATION.md)
  — completed source inspection and clean-reset consequence;
- [`../MEMORY.md`](../MEMORY.md) — exact continuation;
- active source, tests, commands, outputs, and environment — implemented truth;
- [`../archive/2026-07-23_PRE_B2_M2_IMPLEMENTATION.md`](../archive/2026-07-23_PRE_B2_M2_IMPLEMENTATION.md)
  — historical pre-reset implementation only.

The supported core remains a Python implementation for maintainers of public Python
repositories receiving Dependabot dependency-update pull requests.

## 2. Evidence-derived runtime

S001–S005 exposed this minimum product flow:

```text
invocation
→ exact frozen case identity
→ material operations
→ evidence and evidence states
→ claims and interpretations
→ findings
→ transparent baseline
→ conditional-stage activation or non-activation
→ bounded decision or abstention
→ machine and human reports
→ follow-up, rerun, supersession, and changed-boundary transitions
→ review, ownership, and validation
```

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
3. Learn through the owning product responsibility.
4. Build the smallest complete credible supported core.
5. Separate universal and conditional work.
6. Preserve identity, provenance, uncertainty, and degraded evidence states.
7. Prefer deterministic trust controls before semantic automation.
8. Admit dependencies, models, graphs, agents, services, databases, queues, and
   infrastructure only through observed need and comparative evidence.
9. Increase Ali's control through prediction, implementation, testing, diagnosis, and
   explanation.
10. Stop when further work has no material decision, uncertainty, actionability, learning,
    or product value.
11. Historical implementation does not control new design merely because it exists or once
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
| B1 — Implementation responsibility freeze | **Active** | Clean-slate minimum executable responsibility, boundary, tests, ownership work, and one bounded B2 plan accepted |
| B2 — Executable run kernel | Pending | Replay/fixture-to-decision flow with lineage, reports, transitions, tests, and Ali-owned change |
| B3 — Public acquisition and replay | Pending | Exact public acquisition with raw preservation and explicit source failure |
| B4 — Deterministic context and decision support | Pending | Supported Python dependency, CI-authority, target-relevance, conditional-stage, and decision behavior |
| B5 — Persistence, diagnosis, and evaluation | Pending | Justified storage, replay, diagnostics, corpus evaluation, cost, and stopping evidence |
| X1 — Evidence-gated experiments | Pending | Measured adoption or rejection of advanced methods |
| C1 — Hardening, ownership, and portfolio closure | Pending | Reproducible supported core and evidence-indexed ownership proof |

Stages are evidence gates, not calendar promises.

## 6. D1 closure

D1 is complete because:

- the technical evidence gate was satisfied by five contrasting cases;
- stable and conditional responsibilities can be stated at the useful current depth;
- Ali accepted the synthesis, limitations, and replay-first rationale;
- no named discovery uncertainty requires S006 before B1.

D1 acceptance does not authorize B2 implementation or freeze production schemas.

## 7. B1 — Active clean-slate responsibility freeze

B1 is controlled by
[`B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md`](B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md).

### Completed B1 work

- pre-reset package, source, tests, scripts, outputs, and historical execution evidence were
  inspected;
- the implementation was found narrower than the accepted D1 runtime;
- Ali rejected source inheritance for learning clarity;
- the exact old implementation was archived at immutable commit
  `e7425dcfc20f093ac10c9a903f1c4ae50a8b2638`;
- M2 source, tests, scripts, and generated outputs were removed from active paths;
- active package metadata was reset to no runtime dependencies;
- ADR-0002's Pydantic decision was superseded;
- ADR-0001's source/package layout remains accepted.

### Remaining required work

1. Freeze the minimum complete replay-to-decision responsibility.
2. Define what replay fixtures may contain as captured evidence or labeled prepared
   interpretation.
3. Ensure no unexplained final decision or hidden expected action is supplied by callers.
4. Define what B2 must execute and validate deterministically.
5. Compare the standard-library baseline with any proposed dependency; inherit none.
6. Choose the smallest reversible representation and one bounded interface.
7. Define universal and conditional runtime responsibilities.
8. Define B2 acceptance tests and Ali-owned implementation, testing, diagnosis, and
   explanation work.
9. Create one bounded B2 implementation plan only after the responsibility is accepted.
10. Create another ADR only for a durable consequential method choice.

### B1 authorization boundary

B1 authorizes analysis, responsibility freezing, method comparison, and bounded planning.
It does not authorize B2 product-code changes.

### B1 exit gate

B1 passes only when:

- the responsibility is derived from S001–S005, not archived source;
- it generalizes beyond one replay fixture inside the charter boundary;
- no required product behavior is hidden as unexplained caller interpretation;
- universal and conditional responsibilities are explicit;
- the dependency and representation baseline is reversible and adequate;
- security, untrusted-input, credential, and target-mutation boundaries are explicit;
- rejected and deferred methods remain recorded;
- B2 tests and Ali ownership work are concrete;
- archived code and tests have no active runtime or coverage role;
- Ali can explain why the slice is the smallest credible complete executable core;
- one bounded B2 plan is accepted.

## 8. B2 — Executable run kernel

After B1 acceptance, one clean command or bounded application interface should consume a
real-shaped replay fixture and produce reproducible run state, a bounded decision, both
report forms, and transitions.

Minimum behavior:

- invocation distinct from frozen identity;
- stable run and record IDs;
- material operation history;
- evidence states and provenance;
- observation/interpretation/finding separation;
- transparent baseline execution;
- conditional-stage activation or non-activation;
- bounded decision or abstention;
- machine and human reports from the same state;
- follow-up, rerun, supersession, and changed-boundary transitions;
- structural validation;
- invalid, missing, changed-evidence, same-action, action-change, degraded, and early-stop
  tests;
- no credentials or target mutation.

Live acquisition, persistence, services, queues, agents, and models are not required for
B2.

Ali must trace one run, implement or modify central behavior, add or change a meaningful
test, diagnose a failure, and explain evidence authority and claim limits.

## 9. B3 — Public acquisition and replay

Add lawful public GitHub, PyPI, repository, and upstream acquisition only after the B2
kernel exists.

Required behavior includes exact identity, bounded authorized acquisition, raw preservation
or durable references, explicit inaccessible/missing/expired/stale/invalid states,
untrusted-content handling, replay independent of live availability, and acquisition
failure/recovery tests.

## 10. B4 — Deterministic context and decision support

Add supported Python behavior for dependency declarations and locks, role/path evidence,
repository usage, CI dependency identity and responsibility, version and constraint
comparisons, upstream activation-condition mapping, targeted checks, action changes,
stopping, abstention, and conditionally activated analysis.

Acceptance must be demonstrated on supported Python cases.

## 11. B5 — Persistence, diagnosis, and evaluation

Select durable infrastructure only after real run, replay, query, diagnosis, and evaluation
needs exist.

Required outcomes include idempotent storage, supersession, useful queries, diagnostics,
setup and cleanup, staged corpus identity, baseline/full comparisons, coverage, abstention,
cost/stopping analysis, and explicit truth/adjudication limits.

Do not select a database, queue, or service because a historical milestone named it.

## 12. X1 — Evidence-gated experiments

Any model, graph, LLM, agentic, distributed, MLOps, microservice, Kubernetes, or multi-cloud
experiment requires an observed limitation, bounded hypothesis, simpler baseline,
measurable acceptance and rejection rules, security/cost controls, cleanup, and an
adopt/pilot/reject/defer decision.

## 13. C1 — Hardening and ownership

Closure requires reproducible supported-core execution, representative normal/failure/
changed/early-stop cases, secure configuration, tests and CI, run/diagnosis/recovery
instructions, limitations and claim register, assistance disclosure, implemented
architecture explanation, reviewer demonstration, portfolio evidence, and Ali's ability to
modify, test, diagnose, and defend the central flow.

## 14. Learning-by-building cycle

```text
real responsibility
→ minimum blocking concept
→ Ali predicts or challenges
→ bounded investigation or implementation
→ inspect evidence
→ diagnose and correct
→ Ali modifies or tests a central part
→ Ali explains path, authority, and limits
→ record demonstrated depth
```

## 15. Capacity and scope

Standard planning capacity remains up to 24 focused hours per week as a ceiling, not a
quota. Preserve core behavior, evidence integrity, and ownership work first. Defer optional
breadth and experiments before weakening evaluation.

## 16. Current authorized sequence

1. Keep B2 implementation paused.
2. Freeze the clean-slate minimum executable responsibility.
3. Define replay fixture contents and deterministic B2 behavior.
4. Select the smallest dependency, representation, and bounded interface.
5. Define universal and conditional responsibilities.
6. Define B2 acceptance tests and Ali ownership work.
7. Review and accept the freeze.
8. Create and accept one bounded B2 implementation plan.
9. Begin the replay-to-decision kernel only after B1 passes.

Do not restore archived M2 source, resume M2-S03, select S006 without a named blocker,
require a fixed case count, or select permanent architecture before its evidence gate.