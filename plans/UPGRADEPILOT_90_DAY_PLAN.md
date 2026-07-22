# UpgradePilot Evidence-Derived Learning and Building Plan

**Status:** Controlling project-local route and gate plan  
**Owner:** Ali Rajabi  
**Execution period:** 2026-07-20 to 2026-10-17  
**Activated:** 2026-07-23  
**Responsibility:** Project sequence, learning-by-building progression, evidence gates, implementation admission, capacity protection, and final closure

## 1. Authority and replacement

This file is the single owner of UpgradePilot's project route.

It replaces the historical M0–M8 decomposition and the superseded M2-S03
report-first implementation route. Useful requirements from those records survive
only where explicitly retained here, in a current bounded plan, in a specification
or ADR, or in implemented source/test evidence.

The following remain authoritative for their own responsibilities:

- [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md) — mission, user, supported decision,
  product boundary, evidence doctrine, admission rules, and claim limits;
- [`../OPERATING_GUIDE.md`](../OPERATING_GUIDE.md) — ordinary learning, execution,
  assistance fading, blockers, and evidence handling;
- [`../product-simulation/AGENTS.md`](../product-simulation/AGENTS.md) and
  [`../product-simulation/SIMULATION_GOVERNANCE_AND_PLAN.md`](../product-simulation/SIMULATION_GOVERNANCE_AND_PLAN.md)
  — local simulation execution;
- [`../MEMORY.md`](../MEMORY.md) — concise current continuation;
- source, tests, commands, outputs, and the actual environment — implemented truth.

The frozen core remains unchanged: UpgradePilot is a Python implementation for
maintainers of public Python repositories receiving Dependabot pull requests.
Cross-ecosystem simulation may test transferable responsibilities but does not expand
supported product scope.

## 2. Why the route changed

Early implementation assumed a report-first vertical slice with repository context,
baseline evaluation, acquisition, persistence, failure handling, and diagnostics
added mechanically later.

S001–S004 showed that the first credible core must instead be designed around a
complete runtime responsibility:

```text
invocation
→ exact case identity
→ material operations
→ evidence and evidence states
→ claims and interpretations
→ findings
→ transparent baseline
→ bounded decision
→ machine and human reports
→ follow-up, rerun, and supersession
→ stopping, review, and ownership
```

They also established that:

- CI color has no global authority without trigger, job, step, command,
  responsibility, revision, environment, and retention context;
- dependency role is multi-axis and paths may include lock, adapter, framework,
  development/test, and peer-support relationships;
- missing, expired, inaccessible, conflicting, or unreproducible evidence can create
  a concrete action or degraded method state;
- advisory, compatibility, failure-attribution, dynamic-execution, platform, and
  similar responsibilities are conditional;
- simulation artifacts are discovery evidence, not final production schemas;
- investigation must stop when additional work cannot change action, material
  uncertainty, required checks, or a product/evaluation conclusion;
- the baseline can be sufficient, so deeper analysis must not be treated as an
  automatic product win.

## 3. Route principles

1. **Evidence gates control advancement.** Dates, hours, case counts, document counts,
   and artifact counts do not establish completion.
2. **One active route exists.** Do not create a parallel roadmap or competing phase
   hierarchy.
3. **Learn through the owning responsibility.** Concepts are taught and practised
   when the current product responsibility requires them.
4. **Build the smallest credible supported core.** Do not encode one fixture,
   repository, phrase, or expected answer as product behavior.
5. **Separate universal and conditional work.** A conditional stage or artifact
   activates only when evidence requires it.
6. **Preserve evidence and uncertainty.** Missing and degraded states remain visible
   and may change the action.
7. **Prefer deterministic trust controls.** Identity, provenance, validation,
   authority boundaries, stage transitions, and structural consistency should be
   deterministic where feasible.
8. **Admit methods through evidence.** Models, graphs, agents, services, databases,
   queues, and infrastructure enter only after an observed limitation and a simpler
   baseline.
9. **Increase Ali's control progressively.** Central stages require prediction,
   modification, testing, diagnosis, and explanation at a recorded depth.
10. **Stop when sufficient.** Remaining capacity does not justify additional analysis,
    artifacts, abstractions, or architecture.

## 4. Current evidence base

### S001 — transitive advisory and relevant green CI

A retrospective Python case covering transitive documentation tooling, advisory
remediation, dependency-path evidence, corrected historical claims, relevant green
CI, and a normal-review decision.

### S002 — direct declaration, adapter path, and incomplete green CI

A retrospective Python case covering direct declaration, framework-mediated test
use, production-image installation, removed upstream API behavior, skipped relevant
Python tests, expired logs, and a targeted-check decision.

### S003 — failing install and causal attribution

A prospective cross-ecosystem transfer case covering failing CI at `npm ci`,
job/step/command responsibility, peer-range incompatibility, comparison evidence,
causal attribution, recovery transitions, and conditional diagnostic artifacts.

### S004 — baseline sufficiency and stopping

A prospective Python case covering a direct development dependency, exact relevant
ordinary and regression CI, precommitted stop conditions, inactive conditional
stages, investigation-cost recording, and a normal-review decision.

S004 materialized:

```text
baseline_sufficient
full_investigation_added_no_material_value
```

The full process confirmed only that green CI had authority over the changed pytest
responsibility. It did not change the action, add a check, or alter material
uncertainty.

### Current thesis coverage

| Comparative class | Evidence |
|---|---|
| Same action, materially stronger support | S001, S002, S003 |
| Baseline sufficient; no material added value | S004 |
| Baseline wrong action | Not covered |
| Dependency/PR action divergence | Not covered |
| Unresolved comparison | Not covered |

The thesis has contrasting evidence, not representative validation.

## 5. Route overview

| Stage | State | Required outcome |
|---|---|---|
| D0 — Evidence base | Complete | S001–S003 completed, validated, and synthesized |
| D1 — Contrast closure | **Current; S004 complete, S005 remaining** | One action-changing or decision-divergent contrast plus focused synthesis |
| B1 — Implementation responsibility freeze | Pending | Existing source reconciled with evidence; minimum credible runtime responsibility accepted |
| B2 — Executable run kernel | Pending | Reproducible fixture/replay-to-decision flow with lineage, reports, transitions, tests, and Ali-owned change |
| B3 — Public acquisition and replay | Pending | Exact public GitHub/PyPI acquisition with raw preservation and explicit source failure |
| B4 — Deterministic context and decision support | Pending | Supported Python dependency, repository, CI-authority, baseline, conditional-stage, and decision behavior |
| B5 — Persistence, diagnosis, and evaluation | Pending | Justified storage, replay, queries, diagnostics, corpus evaluation, cost and stopping evidence |
| X1 — Evidence-gated experiments and advanced exposure | Pending | Measured adoption/rejection decisions against the supported core |
| C1 — Hardening, ownership, and portfolio closure | Pending | Reproducible supported core, secure operation, ownership defense, and evidence-indexed portfolio |

Stages are gates, not fixed calendar promises. Reorder or repeat only when evidence
changes the dependency structure.

## 6. D1 — Contrast closure

### Completed S004 responsibility

S004 established that the transparent baseline can be sufficient when a small
authority confirmation shows:

- the changed dependency belongs to the exercised path;
- exact-head relevant checks consume the proposed version and pass;
- primary upstream information is coherent;
- no decision-critical contradiction or evidence gap remains.

It also established `STOPPING_EVALUATION.json` as a conditional simulation-artifact
candidate for sufficiency, overreach, stage-activation, or investigation-cost cases.

### Current S005 responsibility

S005 is controlled by
[`../product-simulation/S005_ACTION_CHANGE_OR_DIVERGENCE_REQUIREMENTS.md`](../product-simulation/S005_ACTION_CHANGE_OR_DIVERGENCE_REQUIREMENTS.md).

Prefer a public Python Dependabot case where either:

1. full evidence changes the transparent baseline's broad action; or
2. dependency assessment and current PR action genuinely diverge—for example, the
   update appears acceptable while a pre-existing or unrelated failure blocks the
   PR.

Selection and interpretation must remain evidence-driven. Preserve an unresolved
result rather than force the preferred class.

### D1 exit gate

D1 passes only when:

- S004's sufficiency and stopping result is integrated;
- S005 supplies a material action change, real decision-axis divergence, or an
  honest result showing which contrast is still missing;
- cross-case synthesis classifies stable, conditional, contradicted, unresolved, and
  outside-boundary responsibilities;
- activation, stopping, cost, and divergence behavior are explicit;
- evidence is sufficient to state the minimum credible runtime responsibility;
- Ali reviews the result at the understanding depth required to authorize B1.

No fixed case minimum applies. Add another case only if a named planning uncertainty
still blocks B1.

## 7. B1 — Implementation responsibility freeze

### Purpose

Convert simulation evidence into one bounded executable responsibility without
pretending that manual artifact files are production schemas.

### Required work

1. Inspect current source and tests.
2. Classify existing implementation as:
   - retain unchanged;
   - retain with correction;
   - supersede;
   - experimental evidence only;
   - remove only when separately justified.
3. Define the minimum credible runtime responsibility, including:
   - real input boundary;
   - exact identity resolution;
   - operation and evidence-state representation;
   - finding and decision boundary;
   - transparent baseline execution;
   - conditional-stage activation and stopping state;
   - machine and human projections;
   - follow-up/new-run behavior;
   - validation and security invariants.
4. Select the smallest reversible representation and interface adequate for B2.
5. Write one bounded B2 implementation plan only after the responsibility is
   accepted.
6. Create an ADR only for a durable consequential method.

### B1 exit gate

- the responsibility is derived from cross-case evidence;
- no required behavior is delegated to caller-supplied interpretation;
- universal and conditional responsibilities are explicit;
- the selected representation has a credible generalization path inside the charter
  boundary;
- rejected and deferred methods remain recorded;
- Ali can explain why this is the smallest credible slice.

## 8. B2 — Executable run kernel

### Outcome

A clean command or bounded application interface consumes one real-shaped
fixture/replay input and produces reproducible run state, a bounded decision, and
both report forms.

### Minimum behavior

- invocation distinct from discovered/frozen identity;
- stable run and record identities;
- material operation history;
- evidence records with explicit states and provenance;
- observations distinct from interpretations and findings;
- transparent baseline result;
- conditional-stage activation/non-activation and justified stop state;
- bounded decision or abstention;
- machine and human reports from the same trusted application result;
- follow-up, rerun, supersession, and changed-boundary transitions;
- structural validation;
- invalid, missing, changed-evidence, and early-stop tests;
- no embedded credentials or external mutation.

Live acquisition, database, services, queues, agents, and models are not required for
B2.

### Learning and ownership gate

Ali must, at the claimed scope:

- trace one input through the complete kernel;
- modify one central behavior;
- add or change one meaningful test;
- diagnose one failure;
- explain evidence authority, activation/stopping behavior, limitations, and why the
  output is bounded.

## 9. B3 — Public acquisition and replay

### Outcome

The kernel can acquire or replay lawful public evidence for supported Python
Dependabot cases without hiding source failure.

### Required behavior

- exact repository, PR, base, head, changed-file, package, and version identity;
- bounded GitHub and PyPI/upstream acquisition through authorized interfaces;
- raw preservation or durable references with revision/time context;
- explicit inaccessible, missing, expired, stale, invalid, and partial states;
- untrusted-content handling;
- no source text can create fields, authority, tools, or actions;
- reproducible replay without requiring the source to remain live;
- acquisition diagnostics and representative failure/recovery tests.

### Gate

A supported Python case must run through acquisition and replay with the same
material identity and lineage. Ali must diagnose at least one acquisition or replay
failure.

## 10. B4 — Deterministic context and decision support

### Outcome

UpgradePilot assembles repository-specific evidence and selects a bounded action for
supported Python cases using transparent, inspectable behavior.

### Required behavior

- declaration, lock, optional/development/runtime, and unresolved dependency state;
- dependency-path evidence appropriate to Python packaging;
- repository usage and relevant test/workflow evidence;
- CI trigger, job, step, command, revision, environment, and retention authority;
- version and declared-constraint comparisons;
- transparent baseline v1 or a separately versioned successor;
- conditional activation of advisory, compatibility, repeated-execution,
  failure-attribution, or dynamic-check responsibilities only when required;
- explicit stopping, abstention, targeted-check, and divergence behavior;
- evidence-backed reasons, limitations, and transitions.

S003 may inform generic mechanisms, but B4 acceptance must be proven on the charter's
Python boundary.

### Gate

At least one supported Python case and one changed/degraded variant must demonstrate
that repository context materially constrains the decision without unsupported
certainty.

## 11. B5 — Persistence, diagnosis, and evaluation

### Purpose

Add durable infrastructure only after real run, replay, query, diagnosis, and
evaluation needs are known.

### Required behavior

- one justified persistence mechanism;
- idempotent run storage and explicit supersession/new-run relationships;
- useful queries tied to decisions, evidence gaps, stopping, diagnosis, and replay;
- structured errors and operational diagnostics;
- reproducible setup, migration, and cleanup;
- staged corpus with frozen identity and contamination controls;
- transparent baseline predictions and full-result comparisons;
- coverage, abstention, class-wise, cost-sensitive, and stopping analysis where
  defensible;
- error analysis and explicit truth/adjudication limits;
- measured investigation cost and overreach behavior.

### Admission rule

Do not select SQL, a database, a queue, or a service boundary merely because an old
milestone named it. Select the smallest method that satisfies demonstrated B5 needs.

## 12. X1 — Evidence-gated experiments and advanced exposure

### Admission rule

Every learned, graph, LLM, agentic, or advanced-system experiment requires:

- an observed supported-core limitation;
- a bounded hypothesis;
- a simpler credible baseline;
- measurable success and rejection conditions;
- leakage, security, cost, maintenance, and cleanup controls;
- an adopt, retain-as-pilot, reject, or defer decision.

No successful model or permanent advanced architecture is required.

### Advanced-system obligations

Preserve the chartered learning obligations:

- A1 hands-on exposure for distributed queues, advanced MLOps, microservices,
  Kubernetes, multi-cloud, and bounded autonomous multi-agent systems, or a formally
  documented infeasibility boundary;
- at least two A2 project-integrated pilots unless an explicit strategic review
  changes that requirement;
- A3 permanent adoption only through comparative evidence.

Use the supported UpgradePilot core as the representative workload. One major
exposure package may be active at a time. Each package must include scope ceilings,
security/cost/privacy boundaries, one observable failure or degraded state,
recovery/cleanup evidence, operational-burden comparison, and an adoption decision.

## 13. C1 — Hardening, ownership, and portfolio closure

### Required evidence

- clean supported-core execution;
- declared input/output boundary;
- representative real, changed, failure, and early-stop cases;
- versioned baseline and evaluation results;
- justified analytical and advanced-system decisions;
- appropriate tests and CI;
- secure configuration and public-safe evidence;
- setup, run, diagnosis, recovery, and cleanup instructions;
- limitations and claim register;
- AI-assistance disclosure;
- final architecture and data-flow explanation based on implemented reality;
- concise reviewer demonstration;
- portfolio README/evidence index;
- career-market calibration during an explicit Career review.

### Completion gate

All claims match preserved evidence. Ali can explain, modify, test, query, diagnose,
and defend the central flow while distinguishing supported ownership from bounded
exposure.

## 14. Learning-by-building operating cycle

Every central responsibility should normally follow:

```text
real responsibility
→ minimum blocking concept
→ Ali predicts, reasons, or challenges
→ bounded investigation or implementation
→ inspect actual evidence
→ diagnose and correct
→ Ali modifies or tests a central part
→ Ali explains the path, authority, and limits
→ record demonstrated depth
```

Do not create a detached study phase for topics that the active responsibility does
not require. Repair prerequisites only to the minimum complete blocking depth, then
return to the product work.

## 15. Capacity and scope protection

Standard planning capacity remains up to 24 focused hours per week. It is a ceiling,
not a quota.

When capacity is constrained:

1. preserve the supported core and evidence integrity;
2. preserve learning and diagnosis of central behavior;
3. narrow optional case breadth and polish;
4. reject or defer experiments before weakening evaluation;
5. do not relabel partial work as complete.

Do not begin work merely to fill remaining hours.

## 16. Plan and artifact ownership

- this file owns route stages and gates;
- `MEMORY.md` owns exact continuation;
- local simulation files own S005 execution;
- a bounded implementation plan may be created only at B1 after the minimum runtime
  responsibility is accepted;
- specifications own stable requirements and invariants;
- ADRs own selected durable methods;
- source and tests own implemented truth;
- learning artifacts preserve reusable understanding, not project status;
- working memory preserves material execution evidence, not a second roadmap.

## 17. Superseded route records

The following remain historical evidence and do not control current work:

- [`UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md`](UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md);
- [`M2_S03_EVIDENCE_REPORT_VERTICAL_SLICE_PLAN.md`](M2_S03_EVIDENCE_REPORT_VERTICAL_SLICE_PLAN.md);
- historical M0–M8 route wording.

## 18. Current authorized sequence

1. Keep implementation paused.
2. Screen and execute S005 prospectively under the controlling S005 requirements.
3. Preserve action change, decision divergence, or an honest unresolved result.
4. Perform focused S001–S005 synthesis.
5. Determine whether D1 passes.
6. If D1 passes, freeze the minimum credible runtime responsibility under B1.
7. Create one bounded B2 implementation plan and begin learning by building.
8. If D1 does not pass, authorize only the smallest additional case needed to resolve
   a named blocker.

Do not resume M2-S03, repeat S004, require ten cases, or select permanent architecture
before the B1 gate.
