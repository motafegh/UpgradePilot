# B1 Implementation Responsibility Freeze Requirements

**Status:** Active  
**Activated:** 2026-07-23  
**Owner:** Ali Rajabi  
**Parent route:** [`UPGRADEPILOT_90_DAY_PLAN.md`](UPGRADEPILOT_90_DAY_PLAN.md)  
**D1 acceptance:** [`D1_ACCEPTANCE_AND_B1_ACTIVATION.md`](D1_ACCEPTANCE_AND_B1_ACTIVATION.md)  
**Evidence source:** [`../product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](../product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md)

B1 is the active project stage. It freezes one minimum credible executable
responsibility derived from S001–S005 and reconciled with current implemented truth.

B1 is not B2 implementation. Product-code changes for the new kernel remain paused until
this freeze and one bounded B2 plan are accepted.

## Purpose

Determine exactly what the first executable UpgradePilot core must own, what prepared
replay input may supply, what representation is sufficient and reversible, and which
existing implementation survives.

## Entry conditions

The entry conditions are satisfied:

- Ali reviewed and accepted the D1 synthesis;
- the technical evidence gate is complete;
- the replay-first direction is accepted;
- the stable public-Python Dependabot boundary is unchanged;
- simulation artifacts remain discovery evidence rather than production schemas;
- no named discovery blocker currently requires another scenario.

## Required B1 work

### 1. Inspect implemented truth

Read and, where applicable, run:

- `pyproject.toml` and package configuration;
- current `src/upgradepilot/` modules;
- current tests and fixtures;
- supported commands and entry points;
- actual outputs and failure behavior;
- applicable specifications and ADRs only after checking implementation reality.

Do not infer current behavior from historical plans.

### 2. Reconcile existing implementation

Classify every relevant existing component as:

- **retain unchanged** — already satisfies the accepted responsibility;
- **retain with correction** — useful structure with a bounded defect;
- **supersede** — built for the obsolete report-first boundary;
- **experimental evidence only** — useful lesson, not supported runtime behavior;
- **remove only when separately justified** — deletion must not be automatic cleanup.

The superseded M2-S03 route must not silently become the B2 boundary.

Produce one source-reconciliation record with file/component, current behavior, evidence,
classification, rationale, and consequence.

### 3. Freeze the minimum runtime responsibility

The candidate responsibility must cover, at minimum:

- replay-shaped invocation;
- exact frozen repository, PR, base, head, changed-file, dependency, and version identity;
- stable run and record identities;
- material operation history;
- evidence records with explicit states and provenance;
- observation, interpretation, and finding separation;
- versioned transparent baseline execution;
- conditional-stage activation and non-activation state;
- bounded decision or abstention with reasons and limitations;
- machine and human projections from the same accepted state;
- follow-up, rerun, supersession, and changed-boundary transitions;
- structural identity and lineage validation;
- review, assistance, and ownership state;
- no target mutation.

### 4. Define the semantic boundary

State explicitly what B2 replay input may contain.

Permitted candidates include:

- captured public evidence;
- frozen identity data;
- evidence-state labels with provenance;
- explicitly labeled prepared interpretations where semantic automation is not yet
  admitted.

B2 itself must own deterministic runtime mechanics, validation, baseline execution,
state transitions, report consistency, and the bounded decision boundary selected by B1.

A fixture must not supply an unexplained final decision or hide a required product
answer as caller data.

### 5. Select the smallest reversible representation

Choose only the representation and interfaces needed for B2.

Do not preselect:

- a database;
- services or queues;
- a model or agent runtime;
- a graph system;
- live GitHub/PyPI acquisition;
- deployment architecture.

Prefer ordinary typed Python structures, explicit validation, deterministic functions,
and file-backed fixtures unless the source audit demonstrates a smaller credible option.

Create an ADR only when B1 makes a durable consequential choice.

### 6. Define B2 acceptance tests

At minimum:

- valid replay produces coherent run state, baseline, decision, both reports, and
  transitions;
- invalid or inconsistent identity is rejected;
- missing, inaccessible, partial, conflicting, and superseded evidence states remain
  visible;
- IDs and references resolve;
- observations, interpretations, findings, and decisions cannot be silently collapsed;
- baseline and full action may be the same or different;
- conditional responsibilities may be active or inactive;
- a changed identity requires a new run;
- reports cannot disagree with accepted decision state;
- follow-up and supersession are explicit;
- target mutation is impossible by default;
- no fixture may inject an unexplained final decision.

The test set must include at least one same-action case, one action-change case, one
early-stop case, and one degraded or missing-evidence variant derived from S001–S005.

### 7. Define Ali ownership work

The eventual B2 plan must include central Ali-owned work:

- predict one replay outcome before running it;
- implement or materially modify one runtime behavior;
- add or change one meaningful acceptance test;
- diagnose one deliberately introduced identity, lineage, or report-consistency defect;
- explain the complete flow, authority boundary, conditional activation, stopping, and
  claim limits.

Completion of AI-written code alone cannot satisfy this gate.

## B1 deliverables

B1 should produce only:

1. current-source and test reconciliation record;
2. accepted minimum executable responsibility;
3. prepared-input versus deterministic-behavior boundary;
4. bounded representation and interface decision;
5. explicit universal and conditional responsibilities;
6. B2 acceptance and Ali ownership gates;
7. one bounded B2 implementation plan after responsibility acceptance;
8. ADR only when justified.

Do not create competing implementation plans or architecture variants.

## B1 exit gate

B1 passes only when:

- the responsibility is evidence-derived and checked against current source/tests;
- it generalizes beyond one replay fixture inside the charter boundary;
- no semantic answer required from the product is hidden as unexplained input;
- universal and conditional responsibilities are explicit;
- the representation is reversible and adequate for B2;
- security, untrusted-input, credential, and target-mutation boundaries are explicit;
- rejected and deferred methods remain recorded;
- B2 tests and ownership work are concrete;
- Ali can explain why this is the smallest credible executable core.

## Current next action

Begin with implemented-truth inspection and source/test reconciliation.

Do not create the B2 implementation plan until the reconciliation and minimum runtime
responsibility have been reviewed and accepted.
