# Working Memory — B2 R7 Acceptance, Cleanup, and Baseline Closure

**Date:** 2026-08-26  
**Status:** R7 SELECTED; R7.0 RE-ANCHOR COMPLETE; R7.1 REMOTE SOURCE/TEST AUDIT NEXT  
**Execution branch:** `main`  
**Current plan:** `../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`

## 1. Purpose and execution mode

This is the primary progressive execution record for R7. R7 closes the R1–R6 reconciliation; it is not another feature-expansion phase.

On 2026-08-26 Ali clarified the R7 execution mode:

```text
R7.0–R7.8
→ work fully remotely against GitHub main
→ source/test/commit/diff/real-case/ownership/proof review
→ implement justified cleanup remotely
→ NO local runtime acceptance claims

R7.9
→ after all remote work is finished
→ pull exact frozen main candidate locally
→ run the final validation bundle once

R7.10
→ record accepted executable baseline + handoff
```

Therefore local testing is deliberately **not** interleaved with R7 remote building/review. If the final local gate fails, preserve its exact output, return to the smallest owning remote R7 slice, repair on GitHub, refreeze the candidate, and rerun the required local gate.

Use this one record for ordinary R7 checkpoints:

```text
R7.0  exact entry-state re-anchor
R7.1  remote focused R3–R6 source/test contract audit
R7.2  remote normal investigation/CI orchestration trace
R7.3  remote real-case GitHub evidence pressure
R7.4  architecture/naming/retention review
R7.5  bounded remote cleanup
R7.6  remote post-cleanup source/diff + proof-boundary audit
R7.7  audit lifecycle reconciliation
R7.8  freeze final remote candidate + local validation bundle
R7.9  final local pull + executable validation
R7.10 accepted baseline freeze + mandatory AI/agentic handoff
```

The Learning-by-Doing-and-Building loop remains active proportionately:

```text
small orientation
→ real bounded remote work
→ inspect actual evidence
→ preserve material state
→ concise post-action learning closure
→ ownership/reasoning when useful
→ next bounded slice
```

“Smartly” means no ceremonial teaching or redundant recording for familiar review actions. New failures, proof-boundary changes, ownership decisions, cleanup decisions, and the final runtime gate receive enough explanation/evidence to remain understandable later.

## 2. R7.0 exact entry state

R7 was selected after the R7 plan itself was refined.

Exact `main` revision entering R7:

```text
fa12852598a8f687eac6827a296b87c66b7f932f
```

That revision is a planning revision, not executable authority.

Latest source/test-changing revision before R7 execution:

```text
71df95cb60a0a476dce2ca090de504a77bde1d99
```

The two commits after `71df95cb...` and before R7 execution changed only:

```text
working-memory/2026-08-25_B2-R6-unresolved-selection-proof-preservation-fix.md
plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md
```

Therefore the R3–R6 executable source/test tree was unchanged across those later documentation/planning commits. This identifies the pending implementation tree; it does **not** accept it.

R7.0 completion/live-state commits later moved `main` again through documentation-only changes. Those later SHAs also do not become executable authority merely by being newer.

### Revision semantics now used by R7

```text
R7 ENTRY REVISION
→ exact repository HEAD when R7 began

REMOTE CANDIDATE REVISION
→ final code/test SHA after all remote R7 review/cleanup
→ not yet runtime accepted

ACCEPTED EXECUTABLE REVISION
→ exact remote candidate SHA after R7.9 local deterministic validation passes

CLOSURE REVISION
→ possible later audit/memory/docs-only SHA
→ not newly execution-tested
```

## 3. Latest R6 corrective slice carried into R7

Post-R6 review found:

```text
R3 selection = unresolved
→ R6 derivation seam skipped it
→ no project-environment consumption evidence
→ CI static classification could fall through to not_established
```

The implemented correction in `src/upgradepilot/ci/workflow_commands.py` is:

```text
R3 not_observed
→ no project-environment evidence

R3 unresolved
→ unresolved StaticDependencyConsumptionEvidence
→ preserve workflow/job/step/command + dependency-source identity
→ do not invoke R4 / project-source membership / R5 positive-or-negative composition

R3 observed
→ existing R3 → dependency-domain relation → R5 flow
```

Focused regression pressure uses:

```yaml
- run: uv sync --group "${{ matrix.group }}"
```

Required semantics:

```text
project_environment_selection_unresolved
→ unresolved CI consumption
→ unresolved coverage consumption state

NOT
→ static_dependency_consumption_not_observed / not_established
```

This correction remains pending the final R7.9 local runtime gate. Until then we may establish only source/test-contract evidence around it.

## 4. Executable model under remote R7 review

Normal production route:

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
   → preserve every resulting consumption
→ evaluate_dependency_ci_coverage(...)
→ application/CLI result surface
```

Retained proof boundaries:

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

## 5. R7 execution state after remote-first correction

```text
R7.0 exact state re-anchor                                  COMPLETE
R7.1 remote focused R3–R6 source/test contract audit       NEXT / NOT STARTED
R7.2 remote normal investigation/CI orchestration trace     NOT STARTED
R7.3 remote real-case GitHub evidence pressure              NOT STARTED
R7.4 architecture/naming/retention review                   NOT STARTED
R7.5 bounded remote cleanup                                 NOT STARTED
R7.6 remote post-cleanup source/diff + proof audit          NOT STARTED
R7.7 audit lifecycle reconciliation                        NOT STARTED
R7.8 final remote candidate + local bundle freeze           NOT STARTED
R7.9 final local pull + executable validation               DEFERRED UNTIL R7.8
R7.10 accepted baseline + mandatory handoff                 NOT STARTED
```

Runtime status remains:

```text
focused R3 runtime acceptance                     PENDING R7.9
focused R4 runtime acceptance                     PENDING R7.9
focused R5 runtime acceptance                     PENDING R7.9
focused R6 runtime acceptance                     PENDING R7.9
unresolved-selection regression runtime            PENDING R7.9
nearest dependency/CI/application integration      PENDING R7.9
complete deterministic standard suite              PENDING R7.9
compile/static executable checks                   PENDING R7.9 as required
```

No R3/R4/R5/R6 runtime PASS is claimed during the remote-only phase.

## 6. R7.1 next bounded slice

R7.1 now means **remote focused source/test contract audit**, not local execution.

Inspect together the current source and focused deterministic tests protecting:

```text
R3
- selectors/package scope
- literal --all-packages
- unsupported/dynamic selection → unresolved

R4
- direct/transitive selected-root reachability
- workspace negative-proof asymmetry
- conditional candidate remains unresolved

R5
- uv reachability vs project-source membership mapping
- static consumption != direct exercise/runtime
- not_established scope guard

R6
- real workflow text → R3 → R4/project-source → R5
- multiple matching commands preserved
- irrelevant commands non-positive
- R3 unresolved preservation
- S011 separation
- S005 mediated boundary
```

The questions are:

```text
Does source implement the intended proposition?
Do focused tests actually protect that proposition?
Is any required R3–R6 case missing or only manually fabricated around the production responsibility?
Does any test assertion accidentally encode stronger proof than source is allowed to claim?
```

If a source/test gap is found, repair it remotely and inspect the resulting GitHub diff. Do **not** interrupt the remote sequence merely to run local tests.

R7.2 begins only after this source/test contract set is coherent to remote review depth.

## 7. Final local validation principle

At R7.8, after all remote executable work is finished, freeze one exact candidate and one exact validation bundle.

Expected final shape:

```text
git pull/sync exact main
→ clean worktree + exact candidate SHA
→ focused R3–R6 regressions
→ nearest dependency/CI/application integration regressions
→ complete deterministic standard suite
→ compile/static checks required by repository procedure
→ any still-required live verifier
```

Ali runs that final bundle locally in R7.9. The exact output becomes acceptance evidence. A failure reopens remote work; it does not authorize a local-only patch.

## 8. Post-R7 mandatory handoff

Only successful R7.9 executable validation allows R7.10 to accept the baseline and activate:

```text
plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md
```

That checkpoint must reach an explicit evidence-backed disposition before old Cluster 6 or another ordinary B2 expansion becomes live work.
