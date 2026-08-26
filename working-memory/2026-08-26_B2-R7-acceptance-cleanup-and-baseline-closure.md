# Working Memory — B2 R7 Acceptance, Cleanup, and Baseline Closure

**Date:** 2026-08-26  
**Status:** R7 SELECTED; R7.0 RE-ANCHOR COMPLETE; R7.1 NOT STARTED  
**Execution branch:** `main`  
**Current plan:** `../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`

## 1. Purpose of this record

This is the primary progressive execution record for R7. R7 is the acceptance/cleanup/baseline-freeze closure of the R1–R6 reconciliation, not another feature-expansion phase.

Use this one record for ordinary R7 checkpoints:

```text
R7.0 re-anchor
→ R7.1 focused executable acceptance
→ R7.2 normal investigation/CI integration acceptance
→ R7.3 live S001 external verification
→ R7.4 full deterministic suite
→ R7.5 architecture/naming/retention review
→ R7.6 bounded cleanup if justified
→ R7.7 final post-cleanup executable validation
→ R7.8 proof-boundary audit
→ R7.9 audit lifecycle reconciliation
→ R7.10 baseline freeze + mandatory AI/agentic handoff
```

Create a separate dated repair/debug record only if an unexpected failure or design issue becomes substantial enough to need independent reasoning/evidence provenance. Do not create one artifact per routine test command.

The normal Learning-by-Doing-and-Building loop remains active, but proportionately:

```text
small pre-action orientation
→ real bounded work
→ inspect actual evidence
→ preserve material state
→ concise post-action learning closure
→ ownership/reasoning when useful
→ next bounded slice
```

“Smartly” means no ceremonial teaching or redundant recording for familiar routine checks, while new failures, proof-boundary changes, ownership decisions, and cleanup decisions receive enough explanation and evidence to remain understandable later.

## 2. R7.0 exact entry state

R7 was selected after the R7 plan itself was refined.

Exact `main` revision entering R7:

```text
fa12852598a8f687eac6827a296b87c66b7f932f
```

That revision is a planning revision, not new executable authority.

Latest source/test-changing revision before R7 execution:

```text
71df95cb60a0a476dce2ca090de504a77bde1d99
```

The two commits after `71df95cb...` and before R7 execution changed only:

```text
working-memory/2026-08-25_B2-R6-unresolved-selection-proof-preservation-fix.md
plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md
```

Therefore:

```text
source/test tree at 71df95cb...
=
source/test tree at fa128525...
```

for the R3–R6 executable responsibilities under R7 acceptance. This does **not** mean that tree is accepted; it only identifies the exact executable candidate whose deferred validation now begins in R7.

### Revision semantics to retain

```text
R7 ENTRY REVISION
fa128525...
→ exact repository HEAD when R7 was selected
→ includes the refined R7 plan

PENDING EXECUTABLE CANDIDATE
71df95cb...
→ latest source/test mutation in the R3–R6 chain
→ not yet R7 accepted

future ACCEPTED EXECUTABLE REVISION
→ exact final post-cleanup code/test revision that passes final deterministic validation

future CLOSURE REVISION
→ possible later audit/memory/docs-only commit
→ must not be mislabeled as newly execution-tested
```

## 3. Latest R6 corrective slice reconciled into R7

The original R6 production integration was followed by one bounded proof-preservation correction.

Observed defect:

```text
R3 selection = unresolved
→ R6 derivation seam skipped it
→ no project-environment consumption evidence
→ CI static classification could fall through to not_established
```

Correction now implemented in `src/upgradepilot/ci/workflow_commands.py`:

```text
R3 not_observed
→ no project-environment evidence

R3 unresolved
→ unresolved StaticDependencyConsumptionEvidence
→ preserve exact workflow/job/step/command + dependency source identity
→ do not invoke R4 / project-source membership / R5 positive-or-negative composition

R3 observed
→ existing R3 → dependency-domain relation → R5 path
```

Focused regression pressure uses the admitted dynamic uv-shaped selector:

```yaml
- run: uv sync --group "${{ matrix.group }}"
```

Required result:

```text
project_environment_selection_unresolved
→ unresolved CI consumption
→ unresolved coverage consumption state

NOT
→ static_dependency_consumption_not_observed / not_established
```

This correction is implemented and source-reviewed, but **not runtime accepted yet**.

## 4. Executable model entering R7

The normal R6 production route to validate is:

```text
public PR
→ dependency analysis + typed changed-dependency source context
→ exact admitted PR-head workflow runs
→ exact workflow definition for each admitted run
→ exact project/lock evidence required by the changed-dependency context
→ ci/workflow_commands.py
   → every readable local run step
   → R3 project selection
   → R4 uv selected-root reachability OR separate project-source membership
   → R5 static CI consumption
   → preserve all resulting consumptions
→ evaluate_dependency_ci_coverage(...)
→ application/CLI result surface
```

Important retained proof boundaries:

```text
dependency transition
!= selected-root reachability
!= project-source membership
!= static selection
!= static consumption
!= direct exercise
!= runtime execution/success
!= exact-version runtime witness
!= resolver/currentness
!= behavioral compatibility/safety/action
```

and:

```text
one changed package may have zero, one, or multiple supported CI selection commands
supported summary evidence != unique correct command
R3 unresolved != absence != not_established
conditional candidate != reachable
all-workspace no complete negative domain != not_established
```

## 5. Runtime/acceptance state at R7 entry

R2 already has accepted runtime evidence from its completed acceptance gate.

R3, R4, R5, and R6—including the post-R6 unresolved-selection correction—remain pending executable acceptance.

At R7.0:

```text
focused R3 runtime acceptance                     PENDING
focused R4 runtime acceptance                     PENDING
focused R5 runtime acceptance                     PENDING
focused R6 workflow/integration acceptance         PENDING
unresolved-selection preservation regression       IMPLEMENTED / NOT RUN
nearest dependency/CI/application integration      PENDING
live S001 verifier                                 IMPLEMENTED / NOT RUN
full deterministic standard suite                  PENDING
compile/static checks required by current owners   PENDING
R7 retention/cleanup review                        NOT STARTED
R7 proof-boundary audit                            NOT STARTED
```

No R3/R4/R5/R6 runtime PASS is claimed by this re-anchor.

## 6. R7.0 non-proof

R7.0 establishes state and execution identity only.

It does **not** prove:

- that the focused R3–R6 tests pass;
- that the normal R6 production path executes successfully;
- that the live S001 verifier succeeds today;
- that the complete deterministic suite is green;
- that current transitional surfaces should be retained or removed;
- that no additional proof-strengthening issue remains;
- that R7 is accepted.

## 7. Current next bounded slice

R7.1 — focused R3–R6 executable acceptance.

Before running it, load only the current environment/test-command facts needed for reproducible execution, then use the narrowest meaningful test groups covering:

```text
R3 selector/scope + unresolved states
R4 reachability + workspace completeness + conditional candidates
R5 CI consumption calibration
R6 real workflow derivation + multiple matches + unresolved preservation + S011/S005 transfer boundaries
```

If a focused failure appears:

```text
failure
→ stop broad progression
→ form strongest supported hypothesis
→ run discriminating check
→ smallest repair only if established
→ rerun focused gate
→ record evidence
```

Do not begin R7.2 until R7.1 is green.

## 8. Post-R7 mandatory handoff remains unchanged

Successful R7 acceptance activates:

```text
plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md
```

That AI/agentic checkpoint must reach an explicit evidence-backed disposition before old Cluster 6 or another ordinary B2 expansion becomes live work.
