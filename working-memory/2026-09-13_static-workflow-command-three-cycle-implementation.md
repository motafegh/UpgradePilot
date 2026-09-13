# Static Workflow Command Analysis — Three-Cycle Implementation Working Memory

**Date:** 2026-09-13  
**Session status:** ACTIVE  
**Primary mode:** Learning-by-Doing — three-cycle implementation execution  
**Selected parent plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Selected bounded implementation plan:** [`../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`](../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md)  
**Accepted architecture:** [`../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`](../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md)  
**Previous design/planning memory:** [`2026-09-13_static-shell-direct-install-false-positive-recognition.md`](2026-09-13_static-shell-direct-install-false-positive-recognition.md)

## Three-cycle execution map

The accepted implementation plan will be executed through **three top-level Learning-by-Doing cycles**, each using the normal:

```text
A → B → C → D → E
```

These are not nested sub-cycles inside the previous Phase A. The previous architecture/planning Phase A is closed. Each cycle below owns one coherent implementation responsibility and must reach its own E reassessment before the next cycle starts.

### Cycle 1 — parser, shell-context, and shared command-analysis foundation

Responsibility:

```text
Tree-sitter runtime + grammar compatibility/characterization
→ effective GitHub Actions shell context resolution
→ parser-neutral UpgradePilot command-analysis IR
→ Bash/sh + PowerShell/pwsh + CMD/batch adapters
```

Purpose:

- prove that the selected parser substrate and grammar packages can actually support the admitted propositions under the supported Python environment;
- establish `syntax_family` separately from `execution_profile`;
- create one shared command occurrence/source identity before downstream consumers migrate;
- characterize parser errors, comments, quoting, source spans, command structure, and representative control-flow shapes per shell family;
- keep grammar-specific Tree-sitter nodes behind the adapter boundary.

Cycle 1 pass direction:

```text
compatible parser dependency set
+ characterized admitted grammars
+ conservative shell resolver
+ shared parser-neutral command IR
+ focused multi-shell proof
```

If a shell grammar fails its characterization gate, do not fall back to regex splitting. Preserve that family as unsupported/unresolved and reassess before claiming its admission.

### Cycle 2 — static evidence consumer migration and command identity correction

Responsibility:

```text
shared command-analysis producer
→ direct requirements observation
→ project-environment selection
→ CI direct package invocation / composition
→ segment_index / source-order reconciliation
→ same-step static ordering correction
```

Purpose:

- remove independent command splitting from dependency and CI consumers;
- make direct requirements and project-environment evidence operate on real parsed command occurrences;
- migrate direct package invocation to the same shared command identity;
- make source span/occurrence identity canonical;
- retain a source-order ordinal only if an admitted consumer independently requires it;
- prevent simple source order from being treated as same-path execution proof;
- remove comment/quoted-payload false positives across all migrated static observers.

Cycle 2 pass direction:

```text
one shared command identity source
+ migrated dependency consumers
+ migrated CI static invocation consumer
+ known false-positive classes closed
+ no duplicated normal-path splitters
+ focused + nearby static-composition proof
```

### Cycle 3 — runtime-strengthening correctness, consolidation, and broad proof

Responsibility:

```text
static command occurrence
+ structural/control-flow context
+ effective execution profile
+ exact correlated runtime step evidence
→ bounded runtime-strengthening eligibility
```

Purpose:

- introduce the explicit runtime-strengthening classifier required by ADR-0009;
- admit only command structures for which whole-step success justifies the stronger proposition;
- keep conditional, short-circuited, parser-ambiguous, or execution-profile-ambiguous occurrences static-only/unresolved at the stronger runtime proposition;
- correct direct-exercise/runtime composition where old segment/order assumptions overstate execution;
- remove any remaining obsolete inference routes;
- run focused, nearby, and full deterministic validation;
- perform the plan-level final reassessment before returning to the parent maintainer-action synthesis journey.

The first required positive strengthening class remains deliberately conservative:

```text
one cleanly parsed straightforward top-level command occurrence
+ established syntax family
+ established execution profile
+ exact correlated completed/successful runtime step
→ eligible for the currently admitted stronger runtime proposition
```

Cycle 3 pass direction:

```text
false static premise + successful step → never becomes supported runtime evidence
real conditional/path-dependent command + successful step → static evidence may remain, stronger execution claim does not
straightforward eligible command + successful correlated step → runtime strengthening remains available
+ focused/nearby/full deterministic proof green
```

## Why three cycles

Three cycles are the selected balance between two bad extremes:

```text
one giant implementation cycle
→ too much migration/proof risk before reassessment
```

and:

```text
many tiny cycles
→ fragmented execution, repeated ceremony, weak ownership continuity
```

The grouping follows real engineering boundaries:

1. establish a trustworthy producer/foundation;
2. migrate static consumers onto that producer;
3. compose runtime authority only after static semantics are trustworthy.

E of each cycle is a genuine gate. The next cycle is not automatic if new evidence changes the architecture, proof boundary, or implementation plan.

## Pre-implementation design/planning phase — CLOSED

The previous working memory completed the design responsibility:

```text
confirmed false-positive pressure
→ broader control-flow diagnosis
→ cross-layer owner trace
→ architecture/tooling comparison
→ ADR-0009 accepted
→ bounded P2 implementation/proof plan created
```

No product source/test implementation occurred during that Phase A.

The durable architecture is now owned by ADR-0009; the execution sequence/proof/stop line is owned by the selected implementation plan. This working memory owns only the dated three-cycle execution progression.

## Cycle 1 — current state

```text
Cycle 1: parser, shell-context, and shared command-analysis foundation

A — NEXT / NOT STARTED
B — NOT STARTED
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

### Cycle 1 A responsibility

Cycle 1 A should be bounded because the architecture is already decided. It must orient to the exact foundation implementation boundary and resolve only local questions still needed before Build, including:

- exact compatible Tree-sitter/runtime/grammar dependency set under the supported Python environment;
- representative grammar nodes/source spans/error behavior needed by each adapter;
- effective-shell precedence and runner/default ambiguity cases;
- smallest parser-neutral command IR fields required by current consumers;
- adapter error/admission behavior and the focused proof matrix;
- exact Cycle 1 Build stop line.

Cycle 1 A must not reopen the already accepted parser-backed architecture without new evidence showing ADR-0009 cannot satisfy the responsibility.

## Global implementation constraints retained

Across all three cycles:

- parse broadly, claim narrowly;
- Tree-sitter nodes remain implementation machinery, not dependency/CI contracts;
- parser success does not prove execution;
- unsupported/ambiguous parser or shell evidence remains conservative;
- do not silently fall back to old regex splitters for positive evidence;
- do not assume Bash grammar maturity transfers to PowerShell/CMD;
- do not absorb runtime logs/artifacts, matrix/reusable-workflow expansion, exact installed-version/wheel evidence, Target redesign, or maintainer-action enablement into these cycles;
- preserve the user preference that each A/B/C/D/E stage normally finishes in one or two substantive rounds unless evidence genuinely requires more or Ali explicitly requests finer steps.

## Current handoff

The previous architecture/planning Phase A is closed. The next live action is:

> **Cycle 1 — Phase A: parser, shell-context, and shared command-analysis foundation orientation/design.**

No product Build has been authorized by this working-memory transition itself.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`
