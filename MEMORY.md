# UpgradePilot Current Memory

**Last updated:** 2026-09-12  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** E-phase gap repair / next-slice orientation for the bounded CI static↔runtime correlation bridge. A/B/C/D are complete; the full current limitation/bottleneck/improvement inventory is now recorded, but no next implementation responsibility has been selected.
- **Mode:** Learning-by-Doing analysis/orientation. Learn and rank the E inventory with Ali before opening a new A→E cycle.
- **Selected parent plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Active working memory:** `working-memory/2026-09-12_ci-static-runtime-correlation-bridge.md`.
- **Previous working memory:** `working-memory/2026-09-11_ci-run-job-attempt-coherence-enhancement.md`.
- **Repository route:** continue directly on `main` unless Ali later requests otherwise.
- **Framework status:** ordinary-Python / LangGraph / LangChain comparison remains closed; no framework re-entry is justified.

## Maintainer-action synthesis state retained

The deterministic maintainer-action evaluator remains abstention-only:

```text
PublicPullRequestInvestigation
→ synthesize_maintainer_action(...)
→ MaintainerActionSynthesis(action="abstain")
```

No merge, targeted-check, investigate, block, or defer permission is implemented. `run targeted checks` remains paused while UpgradePilot first determines what uncertainty its own trustworthy read-only evidence path can resolve.

## Previous CI run/job attempt-coherence cycle — CLOSED

The mixed-rerun-attempt defect is repaired and proven. Exact job acquisition binds:

```text
frozen PR head SHA
+ workflow run ID
+ run attempt
→ jobs from that exact attempt
```

Proof on Ali's WSL environment:

```text
focused provider tests      9  OK
nearest CI/application     31  OK
full deterministic suite  533  OK
```

This issue is retired from the current defect inventory.

## CI static↔runtime correlation bridge — implementation/proof/ownership complete

UpgradePilot now keeps three distinct evidence responsibilities:

```text
STATIC WORKFLOW EVIDENCE
        +
RUNTIME ACTIONS EVIDENCE
        ↓
CI CORRELATION EVIDENCE
        ↓
DEPENDENCY-CI INTERPRETATION
```

The first positive job bridge requires exact workflow/run identity, ordinary non-matrix/non-reusable steps jobs, explicit literal unique static job names, unique runtime job names, and exact static/runtime job-name-set matching. Step correlation then requires explicit literal unique static step names, available runtime steps with unique ordered numbers, one runtime match per static name, and preservation of static step-name order as a runtime subsequence.

Unsupported/ambiguous shapes remain unresolved at the correlation layer rather than guessed.

Correlation establishes identity, not execution meaning. Positive runtime execution interpretation additionally requires:

```text
runtime status == completed
runtime conclusion == success
+ static continue-on-error absent or literal false
```

`src/upgradepilot/ci/dependency_exercise.py` now admits:

```text
supported_runtime_correlated
```

when an already-supported static dependency-consuming run step is safely correlated to an exact-attempt completed-successful runtime step without visible continue-on-error masking.

The previous:

```text
supported_not_correlated
```

remains the fallback when static dependency consumption + successful exact-head CI exist but the bridge cannot safely establish the consuming-step↔runtime-step relation.

Important D distinction:

```text
matrix / unsupported shape
→ correlation result: unresolved
```

but when static consumption and successful exact-head CI still exist:

```text
→ dependency-CI coverage may remain supported_not_correlated
```

The bridge still does not prove exact installed dependency version, selected/downloaded wheel, wheel compatibility, behavioral compatibility, complete CI coverage, proposal safety, or a maintainer action.

## Proof

Added/updated proof assets include:

- `tests/test_workflow_runtime_correlation.py`
- `tests/test_ci_runtime_correlated_dependency_coverage.py`
- `tests/test_maintainer_action.py`

Ali ran narrow-to-broad validation in the real WSL project environment:

```text
focused correlation tests
→ PASS / GREEN

nearest CI / investigation / provider / parser / synthesis regression set
→ PASS / GREEN

full deterministic repository suite
→ Ran 549 tests in 0.144s
→ OK
```

Therefore A/B/C/D for this bridge are closed.

## E inventory — current limitations, bottlenecks, and potential improvements

The inventory is deliberately divided by kind. Listing an item does **not** authorize implementation.

### Confirmed correctness / provenance defects

1. **Static shell/direct-install recognition can produce false-positive dependency consumption.** Bounded command-text splitting can treat text inside comments or certain shell text as real install semantics. The prior controlled reproduction included `pip install wheel # -r requirements-dev.txt` being recognized as requirements consumption. This is now especially important because a false static semantic claim can be correctly correlated to a successful runtime step and thereby become stronger-looking wrong evidence.

2. **Requirements/constraints changed-file patch evidence is not bound to the frozen PR head.** The PR identity freezes a head SHA, but the requirements/constraints path later consumes live changed-file patch data and only checks file count. A PR that moves from head A to head B with the same changed-file count can therefore supply B patch content while the resulting evidence is attributed to A. This is a snapshot/provenance defect upstream of later exact-head reasoning.

### Major evidence / architecture bottlenecks

3. **No normal producer for exact target wheel-compatibility evidence.** The artifact-serviceability evaluator has an exact compatibility evidence concept, but the normal investigation path does not yet produce the exact target wheel-tag witness required to populate it.

4. **Target composition discards an already-known CI `job_key`.** Supported CI consumption knows the exact consuming job, but `_compose_target_artifact_environments()` re-invokes Target on the whole workflow without preserving that job identity; Target can therefore re-enter `ambiguous_target_job_selection` even though CI already established the relevant job. This is an evidence-composition/ownership bottleneck to evaluate under earliest-sufficient-owner reasoning.

5. **No exact runtime dependency-version/artifact witness.** The bridge proves static-step↔runtime-step identity and GitHub status/conclusion, but not exact resolved version, wheel/sdist selection, artifact filename/tags, resolver/install output, or exact runtime target tags. Logs/artifacts are only candidates after a precise missing proposition is selected.

6. **CI acquisition failure containment remains a source-traced resilience risk needing fresh proof.** Current orchestration acquires CI before several independent evidence branches and lacks an obvious typed degradation boundary for every provider exception. Do not call this a confirmed current defect until a fresh discriminating current-main reproduction proves it.

### Deliberate conservative safety / coverage limits — not defects by default

7. The correlation bridge does not yet support matrix/strategy jobs, reusable workflows, dynamic/missing/duplicate names, static/runtime name-set mismatches, missing runtime steps, ambiguous runtime matches, or order defects.

8. Target artifact-environment interpretation remains intentionally narrow around multi-job selection, matrix/strategy, reusable workflows, containers, dynamic runner/setup-python declarations, and exact wheel compatibility.

9. Target composition currently promotes supported `direct_requirements` relationships; supported project-environment/uv/pyproject consumption does not yet receive equivalent Target composition.

10. Dependency analysis intentionally supports a bounded source domain and preserves conflicts/multiple incompatible transitions as explicit problems.

11. Changed-file acquisition has an explicit finite provider bound; low priority absent real case pressure.

### Future product / observability / engineering gaps

12. **Maintainer-action synthesis remains abstain-only.** The wider Charter action space is intentionally not implemented yet.

13. **CLI/reporting does not expose the full runtime-correlation diagnostic surface**, including all runtime consumption/direct-exercise and correlation reason/detail fields.

14. **Full investigation persistence/replay/corpus evaluation is not yet a normal product path.** Current bootstrap JSON contracts are not a durable complete evidence-graph replay facility.

## E priority discipline

No next A→E cycle is selected yet. Learn and rank the inventory with Ali using:

```text
1. Can this issue currently create wrong or misattributed evidence?
2. If not, does it block the next decision-critical proposition?
3. Is it a deliberate conservative limit that is acceptable for now?
4. Is it product/presentation work that can wait?
```

Initial risk signal only, not a selected route:

- shell false-positive recognition and patch/head snapshot mismatch are the two confirmed current correctness/provenance defects;
- exact wheel/runtime-artifact evidence and preservation of the known CI `job_key` into Target are major evidence bottlenecks once correctness is trustworthy;
- matrix/reusable/dynamic-name expansion should not be prioritized merely for completeness;
- the previously fixed rerun-attempt defect remains closed.

## Current canonical Learning-by-Doing cycle

```text
Slice: CI static↔runtime correlation bridge

A — DONE
B — DONE
    full suite: 549 tests OK
C — DONE
D — DONE
E — CURRENT
    full limitation/bottleneck/improvement inventory recorded
    learning + priority selection pending
```

Do not yet implement an inventory item, parse job logs, add exact wheel-serviceability semantics, enable `run targeted checks`, add non-abstention maintainer actions, redesign CLI/reporting, or broaden correlation support merely for completeness.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-build-implement`