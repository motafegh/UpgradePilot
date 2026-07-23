# B1 Implementation Responsibility Freeze Requirements

**Status:** Active — implemented-truth inspection and clean source reset complete  
**Activated:** 2026-07-23  
**Owner:** Ali Rajabi  
**Parent route:** [`UPGRADEPILOT_90_DAY_PLAN.md`](UPGRADEPILOT_90_DAY_PLAN.md)  
**D1 acceptance:** [`D1_ACCEPTANCE_AND_B1_ACTIVATION.md`](D1_ACCEPTANCE_AND_B1_ACTIVATION.md)  
**Current reconciliation:** [`B1_CURRENT_SOURCE_AND_TEST_RECONCILIATION.md`](B1_CURRENT_SOURCE_AND_TEST_RECONCILIATION.md)  
**Clean reset:** [`../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md`](../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md)

B1 is the active stage. It must freeze one minimum credible executable responsibility
derived from S001–S005 before any new B2 product code is written.

## Completed B1 entry work

- Ali accepted D1.
- Current source, tests, package metadata, scripts, and outputs were inspected.
- The pre-reset M2 implementation was found narrower than the accepted runtime.
- Ali directed a clean active-source restart for learning clarity.
- Old code, tests, scripts, dependencies, and generated outputs were removed from active
  paths and preserved at immutable commit
  `e7425dcfc20f093ac10c9a903f1c4ae50a8b2638`.
- ADR-0002's Pydantic mandate was superseded.
- The active package is a dependency-free marker with no claimed runtime behavior.

This means B1 no longer chooses which old modules survive. It defines the new responsibility
from evidence and specifications without source inheritance.

## Purpose

Determine exactly:

- what the first executable UpgradePilot core must own;
- what replay input may supply as captured evidence or labeled prepared interpretation;
- what B2 must execute deterministically;
- what smallest representation, interface, and dependencies are adequate;
- what tests and Ali-owned work establish the gate.

## Required B1 work

### 1. Freeze the minimum runtime responsibility

The responsibility must cover, at minimum:

- replay-shaped invocation;
- exact frozen repository, PR, base, head, changed-file, dependency, and version identity;
- stable run and record identities;
- material operation history;
- evidence records with explicit states and provenance;
- observation, interpretation, and finding separation;
- versioned transparent baseline execution;
- conditional-stage activation and non-activation;
- bounded decision or abstention with reasons and limitations;
- machine and human projections from the same accepted state;
- follow-up, rerun, supersession, and changed-boundary transitions;
- structural identity and lineage validation;
- review, assistance, and ownership state;
- no target mutation.

The responsibility must be complete enough to demonstrate the accepted runtime, but small
enough to implement and understand without live acquisition, persistence, models, services,
or deployment infrastructure.

### 2. Define replay input

State explicitly what a replay fixture may contain.

Permitted candidates include:

- invocation request data;
- frozen public case identity captured from a real scenario;
- captured raw/reference public evidence;
- evidence-state labels and provenance;
- explicitly labeled prepared interpretations where semantic automation is not admitted;
- expected comparison values used only by tests, not by runtime decision code.

A fixture must not provide:

- an unexplained final decision;
- hidden expected actions consumed by product code;
- fixture-specific repository logic;
- an unlabeled semantic conclusion presented as raw evidence;
- credentials or private data.

### 3. Define deterministic B2 behavior

B2 must itself own:

- input validation;
- stable ID generation or verification;
- invocation-to-run boundary;
- accepted identity construction;
- operation and lifecycle state;
- evidence-state and provenance validation;
- reference and lineage validation;
- baseline execution;
- conditional responsibility activation/non-activation state;
- the bounded decision boundary selected by B1;
- report consistency;
- follow-up, rerun, supersession, and changed-boundary transitions;
- target-mutation prevention;
- deterministic serialization or projection required by the bounded interface.

No required product answer may be hidden as unexplained caller data.

### 4. Select the smallest dependency baseline

Begin from the standard library and the current dependency-free package.

A dependency may be admitted only when:

1. the frozen responsibility names a concrete requirement;
2. a credible standard-library implementation is compared;
3. complexity, learning cost, maintenance, security, upgrade burden, and reversal are
   explicit;
4. Ali understands and accepts the tradeoff;
5. the B2 plan and tests prove the admitted use.

Pydantic and OpenAI have no inherited status.

### 5. Select the smallest reversible representation and interface

Prefer cohesive modules directly under `src/upgradepilot/` until implemented responsibility
demonstrates a subpackage boundary.

Do not preselect:

- a database;
- services or queues;
- a model or agent runtime;
- a graph system;
- live GitHub/PyPI acquisition;
- deployment architecture;
- a web API or UI.

Select one bounded executable interface, likely a Python application function or minimal
command, only after comparing the simplest credible options.

### 6. Define universal and conditional responsibilities

Universal responsibilities must exist in every replay run.

Conditional responsibilities must be represented as active, inactive, skipped, failed, or
unresolved only when the case requires them. S003/S005 execution comparison, S003 failure
attribution, and S004 stopping evaluation must not become mandatory stages merely because
they appeared in simulations.

### 7. Define B2 acceptance tests

At minimum:

- valid replay produces coherent run state, baseline, decision, reports, and transitions;
- invalid or inconsistent identity is rejected;
- missing, inaccessible, partial, conflicting, and superseded evidence remain visible;
- IDs and references resolve;
- observations, interpretations, findings, and decisions cannot be silently collapsed;
- baseline and full action may be the same or different;
- conditional responsibilities may be active or inactive;
- an early-stop case does not activate unnecessary work;
- changed identity creates a new run boundary;
- reports cannot disagree with accepted decision state;
- follow-up and supersession are explicit;
- target mutation is impossible by default;
- no fixture can inject an unexplained final decision;
- active tests do not import archived code.

The B2 suite must include at least:

- one same-action case;
- one action-change case;
- one early-stop case;
- one degraded or missing-evidence case;
- one invalid identity or lineage case;
- one report-consistency or changed-boundary case.

### 8. Define Ali ownership work

The eventual B2 plan must require Ali to:

- predict one replay outcome before execution;
- implement or materially modify one central runtime behavior;
- add or change one meaningful acceptance test;
- diagnose one deliberately introduced identity, lineage, transition, or report-consistency
  defect;
- explain the full flow, authority boundary, conditional activation, stopping, and claim
  limits;
- explain why archived M2 code was not reused and why the selected dependency baseline is
  adequate.

AI-written code alone cannot satisfy this gate.

## B1 deliverables

B1 should produce only:

1. accepted minimum executable responsibility;
2. prepared-input versus deterministic-behavior boundary;
3. smallest dependency, representation, and interface decision;
4. explicit universal and conditional responsibilities;
5. B2 acceptance and Ali ownership gates;
6. one bounded B2 implementation plan after responsibility acceptance;
7. an ADR only when a durable consequential method is selected.

Do not create competing implementation plans or architecture variants.

## B1 exit gate

B1 passes only when:

- the responsibility is evidence-derived and independent of archived source;
- it generalizes beyond one replay fixture inside the charter boundary;
- no semantic answer required from the product is hidden as unexplained input;
- universal and conditional responsibilities are explicit;
- the dependency baseline and representation are reversible and adequate;
- security, untrusted-input, credential, and target-mutation boundaries are explicit;
- rejected and deferred methods remain recorded;
- B2 tests and ownership work are concrete;
- Ali can explain why this is the smallest credible executable core;
- one bounded B2 plan is accepted.

## Current next action

Freeze the clean-slate minimum executable responsibility and prepared-input versus
deterministic-runtime boundary.

Do not create B2 source until that freeze, its acceptance tests, Ali-owned work, and one
bounded implementation plan are reviewed and accepted.