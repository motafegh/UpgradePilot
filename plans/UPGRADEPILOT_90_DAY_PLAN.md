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

| Stage | State | Required outcome |
|---|---|---|
| D0 — Initial evidence base | Complete | Initial runtime and artifact responsibilities exposed |
| D1 — Contrast closure | **Passed** | S001–S005 synthesized and accepted by Ali |
| B1 — Implementation responsibility freeze | **Active** | Clean-slate minimum real PR-to-decision vertical slice, boundary, tests, ownership work, and one bounded B2 plan accepted |
| B2 — Public PR vertical slice | Pending | One public Python Dependabot PR locator through minimum read-only acquisition, exact identity, bounded evidence evaluation, recommendation or abstention, concise output, tests, and Ali-owned change |
| B3 — Acquisition and replay robustness | Pending | Raw preservation, changed-head handling, source failures, rate limits, recovery, deterministic replay, and broader required public-source acquisition |
| B4 — Deterministic context and decision support | Pending | Supported Python dependency, CI-authority, target-relevance, conditional-stage, stopping, targeted-check, and action-change behavior |
| B5 — Persistence, diagnosis, and evaluation | Pending | Justified storage, diagnostics, corpus evaluation, cost, and stopping evidence |
| X1 — Evidence-gated experiments | Pending | Measured adoption or rejection of advanced methods |
| C1 — Hardening, ownership, and portfolio closure | Pending | Reproducible supported core and evidence-indexed ownership proof |

Stages are evidence gates, not calendar promises.

## 6. D1 closure

D1 is complete because:

- the technical evidence gate was satisfied by five contrasting cases;
- stable and conditional responsibilities can be stated at the useful current depth;
- Ali accepted the synthesis and limitations;
- no named discovery uncertainty requires S006 before B1.

D1 acceptance did not permanently fix implementation order. During B1, Ali identified that
a replay-first learning and implementation sequence obscured the real product workflow. The
route now starts B2 with the thinnest real public PR-to-decision vertical slice while keeping
replay as supporting test and reproducibility behavior.

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
- ADR-0001's source/package layout remains accepted;
- Ali rejected the replay-first B2 sequence because it confused the learning path and did
  not behave like the eventual product.

### Remaining required work

1. Freeze the smallest complete public PR-to-decision vertical slice.
2. Define the initial repository-and-PR input and minimum read-only public acquisition.
3. Define the exact identity, changed-file, dependency-change, CI/check, and minimum
   upstream evidence needed by the selected supported slice.
4. Define what the first runtime evaluates itself and when it must abstain.
5. Define what acquired responses are captured for tests and reproducibility without
   allowing captured expected decisions to drive product code.
6. Compare the standard-library baseline with any proposed dependency; inherit none.
7. Choose the smallest reversible representation and one bounded user-facing interface.
8. Define universal and conditional responsibilities.
9. Define B2 live-smoke and deterministic captured-response tests and Ali-owned
   implementation, testing, diagnosis, and explanation work.
10. Create one bounded B2 implementation plan only after the responsibility is accepted.
11. Create another ADR only for a durable consequential method choice.

### B1 authorization boundary

B1 authorizes analysis, responsibility freezing, method comparison, and bounded planning.
It does not authorize B2 product-code changes.

### B1 exit gate

B1 passes only when:

- the responsibility is derived from S001–S005, not archived source;
- the first interface begins with a real public repository and Dependabot PR locator;
- the supported slice generalizes beyond one known PR inside the charter boundary;
- acquisition, identity freezing, evaluation, output, and abstention responsibilities are
  explicit;
- no required product conclusion is hidden in captured responses or test expectations;
- universal and conditional responsibilities are explicit;
- the dependency and representation baseline is reversible and adequate;
- security, untrusted-input, credentials, rate limits, permissions, and target-mutation
  boundaries are explicit;
- B2 tests and ownership work are concrete;
- archived code and tests have no active runtime or coverage role;
- Ali can explain why the slice is the smallest credible real end-to-end product path;
- one bounded B2 plan is accepted.

## 8. B2 — Public PR vertical slice

After B1 acceptance, one clean command or bounded application interface should accept a
public GitHub repository and Dependabot PR number and produce a bounded recommendation or
abstention from newly acquired public evidence.

Minimum behavior:

- validate the public repository and PR locator;
- acquire PR metadata read-only from GitHub;
- freeze exact repository, PR, base, head, and changed-file identity;
- identify one supported Python dependency-version change without repository-specific
  hardcoding;
- acquire the minimum relevant exact-head check or workflow evidence available through the
  authorized interface;
- acquire the minimum public upstream or package evidence required by the selected slice;
- preserve source, revision/time context, evidence state, and acquisition failure;
- execute a transparent baseline and the bounded evidence-authority check selected by B1;
- activate or decline only the conditional work required by the case;
- produce a bounded recommendation or abstention with reasons, uncertainty, and claim
  limits;
- produce one concise human-readable result and the minimum machine-readable state needed
  for testing and traceability;
- capture acquired responses or normalized evidence for deterministic tests and later
  replay;
- perform no target mutation and require no private repository access.

The first slice does not require persistence, services, queues, agents, models, deployment
infrastructure, exhaustive repository analysis, or a complete future artifact family.

Ali must trace the real request and evidence path, implement or materially modify central
behavior, add or change a meaningful test, diagnose an acquisition/identity/evaluation
failure, and explain evidence authority and claim limits.

## 9. B3 — Acquisition and replay robustness

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

## 10. B4 — Deterministic context and decision support

Expand supported Python behavior for dependency declarations and locks, direct and
transitive relationships, role/path evidence, repository usage, CI dependency identity and
responsibility, version and constraint comparisons, upstream activation-condition mapping,
targeted checks, action changes, stopping, abstention, and conditionally activated analysis.

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
real user-visible responsibility
→ minimum blocking concept
→ Ali predicts or challenges
→ one bounded implementation or investigation action
→ inspect actual source, response, test, or failure evidence
→ diagnose and correct
→ Ali modifies or tests a central part
→ Ali explains the path, authority, and limits
→ record demonstrated depth only when material
```

Internal terminology and artifacts are introduced only when the implemented responsibility
creates the need for them.

## 15. Capacity and scope

Standard planning capacity remains up to 24 focused hours per week as a ceiling, not a
quota. Preserve core behavior, evidence integrity, and ownership work first. Defer optional
breadth and experiments before weakening evaluation.

## 16. Current authorized sequence

1. Keep B2 implementation paused.
2. Freeze the clean-slate minimum public PR-to-decision vertical slice.
3. Define the initial locator, minimum live read-only acquisition, exact identity, evidence,
   evaluation, abstention, and output boundary.
4. Define captured-response use only for deterministic tests, debugging, and later replay.
5. Select the smallest dependency, representation, and user-facing interface.
6. Define universal and conditional responsibilities.
7. Define B2 live-smoke, captured-response, failure, and Ali ownership tests.
8. Review and accept the freeze.
9. Create and accept one bounded B2 implementation plan.
10. Begin the public PR vertical slice only after B1 passes.

Do not restore archived M2 source, resume M2-S03, select S006 without a named blocker,
require a fixed case count, hardcode a known PR result, or select permanent architecture
before its evidence gate.