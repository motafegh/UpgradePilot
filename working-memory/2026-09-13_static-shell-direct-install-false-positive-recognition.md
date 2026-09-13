# Static Shell / Direct-Install False-Positive Recognition — Working Memory

**Date:** 2026-09-13  
**Session status:** ACTIVE  
**Primary mode:** Learning-by-Doing + Planning/Design — A orientation/design  
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

## A — investigation/design — IN PROGRESS / FINAL DESIGN DECISION PENDING

A is read-only. No product source or test mutation is authorized by this record.

### Current source path and ownership trace

The shell-like segment proposition is currently established more than once:

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

The module does use `shlex.split(..., posix=True)` after a candidate segment is selected, but default `shlex.split` comment handling is disabled. Consequently shapes such as:

```text
pip install wheel # -e .[dev]
uv sync # --group docs
```

can expose comment payload as arguments after the segment has already been admitted as a candidate command.

This means the correctness responsibility is broader than a local `_REQUIREMENT_PATTERN` repair in `direct_install.py`.

### CI composition duplicates the same textual splitter

`src/upgradepilot/ci/workflow_commands.py` has a separate private `_shell_segments(...)` with the same regex split.

It uses that duplicate for two material responsibilities:

1. validating that externally supplied project-environment evidence references a segment index inside the same static command segmentation;
2. locating direct changed-package invocation and preserving its segment index for same-job ordering/direct-exercise evidence.

Therefore a repair only in dependency `workflow_context.py` could create cross-layer disagreement. The duplicate CI splitter is not an independent semantic owner; it reconstructs the same static segment identity from the same command text.

It also has the same false-positive shape for direct invocation. For example, quoted/comment text containing a separator followed by `pytest ...` can be split into a manufactured segment beginning with `pytest`, which may become false direct-exercise evidence.

### Existing test pressure

`tests/test_direct_install_declaration.py` already protects:

- ordinary direct requirements install;
- working-directory precedence;
- dynamic/unresolved paths;
- a nonmatching requirements file;
- a simple quoted `echo "pip install ..."` negative case;
- ordinary multi-segment ordering;
- invalid dependency-source paths.

It does not yet discriminate comment payload or quoted separator payload failures.

`tests/test_project_environment_selection.py` protects ordinary pip/uv selectors, dynamic/unresolved context, a simple echoed-pip negative, valid multi-segment indices, and malformed quoting. It likewise does not currently prove comment/separator-payload safety.

`tests/test_workflow_dependency_evidence.py` and `tests/test_ci_runtime_correlated_dependency_coverage.py` provide the nearest composition/runtime proof surfaces: static positive consumption/direct-exercise evidence can flow into runtime-correlated CI evidence when the containing step is correlated and successful.

### Shell-dialect boundary discovered in A

GitHub Actions does not have one universal shell grammar. The provider already preserves explicit step/job/workflow shell fields. GitHub's current documented defaults include Bash/sh on non-Windows runners, PowerShell on Windows, plus explicit/custom Bash, sh, pwsh, powershell, cmd, python, and custom shell templates.

Therefore a POSIX/Bash-like lexical rule must not be represented as general GitHub Actions shell semantics.

A must bound the command-recognition domain explicitly. Unsupported or unestablished shell semantics should remain conservative rather than being guessed into positive evidence.

### Standard-library `shlex` assessment

Python `shlex` is useful evidence and may be useful implementation machinery because it supports Unix-shell-like quoting, escapes, and punctuation tokens. It is not a general GitHub Actions shell parser, and its standard comment handling is not an exact model of every Bash comment boundary or any PowerShell/cmd syntax.

A direct `shlex.split(...)` replacement is therefore not by itself a sufficient design.

### Alternatives considered

#### Option 1 — patch only `direct_install.py`

Not selected as the likely design.

It can suppress the two known direct-requirements examples, but it would leave the same lexical failure in project-environment selection and CI direct-invocation recognition. It can also leave segment-index identity inconsistent between dependency and CI layers.

#### Option 2 — direct drop-in replacement with standard-library `shlex`

Not selected as a complete design.

It provides useful POSIX-like lexical machinery but does not establish arbitrary GitHub shell semantics and does not automatically give the exact conservative comment/unsupported-state behavior this responsibility requires.

#### Option 3 — full shell parser / AST dependency

Not justified as the first repair.

It creates additional dependency/maintenance/generalization cost, still requires choosing which shell dialect(s) are supported, and exceeds the currently selected correctness proposition.

#### Option 4 — shared bounded lexical command segmentation

Current leading design.

One shared owner would establish the top-level static command segments used by dependency observers and CI composition. The mechanism would be a deliberately bounded lexical scanner/state machine rather than a full shell AST/execution model.

Within its admitted shell domain it should, at minimum:

- recognize the currently supported top-level separators only when outside quoted/comment payload;
- prevent quoted separators from manufacturing executable segments;
- prevent comment payload from contributing positive command arguments/segments;
- preserve stable segment ordering/indices for downstream composition;
- handle the minimum necessary escaping so escaped separators do not become false boundaries;
- surface malformed or unsupported lexical shapes conservatively instead of guessing;
- be reused by direct-install, project-environment, and CI direct-invocation/segment validation rather than maintaining duplicate splitters.

This is a lexer-level correctness boundary, not a claim to parse or execute shell programs.

### Explicit non-goals / likely unsupported shapes

Unless evidence in the final A decision requires otherwise, this cycle should not attempt general support for:

- arbitrary Bash/POSIX grammar;
- PowerShell/cmd/Python/custom-shell semantics;
- here-documents/here-strings;
- nested command substitution/subshell interpretation;
- pipelines/control structures beyond the currently admitted top-level ordering need;
- variable expansion or runtime command execution semantics.

Those shapes should not be guessed into positive dependency evidence merely to preserve breadth.

### Remaining A decision

One material decision remains before A can close:

```text
Should the first accepted command-recognition boundary explicitly restrict positive lexical interpretation to an admitted Unix-like shell domain, leaving non-admitted/custom/unestablished shells unresolved, rather than attempting Bash + PowerShell + cmd support in this repair?
```

Current evidence favors the conservative Unix-like bounded domain because the active correctness responsibility is to stop false positives, not to universalize shell interpretation. This remains to be confirmed through the Learning-by-Doing ownership/design review before B is proposed.

### Provisional B proof obligations if the design is accepted

Focused proof should discriminate at least:

```text
real direct requirements install
→ remains positive

commented requirement flag
→ cannot become positive

quoted separator + install-looking payload
→ cannot manufacture a positive segment

real multi-segment install
→ remains positive with stable segment ordering

project-environment comment/quoted payload analogues
→ cannot become positive selectors

CI direct-package invocation comment/quoted payload analogues
→ cannot become positive direct exercise

malformed/unsupported admitted-shell lexical shape
→ unresolved/conservative rather than guessed

supported static premise + successful runtime step
→ may still become runtime-correlated

false static premise + successful runtime step
→ must not become runtime-correlated support
```

Nearest focused owners include:

- `tests/test_direct_install_declaration.py`
- `tests/test_project_environment_selection.py`
- `tests/test_workflow_dependency_evidence.py`
- `tests/test_ci_runtime_correlated_dependency_coverage.py`

Then broaden proportionately to nearby CI/investigation regressions and the full deterministic suite.

## Learning-by-Doing granularity rule

Ali explicitly clarified the cycle rhythm on 2026-09-13:

> A→B→C→D→E are the real cycle stages. Do not recursively turn each stage into another elaborate sub-cycle. By default, finish each stage in one or two substantive rounds. Use more only when the situation genuinely demands it or Ali explicitly asks for smaller sub-steps.

Apply this as a proportionality preference, not as a reason to skip material reasoning or proof.

## Stop line

A remains read-only. Do not yet:

- modify product source/tests before the A design is closed and Build is explicitly authorized;
- adopt a general-purpose shell parser merely because shell syntax is complex;
- claim support for arbitrary Bash/POSIX/PowerShell/cmd/custom-shell semantics;
- combine this correction with matrix/reusable-workflow expansion;
- parse runtime logs/artifacts;
- add exact installed-version/wheel semantics;
- redesign Target composition;
- enable a non-abstention maintainer action;
- reopen the closed exact-revision provenance cycle without new regression evidence.

## Current Learning-by-Doing state

```text
Slice: static shell / direct-install false-positive recognition

A — IN PROGRESS
    source/test/owner trace complete
    shared lexical owner is the leading design
    one final shell-domain/ownership decision remains

B — NOT STARTED
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
