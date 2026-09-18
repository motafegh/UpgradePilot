# Cycle 3 Phase B — Runtime-Strengthening Build Working Memory

**Date:** 2026-09-18  
**Status:** ACTIVE  
**Primary operation:** Build / Implement  
**Method:** Learning-by-Doing  
**Selected plan:** [`../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`](../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md)  
**Architecture owner:** [`../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`](../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md)  
**Phase-A design record:** [`2026-09-17_cycle3-runtime-strengthening-phase-a-orientation.md`](2026-09-17_cycle3-runtime-strengthening-phase-a-orientation.md)

## Responsibility

Implement the accepted Cycle-3 runtime-strengthening contract without reopening closed Phase-A
semantics unless executable evidence exposes a concrete contradiction.

The build must preserve this boundary:

```text
static command occurrence
+ provider-owned positive whole-step/position fact
+ effective execution profile
+ exact runtime step correlation
+ runtime status / continue-on-error interpretation
→ bounded Runtime-Correlated Support for the exact occurrence
```

It still does not prove exact inner-command execution/success, exact installed version,
artifact choice, compatibility, update safety, or maintainer action.

## Phase-B build roadmap

Phase B is one bounded implementation responsibility executed as three coherent build stages,
followed by final proof/closure.

### Build Stage 1 — Provider Structural Admission

Goal:

```text
existing Tree-sitter CST
→ bounded parser-neutral positive whole-step/position facts
→ known false-straightforward structures cannot enter the positive family
```

Scope:

- implement provider-owned positive facts for:
  - Sole Ordinary Top-Level Command Admission;
  - First Sequential Bash/sh Command Admission;
- use the whole parsed script, not `source_order == 0`, as the admission basis;
- prevent false positive admission for the Phase-A identified structures, including Bash
  status inversion, background/asynchronous execution, process substitution, compound
  structure, and relevant PowerShell/CMD non-command control-flow pressure;
- keep Tree-sitter nodes private;
- do not change CI runtime-strengthening behavior yet;
- add/adjust focused provider proofs only.

Stop line:

- no occurrence-level CI handoff yet;
- no runtime aggregation changes;
- no general shell CFG/interpreter;
- no S004 `&&` positive support.

Learning/recording rhythm:

```text
A — orient the provider structural responsibility
B — implement the bounded provider facts + focused tests
C — progressively record implementation/proof/limitations here
D — explain/teach what was actually built and why
E — repair any important understanding/implementation gap and orient Stage 2
```

Current state:

```text
A orientation                 ACTIVE
B implementation              NOT STARTED
C state preservation           ACTIVE
D post-build learning          NOT STARTED
E gap repair / next orientation NOT STARTED
```

### Build Stage 2 — Exact Occurrence Handoff and Eligibility

Goal:

```text
exact StaticCommandLocation
+ provider structural admission
+ execution profile
+ static proposition kind
→ exact runtime-strengthening candidate
→ eligible | ineligible | unresolved
```

Scope:

- preserve exact occurrence identity/context through the existing one-analysis traversal;
- do not invent a second command identity;
- classify eligibility from accepted provider facts + structural/profile facts;
- prove multiple occurrences in one step do not collapse into one strengthening candidate;
- keep `workflow_runtime_correlation.py` identity-only;
- stop before changing final workflow runtime aggregation.

Stage 2 begins only after Stage 1 is reviewed, recorded, and taught.

### Build Stage 3 — Runtime Composition

Goal:

```text
exact runtime-strengthening candidate
+ existing exact runtime step correlation
+ continue-on-error interpretation
+ factual runtime status/conclusion
→ supported | not_established | unresolved runtime-strengthening result
→ correct workflow static fallback / runtime-correlated / broader unresolved state
```

Scope:

- remove the current early `(job_key, step_source_index)` reduction from runtime
  strengthening;
- preserve factual failed/skipped/cancelled outcomes;
- preserve static `supported_not_correlated` when stronger evidence is merely unavailable
  or structurally inadmissible;
- keep eligible exact runtime non-success materially visible at the broader CI layer;
- apply the same exact-occurrence composition separately to direct exercise.

Stage 3 begins only after Stage 2 is reviewed, recorded, and taught.

### Final proof and Phase-B closure

After the three build stages:

```text
focused provider proof
→ focused eligibility/composition proof
→ runtime-correlated CI proof
→ direct-exercise proof
→ nearby regression proof
→ full deterministic product suite
→ S001/S002 useful-positive pressure
→ S004 deferred/re-entry pressure
→ state/memory closure
```

Record actual executable proof results. Historical test totals are not proof.

## Progressive-recording rule

After every material discovery, implementation decision, focused proof result, failure, or
scope correction:

1. update this working memory before moving materially forward;
2. distinguish planned behavior from actual source/test evidence;
3. preserve failures/proof debt explicitly;
4. update `MEMORY.md` only when the live stage/milestone/blocker changes;
5. do not silently move to the next build stage before the current stage's teaching/review.

## Stage-transition rule

For each Build stage:

```text
implement
→ inspect the actual diff/source
→ focused validation as available
→ record
→ teach/explain the logical + conceptual model
→ resolve material questions/gaps
→ only then enter the next stage
```

Ali may challenge or redirect any stage before the next transition.

## Current entry state

Phase A is complete and accepted.

Phase B Stage 1 is formally selected and authorized.

No Stage-1 product source/test mutation has yet been performed in this working record.

`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
