# UpgradePilot Current Memory

**Last updated:** 2026-09-14  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** implement parser-backed static workflow-command semantic correctness and safe runtime strengthening through three bounded Learning-by-Doing cycles.
- **Mode:** Learning-by-Doing — **Cycle 1 CLOSED; Cycle 2 / Phase A COMPLETE; Phase B is next and not yet started**.
- **Selected parent plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Selected bounded implementation plan:** `plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`.
- **Accepted method owner:** `docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`.
- **Active working memory:** `working-memory/2026-09-14_static-command-consumer-migration-and-identity.md`.
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

### Cycle 2 — static evidence consumer migration and command identity correction — CURRENT / B NEXT

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
B — NEXT / NOT STARTED
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

Use a small provider-owned parser-neutral command-location value object conceptually; neither identity level is runtime execution proof.

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

#### Current Build pressure

`dependency/direct_install.py` still uses `bounded_shell_segments(...)`, regex command recognition, and `matched_segment_index`.

`dependency/environment_selection.py` still uses textual segmentation plus regex/`shlex` parsing and stores `segment_index`.

`ci/workflow_commands.py` still has a second `_shell_segments(...)`, fragment-based direct package invocation, raw-command revalidation, and segment-index composition.

`ci/consumption.py` still exposes `segment_index`, and `ci/dependency_exercise.py` still performs tuple ordering.

These are now bounded Build targets under the accepted A1–A6 contract.

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

Enter **Cycle 2 Phase B — bounded consumer migration Build** using the accepted A1–A6 contract in the active working memory.

Start from the smallest dependency-facing implementation seam needed to introduce canonical command location / typed-analysis input, then migrate direct requirements and project-environment observers before consolidating CI composition. Validate narrowly after each meaningful increment and preserve Cycle 2 state before expanding.

## Current stop line

During Cycle 2 B:

- implement only the accepted A1–A6 migration responsibility;
- do not change Cycle 3 runtime-strengthening/static↔runtime correlation policy;
- do not treat static source order as execution proof;
- do not expose Tree-sitter nodes as dependency/CI contracts;
- do not keep old textual splitters as positive-evidence fallback after a consumer is migrated;
- do not absorb runtime logs/artifacts, matrix/reusable-workflow execution, exact installed-version/wheel evidence, Target redesign, or maintainer-action enablement;
- if Build exposes a real insufficiency in the Cycle 1 IR or accepted Phase A contract, stop that slice and return the exact gap to design rather than extending semantics ad hoc.

After all three static-command cycles close, re-audit the parent synthesis evidence path and select the next decision-critical bottleneck rather than broadening automatically.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`
