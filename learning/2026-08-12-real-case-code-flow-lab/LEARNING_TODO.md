# UpgradePilot Learning TODO

**Broad rules:** [`LEARNING_PLAN.md`](LEARNING_PLAN.md)  
**Latest orientation:** [`2026-08-15_PHASE_E_ONBOARDING_REALIGNMENT.md`](2026-08-15_PHASE_E_ONBOARDING_REALIGNMENT.md)  
**Synchronized product baseline:** `main@1e3027f87fa5b187c7d333472fe849aa6a49b049`  
**Learning-branch sync merge:** `f6b433aa00b4d91d0542632bd4af632fb8b0a786`

## Status

- `[x]` covered
- `[ ]` open
- `▶ CURRENT` recommended current target unless Ali redirects
- `NEXT` likely continuation
- `POSTPONED` intentionally open, not complete
- `WAIT FOR MAIN` implementation not yet present
- `WRITTEN / VALIDATION PENDING` source/tests exist but required validation has not yet completed

Skipped/postponed work stays unchecked. Later work may become current before earlier work is completed.

---

## 0. Learning lab

- [x] Dedicated learning branch/workspace created.
- [x] Broad learning plan written.
- [x] Learning-order override and prerequisite-recovery rule added.
- [x] August 14 synchronization/orientation checkpoint preserved.
- [x] August 15 Phase-E onboarding realignment recorded.
- [x] Re-synced through current `main@1e3027f87fa5b187c7d333472fe849aa6a49b049`.
- [x] Main/live state and separate learning-lab intent reconciled: main may continue implementation; this branch may continue learning because Ali explicitly requested it here.

**Preserved state:** no substantive code-flow lesson was completed before this realignment. Older technical items remain open unless explicitly demonstrated during later work.

---

## 1. Phase-E architecture + Cluster-1/2 onboarding `▶ CURRENT`

Current main state:

```text
✓ Cluster 0 — green baseline
✓ Cluster 1 — PyYAML parser boundary
→ Cluster 2 — typed static workflow IR written; WSL validation pending
```

This learning block does not perform Cluster-2 validation and does not begin Cluster 3. It studies the current code accurately while `main` remains the implementation owner.

### 1A. Why Phase E exists

- [ ] Locate the current Target workflow reader in `target/artifact_environment.py`.
- [ ] Locate the current CI workflow reader in `ci/workflow_commands.py`.
- [ ] Identify provider structure they independently reconstruct.
- [ ] Identify domain meaning that must **not** be shared merely because parsing overlaps.
- [ ] Explain why duplicated provider parsing became more than cosmetic duplication.
- [ ] Explain the proof-strength problem in current Target `dependency_environment_formation` wording.
- [ ] Explain the proof-strength problem in current CI `state="proven"` semantics.

### 1B. Accepted architecture boundary

- [ ] Trace:

```text
RepositoryTextFile
        ↓
bounded GitHub Actions static workflow-definition IR
owner = upgradepilot.github
        ↓
   CI       Target
```

- [ ] Why shared representation belongs to `upgradepilot.github`, not `ci/`, `target/`, or generic `common/`.
- [ ] Why runtime `WorkflowRun` / `WorkflowJob` / `WorkflowStep` remain separate contracts.
- [ ] Why `needs` and source order are structural evidence, not runtime continuity proof.
- [ ] Why valid dynamic values remain readable structure instead of parser failure.
- [ ] Explain: share the lowest layer where meaning is genuinely identical; keep domain conclusions with the responsible consumer.

### 1C. Cluster 1 — PyYAML parser/traversal foundation

- [ ] Why PyYAML was admitted instead of extending custom indentation readers as the shared foundation.
- [ ] `yaml.compose(...)` versus application-object construction at the depth needed here.
- [ ] Why `yaml.BaseLoader` textual scalar preservation matters.
- [ ] `MappingNode`, `SequenceNode`, `ScalarNode` at the depth used here.
- [ ] literal/folded block scalars and `run: |` / `run: >`.
- [ ] source marks.
- [ ] duplicate mapping-pair visibility before dictionary collapse.
- [ ] controlled malformed-YAML failure through `WorkflowYamlParseError`.
- [ ] recursive-alias rejection.
- [ ] bounded depth/node-visit safeguards.
- [ ] PyYAML nodes are private parser machinery, not product/domain contracts.
- [ ] parser safety is proportionate, not a generalized hostile-YAML program.

### 1D. Cluster 2 typed static workflow IR `WRITTEN / VALIDATION PENDING`

Current provider contracts include:

```text
SourceSpan
StaticScalarValue / StaticSequenceValue / StaticMappingValue
RunDefaults
RunStepDefinition / UsesStepDefinition / StepProblem
StepsJobDefinition / ReusableWorkflowJobDefinition / JobProblem
WorkflowDefinition / WorkflowDefinitionProblem
parse_workflow_definition(...)
```

- [ ] Why these are provider-specific static objects rather than YAML objects or CI/Target domain objects.
- [ ] Trace `RepositoryTextFile → parse_workflow_definition(...) → WorkflowDefinition | WorkflowDefinitionProblem`.
- [ ] `StaticScalarValue.text` and `contains_expression`.
- [ ] bounded sequence/mapping preservation for fields such as `needs`, `runs-on`, `strategy`, `container`, and `with`.
- [ ] ordered `source_index` without runtime-order claims.
- [ ] `SourceSpan` and 1-based source locations.
- [ ] `StepsJobDefinition` versus `ReusableWorkflowJobDefinition`.
- [ ] reusable workflow represented without execution/expansion.
- [ ] workflow-level problem versus local `JobProblem` / `StepProblem`.
- [ ] local bad job/step can remain localized while readable siblings survive.
- [ ] duplicate material key / duplicate job-ID handling.
- [ ] expressions preserved rather than evaluated.

### 1E. Workflow-definition tests as executable semantics

Cluster-1 tests:

- [ ] textual scalar/node-shape preservation.
- [ ] block scalar decoding + source marks.
- [ ] duplicate pair visibility.
- [ ] malformed YAML controlled error.
- [ ] recursive alias guard.
- [ ] depth/node-visit guards.

Cluster-2 written regressions:

- [ ] ordered multi-job structure + dynamic values + ordered run/uses steps.
- [ ] workflow/job/step run-default inputs.
- [ ] matrix/strategy and container structure without execution semantics.
- [ ] reusable workflow job preservation without expansion.
- [ ] duplicate job identity → workflow-level problem.
- [ ] local ambiguous job → `JobProblem` while healthy sibling survives.
- [ ] local ambiguous step → `StepProblem` while sibling order survives.
- [ ] malformed YAML / wrong workflow path → typed `WorkflowDefinitionProblem`.
- [ ] source-topology test protects `upgradepilot.github.workflow_definition` as the owner.
- [ ] what these written tests prove structurally.
- [ ] what cannot be called validated/green until the required WSL run succeeds.

### 1F. Cluster-1 dependency-contract regression incident

- [ ] Why adding PyYAML correctly broke the old exact runtime-dependency test.
- [ ] stale contract expectation versus parser/architecture defect.
- [ ] why the repair strengthened rather than weakened the dependency contract.
- [ ] current `pyproject.toml` dependency surface.

### 1G. Boundaries still intentionally open

- [ ] `consumer unresolved != parser failure`.
- [ ] `YAML syntax normalization != GitHub Actions domain interpretation`.
- [ ] `static declaration != runtime execution != runtime success`.
- [ ] multiple jobs structurally readable != consumer proposition resolved.
- [ ] CI and Target not migrated merely because the shared IR exists.
- [ ] direct-install declaration observation remains dependency-owned.
- [ ] package invocation/exercise remains CI-specific.
- [ ] Cluster 2 written != Cluster 2 validated/complete.
- [ ] main's default deep-learning deferral does not block this explicitly requested separate learning-lab session and does not authorize changing main from here.

**Done when:** Ali can explain why Phase E exists, identify the shared-vs-domain boundary, trace the Cluster-1 foundation and current Cluster-2 IR, predict structural result/problem behavior, and state exactly what is written versus what remains unvalidated/unmigrated.

---

## 2. Target Artifact Environment positive flow `POSTPONED / pull prerequisites as needed`

Current pre-migration flow:

```text
RepositoryTextFile
+ dependency source path
→ interpret_target_artifact_environment(...)
→ TargetArtifactEnvironmentEvidence or explicit problem
```

The new shared provider IR does not by itself migrate Target.

- [ ] `RepositoryTextFile` provenance: repository/revision/path/blob.
- [ ] one-job/steps shape in current Target reader.
- [ ] `runs-on` static declaration evidence.
- [ ] `actions/setup-python` literal `python-version` evidence.
- [ ] direct dependency-source installation under current shallow rule.
- [ ] `not_observed` versus established absence.
- [ ] trace one positive focused Target test.
- [ ] explain why exact wheel compatibility remains unresolved.
- [ ] explain why current runtime-sounding formation terminology is scheduled for correction.
- [ ] compare current Target limitations with shared-IR structural readability.

---

## 3. Artifact Serviceability Increment 2 `OPEN`

- [ ] `TargetWheelCompatibilityEvidence` / problem contract.
- [ ] `ArtifactServiceabilityImpactAssessment`.
- [ ] `evaluate_artifact_serviceability_impact(...)`.
- [ ] old published tags ∩ target-supported tags.
- [ ] proposed published tags ∩ target-supported tags.
- [ ] why removed tags alone cannot establish target loss.
- [ ] predict applicable / not applicable / unresolved / identity-rejection cases.

---

## 4. Partial environment → exact wheel compatibility bridge `OPEN`

- [ ] what current `TargetArtifactEnvironmentEvidence` establishes.
- [ ] facts still missing for exact target wheel tags.
- [ ] why local `sys_tags()` is not remote-target evidence.
- [ ] broad Python/platform labels versus exact tags.
- [ ] smallest justified next proposition/evidence step when this responsibility becomes current.

---

## 5. Artifact Serviceability Increment 1 `POSTPONED / pull prerequisites as needed`

- [ ] wheel vs sdist.
- [ ] interpreter / ABI / platform tags.
- [ ] `packaging.tags.Tag` and `parse_wheel_filename(...)`.
- [ ] old/proposed artifact inventory comparison.
- [ ] removed/added tag sets.
- [ ] wheel-ordering parser failure and responsibility-matched validation.

---

## 6. Generic applicability composition `POSTPONED / pull prerequisites as needed`

- [ ] proposition assessment.
- [ ] applicability path assessment.
- [ ] candidate applicability assessment.
- [ ] established/refuted/unresolved/conflicted.
- [ ] evidence coverage vs path-model coverage.
- [ ] path and candidate composition.

---

## 7. Python-support complete reasoning loop `POSTPONED`

- [ ] grounded support-drop claim → impact candidate.
- [ ] pre-investigation applicability.
- [ ] discriminating target-declaration investigation.
- [ ] target Python interpretation/relevance.
- [ ] reevaluation + no-blind-repeat.

---

## 8. PR/evidence foundations `POSTPONED`

- [ ] compact runtime/orchestration map.
- [ ] PR → `PullRequestIdentity` → changed files.
- [ ] `DependencyVersionChange`.
- [ ] exact-head CI evidence.
- [ ] PyPI and upstream evidence.

Teach only required pieces just in time.

---

## 9. Cross-mechanism / cross-responsibility architecture transfer

- [ ] compare Python-support and artifact-serviceability responsibilities.
- [ ] compare CI and Target as separate consumers of shared provider structure.
- [ ] identify genuinely shared concepts.
- [ ] preserve mechanism/domain-specific semantics.
- [ ] explain evidence-earned abstraction.
- [ ] reject one premature generic abstraction using current code evidence.
- [ ] connect ADR-0007 responsibility ownership with ADR-0008 provider ownership.

---

## 10. Remaining Phase-E implementation state

- [ ] Cluster-2 WSL validation and completed/green classification, when main records it.
- [ ] Cluster 3 — shared direct-install declaration observation.
- [ ] Cluster 4 — Target migration/proof-semantic correction.
- [ ] Cluster 5 — CI migration/proof-claim narrowing.
- [ ] Cluster 6 — repository-path ownership reconciliation.
- [ ] Cluster 7 — Tranche-1 acceptance gate.
- [ ] optional Tranche-2 static↔runtime correlation if separately selected and implemented.
- [ ] later heterogeneous mechanism-result handoff/synthesis.
- [ ] recommendation/abstention and traceable output when implemented.

Do not infer later completion from plan order or partial commits.

---

## End-of-session update

- check only demonstrated items;
- keep skipped items open;
- preserve an exact resume point when jumping;
- sync `main` before affected new work;
- distinguish historical checkpoint state from current orientation;
- distinguish architecture intent from written implementation;
- distinguish written implementation from validated completion;
- preserve separation between main execution and learning-branch work;
- choose next by current value + prerequisites + Ali's direction, not checkbox order.
