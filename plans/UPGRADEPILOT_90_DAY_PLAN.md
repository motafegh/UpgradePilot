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
→ technical impact candidates and candidate-specific applicability
→ discriminating investigation activation, feedback, or justified stopping when needed
→ repository/context synthesis and overall evidence sufficiency
→ bounded recommendation or abstention
→ concise human and machine output
→ captured evidence for reproducibility, testing, rerun, and replay
→ review, ownership, and validation
```

Replay is supporting reproducibility/testing behavior. It must not replace the real PR-to-decision path as the primary product interface.

## 3. Route principles

1. Evidence gates control advancement; elapsed time, case count, document count, and code volume do not.
2. `MEMORY.md` selects one live position on this route.
3. Learn and build through the real end-to-end product responsibility.
4. Prefer a thin **complete** vertical path over isolated internal subsystems, but keep the implementation/method horizon at the complete owning responsibility rather than the next fixture or proof case.
5. Implement in small testable increments, then deliberately thicken central responsibilities with materially different real-case pressure before accepting fixture-shaped architecture as the product method.
6. Use product-simulation cases as discovery, transfer, and adversarial evidence—not as a feature backlog or required case-count sequence.
7. Generalize only where contrasting real responsibilities demonstrate stable sameness; keep mechanism-specific semantics separate where they materially differ.
8. Use captured responses/replay to test real behavior, not to substitute for live acquisition.
9. Preserve identity, provenance, uncertainty, degraded evidence, non-activation, and abstention.
10. Prefer deterministic trust controls before semantic automation.
11. Admit dependencies, models, graphs, agents, services, databases, queues, and infrastructure only through observed need and comparative evidence.
12. Increase Ali's control through prediction, implementation, testing, diagnosis, transfer reasoning, and explanation.
13. Historical implementation does not control new design by inheritance.
14. Stop when further work has no material decision, uncertainty, actionability, learning, transfer, or product value—not merely because the first specimen has passed.

## 4. Route overview

| Stage | Required outcome |
|---|---|
| D0 — Initial evidence base | Expose initial runtime and artifact responsibilities through real-case evidence. |
| D1 — Contrast closure | Synthesize materially contrasting cases sufficiently to freeze the first implementation responsibility. |
| B1 — Implementation responsibility freeze | Establish the real PR-first boundary, clean source baseline, minimum acquisition/error model, first interface, tests, and ownership direction required for B2. |
| B2 — Public PR vertical slice | Carry the public Python Dependabot flow through read-only acquisition, exact identity, evidence-backed reasoning, recommendation or abstention, concise output, tests, and representative contrast across central variable-input responsibilities so the first specimen does not define the method horizon. |
| B3 — Acquisition and replay robustness | Add raw preservation, changed-head handling, source failures, rate limits, recovery, deterministic replay, and broader required public-source acquisition. |
| B4 — Deterministic context and decision support | Expand supported dependency, CI-authority, target-relevance, impact, applicability, conditional-stage, stopping, targeted-check, and action-change behavior across the supported Python domain. |
| B5 — Persistence, diagnosis, and evaluation | Add justified storage, diagnostics, corpus evaluation, cost, and stopping evidence. |
| X1 — Evidence-gated advanced-method checkpoint | Conditionally evaluate and adopt, pilot, reject, or defer advanced methods against a simpler credible baseline when an owning B2–B5 responsibility has exposed a concrete limitation. |
| C1 — Hardening, ownership, and portfolio closure | Demonstrate a reproducible supported core and evidence-indexed ownership proof. |

Stages are evidence gates, not calendar promises.

**X1 is the one intentionally non-linear checkpoint.** It may be selected from B2, B3, B4, or B5 before those stages are fully complete only when all of the following are true:

- an observed limitation exists in an already admitted product/evaluation responsibility;
- a simpler credible baseline already exists;
- the experiment is bounded with measurable acceptance/rejection conditions;
- security, cost, cleanup, and claim limits are explicit;
- `MEMORY.md` explicitly selects the checkpoint/plan;
- running the experiment does not silently waive the owning stage's unfinished core outcomes.

After the X1 experiment reaches `adopt`, `retain as pilot`, `reject`, or `defer`, return to the owning B-stage unless `MEMORY.md` explicitly selects a different admitted continuation. Early X1 activation is therefore a method checkpoint, not permission to skip B2–B5 product responsibilities or replace the supported deterministic core with an experiment.

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

B2 implementation should remain incremental, but central architecture and method choices must be made against the complete B2 responsibility and credible variation inside the supported boundary. A first public case may establish the walking path; it does not by itself establish that the method is sufficiently general.

B2 exit requires credible end-to-end evidence for:

- locator validation and public read-only acquisition;
- exact repository/PR/base/head/changed-file identity;
- supported Python dependency-version change handling without case hardcoding;
- minimum relevant CI/workflow evidence;
- minimum required public package/upstream evidence;
- explicit source/revision/evidence-state/failure preservation;
- transparent evidence-authority checks;
- mechanism-specific technical impact and candidate-specific applicability where activated;
- conditional discriminating investigation, feedback, pruning, or justified non-activation where needed;
- repository/context evidence kept distinct from technical applicability when those responsibilities differ;
- bounded recommendation or abstention with reasons/uncertainty/claim limits;
- concise human-readable output and minimum machine-readable traceability state;
- deterministic tests/replay support from captured or normalized evidence;
- at least one materially different transfer/implementation contrast across the central reasoning responsibility so accepted architecture is not justified solely by one known mechanism/fixture;
- no target mutation and no private-repository requirement;
- at least one meaningful owner-controlled explanation, modification, test, diagnosis, or transfer argument.

The detailed sequence, source paths, algorithms, contrast set, and proof matrices belong to bounded B2 plans and accepted ADRs/specifications, not this route.

B2 does **not** require systematic breadth across every Python impact mechanism. That broader supported-domain expansion remains primarily B4 work. The B2 contrast requirement exists to prevent fixture-shaped architecture, not to finish the mature system early.

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

Expand supported Python behavior for dependency declarations/locks, dependency role/path, repository usage, CI authority, version/constraint comparisons, upstream activation-condition mapping, impact mechanisms, candidate applicability, targeted checks, action changes, stopping, abstention, and conditionally activated analysis.

Acceptance must be demonstrated on supported Python cases rather than inferred from architecture alone.

## 11. B5 — Persistence, diagnosis, and evaluation

Introduce durable infrastructure only after real run, replay, query, diagnosis, and evaluation needs exist.

Required outcomes include justified storage, idempotence/supersession, useful queries, diagnostics, setup/cleanup, staged corpus identity, baseline/full comparisons, abstention/coverage, cost/stopping analysis, and explicit truth/adjudication limits.

Do not select infrastructure because an earlier plan or conventional architecture named it.

## 12. X1 — Evidence-gated experiments

X1 is a conditional checkpoint for advanced methods, not a license to add technology for portfolio breadth.

Any model, graph, agentic, distributed, MLOps, microservice, Kubernetes, multi-cloud, or similar experiment requires:

- an observed limitation in an already admitted owning responsibility;
- a bounded hypothesis;
- a simpler credible baseline;
- measurable acceptance/rejection rules;
- security/cost controls and cleanup;
- explicit live selection in `MEMORY.md`;
- adopt, pilot, reject, or defer disposition.

X1 may be invoked early from B2–B5 when Section 4's conditional-entry rules are satisfied. The experiment must remain subordinate to the owning product responsibility and must preserve a runnable simpler baseline. It may not silently erase unfinished B-stage requirements.

An experiment result does not become product architecture until its owning product responsibility admits and implements it. If adopted, update the required ADR/specification/plan before normal product integration. If retained as pilot, rejected, or deferred, preserve that result and return to the owning route without technology-chasing.

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

Planning capacity is a ceiling, not a quota. Preserve core behavior, evidence integrity, ownership work, and responsibility-level generality first; defer optional breadth and experiments before weakening evaluation.

Do not restore archived M2 source, resume superseded report-first work, select more simulation merely to continue activity, require a fixed case count, hardcode a known PR result, or choose permanent architecture before its evidence gate.

Do not confuse these two statements:

```text
implement only what is justified now
```

and:

```text
design only for the first known case
```

The first remains required. The second is prohibited by the Minimum Useful Generality specification when the owning responsibility is broader.

## 15. Route maintenance

Change this file only when stage order, gate definitions, required outcomes, route principles, or the stable product-flow horizon changes.

Do not update it for:

- stage activation/completion;
- latest commits or test results;
- immediate blockers/continuation;
- selection of one bounded plan;
- ordinary implementation progress.

Those live facts belong only in `MEMORY.md`.
