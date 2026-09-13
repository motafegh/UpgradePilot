# UpgradePilot Current Memory

**Last updated:** 2026-09-13  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** implement parser-backed static workflow-command semantic correctness and safe runtime strengthening through three bounded Learning-by-Doing cycles.
- **Mode:** Learning-by-Doing — **Cycle 1 / Phase B Build in progress**.
- **Selected parent plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Selected bounded implementation plan:** `plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`.
- **Accepted method owner:** `docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`.
- **Active working memory:** `working-memory/2026-09-13_static-workflow-command-three-cycle-implementation.md`.
- **Previous design/planning working memory:** `working-memory/2026-09-13_static-shell-direct-install-false-positive-recognition.md`.
- **Repository route:** continue directly on `main` unless Ali later requests otherwise.

The parent synthesis journey still prioritizes correctness/provenance reinforcement before broader evidence production or non-abstention maintainer-action expansion.

## Closed foundations retained

- exact run/job attempt coherence is closed and proven;
- bounded static↔runtime correlation is closed and proven within its admitted identity boundary;
- exact-revision requirements/constraints changed-file provenance is closed and proven, with the previous validation horizon of 13 focused + 15 nearby + 566 full deterministic tests green;
- the static workflow-command architecture/design phase is closed: ADR-0009 is accepted and the bounded P2 implementation/proof plan exists.

Do not reopen these without concrete contradictory/regression evidence.

## Accepted workflow-command architecture

ADR-0009 selects:

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

First architecture families:

```text
Bash / sh
PowerShell / pwsh
Windows CMD / batch
```

Retained boundaries:
- parse broadly, claim narrowly;
- syntax family and GitHub execution profile are distinct;
- Tree-sitter nodes remain implementation machinery behind UpgradePilot-owned contracts;
- static command occurrence does not establish command execution/success;
- parser/grammar uncertainty remains conservative and must not fall back to the old regex splitter for positive evidence;
- Python shell mode and arbitrary custom interpreters remain separate language responsibilities.

## Three-cycle implementation structure

### Cycle 1 — parser, shell-context, and shared command-analysis foundation — CURRENT

```text
Tree-sitter runtime + grammar compatibility/characterization
→ effective shell resolution
→ parser-neutral command IR
→ Bash/sh + PowerShell/pwsh + CMD/batch adapters
```

Current state:

```text
A — COMPLETE
B — IN PROGRESS
    parser compatibility characterization passed on second trial
    shell-context + parser-neutral command-analysis foundation implemented
    focused local validation is NEXT
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

### Cycle 1 B evidence so far

The initial A-selected trial used:

```text
tree-sitter==0.24.0
tree-sitter-bash==0.25.1
tree-sitter-pwsh==0.38.1
tree-sitter-batch==0.11.1
```

The packages installed together, but executable characterization failed before parsing:

```text
grammar ABI = 15
Tree-sitter 0.24 accepted language ABI = 13..14
→ incompatible
```

The characterization gate worked as intended: no dependency metadata or adapter assumption was accepted from package metadata alone.

The smallest corrected trial upgraded only the runtime:

```text
tree-sitter==0.25.0
tree-sitter-bash==0.25.1
tree-sitter-pwsh==0.38.1
tree-sitter-batch==0.11.1
```

Observed local evidence from Ali's WSL/Python 3.12 environment:

```text
pip check → No broken requirements found
runtime language ABI range = 13..15
bash grammar ABI = 15
powershell grammar ABI = 15
cmd grammar ABI = 15
characterization RESULT=PASS
```

The retained characterization showed all three grammars can support the current normalized propositions:

- comments do not become commands/arguments;
- quoted separator/command-looking payload remains inside one real command;
- ordinary multiple commands retain separate source spans/order;
- Bash `list`, PowerShell `pipeline_chain_tail`, and CMD `cond_exec` expose short-circuit structure;
- Bash/PowerShell/CMD conditional and pipeline structures remain distinguishable;
- malformed examples set parser error state;
- UTF-8 source byte spans cover Unicode command text correctly.

The exact characterized parser set is now the initial product dependency contract. It is pinned exactly because current adapters depend on observed CST schemas; upgrades should rerun the retained characterization probe rather than silently widening an unproven range.

### Cycle 1 B implementation now present

Provider-owned shell resolution:

`src/upgradepilot/github/workflow_command_shell.py`

It implements:

```text
step shell
> job defaults.run.shell
> workflow defaults.run.shell
> job-container default when present
> safely established hosted platform default
```

and keeps:

```text
syntax_family != execution_profile
```

Current admitted default profiles include the GitHub job-container rule that unspecified `run` steps inside a job container use `sh`; this remains Bash/sh syntax with a distinct `github_default_container_sh` execution profile.

Shared parser-neutral command analysis:

`src/upgradepilot/github/workflow_command_analysis.py`

It provides:

```text
StaticCommandAnalysis
StaticCommandOccurrence
StaticCommandAtom
CommandSourceSpan
structured parse/problem state
```

and maps grammar-specific CST nodes into common source-order/span/atom/structural-context records. A material parser error fails closed with zero admitted occurrences and no regex fallback.

Focused proof added:

- `tests/test_github_workflow_command_analysis.py`
- expanded `tests/test_runtime_dependency_contract.py`
- expanded `tests/test_source_topology.py`

Implementation commits after the successful characterization-probe update:

```text
b562a5b2  feat: resolve effective workflow command shell
ae358f22  feat: add parser-backed workflow command analysis
2b3fbf2d  build: add characterized shell parser dependencies
31b59465  test: protect characterized shell parser stack
58639635  test: prove workflow command analysis foundation
67d8017f  test: include workflow command owners in source topology
```

No Cycle 2 consumer migration has started: `direct_install.py`, `environment_selection.py`, CI command composition, `segment_index`, and runtime-strengthening behavior remain unchanged.

### Cycle 2 — static evidence consumer migration and command identity correction — PLANNED

```text
shared command-analysis producer
→ direct requirements
→ project-environment selection
→ CI direct package invocation/composition
→ segment_index/source-order reconciliation
→ same-step static ordering correction
```

Cycle 2 begins only after Cycle 1 reaches E and the foundation is accepted.

### Cycle 3 — runtime-strengthening correctness, consolidation, and broad proof — PLANNED

```text
static command occurrence
+ structural/control-flow context
+ effective execution profile
+ exact correlated runtime step evidence
→ bounded runtime-strengthening eligibility
```

Cycle 3 owns runtime-strengthening policy, final obsolete-path removal, and focused → nearby → full deterministic proof.

## Immediate next action

Validate Cycle 1 B locally from narrow to nearby proof:

```text
characterization replay
→ focused workflow-command + dependency-contract + source-topology tests
→ existing workflow-definition regression tests
```

If failures expose adapter/schema mistakes, diagnose and repair inside B. If focused/nearby proof is green, preserve B implementation evidence and advance to Cycle 1 C rather than beginning Cycle 2 automatically.

## Current stop line

During Cycle 1 B do not:

- migrate direct requirements, project-environment, or CI package-invocation consumers;
- change runtime-strengthening/static↔runtime CI policy;
- expose Tree-sitter nodes as product/domain contracts;
- treat parser success as execution proof;
- fall back to old regex splitters for positive evidence;
- parse runtime logs/artifacts;
- combine this work with matrix/reusable-workflow expansion, exact installed-version/wheel evidence, Target redesign, or maintainer-action enablement.

After all three static-command cycles close, re-audit the evidence path and select the next decision-critical bottleneck rather than broadening automatically.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
