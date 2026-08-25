# Working Memory — B2 R6 Unresolved Selection Proof-Preservation Fix

**Date:** 2026-08-25  
**Status:** IMPLEMENTED TO STATIC/SOURCE-REVIEW DEPTH; RUNTIME ACCEPTANCE DEFERRED  
**Execution branch:** `main`  
**Parent R6 record:** `2026-08-25_B2-R6-real-workflow-reachability-integration.md`

## Finding

Post-R6 review found a bounded proof-preservation defect in the production seam:

```text
R3 observation = unresolved
→ derive_project_environment_consumptions() skipped it
→ no external project-environment consumption existed
→ CI static classification could fall through to:
   static_dependency_consumption_not_observed
   / not_established
```

That strengthened the evidence incorrectly. R3 deliberately uses `unresolved` for material uncertainty such as a dynamic uv group selector, unsupported package targeting, negative selector interaction, dynamic project paths, or unresolved project discovery. Such uncertainty must not disappear before CI coverage classification.

## Smallest correction

`src/upgradepilot/ci/workflow_commands.py` now distinguishes the three R3 states explicitly:

```text
not_observed
→ contribute no project-environment evidence

unresolved
→ preserve one unresolved StaticDependencyConsumptionEvidence
→ retain exact workflow/job/step/command + dependency source identity
→ do not invoke R4 or project-source membership
→ do not invoke R5 supported/not-established composition

observed
→ unchanged R3 → dependency-domain → R5 path
```

The preservation helper is intentionally local to the R6 workflow-composition seam. R3 selector semantics, R4 reachability semantics, and R5 evidence mapping were not broadened or redesigned.

For unresolved observations, R3 currently reports uncertainty at run-step scope. If it preserved a declaration, its first segment index is retained; otherwise segment zero is used as the existing conservative step-local unresolved placeholder, matching the direct-install unresolved convention.

## Focused regression

`tests/test_r6_project_environment_workflow_integration.py` now includes a GitHub Actions workflow with the valid uv-shaped dynamic selector:

```yaml
- run: uv sync --group "${{ matrix.group }}"
```

Expected flow:

```text
exact workflow text
→ R3 project_environment_selection_unresolved
→ R6 unresolved StaticDependencyConsumptionEvidence
→ CI coverage consumption_state = unresolved
→ overall coverage = unresolved
```

The regression explicitly protects against the former fallback:

```text
static_dependency_consumption_not_observed
```

The existing S001 supported-command regressions remain in the same focused suite, so this correction does not intentionally change positive docs reachability or multi-command preservation.

## Verification status

```text
end-to-end source trace                         COMPLETE
proof-strengthening defect                      CONFIRMED
smallest R6 seam correction                     IMPLEMENTED
focused dynamic-selector regression             IMPLEMENTED
post-write connector source inspection          PASS to static review depth
local focused runtime                           DEFERRED
complete standard suite                         DEFERRED
compileall                                      DEFERRED
```

No runtime PASS is claimed. This correction must be included in the later deferred R3/R4/R5/R6 executable validation gate before R7 acceptance.
