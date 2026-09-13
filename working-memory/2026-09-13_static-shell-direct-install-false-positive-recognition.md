# Static Shell / Direct-Install False-Positive Recognition — Working Memory

**Date:** 2026-09-13  
**Session status:** ACTIVE  
**Primary mode:** Learning-by-Doing + Planning/Design — Phase A design investigation  
**Selected parent plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Previous:** [`2026-09-12_exact-revision-requirements-constraints-evidence-coherence.md`](2026-09-12_exact-revision-requirements-constraints-evidence-coherence.md)

## Starting point

The preceding exact-revision requirements/constraints provenance cycle is closed A→E. Its provider-owned changed-file snapshot fence was implemented and validated with:

```text
13 focused provider tests green
15 nearby regressions green
566 full deterministic tests green
```

The next selected correctness responsibility is the remaining confirmed static shell/direct-install false-positive recognition defect already retained by the parent synthesis journey.

This selection follows the current priority discipline:

```text
wrong / overstated evidence
before
broader evidence production or action expansion
```

Runtime correlation can strengthen a static dependency-consumption premise by proving that the containing workflow step ran successfully. It therefore becomes more important that the static premise itself not be a false positive.

## Confirmed failure shape retained from prior investigation

The earlier controlled investigation reproduced examples such as:

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

These examples are now treated as symptoms of a broader command-semantics problem rather than as the complete implementation horizon.

## Phase A structure for this responsibility

Ali explicitly asked to keep the overall A→E cycle intact while subdividing this consequential design stage enough to reason properly:

```text
A-1 — preserve/reframe the real correctness problem and current implementation/owner trace
A-2 — investigate and compare credible architectural options, including higher-cost options when they may reduce future correction debt
A-3 — Ali + AI decide the selected design together, record the decision/proof boundary, and formally close Phase A
```

This is an explicit exception to the normal preference to finish one stage in one or two shots. It is not a reusable nested-cycle pattern.

## A-1 — PROBLEM / OWNER REFRAME — COMPLETE

A-1 is read-only. No product source or test mutation has occurred.

### User correction that changed the design horizon

Ali rejected a too-narrow interpretation of proportionality. The corrected principle for this responsibility is:

> Implementation complexity and migration cost are costs to weigh, not vetoes. Prefer the design that is professionally balanced across correctness, supported product breadth, maintainability, migration cost, future repair cost, and proof strength. A higher-cost change is justified when evidence shows that a smaller repair would preserve a weak foundation and likely create more expensive repeated corrections later.

This is consistent with `JUST-003` / proportionality: “simpler” means the simplest design that adequately satisfies the admitted responsibility and proof boundary, not the fewest changed lines today.

### Current source path and ownership trace

The shell-like command proposition is currently established more than once:

```text
GitHub workflow run scalar
→ RunStepDefinition.command.text

→ dependency/workflow_context.bounded_shell_segments(...)
   → direct_install.observe_direct_installation_declaration(...)
   → environment_selection.observe_project_environment_selection(...)

→ ci/workflow_commands._shell_segments(...)
   → project-environment segment-index validation
   → direct package invocation detection / source ordering
```

This matters because `segment_index` is carried across layers as static source identity/order. If dependency observers and CI composition use different segmentation rules, the same integer can refer to different command fragments even when each local parser appears internally correct.

Under Core `JUST-004`, that proposition should have one earliest sufficient owner unless a later layer has an independent reason to reconstruct it.

### Shared dependency segmentation owner

`src/upgradepilot/dependency/workflow_context.py` currently owns:

```python
bounded_shell_segments(command)
```

implemented as a textual split over:

```text
&&
||
;
newline
```

It is deliberately not a shell AST and currently has no quote/comment awareness.

### Direct requirements installation

`src/upgradepilot/dependency/direct_install.py` consumes `bounded_shell_segments(...)`, recognizes a pip-install-looking prefix, then searches the whole candidate segment for `-r` / `--requirement`.

Therefore:

```text
pip install wheel # -r requirements-dev.txt
```

remains one segment, starts like a pip install, and the requirements-file matcher can see the commented `-r` payload. The comment is therefore promoted into positive installation semantics.

Quoted separator data creates a different failure:

```text
echo "note; pip install -r requirements-dev.txt"
```

The textual semicolon split manufactures a second segment beginning with `pip install`, even though the semicolon is quoted data.

### Project-environment selection is affected by the same lexical defect

`src/upgradepilot/dependency/environment_selection.py` also consumes `bounded_shell_segments(...)` before interpreting pip local-project and uv selector commands.

The module uses `shlex.split(..., posix=True)` after a candidate segment is selected, but that does not repair incorrect upstream segmentation and default `shlex.split` comment handling is not a general GitHub Actions shell model.

Consequently shapes such as:

```text
pip install wheel # -e .[dev]
uv sync # --group docs
```

can expose comment payload as meaningful arguments after the segment has already been admitted as a candidate command.

### CI composition duplicates the same textual splitter

`src/upgradepilot/ci/workflow_commands.py` has a separate private `_shell_segments(...)` with the same regex split.

It uses that duplicate for two material responsibilities:

1. validating that externally supplied project-environment evidence references a segment index inside the same static command segmentation;
2. locating direct changed-package invocation and preserving its segment index for same-job ordering/direct-exercise evidence.

Therefore a repair only in dependency `workflow_context.py` could create cross-layer disagreement. The duplicate CI splitter is not an independent semantic owner; it reconstructs the same static segment identity from the same command text.

It also has the same false-positive shape for direct invocation. For example, quoted/comment text containing a separator followed by `pytest ...` can be split into a manufactured segment beginning with `pytest`, which may become false direct-exercise evidence.

### Broader command-control-flow problem discovered after the initial lexical framing

The corrected A horizon also exposes a second class that is not solved merely by quote/comment-aware splitting:

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

The install command can be real source syntax yet not execute. Current runtime correlation is at the GitHub Actions user-defined step level; it can establish that the whole step completed successfully, not that every internal shell command executed successfully.

Current coverage logic can strengthen a supported static consumption when the containing correlated run step is completed/successful. Therefore the design must keep at least these propositions distinct:

```text
real command occurrence exists in static source
≠ command is guaranteed to execute on every successful path
≠ containing GitHub step completed successfully
```

This means the responsibility is broader than fixing regex tokenization. The architecture must provide enough command structure/control-flow classification to prevent step-level runtime success from overclaiming internal-command execution.

### Existing proof surfaces

`tests/test_direct_install_declaration.py` already protects ordinary direct requirements installs, working-directory precedence, dynamic/unresolved paths, a nonmatching requirements file, a simple quoted echo negative case, ordinary multi-segment ordering, and invalid dependency-source paths.

`tests/test_project_environment_selection.py` protects ordinary pip/uv selectors, dynamic/unresolved context, a simple echoed-pip negative, valid multi-segment indices, and malformed quoting.

`tests/test_workflow_dependency_evidence.py` and `tests/test_ci_runtime_correlated_dependency_coverage.py` provide the nearest composition/runtime proof surfaces: static positive consumption/direct-exercise evidence can flow into runtime-correlated CI evidence when the containing step is correlated and successful.

### Shell-dialect boundary

GitHub Actions does not have one universal shell grammar. The provider already preserves explicit step/job/workflow shell fields. Built-in workflow use includes Bash/sh, PowerShell/pwsh, cmd on Windows, Python, and custom shell templates; defaults depend on runner/platform.

A POSIX-only lexical rule therefore cannot be represented as general GitHub Actions command semantics.

### A-1 outcome

The original “Unix-like quote/comment-aware splitter” recommendation is **superseded as too narrow**.

The active design question is now:

> What shared command-analysis architecture gives UpgradePilot a trustworthy, maintainable basis for static command occurrence, ordering/control-flow confidence, and later step-level runtime strengthening across the materially relevant GitHub Actions shell domain, without attempting to execute arbitrary workflow programs?

## A-2 — ARCHITECTURE / OPTION INVESTIGATION — ACTIVE

A-2 must compare credible designs without preferring a smaller change solely because it is cheaper today.

Comparison dimensions:

1. correctness against the confirmed comment/quote failures;
2. ability to distinguish static command occurrence from execution certainty/control-flow;
3. shell-family breadth appropriate to the current product;
4. one shared source of command identity/order across dependency and CI layers;
5. long-term maintainability and future correction cost;
6. dependency/supply-chain/runtime cost;
7. migration impact on existing source contracts such as `segment_index`;
8. ability to fail conservatively on unsupported/ambiguous syntax;
9. testability and source traceability;
10. proportionality relative to UpgradePilot’s maintainer-decision evidence role.

Credible option families to investigate:

### Option family 1 — enhanced handcrafted lexical scanner

A shared in-project scanner/state machine handles quoting, escaping, comments, separators and selected control operators, then emits a bounded internal command representation.

Question: can this remain genuinely bounded and trustworthy, or does multi-shell/control-flow support turn it into an increasingly expensive home-grown parser?

### Option family 2 — shell-specific parsing libraries behind one UpgradePilot command IR

Use maintained parser/grammar implementations for relevant shell families, normalize only the subset UpgradePilot needs into a small internal representation, and keep dependency/CI observers independent of parser-library AST types.

Question: which parser ecosystem has sufficient maturity, Python integration, shell-family coverage, grammar quality, licensing/maintenance characteristics, and error-tolerant behavior to justify the dependency?

### Option family 3 — hybrid parser + conservative analysis

Use parser-backed syntax for shell families where the tooling is strong, plus a small UpgradePilot control-flow/command-analysis layer that determines whether a real command occurrence is unconditional, conditional/uncertain, or unsupported for runtime strengthening.

This is currently the strongest conceptual architecture, but A-2 must establish whether its dependency/complexity cost is justified and what exact shell families should be admitted first.

### Option family 4 — stronger static interpretation plus runtime-command evidence

Instead of relying only on step-level success to strengthen internal command semantics, obtain finer runtime evidence where available (for example logs or other command-level traces) and use static parsing only for source intent/identity.

This may be stronger conceptually but can introduce substantial acquisition/parsing/provenance responsibilities and is outside the current parent plan unless A-2 shows that static-only strengthening cannot be made sufficiently sound. It must be compared, not silently adopted.

### Option family 5 — deliberately narrower positive evidence contract

Reduce the positive static/runtime claim to command shapes whose execution can be established without general control-flow analysis, preserving other real commands as unresolved.

This remains a legitimate fallback, but must be evaluated by lost product coverage and future pressure rather than selected merely for implementation convenience.

## A-3 — JOINT DESIGN DECISION — PENDING

A-3 will happen after A-2 evidence/teaching. Ali and AI will decide together:

- the admitted product responsibility for this cycle;
- the command-analysis architecture;
- supported shell families and how effective shell identity is established;
- the internal representation/ownership boundary;
- treatment of conditional/ambiguous control flow;
- relationship between static command evidence and step-level runtime success;
- dependency/ADR consequences;
- B implementation/proof boundary and stop line.

Only after A-3 will Phase A be marked complete and B become eligible for explicit Build/Implement authorization.

## Learning-by-Doing granularity rule

Ali previously clarified the overall cycle rhythm:

> A→B→C→D→E are the real cycle stages. Do not recursively turn each stage into another elaborate sub-cycle. By default, finish each stage in one or two substantive rounds. Use more only when the situation genuinely demands it or Ali explicitly asks for smaller sub-steps.

A-1/A-2/A-3 are explicitly requested for this consequential design decision and should not become a reusable nested-cycle pattern.

## Stop line

Phase A remains read-only. Do not yet:

- modify product source/tests before A-3 selects the design and Build is explicitly authorized;
- choose an external parser merely because it is feature-rich or educational;
- reject a stronger design solely because migration/dependency cost is higher;
- claim support for a shell family without evidence that its parser/analysis boundary is sound enough;
- treat parser success as proof that a command executed;
- parse runtime logs/artifacts unless A-2/A-3 demonstrate that command-level runtime evidence is required for the selected responsibility;
- combine this responsibility with matrix/reusable-workflow expansion;
- add exact installed-version/wheel semantics;
- redesign Target composition;
- enable a non-abstention maintainer action;
- reopen the closed exact-revision provenance cycle without new regression evidence.

## Current Learning-by-Doing state

```text
Slice: static workflow-command semantic correctness and safe runtime strengthening

A — IN PROGRESS
    A-1 — COMPLETE
        problem/owner horizon reframed; narrow lexical-only repair superseded
    A-2 — ACTIVE
        architecture/tooling/control-flow/shell-family options under investigation
    A-3 — PENDING
        joint decision + formal A closure

B — NOT STARTED
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
