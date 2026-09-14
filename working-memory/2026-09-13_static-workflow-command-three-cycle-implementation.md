# Static Workflow Command Analysis — Three-Cycle Implementation Working Memory

**Date:** 2026-09-13  
**Last progressed:** 2026-09-14  
**Session status:** ACTIVE  
**Primary mode:** Learning-by-Doing — three-cycle implementation execution  
**Selected parent plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Selected bounded implementation plan:** [`../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`](../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md)  
**Accepted architecture:** [`../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`](../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md)  
**Previous design/planning memory:** [`2026-09-13_static-shell-direct-install-false-positive-recognition.md`](2026-09-13_static-shell-direct-install-false-positive-recognition.md)

## Three-cycle execution map

```text
Cycle 1 — parser, shell-context, shared command-analysis foundation — CURRENT
A → B → C → D → E

Cycle 2 — static evidence consumer migration + command identity
A → B → C → D → E

Cycle 3 — runtime-strengthening correctness + consolidation + broad proof
A → B → C → D → E
```

The boundaries remain:

```text
Cycle 1 → establish a trustworthy producer/foundation
Cycle 2 → migrate static consumers onto it
Cycle 3 → compose runtime authority only after static semantics are trustworthy
```

---

# Cycle 1 — parser, shell-context, and shared command-analysis foundation

## Current state

```text
A — COMPLETE
B — IN PROGRESS
    parser/grammar characterization ✅
    foundation implementation ✅
    synchronized local focused/nearby validation ← BLOCKED BY TEMPORARY DNS/PULL FAILURE
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

## A — closed decisions retained

Cycle 1 A did not reopen ADR-0009. It fixed the local implementation boundary:

- characterize the Tree-sitter runtime and three grammar packages before accepting dependency metadata;
- resolve effective shell as `step > job defaults > workflow defaults > environment default when safely established`;
- keep `syntax_family` separate from GitHub `execution_profile`;
- admit Bash/sh, PowerShell/pwsh, and CMD/batch as the first shell families;
- leave Python and arbitrary custom interpreters outside this shell-command responsibility;
- use one parser-neutral UpgradePilot IR with source spans/order, literal/dynamic atoms, structural context, and structured problem states;
- fail closed on material parser errors; never re-enter the old regex splitter for positive evidence;
- stop Cycle 1 before migrating direct requirements, project-environment selection, CI invocation/segment identity, or runtime strengthening.

Ali's ownership review was sufficient. The durable mental model is:

```text
compatibility-first dependency selection
syntax family != GitHub execution profile
parser uncertainty must remain uncertainty
prove the producer before migrating consumers
```

---

## B — Build/Implement — IN PROGRESS

### B1 — parser/grammar characterization

Retained probe:

`tools/verification/2026-09-13_tree_sitter_shell_grammar_characterization.py`

Representative cases cover simple commands, comments, quoted command-looking payloads, multiple commands, short circuits, conditionals, pipelines, malformed input, and Unicode/source-span fidelity across Bash, PowerShell, and CMD.

### Trial 1 — useful failure

```text
tree-sitter==0.24.0
tree-sitter-bash==0.25.1
tree-sitter-pwsh==0.38.1
tree-sitter-batch==0.11.1
```

Observed:

```text
packages installed
→ parser construction failed
ValueError: Incompatible Language version 15. Must be between 13 and 14
```

Diagnosis:

```text
current grammar wheels = ABI 15
Tree-sitter 0.24 runtime = ABI 13..14
→ package metadata hint was insufficient executable evidence
```

No product dependency contract was accepted from this trial.

### Trial 2 — PASSED

Smallest correction:

```text
tree-sitter==0.25.0
tree-sitter-bash==0.25.1
tree-sitter-pwsh==0.38.1
tree-sitter-batch==0.11.1
```

Ali's local WSL/Python 3.12 evidence:

```text
pip check → No broken requirements found
runtime ABI range = 13..15
grammar ABI bash = 15
grammar ABI powershell = 15
grammar ABI cmd = 15
RESULT=PASS
```

Observed grammar facts support the accepted normalized propositions:

- comments remain non-command syntax;
- quoted separators/command-looking text do not manufacture commands;
- real commands have deterministic source spans/order;
- Bash `list`, PowerShell `pipeline_chain_tail`, and CMD `cond_exec` expose short-circuit structure;
- conditionals and pipelines remain structurally distinguishable;
- malformed examples set parser error state;
- UTF-8 byte spans remain coherent for Unicode text.

The exact characterized set is therefore the initial product dependency contract. Future parser/grammar upgrades must replay characterization before changing the contract.

### B2 — foundation implementation present

Provider shell context:

`src/upgradepilot/github/workflow_command_shell.py`

It owns:

```text
step shell
> job defaults.run.shell
> workflow defaults.run.shell
> job-container default sh when applicable
> safely established hosted platform default
```

and separates `syntax_family` from `execution_profile`.

Shared parser-neutral command analysis:

`src/upgradepilot/github/workflow_command_analysis.py`

It owns:

```text
StaticCommandAnalysis
StaticCommandOccurrence
StaticCommandAtom
CommandSourceSpan
structured parse/problem state
```

Tree-sitter nodes remain private. Material parser errors fail closed with no regex fallback.

The product dependency contract in `pyproject.toml` now records the exact characterized parser stack.

Focused proof added/updated:

- `tests/test_github_workflow_command_analysis.py`
- `tests/test_runtime_dependency_contract.py`
- `tests/test_source_topology.py`

Implementation commits after the successful characterization-probe update:

```text
b562a5b2  feat: resolve effective workflow command shell
ae358f22  feat: add parser-backed workflow command analysis
2b3fbf2d  build: add characterized shell parser dependencies
31b59465  test: protect characterized shell parser stack
58639635  test: prove workflow command analysis foundation
67d8017f  test: include workflow command owners in source topology
```

No Cycle 2 consumer migration has started.

### B3 — local validation attempt on 2026-09-14

Requested validation route:

```text
git pull origin main
pip check
retained characterization replay
focused command-analysis + runtime-dependency + topology tests
existing workflow-definition regression tests
```

Observed first command:

```text
fatal: unable to access 'https://github.com/motafegh/UpgradePilot.git/':
Could not resolve host: github.com
```

Consequence: the local checkout did **not** synchronize to the foundation implementation commits.

The remaining commands still ran against the older local revision. Evidence from that run must therefore be separated:

```text
pip check → PASS
retained parser characterization → RESULT=PASS
```

These remain valid parser-stack/environment evidence because the updated characterization probe already existed on that older synchronized revision.

However the focused product validation was **not performed against the new implementation**. The test loader reported:

```text
ModuleNotFoundError: No module named 'tests.test_github_workflow_command_analysis'
```

This is consistent with the stale checkout: the new test module had not been pulled locally. The other 18 selected tests passed, but they are existing/stale-revision tests and do not prove the new foundation.

Classification:

```text
NOT a product-code regression
NOT a parser-characterization failure
TEMPORARY ENVIRONMENT/SYNCHRONIZATION BLOCKER
```

Do not repair product code based on this result.

### B next action

Once DNS/GitHub access resolves:

```text
git pull origin main
verify local HEAD includes the foundation commits
pip check
run the focused/nearby unittest set again
```

Only a synchronized run can prove or falsify the new foundation implementation.

If synchronized focused/nearby tests are green, preserve the B proof and advance to Cycle 1 C. If they expose implementation defects, repair them inside B.

---

## Global constraints retained

- parse broadly, claim narrowly;
- Tree-sitter nodes are implementation machinery, not dependency/CI contracts;
- parser success does not prove execution;
- unsupported/ambiguous parser or shell evidence remains conservative;
- no regex fallback for positive evidence;
- do not assume equal grammar maturity across Bash/PowerShell/CMD;
- do not absorb runtime logs/artifacts, matrix/reusable-workflow expansion, exact installed-version/wheel evidence, Target redesign, or maintainer-action enablement;
- do not begin Cycle 2 until Cycle 1 reaches E.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
