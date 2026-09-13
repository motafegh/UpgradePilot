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
- prove the selected parser substrate/grammars under the supported Python environment;
- establish `syntax_family` separately from `execution_profile`;
- create one shared command occurrence/source identity before downstream consumers migrate;
- characterize comments, strings/quotes, source spans, control-flow shape, and parser errors per shell family;
- keep Tree-sitter nodes behind the adapter boundary.

Cycle 1 pass direction:

```text
compatible parser dependency set
+ characterized admitted grammars
+ conservative shell resolver
+ shared parser-neutral command IR
+ focused multi-shell proof
```

If a grammar fails its characterization gate, do not fall back to regex splitting. Preserve that family as unsupported/unresolved and reassess before claiming admission.

### Cycle 2 — static evidence consumer migration and command identity correction

```text
shared command-analysis producer
→ direct requirements observation
→ project-environment selection
→ CI direct package invocation / composition
→ segment_index / source-order reconciliation
→ same-step static ordering correction
```

Purpose: remove duplicate command splitting, migrate static consumers onto real parsed command occurrences, make source-span/occurrence identity canonical, close comment/quoted-payload false positives, and stop treating simple source order as same-path execution proof.

### Cycle 3 — runtime-strengthening correctness, consolidation, and broad proof

```text
static command occurrence
+ structural/control-flow context
+ effective execution profile
+ exact correlated runtime step evidence
→ bounded runtime-strengthening eligibility
```

Purpose: strengthen only command structures whose relationship to whole-step success is justified, keep conditional/short-circuited/ambiguous occurrences static-only or unresolved at the stronger runtime proposition, remove remaining obsolete inference routes, then run focused → nearby → full deterministic proof.

The first required positive strengthening class remains deliberately conservative:

```text
one cleanly parsed straightforward top-level command occurrence
+ established syntax family
+ established execution profile
+ exact correlated completed/successful runtime step
→ eligible for the currently admitted stronger runtime proposition
```

## Why three cycles

Three cycles balance two bad extremes:

```text
one giant cycle
→ too much migration/proof risk before reassessment

many tiny cycles
→ fragmented implementation and repeated ceremony
```

The engineering boundaries are:
1. establish a trustworthy producer/foundation;
2. migrate static consumers onto it;
3. compose runtime authority only after static semantics are trustworthy.

Each cycle's E is a genuine gate.

## Pre-implementation design/planning phase — CLOSED

The previous working memory completed:

```text
confirmed false-positive pressure
→ broader control-flow diagnosis
→ cross-layer owner trace
→ architecture/tooling comparison
→ ADR-0009 accepted
→ bounded P2 implementation/proof plan created
```

No product source/test implementation occurred during that design phase.

## Cycle 1 — parser, shell-context, and shared command-analysis foundation

### Current state

```text
A — COMPLETE
    orientation/design + ownership review complete
B — NEXT / NOT STARTED
    explicit Build/Implement authorization required
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

Cycle 1 A remained read-only with respect to product source/tests/dependencies.

### A responsibility

Cycle 1 A was intentionally bounded because ADR-0009 already selected the architecture. It resolved only local foundation questions needed before Build:

- compatible Tree-sitter/runtime/grammar characterization starting point;
- effective-shell precedence and conservative platform/default inference;
- minimum parser-neutral command IR needed by current consumers and later runtime strengthening;
- adapter admission/error behavior;
- representative multi-shell characterization/proof matrix;
- exact Cycle 1 Build stop line.

No evidence required reopening ADR-0009.

### A finding 1 — parser dependency characterization starting point

UpgradePilot currently requires:

```text
Python >=3.12
local reusable baseline: Python 3.12.3 under WSL2
```

Current project runtime dependencies remain `requests`, `packaging`, and `PyYAML`; Tree-sitter packages are not yet part of project metadata.

The current grammar packages investigated are:

```text
tree-sitter-bash   0.25.1
tree-sitter-pwsh   0.38.1
tree-sitter-batch  0.11.1
```

Their package metadata advertises optional Tree-sitter core compatibility around:

```text
tree-sitter ~=0.24
```

Therefore Cycle 1 B should begin characterization from the exact trial set:

```text
tree-sitter==0.24.0
tree-sitter-bash==0.25.1
tree-sitter-pwsh==0.38.1
tree-sitter-batch==0.11.1
```

This is a characterization input, not the final long-term dependency constraint. Final `pyproject.toml` ranges must be selected from observed compatibility and normal UpgradePilot dependency policy. A newer-runtime probe is justified only if the declared 0.24 line is insufficient or later evidence gives a concrete reason to widen support.

### A finding 2 — effective-shell owner and precedence

The existing GitHub workflow IR already preserves:

```text
workflow defaults.run.shell
job defaults.run.shell
step shell
job runs-on typed static value
```

The effective-shell resolver therefore belongs beside the GitHub Actions static-definition boundary, not under dependency or CI consumers.

Precedence:

```text
step shell
> job defaults.run.shell
> workflow defaults.run.shell
> platform default when runner platform is safely established statically
```

A dynamic/expression-backed higher-precedence shell shadows lower levels and yields unresolved shell context rather than falling through.

### A finding 3 — syntax family vs execution profile

The resolver must preserve two distinct facts:

```text
syntax_family
→ how the run script is parsed

execution_profile
→ how GitHub invokes that script / what wrapper behavior is established
```

Initial syntax mapping:

```text
bash / sh         → bash-family syntax
pwsh / powershell → powershell syntax
cmd               → cmd/batch syntax
python            → outside this shell-command responsibility
other interpreter → unsupported/unresolved
```

Built-in/default and custom wrapper profiles remain distinct. A literal custom template such as `bash {0}` may use Bash syntax while retaining `custom_shell_template` as its execution profile; it must not silently inherit GitHub's built-in Bash wrapper guarantees.

### A finding 4 — conservative platform-default inference

With no explicit shell:

- literal standard GitHub-hosted `ubuntu-*` / `macos-*` labels may establish the non-Windows default family;
- literal standard GitHub-hosted `windows-*` labels may establish the Windows PowerShell default;
- dynamic/matrix `runs-on` remains unresolved;
- self-hosted/custom labels must not be treated as authoritative proof of the actual OS merely from label spelling;
- explicit admitted shell declarations do not require platform inference for syntax-family selection.

### A finding 5 — minimum parser-neutral command IR

The foundation does not need a generic shell AST or full control-flow graph.

Conceptually the smallest useful representation is:

```text
EffectiveShellContext
    state
    source
    raw declaration
    syntax_family
    execution_profile

StaticCommandAnalysis
    state
    shell_context
    command_occurrences[]
    problems[]

StaticCommandOccurrence
    source_order
    source_span
    raw_source
    executable_atom
    argument_atoms[]
    structural_context[]

StaticCommandAtom
    raw_source
    literal_value | None
    state
```

The fields are earned by current consumer pressure:
- direct requirements needs literal pip/python-pip/requirement-path atoms;
- project-environment selection needs pip/uv option/project atoms;
- CI package invocation needs literal invocation identity and deterministic source order;
- Cycle 2 needs one shared occurrence identity instead of independently reconstructed segment ordinals;
- Cycle 3 needs structural context for runtime-strengthening eligibility.

Tree-sitter nodes and grammar-specific node indexes are not durable identity. Command occurrence identity is derived from exact workflow/job/step source context plus stable source span/order.

### A finding 6 — bounded structural context

A general CFG is not required. The adapters should normalize enough context for current propositions, such as:

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

An occurrence may carry multiple tags when appropriate.

### A finding 7 — parser error/admission baseline

Tree-sitter error recovery does not itself establish trustworthy meaning.

Initial admission rule:

```text
clean relevant parse
→ command occurrences may be admitted

material ERROR / MISSING / unsupported structure
→ unresolved / unsupported
→ no positive fallback through the old regex splitter
```

For the first Cycle 1 implementation, broad fail-closed handling is preferable to prematurely salvaging apparently unaffected regions. Narrower salvage can be reconsidered only with evidence.

### A finding 8 — untrusted-input/resource boundary

Repository workflow text is untrusted evidence. `RepositoryTextFile` already bounds exact text to 1,000,000 UTF-8 bytes. Cycle 1 should keep parser traversal bounded/non-recursive where practical; exact local traversal limits are implementation/test details unless evidence shows the repository bound is insufficient. No shell/script execution is part of parsing.

### A finding 9 — B characterization matrix

For each admitted shell family, B should characterize idiomatic examples for equivalent UpgradePilot invariants:

```text
1. simple real command
2. comment containing install/invocation-looking text
3. quoted/string separator + command-looking text
4. multiple top-level commands
5. short-circuit command
6. conditional command
7. pipeline or nested command
8. malformed/error-recovered source
9. Unicode/source-span fidelity
```

Characterization must record:
- actual command/control node shapes;
- executable/argument extraction feasibility;
- source byte/point spans;
- ERROR/MISSING behavior;
- whether the grammar can support the normalized context required by the IR.

The three adapters may use different grammar-node mappings. The common contract is equivalent UpgradePilot semantics, not identical CST shapes.

### A finding 10 — exact Cycle 1 Build boundary

Cycle 1 B may modify only:

```text
parser dependencies
+ effective shell context
+ shared parser-neutral command IR
+ Bash/PowerShell/CMD adapters
+ focused characterization/foundation tests
```

Cycle 1 stops before migrating:
- `direct_install.py` command interpretation;
- `environment_selection.py` command interpretation;
- CI direct package invocation / `segment_index` composition;
- runtime-strengthening/static↔runtime CI behavior;
- obsolete current-consumer splitters.

Leaving the existing consumers temporarily intact during Cycle 1 is migration sequencing, not architectural fallback approval.

### A ownership review — COMPLETE

Ali's understanding was sufficient to close A, with these refinements preserved:

1. **Compatibility-first trial set.** Ali correctly identified compatibility/conflict risk. The precise rule is to begin from the grammars' declared `tree-sitter~=0.24` compatibility line and earn any wider runtime range through evidence rather than choosing latest automatically.
2. **Syntax vs invocation semantics.** Ali correctly separated understanding what language/structure the code uses from whether/how it actually executes. The precise model is `syntax_family` for parsing and `execution_profile` for GitHub invocation/wrapper semantics.
3. **No regex fallback.** Ali identified consistency/reproducibility concerns. The stronger reason is evidential trust: parser uncertainty must remain uncertainty; falling back to the old splitter would convert an explicit inability to establish structure into guessed positive evidence and recreate the defect class being repaired.
4. **Producer before consumers.** Ali correctly identified the need to build the base first. The exact engineering reason is to characterize/prove one stable shared producer before coupling dependency and CI consumers to it, keeping failures attributable and migration risk bounded.

No further A design question is currently material.

## Global implementation constraints retained

Across all three cycles:

- parse broadly, claim narrowly;
- Tree-sitter nodes remain implementation machinery, not dependency/CI contracts;
- parser success does not prove execution;
- unsupported/ambiguous parser or shell evidence remains conservative;
- do not silently fall back to old regex splitters for positive evidence;
- do not assume Bash grammar maturity transfers to PowerShell/CMD;
- do not absorb runtime logs/artifacts, matrix/reusable-workflow expansion, exact installed-version/wheel evidence, Target redesign, or maintainer-action enablement into these cycles;
- preserve the preference that each A/B/C/D/E stage normally finishes in one or two substantive rounds unless evidence genuinely requires more or Ali explicitly requests finer steps.

## Current handoff

Cycle 1 Phase A is formally complete.

The next eligible action is **Cycle 1 B — Build/Implement**, beginning with the parser dependency/grammar characterization gate and only then implementing the shell resolver, shared IR, adapters, and focused foundation tests within the Cycle 1 stop line.

Product source/tests/dependency metadata remain unchanged until Ali explicitly authorizes B/Build.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`
