# B2 R3 — uv package-scope preservation implementation

**Date:** 2026-08-25  
**Base main:** `1a3f2b3f64daa0a1063577c8970aca1710f3cb1b`  
**State:** R3 IN PROGRESS — implementation/test candidate complete; local runtime validation pending  
**Authority:** dated working evidence only; `MEMORY.md` remains the sole live-state owner.

## Bounded responsibility

R3 preserves the minimum material uv command package scope required by current evidence, beginning with real S001:

```text
uv sync --all-packages --group docs
```

Before R3, `environment_selection.py` retained the explicit `docs` selector but silently discarded `--all-packages`. `uv_membership.py` therefore evaluated one bound project and could in principle return `not_established` even though the real command selected all workspace packages.

The plan requires the asymmetry:

```text
positive witness
→ one sound in-scope root/path may establish reachability

not_established
→ requires exhaustion of the complete root/scope domain claimed by the result
```

R3 must not become a complete uv workspace/config/environment interpreter.

## Selected design

The smallest current producer-owned scope fact is:

```python
type ProjectEnvironmentPackageScope = Literal[
    "bound_project",
    "all_workspace_packages",
]
```

`ProjectEnvironmentSelectionDeclaration` now carries:

```python
package_scope: ProjectEnvironmentPackageScope = "bound_project"
```

Meaning:

```text
bound_project
→ explicit selectors apply to the independently bound project

all_workspace_packages
→ uv explicitly used --all-packages; the selectors have workspace-wide package scope
```

The default preserves existing pip and ordinary uv declarations without creating a separate generic workspace abstraction.

## Producer change

`src/upgradepilot/dependency/environment_selection.py` now:

- preserves `--all-packages` as `package_scope="all_workspace_packages"`;
- preserves ordinary uv/pip selection as `bound_project`;
- continues preserving dependency-group `mode="include" | "only"`;
- leaves unsupported package-targeting scope such as `--package`, `--directory`, and `--no-project` unresolved;
- does not emit a misleading bound-project declaration for those unsupported targeting forms;
- does not add defaults, exclusions, conflicts, package targeting semantics, or complete uv option interpretation.

## Consumer / proof calibration

`src/upgradepilot/dependency/uv_membership.py` consumes the declaration scope without attempting to reconstruct a complete workspace.

For `bound_project`:

```text
bound project explicit roots
→ existing deterministic traversal
→ member | unresolved | not_established
```

For `all_workspace_packages`:

```text
bound project explicit roots contain unconditional witness
→ member
```

because one sound in-scope witness is sufficient.

If those roots do not contain a witness:

```text
all_workspace_packages
+ only bound-project roots exhausted
→ unresolved
  reason = uv_membership_workspace_scope_not_exhausted
```

not `not_established`.

This is deliberate. R3 does not guess the full workspace member set from every editable/virtual lock record because exact workspace membership/discovery can depend on project/workspace configuration and belongs to a broader responsibility than this slice. Guessing would trade a false negative for possible false positives or unsupported scope interpretation.

## Focused regressions

Updated:

- `tests/test_project_environment_selection.py`
- `tests/test_uv_selected_environment_membership.py`

Added:

- `tests/test_uv_package_scope.py`

The focused coverage protects:

- S001-shaped `uv sync --all-packages --group docs` preserving workspace-wide scope;
- ordinary uv selection remaining bound-project scope;
- uv-run option-prefix handling preserving `--all-packages` before the child command;
- unsupported `--package` targeting staying unresolved without a false bound-project declaration;
- S001 positive witness remaining valid under all-workspace scope;
- no-witness all-workspace evaluation returning unresolved rather than false `not_established`;
- an explicit multi-member `[tool.uv.workspace]` fixture where another workspace member has the target root, proving the producer→consumer flow cannot falsely conclude `not_established` after inspecting only the bound project.

## Scope intentionally not pulled forward

R3 does not implement:

```text
complete workspace discovery / member enumeration
workspace globs/excludes
--package targeting semantics
uv default groups
negative selector semantics
conflicts
complete --only-group environment semantics
R4 membership/reachability naming redesign
R5 CI rebinding
lock currentness/resolver/runtime execution
```

`DependencyGroupSelector.mode` remains preserved so later propositions do not erase `--group` versus `--only-group`, but R3 does not build a complete environment interpreter around that distinction.

## Source/diff review

Executable/test change surface from the accepted R2 base is bounded to:

```text
src/upgradepilot/dependency/environment_selection.py
src/upgradepilot/dependency/uv_membership.py
tests/test_project_environment_selection.py
tests/test_uv_selected_environment_membership.py
tests/test_uv_package_scope.py
```

No R4/R5 implementation was intentionally introduced.

## Validation state / next action

Runtime acceptance is not yet claimed. The assistant cannot execute the established local `.venv` through the GitHub connector, so the next evidence must come from the synchronized project environment on Ali's machine.

Required narrow-to-broad validation:

```bash
.venv/bin/python -m unittest \
  tests/test_project_environment_selection.py \
  tests/test_uv_selected_environment_membership.py \
  tests/test_uv_package_scope.py

.venv/bin/python -m unittest discover -s tests -p 'test_uv*.py'
.venv/bin/python -m unittest discover -s tests
.venv/bin/python -m compileall -q src tests
```

If focused runtime exposes a regression, diagnose/fix inside R3 before broadening. R3 remains IN PROGRESS until runtime evidence is green and a final diff/ownership review confirms the bounded scope.
