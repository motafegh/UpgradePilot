# UpgradePilot Current Memory

**Last updated:** 2026-09-14  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** implement parser-backed static workflow-command semantic correctness and safe runtime strengthening through three bounded Learning-by-Doing cycles.
- **Mode:** Learning-by-Doing — **Cycle 1 / Phases A-B-C-D complete; E closure/orientation is next**.
- **Selected parent plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Selected bounded implementation plan:** `plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`.
- **Accepted method owner:** `docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`.
- **Active working memory:** `working-memory/2026-09-13_static-workflow-command-three-cycle-implementation.md`.
- **Repository route:** continue directly on `main` unless Ali later requests otherwise.

## Closed foundations retained

- exact run/job attempt coherence is closed and proven;
- bounded static↔runtime correlation is closed and proven within its admitted identity boundary;
- exact-revision requirements/constraints provenance is closed and proven;
- static workflow-command architecture/design is closed: ADR-0009 is accepted and the bounded P2 implementation/proof plan exists.

Do not reopen these without contradictory/regression evidence.

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

### Cycle 1 — parser, shell-context, and shared command-analysis foundation — CURRENT

```text
Tree-sitter compatibility/characterization
→ effective shell resolution
→ parser-neutral command IR
→ Bash/PowerShell/CMD adapters
```

Current state:

```text
A — COMPLETE
B — COMPLETE
C — COMPLETE
D — COMPLETE
E — NEXT / NOT STARTED
```

### Cycle 1 B proof

The initial `tree-sitter==0.24.0` trial failed usefully because current grammar wheels use language ABI 15 while runtime 0.24 accepts only ABI 13..14.

The smallest corrected parser stack passed characterization:

```text
tree-sitter==0.25.0
tree-sitter-bash==0.25.1
tree-sitter-pwsh==0.38.1
tree-sitter-batch==0.11.1
```

Observed locally under WSL/Python 3.12:

```text
pip check → No broken requirements found
runtime ABI range = 13..15
bash/powershell/cmd grammar ABI = 15
characterization RESULT=PASS
```

The characterization supports the current normalized propositions: comments/quoted payloads do not manufacture commands, short-circuit/conditional/pipeline syntax remains structurally distinguishable, malformed input reports parser error state, and UTF-8 source spans remain coherent.

The exact characterized stack is the initial product dependency contract.

### Cycle 1 implementation proven at its bounded horizon

Implemented owners:

- `src/upgradepilot/github/workflow_command_shell.py`
- `src/upgradepilot/github/workflow_command_analysis.py`
- exact characterized Tree-sitter dependencies in `pyproject.toml`
- focused proof in `tests/test_github_workflow_command_analysis.py`
- updated runtime-dependency and source-topology tests.

Effective shell precedence includes:

```text
step shell
> job defaults.run.shell
> workflow defaults.run.shell
> job-container default sh when applicable
> safely established hosted platform default
```

On 2026-09-14 Ali synchronized successfully to main and ran the bounded validation set:

```text
python -m pip check
→ No broken requirements found

python -m unittest -v \
  tests.test_github_workflow_command_analysis \
  tests.test_runtime_dependency_contract \
  tests.test_source_topology \
  tests.test_github_workflow_definition
→ Ran 34 tests
→ OK
```

This supersedes the earlier DNS-blocked/stale-checkout attempt. The prior `ModuleNotFoundError` was an environment synchronization artifact, not a product defect.

Cycle 1 B proof establishes the parser/shell/IR foundation at the intended focused + nearest-provider horizon. It does **not** yet prove migrated dependency/CI consumers or runtime strengthening; those belong to Cycles 2 and 3. Broad/full deterministic proof remains planned for the later consolidation horizon rather than being redundantly required here.

### Cycle 1 C — state preservation — COMPLETE

The successful characterization, implementation boundary, 34/34 validation result, proof limits, and next-phase state are preserved in this memory and the active working-memory record.

### Cycle 1 D — ownership/review — COMPLETE

Ownership review established the following mental model:

```text
WorkflowDefinition
→ EffectiveShellContext
→ correct shell-family parser
→ shell-specific CST
→ parser-neutral StaticCommandAnalysis / StaticCommandOccurrence
→ future static consumers
```

Key retained learning:
- `EffectiveShellContext` establishes which shell language actually governs a `run:` block before parser selection; it does not establish command execution.
- syntax family and execution profile remain separate because knowing how to parse a script is weaker than knowing which GitHub wrapper semantics apply.
- `StaticCommandOccurrence` improves over regex segments by preserving real command syntax, source spans/order, executable/argument atoms, and structural context while excluding comments/quoted command-looking payloads structurally.
- short-circuit/conditional/pipeline occurrences may be real static commands without any claim that they executed or succeeded.
- material parser error returns zero admitted occurrences because recovered command-looking syntax is not sufficient evidence for positive product claims.
- source span/order is static occurrence identity only, not runtime execution or same-path proof.

Ali's ownership check passed. No implementation defect or ownership gap was exposed, so no return to B is justified.

No Cycle 2 consumer migration has started.

### Cycle 2 — static evidence consumer migration and command identity correction — PLANNED

```text
shared command-analysis producer
→ direct requirements
→ project-environment selection
→ CI direct package invocation/composition
→ segment_index/source-order reconciliation
→ same-step static ordering correction
```

Cycle 2 should begin only after Cycle 1 E formally closes this foundation and orients the local Cycle 2 A questions.

### Cycle 3 — runtime-strengthening correctness, consolidation, and broad proof — PLANNED

```text
static command occurrence
+ structural/control-flow context
+ effective execution profile
+ exact correlated runtime step evidence
→ bounded runtime-strengthening eligibility
```

Begins only after Cycle 2 reaches E.

## Immediate next action

Enter **Cycle 1 Phase E — gap repair + closure + Cycle 2 orientation**.

E should confirm that no Cycle 1 defect remains, close Cycle 1 at its bounded proof horizon, and identify the smallest local questions Cycle 2 A must answer before implementation. Do not begin Cycle 2 source migration during Cycle 1 E.

## Current stop line

Until Cycle 1 E closes, do not migrate direct requirements, project-environment selection, CI command identity/`segment_index`, or runtime-strengthening behavior; do not expose Tree-sitter nodes as product contracts; do not fall back to old regex splitters for positive evidence; and do not absorb unrelated evidence/action expansion.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
