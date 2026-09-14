# Static Workflow Command Analysis — Three-Cycle Implementation Working Memory

**Date:** 2026-09-13  
**Last progressed:** 2026-09-14  
**Session status:** ACTIVE  
**Primary mode:** Learning-by-Doing — three-cycle implementation execution  
**Selected parent plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Selected bounded implementation plan:** [`../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`](../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md)  
**Accepted architecture:** [`../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`](../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md)

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
B — COMPLETE
C — COMPLETE
D — NEXT / NOT STARTED
E — NOT STARTED
```

## A — closed decisions retained

Cycle 1 A kept ADR-0009 intact and fixed only the local build boundary:

- characterize Tree-sitter runtime + Bash/PowerShell/CMD grammars before accepting dependency metadata;
- resolve shell precedence as `step > job defaults > workflow defaults > safely established environment default`;
- keep `syntax_family` separate from GitHub `execution_profile`;
- admit Bash/sh, PowerShell/pwsh, and CMD/batch as the first shell families;
- keep Python/arbitrary custom interpreters outside this shell-command responsibility;
- use one parser-neutral UpgradePilot IR with source spans/order, literal/dynamic atoms, structural context, and structured problem states;
- fail closed on material parser errors and never re-enter old regex splitting for positive evidence;
- stop Cycle 1 before migrating direct requirements, project-environment selection, CI invocation/segment identity, or runtime strengthening.

Ali's ownership review was sufficient. The durable mental model is:

```text
compatibility-first dependency selection
syntax family != GitHub execution profile
parser uncertainty must remain uncertainty
prove the producer before migrating consumers
```

---

## B — Build/Implement — COMPLETE

### B1 — retained parser/grammar characterization

Retained probe:

`tools/verification/2026-09-13_tree_sitter_shell_grammar_characterization.py`

The first exact trial was intentionally evidence-seeking:

```text
tree-sitter==0.24.0
tree-sitter-bash==0.25.1
tree-sitter-pwsh==0.38.1
tree-sitter-batch==0.11.1
```

It failed usefully during parser construction:

```text
ValueError: Incompatible Language version 15. Must be between 13 and 14
```

Diagnosis:

```text
current grammar wheels = ABI 15
Tree-sitter 0.24 runtime = ABI 13..14
→ metadata hint was insufficient executable evidence
```

The smallest corrected trial changed only the runtime:

```text
tree-sitter==0.25.0
tree-sitter-bash==0.25.1
tree-sitter-pwsh==0.38.1
tree-sitter-batch==0.11.1
```

Ali's WSL/Python 3.12 evidence:

```text
pip check → No broken requirements found
runtime ABI range = 13..15
grammar ABI bash = 15
grammar ABI powershell = 15
grammar ABI cmd = 15
RESULT=PASS
```

Observed grammar facts support the current normalized propositions:

- comments remain non-command syntax;
- quoted separators/command-looking text do not manufacture commands;
- real commands retain deterministic source spans/order;
- Bash `list`, PowerShell `pipeline_chain_tail`, and CMD `cond_exec` expose short-circuit structure;
- conditional and pipeline structure remains distinguishable;
- malformed fixtures set parser error state;
- UTF-8 byte spans remain coherent for Unicode source.

### B2 — implemented foundation

#### Effective shell owner

`src/upgradepilot/github/workflow_command_shell.py`

It owns:

```text
step shell
> job defaults.run.shell
> workflow defaults.run.shell
> job-container default sh when applicable
> safely established hosted platform default
```

and deliberately keeps:

```text
syntax_family != execution_profile
```

#### Shared parser-neutral command owner

`src/upgradepilot/github/workflow_command_analysis.py`

It owns:

```text
StaticCommandAnalysis
StaticCommandOccurrence
StaticCommandAtom
CommandSourceSpan
structured parse/problem state
```

Tree-sitter nodes remain private. Material parser errors fail closed with zero admitted occurrences and no textual fallback.

#### Dependency contract

`pyproject.toml` records the exact characterized stack:

```text
tree-sitter==0.25.0
tree-sitter-bash==0.25.1
tree-sitter-pwsh==0.38.1
tree-sitter-batch==0.11.1
```

Exact pins are deliberate at this stage because the adapters depend on observed CST schemas. Version movement should replay the retained characterization before changing the contract.

#### Focused permanent proof

Added/updated:

- `tests/test_github_workflow_command_analysis.py`
- `tests/test_runtime_dependency_contract.py`
- `tests/test_source_topology.py`

Implementation commits after the characterization-probe update:

```text
b562a5b2  feat: resolve effective workflow command shell
ae358f22  feat: add parser-backed workflow command analysis
2b3fbf2d  build: add characterized shell parser dependencies
31b59465  test: protect characterized shell parser stack
58639635  test: prove workflow command analysis foundation
67d8017f  test: include workflow command owners in source topology
```

### B3 — temporary local synchronization blocker

A first local proof attempt on 2026-09-14 began with `git pull origin main`, but DNS failed:

```text
Could not resolve host: github.com
```

The local tree therefore remained on an older revision. The resulting:

```text
ModuleNotFoundError: tests.test_github_workflow_command_analysis
```

was classified correctly as an environment/synchronization artifact, not a product regression. The retained parser characterization still passed in that attempt.

### B4 — synchronized focused + nearby proof — PASSED

After network access recovered, Ali synchronized successfully:

```text
de7c7f52..6d5c1dc1  main -> origin/main
Fast-forward
```

Environment proof:

```text
python -m pip check
→ No broken requirements found
```

Bounded product/regression proof:

```text
python -m unittest -v \
  tests.test_github_workflow_command_analysis \
  tests.test_runtime_dependency_contract \
  tests.test_source_topology \
  tests.test_github_workflow_definition
```

Observed result:

```text
Ran 34 tests in 0.023s
OK
```

The 34 passing tests cover the new shell resolver, parser-neutral command analysis, parser-stack dependency contract, source topology, and nearest existing workflow-definition provider regressions.

### B proof boundary

Cycle 1 B is now proven at its intended bounded horizon:

```text
characterized parser stack
+ implemented shell resolver
+ implemented shared parser-neutral command IR/adapters
+ focused and nearest-provider regression proof green
```

This does **not** prove:

- migrated `direct_install.py` semantics;
- migrated project-environment selection;
- CI package invocation / `segment_index` reconciliation;
- runtime-strengthening eligibility;
- the final full deterministic repository horizon.

Those belong to Cycles 2 and 3. Avoid inflating the 34-test result beyond this producer/foundation responsibility.

No Cycle 2 consumer migration has started.

---

## C — progressive state preservation — COMPLETE

The meaningful B progression is now preserved in both this working memory and `MEMORY.md`:

- first ABI-incompatible trial and its diagnosis;
- exact characterized passing parser stack;
- shell-resolution and command-analysis owners;
- exact dependency-contract rationale;
- temporary DNS/stale-checkout non-regression classification;
- synchronized 34/34 focused + nearby proof;
- explicit proof limits and remaining cycle boundaries.

No separate working-memory record was created because this remains the same three-cycle responsibility.

---

## D — post-action learning / ownership review — NEXT

D should now review, in moderate depth:

1. what `workflow_command_shell.py` establishes and deliberately does not establish;
2. how `workflow_command_analysis.py` converts three different CST schemas into one common IR;
3. why comments/quotes are now structurally excluded rather than filtered heuristically;
4. why conditional/short-circuit/pipeline occurrences remain real static commands while carrying weaker structural context;
5. why `root.has_error` currently fails the whole run analysis closed;
6. why source byte spans/source order are static identity only, not runtime execution proof;
7. what the 34-test horizon proves and what remains for Cycles 2 and 3.

If D exposes a concrete implementation defect or ownership gap, return to B narrowly. Otherwise proceed to E for Cycle 1 closure and Cycle 2 orientation.

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
