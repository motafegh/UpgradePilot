# UpgradePilot Current Memory

**Last updated:** 2026-09-14  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** implement parser-backed static workflow-command semantic correctness and safe runtime strengthening through three bounded Learning-by-Doing cycles.
- **Mode:** Learning-by-Doing — **Cycle 1 CLOSED; Cycle 2 / Phase A is next and not yet started**.
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

### Cycle 2 — static evidence consumer migration and command identity correction — CURRENT / A NEXT

```text
shared command-analysis producer
→ direct requirements observation
→ project-environment selection
→ CI direct package invocation/composition
→ segment_index / occurrence-identity reconciliation
→ bounded same-step static ordering correction
```

Current state:

```text
A — NEXT / NOT STARTED
B — NOT STARTED
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

Cycle 2 A remains read-only with respect to product source/tests.

#### Current migration pressure

`dependency/direct_install.py` still uses `bounded_shell_segments(...)`, regex command recognition, and `matched_segment_index`.

`dependency/environment_selection.py` still uses textual segmentation plus its own regex/`shlex` parsing and stores `segment_index` in project-environment declarations.

`ci/workflow_commands.py` still has a second `_shell_segments(...)`, scans fragments for direct package invocation, validates project-environment evidence by re-splitting raw command text, and carries `segment_index` into CI evidence.

`ci/consumption.py` exposes `segment_index` in `StaticDependencyConsumptionEvidence`, so command-location migration is cross-layer rather than a private-helper replacement.

#### Exact Cycle 2 A questions

Before Build, resolve:

1. **Single analysis handoff seam:** where one run step is analyzed exactly once and how `StaticCommandAnalysis` / occurrences are passed to dependency observers.
2. **Canonical static command identity:** likely workflow/revision/job/step outer identity plus occurrence source span/order; decide whether to introduce a dedicated value object or store fields directly.
3. **`segment_index` reconciliation:** classify every remaining use as replace, retain only as derived source-order ordinal, or remove.
4. **Dependency observer interpretation:** map literal/dynamic/unsupported command atoms into existing direct-install and project-environment semantics without moving pip/uv meaning into the GitHub layer.
5. **Direct package invocation:** recognize admitted invocation prefixes from parsed atoms while keeping package meaning in CI.
6. **Same-step static ordering:** preserve only ordering claims justified by static structure; source order must not become same-path execution proof.

Important Cycle 2 distinction:

```text
conditional/short-circuit command may still be a real static declaration
!= eligible for runtime strengthening
```

Static declaration semantics belong to Cycle 2; runtime-strengthening eligibility remains Cycle 3.

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

Enter **Cycle 2 Phase A — read-only migration/identity orientation** using the active working memory.

Inspect the exact current callers/tests and resolve only the local handoff, identity, unresolved-state, and same-step ordering decisions necessary before Build. Do not start source migration until Cycle 2 A is complete and Build is explicitly entered.

## Current stop line

During Cycle 2 A do not:

- modify direct-install/project-environment/CI command consumer source or tests;
- remove existing splitters yet;
- change runtime-strengthening/static↔runtime correlation policy;
- treat source order as execution-path proof;
- expose Tree-sitter nodes as dependency/CI contracts;
- absorb runtime logs/artifacts, matrix/reusable-workflow execution, exact installed-version/wheel evidence, Target redesign, or maintainer-action enablement.

After all three static-command cycles close, re-audit the parent synthesis evidence path and select the next decision-critical bottleneck rather than broadening automatically.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`
