# UpgradePilot Current Memory

**Last updated:** 2026-09-07  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** integrate the existing artifact-serviceability and target artifact-environment responsibilities through the normal `PublicPullRequestInvestigation` path and human-facing output while preserving proof strength and mechanism-specific semantics.
- **Mode:** Build/Implement + Learning-by-Doing.
- **Selected plan:** `plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md`.
- **Active working memory:** `working-memory/2026-09-07_2149_target-artifact-environment-composition.md`.
- **Previous execution record:** `working-memory/2026-09-07_1748_artifact-serviceability-candidate-composition.md`.
- **Contract/design record:** `working-memory/2026-09-06_artifact-serviceability-public-investigation-integration-session.md`.
- **Framework status:** the bounded ordinary-Python / LangGraph / LangChain investigation is closed for now and is not the current implementation target. Detailed disposition and re-entry evidence live in `working-memory/2026-09-06_1853_framework-experiment-deferral-and-core-capability-return.md`.

## Recent commitment and continuity trail

This section is a compact navigation index across the recent engineering journey. It does not duplicate the detailed reasoning, evidence, or execution history owned by the linked plans and working memories.

### Impact, applicability, and investigation foundation — completed parent/provenance

- Historical parent plan: `plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`.
- This plan established the broader deterministic impact/applicability/investigation responsibility from which the current artifact-serviceability integration was specialized. Completed foundation work is not being reopened without new evidence.

### Bounded EvidenceGapPlanner implementation/comparison — closed for now

- Parent implementation/comparison plan: `plans/BOUNDED_EVIDENCE_GAP_PLANNER_IMPLEMENTATION_COMPARISON_AND_EVALUATION_PLAN.md`.
- Learning-depth/re-entry companion: `plans/BOUNDED_EVIDENCE_GAP_PLANNER_IMPLEMENTATION_COMPARISON_LEARNING_DEPTH_AND_REENTRY_MAP.md`.
- LangGraph bounded implementation/comparison plan: `plans/LANGGRAPH_BOUNDED_EVIDENCE_GAP_PLANNER_INDEPENDENT_DESIGN_IMPLEMENTATION_AND_COMPARISON_PLAN.md`.
- Real LangGraph smoke-build record: `working-memory/2026-09-06_1652_real-pydantic-python-support-langgraph-smoke-build.md`.
- Real LangGraph executable-proof record: `working-memory/2026-09-06_1752_real-pydantic-python-support-langgraph-executable-proof.md`.
- LangGraph value/cost findings: `working-memory/2026-09-06_1810_langgraph-framework-value-cost-findings.md`.
- Framework closure and return-to-core record: `working-memory/2026-09-06_1853_framework-experiment-deferral-and-core-capability-return.md`.
- Current disposition: ordinary Python and LangGraph remain bounded experiment evidence; executable LangChain/product-framework adoption is deferred until materially richer product pressure earns re-entry.

### Semantic responsibility naming reconciliation — completed

- Working memory: `working-memory/2026-09-06_semantic-responsibility-naming-enforcement.md`.
- Current effect: active navigation uses semantic responsibility names; old coordinate-heavy filenames/identifiers remain only where historical provenance requires them.

### Artifact-serviceability public investigation integration — ACTIVE

- Active plan: `plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md`.
- Contract/design record: `working-memory/2026-09-06_artifact-serviceability-public-investigation-integration-session.md`.
- Slice-2 execution/learning record: `working-memory/2026-09-07_1748_artifact-serviceability-candidate-composition.md`.
- Current Slice-3 record: `working-memory/2026-09-07_2149_target-artifact-environment-composition.md`.
- Current checkpoint: Slice 1 and Slice 2 are closed through the canonical A–E Learning-by-Doing cycle. Slice 3 A/B are complete at the structural source/test evidence boundary and C state preservation is being completed. Local executable validation remains intentionally deferred until system access returns and must not be treated as passing evidence.

## Current implementation and proof boundary

`PublicPullRequestInvestigation` exposes:

```text
old_package_result
artifact_serviceability_candidate_result
target_artifact_environment_results
artifact_serviceability_impact_result
```

The application now performs:

```text
proposed exact PackageReleaseEvidence
→ acquire exact old PackageReleaseResult
→ if old evidence exists, delegate to build_artifact_serviceability_impact_candidate
→ preserve evidence-problem / no-candidate / real-candidate distinctly
→ for a real candidate, create initial unresolved ArtifactServiceabilityImpactAssessment
→ reuse CI-owned exact workflow definitions
→ select only supported direct-requirements consumption relationships
→ join each to one exact RequirementsFileDependencyContext
→ interpret Target artifact-environment evidence/problem through its existing owner
→ preserve dependency-source ↔ target-result associations
```

The Target composition gate deliberately excludes unresolved CI relationships and project-environment/uv consumption from this first integration. It does not create a workflow × source cross-product and does not use CI job identity to bypass current Target multi-job abstention semantics.

Current implementation state:

```text
result contract                                  → implemented
old release acquisition                          → implemented
artifact-serviceability candidate composition    → implemented
initial unresolved artifact assessment           → implemented
target artifact-environment composition          → implemented for supported direct-requirements relations
exact target compatibility composition           → not admitted from current static evidence
artifact applicability re-evaluation             → not performed; current assessment remains unresolved
CLI explanation                                  → not implemented
```

Focused integration tests now cover:

- positive candidate formation;
- no-candidate state;
- artifact evidence problem;
- old-release provider problem;
- independence from a later upstream stop;
- supported direct-requirements CI relation producing one exact Target association;
- no-candidate keeping Target composition inactive;
- unresolved direct-requirements CI relation not entering Target composition;
- multi-job Target ambiguity remaining an explicit Target problem despite CI job relevance;
- static Target facts leaving exact wheel compatibility and artifact applicability unresolved.

**Executable proof debt:** system access to the normal WSL control plane is currently unavailable and local execution was explicitly postponed. The typed-contract, candidate-composition, and Slice-3 target-composition changes are source/diff-inspected but **not executable-proven**. The latest source/test commit has no remote commit statuses. Focused and broader tests remain required before final plan closure.

Normal project execution topology remains owned by `ENVIRONMENT.md`; the assistant-side sandbox is not the UpgradePilot control plane.

## Immediate continuation

Follow the canonical A–E Learning-by-Doing cycle defined near the top of `AGENTS.md`.

For current plan **Slice 3 — target artifact-environment and applicability composition**:

```text
A — done: pre-implementation learning + evidence-gated selection decision
B — done, executable proof deferred: source/test composition committed and diff-inspected
C — done: current detailed working memory + this live state reconciled
D — NEXT: post-implementation learning / ownership check
E — then: repair learning gaps + orient the next bounded responsibility
```

Do not begin Slice-4 CLI implementation before Slice-3 D/E are closed unless Ali explicitly redirects.

The current Slice-3 proof model to preserve during D/E is:

```text
supported direct-requirements CI consumption
+
exact matching dependency source
+
exact workflow definition already acquired for CI
→ TargetArtifactEnvironmentEvidence | TargetArtifactEnvironmentProblem

BUT
TargetArtifactEnvironmentResult
≠ TargetWheelCompatibilityEvidence

therefore
artifact applicability remains unresolved
```

When WSL access returns, resume deferred proof beginning with the focused investigation family, then `tests/test_target_artifact_environment.py`, `tests/test_artifact_serviceability.py`, nearest integration/package/CLI tests selected from the actual diff, and finally the full deterministic suite according to the plan.

## Active engineering constraints

- Exact old/proposed package-release evidence remains provider-owned; `investigation.py` coordinates rather than reimplementing wheel or PyPI semantics.
- Candidate discovery and target applicability remain separate states.
- Static workflow facts such as runner, Python version, and install declarations do **not** establish exact target wheel compatibility. Current `TargetArtifactEnvironmentEvidence` must not be promoted into `TargetWheelCompatibilityEvidence` without stronger admitted evidence.
- Supported CI static consumption establishes a workflow/source relationship only at its own proof strength; unresolved CI relationships are not silently promoted into Target associations.
- The first Target-composition gate is intentionally limited to supported `direct_requirements`; supported uv/project-environment consumption remains real CI evidence but is not rebound into a Target interpreter that does not own that mechanism.
- Presence of a proposed source distribution does not prove source-build success or overall installability.
- Artifact-serviceability state is mechanism-specific technical evidence, not an overall maintainer recommendation.
- Independent CI, Python-support, package, artifact, and Target evidence already earned by the investigation must not be erased by a later unrelated stop.
- Repository, pull-request revision, dependency identity, release versions, workflow source, source path, and target evidence must remain exactly aligned across composition.
- Deferred local validation is proof debt, not a pass claim; final plan closure still requires focused, nearest, and full deterministic executable evidence.
- Framework experimentation remains deferred until richer real product pressure earns re-entry; the detailed trigger and proof history live in the framework closure working memory rather than here.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`