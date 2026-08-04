# UpgradePilot Evidence-Derived Learning and Building Plan

**Status:** Controlling project-local route and gate plan  
**Owner:** Ali Rajabi  
**Activated:** 2026-07-23

## 1. Responsibility

This file owns only:

- stage sequence;
- stage gate purpose;
- required outcomes for advancement;
- stable route principles;
- the stable end-to-end product-flow horizon.

It does **not** record which stage is selected, passed, active, blocked, or next. `../MEMORY.md` is the sole live-state owner.

Other responsibilities remain with their normal owners:

- mission, user, product boundary, evidence doctrine, claims → `../PROJECT_CHARTER.md`;
- learning/execution method → `../OPERATING_GUIDE.md`;
- stable technical behavior → accepted specifications;
- consequential implementation methods → accepted ADRs;
- bounded execution scope/proof/stop lines → selected bounded plans;
- implemented truth → source, tests, commands, outputs, and environment;
- dated historical evidence → acceptance and working-memory records.

Historical route transitions and D1 evidence are preserved separately, including:

- [`D1_ACCEPTANCE_AND_B1_ACTIVATION.md`](D1_ACCEPTANCE_AND_B1_ACTIVATION.md)
- [`../product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](../product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md)
- [`../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md`](../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md)

They explain how the route was derived; they do not need to be reproduced here.

## 2. Stable product-flow horizon

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

Replay is supporting reproducibility/testing behavior. It must not replace the real PR-to-decision path as the primary product interface.

## 3. Route principles

1. Evidence gates control advancement; elapsed time, case count, document count, and code volume do not.
2. `MEMORY.md` selects one live position on this route.
3. Learn and build through the real end-to-end product responsibility.
4. Prefer the thinnest complete credible vertical slice over isolated internal subsystems.
5. Use captured responses/replay to test real behavior, not to substitute for live acquisition.
6. Preserve identity, provenance, uncertainty, degraded evidence, non-activation, and abstention.
7. Prefer deterministic trust controls before semantic automation.
8. Admit dependencies, models, graphs, agents, services, databases, queues, and infrastructure only through observed need and comparative evidence.
9. Increase Ali's control through prediction, implementation, testing, diagnosis, and explanation.
10. Historical implementation does not control new design by inheritance.
11. Stop when further work has no material decision, uncertainty, actionability, learning, or product value.

## 4. Route overview

| Stage | Required outcome |
|---|---|
| D0 — Initial evidence base | Expose initial runtime and artifact responsibilities through real-case evidence. |
| D1 — Contrast closure | Synthesize materially contrasting cases sufficiently to freeze the first implementation responsibility. |
| B1 — Implementation responsibility freeze | Establish the real PR-first boundary, clean source baseline, minimum acquisition/error model, first interface, tests, and ownership direction required for B2. |
| B2 — Public PR vertical slice | Carry one public Python Dependabot PR through minimum read-only acquisition, exact identity, bounded evidence evaluation, recommendation or abstention, concise output, tests, and one central owner-controlled change. |
| B3 — Acquisition and replay robustness | Add raw preservation, changed-head handling, source failures, rate limits, recovery, deterministic replay, and broader required public-source acquisition. |
| B4 — Deterministic context and decision support | Expand supported dependency, CI-authority, target-relevance, conditional-stage, stopping, targeted-check, and action-change behavior. |
| B5 — Persistence, diagnosis, and evaluation | Add justified storage, diagnostics, corpus evaluation, cost, and stopping evidence. |
| X1 — Evidence-gated experiments | Measure and adopt, pilot, reject, or defer advanced methods against simpler baselines. |
| C1 — Hardening, ownership, and portfolio closure | Demonstrate a reproducible supported core and evidence-indexed ownership proof. |

Stages are evidence gates, not calendar promises.

## 5. D0 — Initial evidence base

Produce enough real-case/manual evidence to reveal the product's decision, evidence, reporting, stopping, and artifact responsibilities.

D0 must not treat one case as representative or freeze production architecture from simulation convenience.

## 6. D1 — Contrast closure

Use materially contrasting cases to determine:

- universal versus conditional responsibilities;
- when a transparent baseline is sufficient or wrong;
- when target-specific evidence changes action or confidence;
- which uncertainties must remain visible;
- where implementation should begin.

D1 exit requires an accepted synthesis and explicit implementation-entry decision.

## 7. B1 — Implementation responsibility freeze

Before product implementation expands, establish:

- the smallest complete real user-visible responsibility;
- public read-only permission boundary;
- exact identity and evidence-authority requirements;
- clean active source boundary;
- simplest credible dependencies/methods;
- acceptance tests, claim limits, and stop lines;
- ownership-bearing work required before B2.

B1 must not inherit archived methods automatically.

## 8. B2 — Public PR vertical slice

One clean interface accepts a public GitHub repository and PR locator and grows toward a bounded recommendation or abstention from newly acquired public evidence.

B2 exit requires credible end-to-end evidence for:

- locator validation and public read-only acquisition;
- exact repository/PR/base/head/changed-file identity;
- one supported Python dependency-version change without case hardcoding;
- minimum relevant CI/workflow evidence;
- minimum required public package/upstream evidence;
- explicit source/revision/evidence-state/failure preservation;
- transparent baseline and bounded evidence-authority checks;
- conditional analysis only when activated by evidence;
- bounded recommendation or abstention with reasons/uncertainty/claim limits;
- concise human-readable output and minimum machine-readable traceability state;
- deterministic tests/replay support from captured or normalized evidence;
- no target mutation and no private-repository requirement;
- at least one meaningful owner-controlled explanation, modification, test, or diagnosis.

The detailed sequence, source paths, algorithms, and proof matrices belong to bounded B2 plans and accepted ADRs/specifications, not this route.

## 9. B3 — Acquisition and replay robustness

Strengthen the real acquisition path with:

- raw response preservation or durable references when justified;
- explicit inaccessible/missing/expired/stale/invalid/conflicting/failed-source states;
- changed-head detection and clean new-analysis boundaries;
- rate-limit, timeout, network, malformed-response, and partial-source handling;
- secure optional credential use only when justified;
- deterministic replay independent of live availability;
- acquisition failure/recovery tests;
- broader required public-source acquisition within the supported boundary.

## 10. B4 — Deterministic context and decision support

Expand supported Python behavior for dependency declarations/locks, dependency role/path, repository usage, CI authority, version/constraint comparisons, upstream activation-condition mapping, targeted checks, action changes, stopping, abstention, and conditionally activated analysis.

Acceptance must be demonstrated on supported Python cases rather than inferred from architecture alone.

## 11. B5 — Persistence, diagnosis, and evaluation

Introduce durable infrastructure only after real run, replay, query, diagnosis, and evaluation needs exist.

Required outcomes include justified storage, idempotence/supersession, useful queries, diagnostics, setup/cleanup, staged corpus identity, baseline/full comparisons, abstention/coverage, cost/stopping analysis, and explicit truth/adjudication limits.

Do not select infrastructure because an earlier plan or conventional architecture named it.

## 12. X1 — Evidence-gated experiments

Any model, graph, agentic, distributed, MLOps, microservice, Kubernetes, multi-cloud, or similar experiment requires:

- observed limitation;
- bounded hypothesis;
- simpler credible baseline;
- measurable acceptance/rejection rules;
- security/cost controls and cleanup;
- adopt, pilot, reject, or defer disposition.

An experiment result does not become product architecture until its owning product responsibility admits and implements it.

## 13. C1 — Hardening and ownership

Closure requires:

- reproducible supported-core execution;
- representative normal/failure/changed/early-stop cases;
- secure configuration;
- appropriate tests and CI;
- run/diagnosis/recovery instructions;
- limitations and claim register;
- assistance disclosure;
- implemented architecture explanation;
- reviewer demonstration and portfolio evidence;
- Ali's ability to modify, test, diagnose, and defend the central flow.

## 14. Capacity and scope discipline

Planning capacity is a ceiling, not a quota. Preserve core behavior, evidence integrity, and ownership work first; defer optional breadth and experiments before weakening evaluation.

Do not restore archived M2 source, resume superseded report-first work, select more simulation merely to continue activity, require a fixed case count, hardcode a known PR result, or choose permanent architecture before its evidence gate.

## 15. Route maintenance

Change this file only when stage order, gate definitions, required outcomes, route principles, or the stable product-flow horizon changes.

Do not update it for:

- stage activation/completion;
- latest commits or test results;
- immediate blockers/continuation;
- selection of one bounded plan;
- ordinary implementation progress.

Those live facts belong only in `MEMORY.md`.
