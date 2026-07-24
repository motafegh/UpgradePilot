# B1 Implementation Responsibility Freeze Requirements

**Status:** Active — real PR vertical-slice correction accepted  
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
- Ali rejected the replay-first B2 sequence because it introduced internal terminology and
  an artificial starting interface before the real product workflow was understood.

This means B1 defines the new responsibility from evidence and specifications without
source inheritance, and the first executable slice must resemble the eventual product from
its initial input through its visible output.

## Purpose

Determine exactly:

- what the first real public PR-to-decision UpgradePilot slice must own;
- what repository and PR input it accepts;
- what minimum public evidence it acquires read-only;
- what exact identity, evidence, evaluation, abstention, and output behavior B2 owns;
- what acquired responses are captured only for tests, debugging, and reproducibility;
- what smallest representation, interface, and dependencies are adequate;
- what tests and Ali-owned work establish the gate.

## Required B1 work

### 1. Freeze the minimum real product responsibility

The responsibility must begin with a public GitHub repository and Dependabot PR locator and
cover, at minimum:

- locator validation;
- read-only acquisition of PR metadata;
- exact repository, PR, base, head, and changed-file identity;
- one supported Python dependency-version change;
- the minimum relevant exact-head CI/check evidence available through the selected
  authorized interface;
- the minimum public package or upstream evidence required by the selected slice;
- evidence records with explicit source, revision/time context, state, and provenance;
- observation, interpretation, and finding separation where the slice needs it;
- transparent baseline execution;
- one bounded evidence-authority evaluation derived from S001–S005;
- conditional-stage activation and non-activation only where required;
- bounded recommendation or abstention with reasons, uncertainty, and limitations;
- one concise human-readable result and minimum machine-readable state;
- capture of acquired responses or normalized evidence for deterministic testing and later
  replay;
- no target mutation and no private-repository access.

The responsibility must be complete enough to behave like the eventual product, but small
enough to implement and understand without persistence, services, queues, models, agents,
deployment infrastructure, exhaustive repository analysis, or the full future artifact
family.

### 2. Define the live input and acquisition boundary

The initial user-facing input should be no more than the public repository identity and
Dependabot PR number or an equivalent public PR URL.

B1 must define:

- how the locator is validated;
- which GitHub data is required to freeze the exact proposal;
- which changed-file and check information is required by the first supported slice;
- which public package or upstream source is required, if any;
- what happens when information is missing, inaccessible, stale, malformed, contradictory,
  or changes during acquisition;
- whether unauthenticated public access is adequate or an optional token is justified;
- the exact no-write and permission boundary.

No caller may provide an unexplained final decision, hidden expected action,
repository-specific decision rule, or unlabeled semantic conclusion as product input.

### 3. Define B2 evaluation and output behavior

B2 must itself own:

- locator and acquired-response validation;
- exact identity construction and changed-head detection;
- dependency-change extraction for the selected supported form;
- evidence-state and provenance handling;
- the transparent baseline;
- the bounded CI/evidence-authority evaluation selected by B1;
- conditional activation or justified non-activation;
- recommendation or abstention;
- reason and limitation consistency;
- human output and minimum machine state consistency;
- target-mutation prevention;
- capture required for tests and reproducibility.

Captured responses may reproduce source evidence. They must not supply the product decision
to runtime logic. Expected decisions may exist only in tests.

### 4. Select the smallest dependency baseline

Begin from the standard library and the current dependency-free package.

A dependency may be admitted only when:

1. the frozen responsibility names a concrete requirement;
2. a credible standard-library implementation is compared;
3. complexity, learning cost, maintenance, security, upgrade burden, and reversal are
   explicit;
4. Ali understands and accepts the tradeoff;
5. the B2 plan and tests prove the admitted use.

This comparison applies especially to HTTP access, data validation, version parsing, and
command-line handling. Pydantic, OpenAI, Requests, HTTPX, and other libraries have no
inherited status.

### 5. Select the smallest reversible representation and interface

Prefer cohesive modules directly under `src/upgradepilot/` until implemented responsibility
demonstrates a subpackage boundary.

Do not preselect:

- a database;
- services or queues;
- a model or agent runtime;
- a graph system;
- deployment architecture;
- a web API or UI;
- a large contract or artifact hierarchy.

Select one bounded user-facing interface, likely a minimal command or Python application
function accepting a repository and PR number, only after comparing the simplest credible
options.

### 6. Define universal and conditional responsibilities

Universal responsibilities must exist in every supported B2 analysis:

- locator validation;
- public read-only acquisition;
- exact identity freezing;
- supported dependency-change recognition or explicit unsupported state;
- evidence-state preservation;
- recommendation or abstention;
- reasons and limitations;
- no target mutation.

Conditional responsibilities activate only when the case requires them. Upstream evidence,
deeper CI responsibility inspection, stopping evaluation, targeted-check design, failure
attribution, dynamic reproduction, and similar work must not become mandatory merely
because they appeared in simulations.

### 7. Define B2 acceptance tests

At minimum:

- a real public smoke path accepts a repository and Dependabot PR locator, freezes the exact
  proposal, and reaches a bounded result or honest abstention;
- deterministic tests use captured responses or normalized evidence without live-network
  dependence;
- invalid repository or PR input is rejected;
- a changed head is detected rather than silently mixed with earlier evidence;
- an unsupported dependency-change shape produces an explicit unsupported state or
  abstention;
- missing, inaccessible, partial, conflicting, or malformed evidence remains visible;
- relevant CI authority may be sufficient or insufficient;
- an early-stop case does not activate unnecessary work;
- human and machine outputs cannot disagree;
- no captured expected decision is consumed by product logic;
- target mutation is impossible by default;
- active tests do not import archived code.

The initial suite should include only the smallest set needed to prove the slice, including:

- one successful S004-shaped path;
- one missing or insufficient-evidence path;
- one invalid locator or identity path;
- one changed-head or output-consistency path.

Additional same-action, action-change, and broader dependency-shape cases belong when the
implemented responsibility reaches them.

### 8. Define Ali ownership work

The eventual B2 plan must require Ali to:

- explain the real request-to-evidence-to-output flow before implementation;
- predict one public PR result or abstention before execution;
- implement or materially modify one central acquisition, identity, extraction, evaluation,
  or output behavior;
- add or change one meaningful test;
- diagnose one deliberately introduced acquisition, identity, evidence-authority, or output
  defect;
- explain the permission boundary, evidence authority, stopping condition, and claim limits;
- explain why archived M2 code was not reused and why the selected dependency baseline is
  adequate.

AI-written code alone cannot satisfy this gate.

## B1 deliverables

B1 should produce only:

1. accepted minimum public PR-to-decision vertical slice;
2. minimum acquisition, identity, evaluation, abstention, and output boundary;
3. captured-response testing and replay support boundary;
4. smallest dependency, representation, and interface decision;
5. B2 acceptance and Ali ownership gates;
6. one bounded B2 implementation plan after responsibility acceptance;
7. an ADR only when a durable consequential method is selected.

Do not create competing implementation plans, architecture variants, or a separate replay
product path.

## B1 exit gate

B1 passes only when:

- the responsibility is evidence-derived and independent of archived source;
- the first interface begins with a real public repository and Dependabot PR locator;
- the supported slice generalizes beyond one known PR inside the charter boundary;
- acquisition, exact identity, evidence, evaluation, output, and abstention are explicit;
- captured responses support testing and reproducibility without supplying product answers;
- universal and conditional responsibilities are explicit;
- the dependency baseline and representation are reversible and adequate;
- security, untrusted-input, credentials, permissions, rate limits, and target-mutation
  boundaries are explicit;
- B2 tests and ownership work are concrete;
- Ali can explain why this is the smallest credible real end-to-end product slice;
- one bounded B2 plan is accepted.

## Current next action

Freeze the minimum public PR-to-decision vertical slice, beginning with repository and PR
input and ending with a bounded recommendation or abstention from newly acquired public
evidence.

Do not create B2 source until that slice, its acquisition and evaluation boundaries, tests,
Ali-owned work, and one bounded implementation plan are reviewed and accepted.