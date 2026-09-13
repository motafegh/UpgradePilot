# Static Workflow Command Analysis — Three-Cycle Implementation Working Memory

**Date:** 2026-09-13  
**Session status:** ACTIVE  
**Primary mode:** Learning-by-Doing — three-cycle implementation execution  
**Selected parent plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Selected bounded implementation plan:** [`../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`](../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md)  
**Accepted architecture:** [`../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`](../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md)  
**Previous design/planning memory:** [`2026-09-13_static-shell-direct-install-false-positive-recognition.md`](2026-09-13_static-shell-direct-install-false-positive-recognition.md)

## Three-cycle execution map

The accepted implementation plan will be executed through **three top-level Learning-by-Doing cycles**, each using the normal:

```text
A → B → C → D → E
```

These are not nested sub-cycles inside the previous Phase A. The previous architecture/planning Phase A is closed. Each cycle below owns one coherent implementation responsibility and must reach its own E reassessment before the next cycle starts.

### Cycle 1 — parser, shell-context, and shared command-analysis foundation

Responsibility:

```text
Tree-sitter runtime + grammar compatibility/characterization
→ effective GitHub Actions shell context resolution
→ parser-neutral UpgradePilot command-analysis IR
→ Bash/sh + PowerShell/pwsh + CMD/batch adapters
```

Purpose:

- prove that the selected parser substrate and grammar packages can actually support the admitted propositions under the supported Python environment;
- establish `syntax_family` separately from `execution_profile`;
- create one shared command occurrence/source identity before downstream consumers migrate;
- characterize parser errors, comments, quoting, source spans, command structure, and representative control-flow shapes per shell family;
- keep grammar-specific Tree-sitter nodes behind the adapter boundary.

Cycle 1 pass direction:

```text
compatible parser dependency set
+ characterized admitted grammars
+ conservative shell resolver
+ shared parser-neutral command IR
+ focused multi-shell proof
```

If a shell grammar fails its characterization gate, do not fall back to regex splitting. Preserve that family as unsupported/unresolved and reassess before claiming its admission.

### Cycle 2 — static evidence consumer migration and command identity correction

Responsibility:

```text
shared command-analysis producer
→ direct requirements observation
→ project-environment selection
→ CI direct package invocation / composition
→ segment_index / source-order reconciliation
→ same-step static ordering correction
```

Purpose:

- remove independent command splitting from dependency and CI consumers;
- make direct requirements and project-environment evidence operate on real parsed command occurrences;
- migrate direct package invocation to the same shared command identity;
- make source span/occurrence identity canonical;
- retain a source-order ordinal only if an admitted consumer independently requires it;
- prevent simple source order from being treated as same-path execution proof;
- remove comment/quoted-payload false positives across all migrated static observers.

Cycle 2 pass direction:

```text
one shared command identity source
+ migrated dependency consumers
+ migrated CI static invocation consumer
+ known false-positive classes closed
+ no duplicated normal-path splitters
+ focused + nearby static-composition proof
```

### Cycle 3 — runtime-strengthening correctness, consolidation, and broad proof

Responsibility:

```text
static command occurrence
+ structural/control-flow context
+ effective execution profile
+ exact correlated runtime step evidence
→ bounded runtime-strengthening eligibility
```

Purpose:

- introduce the explicit runtime-strengthening classifier required by ADR-0009;
- admit only command structures for which whole-step success justifies the stronger proposition;
- keep conditional, short-circuited, parser-ambiguous, or execution-profile-ambiguous occurrences static-only/unresolved at the stronger runtime proposition;
- correct direct-exercise/runtime composition where old segment/order assumptions overstate execution;
- remove any remaining obsolete inference routes;
- run focused, nearby, and full deterministic validation;
- perform the plan-level final reassessment before returning to the parent maintainer-action synthesis journey.

The first required positive strengthening class remains deliberately conservative:

```text
one cleanly parsed straightforward top-level command occurrence
+ established syntax family
+ established execution profile
+ exact correlated completed/successful runtime step
→ eligible for the currently admitted stronger runtime proposition
```

Cycle 3 pass direction:

```text
false static premise + successful step → never becomes supported runtime evidence
real conditional/path-dependent command + successful step → static evidence may remain, stronger execution claim does not
straightforward eligible command + successful correlated step → runtime strengthening remains available
+ focused/nearby/full deterministic proof green
```

## Why three cycles

Three cycles are the selected balance between two bad extremes:

```text
one giant implementation cycle
→ too much migration/proof risk before reassessment
```

and:

```text
many tiny cycles
→ fragmented execution, repeated ceremony, weak ownership continuity
```

The grouping follows real engineering boundaries:

1. establish a trustworthy producer/foundation;
2. migrate static consumers onto that producer;
3. compose runtime authority only after static semantics are trustworthy.

E of each cycle is a genuine gate. The next cycle is not automatic if new evidence changes the architecture, proof boundary, or implementation plan.

## Pre-implementation design/planning phase — CLOSED

The previous working memory completed the design responsibility:

```text
confirmed false-positive pressure
→ broader control-flow diagnosis
→ cross-layer owner trace
→ architecture/tooling comparison
→ ADR-0009 accepted
→ bounded P2 implementation/proof plan created
```

No product source/test implementation occurred during that Phase A.

The durable architecture is now owned by ADR-0009; the execution sequence/proof/stop line is owned by the selected implementation plan. This working memory owns only the dated three-cycle execution progression.

## Cycle 1 — parser, shell-context, and shared command-analysis foundation

### Current state

```text
A — IN PROGRESS
    first substantive orientation/design round complete
B — NOT STARTED
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

Cycle 1 A is read-only with respect to product source/tests/dependencies. Working-memory preservation is allowed.

### A responsibility

Cycle 1 A is bounded because the durable architecture is already decided. It resolves only local foundation questions needed before Build:

- compatible Tree-sitter/runtime/grammar characterization starting point under the supported Python environment;
- effective shell precedence and conservative platform/default inference;
- smallest parser-neutral command-analysis IR required by current consumers and later runtime strengthening;
- adapter admission/error behavior;
- representative multi-shell characterization/proof matrix;
- exact Cycle 1 Build stop line.

It must not reopen ADR-0009 without new evidence that the accepted parser-backed architecture cannot satisfy the responsibility.

### A finding 1 — environment and parser dependency characterization starting point

UpgradePilot currently requires:

```text
Python >=3.12
local reusable baseline: Python 3.12.3 under WSL2
```

Current project runtime dependencies remain only `requests`, `packaging`, and `PyYAML`; no Tree-sitter packages are installed by project metadata yet.

Current package evidence as of 2026-09-13:

```text
tree-sitter latest       0.26.0
tree-sitter-bash         0.25.1
tree-sitter-pwsh         0.38.1
tree-sitter-batch        0.11.1
```

The important compatibility fact is that the current Bash, PowerShell and Batch grammar package metadata each advertises the optional core runtime as:

```text
tree-sitter ~=0.24
```

`~=0.24` means the grammar maintainers are declaring compatibility within the 0.24 line, not automatically with the latest 0.26 runtime. Tree-sitter 0.24.0 also publishes CPython 3.12 wheels, including manylinux x86-64 appropriate to the normal WSL baseline.

Therefore Cycle 1 B should begin characterization from this exact **trial set**, not immediately write final dependency ranges:

```text
tree-sitter==0.24.0
tree-sitter-bash==0.25.1
tree-sitter-pwsh==0.38.1
tree-sitter-batch==0.11.1
```

This is a characterization input, **not yet the accepted long-term dependency constraint**. B must prove imports/parser construction/representative behavior first. Final `pyproject.toml` ranges should be chosen from observed compatibility and normal UpgradePilot dependency policy rather than copying latest versions or broadening beyond declared grammar compatibility without evidence.

A secondary newer-runtime probe (`tree-sitter==0.26.0`) is not required for the initial gate. It becomes justified only if the 0.24 line cannot satisfy a material requirement or there is concrete value in proving later runtime compatibility.

### A finding 2 — effective-shell resolution owner and precedence

The existing GitHub static workflow IR already preserves the required inputs:

```text
workflow defaults.run.shell
job defaults.run.shell
step shell
job runs-on typed static value
```

The shell resolver therefore belongs beside the GitHub Actions static workflow-definition boundary rather than under dependency or CI consumers.

Accepted precedence:

```text
step shell
> job defaults.run.shell
> workflow defaults.run.shell
> platform default when the runner platform is safely statically established
```

This mirrors GitHub Actions' most-specific-default rule.

A dynamic/expression-backed higher-precedence shell declaration shadows lower levels and yields unresolved shell context rather than falling through to a lower declaration.

### A finding 3 — shell syntax family and execution profile mapping

The resolver must keep two different facts:

```text
syntax_family
→ how run text is parsed

execution_profile
→ how GitHub invokes the temporary script / what wrapper behavior is established
```

Initial admitted syntax mapping:

```text
bash / sh                     → bash-family syntax
pwsh / powershell             → powershell syntax
cmd                           → cmd/batch syntax
python                        → unsupported for this shell-command responsibility
other interpreter             → unsupported/unresolved
```

Built-in/default execution profiles remain distinct, including at least:

```text
GitHub non-Windows unspecified default
github explicit bash
github explicit sh
github built-in pwsh
github built-in powershell
github built-in cmd
custom shell template
unresolved
```

A simple literal custom shell template whose executable clearly identifies an admitted family (for example `bash {0}`) may use that family's syntax parser while retaining `custom_shell_template` as its execution profile. Ambiguous/custom interpreter templates remain unresolved/unsupported.

### A finding 4 — conservative platform-default inference

When `shell` is unspecified, syntax depends on the actual runner platform.

For the first Cycle 1 implementation, platform-default inference should be deliberately conservative:

- literal standard GitHub-hosted labels that clearly establish `ubuntu-*` or `macos-*` may establish the non-Windows default shell family;
- literal standard GitHub-hosted `windows-*` labels may establish the Windows PowerShell default;
- dynamic/matrix `runs-on` remains unresolved;
- self-hosted/custom label sets must not be treated as authoritative proof of actual OS merely because one label says `linux`, `windows`, or `macos`;
- explicit admitted `shell` declarations do not require runner-platform inference for syntax-family selection.

This avoids converting labels/expressions into stronger platform facts than the static workflow actually establishes.

### A finding 5 — minimum parser-neutral command IR

The existing consumers show that the foundation does not need a generic shell AST or control-flow graph.

The smallest useful internal representation should conceptually contain:

```text
EffectiveShellContext
    state
    source               # step / job / workflow / platform default
    raw declaration
    syntax_family
    execution_profile

StaticCommandAnalysis
    state                # analyzed / unresolved / unsupported
    shell_context
    command_occurrences[]
    problems[]

StaticCommandOccurrence
    source_order
    source_span          # UTF-8 byte range + line/column points relative to run text
    raw_source
    executable_atom
    argument_atoms[]
    structural_context[]

StaticCommandAtom
    raw_source
    literal_value | None
    state                # literal / dynamic-or-unsupported
```

The exact class/enum names remain implementation details; the contract above is the required information shape.

Why these fields are earned by current pressure:

- direct requirements needs literal `pip` / `python -m pip` executable/arguments and `-r` path atoms;
- project-environment selection needs literal pip/uv command and option/project atoms;
- CI direct package invocation needs literal executable/prefix atoms and deterministic source order;
- Cycle 2 needs one shared occurrence identity instead of independently reconstructed segment ordinals;
- Cycle 3 needs structural context to distinguish straightforward top-level commands from conditional/short-circuit/nested structures;
- raw source + span preserves traceability without leaking Tree-sitter nodes.

Occurrence identity is scoped by the exact workflow source + job/step identity and the occurrence's source span/order. A Tree-sitter node object or grammar-specific node index must never be the durable identity.

### A finding 6 — initial structural context vocabulary

Cycle 1 does not need a general CFG. It only needs enough context to prevent later evidence overclaim and to support current static ordering.

The adapter should preserve a bounded context vocabulary such as:

```text
straightforward_top_level
linear_chain
short_circuit
conditional
loop
pipeline
function_or_block
nested_or_subshell
other_supported_nested
unsupported_or_ambiguous
```

An occurrence may carry more than one context tag when structurally appropriate (for example a pipeline inside a conditional). Shell-specific syntax remains inside the adapter; downstream consumers see only normalized UpgradePilot context.

### A finding 7 — parser error/admission baseline

Tree-sitter recovery is useful, but a recovered tree is not automatically trustworthy evidence.

The initial Cycle 1 positive-admission rule should be intentionally conservative:

```text
clean parse with no ERROR/MISSING affecting the run script
→ occurrences may be admitted

ERROR/MISSING or materially unsupported parse shape
→ StaticCommandAnalysis unresolved/unsupported
→ no positive command evidence from fallback regex splitting
```

For the first implementation, treating any material parser error in the run script as unresolved is preferable to prematurely implementing local error-region salvage. Later evidence may justify a narrower unaffected-region rule, but that is not required to close Cycle 1.

### A finding 8 — untrusted-input/resource boundary

Repository text is already bounded to 1,000,000 UTF-8 bytes by `RepositoryTextFile`. GitHub documents a much smaller normal `run:` command limit, but UpgradePilot must still treat arbitrary repository workflow text as untrusted evidence rather than assuming GitHub already accepted it.

Cycle 1 should therefore keep parser traversal bounded and non-recursive where practical. Exact local command-size/node-visit constants remain implementation/test details unless B evidence shows the existing repository bound is insufficient. No arbitrary code execution or shell invocation is part of the parser path.

### A finding 9 — shell-adapter characterization matrix for B

B should first characterize actual parse trees before writing consumer-facing adapter logic. For each admitted shell family, use idiomatic fixtures that prove the same UpgradePilot invariants rather than identical syntax strings.

Minimum classes:

```text
1. simple real command
2. comment containing install/invocation-looking text
3. quoted/string separator + command-looking text
4. multiple top-level commands
5. short-circuit command
6. conditional command
7. pipeline or nested command shape
8. malformed/error-recovered source
9. Unicode/source-span fidelity
```

Characterization must record:

- root/command/control node shapes actually produced;
- executable/argument extraction feasibility;
- source byte/point spans;
- ERROR/MISSING behavior;
- whether the grammar can support the normalized context required by the IR.

The Bash, PowerShell and CMD adapters may use different grammar node mappings. The common requirement is equivalent UpgradePilot semantics, not identical CST structure.

### A finding 10 — exact Cycle 1 Build boundary

Cycle 1 B may modify only the foundation necessary to prove this producer:

```text
parser dependencies
+ effective shell context
+ shared command-analysis IR
+ three shell adapters
+ focused characterization/foundation tests
```

Cycle 1 must stop before migrating:

- `direct_install.py` command interpretation;
- `environment_selection.py` command interpretation;
- CI direct package invocation / `segment_index` composition;
- runtime-strengthening eligibility or static↔runtime CI behavior;
- obsolete splitter removal from current consumers.

Those belong to Cycles 2 and 3. Keeping the old consumers temporarily during Cycle 1 is therefore intentional migration sequencing, not architectural fallback approval.

### A round-1 result

No evidence currently requires reopening ADR-0009 or splitting Cycle 1 further.

The remaining ownership check before formally closing Cycle 1 A is small:

1. why the Tree-sitter **trial** runtime should start at 0.24 rather than simply choosing latest 0.26;
2. why `syntax_family` and `execution_profile` must be separate;
3. why a parser error should become unresolved rather than trigger the old regex splitter;
4. why Cycle 1 stops before migrating direct-install/CI consumers even though the new producer will exist.

If these are materially understood, A can close in the next round and B can begin with explicit Build authorization.

## Global implementation constraints retained

Across all three cycles:

- parse broadly, claim narrowly;
- Tree-sitter nodes remain implementation machinery, not dependency/CI contracts;
- parser success does not prove execution;
- unsupported/ambiguous parser or shell evidence remains conservative;
- do not silently fall back to old regex splitters for positive evidence;
- do not assume Bash grammar maturity transfers to PowerShell/CMD;
- do not absorb runtime logs/artifacts, matrix/reusable-workflow expansion, exact installed-version/wheel evidence, Target redesign, or maintainer-action enablement into these cycles;
- preserve the user preference that each A/B/C/D/E stage normally finishes in one or two substantive rounds unless evidence genuinely requires more or Ali explicitly requests finer steps.

## Current handoff

Cycle 1 A is in progress after its first substantive round. The next step is a concise ownership check/correction and, if sufficient, formal A closure.

No product Build has been authorized by this A-stage work.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`
