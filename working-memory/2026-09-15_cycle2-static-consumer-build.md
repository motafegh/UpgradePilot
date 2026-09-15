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

Learning cadence agreed with Ali for the rest of B:

```text
each bounded Build slice
→ brief what / why / remaining-transition checkpoint

Phase B fully implemented + validated
→ one proper integrated implementation-learning session over the stable final code
```

This avoids teaching temporary intermediate compatibility shapes as if they were final architecture.

---

## B1 — provider command location + direct-install parser-backed seam — IMPLEMENTED / PROOF NOT YET EXECUTED

### Change model

The first Build slice intentionally stopped before changing the large CI composition surface.

```text
shared StaticCommandOccurrence
→ provider-owned StaticCommandLocation
→ dependency direct-install observer can consume StaticCommandAnalysis
→ focused dependency tests use only the parser-neutral analysis route
```

### Source changes

Added:

`src/upgradepilot/github/workflow_command_location.py`

`StaticCommandLocation` contains:

```text
source_span
source_order
```

and is derived from `StaticCommandOccurrence`. Its meaning remains static occurrence source identity only.

Updated:

`src/upgradepilot/dependency/direct_install.py`

The parser-backed observer:

- consumes typed executable/argument atoms directly;
- preserves current admitted `pip` / `pip3` and `python` / `python3 -m pip install` forms;
- reads bounded `-r` / `--requirement` values from typed atoms;
- preserves working-directory/path ownership in the dependency layer;
- returns unresolved when analysis itself is unresolved/unsupported/parse-error;
- preserves unresolved for material dynamic/unsupported pip/path atoms;
- lets an independently established matching literal requirements path survive unrelated dynamic arguments;
- accepts real static occurrences regardless of path-dependent structural tags because declaration presence is not execution proof;
- carries `command_location` when a specific parsed occurrence is established.

Focused tests in `tests/test_direct_install_declaration.py` were rewritten around parser-neutral analysis fixtures.

B1 commits:

```text
a5d372b525ee0e7b2c23bb8e17755fd6a01e2a93  feat: add static command location identity
6566de0603c532653040ea42860502aaed044529  feat: consume parsed command analysis for direct installs
527a4c9234607654f8be3da9b672a73758c22c88  test: prove parser-backed direct install observation
c6006285e5860809d798a3177a9c4c6a9424cd49  docs: preserve cycle 2 build slice one
```

B1 proof statement remained:

```text
implementation committed
+ focused tests written/reconciled
+ connector source/diff inspection
!= focused tests executed
!= nearby integration proof
!= production direct-requirements migration complete
```

---

## B2 — production direct-requirements + parsed invocation/order handoff — IMPLEMENTED / EXECUTION PROOF PENDING

### Why B2 expanded slightly from the initial handoff description

Once direct-requirements evidence stopped carrying the old integer ordinal, the existing direct-exercise classifier could no longer safely compare:

```text
(step_source_index, segment_index)
```

Retaining or fabricating an integer merely to keep that classifier alive would violate accepted A3/A6. The smallest coherent implementation therefore migrated the tightly coupled seam together:

```text
one parsed run-step analysis
→ direct-requirements interpretation
→ direct-package invocation interpretation
→ canonical occurrence locations
→ explicit bounded static ordering relation
```

Project-environment selection itself was deliberately left for the next slice.

### Production handoff

Updated:

`src/upgradepilot/ci/workflow_commands.py`

For each readable `RunStepDefinition` in the normal CI evidence pass:

```text
command_analysis = analyze_run_step_commands(definition, job, entry)
```

is now established once and reused by both:

```text
direct requirements observer
CI direct-package invocation observer
```

Direct-requirements CI evidence now carries:

```text
outer workflow/job/step identity
+ command_location
+ structural_context
```

and uses:

```text
segment_index = None
```

No `0` placeholder is fabricated for migrated unresolved evidence.

### Direct-install legacy route removed

`src/upgradepilot/dependency/direct_install.py` now requires `StaticCommandAnalysis` from its caller.

The B1 regex / `bounded_shell_segments(...)` compatibility route was removed. The migrated direct-requirements observer therefore has no textual positive-evidence fallback.

`matched_segment_index` remains only as a temporary data-field compatibility surface while the rest of Cycle 2 migrates; the parser-backed producer never populates it.

### Direct package invocation now comes from parsed occurrences

`ci/workflow_commands.py` no longer uses `_first_package_invocation_segment_index(...)` or the old general CI `_shell_segments(...)` path for direct invocation.

The first migrated recognizer preserves only the accepted shapes:

```text
<package>
python/python3 -m <package>
uv run <package>
poetry run <package>
pipenv run <package>
coverage run -m <package>
```

Positive invocation evidence carries:

```text
command_location
structural_context
```

A recognized literal wrapper with a material dynamic/unsupported prefix or target is retained as typed `unresolved` invocation evidence rather than converted to absence.

### Explicit static ordering owner

Added:

`src/upgradepilot/ci/static_command_order.py`

It owns only:

```text
consumption vs invocation
→ ordered_after | not_after | unresolved
```

Rules implemented:

- different job → not after;
- later user-defined step in same job → ordered after;
- earlier user-defined step → not after;
- same-step parsed occurrences require strictly increasing `source_order`;
- a later same-step occurrence with short-circuit / conditional / loop / pipeline / function-or-block / nested-or-subshell structure → unresolved;
- same/earlier occurrence → not after;
- mixed parsed/legacy same-step identities → unresolved rather than guessed.

A temporary legacy-to-legacy `segment_index` comparison remains only for the not-yet-migrated project-environment identity path. Parsed evidence is never converted back to an ordinal for this purpose.

### Direct-exercise composition corrected

Updated:

`src/upgradepilot/ci/dependency_exercise.py`

Positive direct exercise now requires the explicit ordering relation to return `ordered_after`.

Path-dependent same-step source order becomes `unresolved`, not supported. Runtime correlation remains job/step scoped exactly as before; Cycle 3 runtime-strengthening policy was not changed.

### Evidence contract transition

Updated:

`src/upgradepilot/ci/consumption.py`

`StaticDependencyConsumptionEvidence` now permits:

```text
segment_index: int | None
command_location: StaticCommandLocation | None
structural_context: tuple[StaticCommandStructure, ...]
```

Current meaning:

```text
direct_requirements
→ parsed command location + structure; segment_index None

project_environment
→ temporary legacy segment identity until B3
```

This is an explicit migration state, not intended final dual architecture.

### Test/proof assets written

Added:

- `tests/test_static_command_order.py`
- `tests/test_parser_backed_ci_command_evidence.py`
- `tests/test_ci_static_direct_exercise_order.py`

They protect:

- later-step ordering;
- clean same-step ordering;
- short-circuit same-step unresolved behavior;
- before-consumption not-after behavior;
- mixed legacy/parsed same-step unresolved behavior;
- one shared analysis supplying both consumption and invocation locations;
- quoted command-looking payload not manufacturing invocation;
- other-repository checkout not rebinding parsed evidence;
- unresolved shell context not fabricating command identity;
- clean same-step install → package invocation support;
- short-circuit install → invocation remaining unresolved.

Existing CI synthetic fixtures in:

- `tests/test_workflow_dependency_evidence.py`
- `tests/test_ci_dependency_coverage.py`

were corrected to explicitly establish Bash through workflow `defaults.run.shell`. This preserves what those tests actually own—CI composition—without weakening the provider rule that an omitted/unknown runner does not establish a default shell.

### B2 commit

```text
328e0b2eee3652e6a552a7b1cfbfda3c46b4c44a
feat: migrate direct CI command evidence to parsed identity
```

The commit is one coherent tree update so `main` does not pass through temporarily incompatible identity contracts.

### B2 audit result

Post-commit connector inspection confirmed:

- direct requirements use shared parser analysis in the production CI path;
- direct package invocation uses the same analysis;
- migrated direct requirements do not fabricate `segment_index=0`;
- old direct-install textual fallback is gone;
- old CI package-invocation splitter/regex path is gone;
- the only remaining textual command splitter in `ci/workflow_commands.py` is explicitly named/scoped to legacy project-environment validation.

GitHub Actions inspection for `328e0b2...` reports zero workflow runs. The repository's sole verification workflow is `workflow_dispatch` only, so no push-triggered execution proof exists for this commit.

Therefore the current proof statement is:

```text
B2 implementation committed
+ source/diff audit complete
+ focused/integration tests written or reconciled
+ source strings syntax-checked during Build preparation
!= repository test suite executed
!= hosted verification run executed
```

Do not report B2 tests as passing until an execution environment actually runs them.

---

## Current transition boundary after B2

Migrated:

```text
direct requirements
CI direct package invocation
bounded direct-exercise ordering for parsed evidence
```

Still legacy / next target:

```text
dependency/environment_selection.py
→ textual segmentation + regex/shlex
→ ProjectEnvironmentSelectionDeclaration.segment_index

derive_project_environment_consumptions(...)
→ separate workflow parse/traversal

project-environment CI validation
→ temporary legacy segment validation
```

Because A1 ultimately requires one workflow-level traversal and one analysis per run step reused by all static consumers, Phase B is not complete yet.

---

## Next exact Build slice — B3

Migrate project-environment selection onto shared `StaticCommandAnalysis` and canonical command location while preserving dependency-owned pip/uv semantics.

Target shape:

```text
RunStepDefinition
+ same StaticCommandAnalysis
+ project path/default context
→ ProjectEnvironmentSelectionObservation / declarations
   carrying canonical command occurrence location
```

Then reconcile:

- `ProjectEnvironmentSelectionDeclaration.segment_index` → command location;
- unresolved project-environment evidence without fabricated location;
- project-environment CI composition/validation against exact analyzed occurrence;
- removal of `_legacy_project_environment_shell_segments(...)` once no consumer needs it;
- movement toward the accepted single workflow traversal rather than the current separate `derive_project_environment_consumptions(...)` parse/walk.

Do not broaden uv/pip selector semantics during this migration.

### Proof requirement before Phase B closure

Phase B cannot be called complete from source inspection alone. Obtain executable focused/nearby proof when an execution route is available, then broaden proportionately before B closure.

---

## Stop line

Do not during B3:

- change Cycle 3 runtime-strengthening eligibility;
- treat static source order as execution proof;
- broaden uv/poetry/pipenv wrapper semantics;
- introduce general control-flow simulation;
- add runtime logs/artifacts, matrix/reusable-workflow execution, Python/custom-interpreter analysis, Target redesign, exact installed-version/wheel evidence, or maintainer-action enablement;
- keep textual splitters as a positive-evidence path after project-environment migration is complete.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
