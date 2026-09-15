# Cycle 2 Static Consumer Build — Working Memory

**Date:** 2026-09-15  
**Session status:** ACTIVE  
**Primary mode:** Learning-by-Doing — Cycle 2 / Phase B Build  
**Selected parent plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Selected bounded implementation plan:** [`../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`](../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md)  
**Accepted architecture:** [`../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`](../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md)  
**Phase A decision owner:** [`2026-09-14_static-command-consumer-migration-and-identity.md`](2026-09-14_static-command-consumer-migration-and-identity.md)

## Cycle 2 state

```text
A — COMPLETE
B — IN PROGRESS
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

Phase B implements only the accepted A1–A6 migration contract. Cycle 3 runtime-strengthening policy remains out of scope.

---

## B1 — provider command location + direct-install parser-backed seam — IMPLEMENTED / PROOF NOT YET EXECUTED

### Change model

The first Build slice intentionally stops before changing the large CI composition surface.

```text
shared StaticCommandOccurrence
→ provider-owned StaticCommandLocation
→ dependency direct-install observer can consume StaticCommandAnalysis
→ focused dependency tests use only the parser-neutral analysis route
```

This establishes the new dependency-facing contract without yet claiming that the normal production CI caller has migrated.

### Source changes

#### 1. Provider-owned command location

Added:

`src/upgradepilot/github/workflow_command_location.py`

`StaticCommandLocation` contains:

```text
source_span
source_order
```

and is derived from `StaticCommandOccurrence`.

Its meaning remains only static occurrence source identity. It does not prove execution, success, or same-path ordering.

Commit:

`a5d372b525ee0e7b2c23bb8e17755fd6a01e2a93` — `feat: add static command location identity`

#### 2. Direct requirements can consume shared analysis

Updated:

`src/upgradepilot/dependency/direct_install.py`

New parser-backed input:

```text
RunStepDefinition
+ StaticCommandAnalysis
+ dependency source path / working-directory context
→ DirectInstallDeclarationObservation
```

The parser-backed route:

- consumes `StaticCommandOccurrence.executable` / `.arguments` directly;
- preserves current admitted `pip` / `pip3` and `python` / `python3 -m pip install` forms;
- reads bounded `-r` / `--requirement` values from typed atoms;
- preserves working-directory/path ownership in the dependency layer;
- returns unresolved when analysis itself is unresolved/unsupported/parse-error;
- preserves unresolved for material dynamic/unsupported pip/path atoms;
- lets an independently established matching literal requirements path survive unrelated dynamic arguments;
- accepts real static occurrences regardless of short-circuit/conditional-style structural tags because Cycle 2 is static declaration observation, not runtime strengthening;
- carries `command_location` when a specific parsed occurrence is established.

A temporary legacy route remains only because the normal CI orchestration caller has not yet been changed to provide `StaticCommandAnalysis`. It is explicitly transitional and is not used as fallback by the parser-backed route.

`matched_segment_index` likewise remains temporarily only for that unmigrated caller. New parser-backed observations leave it unset.

Commit:

`6566de0603c532653040ea42860502aaed044529` — `feat: consume parsed command analysis for direct installs`

#### 3. Focused dependency proof rewritten around parser-neutral IR

Updated:

`tests/test_direct_install_declaration.py`

The focused tests now inject `StaticCommandAnalysis` / `StaticCommandOccurrence` values directly rather than asking the dependency unit test to own shell parsing.

Protected behaviors include:

- ordinary direct requirements declaration;
- working-directory precedence;
- parent-path resolution;
- dynamic working-directory/path unresolved behavior;
- nonmatching source behavior;
- quoted/echoed command-looking payload not becoming a direct install;
- static declaration presence surviving short-circuit structural context;
- canonical occurrence source order through `command_location`;
- established positive requirement path surviving unrelated dynamic argument uncertainty;
- parser-analysis failure remaining unresolved with no textual fallback;
- invalid dependency-source boundary validation.

Commit:

`527a4c9234607654f8be3da9b672a73758c22c88` — `test: prove parser-backed direct install observation`

---

## B1 proof state

GitHub connector inspection confirms the three-commit delta from Phase B entry contains only:

```text
src/upgradepilot/github/workflow_command_location.py
src/upgradepilot/dependency/direct_install.py
tests/test_direct_install_declaration.py
```

The repository exposes no combined status checks and no workflow runs for commit `527a4c9...`.

Therefore the current proof statement is deliberately limited:

```text
implementation committed
+ focused tests written/reconciled
+ connector-side source/diff inspection performed
!= focused tests executed
!= nearby integration suite executed
!= production direct-requirements migration complete
```

Do not report these tests as passing until an execution environment actually runs them.

---

## Important retained transition boundary

The normal production path in `ci/workflow_commands.py` still calls:

```text
observe_direct_installation_declaration(...)
```

without supplying `StaticCommandAnalysis`.

Therefore it still reaches the temporary legacy splitter route.

This is intentional only across the B1 → B2 boundary. It must not be mistaken for final dual-path architecture.

The direct-requirements consumer is not considered migrated until the CI traversal analyzes the step once, passes the shared analysis into the observer, and downstream CI evidence stops depending on the old fabricated/segment ordinal contract.

---

## Next exact Build slice — B2

Migrate the normal direct-requirements production handoff:

```text
ci/workflow_commands.py
→ analyze_run_step_commands(definition, job, entry) once per run step
→ pass the same StaticCommandAnalysis to direct-install interpretation
→ carry canonical command location into CI consumption evidence
→ remove direct-requirements `segment_index=0` placeholders
→ stop deriving direct-requirements identity from `matched_segment_index`
→ remove the temporary direct-install legacy route once no production caller needs it
```

B2 must preserve checkout-provenance semantics and must not yet broaden into project-environment migration or direct-package invocation unless a small shared seam is necessary to avoid re-analysis.

If B2 requires changing `StaticDependencyConsumptionEvidence`, reconcile only the location fields needed by the direct-requirements path and keep project-environment migration explicit rather than silently rewriting its semantics.

After B2, run/obtain the narrowest executable proof available before moving into project-environment selection.

---

## Stop line

Do not during B2:

- change Cycle 3 runtime-strengthening eligibility;
- use `source_order` itself as execution-path proof;
- migrate project-environment semantics opportunistically unless required by a shared type contract and explicitly bounded;
- expand direct package invocation wrapper semantics;
- add runtime logs/artifacts, matrix/reusable-workflow execution, Python/custom-interpreter analysis, Target redesign, or maintainer-action enablement.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
