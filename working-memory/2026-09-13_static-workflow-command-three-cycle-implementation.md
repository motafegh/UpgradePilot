# Static Workflow Command Analysis — Three-Cycle Implementation Working Memory

**Date:** 2026-09-13  
**Session status:** ACTIVE  
**Primary mode:** Learning-by-Doing — three-cycle implementation execution  
**Selected parent plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Selected bounded implementation plan:** [`../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`](../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md)  
**Accepted architecture:** [`../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`](../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md)  
**Previous design/planning memory:** [`2026-09-13_static-shell-direct-install-false-positive-recognition.md`](2026-09-13_static-shell-direct-install-false-positive-recognition.md)

## Three-cycle execution map

The accepted implementation plan is executed through three top-level Learning-by-Doing cycles, each using the normal:

```text
A → B → C → D → E
```

These are not nested sub-cycles inside the previous architecture/design Phase A. Each cycle owns one coherent implementation responsibility and reaches its own E reassessment before the next cycle starts.

### Cycle 1 — parser, shell-context, and shared command-analysis foundation — CURRENT

```text
Tree-sitter runtime + grammar compatibility/characterization
→ effective GitHub Actions shell context resolution
→ parser-neutral UpgradePilot command-analysis IR
→ Bash/sh + PowerShell/pwsh + CMD/batch adapters
```

Purpose:
- prove the parser substrate/grammars under the supported Python environment;
- establish `syntax_family` separately from `execution_profile`;
- create one shared command occurrence/source identity before downstream consumers migrate;
- characterize comments, strings/quotes, source spans, control-flow shape, and parser errors per shell family;
- keep Tree-sitter nodes behind the adapter boundary.

### Cycle 2 — static evidence consumer migration and command identity correction

```text
shared command-analysis producer
→ direct requirements observation
→ project-environment selection
→ CI direct package invocation / composition
→ segment_index / source-order reconciliation
→ same-step static ordering correction
```

Purpose: migrate current static consumers onto one parsed command source and close comment/quoted-payload false positives without retaining duplicated normal-path splitters.

### Cycle 3 — runtime-strengthening correctness, consolidation, and broad proof

```text
static command occurrence
+ structural/control-flow context
+ effective execution profile
+ exact correlated runtime step evidence
→ bounded runtime-strengthening eligibility
```

Purpose: whole-step runtime success may strengthen only command occurrences whose static structure and execution profile actually justify that stronger proposition.

## Why three cycles

Three cycles balance two bad extremes:

```text
one giant cycle
→ too much migration/proof risk before reassessment

many tiny cycles
→ fragmented implementation and repeated ceremony
```

The ownership boundaries are:
1. establish a trustworthy producer/foundation;
2. migrate static consumers onto it;
3. compose runtime authority only after static semantics are trustworthy.

Each cycle's E is a genuine gate.

---

# Cycle 1 — parser, shell-context, and shared command-analysis foundation

## Current state

```text
A — COMPLETE
B — IN PROGRESS
    dependency/grammar characterization passed on second trial
    foundation source + focused tests implemented
    local narrow-to-nearby validation NEXT
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

## A — orientation/design — COMPLETE

ADR-0009 already selected the architecture, so Cycle 1 A resolved only local implementation boundaries.

### A conclusions retained

#### 1. Compatibility-first parser admission

UpgradePilot supports Python `>=3.12`; the reusable local baseline is Python 3.12.3 under WSL2.

Initial grammar candidates:

```text
tree-sitter-bash   0.25.1
tree-sitter-pwsh   0.38.1
tree-sitter-batch  0.11.1
```

Package metadata suggested a Tree-sitter core line around `~=0.24`, but A explicitly treated that as a characterization hypothesis rather than executable proof.

#### 2. Effective shell precedence

```text
step shell
> job defaults.run.shell
> workflow defaults.run.shell
> environment default when safely established
```

A dynamic higher-precedence declaration shadows lower levels and yields unresolved context rather than falling through.

#### 3. Syntax family and execution profile are separate facts

```text
syntax_family
→ how static run text is parsed

execution_profile
→ how GitHub invokes the script / which wrapper semantics are established
```

Initial admitted syntax families:

```text
bash / sh
powershell / pwsh
cmd / batch
```

Python and arbitrary custom interpreters are separate language responsibilities.

#### 4. Conservative default inference

Literal hosted Ubuntu/macOS labels may establish the ordinary non-Windows default; literal hosted Windows labels may establish the Windows PowerShell default. Dynamic/matrix/self-hosted/custom runner labels do not justify guessed platform defaults.

#### 5. Parser-neutral shared IR

The minimum useful common representation was selected around:

```text
EffectiveShellContext
StaticCommandAnalysis
StaticCommandOccurrence
StaticCommandAtom
source span + deterministic source order
bounded structural context
structured unresolved/unsupported/error states
```

Tree-sitter nodes and grammar-specific indexes must not escape into dependency/CI contracts.

#### 6. Structural context, not a general CFG

The foundation needs enough normalized structure to distinguish at least:

```text
straightforward top-level
linear sequence
short circuit
conditional
loop
pipeline
function/block
nested/subshell
```

It does not need a universal shell executor or general control-flow graph.

#### 7. Fail closed on parser uncertainty

```text
clean relevant parse
→ occurrences may be admitted

material parse error / unsupported shell structure
→ unresolved/unsupported
→ no positive fallback through old regex splitters
```

#### 8. Cycle 1 stop line

Cycle 1 may implement parser dependencies, shell context, shared IR/adapters, and focused foundation tests only.

It must stop before migrating:
- `dependency/direct_install.py`;
- `dependency/environment_selection.py`;
- CI direct package invocation / `segment_index` composition;
- runtime-strengthening/static↔runtime CI behavior;
- obsolete current-consumer splitters.

### A ownership review

Ali's review was sufficient. The durable learning points are:

```text
compatibility-first dependency selection
syntax family != GitHub execution profile
parser uncertainty must remain uncertainty
prove the shared producer before migrating consumers
```

No further A design question was material.

---

## B — Build/Implement — IN PROGRESS

### B1 — retained characterization gate

Retained probe:

`tools/verification/2026-09-13_tree_sitter_shell_grammar_characterization.py`

It uses UpgradePilot's real workflow-definition IR and checks the parser stack against representative Bash, PowerShell, and CMD cases:

```text
simple command
comment payload
quoted command-looking payload
multiple commands
short circuit
conditional
pipeline
malformed source
Unicode/source spans
```

### B1 trial 1 — FAILED usefully

Initial exact trial:

```text
tree-sitter==0.24.0
tree-sitter-bash==0.25.1
tree-sitter-pwsh==0.38.1
tree-sitter-batch==0.11.1
```

Observed locally:

```text
all packages installed
→ parser construction failed
ValueError: Incompatible Language version 15. Must be between 13 and 14
```

Diagnosis:

```text
current grammar wheels = language ABI 15
Tree-sitter 0.24 runtime = ABI 13..14
→ package metadata compatibility hint was insufficient for these built wheels
```

Consequence: do not accept 0.24 into product metadata and do not reinterpret the failure as an architecture defect. The characterization gate prevented an unproven dependency integration.

### B1 trial 2 — PASSED

Smallest corrected trial changed only the runtime:

```text
tree-sitter==0.25.0
tree-sitter-bash==0.25.1
tree-sitter-pwsh==0.38.1
tree-sitter-batch==0.11.1
```

Ali's local WSL/Python 3.12 evidence:

```text
pip check → No broken requirements found
runtime language ABI range = 13..15
grammar_abi[bash] = 15
grammar_abi[powershell] = 15
grammar_abi[cmd] = 15
RESULT=PASS
```

Observed CST facts:

#### Bash

- simple external command → `program > command` with `command_name` + `word` arguments;
- comment payload → separate `comment`, not command arguments;
- quoted separator payload → one `string`, no manufactured command;
- `&&` / `||` forms → `list` containing real commands;
- conditional → `if_statement` containing its command occurrences;
- pipeline → `pipeline` containing its real commands;
- malformed conditional → root `has_error=True`;
- UTF-8 spans cover Unicode source bytes correctly.

#### PowerShell

- commands appear under `pipeline > pipeline_chain > command`;
- comments remain separate `comment` nodes;
- quoted separator payload remains within one command;
- semicolon-separated statements remain distinct pipelines/commands;
- `||` exposes `pipeline_chain_tail` between command chains;
- conditional commands remain under `if_statement` / `statement_block`;
- real pipe connects multiple command nodes within a pipeline chain;
- malformed block sets `has_error=True`;
- UTF-8 spans remain coherent.

The grammar schema further exposes `command_name` and `command_elements`, with argument separators distinct from generic/literal command elements.

#### CMD / batch

- simple external command → `cmd` with `command_name` + `argument_list`;
- `REM` remains a `comment`;
- quoted `&` remains inside one `string`;
- ordinary `&` sequence → `command_sep`;
- `||` → `cond_exec`;
- conditional → `if_stmt`;
- pipeline → `pipe_stmt`;
- malformed conditional creates an `ERROR` node and root `has_error=True`;
- UTF-8 spans remain coherent.

### Additional B shell-context correction — job containers

Current GitHub Actions documentation states that an unspecified `run` shell inside a job container defaults to `sh`, not the ordinary host Bash default. The workflow IR already preserves `job.container`.

Therefore the implemented resolver includes:

```text
explicit step/job/workflow shell
> job-container default sh
> hosted platform default
```

The container default uses Bash/sh syntax but a distinct execution profile:

```text
syntax_family = bash
execution_profile = github_default_container_sh
```

This is a local correctness refinement inside the accepted shell-context responsibility, not a new architecture.

### B2 — implementation now present

#### Provider-owned effective shell context

`src/upgradepilot/github/workflow_command_shell.py`

Current responsibilities:
- apply step > job > workflow precedence;
- preserve dynamic higher-precedence ambiguity;
- distinguish syntax family from execution profile;
- model GitHub-hosted non-Windows/Windows defaults conservatively;
- model job-container default `sh` separately;
- admit known custom Bash/PowerShell/CMD executable syntax while retaining `custom_shell_template` execution semantics;
- keep Python/arbitrary interpreters unsupported for this shell-analysis responsibility.

Commit:

```text
b562a5b2  feat: resolve effective workflow command shell
```

#### Parser-neutral shared command analysis

`src/upgradepilot/github/workflow_command_analysis.py`

Current responsibilities:
- choose the Tree-sitter grammar from the resolved syntax family;
- fail closed on `root.has_error`;
- traverse the syntax tree with bounded depth/visit limits;
- extract real grammar command nodes per family;
- normalize executable/argument atoms as literal/dynamic/unsupported;
- preserve UTF-8 source spans and deterministic source order;
- normalize structural context for short-circuit/conditional/pipeline/etc.;
- keep all Tree-sitter `Node` objects private.

Commit:

```text
ae358f22  feat: add parser-backed workflow command analysis
```

#### Characterized runtime dependency contract

`pyproject.toml` now adds the exact proven set:

```text
tree-sitter==0.25.0
tree-sitter-bash==0.25.1
tree-sitter-pwsh==0.38.1
tree-sitter-batch==0.11.1
```

These are exact initially because the product adapters depend on observed CST schemas. Future version movement should rerun the retained characterization probe before widening/changing the dependency contract.

Commit:

```text
2b3fbf2d  build: add characterized shell parser dependencies
```

#### Focused permanent proof

Added/updated:

- `tests/test_github_workflow_command_analysis.py`
- `tests/test_runtime_dependency_contract.py`
- `tests/test_source_topology.py`

The focused test family covers:
- shell precedence and dynamic shadowing;
- hosted platform defaults;
- job-container default `sh`;
- custom-shell syntax/profile separation;
- Python-shell exclusion;
- common literal external-command atoms across Bash/PowerShell/CMD;
- comments/quoted payloads not manufacturing commands;
- short-circuit/conditional/pipeline structural preservation;
- material parser errors failing closed;
- Unicode byte-span identity;
- deterministic source order;
- exact characterized dependency versions;
- direct importability of the new responsibility owners.

Commits:

```text
31b59465  test: protect characterized shell parser stack
58639635  test: prove workflow command analysis foundation
67d8017f  test: include workflow command owners in source topology
```

### B current proof boundary

Implementation is present but not yet accepted as proven. The GitHub repository has no commit-status checks attached to the direct-main implementation commits, so local deterministic validation is required.

Next validation route:

```text
1. replay retained characterization
2. run focused command-analysis + runtime-dependency + topology tests
3. run existing workflow-definition tests as nearest provider regression
4. diagnose any failure inside Cycle 1 B
```

Cycle 1 B must not be closed merely because source exists.

---

## Global implementation constraints retained

Across all three cycles:

- parse broadly, claim narrowly;
- Tree-sitter nodes remain implementation machinery, not dependency/CI contracts;
- parser success does not prove execution;
- unsupported/ambiguous parser or shell evidence remains conservative;
- do not silently fall back to old regex splitters for positive evidence;
- do not assume Bash grammar maturity transfers to PowerShell/CMD;
- do not absorb runtime logs/artifacts, matrix/reusable-workflow expansion, exact installed-version/wheel evidence, Target redesign, or maintainer-action enablement into these cycles;
- each A/B/C/D/E stage should normally finish in one or two substantive rounds unless evidence genuinely requires more.

## Current handoff

Cycle 1 Phase B is active.

The immediate next action is local narrow-to-nearby validation of the implemented foundation. If the focused/nearby tests reveal adapter/schema mistakes, repair them inside B. If they pass, preserve the B proof and advance to Cycle 1 C; do not begin Cycle 2 automatically.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
