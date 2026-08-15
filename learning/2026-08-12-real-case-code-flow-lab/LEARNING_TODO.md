# UpgradePilot Learning TODO

**Broad rules:** [`LEARNING_PLAN.md`](LEARNING_PLAN.md)  
**Latest orientation:** [`2026-08-15_PHASE_E_ONBOARDING_REALIGNMENT.md`](2026-08-15_PHASE_E_ONBOARDING_REALIGNMENT.md)  
**Synchronized product baseline:** `main@54ce69082b0d74ec0412b05264dfae897f970d47`  
**Learning-branch sync merge:** `4bedb554174a8300f6b39233b2446c9049fb87e5`

## Status

- `[x]` covered
- `[ ]` open
- `▶ CURRENT` recommended current target unless Ali redirects
- `NEXT` likely continuation
- `POSTPONED` intentionally open, not complete
- `WAIT FOR MAIN` implementation not yet present
- `SOURCE PRESENT / LIVE COMPLETION PENDING` source/tests exist but live validated completion has not yet been recorded by the owning project state/evidence

Skipped/postponed work stays unchecked. Later work may become current before earlier work is completed.

---

## 0. Learning lab

- [x] Dedicated learning branch/workspace created.
- [x] Broad learning plan written.
- [x] Learning-order override and prerequisite-recovery rule added.
- [x] August 14 synchronization/orientation checkpoint preserved.
- [x] Initial August 15 Phase-E onboarding realignment recorded.
- [x] Re-synced after new Cluster-2 source/test commits landed, through `main@54ce69082b0d74ec0412b05264dfae897f970d47`.

**Preserved state:** no substantive code-flow lesson was completed before this realignment. Older technical items remain open unless they are explicitly demonstrated during later work.

---

## 1. Phase-E architecture + Cluster-1/2 onboarding `▶ CURRENT`

Current source progression:

```text
existing duplicated shallow GitHub Actions readers
        ↓
accepted ADR-0008 architecture
        ↓
Cluster 1 PyYAML parser/traversal foundation
        ↓
new typed bounded GitHub Actions static workflow IR source/tests
```

Important status distinction at this snapshot:

```text
Cluster-2 source/tests are present
!= Cluster 2 is yet recorded as completed/green in MEMORY.md
```

### 1A. Why Phase E exists

- [ ] Locate the current Target workflow reader in `target/artifact_environment.py`.
- [ ] Locate the current CI workflow reader in `ci/workflow_commands.py`.
- [ ] Identify the provider structure they independently parse.
- [ ] Identify the domain meaning that must **not** be shared merely because parsing overlaps.
- [ ] Explain why duplicated provider parsing became more than cosmetic duplication.
- [ ] Explain the proof-strength problem exposed by current Target `dependency_environment_formation` wording.
- [ ] Explain the proof-strength problem exposed by current CI `state="proven"` semantics.

### 1B. Accepted architecture boundary

- [ ] Trace the intended dependency direction:

```text
RepositoryTextFile
        ↓
bounded GitHub Actions static workflow-definition IR
owner = upgradepilot.github
        ↓
   CI       Target
```

- [ ] Explain why the shared representation belongs to `upgradepilot.github`, not `ci/`, `target/`, or generic `common/`.
- [ ] Explain why runtime `WorkflowRun` / `WorkflowJob` / `WorkflowStep` remain separate contracts.
- [ ] Explain why `needs` and source order are structural evidence, not runtime continuity proof.
- [ ] Explain why valid dynamic values should remain readable structure rather than parser failure.
- [ ] Explain the rule: share the lowest layer where meaning is genuinely identical; keep domain conclusions with the responsible consumer.

### 1C. Cluster 1 — PyYAML parser/traversal foundation

- [ ] Why PyYAML was admitted instead of continuing custom indentation readers as the shared foundation.
- [ ] `yaml.compose(...)` versus ordinary application-object construction at the depth needed here.
- [ ] Why `yaml.BaseLoader` preserving textual scalar values matters.
- [ ] `MappingNode`, `SequenceNode`, and `ScalarNode` at the depth used by current code.
- [ ] YAML literal/folded block scalars and why `run: |` / `run: >` matter.
- [ ] Source marks and what later extraction/diagnostics use them for.
- [ ] Why duplicate mapping pairs must remain visible before ordinary dictionary collapse.
- [ ] Controlled malformed-YAML failure through `WorkflowYamlParseError`.
- [ ] Recursive-alias rejection.
- [ ] Bounded depth and node-visit safeguards.
- [ ] Explain why PyYAML node objects are private parser machinery, not UpgradePilot evidence/domain contracts.
- [ ] Explain why parser safety is proportionate rather than a generalized hostile-YAML program.

### 1D. New typed static workflow IR `SOURCE PRESENT / LIVE COMPLETION PENDING`

Current provider source now includes:

```text
SourceSpan
StaticScalarValue / StaticSequenceValue / StaticMappingValue
RunDefaults
RunStepDefinition / UsesStepDefinition / StepProblem
StepsJobDefinition / ReusableWorkflowJobDefinition / JobProblem
WorkflowDefinition / WorkflowDefinitionProblem
parse_workflow_definition(...)
```

- [ ] Explain why these are provider-specific static objects rather than YAML objects or CI/Target domain objects.
- [ ] Trace `RepositoryTextFile → parse_workflow_definition(...) → WorkflowDefinition | WorkflowDefinitionProblem`.
- [ ] Explain `StaticScalarValue.text` and `contains_expression`.
- [ ] Explain bounded preservation of sequence/mapping structure for fields such as `needs`, `runs-on`, `strategy`, `container`, and `with`.
- [ ] Explain ordered `source_index` on jobs/steps without treating source order as runtime order.
- [ ] Explain `SourceSpan` as source-location evidence/diagnostic support.
- [ ] Distinguish `StepsJobDefinition` from `ReusableWorkflowJobDefinition`.
- [ ] Explain why reusable workflows are represented but not executed/expanded.
- [ ] Distinguish workflow-level problems from local `JobProblem` / `StepProblem`.
- [ ] Explain why a local bad job/step can be preserved without destroying readable siblings.
- [ ] Explain duplicate material key / duplicate job-id handling before semantic collapse.
- [ ] Explain why dynamic expressions are preserved rather than evaluated.

### 1E. Current workflow-definition tests as executable semantics

Cluster-1 parser-boundary tests remain relevant:

- [ ] textual scalar/node-shape preservation.
- [ ] block scalar decoding + source marks.
- [ ] duplicate mapping-pair visibility.
- [ ] malformed YAML controlled error.
- [ ] recursive alias guard.
- [ ] depth/node-visit guards.

New IR regressions:

- [ ] ordered multi-job structure + dynamic values + ordered run/uses steps.
- [ ] workflow/job run-default preservation.
- [ ] matrix/strategy and container structure preservation without execution semantics.
- [ ] reusable-workflow job preservation without expansion.
- [ ] duplicate job identity → workflow-level problem.
- [ ] local ambiguous job → `JobProblem` while healthy sibling survives.
- [ ] local ambiguous step → `StepProblem` while sibling order survives.
- [ ] malformed YAML / wrong workflow path → typed `WorkflowDefinitionProblem`.
- [ ] explain what these tests prove and what they still do **not** prove about CI/Target/runtime behavior.

### 1F. Dependency-contract regression incident

- [ ] Explain why adding PyYAML correctly broke the old exact runtime-dependency test.
- [ ] Distinguish stale contract expectation from parser/architecture defect.
- [ ] Explain why the repair strengthened rather than weakened the runtime dependency contract.
- [ ] Read the current `pyproject.toml` runtime dependency surface.

### 1G. Boundaries still intentionally open

- [ ] Explain `consumer unresolved != parser failure`.
- [ ] Explain `YAML syntax normalization != GitHub Actions domain interpretation`.
- [ ] Explain `static declaration != runtime execution != runtime success`.
- [ ] Explain why multiple jobs may be structurally readable while Target/CI still cannot safely answer their own proposition.
- [ ] Explain why CI and Target are not migrated merely because the shared IR now exists.
- [ ] Explain why direct-install declaration observation remains a separate dependency-owned responsibility.
- [ ] Explain why package invocation/exercise remains CI-specific.
- [ ] Distinguish source/test implementation presence from validated cluster completion/live continuation.

**Done when:** Ali can explain why Phase E exists, identify the shared-vs-domain boundary, trace the Cluster-1 parser foundation and the current typed IR, predict structural result/problem behavior for changed workflow shapes, and state precisely what the current source/tests prove and do not prove.

---

## 2. Target Artifact Environment positive flow `POSTPONED / pull prerequisites as needed`

Current pre-migration flow:

```text
RepositoryTextFile
+ dependency source path
→ interpret_target_artifact_environment(...)
→ TargetArtifactEnvironmentEvidence or explicit problem
```

This remains current implemented consumer behavior at this snapshot. The new shared provider IR does not by itself migrate Target.

Prerequisites pulled in just-in-time:

- [ ] `RepositoryTextFile` provenance: repository/revision/path/blob.
- [ ] GitHub Actions workflow → jobs → steps.
- [ ] `runs-on` as static declaration evidence.
- [ ] `actions/setup-python` literal `python-version` declaration evidence.
- [ ] direct dependency-source installation declaration under the current shallow rule.
- [ ] `not_observed` versus established absence.

Main trace:

- [ ] Trace one positive focused test into `interpret_target_artifact_environment(...)`.
- [ ] Follow runner extraction.
- [ ] Follow setup-python version extraction.
- [ ] Follow dependency installation detection.
- [ ] Inspect returned provenance, job scope, facts, limitations, and current formation state.
- [ ] Explain why `exact_wheel_compatibility_state` remains `unresolved`.
- [ ] Explain why current runtime-sounding formation terminology is scheduled for semantic correction in Phase E.

Boundary transfer:

- [ ] no direct dependency install → `not_observed`.
- [ ] dynamic Python version → preserve partial known facts.
- [ ] multiple/matrix/ambiguous job → current explicit problem.
- [ ] distinguish current Target consumer limitation from shared-provider structural readability.
- [ ] weak provenance/unsupported workflow path → explicit problem.
- [ ] explain why runner + Python version is not an exact wheel-tag set.

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

- [ ] List what current `TargetArtifactEnvironmentEvidence` establishes.
- [ ] Identify facts still missing for exact target wheel tags.
- [ ] Explain why local `sys_tags()` is not remote-target evidence.
- [ ] Explain why broad Python/platform labels are weaker than exact tags.
- [ ] Identify the smallest justified next proposition/evidence step from current project state.

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

These are not mandatory gates for Section 1; teach only required pieces just-in-time.

---

## 9. Cross-mechanism / cross-responsibility architecture transfer

- [ ] compare Python-support and artifact-serviceability responsibilities.
- [ ] compare CI and Target as separate consumers of one provider-specific static structure.
- [ ] identify genuinely shared concepts.
- [ ] preserve mechanism/domain-specific semantics.
- [ ] explain evidence-earned abstraction.
- [ ] reject one premature generic abstraction using current code evidence.
- [ ] reconnect ADR-0007 responsibility ownership with ADR-0008 shared-provider ownership.

---

## 10. Remaining Phase-E work

- [ ] Cluster-2 validated/green completion state, when the owning live/evidence records establish it.
- [ ] Cluster 3 — shared direct-install declaration observation.
- [ ] Cluster 4 — Target migration/proof-semantic correction.
- [ ] Cluster 5 — CI migration/proof-claim narrowing.
- [ ] Cluster 6 — repository-path ownership reconciliation.
- [ ] Cluster 7 — Tranche-1 acceptance gate.
- [ ] optional Tranche-2 static↔runtime correlation if separately selected and implemented.
- [ ] later heterogeneous mechanism-result handoff/synthesis.
- [ ] recommendation/abstention and traceable output when implemented.

Do not infer later completion from source order, plan order, or partial commits.

---

## End-of-session update

- check only demonstrated items;
- keep skipped items open;
- preserve an exact resume point when jumping;
- sync `main` before affected new work;
- distinguish historical checkpoint state from current orientation;
- distinguish intended architecture from source/test implementation;
- distinguish source/test implementation from validated/live completion;
- choose next by current value + prerequisites + Ali's direction, not checkbox order.
