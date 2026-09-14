# UpgradePilot Current Memory

**Last updated:** 2026-09-14  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** implement parser-backed static workflow-command semantic correctness and safe runtime strengthening through three bounded Learning-by-Doing cycles.
- **Mode:** Learning-by-Doing — **Cycle 1 / Phase B Build in progress**.
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
B — IN PROGRESS
    parser/grammar characterization ✅
    foundation implementation ✅
    synchronized focused/nearby validation ← BLOCKED BY TEMPORARY DNS/PULL FAILURE
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

### Cycle 1 B evidence

The initial `tree-sitter==0.24.0` trial failed because current grammar wheels use language ABI 15 while runtime 0.24 accepts only ABI 13..14.

The smallest corrected trial passed:

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

The exact characterized stack is now the initial product dependency contract.

### Cycle 1 B implementation present

- `src/upgradepilot/github/workflow_command_shell.py`
- `src/upgradepilot/github/workflow_command_analysis.py`
- exact characterized Tree-sitter dependencies in `pyproject.toml`
- focused proof in `tests/test_github_workflow_command_analysis.py`
- updated runtime-dependency and source-topology tests.

Important shell precedence includes:

```text
step shell
> job defaults.run.shell
> workflow defaults.run.shell
> job-container default sh when applicable
> safely established hosted platform default
```

No Cycle 2 consumer migration has started.

### Current blocker — 2026-09-14 local validation attempt

The requested local validation began with:

```text
git pull origin main
```

but failed with:

```text
Could not resolve host: github.com
```

Therefore the local checkout stayed on the older revision and did not receive the new foundation implementation/test files.

What is valid from that attempt:

```text
pip check → PASS
retained parser characterization → RESULT=PASS
```

What is **not** a product regression:

```text
ModuleNotFoundError: tests.test_github_workflow_command_analysis
```

The new test module was absent only because the pull failed. Existing selected tests ran on the stale checkout and passed, but they do not prove the new implementation.

Classification:

```text
TEMPORARY ENVIRONMENT/SYNCHRONIZATION BLOCKER
not a parser failure
not a foundation regression
```

## Immediate next action

When GitHub/DNS access is available:

```text
git pull origin main
verify the pull succeeds
pip check
python -m unittest -v \
  tests.test_github_workflow_command_analysis \
  tests.test_runtime_dependency_contract \
  tests.test_source_topology \
  tests.test_github_workflow_definition
```

The retained characterization does not need another diagnostic investigation unless it changes; it has already passed on the exact parser stack. If the synchronized focused/nearby tests pass, preserve B proof and advance to Cycle 1 C. If they reveal implementation defects, repair inside B.

### Cycle 2 — static evidence consumer migration and command identity correction — PLANNED

Begins only after Cycle 1 reaches E.

### Cycle 3 — runtime-strengthening correctness, consolidation, and broad proof — PLANNED

Begins only after Cycle 2 reaches E.

## Current stop line

During Cycle 1 B do not migrate direct requirements, project-environment selection, CI command identity/`segment_index`, or runtime-strengthening behavior; do not expose Tree-sitter nodes as product contracts; do not fall back to old regex splitters for positive evidence; and do not absorb unrelated evidence/action expansion.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
