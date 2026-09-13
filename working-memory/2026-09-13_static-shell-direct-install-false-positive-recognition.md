# Static Workflow Command Semantic Correctness — Working Memory

**Date:** 2026-09-13  
**Session status:** ACTIVE  
**Primary mode:** Learning-by-Doing + Planning/Design — Phase A design/planning  
**Selected parent plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Accepted architecture:** [`../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`](../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md)  
**Previous:** [`2026-09-12_exact-revision-requirements-constraints-evidence-coherence.md`](2026-09-12_exact-revision-requirements-constraints-evidence-coherence.md)

## Starting point

The preceding exact-revision requirements/constraints provenance cycle is closed A→E. Its provider-owned changed-file snapshot fence was implemented and validated with:

```text
13 focused provider tests green
15 nearby regressions green
566 full deterministic tests green
```

The next selected correctness responsibility began from a confirmed static shell/direct-install false-positive defect. The parent synthesis journey still prioritizes wrong/overstated evidence before broader evidence production or non-abstention action expansion.

Earlier controlled examples included:

```text
pip install -r requirements-dev.txt
→ observed

pip install wheel
→ not_observed

pip install wheel # -r requirements-dev.txt
→ observed — false positive

echo "pip install -r requirements-dev.txt"
→ not_observed

echo "note; pip install -r requirements-dev.txt"
→ observed — false positive
```

These examples are now understood as symptoms of a broader **static workflow-command semantic correctness** problem rather than the complete implementation horizon.

## Phase A structure for this responsibility

Ali explicitly requested a finer A-stage breakdown for this consequential design responsibility:

```text
A-1 — reframe the real correctness problem and owner path
A-2 — investigate/compare credible architectures and tooling
A-3 — jointly select and formally accept the durable architecture
A-4 — write the bounded implementation/proof plan, then close Phase A
```

This is an explicit exception to the normal preference to finish an A→E stage in one or two substantive rounds. It is not a reusable nested-cycle pattern.

## A-1 — PROBLEM / OWNER REFRAME — COMPLETE

### User correction that changed the horizon

Ali rejected a too-narrow interpretation of proportionality. The corrected principle for this responsibility is:

> Implementation complexity and migration cost are costs to weigh, not vetoes. Prefer the design that is professionally balanced across correctness, product breadth, maintainability, migration cost, future repair cost, and proof strength. A higher-cost change is justified when evidence shows that a smaller repair would preserve a weak foundation and likely cause more expensive repeated corrections later.

This is consistent with `JUST-003`: “simpler” means the simplest design that adequately satisfies the complete admitted responsibility and proof boundary, not the fewest changed lines today.

### Current implementation/owner trace

The same shell-command proposition is currently reconstructed more than once:

```text
GitHub workflow run scalar
→ RunStepDefinition.command.text

→ dependency/workflow_context.bounded_shell_segments(...)
   → direct_install.observe_direct_installation_declaration(...)
   → environment_selection.observe_project_environment_selection(...)

→ ci/workflow_commands._shell_segments(...)
   → project-environment segment-index validation
   → direct package invocation / source ordering
```

`bounded_shell_segments(...)` and the CI-local `_shell_segments(...)` both split text over `&&`, `||`, `;`, and newline without real shell quote/comment/control-flow ownership.

Because `segment_index` crosses layers as source identity/order, different splitters can make the same integer refer to different command fragments. Under `JUST-004`, this proposition needs one earliest sufficient owner rather than duplicate reconstruction.

### Confirmed lexical false-positive classes

Direct requirements observation can treat comment payload as arguments:

```text
pip install wheel # -r requirements-dev.txt
```

Quoted separator data can manufacture a false executable-looking segment:

```text
echo "note; pip install -r requirements-dev.txt"
```

Project-environment selection is exposed to the same class because it consumes the shared splitter before interpreting pip/uv selectors. CI package-invocation detection is exposed because `workflow_commands.py` has its own equivalent splitter.

### Broader control-flow defect discovered during A

A quote/comment-aware lexer alone would still be insufficient. A command can be genuine static source but not execute on a successful path:

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

Current runtime correlation is at the GitHub Actions **user-defined step** level. It can prove that the whole step completed successfully, not that every internal shell command executed successfully.

Therefore the design must keep these propositions distinct:

```text
real command occurrence exists in static source
!= command is guaranteed to execute on every successful path
!= containing GitHub step completed successfully
```

This matches Product Decision Model §9.2:

```text
workflow definition declares command X
!= command X executed
!= command X succeeded
```

### Shell-language and execution-profile boundary

GitHub Actions does not have one universal shell grammar. Relevant built-in families include Bash/sh, PowerShell/pwsh, Windows cmd, Python and custom shell templates.

The provider already preserves workflow/job/step shell declarations and typed `runs-on` structure. A-1 established that two facts must remain separate:

```text
syntax family
→ how source text is parsed

execution profile
→ how GitHub invokes the script and what wrapper-level execution implications exist
```

For example, built-in `shell: bash` and custom `shell: bash {0}` both use Bash syntax but do not have the same GitHub wrapper flags.

### A-1 outcome

The original “Unix-like quote/comment-aware splitter” recommendation was superseded as too narrow.

The responsibility became:

> establish a trustworthy shared command-analysis boundary for static command occurrence, structural/control-flow context, shared command identity, and later safe step-level runtime strengthening across the materially relevant GitHub Actions shell domain without executing arbitrary workflow programs.

## A-2 — ARCHITECTURE / OPTION INVESTIGATION — COMPLETE

A-2 remained read-only and compared options across correctness, control-flow expressiveness, shell breadth, shared ownership, maintainability, dependency/supply-chain cost, migration pressure, conservative failure behavior, testability, and future correction cost.

### Enhanced handcrafted scanner

A shared state machine could fix quote/comment/escape handling cheaply, but supporting Bash/sh + PowerShell + cmd and their control structures would steadily turn UpgradePilot into the maintainer of three partial shell parsers.

**Assessment:** useful only for tiny adapter utilities; rejected as the durable primary architecture.

### `shlex`, bashlex, ShellCheck-style narrow tools

`shlex` is useful Unix lexical machinery but is not a multi-shell control-flow parser. Bash-specific tools can provide stronger Bash structure but do not solve the PowerShell/CMD/common-owner problem and can introduce separate tool/runtime/license concerns.

**Assessment:** potentially useful supporting mechanisms, not the shared architecture.

### Shell-native heterogeneous parsers

PowerShell's own parser is semantically attractive, but a shell-native strategy would create materially different runtime/integration paths for Bash, PowerShell and CMD, with no equally simple common CMD API.

**Assessment:** technically credible, but higher integration/environment complexity than a common parser substrate.

### Tree-sitter parser family

Tree-sitter emerged as the strongest common substrate:

- current Python runtime and Python 3.12 support;
- established Tree-sitter Bash grammar;
- active PowerShell and Windows Batch/CMD grammars with Python bindings;
- syntax trees expose quotes/comments/commands/control-flow rather than requiring UpgradePilot regex reconstruction;
- parser error recovery exposes `ERROR`/`MISSING`/`has_error`, allowing UpgradePilot to fail conservatively when material syntax is not trustworthy.

Important qualification: the Bash grammar is materially more mature than the newer PowerShell/CMD grammars. Grammar trust must therefore be earned per adapter through characterization tests; Tree-sitter membership alone does not make all grammars equally trustworthy.

**Assessment:** strongest parser substrate, provided parser-library nodes remain behind an UpgradePilot-owned boundary.

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
command observers
    direct requirements
    project environment
    direct package invocation
        ↓
separate runtime-strengthening classifier
        ↓
step-level runtime evidence only where the relationship is justified
```

The governing principle is:

> **parse broadly, claim narrowly**.

A real command inside a conditional may remain useful static declaration evidence without being upgraded to proven runtime execution because the containing step succeeded.

### Runtime logs

Ordinary GitHub Actions logs are diagnostic output, not a guaranteed complete structured command-execution ledger. Debug/trace modes are optional and cannot be assumed for arbitrary public PRs.

**Assessment:** possible future independent evidence source; not the primary correction mechanism.

### A-2 ranking

```text
1. Tree-sitter shell parsers + UpgradePilot-owned command IR + conservative runtime-strengthening policy
2. Shell-native heterogeneous parsers + common IR
3. Shared handcrafted multi-shell parser/scanner
4. Narrow lexer/local regex fixes

Runtime logs → later independent evidence candidate, not replacement for static command analysis
```

## A-3 — JOINT ARCHITECTURE DECISION — COMPLETE / ACCEPTED

Ali reviewed the A-2 result and formally accepted the leading architecture as the best professional balance for UpgradePilot.

The durable method is now owned by:

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

The first architecture is designed for:

```text
Bash / sh
PowerShell / pwsh
Windows CMD / batch
```

Python shell mode and arbitrary custom interpreters are separate language responsibilities and must not be force-parsed as shell commands. A custom shell template that clearly invokes a supported shell may reuse that syntax family while retaining a distinct execution profile.

### Why selected

The option is more expensive than a local bug fix, but the additional cost earns capabilities already demonstrated as necessary:

1. **one shared command identity/structure** across dependency and CI consumers;
2. **real syntax structure** for comments, quotes, chains, branches and other material control contexts;
3. **multi-shell breadth** appropriate to GitHub Actions instead of baking a Unix-only blind spot into the replacement;
4. **future extension through one IR/classifier** rather than repeated regex additions in several consumers;
5. **static occurrence separated from runtime execution authority**, preserving useful evidence without overclaiming;
6. **conservative parser-error handling** rather than fallback guessing;
7. **contained library coupling** because Tree-sitter AST/CST nodes stay behind UpgradePilot adapters.

The alternative of a handcrafted multi-shell parser was rejected not because implementation is expensive, but because that option transfers a growing parser-maintenance responsibility to UpgradePilot with weaker long-term leverage.

### Accepted claim boundary

Parser success means only that the admitted parser/adapter produced usable static structure. It does not prove command execution.

A successful correlated GitHub Actions step may strengthen an internal command occurrence only when both:

```text
static command/control-flow structure
+
effective execution profile
```

justify the inference.

Conditional, short-circuited, parser-ambiguous, execution-profile-ambiguous, or otherwise unsupported structures remain static-only or unresolved for the stronger runtime proposition.

### `segment_index`

Current `segment_index` is migration pressure, not permanent architectural authority.

Source order may remain useful, but a flat ordinal must no longer be the sole basis for execution-order claims when control flow can invalidate that inference. The implementation plan will decide the smallest safe migration/compatibility path toward the shared command occurrence identity.

### A-3 durable consequences

- Tree-sitter runtime + admitted grammar packages become candidate runtime dependencies once implementation begins;
- the exact dependency versions are intentionally not selected by the ADR and must be proven during implementation integration;
- grammar characterization is required per shell family, especially for the newer PowerShell/CMD grammars;
- the shared command IR and effective shell resolver become cross-module migration responsibilities;
- runtime-strengthening semantics require their own focused tests beyond parser correctness.

No product source/tests have been modified yet, and ADR acceptance does not prove parser installation or product behavior.

## A-4 — BOUNDED IMPLEMENTATION / PROOF PLAN — NEXT / JUSTIFIED

A-3 exposed enough implementation and migration breadth that a durable bounded plan is now justified.

Planning/Design classification: **P2 — consequential plan**.

Why a plan is warranted:

```text
accepted parser-framework dependency
+ three shell-family adapters
+ effective-shell resolution
+ new shared command IR
+ migration of several existing consumers
+ segment_index/order semantics pressure
+ runtime-strengthening policy refinement
+ focused → integration → broad proof layers
```

Wrong sequencing could create substantial rework—for example migrating consumers before the shared IR/adapter contract is proven, or changing runtime-strengthening behavior before static source identity is stable.

### A-4 should create one plan, not a plan family

One responsibility still owns the work, so a P3 plan family would be unnecessary ceremony.

Recommended plan identity:

```text
plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md
```

The plan should reference ADR-0009 instead of re-specifying it and coordinate at least:

1. dependency integration / parser characterization gate;
2. effective shell context/resolution;
3. shell adapters + UpgradePilot command IR;
4. direct-requirements and project-environment migration;
5. CI direct-package invocation / ordering migration;
6. runtime-strengthening eligibility migration;
7. `segment_index` compatibility/removal decision based on actual consumers;
8. focused multi-shell proof;
9. static→runtime composition/regression proof;
10. full deterministic regression proof;
11. explicit stop line preventing logs/artifacts, matrix/reusable expansion, exact wheel/version semantics, or maintainer-action enablement from entering this build.

### A-4 authorization state

The plan is **needed and recommended**, but no plan file has been created in A-3 merely from architecture acceptance. A-4 is the exact next Planning/Design action.

Product source/test Build remains unauthorized until the bounded plan exists and Ali explicitly moves the cycle into B/Build.

## Learning-by-Doing granularity rule

Ali's default rule remains:

> A→B→C→D→E are the real cycle stages. Do not recursively turn each stage into another elaborate sub-cycle. By default, finish each stage in one or two substantive rounds; use more only when genuinely required or explicitly requested.

A-1/A-2/A-3/A-4 are explicitly requested/justified for this consequential architecture decision and should not become a reusable nested-cycle pattern.

## Stop line

Phase A remains read-only with respect to product source/tests.

Do not yet:

- implement Tree-sitter dependencies or product source before the A-4 plan is written and Build is explicitly authorized;
- expose Tree-sitter parser nodes as ordinary dependency/CI contracts;
- treat parser success as execution proof;
- silently fall back to old regex splitters when a parser/grammar is uncertain;
- claim equal maturity/proof for Bash, PowerShell and CMD grammars without characterization;
- parse runtime logs/artifacts as part of this correction;
- combine this work with matrix/reusable-workflow expansion;
- add exact installed-version/wheel semantics;
- redesign Target composition;
- enable a non-abstention maintainer action;
- reopen the closed exact-revision provenance cycle without new regression evidence.

## Current Learning-by-Doing state

```text
Slice: static workflow-command semantic correctness and safe runtime strengthening

A — IN PROGRESS
    A-1 — COMPLETE
        problem/owner horizon reframed
    A-2 — COMPLETE
        credible architecture/tooling options compared
    A-3 — COMPLETE / ACCEPTED
        ADR-0009 selects Tree-sitter parsers + UpgradePilot command IR + conservative runtime strengthening
    A-4 — NEXT
        write one P2 bounded implementation/proof plan; then Phase A can close

B — NOT STARTED
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
