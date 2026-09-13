# Static Shell / Direct-Install False-Positive Recognition — Working Memory

**Date:** 2026-09-13  
**Session status:** ACTIVE  
**Primary mode:** Learning-by-Doing — A orientation/design  
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

The defect is not that UpgradePilot lacks a complete shell interpreter. The correctness problem is narrower: current bounded command-text segmentation can manufacture an install-looking segment from text that shell syntax would keep inside a comment or quoted payload, allowing static dependency consumption to be promoted incorrectly.

## Current source pressure confirmed at E handoff

### Shared bounded segmentation

`src/upgradepilot/dependency/workflow_context.py` currently owns:

```python
bounded_shell_segments(command)
```

with a textual split over:

```text
&&
||
;
newline
```

The helper explicitly says it is not a shell AST. It currently has no quote/comment awareness.

### Direct requirements installation

`src/upgradepilot/dependency/direct_install.py` iterates `bounded_shell_segments(step.command.text)`, then recognizes pip-install-looking segments and `-r/--requirement` paths.

This is the directly confirmed false-positive path.

### Nearby shared consumer

`src/upgradepilot/dependency/environment_selection.py` also iterates `bounded_shell_segments(step.command.text)` before interpreting pip/uv project-environment selectors.

Therefore A must not assume the correction belongs only in `direct_install.py`. The next design responsibility is to determine whether the earliest sufficient owner is:

```text
shared bounded shell segmentation
vs
one or more narrower observers
```

and to select the smallest sound mechanism without accidentally claiming full shell semantics.

## Existing focused proof pressure

`tests/test_direct_install_declaration.py` already protects ordinary direct requirements installs, working-directory precedence, dynamic/unresolved paths, a nonmatching requirements file, a simple quoted `echo "pip install ..."` negative case, and ordinary multi-segment ordering.

The known defect requires discriminating cases beyond that existing simple echo test, especially comment payloads and quoted separator payloads that the current regex splitter can fragment into install-looking segments.

A should inspect the closest tests for every materially affected shared consumer before deciding the implementation/proof surface.

## A — next responsibility

A should establish, in one or two substantive rounds unless evidence demands more:

1. the exact false-positive classes that are inside the admitted correction;
2. the earliest sufficient owner for shell-segment recognition;
3. whether the shared helper can be made sound enough without introducing a full shell parser or falsely supporting multiple shell dialects;
4. what existing positive behavior must remain unchanged;
5. the smallest focused proof set that discriminates the real defect;
6. the explicit non-claims/unsupported shell shapes that should remain conservative.

Useful current source owners to inspect first:

- `src/upgradepilot/dependency/workflow_context.py`
- `src/upgradepilot/dependency/direct_install.py`
- `src/upgradepilot/dependency/environment_selection.py`
- `src/upgradepilot/ci/workflow_commands.py`
- `tests/test_direct_install_declaration.py`
- nearest project-environment/workflow-command tests if shared ownership is selected.

## Learning-by-Doing granularity rule

Ali explicitly clarified the cycle rhythm on 2026-09-13:

> A→B→C→D→E are the real cycle stages. Do not recursively turn each stage into another elaborate sub-cycle. By default, finish each stage in one or two substantive rounds. Use more only when the situation genuinely demands it or Ali explicitly asks for smaller sub-steps.

Apply this as a proportionality preference, not as a reason to skip material reasoning or proof.

## Stop line

At this handoff, A is read-only. Do not yet:

- modify product source/tests before the A design is sufficiently resolved and Build is authorized;
- adopt a general-purpose shell parser merely because shell syntax is complex;
- claim support for arbitrary Bash/POSIX/PowerShell/cmd semantics;
- combine this correction with matrix/reusable-workflow expansion;
- parse runtime logs/artifacts;
- add exact installed-version/wheel semantics;
- redesign Target composition;
- enable a non-abstention maintainer action;
- reopen the closed exact-revision provenance cycle without new regression evidence.

## Current Learning-by-Doing state

```text
Slice: static shell / direct-install false-positive recognition

A — NEXT / NOT YET DESIGNED
    current source pressure and known failure shape re-anchored

B — NOT STARTED
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
