# B1 Implementation Responsibility Freeze Requirements — Historical Gate Record

**Historical status:** Completed; B2 entry accepted on 2026-07-24  
**Activated:** 2026-07-23  
**Completed:** 2026-07-24  
**Owner:** Ali Rajabi  
**Parent route:** [`UPGRADEPILOT_90_DAY_PLAN.md`](UPGRADEPILOT_90_DAY_PLAN.md)  
**Accepted B2 gate definition:** [`B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)  
**D1 acceptance:** [`D1_ACCEPTANCE_AND_B1_ACTIVATION.md`](D1_ACCEPTANCE_AND_B1_ACTIVATION.md)  
**Pre-reset reconciliation:** [`B1_CURRENT_SOURCE_AND_TEST_RECONCILIATION.md`](B1_CURRENT_SOURCE_AND_TEST_RECONCILIATION.md)  
**Clean reset:** [`../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md`](../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md)

This file preserves the requirements and evidence used to freeze the minimum credible public
PR vertical slice before B2 implementation began. It is a dated gate record, not the live
project position, selected plan, or continuation owner. Read [`../MEMORY.md`](../MEMORY.md)
for those facts.

## Historical B1 entry work

B1 began after:

- Ali accepted D1;
- source, tests, package metadata, scripts, and outputs were inspected;
- the pre-reset M2 implementation was found narrower than the accepted runtime;
- Ali directed a clean active-source restart for learning clarity;
- old code, tests, scripts, dependencies, and generated outputs were removed from active
  paths and preserved at immutable commit
  `e7425dcfc20f093ac10c9a903f1c4ae50a8b2638`;
- ADR-0002's Pydantic mandate was superseded;
- Ali rejected a replay-first B2 sequence because it introduced prepared inputs and internal
  terminology before the real product workflow.

The gate therefore had to define the new responsibility from evidence and specifications
without source inheritance. The first executable slice had to resemble the eventual product
from its public input through visible output.

## Purpose

B1 had to determine:

- what the first real public PR-to-decision UpgradePilot slice owns;
- what repository and PR input it accepts;
- what minimum public evidence it acquires read-only;
- what exact identity, evidence, evaluation, abstention, and output behavior B2 owns;
- what acquired responses are captured only for tests, debugging, and reproducibility;
- what smallest representation, interface, and dependencies are adequate;
- what tests and Ali-controlled work establish the gate.

## Required B1 work

### 1. Freeze the minimum real product responsibility

The responsibility had to begin with a public GitHub repository and Dependabot PR locator and
cover, at minimum:

- locator validation;
- read-only acquisition of PR metadata;
- exact repository, PR, base, head, and changed-file identity;
- one supported Python dependency-version change;
- the minimum relevant exact-head CI or check evidence available through the selected
  authorized interface;
- the minimum public package or upstream evidence required by the supported slice;
- explicit source, revision or time context, evidence state, and provenance;
- observation, interpretation, and finding separation where needed;
- transparent baseline execution;
- one bounded evidence-authority evaluation derived from S001–S005;
- conditional activation and non-activation only where required;
- bounded recommendation or abstention with reasons, uncertainty, and limitations;
- one concise human-readable result and minimum machine-readable state;
- capture of acquired responses or normalized evidence for deterministic testing and replay;
- no target mutation and no private-repository access.

The responsibility had to be complete enough to behave like the eventual product but small
enough to avoid premature persistence, services, queues, models, agents, deployment
infrastructure, exhaustive repository analysis, or a complete future artifact family.

### 2. Define the public input and acquisition boundary

The user-facing input was bounded to the public repository identity and Dependabot PR number
or an equivalent public PR URL.

B1 had to define:

- how the locator is validated;
- which GitHub data freezes the exact proposal;
- which changed-file and check information the first supported slice requires;
- which public package or upstream source is required, if any;
- what happens when information is missing, inaccessible, stale, malformed, contradictory,
  or changes during acquisition;
- whether unauthenticated public access is adequate or an optional token is justified;
- the exact no-write and permission boundary.

No caller may provide an unexplained final decision, hidden expected action,
repository-specific decision rule, or unlabeled semantic conclusion as product input.

### 3. Define B2 evaluation and output behavior

B2 was required to own:

- locator and acquired-response validation;
- exact identity construction and changed-head detection;
- dependency-change extraction for the selected supported form;
- evidence-state and provenance handling;
- the transparent baseline;
- a bounded CI or evidence-authority evaluation;
- conditional activation or justified non-activation;
- recommendation or abstention;
- reason and limitation consistency;
- human output and minimum machine-state consistency;
- target-mutation prevention;
- capture required for tests and reproducibility.

Captured responses may reproduce source evidence. They must not supply the product decision
to runtime logic. Expected decisions may exist only in tests or manual evaluation records.

### 4. Select the smallest dependency baseline

B1 required comparison against the standard library before admitting a dependency.

A dependency could be admitted only when:

1. the responsibility named a concrete requirement;
2. a credible standard-library implementation was compared;
3. complexity, learning cost, maintenance, security, upgrade burden, and reversal were explicit;
4. Ali understood and accepted the trade-off;
5. source and tests proved the admitted use.

This applied especially to HTTP access, data validation, version parsing, and command-line
handling. Pydantic, OpenAI, Requests, HTTPX, and other libraries had no inherited status.

### 5. Select the smallest reversible representation and interface

B1 required cohesive modules directly under `src/upgradepilot/` until implemented
responsibility demonstrated a subpackage boundary.

It prohibited preselection of:

- a database;
- services or queues;
- a model or agent runtime;
- a graph system;
- deployment architecture;
- a web API or UI;
- a large contract or artifact hierarchy.

The first interface had to be one bounded command or Python application function accepting a
repository and PR number after comparing the simplest credible options.

### 6. Define universal and conditional responsibilities

Universal responsibilities for a supported B2 analysis:

- locator validation;
- public read-only acquisition;
- exact identity freezing;
- supported dependency-change recognition or explicit unsupported state;
- evidence-state preservation;
- recommendation or abstention;
- reasons and limitations;
- no target mutation.

Conditional responsibilities activate only when required. Upstream evidence, deeper CI
inspection, stopping evaluation, targeted-check design, failure attribution, dynamic
reproduction, and similar work must not become mandatory merely because one simulation used
them.

### 7. Define B2 acceptance tests

The gate required, at minimum:

- a real public smoke path that accepts a repository and Dependabot PR locator, freezes the
  exact proposal, and reaches a bounded result or honest abstention;
- deterministic tests using controlled responses or normalized evidence without live-network dependence;
- invalid repository or PR input rejection;
- changed-head detection rather than silent evidence mixing;
- an explicit unsupported result for an unsupported dependency-change shape;
- visible missing, inaccessible, partial, conflicting, or malformed evidence;
- sufficient, insufficient, or unresolved CI authority;
- justified non-activation in an early-stop case;
- consistent human and machine outputs;
- no captured expected decision consumed by product logic;
- target mutation impossible by default;
- no active import of archived code.

The initial suite was to prove the smallest supported path and representative negative states,
not broad domain coverage.

### 8. Define Ali-controlled ownership work

The B2 gate required Ali eventually to:

- explain the real request-to-evidence-to-output flow;
- predict a result or abstention before execution;
- implement or materially modify a central acquisition, identity, extraction, evaluation, or
  output behavior;
- add or change a meaningful test;
- diagnose a deliberately introduced acquisition, identity, evidence-authority, or output defect;
- explain the permission boundary, evidence authority, stopping condition, and claim limits;
- explain why archived M2 code was not reused and why the selected dependency baseline is adequate.

AI-written code alone cannot satisfy this ownership requirement.

## Historical B1 deliverables

B1 produced:

1. an accepted minimum public PR-to-decision vertical-slice definition;
2. minimum acquisition, identity, evaluation, abstention, and output boundaries;
3. captured-response testing and replay-support boundaries;
4. reversible dependency, representation, and interface decisions;
5. B2 acceptance and ownership gates;
6. a bounded B2 plan;
7. no additional ADR where reversible choices did not require one.

## Historical exit evidence

B2 entry was accepted because:

- the responsibility was evidence-derived and independent of archived source;
- the interface began with a real public repository and Dependabot PR locator;
- the supported slice generalized beyond one known PR inside the charter boundary;
- acquisition, exact identity, evidence, evaluation, output, and abstention were explicit;
- captured responses supported testing and reproducibility without supplying product answers;
- universal and conditional responsibilities were separated;
- the dependency baseline and representation were reversible and adequate;
- security, untrusted-input, credentials, permissions, rate limits, and target-mutation
  boundaries were explicit at the required entry depth;
- B2 tests and ownership work were concrete;
- Ali accepted the bounded B2 entry definition.

This record has no live handoff. The route, selected plan, latest verified behavior, and exact
continuation are owned only by `../MEMORY.md`.