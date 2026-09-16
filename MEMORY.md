# UpgradePilot Current Memory

**Last updated:** 2026-09-16  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** complete and prove parser-backed static workflow-command consumer migration before entering runtime-strengthening work.
- **Mode:** Learning-by-Doing — **Cycle 1 CLOSED; Cycle 2 / Phase A COMPLETE; Phase B implementation COMPLETE through B1–B5, but Phase B remains formally IN PROGRESS because executable proof is still pending**.
- **Selected parent plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Selected bounded implementation plan:** `plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`.
- **Accepted method owner:** `docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`.
- **Active working memory:** `working-memory/2026-09-15_cycle2-static-consumer-build.md`.
- **Phase A decision memory:** `working-memory/2026-09-14_static-command-consumer-migration-and-identity.md`.
- **Closed Cycle 1 working memory:** `working-memory/2026-09-13_static-workflow-command-three-cycle-implementation.md`.
- **Repository route:** continue directly on `main` unless Ali later requests otherwise.
- **Learning cadence:** do not teach transitional B1–B5 code piecemeal as final architecture. After executable Phase-B proof is green, perform one integrated implementation-learning session over the stable final consumer migration using the active working-memory learning map and final source/tests.

## Closed foundations retained

- exact run/job attempt coherence is closed and proven;
- bounded static↔runtime correlation is closed and proven within its previous admitted identity boundary;
- exact-revision requirements/constraints provenance is closed and proven;
- static workflow-command architecture/design is closed: ADR-0009 is accepted and the bounded implementation/proof plan exists;
- **Cycle 1 parser/shell/command-analysis foundation is closed and proven at its intended bounded horizon.**

Do not reopen these without concrete contradictory/regression evidence.

## Accepted workflow-command architecture

```text
GitHub Actions RunStepDefinition
+ effective shell context
        ↓
Tree-sitter shell-family parser
        ↓
UpgradePilot-owned static command IR
        ↓
static dependency/project/invocation observers
        ↓
separate conservative runtime-strengthening policy
```

First shell families:

```text
Bash / sh
PowerShell / pwsh
Windows CMD / batch
```

Retained principles:

- parse broadly, claim narrowly;
- syntax family and execution profile are distinct;
- Tree-sitter nodes remain private implementation machinery;
- static occurrence does not prove command execution/success;
- parser uncertainty remains conservative with no regex fallback for positive evidence;
- Python/custom interpreters remain separate language responsibilities.

## Three-cycle implementation structure

### Cycle 1 — parser, shell-context, and shared command-analysis foundation — CLOSED

```text
A — COMPLETE
B — COMPLETE
C — COMPLETE
D — COMPLETE
E — COMPLETE
```

Cycle 1 established:

- characterized parser stack:
  - `tree-sitter==0.25.0`
  - `tree-sitter-bash==0.25.1`
  - `tree-sitter-pwsh==0.38.1`
  - `tree-sitter-batch==0.11.1`;
- provider-owned shell resolution and parser-neutral command analysis;
- `EffectiveShellContext`, `StaticCommandAnalysis`, `StaticCommandOccurrence`, `StaticCommandAtom`, source span/order, and structural context;
- fail-closed behavior on material parse errors;
- no positive regex fallback.

Bounded Cycle-1 proof:

```text
parser characterization RESULT=PASS
python -m pip check → PASS
34 focused + nearest-provider tests → PASS
```

That proof covers the producer/foundation only, not Cycle-2 consumer migration or Cycle-3 runtime strengthening.

### Cycle 2 — static evidence consumer migration and command identity correction — CURRENT / PROOF GATE

Current state:

```text
A — COMPLETE
B — IN PROGRESS
    implementation — COMPLETE through B1+B2+B3+B4+B5
    executable proof — PENDING
C — NOT STARTED formally
D — NOT STARTED
E — NOT STARTED
```

Progressive working-memory preservation has occurred throughout B. Formal Phase C is not entered while the Phase-B executable proof gate remains open.

#### Accepted A1–A6 contract now implemented

```text
A1  one parsed WorkflowDefinition / one CI workflow traversal /
    analyze each RunStepDefinition exactly once

A2  outer identity = workflow path + revision + job key + step_source_index
    inner identity = StaticCommandLocation(source_span, source_order)

A3  segment_index overload removed from final migrated contracts;
    ordering is an explicit CI relation, not an ordinal identity trick

A4  dependency observers consume StaticCommandAnalysis / typed atoms;
    shell parser remains provider-owned

A5  CI package invocation is recognized from real parsed command occurrences

A6  same-step composition uses
    ordered_after | not_after | unresolved
    with parser-neutral structural context
```

Final static consumer shape:

```text
one WorkflowDefinition
        ↓
one CI workflow traversal
        ↓
for each RunStepDefinition:
    analyze_run_step_commands(...) once
        ↓
    same StaticCommandAnalysis reused by:
      direct requirements
      project environment
      package invocation
        ↓
    canonical StaticCommandLocation + structural_context
        ↓
    bounded CI static ordering
```

No migrated consumer reconstructs shell command identity with textual splitting as a positive fallback.

#### B1 — canonical command location + direct-install seam — IMPLEMENTED

Key commits:

```text
a5d372b525ee0e7b2c23bb8e17755fd6a01e2a93
6566de0603c532653040ea42860502aaed044529
527a4c9234607654f8be3da9b672a73758c22c88
```

Established provider-owned `StaticCommandLocation` and parser-neutral direct-install interpretation.

#### B2 — direct requirements + package invocation + static ordering — IMPLEMENTED

```text
328e0b2eee3652e6a552a7b1cfbfda3c46b4c44a
feat: migrate direct CI command evidence to parsed identity
```

Established parsed direct-requirements evidence, parsed package-invocation evidence, structural context, and CI-owned bounded static ordering. The implementation deliberately corrected the old `(step_source_index, segment_index)` coupling instead of fabricating a replacement ordinal.

#### B3 — project-environment selection migration — IMPLEMENTED

```text
7cb7820bf284b3f1fd2a62e0623a23917f9b2790
feat: migrate project environment selection to parsed commands
```

Established:

- parser-backed pip local-project / uv selector interpretation;
- canonical location/structure on project-environment declarations;
- no fabricated inner-command location for step-scoped unresolved evidence;
- shared dependency-owned `pip_command.py` prefix recognition;
- preservation of existing bounded pip/uv semantics without scope expansion.

After B3, project-environment semantics were migrated but the normal application still traversed the workflow twice. That explicit A1 gap became B4.

#### B4 — single production workflow traversal — IMPLEMENTED

```text
069e61c2c65a282ba21472b361035ecbc4223eae
feat: consolidate static workflow evidence traversal
```

Normal investigation now passes exact project-environment **sources** into CI coverage rather than precomputing consumptions in a separate traversal.

`inspect_workflow_dependency_evidence(...)` is the one normal static traversal and reuses one command analysis per run step across all three consumers.

`derive_project_environment_consumptions(...)` remains only as a thin standalone compatibility/test entry over the same internal collector, not a second semantic implementation.

Added `tests/test_single_pass_workflow_static_evidence.py` to protect the one-analysis seam.

#### B5 — remove legacy ordinal compatibility — IMPLEMENTED

Latest code-bearing Phase-B commit:

```text
5d783df4e8ab899178df1597e3554d8c39d42509
refactor: remove legacy static command ordinals
```

Removed from active migrated contracts:

```text
matched_segment_index
ProjectEnvironmentSelectionDeclaration.segment_index
StaticDependencyConsumptionEvidence.segment_index
DirectPackageInvocationEvidence.segment_index
legacy same-step segment ordering
legacy project-environment shell-segment validation
```

Focused precomposed project-environment test evidence remains supported only when it preserves canonical parsed command identity/structure.

B5 also found and repaired one real migration residue: `tests/test_uv_package_scope.py` still used the pre-B3 project-selection API without caller-supplied `StaticCommandAnalysis`.

The first B5 atomic Git-tree attempt failed before `main` moved because one prepared blob SHA was no longer valid. The prepared objects were revalidated/recreated and the complete tree was then committed atomically. No partial product state was published.

The detailed B1–B5 engineering path, failures, rationale, file map, and future learning map are preserved in the active working memory.

## Current executable proof boundary

Phase B cannot be called closed from source inspection alone.

Current evidence:

```text
B1–B5 product source/tests committed
+ connector commit/diff audits complete
+ focused/nearby proof assets written/reconciled
+ final migration-residue audit complete
!= focused tests executed on final implementation
!= nearby tests executed on final implementation
!= full deterministic suite executed on final implementation
```

Final code-bearing commit `5d783df4...` has no GitHub status checks.

`.github/workflows/product-verification.yml` remains intentionally `workflow_dispatch` only. Its configured hosted proof installs the package in a fresh Python 3.12 environment, runs `pip check`, verifies CLI entry points, runs focused investigation tests, then runs the full deterministic unittest suite.

Current GitHub connector capabilities can inspect/rerun existing workflow runs but do not expose creation of a new manual workflow-dispatch run.

A read-only local clone attempt for exact-SHA execution also failed before repository acquisition because this execution runtime could not resolve `github.com`:

```text
Could not resolve host: github.com
```

This is an environment/tooling limitation, not a product test failure. Do not report the new Phase-B tests as passing until they are actually executed.

### Cycle 3 — runtime-strengthening correctness, consolidation, and broad proof — PLANNED / NOT STARTED

```text
static command occurrence
+ structural/control-flow context
+ effective execution profile
+ exact correlated runtime step evidence
→ bounded runtime-strengthening eligibility
```

Cycle 3 must not begin until the Cycle-2 Phase-B proof gate and integrated learning/ownership check are completed.

## Immediate next action

Obtain executable proof for the final Phase-B implementation.

Preferred existing hosted route:

```text
manually dispatch Product verification
→ record exact tested revision/run
→ inspect fresh-environment install + pip check
→ focused investigation composition
→ full deterministic unittest suite
```

If proof fails, diagnose and repair the exact failing B responsibility and preserve that correction before advancing.

If proof is green:

1. record exact run/commands/counts and close Phase B;
2. reconcile formal state preservation;
3. perform Ali's requested integrated B1–B5 implementation-learning session using the active working-memory learning map plus final source/tests;
4. repair any ownership gap exposed by the learning check;
5. only then enter Cycle 3.

## Current stop line

Until Phase B executable proof closes:

- do not start Cycle 3 runtime-strengthening eligibility changes;
- do not treat static source order as execution proof;
- do not expose Tree-sitter nodes as dependency/CI contracts;
- do not broaden pip/uv/package-wrapper semantics merely because typed atoms exist;
- do not reintroduce textual splitters as positive-evidence fallback;
- do not change CI trigger policy merely to manufacture proof without separate authorization;
- do not absorb runtime logs/artifacts, matrix/reusable-workflow execution, exact installed-version/wheel evidence, Target redesign, or maintainer-action enablement.

After all three command-analysis cycles close, re-audit the parent synthesis evidence path and select the next decision-critical bottleneck rather than broadening automatically.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
