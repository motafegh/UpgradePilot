# UpgradePilot Learning TODO

**Broad rules:** [`LEARNING_PLAN.md`](LEARNING_PLAN.md)  
**Latest sync:** [`2026-08-14_MAIN_SYNC_AND_LEARNING_ORIENTATION.md`](2026-08-14_MAIN_SYNC_AND_LEARNING_ORIENTATION.md)  
**Synchronized product baseline:** `main@8c1415e61aab4b16e80bb3f09ba7fb9a77b54ae1`

## Status

- `[x]` covered
- `[ ]` open
- `▶ CURRENT` recommended current target unless Ali redirects
- `NEXT` likely continuation
- `POSTPONED` intentionally open, not complete
- `WAIT FOR MAIN` implementation not yet present

Skipped/postponed work stays unchecked. Later work may become current before earlier work is completed.

---

## 0. Learning lab

- [x] Dedicated learning branch/workspace created.
- [x] Broad learning plan written.
- [x] Learning-order override and prerequisite-recovery rule added.
- [x] Synced with `main@8c1415e61aab4b16e80bb3f09ba7fb9a77b54ae1`.
- [x] 2026-08-14 sync/orientation checkpoint recorded.

**Preserved state:** no substantive code-flow lesson had started before this sync.

---

## 1. Target Artifact Environment positive flow `▶ CURRENT`

Current flow:

```text
RepositoryTextFile
+ dependency source path
→ interpret_target_artifact_environment(...)
→ TargetArtifactEnvironmentEvidence or explicit problem
```

Prerequisites pulled in just-in-time:

- [ ] `RepositoryTextFile` provenance: repository/revision/path/blob.
- [ ] GitHub Actions workflow → jobs → one job → steps.
- [ ] `runs-on` as observed runner evidence.
- [ ] `actions/setup-python` literal `python-version` evidence.
- [ ] direct dependency-source installation as environment-formation evidence.
- [ ] `not_observed` versus established absence.

Main trace:

- [ ] Trace one positive focused test into `interpret_target_artifact_environment(...)`.
- [ ] Follow runner extraction.
- [ ] Follow setup-python version extraction.
- [ ] Follow dependency installation detection.
- [ ] Inspect returned provenance, job scope, facts, limitations, and formation state.
- [ ] Explain why `exact_wheel_compatibility_state` remains `unresolved`.

Boundary transfer:

- [ ] no direct dependency install → `not_observed`.
- [ ] dynamic Python version → preserve partial known facts.
- [ ] multiple/matrix/ambiguous job → explicit problem.
- [ ] weak provenance/unsupported workflow path → explicit problem.
- [ ] explain why runner + Python version is not an exact wheel-tag set.

**Done when:** Ali can predict evidence vs `not_observed` vs problem and explain exactly what the result proves and does not prove.

---

## 2. Artifact Serviceability Increment 2 `NEXT`

```text
ArtifactServiceabilityImpactCandidate
+ TargetWheelCompatibilityEvidence
→ old compatible path?
→ proposed compatible path?
→ candidate applicability
```

- [ ] `TargetWheelCompatibilityEvidence` / problem contract.
- [ ] `ArtifactServiceabilityImpactAssessment`.
- [ ] `evaluate_artifact_serviceability_impact(...)`.
- [ ] old published tags ∩ target-supported tags.
- [ ] proposed published tags ∩ target-supported tags.
- [ ] why removed tags alone cannot establish target loss.
- [ ] predict focused cases: applicable / not applicable / unresolved / identity rejection.

**Done when:** Ali can compute the bounded result from old/proposed inventories plus exact target tag evidence.

---

## 3. Partial environment → exact wheel compatibility bridge `NEXT AFTER 2`

- [ ] List what `TargetArtifactEnvironmentEvidence` actually establishes.
- [ ] Identify facts still missing for exact target wheel tags.
- [ ] Explain why local `sys_tags()` is not remote-target evidence.
- [ ] Explain why broad Python/platform labels are weaker than exact tags.
- [ ] Identify the smallest justified next proposition/evidence step from current project state.

If `main` implements this bridge first, sync and replace this conceptual item with the actual source/test flow.

---

## 4. Artifact Serviceability Increment 1 `POSTPONED / pull prerequisites as needed`

- [ ] wheel vs sdist.
- [ ] interpreter / ABI / platform tags.
- [ ] `packaging.tags.Tag` and `parse_wheel_filename(...)`.
- [ ] old/proposed artifact inventory comparison.
- [ ] removed/added tag sets.
- [ ] wheel-ordering parser failure and responsibility-matched validation.

---

## 5. Generic applicability composition `POSTPONED / pull prerequisites as needed`

- [ ] proposition assessment.
- [ ] applicability path assessment.
- [ ] candidate applicability assessment.
- [ ] established/refuted/unresolved/conflicted.
- [ ] evidence coverage vs path-model coverage.
- [ ] path and candidate composition.

---

## 6. Python-support complete reasoning loop `POSTPONED`

- [ ] grounded support-drop claim → impact candidate.
- [ ] pre-investigation applicability.
- [ ] discriminating target-declaration investigation.
- [ ] target Python interpretation/relevance.
- [ ] reevaluation + no-blind-repeat.

---

## 7. PR/evidence foundations `POSTPONED`

- [ ] compact runtime/orchestration map.
- [ ] PR → `PullRequestIdentity` → changed files.
- [ ] `DependencyVersionChange`.
- [ ] exact-head CI evidence.
- [ ] PyPI and upstream evidence.

These are not mandatory gates for Section 1; teach only required pieces just-in-time.

---

## 8. Cross-mechanism architecture checkpoint

- [ ] compare Python-support and artifact-serviceability responsibilities.
- [ ] identify genuinely shared concepts.
- [ ] preserve mechanism-specific semantics.
- [ ] explain evidence-earned abstraction.
- [ ] reject one premature generic abstraction using current code evidence.

---

## 9. Future work `WAIT FOR MAIN`

- [ ] next implemented step toward exact target wheel compatibility.
- [ ] artifact investigation/stop lifecycle if implemented.
- [ ] later B2 technical handoff/synthesis/evidence sufficiency.
- [ ] recommendation/abstention and traceable output when implemented.

---

## End-of-session update

- check only demonstrated items;
- keep skipped items open;
- preserve an exact resume point when jumping;
- sync `main` before affected new work;
- choose next by current value + prerequisites + Ali's direction, not checkbox order.
