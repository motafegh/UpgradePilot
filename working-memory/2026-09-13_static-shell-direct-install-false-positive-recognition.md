# Static Workflow Command Semantic Correctness — Design/Planning Working Memory

**Date:** 2026-09-13  
**Session status:** CLOSED — design/planning Phase A completed; implementation execution moved to a new three-cycle working memory  
**Primary mode:** Historical Learning-by-Doing + Planning/Design record  
**Selected parent plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Accepted architecture:** [`../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`](../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md)  
**Selected bounded implementation plan:** [`../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`](../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md)  
**Implementation continuation:** [`2026-09-13_static-workflow-command-three-cycle-implementation.md`](2026-09-13_static-workflow-command-three-cycle-implementation.md)  
**Previous:** [`2026-09-12_exact-revision-requirements-constraints-evidence-coherence.md`](2026-09-12_exact-revision-requirements-constraints-evidence-coherence.md)

## Closure / handoff

This record owns the completed design/planning reasoning only. Phase A is formally closed.

Implementation is intentionally regrouped into three fresh top-level Learning-by-Doing cycles under the selected plan:

```text
Cycle 1 — parser, shell-context, and shared command-analysis foundation
Cycle 2 — static evidence consumer migration and command identity correction
Cycle 3 — runtime-strengthening correctness, consolidation, and broad proof
```

The active execution state now belongs to `working-memory/2026-09-13_static-workflow-command-three-cycle-implementation.md` and `MEMORY.md`.

No product source/test implementation occurred in this design/planning record.

## Starting point

The preceding exact-revision requirements/constraints provenance cycle is closed A→E and was validated with:

```text
13 focused provider tests green
15 nearby regressions green
566 full deterministic tests green
```

The next selected correctness responsibility began from a confirmed static shell/direct-install false-positive defect. The parent synthesis journey still prioritizes wrong/overstated evidence before broader evidence production or non-abstention action expansion.

Earlier controlled examples included:

```text
pip install wheel # -r requirements-dev.txt
→ observed — false positive

echo "note; pip install -r requirements-dev.txt"
→ observed — false positive
```

These examples are now understood as symptoms of a broader **static workflow-command semantic correctness** problem rather than the complete implementation horizon.

## Phase A structure used for this responsibility

Ali explicitly requested a finer A-stage breakdown because the first narrow repair proposal risked repeating the same under-design pattern:

```text
A-1 — reframe the real correctness problem and owner path
A-2 — investigate/compare credible architectures and tooling
A-3 — jointly select and formally accept the durable architecture
A-4 — write the bounded implementation/proof plan, then close Phase A
```

This was an explicit exception to the normal preference to finish an A→E stage in one or two substantive rounds. It is not a reusable nested-cycle pattern.

## A-1 — PROBLEM / OWNER REFRAME — COMPLETE

### User correction that changed the horizon

Ali rejected a too-narrow interpretation of proportionality:

> Implementation complexity and migration cost are costs to weigh, not vetoes. Prefer the design that is professionally balanced across correctness, product breadth, maintainability, migration cost, future repair cost, and proof strength. A higher-cost change is justified when evidence shows that a smaller repair would preserve a weak foundation and likely cause more expensive repeated corrections later.

This is consistent with `JUST-003`: “simpler” means the simplest design that adequately satisfies the complete admitted responsibility and proof boundary, not the fewest changed lines today.

### Current implementation/owner trace

The same command proposition is currently reconstructed more than once:

```text
RunStepDefinition.command.text

→ dependency/workflow_context.bounded_shell_segments(...)
   → direct requirements observation
   → project-environment selection

→ ci/workflow_commands._shell_segments(...)
   → segment-index reconciliation
   → direct package invocation / source ordering
```

Both split raw text over `&&`, `||`, `;`, and newline without real shell quote/comment/control-flow ownership. Because `segment_index` crosses layers, independent splitters can make the same ordinal refer to different source fragments. Under `JUST-004`, command structure/identity needs one earliest sufficient owner.

### Broader defect discovered during A

A quote/comment-aware lexer alone would still be insufficient. A command can be genuine source syntax yet not execute:

```text
true || pip install -r requirements-dev.txt
```

or:

```text
if false; then
    pip install -r requirements-dev.txt
fi
echo done
```

Current runtime correlation proves the user-defined GitHub Actions **step** executed/succeeded, not every internal command.

Therefore:

```text
real command occurrence exists
!= command is guaranteed to execute
!= containing step succeeded
```

This matches Product Decision Model §9.2:

```text
workflow definition declares command X
!= command X executed
!= command X succeeded
```

### Shell-language and execution-profile boundary

GitHub Actions has multiple shell families. A-1 established that the architecture must separate:

```text
syntax family
→ how source text is parsed

execution profile
→ how GitHub invokes that script and what wrapper-level execution implications exist
```

For example, built-in `shell: bash` and custom `shell: bash {0}` may share Bash syntax but not GitHub's same wrapper flags.

### A-1 outcome

The original Unix-like quote/comment-aware splitter proposal was superseded as too narrow.

The responsibility became:

> establish a trustworthy shared command-analysis boundary for static command occurrence, structural/control-flow context, shared command identity, and later safe step-level runtime strengthening across the materially relevant GitHub Actions shell domain without executing arbitrary workflow programs.

## A-2 — ARCHITECTURE / OPTION INVESTIGATION — COMPLETE

A-2 compared options across correctness, control-flow expressiveness, shell breadth, shared ownership, maintainability, dependency/supply-chain cost, migration pressure, conservative failure behavior, testability, and future correction cost.

### Enhanced handcrafted scanner

Could fix the first lexical cases, but Bash/sh + PowerShell + CMD control syntax would turn UpgradePilot into the maintainer of several partial shell parsers.

**Assessment:** not preferred as the durable architecture.

### `shlex`, Bash-specific tooling, ShellCheck-style approaches

Useful for narrower Unix/Bash problems but do not provide one balanced multi-shell architecture and do not by themselves solve the control-flow/runtime-authority boundary.

**Assessment:** supporting tools only, not the shared foundation.

### Shell-native heterogeneous parsers

Potentially high fidelity, especially PowerShell's official parser, but creates materially different runtime/integration paths across shell families and no clean common CMD substrate.

**Assessment:** credible second choice, higher integration complexity.

### Tree-sitter parser family

Tree-sitter emerged as the strongest common substrate:

- current Python runtime and Python 3.12 support;
- established Bash grammar;
- active PowerShell and Windows Batch/CMD grammars with Python bindings;
- syntax trees expose commands/comments/strings/control structures instead of requiring regex reconstruction;
- parse recovery surfaces error state that UpgradePilot can treat conservatively.

Important qualification: Bash is materially more mature than the newer PowerShell/CMD grammars, so grammar trust must be earned separately through characterization.

### Parser-backed syntax + UpgradePilot semantic policy

A-2 concluded that Tree-sitter alone is insufficient because syntax structure is not execution proof.

The strongest complete architecture is:

```text
RunStepDefinition + workflow/job context
        ↓
effective shell resolver
        ↓
ShellContext
    syntax_family
    execution_profile
        ↓
shell-specific Tree-sitter adapter
        ↓
UpgradePilot static command IR
        ↓
direct requirements / project environment / package invocation
        ↓
separate runtime-strengthening classifier
        ↓
step-level runtime evidence only where justified
```

The governing principle is:

> **parse broadly, claim narrowly**.

Runtime logs remain a possible later independent evidence source, not a substitute for sound static command semantics.

### A-2 ranking

```text
1. Tree-sitter shell parsers + UpgradePilot-owned command IR + conservative runtime-strengthening policy
2. Shell-native heterogeneous parsers + common IR
3. Shared handcrafted multi-shell parser/scanner
4. Narrow lexer/local regex fixes
```

## A-3 — JOINT ARCHITECTURE DECISION — COMPLETE / ACCEPTED

Ali reviewed A-2 and formally accepted the leading architecture. The durable method is now owned by:

- [`../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`](../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md)

### Accepted architecture

```text
GitHub Actions static run step
+ effective shell context
        ↓
Tree-sitter shell-family parser
        ↓
UpgradePilot-owned command IR
        ↓
static dependency/project/invocation observers
        ↓
separate conservative runtime-strengthening policy
```

The architecture is designed for:

```text
Bash / sh
PowerShell / pwsh
Windows CMD / batch
```

Python shell mode and arbitrary custom interpreters are separate language responsibilities. A custom shell template that clearly invokes a supported shell may reuse that syntax family while retaining a distinct execution profile.

### Why selected

The additional implementation cost earns already-demonstrated needs:

1. one shared command identity/structure across dependency and CI consumers;
2. real syntax structure for comments, quotes, chains, branches and other material control contexts;
3. multi-shell breadth appropriate to GitHub Actions;
4. future extension through one IR/classifier rather than repeated regex additions;
5. static occurrence separated from runtime execution authority;
6. conservative parser-error behavior;
7. parser-library coupling contained behind UpgradePilot adapters.

The handcrafted multi-shell alternative was rejected because it transfers a growing parser-maintenance responsibility to UpgradePilot, not simply because it is more work.

### Accepted claim boundary

Parser success establishes usable static structure only. It does not prove execution.

A correlated successful GitHub Actions step may strengthen an internal command only when both:

```text
static command/control-flow structure
+
effective execution profile
```

justify the inference.

Conditional, short-circuited, parser-ambiguous, execution-profile-ambiguous, or unsupported structures remain static-only or unresolved for the stronger runtime proposition.

Current `segment_index` is migration pressure, not permanent architecture. Source order may remain useful, but a flat ordinal must not be treated as execution-order proof.

## A-4 — BOUNDED IMPLEMENTATION / PROOF PLAN — COMPLETE

A-3 exposed enough dependency, migration and proof breadth to justify one P2 consequential plan rather than moving directly into source mutation.

Created and selected:

- [`../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`](../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md)

Plan creation commit:

```text
fff97cbb  docs: add static workflow command analysis implementation plan
```

### Plan route

The implementation plan coordinates:

```text
parser dependency/grammar characterization
→ effective shell resolution
→ shared parser-neutral command IR
→ Bash/sh + PowerShell/pwsh + CMD/batch adapters
→ direct requirements migration
→ project-environment migration
→ CI package invocation / command-identity migration
→ explicit runtime-strengthening eligibility
→ same-step ordering/direct-exercise correction
→ obsolete splitter removal
→ focused proof
→ nearby integration/runtime regressions
→ full deterministic proof
```

### Important implementation gates preserved

- select Tree-sitter/grammar dependency ranges only after import/parser compatibility characterization on the supported Python environment;
- trust each shell grammar independently; Bash maturity does not transfer automatically to PowerShell/CMD;
- a grammar that fails the current proposition gate remains unsupported/unresolved rather than falling back to regex splitting;
- parser error that may affect a material command proposition must not silently become `not_observed`;
- source span + deterministic occurrence order becomes the canonical command identity direction;
- a source-order ordinal may remain only if an admitted consumer still earns it, and never as execution proof;
- the first required runtime-strengthening class is deliberately conservative: one cleanly parsed straightforward top-level command with established syntax family and execution profile;
- richer/conditional structures may still be statically observed without receiving stronger runtime authority;
- additional strengthening classes require shell-specific evidence, not convenience.

### Explicit prohibited scope retained

The plan does not admit arbitrary workflow execution, generic shell engines, matrix/reusable expansion, runtime log parsing as the primary fix, exact installed versions/wheels, Target redesign, other CI providers, arbitrary interpreter languages, or maintainer-action enablement.

## Phase A result — FORMALLY CLOSED

Phase A completed the full design responsibility:

```text
confirmed false positive
→ broader control-flow diagnosis
→ cross-layer owner trace
→ architecture/tooling comparison
→ durable ADR selection
→ bounded implementation/proof plan
```

No product source/test implementation occurred during Phase A.

The implementation responsibility now continues in the dedicated three-cycle working memory rather than treating the implementation plan as one oversized B stage.

## Learning-by-Doing granularity rule retained

Ali's default rule remains:

> A→B→C→D→E are the real cycle stages. Do not recursively turn each stage into another elaborate sub-cycle. By default, finish each stage in one or two substantive rounds; use more only when genuinely required or explicitly requested.

A-1/A-2/A-3/A-4 were explicitly requested/justified for this consequential design responsibility and are now historical.

## Historical stop line

At the close of this record, the following remain outside the selected implementation responsibility:

- exposing Tree-sitter parser nodes as ordinary dependency/CI contracts;
- treating parser success as execution proof;
- silently falling back to old regex splitters when a parser/grammar is uncertain;
- claiming equal maturity/proof for Bash, PowerShell and CMD grammars without characterization;
- runtime logs/artifacts as the primary command-execution fix;
- matrix/reusable-workflow expansion;
- exact installed-version/wheel semantics;
- Target composition redesign;
- non-abstention maintainer-action enablement;
- reopening the closed exact-revision provenance cycle without new regression evidence.

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
