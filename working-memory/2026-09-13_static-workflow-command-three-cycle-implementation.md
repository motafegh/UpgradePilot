# Static Workflow Command Analysis — Cycle 1 Closure Working Memory

**Date opened:** 2026-09-13  
**Closed:** 2026-09-14  
**Session status:** HISTORICAL / CLOSED  
**Selected parent plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Selected bounded implementation plan:** [`../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`](../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md)  
**Accepted architecture:** [`../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`](../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md)

## Three-cycle execution map

```text
Cycle 1 — parser, shell-context, shared command-analysis foundation — CLOSED
A → B → C → D → E ✅

Cycle 2 — static evidence consumer migration + command identity — NEXT
A → B → C → D → E

Cycle 3 — runtime-strengthening correctness + consolidation + broad proof
A → B → C → D → E
```

This record now owns the historical evidence for Cycle 1 only. The active continuation is:

`working-memory/2026-09-14_static-command-consumer-migration-and-identity.md`

---

## Cycle 1 bounded responsibility

```text
Tree-sitter runtime + grammar characterization
→ effective GitHub Actions shell context
→ parser-neutral UpgradePilot command-analysis IR
→ Bash/sh + PowerShell/pwsh + CMD/batch adapters
```

Cycle 1 deliberately stopped before direct-requirements migration, project-environment migration, CI package-invocation/command-identity migration, and runtime-strengthening policy.

## A — COMPLETE

Cycle 1 A retained ADR-0009 and resolved only local implementation boundaries:

- characterize parser runtime/grammars before accepting dependency metadata;
- resolve shell precedence as `step > job defaults > workflow defaults > safely established environment default`;
- keep `syntax_family` separate from `execution_profile`;
- admit Bash/sh, PowerShell/pwsh, and CMD/batch first;
- keep Python/arbitrary custom interpreters outside this shell responsibility;
- use one parser-neutral IR with source spans/order, literal/dynamic atoms, structural context, and explicit problem states;
- fail closed on material parser errors with no positive regex fallback.

Ownership review established the durable mental model:

```text
compatibility-first dependency selection
syntax family != GitHub execution profile
parser uncertainty must remain uncertainty
prove the shared producer before migrating consumers
```

## B — COMPLETE

### Characterization

Initial trial:

```text
tree-sitter==0.24.0
tree-sitter-bash==0.25.1
tree-sitter-pwsh==0.38.1
tree-sitter-batch==0.11.1
```

failed usefully because the current grammar wheels use language ABI 15 while Tree-sitter 0.24 accepts ABI 13..14.

Smallest corrected trial:

```text
tree-sitter==0.25.0
tree-sitter-bash==0.25.1
tree-sitter-pwsh==0.38.1
tree-sitter-batch==0.11.1
```

passed under the supported WSL/Python 3.12 environment:

```text
pip check → No broken requirements found
runtime ABI range = 13..15
bash/powershell/cmd grammar ABI = 15
characterization RESULT=PASS
```

The retained probe established that comments and quoted payloads do not manufacture commands, real occurrences preserve source spans/order, short-circuit/conditional/pipeline structure remains visible, malformed fixtures report parser errors, and UTF-8 byte spans are coherent.

### Implementation

Implemented:

- `src/upgradepilot/github/workflow_command_shell.py`
- `src/upgradepilot/github/workflow_command_analysis.py`
- exact characterized parser-stack dependencies in `pyproject.toml`
- focused proof in `tests/test_github_workflow_command_analysis.py`
- parser dependency-contract and source-topology protection.

The shell resolver owns:

```text
step shell
> job defaults.run.shell
> workflow defaults.run.shell
> job-container default sh when applicable
> safely established hosted platform default
```

and preserves `syntax_family != execution_profile`.

The shared analysis owner exposes parser-neutral:

```text
StaticCommandAnalysis
StaticCommandOccurrence
StaticCommandAtom
CommandSourceSpan
structural context
structured problem state
```

Tree-sitter nodes remain private. Material parse errors yield zero admitted occurrences and no textual fallback.

### Proof

A first local run was blocked by temporary DNS failure before synchronization; its `ModuleNotFoundError` was correctly classified as a stale-checkout/environment artifact, not a product regression.

After synchronization, bounded validation passed:

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

This proves the Cycle 1 producer/foundation at its intended focused + nearest-provider horizon. It does not prove consumer migration, runtime strengthening, or the final full deterministic repository horizon.

## C — COMPLETE

State preservation captured:

- failed ABI-14 trial and diagnosis;
- exact ABI-15-compatible parser stack;
- shell/command-analysis owners;
- dependency pin rationale;
- temporary synchronization blocker classification;
- synchronized 34/34 proof;
- explicit proof limits.

## D — COMPLETE

Ownership review established:

```text
WorkflowDefinition
→ EffectiveShellContext
→ shell-family Tree-sitter CST
→ parser-neutral StaticCommandAnalysis
→ later dependency/CI consumers
```

Key learning:

- effective shell context establishes which language actually governs the `run:` text before parser selection;
- Bash/PowerShell/CMD CSTs are normalized into one UpgradePilot command IR;
- real static command occurrence is distinct from command execution/success;
- `true || pip install ...` contains a real short-circuited static occurrence but does not establish that the install executed;
- source span/order is static identity, not runtime proof;
- material parser ambiguity remains uncertainty even when recovered syntax contains command-looking text.

Ali's D ownership check passed. No implementation defect or ownership gap required a return to B.

## E — COMPLETE

### Gap-repair decision

No Cycle 1 repair is justified before closure:

```text
parser characterization green
+ foundation implementation present
+ focused/nearest-provider proof 34/34 green
+ ownership review passed
→ no unresolved Cycle 1 defect
```

The remaining old textual splitters are **not** a Cycle 1 defect because consumer migration was explicitly deferred to Cycle 2. They become Cycle 2 migration targets and must not survive as parallel positive-evidence fallbacks once their consumers migrate.

### What Cycle 2 may trust

Cycle 2 may treat the following as established foundation contracts:

- effective shell resolution is provider-owned;
- supported shell scripts can be converted into one parser-neutral `StaticCommandAnalysis`;
- `StaticCommandOccurrence` is the shared static command source;
- comments/quoted payloads are excluded structurally rather than by downstream heuristics;
- occurrence source span + deterministic source order are available for canonical static identity;
- structural context preserves conditional/short-circuit/pipeline/etc. distinctions;
- parser/shell uncertainty is explicit and must propagate conservatively.

Cycle 2 must **not** reinterpret those contracts as execution/success authority.

### Cycle 2 orientation discovered during E

Current consumers still have three independent pressures:

1. `dependency/direct_install.py` uses `bounded_shell_segments(...)`, regex command recognition, and `matched_segment_index`.
2. `dependency/environment_selection.py` uses the same textual segmentation plus its own `shlex`/regex interpretation and stores `segment_index` in each declaration.
3. `ci/workflow_commands.py` contains another private `_shell_segments(...)`, derives direct package invocation from fragments, validates externally supplied project-environment consumption by re-splitting command text, and carries `segment_index` into CI evidence.

`StaticDependencyConsumptionEvidence` also currently exposes `segment_index`, so migration must deliberately update the cross-layer location contract rather than only replacing one helper.

Cycle 2 A therefore needs to resolve these local questions before Build:

```text
1. Where is one run step analyzed exactly once, and how is the shared
   StaticCommandAnalysis handed to dependency-domain consumers?

2. What is the canonical cross-layer static command location/identity shape?
   It must be based on the shared occurrence span/order, not independent re-splitting.

3. Which current segment_index fields/callers genuinely need a derived source-order
   ordinal during migration, and which should be replaced outright?

4. How do direct-requirements and project-environment observers consume literal/dynamic/
   unsupported atoms while preserving their existing domain semantics and unresolved states?

5. How does direct package invocation use the same occurrence identity without moving
   package/dependency meaning into the GitHub parser layer?

6. Which same-step ordering propositions can remain after source-order identity replaces
   segment_index, without claiming same execution path? Stronger runtime implications remain
   Cycle 3.
```

No Cycle 2 source/test implementation occurred during E.

## Cycle 1 final status

```text
A — COMPLETE
B — COMPLETE
C — COMPLETE
D — COMPLETE
E — COMPLETE

CYCLE 1 — CLOSED
```

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
