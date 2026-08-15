# UpgradePilot Learning TODO

**Broad rules:** [`LEARNING_PLAN.md`](LEARNING_PLAN.md)  
**Latest orientation:** [`2026-08-15_PHASE_E_ONBOARDING_REALIGNMENT.md`](2026-08-15_PHASE_E_ONBOARDING_REALIGNMENT.md)  
**Synchronized product baseline:** `main@89d2b845647a7159cb276cbb38c0cdea0608d8af`  
**Learning-branch sync merge:** `6e53c7a6c50dfa42e7cb1a26bc083040bdf0f996`

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
- [x] August 14 synchronization/orientation checkpoint preserved.
- [x] Synced with `main@89d2b845647a7159cb276cbb38c0cdea0608d8af` through merge `6e53c7a6c50dfa42e7cb1a26bc083040bdf0f996`.
- [x] August 15 Phase-E onboarding realignment checkpoint recorded.

**Preserved state:** no substantive code-flow lesson was completed before the Phase-E realignment. Older technical items remain open unless they are explicitly demonstrated during later work.

---

## 1. Phase-E architecture + Cluster-1 onboarding `▶ CURRENT`

Current product checkpoint:

```text
existing duplicated shallow GitHub Actions readers
        ↓
accepted ADR-0008 architecture
        ↓
Cluster 1 PyYAML parser/traversal boundary
        ↓
future typed static workflow-definition IR
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

### 1C. Cluster 1 — PyYAML parser/traversal boundary

Current implemented slice:

```text
untrusted workflow YAML text
→ yaml.compose(..., Loader=yaml.BaseLoader)
→ PyYAML representation nodes
→ controlled parse failure
→ bounded recursive-alias / depth / node traversal validation
```

- [ ] Why PyYAML was admitted instead of continuing the custom indentation readers as the shared foundation.
- [ ] `yaml.compose(...)` versus ordinary object construction at the depth needed here.
- [ ] Why `yaml.BaseLoader` preserving textual scalar values matters.
- [ ] `MappingNode`, `SequenceNode`, and `ScalarNode` at the depth used by current code.
- [ ] YAML literal/folded block scalars and why `run: |` / `run: >` matter.
- [ ] Source marks and what future diagnostics/extraction may use them for.
- [ ] Why duplicate mapping pairs must remain visible before ordinary dictionary collapse.
- [ ] Controlled malformed-YAML failure through `WorkflowYamlParseError`.
- [ ] Recursive-alias rejection.
- [ ] Bounded depth and node-visit safeguards.
- [ ] Explain why PyYAML node objects are private parser machinery, not UpgradePilot evidence/domain contracts.
- [ ] Explain why parser safety is proportionate rather than a generalized hostile-YAML program.

### 1D. Cluster-1 tests as executable semantics

- [ ] Trace `test_base_loader_preserves_text_and_node_shapes`.
- [ ] Trace `test_block_scalars_are_yaml_decoded_and_keep_source_marks`.
- [ ] Trace duplicate-key visibility test.
- [ ] Trace malformed-YAML controlled-error test.
- [ ] Trace recursive-alias guard test.
- [ ] Trace depth/node-visit limit test.
- [ ] Explain what this focused suite proves.
- [ ] Explain what it does **not** prove about GitHub Actions semantics.

### 1E. Dependency-contract regression incident

- [ ] Explain why adding PyYAML correctly broke the old exact runtime-dependency test.
- [ ] Distinguish stale contract expectation from parser/architecture defect.
- [ ] Explain why the repair strengthened rather than weakened the runtime dependency contract.
- [ ] Read the current `pyproject.toml` runtime dependency surface.

### 1F. Current boundaries before Cluster 2

- [ ] Explain why the typed static workflow-definition IR does not exist yet.
- [ ] Explain `consumer unresolved != parser failure`.
- [ ] Explain `YAML syntax normalization != GitHub Actions domain interpretation`.
- [ ] Explain `static declaration != runtime execution != runtime success`.
- [ ] Explain why multiple jobs may be structurally readable while Target/CI still cannot safely answer their own proposition.
- [ ] Explain what Cluster 2 is expected to add conceptually without implementing it.

**Done when:** Ali can explain why Phase E exists, identify the exact shared-vs-domain boundary, trace Cluster 1 source/tests, predict parser success versus controlled failure for changed YAML shapes, and state precisely what Cluster 1 proves and does not prove.

---

## 2. Target Artifact Environment positive flow `POSTPONED / pull prerequisites as needed`

Current pre-migration flow:

```text
RepositoryTextFile
+ dependency source path
→ interpret_target_artifact_environment(...)
→ TargetArtifactEnvironmentEvidence or explicit problem
```

This is still real implemented behavior, but ADR-0008/Phase E has already identified it as a consumer that will later migrate away from its local shallow workflow parser. Study it now when it helps explain the Phase-E contrast, or return to it deeply after the current onboarding block.

Prerequisites pulled in just-in-time:

- [ ] `RepositoryTextFile` provenance: repository/revision/path/blob.
- [ ] GitHub Actions workflow → jobs → one job → steps.
- [ ] `runs-on` as observed static runner declaration evidence.
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
- [ ] distinguish current consumer limitation from future shared-parser readability.
- [ ] weak provenance/unsupported workflow path → explicit problem.
- [ ] explain why runner + Python version is not an exact wheel-tag set.

**Done when:** Ali can predict current evidence vs `not_observed` vs problem, explain exactly what the old Target slice proves/does not prove, and distinguish its current consumer limitations from the future provider parser boundary.

---

## 3. Artifact Serviceability Increment 2 `NEXT AFTER RELEVANT PREREQUISITES`

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

## 4. Partial environment → exact wheel compatibility bridge `OPEN`

- [ ] List what current `TargetArtifactEnvironmentEvidence` actually establishes.
- [ ] Identify facts still missing for exact target wheel tags.
- [ ] Explain why local `sys_tags()` is not remote-target evidence.
- [ ] Explain why broad Python/platform labels are weaker than exact tags.
- [ ] Identify the smallest justified next proposition/evidence step from current project state.

If `main` implements this bridge first, sync and replace this conceptual item with the actual source/test flow.

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

## 10. Future Phase-E work `WAIT FOR MAIN / DO NOT PRETEND IMPLEMENTED`

- [ ] Cluster 2 — typed bounded GitHub Actions static workflow IR, after implementation actually resumes and lands.
- [ ] Cluster 3 — shared direct-install declaration observation.
- [ ] Cluster 4 — Target migration/proof-semantic correction.
- [ ] Cluster 5 — CI migration/proof-claim narrowing.
- [ ] Cluster 6 — repository-path ownership reconciliation.
- [ ] Cluster 7 — Tranche-1 acceptance gate.
- [ ] optional Tranche-2 static↔runtime correlation if separately selected and implemented.
- [ ] later heterogeneous mechanism-result handoff/synthesis.
- [ ] recommendation/abstention and traceable output when implemented.

Study of intended responsibilities may occur for orientation. Do not check implementation-learning items until corresponding implementation truth exists and is actually learned.

---

## End-of-session update

- check only demonstrated items;
- keep skipped items open;
- preserve an exact resume point when jumping;
- sync `main` before affected new work;
- distinguish historical checkpoint state from current orientation;
- distinguish intended architecture from implemented behavior;
- choose next by current value + prerequisites + Ali's direction, not checkbox order.
