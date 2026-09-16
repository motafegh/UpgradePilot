# UpgradePilot Current Memory

**Last updated:** 2026-09-16  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** perform the integrated Cycle-2 Phase-B implementation-learning / ownership check over the now-stable parser-backed static workflow-command consumer architecture before entering runtime-strengthening work.
- **Mode:** Learning-by-Doing — **Cycle 1 CLOSED; Cycle 2 Phase A COMPLETE; Cycle 2 Phase B CLOSED with hosted executable proof green; Cycle 3 NOT STARTED**.
- **Selected parent plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Selected bounded implementation plan:** `plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`.
- **Accepted method owner:** `docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`.
- **Active working memory / proof closure:** `working-memory/2026-09-16_cycle2-phase-b-hosted-proof-closure.md`.
- **Phase-B engineering / learning map:** `working-memory/2026-09-15_cycle2-static-consumer-build.md`.
- **Hosted proof-repair records:** `working-memory/2026-09-16_phase-b-hosted-proof-repair.md` and `working-memory/2026-09-16_phase-b-hosted-proof-repair-3.md`.
- **Phase A decision memory:** `working-memory/2026-09-14_static-command-consumer-migration-and-identity.md`.
- **Closed Cycle 1 working memory:** `working-memory/2026-09-13_static-workflow-command-three-cycle-implementation.md`.
- **Repository route:** continue directly on `main` unless Ali later requests otherwise.
- **Learning cadence:** Phase B is now stable and proven. Perform one integrated implementation-learning session over the final B1–B5 architecture using the engineering record plus final source/tests; repair any real ownership gap before selecting/starting Cycle 3.

## Closed foundations retained

The following are closed at their accepted horizons and must not be reopened without concrete contradictory/regression evidence:

- exact run/job attempt coherence;
- bounded static↔runtime correlation within its previous admitted identity boundary;
- exact-revision requirements/constraints provenance;
- ADR-0009 static workflow-command architecture/design;
- **Cycle 1 parser/shell/command-analysis foundation**;
- **Cycle 2 Phase B static evidence consumer migration and command-identity correction**.

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

First admitted shell families:

```text
Bash / sh
PowerShell / pwsh
Windows CMD / batch
```

Retained principles:

- parse broadly, claim narrowly;
- syntax family and execution profile are distinct;
- Tree-sitter nodes remain private implementation machinery;
- static occurrence does not prove command execution or success;
- parser uncertainty remains conservative with no regex/text-splitter fallback for positive evidence;
- Python/custom interpreters remain separate language responsibilities.

## Cycle 1 — parser, shell-context, and shared command-analysis foundation — CLOSED

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

That proof covers the producer/foundation only; Cycle 2 has its own proof below.

## Cycle 2 — static evidence consumer migration and command identity correction — PHASE B CLOSED

### Accepted A1–A6 contract — IMPLEMENTED

```text
A1  one parsed WorkflowDefinition / one normal CI workflow traversal /
    analyze each RunStepDefinition exactly once

A2  outer identity = workflow path + revision + job key + step_source_index
    inner identity = StaticCommandLocation(source_span, source_order)

A3  segment_index overload removed from final migrated contracts;
    ordering is an explicit CI relation, not an ordinal identity trick

A4  dependency observers consume StaticCommandAnalysis / typed atoms;
    shell parsing remains provider-owned

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

### B1 — canonical command location + direct-install seam — COMPLETE

Key commits:

```text
a5d372b525ee0e7b2c23bb8e17755fd6a01e2a93
6566de0603c532653040ea42860502aaed044529
527a4c9234607654f8be3da9b672a73758c22c88
```

Established provider-owned `StaticCommandLocation` and parser-neutral direct-install interpretation.

### B2 — direct requirements + package invocation + static ordering — COMPLETE

```text
328e0b2eee3652e6a552a7b1cfbfda3c46b4c44a
feat: migrate direct CI command evidence to parsed identity
```

Established parsed direct-requirements evidence, parsed package-invocation evidence, structural context, and CI-owned bounded static ordering. The old `(step_source_index, segment_index)` coupling was corrected rather than replaced with another fabricated ordinal.

### B3 — project-environment selection migration — COMPLETE

```text
7cb7820bf284b3f1fd2a62e0623a23917f9b2790
feat: migrate project environment selection to parsed commands
```

Established parser-backed pip local-project / uv selector interpretation, canonical command location/structure, shared dependency-owned pip-prefix recognition, and no fabricated inner-command identity for step-scoped unresolved evidence.

### B4 — single production workflow traversal — COMPLETE

```text
069e61c2c65a282ba21472b361035ecbc4223eae
feat: consolidate static workflow evidence traversal
```

Normal investigation passes exact project-environment **sources** into CI coverage. `inspect_workflow_dependency_evidence(...)` owns the one normal static traversal and reuses one command analysis per run step across direct requirements, project environment, and package invocation.

`derive_project_environment_consumptions(...)` remains only as a thin standalone compatibility/test entry over the same internal collector, not a second semantic implementation.

### B5 — remove legacy ordinal compatibility — COMPLETE

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

Focused precomposed project-environment test evidence is admitted only when it preserves canonical parsed command identity/structure.

Detailed B1–B5 implementation pressure, discoveries, failures, rationale, file map, and learning map remain in `working-memory/2026-09-15_cycle2-static-consumer-build.md`.

## Phase B hosted executable proof — CLOSED / PASS

Authoritative hosted proof:

```text
workflow: Product verification
run id: 35108271298
run attempt: 1
event: workflow_dispatch
head branch: main
tested revision: ee93143b58c3cf0dbb191c543ef4a66a437d0aec
job id: 104835021439
result: SUCCESS
```

Verified proof layers:

```text
checkout exact selected revision                 PASS
CPython 3.12.14 setup                            PASS
fresh virtual environment + pip install .        PASS
python -m pip check                              PASS — no broken requirements
installed CLI entry point checks                 PASS
focused investigation composition               PASS — 15/15
full deterministic product regression            PASS — 587/587
```

The full suite finished:

```text
Ran 587 tests in 0.293s
OK
```

The fresh environment also installed the characterized Tree-sitter stack exactly:

```text
tree-sitter==0.25.0
tree-sitter-bash==0.25.1
tree-sitter-batch==0.11.1
tree-sitter-pwsh==0.38.1
```

The hosted proof gate exposed and repaired several bounded migration residues before closure. The detailed sequence is preserved in the two hosted proof-repair working memories and summarized in the Phase-B proof-closure memory.

Important retained lessons:

- a strict internal evidence-contract migration must update secondary downstream consumers as well as the primary path;
- removing an obsolete identity field can leave stale test fixtures after production contracts are already clean;
- parser-backed architecture may move uncertainty to an earlier trustworthy owner without changing the final conservative proposition;
- step-scoped unresolved evidence does not imply exact inner-command identity;
- the B4 single-traversal architecture prevents semantic command identity from being detached and later guessed/rebound;
- proof failures must be classified before repair rather than reflexively weakening product boundaries.

Phase B is therefore closed at its intended implementation/proof horizon.

## Current learning / ownership check — NEXT

Before Cycle 3, perform Ali's agreed integrated B1–B5 implementation-learning session over the stable proven source.

Primary trace:

```text
workflow run step
→ effective shell resolution
→ StaticCommandAnalysis
→ StaticCommandOccurrence
→ StaticCommandLocation
→ direct requirements interpretation
→ project-environment interpretation
→ package invocation
→ CI evidence composition
→ bounded static ordering
```

Use one or two real UpgradePilot/product-simulation cases end-to-end and explicitly distinguish:

```text
what existed before
→ what was wrong or overloaded
→ what B changed
→ why each boundary exists
→ what final implementation guarantees
→ what it deliberately does NOT guarantee
```

If the ownership check exposes a real understanding or implementation gap, repair only that bounded gap and preserve it before advancing.

## Cycle 3 — runtime-strengthening correctness, consolidation, and broad proof — PLANNED / NOT STARTED

Planned responsibility:

```text
static command occurrence
+ structural/control-flow context
+ effective execution profile
+ exact correlated runtime step evidence
→ bounded runtime-strengthening eligibility
```

Cycle 3 must not begin until the integrated Phase-B learning/ownership check is completed and any gap exposed by it is repaired.

## Immediate next action

Perform the integrated Phase-B implementation-learning / ownership check using:

- `working-memory/2026-09-15_cycle2-static-consumer-build.md` for the B1–B5 engineering journey;
- `working-memory/2026-09-16_phase-b-hosted-proof-repair.md` and `working-memory/2026-09-16_phase-b-hosted-proof-repair-3.md` for proof-driven corrections;
- `working-memory/2026-09-16_cycle2-phase-b-hosted-proof-closure.md` for final executable proof;
- the final source/tests as the stable implementation authority.

Do not treat transitional B1–B4 states as the final architecture during teaching.

## Current stop line

Until the integrated Phase-B learning/ownership check closes:

- do not start Cycle 3 runtime-strengthening eligibility changes;
- do not treat static source order as execution proof;
- do not expose Tree-sitter nodes as dependency/CI contracts;
- do not broaden pip/uv/package-wrapper semantics merely because typed atoms exist;
- do not reintroduce textual splitters as positive-evidence fallback;
- do not absorb runtime logs/artifacts, matrix/reusable-workflow execution, exact installed-version/wheel evidence, Target redesign, or maintainer-action enablement.

After all three command-analysis cycles close, re-audit the parent synthesis evidence path and select the next decision-critical bottleneck rather than broadening automatically.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
