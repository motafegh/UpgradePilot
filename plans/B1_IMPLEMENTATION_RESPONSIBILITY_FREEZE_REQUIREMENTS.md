# B1 Implementation Responsibility Freeze Requirements

**Status:** Prepared; activation pending Ali acceptance of D1 synthesis  
**Date:** 2026-07-23  
**Parent route:** [`UPGRADEPILOT_90_DAY_PLAN.md`](UPGRADEPILOT_90_DAY_PLAN.md)  
**Evidence source:** [`../product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](../product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md)

This file prepares the next bounded project step. It is not an implementation plan and does not authorize code changes before the D1 acceptance review.

## Purpose

Freeze one minimum credible executable responsibility derived from S001–S005, reconcile it with the existing source and tests, and define the exact boundary for a later B2 implementation plan.

## Entry conditions

B1 may become active only when:

- Ali has reviewed the D1 final synthesis;
- material disagreements or misunderstandings are recorded and resolved or explicitly deferred;
- Ali accepts that the first executable core should begin from replay/fixture state rather than live acquisition;
- implementation remains inside the charter's public Python Dependabot boundary;
- no simulation artifact is treated as a final production schema.

## Required B1 work

### 1. Inspect implemented truth

Read the current source, tests, package configuration, commands, and outputs. Do not infer behavior from historical plans or documentation.

### 2. Reconcile existing implementation

Classify every relevant existing component as:

- retain unchanged;
- retain with correction;
- supersede;
- experimental evidence only;
- remove only when separately justified.

The superseded M2-S03 report-first route must not silently become the implementation boundary.

### 3. Freeze the minimum runtime responsibility

The accepted responsibility must cover, at minimum:

- replay-shaped invocation;
- exact frozen case identity;
- stable run and record identities;
- material operation history;
- evidence records and explicit states;
- observation/interpretation/finding separation;
- transparent baseline execution;
- bounded decision or abstention;
- machine and human projections from the same state;
- follow-up, rerun, supersession, and changed-boundary transitions;
- conditional-stage activation state;
- structural validation and security invariants;
- review and assistance state;
- no target mutation.

### 4. Define semantic boundary

B1 must state which inputs B2 may receive as prepared replay evidence or labeled interpretations, and which behavior B2 itself must execute deterministically.

B2 must not accept an unexplained final decision as fixture input.

### 5. Select the smallest reversible representation

Choose only the representation and interfaces necessary for B2. Do not preselect:

- database;
- services or queues;
- model or agent runtime;
- graph system;
- live GitHub/PyPI acquisition;
- deployment architecture.

Create an ADR only if a durable consequential choice is actually made.

### 6. Define B2 acceptance tests

At minimum:

- valid replay produces coherent run, baseline, decision, both reports, and transitions;
- invalid or inconsistent identity is rejected;
- missing and inaccessible evidence states remain visible;
- references and IDs resolve;
- baseline and full action may be same or different;
- conditional stages may be active or inactive;
- changed identity requires a new run;
- reports cannot disagree with accepted decision state;
- target mutation is impossible by default.

### 7. Define Ali ownership work

The eventual B2 plan must include Ali-owned work at a central point:

- predict one run outcome;
- implement or materially modify one runtime behavior;
- add or change one meaningful test;
- diagnose one deliberately introduced inconsistency;
- explain the complete path and limits without treating AI output as proof.

## B1 deliverables

B1 should produce only:

1. accepted minimum runtime responsibility;
2. current-source reconciliation record;
3. bounded representation and interface decision;
4. explicit universal and conditional responsibilities;
5. B2 acceptance and ownership gates;
6. one bounded B2 implementation plan after acceptance;
7. ADR only when justified.

Do not create multiple competing plans or architecture variants.

## Exit gate

B1 passes only when:

- the responsibility is evidence-derived and generalizes beyond one fixture;
- no semantic answer required from the product is hidden as unexplained caller input;
- universal and conditional responsibilities are explicit;
- the representation is reversible and adequate for B2;
- security and target-mutation boundaries are explicit;
- rejected and deferred methods remain recorded;
- Ali can explain why this is the smallest credible executable core.

## Current next action

Perform the Ali D1 acceptance review. After acceptance, inspect current source/tests and execute this freeze before writing the B2 implementation plan.