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
D — COMPLETE
E — NEXT / NOT STARTED
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

## D — post-action learning / ownership review — COMPLETE

Phase D transferred ownership of the actual Cycle 1 foundation rather than adding implementation.

### D mental model

```text
WorkflowDefinition
→ EffectiveShellContext
→ shell-family Tree-sitter CST
→ parser-neutral StaticCommandAnalysis
→ future Cycle 2 consumers
```

Each stage owns one narrower proposition and does not borrow authority from later stages.

### D concepts reviewed

1. **Effective shell comes before parsing.** `EffectiveShellContext` establishes which shell language actually governs one `run:` block and which GitHub/custom execution profile is statically established. This allows selection of the correct parser without guessing and deliberately does not prove command execution or success.
2. **CST vs UpgradePilot IR.** Bash, PowerShell, and CMD expose different Tree-sitter syntax trees; shell-specific adapters normalize those into shared `StaticCommandOccurrence` / `StaticCommandAtom` records so later dependency/CI consumers do not inherit grammar-specific node schemas.
3. **Occurrence identity is richer than text segmentation.** Source byte spans, deterministic source order, real executable/argument atoms, and structural context replace regex-created fragments as the canonical static-command representation.
4. **Structural presence is separate from runtime execution.** A short-circuited or conditional `pip install` can be a real static command occurrence while still lacking evidence that it executed or succeeded.
5. **Fail closed on parser ambiguity.** Material parser error yields zero admitted occurrences because partial recovered syntax cannot safely authorize positive product evidence; old regex splitting is not a fallback.
6. **Static identity is not runtime identity.** Source span/order tells different consumers which static command they are discussing; it does not prove same-path execution, actual execution, or success.
7. **Proof horizon stays bounded.** The 34/34 test result proves the producer/foundation responsibility only. Consumer migration and runtime strengthening remain Cycle 2 and Cycle 3 responsibilities.

### D ownership check — PASSED

Ali's answers were sufficient, with these refinements:

- For shell context, the precise point is not merely to know which grammar UpgradePilot supports; it is to establish **which shell language actually governs the `run:` text** before choosing a grammar.
- `StaticCommandOccurrence` improves over the old segment model because real syntax distinguishes comments, quoted payloads, conditionals, short circuits, pipelines, and source identity without manufacturing commands from textual separators; uncertainty remains explicit rather than guessed.
- `true || pip install ...` is specifically **short-circuit** structure. Cycle 1 establishes that the `pip install` is a real static occurrence and marks its structure; it does not establish that the second command executed or succeeded.
- A material parse error must remain uncertainty. Merely seeing command-looking text inside Tree-sitter's recovered tree is insufficient evidence for an admitted occurrence because the surrounding malformed syntax may change its meaning.

No ownership gap or implementation defect was exposed during D, so no return to B is justified.

---

## E — gap repair + next-cycle orientation — NEXT

E should now:

1. confirm Cycle 1 has no unresolved defect requiring repair;
2. close Cycle 1 formally at its bounded proof horizon;
3. orient Cycle 2 around the already-planned static-consumer migration responsibility;
4. identify only the local Cycle 2 A questions that still need resolution before its Build phase;
5. avoid beginning Cycle 2 implementation during Cycle 1 E.

---

## Global constraints retained

- parse broadly, claim narrowly;
- Tree-sitter nodes are implementation machinery, not dependency/CI contracts;
- parser success does not prove execution;
- unsupported/ambiguous parser or shell evidence remains conservative;
- no regex fallback for positive evidence;
- do not assume equal grammar maturity across Bash/PowerShell/CMD;
- do not absorb runtime logs/artifacts, matrix/reusable-workflow expansion, exact installed-version/wheel evidence, Target redesign, or maintainer-action enablement;
- do not begin Cycle 2 implementation until Cycle 1 E closes and Cycle 2 A completes.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
