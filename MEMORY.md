# UpgradePilot Current Memory

**Last updated:** 2026-09-15  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** implement parser-backed static workflow-command semantic correctness and safe runtime strengthening through three bounded Learning-by-Doing cycles.
- **Mode:** Learning-by-Doing — **Cycle 1 CLOSED; Cycle 2 / Phase A COMPLETE; Phase B IN PROGRESS; B1 implemented, execution proof pending**.
- **Selected parent plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Selected bounded implementation plan:** `plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`.
- **Accepted method owner:** `docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`.
- **Active working memory:** `working-memory/2026-09-15_cycle2-static-consumer-build.md`.
- **Phase A decision memory:** `working-memory/2026-09-14_static-command-consumer-migration-and-identity.md`.
- **Closed Cycle 1 working memory:** `working-memory/2026-09-13_static-workflow-command-three-cycle-implementation.md`.
- **Repository route:** continue directly on `main` unless Ali later requests otherwise.

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

Cycle 1 D ownership review passed. Cycle 1 E found no unresolved repair item; remaining old textual splitters are Cycle 2 migration targets, not Cycle 1 defects.

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

Use a small provider-owned parser-neutral command-location value object; neither identity level is runtime execution proof.

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

Do not broaden into a general wrapper CLI parser during this migration. Material uncertainty in a recognized wrapper/target position must remain explicit rather than becoming absence.

A6 — **bounded static ordering**

Use a CI-owned relation conceptually:

```text
ordered_after | not_after | unresolved
```

- different user-defined steps retain admitted `step_source_index` static ordering;
- same-step positive ordering requires distinct occurrences, increasing source order, and clean top-level linear-chain structure;
- short-circuit/conditional/loop/pipeline/function/nested relations do not earn same-step ordering merely from source order;
- same occurrence is not strictly “after” itself;
- this remains static ordering only, not execution/success proof.

No broader command IR or ADR reassessment was required by Phase A.

#### Phase B B1 — implemented, proof not yet executed

B1 established the first new seam:

- added provider-owned `src/upgradepilot/github/workflow_command_location.py` with `StaticCommandLocation(source_span, source_order)` derived from `StaticCommandOccurrence`;
- updated `dependency/direct_install.py` so a parser-backed caller can supply `StaticCommandAnalysis`;
- the parser-backed observer interprets typed executable/argument atoms directly, preserves material uncertainty, and carries exact `command_location` when a specific occurrence exists;
- focused direct-install tests were rewritten to inject parser-neutral analyses rather than own shell parsing;
- tests cover ordinary positive paths, working-directory/path semantics, quoted-text rejection, dynamic/unresolved cases, static presence under short-circuit structure, command location, positive-fact survival under unrelated dynamic arguments, and parser-failure no-fallback behavior.

B1 commits:

```text
a5d372b525ee0e7b2c23bb8e17755fd6a01e2a93  feat: add static command location identity
6566de0603c532653040ea42860502aaed044529  feat: consume parsed command analysis for direct installs
527a4c9234607654f8be3da9b672a73758c22c88  test: prove parser-backed direct install observation
c6006285e5860809d798a3177a9c4c6a9424cd49  docs: preserve cycle 2 build slice one
```

Proof boundary:

```text
implementation committed
+ focused tests written/reconciled
+ connector source/diff inspection
!= focused tests executed
!= nearby integration proof
!= production direct-requirements migration complete
```

GitHub reports no combined status checks and no workflow runs for the B1 test commit, so do not report the new tests as passing yet.

#### Current migration pressure

The normal production direct-requirements caller in `ci/workflow_commands.py` still does not supply `StaticCommandAnalysis`, so it intentionally reaches the temporary legacy route in `direct_install.py`.

`matched_segment_index` remains transitional only for that unmigrated path; parser-backed observations use `command_location` and leave the old ordinal unset.

`dependency/environment_selection.py` still uses textual segmentation plus regex/`shlex` parsing and stores `segment_index`.

`ci/workflow_commands.py` still has a second `_shell_segments(...)`, fragment-based direct package invocation, raw-command revalidation, and segment-index composition.

`ci/consumption.py` still exposes `segment_index`, and `ci/dependency_exercise.py` still performs tuple ordering.

These remain bounded Phase B migration targets.

### Cycle 3 — runtime-strengthening correctness, consolidation, and broad proof — PLANNED

```text
static command occurrence
+ structural/control-flow context
+ effective execution profile
+ exact correlated runtime step evidence
→ bounded runtime-strengthening eligibility
```

Cycle 3 owns runtime-strengthening policy, final obsolete-path removal if any remains, and focused → nearby → full deterministic proof.

## Immediate next action

Continue **Cycle 2 Phase B — B2 direct-requirements production handoff**.

Exact next slice:

```text
ci/workflow_commands.py
→ analyze each relevant RunStepDefinition once
→ pass the shared StaticCommandAnalysis to direct-install interpretation
→ carry canonical command location into CI consumption evidence
→ remove direct-requirements segment-index placeholders/identity
→ remove the temporary direct-install legacy route when no production caller needs it
```

Preserve checkout-provenance semantics. If `StaticDependencyConsumptionEvidence` must change, reconcile only the location contract needed by this slice and keep project-environment migration explicit.

Obtain the narrowest executable proof available before expanding to project-environment selection.

## Current stop line

During Cycle 2 B:

- implement only the accepted A1–A6 migration responsibility;
- do not change Cycle 3 runtime-strengthening/static↔runtime correlation policy;
- do not treat static source order as execution proof;
- do not expose Tree-sitter nodes as dependency/CI contracts;
- do not keep old textual splitters as positive-evidence fallback after a consumer is actually migrated;
- do not absorb runtime logs/artifacts, matrix/reusable-workflow execution, exact installed-version/wheel evidence, Target redesign, or maintainer-action enablement;
- if Build exposes a real insufficiency in the Cycle 1 IR or accepted Phase A contract, stop that slice and return the exact gap to design rather than extending semantics ad hoc.

After all three static-command cycles close, re-audit the parent synthesis evidence path and select the next decision-critical bottleneck rather than broadening automatically.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
