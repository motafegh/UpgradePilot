# B2 Cross-Responsibility Architecture Reconciliation — Phase-D Closure

**Date:** 2026-08-15  
**Operation:** Phase-D decision classification, durable promotion, and Phase-E handoff  
**Result classification:** ACCEPTED / PHASE D COMPLETE  
**Primary reasoning record:** [`2026-08-14_B2-cross-responsibility-architecture-reconciliation-progress.md`](2026-08-14_B2-cross-responsibility-architecture-reconciliation-progress.md)  
**Phase-C simulation evidence:** [`../product-simulation/CROSS_RESPONSIBILITY_ARCHITECTURE_PHASE_C_PRESSURE_TEST_01.md`](../product-simulation/CROSS_RESPONSIBILITY_ARCHITECTURE_PHASE_C_PRESSURE_TEST_01.md)  
**Durable architecture owner:** [`../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md`](../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md)  
**Implementation handoff:** [`../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md`](../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md)

## 1. Purpose

Close the Phase-D portion of the selected B2 cross-responsibility architecture checkpoint after the progressive Phase-A/B investigation, Phase-C adversarial/transfer pressure, and explicit D1–D4 decisions were accepted.

This record is a closure/acceptance addendum, not a second progressive investigation. The August 14 progressive record remains the detailed reasoning/evidence trail through F-054. Stable accepted architecture is now promoted to ADR-0008, implementation sequencing to the Phase-E plan, parser safety to `SECURITY.md`, and live continuation to `MEMORY.md`.

## 2. Evidence basis carried into Phase D

Phase D did not reopen the architecture search. It classified the pressure-tested conclusions already established by:

- current source and tests across GitHub, CI, Target, dependency, impact, and application orchestration;
- ADR-0007 source-responsibility ownership;
- AUDIT-002 CI proof-strength hazards;
- real S002/S004 workflow structure;
- S008 target/artifact evidence separation;
- S011 optional-environment/CI-coverage pressure;
- S010 heterogeneous-mechanism pressure;
- the simulation-side Phase-C pressure test;
- main-side supplemental S003/S005/S007/S012 checks.

The combined Phase-C conclusion entering Phase D was:

```text
OPTION B
SUPPORTED WITH REQUIRED MODIFICATIONS / CONSTRAINTS
```

No examined pressure required returning to duplicated local CI/Target parsers or adopting a broad combined static+runtime base abstraction.

## 3. Accepted D1 — shared static workflow architecture

Accepted:

```text
RepositoryTextFile
        ↓
bounded provider-specific GitHub Actions static workflow-definition IR
owner = upgradepilot.github
        ↓
   ┌────┴────┐
   ▼         ▼
  CI       Target
```

Also accepted:

- the shared structural layer preserves multiple safely readable jobs and visible provider structure;
- `needs` and source order remain structural evidence, not runtime continuity proof;
- dynamic values are readable structure rather than parser failure;
- CI and Target remain separate interpreters with different semantic responsibilities.

Rejected:

```text
one broad base object that merges
static workflow definition
+
runtime WorkflowRun / WorkflowJob / WorkflowStep
```

Deferred:

- arbitrary multi-job CI/Target semantic composition;
- cross-job environment continuity/transfer inference.

## 4. Accepted D2 — parser method and proportional security

Accepted method:

```text
RepositoryTextFile.content
        ↓
PyYAML representation/node parsing
        ↓
bounded GitHub Actions extraction
        ↓
typed provider IR
```

PyYAML is accepted as the selected parser dependency/method. Actual dependency addition/version-range proof belongs to Phase E.

Parser/node objects remain internal syntax machinery; UpgradePilot does not expose a generic YAML AST/domain model.

Accepted proportional untrusted-YAML boundary:

- no arbitrary application-object construction;
- malformed/materially ambiguous source fails safely;
- preserve the existing repository source-size bound;
- detect ambiguity where silent key/identity collapse would fabricate meaning;
- apply bounded traversal/recursion sufficient for obvious alias/cycle/resource abuse;
- keep exact numeric budgets/implementation mechanics in Phase E unless evidence justifies stronger policy.

The general invariant was promoted to [`../SECURITY.md`](../SECURITY.md).

Rejected:

- default/arbitrary-object YAML loading of untrusted repository evidence;
- expanding parser hardening into an unrelated hostile-parser framework without demonstrated need.

## 5. Accepted D3 — Target/CI proof semantics

### Target

Accepted that the current static-only:

```text
dependency_environment_formation = established | not_observed
```

uses runtime-sounding semantics that must migrate during Tranche 1 to a static direct-installation-declaration/configuration proposition.

Exact replacement type/field names are implementation work.

### Shared direct-install observation

Accepted one bounded dependency-owned primitive:

```text
static run command
+ effective working-directory context
+ independently established dependency-source path
→ direct installation declaration observation
```

Owner:

```text
upgradepilot.dependency
```

Its proof strength stops at declaration/configuration.

```text
direct install declaration observed
!= executed
!= succeeded
!= exact proposed version installed
!= generic dependency consumption
!= package exercise
```

S005 is the key guard against over-generalization: exact dependency authority may flow through lock/resolver/tox/uv/matrix or other evidence chains.

### CI

Package invocation/exercise recognition remains CI-specific.

Accepted that current CI `state="proven"` semantics must be narrowed/refined during Tranche 1 so successful exact-head run/job evidence plus static install/invocation recognition is not presented as matched-command runtime-success proof.

### Static↔runtime correlation

Accepted as a **separate optional architecture responsibility**, but exact matching algorithm/implementation is deferred to Tranche 2.

```text
static workflow IR
        │
        │ explicit optional correlation
        ▼
runtime WorkflowRun / WorkflowJob / WorkflowStep
```

Stronger correlation remains proposition/evidence-relative rather than a universal mandatory pipeline stage.

## 6. Accepted D4 — surrounding architecture and handoff

### Heterogeneous mechanism orchestration

Accepted responsibility pressure:

```text
application orchestration must eventually carry multiple
mechanism-specific typed results without endless per-mechanism field sprawl
```

Exact envelope/type design is deferred until artifact serviceability actually enters the real application path.

No universal impact/result object and no orchestration ADR is accepted now.

### Repository-path drift

Accepted a bounded cleanup under existing ADR-0007 ownership:

```text
github/repository.py private repository-path validator
→ remove/reconcile
→ reuse source-neutral src/upgradepilot/repository_path.py
```

Provider-specific path meaning remains with the provider caller.

No new ADR is required for this correction.

### Durable promotion

Accepted one new ADR rather than multiple fragmented ADRs:

- [`ADR-0008-bounded-static-github-actions-workflow-definition.md`](../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md)

The ADR owns:

- shared provider-specific static workflow IR;
- `upgradepilot.github` ownership;
- multi-job structural preservation;
- static/runtime base-contract separation;
- PyYAML method selection;
- provider/domain dependency direction;
- shared direct-install declaration boundary;
- proof-strength migration requirement;
- rejected broad combined/universal alternatives.

No broad Product Decision Model specification rewrite is required; framework-independent proof-strength semantics remain owned by the existing canonical specification.

### Implementation promotion

Accepted one bounded Phase-E implementation/refactor plan:

- [`B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md`](../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md)

It separates:

```text
Tranche 1
static IR + PyYAML + consumer migration + semantic correction + path cleanup

Tranche 2
optional static↔runtime correlation + stronger CI proof

later separate responsibility
heterogeneous mechanism orchestration when second mechanism enters application path
```

## 7. Durable-owner map after closure

```text
framework-independent evidence/decision semantics
→ docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md

shared GitHub Actions static architecture + PyYAML method
→ docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md

source responsibility baseline
→ docs/architecture/ADR-0007-responsibility-based-python-subpackages.md

untrusted workflow parser safety invariant
→ SECURITY.md

implementation sequence / validation / stop lines
→ plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md

Phase A–C reasoning/evidence
→ working-memory/2026-08-14_B2-cross-responsibility-architecture-reconciliation-progress.md

Phase-D acceptance/promotion provenance
→ this closure record

live continuation / latest verification
→ MEMORY.md
```

## 8. Architecture checkpoint result

Phase D is complete.

Accepted architecture:

```text
RAW EXACT REPOSITORY WORKFLOW
        ↓
BOUNDED GITHUB ACTIONS STATIC IR
        ↓
   ┌────┴────┐
   ▼         ▼
  CI       Target

separate runtime Actions evidence
        ↓
optional later explicit correlation
```

The key proof boundary remains:

```text
static declaration
!= runtime execution
!= runtime success
!= environment formation
!= dependency exercise
```

The key abstraction boundary remains:

```text
share the lowest layer where meaning is genuinely identical
keep domain conclusions with their responsible consumer
```

## 9. Implementation authorization and stop line

Phase-D acceptance authorizes **Phase E planning/execution under the new implementation plan**, not unbounded source work.

Immediate implementation should begin with Tranche 1 only.

Do not silently bundle Tranche 2 runtime correlation or heterogeneous mechanism orchestration into the first migration.

Implementation evidence must be recorded separately with exact source/test/command results. This closure record does not prove that ADR-0008 is implemented.
