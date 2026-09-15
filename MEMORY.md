# UpgradePilot Current Memory

**Last updated:** 2026-09-15  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** implement parser-backed static workflow-command semantic correctness and safe runtime strengthening through three bounded Learning-by-Doing cycles.
- **Mode:** Learning-by-Doing — **Cycle 1 CLOSED; Cycle 2 / Phase A COMPLETE; Phase B IN PROGRESS; B1+B2 implemented, executable proof still pending; B3 next**.
- **Selected parent plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Selected bounded implementation plan:** `plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`.
- **Accepted method owner:** `docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`.
- **Active working memory:** `working-memory/2026-09-15_cycle2-static-consumer-build.md`.
- **Phase A decision memory:** `working-memory/2026-09-14_static-command-consumer-migration-and-identity.md`.
- **Closed Cycle 1 working memory:** `working-memory/2026-09-13_static-workflow-command-three-cycle-implementation.md`.
- **Repository route:** continue directly on `main` unless Ali later requests otherwise.
- **Learning cadence for Phase B:** brief ownership checkpoints during implementation; after B is fully implemented and validated, perform one integrated learning session over the stable final implementation.

## Closed foundations retained

- exact run/job attempt coherence is closed and proven;
- bounded static↔runtime correlation is closed and proven within its admitted identity boundary;
- exact-revision requirements/constraints provenance is closed and proven;
- static workflow-command architecture/design is closed: ADR-0009 is accepted and the bounded P2 implementation/proof plan exists;
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

- exact characterized parser stack:
  - `tree-sitter==0.25.0`
  - `tree-sitter-bash==0.25.1`
  - `tree-sitter-pwsh==0.38.1`
  - `tree-sitter-batch==0.11.1`;
- provider-owned `workflow_command_shell.py`;
- parser-neutral `workflow_command_analysis.py`;
- `EffectiveShellContext`, `StaticCommandAnalysis`, `StaticCommandOccurrence`, `StaticCommandAtom`, and source-span/order identity;
- structural distinction for straightforward/linear/short-circuit/conditional/loop/pipeline/nested forms;
- broad fail-closed behavior on material parse errors;
- no positive regex fallback.

Bounded proof:

```text
parser characterization RESULT=PASS
python -m pip check → PASS
34 focused + nearest-provider tests → PASS
```

The 34-test proof establishes the producer/foundation only. It does not prove consumer migration, runtime strengthening, or the final full deterministic repository horizon.

### Cycle 2 — static evidence consumer migration and command identity correction — CURRENT / B IN PROGRESS

```text
shared command-analysis producer
→ direct requirements observation
→ project-environment selection
→ CI direct package invocation/composition
→ canonical occurrence identity
→ bounded static ordering relation
```

Current state:

```text
A — COMPLETE
B — IN PROGRESS
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

#### Phase A accepted migration contract

A1 — **single analysis seam**

```text
one parsed WorkflowDefinition
→ one CI workflow traversal
→ analyze each RunStepDefinition exactly once
→ reuse StaticCommandAnalysis / occurrences downstream
```

GitHub owns shell syntax/IR; dependency owns pip/uv meaning; CI owns workflow traversal, package invocation, checkout provenance, and cross-evidence composition.

A2 — **canonical command identity**

```text
outer: workflow path + revision + job key + step_source_index
inner: command source span + deterministic source_order
```

Use provider-owned parser-neutral `StaticCommandLocation`; neither identity level is runtime execution proof.

A3 — **remove `segment_index` overload**

```text
identity → canonical command occurrence location
ordering → explicit bounded CI ordering relation
placeholder / ordinal-bounds validation → remove
```

Do not fabricate command location `0` for step-scoped unresolved evidence.

A4 — **dependency observers consume typed atoms**

- pass `StaticCommandAnalysis` into dependency observers;
- interpret literal executable/argument atoms directly;
- material dynamic/unsupported pip/uv tokens remain unresolved;
- unrelated uncertainty does not erase an established positive static declaration;
- do not reparse raw command text with shell splitting/`shlex` as the command-identity source;
- real conditional/short-circuit/etc. occurrences may remain static declarations; execution eligibility is separate.

A5 — **CI package invocation from parsed occurrences**

Preserve the currently admitted direct/wrapper shapes from typed atoms:

```text
<package>
python/python3 -m <package>
uv run <package>
poetry run <package>
pipenv run <package>
coverage run -m <package>
```

Material uncertainty in a recognized wrapper/target position remains explicit rather than becoming absence.

A6 — **bounded static ordering**

Use a CI-owned relation:

```text
ordered_after | not_after | unresolved
```

- different user-defined steps retain admitted `step_source_index` static ordering;
- same-step positive ordering requires distinct occurrences, increasing source order, and clean top-level/linear structure;
- short-circuit/conditional/loop/pipeline/function/nested relations do not earn same-step ordering merely from source order;
- same occurrence is not strictly “after” itself;
- this remains static ordering only, not execution/success proof.

#### Phase B B1 — command location + dependency observer seam — IMPLEMENTED

B1 added `StaticCommandLocation(source_span, source_order)` and changed the direct-install observer to consume `StaticCommandAnalysis` / typed atoms. Focused direct-install tests were rewritten around parser-neutral analysis fixtures.

B1 implementation/test commits:

```text
a5d372b525ee0e7b2c23bb8e17755fd6a01e2a93
6566de0603c532653040ea42860502aaed044529
527a4c9234607654f8be3da9b672a73758c22c88
```

#### Phase B B2 — production direct-requirements + parsed invocation/order seam — IMPLEMENTED

Commit:

```text
328e0b2eee3652e6a552a7b1cfbfda3c46b4c44a
feat: migrate direct CI command evidence to parsed identity
```

B2 established:

```text
one StaticCommandAnalysis per run step in normal CI traversal
→ direct requirements interpretation
→ direct package invocation interpretation
→ exact StaticCommandLocation + structural context
→ explicit CI static-order relation
```

Key current facts:

- production direct requirements now receive shared `StaticCommandAnalysis`;
- `dependency/direct_install.py` no longer has the B1 regex/text-split compatibility route;
- migrated direct-requirements evidence carries `command_location` and does not fabricate `segment_index=0`;
- direct package invocation is recognized from typed parsed occurrences, preserving only accepted wrapper shapes;
- dynamic/unsupported material invocation targets are retained as typed unresolved candidates;
- added `ci/static_command_order.py` with `ordered_after | not_after | unresolved`;
- same-step short-circuit/conditional/loop/pipeline/function/nested source order cannot become direct-exercise support;
- runtime correlation remains job/step scoped and unchanged; Cycle 3 policy has not started;
- existing synthetic CI tests now explicitly establish Bash where their responsibility is CI composition rather than shell selection.

B2 focused/integration proof assets:

```text
tests/test_static_command_order.py
tests/test_parser_backed_ci_command_evidence.py
tests/test_ci_static_direct_exercise_order.py
tests/test_workflow_dependency_evidence.py  (reconciled)
tests/test_ci_dependency_coverage.py        (reconciled)
```

Current proof boundary remains deliberately limited:

```text
B1+B2 implementation committed
+ source/diff audit complete
+ focused/integration tests written/reconciled
+ source strings syntax-checked during Build preparation
!= repository tests executed
!= hosted verification run executed
```

GitHub Actions shows zero workflow runs for B2 commit `328e0b2...`. The repository verification workflow is `workflow_dispatch` only, so no push-triggered proof exists. Do not report the new tests as passing yet.

#### Remaining Phase B migration pressure

Still legacy / next target:

`dependency/environment_selection.py` still uses textual segmentation plus regex/`shlex` and stores `segment_index`.

`derive_project_environment_consumptions(...)` still parses/walks the workflow separately from the normal CI evidence pass.

Project-environment CI evidence/validation still uses the temporary legacy segment identity. The only remaining textual command splitter in `ci/workflow_commands.py` is explicitly scoped to this unmigrated project-environment validation path.

`StaticDependencyConsumptionEvidence` is intentionally transitional during B:

```text
direct_requirements → command_location + structural_context; segment_index None
project_environment → legacy segment_index until B3
```

This duality is not the final architecture.

### Cycle 3 — runtime-strengthening correctness, consolidation, and broad proof — PLANNED

```text
static command occurrence
+ structural/control-flow context
+ effective execution profile
+ exact correlated runtime step evidence
→ bounded runtime-strengthening eligibility
```

Cycle 3 owns runtime-strengthening policy and final focused → nearby → full deterministic proof after Cycle 2 closes.

## Immediate next action

Continue **Cycle 2 Phase B — B3 project-environment migration**.

Exact target:

```text
same RunStepDefinition + shared StaticCommandAnalysis
+ project path / working-directory context
→ dependency-owned pip/uv project-environment interpretation
→ canonical command occurrence location
→ CI project-environment composition/validation from that exact occurrence
```

B3 should:

- migrate `ProjectEnvironmentSelectionDeclaration.segment_index` to command location;
- consume typed command atoms rather than textual segmentation/`shlex`;
- preserve current bounded pip/uv selectors/package-scope semantics without broadening them;
- remove fabricated project-environment locations for step-scoped unresolved states;
- remove the remaining legacy project-environment splitter/segment validation once unused;
- move toward the accepted one-workflow-traversal / one-analysis-per-run-step shape rather than keeping the current separate parse/walk as final architecture.

After project-environment migration, reconcile the remaining workflow-level traversal/composition seam and obtain executable focused/nearby proof before Phase B is declared complete.

## Current stop line

During Cycle 2 B:

- implement only accepted A1–A6 migration responsibility;
- do not change Cycle 3 runtime-strengthening/static↔runtime correlation policy;
- do not treat static source order as execution proof;
- do not expose Tree-sitter nodes as dependency/CI contracts;
- do not broaden current pip/uv/package-wrapper semantics merely because typed atoms now exist;
- do not keep textual splitters as positive-evidence fallback after their consumer is migrated;
- do not absorb runtime logs/artifacts, matrix/reusable-workflow execution, exact installed-version/wheel evidence, Target redesign, or maintainer-action enablement;
- if Build exposes a real insufficiency in Cycle 1 IR or the accepted A1–A6 contract, stop that slice and return the exact gap to design rather than extending semantics ad hoc.

After all three static-command cycles close, re-audit the parent synthesis evidence path and select the next decision-critical bottleneck rather than broadening automatically.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
