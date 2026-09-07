# UpgradePilot Current Memory

**Last updated:** 2026-09-07  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** integrate the existing artifact-serviceability and target artifact-environment responsibilities through the normal `PublicPullRequestInvestigation` path and human-facing output while preserving proof strength and mechanism-specific semantics.
- **Mode:** Build/Implement + Learning-by-Doing.
- **Selected plan:** `plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md`.
- **Active working memory:** `working-memory/2026-09-06_artifact-serviceability-public-investigation-integration-session.md`.
- **Framework status:** the bounded ordinary-Python / LangGraph / LangChain investigation is closed for now and is not the current implementation target. Detailed disposition and re-entry evidence live in `working-memory/2026-09-06_1853_framework-experiment-deferral-and-core-capability-return.md`.

## Current implementation and proof boundary

The result-contract/evidence-flow decision is complete and the additive typed-contract edit is committed on `main`.

`PublicPullRequestInvestigation` now has application-level places for:

```text
old_package_result
artifact_serviceability_candidate_result
target_artifact_environment_results
artifact_serviceability_impact_result
```

`DependencySourceArtifactEnvironmentResult` preserves the association between one dependency source context and one target artifact-environment result.

The new fields are still inactive/default because the artifact-serviceability orchestration has **not** been implemented yet. In particular:

```text
old release acquisition                         → not implemented
artifact-serviceability candidate composition   → not implemented
target artifact-environment composition         → not implemented
artifact applicability re-evaluation             → not implemented
CLI explanation                                  → not implemented
```

The existing dependency-problem investigation test protects the new inactive defaults, but the focused `tests.test_investigation` family has not yet been executed in Ali's normal WSL control plane after this contract change. That executable proof is the current gate.

Normal project execution topology remains owned by `ENVIRONMENT.md`; the assistant-side sandbox is not the UpgradePilot control plane.

## Immediate continuation

First run the focused proof in the normal WSL checkout:

```bash
cd /home/motafeq/projects/UpgradePilot
git pull --ff-only
source .venv/bin/activate
python -m unittest tests.test_investigation -v
```

Then:

```text
focused proof PASS
→ record the result and close the typed-contract slice
→ begin artifact-serviceability candidate composition

focused proof FAIL
→ diagnose and repair that exact contract/investigation failure
→ rerun before advancing
```

The next implementation slice after a green focused proof is deliberately narrow:

```text
established proposed PackageReleaseEvidence
→ acquire exact old PackageReleaseResult
→ when both releases are evidence, call build_artifact_serviceability_impact_candidate
→ preserve provider problem / no-candidate / evidence-problem / candidate distinctly
→ create an unresolved ArtifactServiceabilityImpactAssessment only when a real candidate exists
```

Do not yet batch target artifact-environment acquisition or CLI rendering into that slice.

## Active engineering constraints

- Exact old/proposed package-release evidence must remain provider-owned; `investigation.py` coordinates rather than reimplementing wheel or PyPI semantics.
- Candidate discovery and target applicability remain separate states.
- Static workflow facts such as runner, Python version, and install declarations do **not** establish exact target wheel compatibility. Current `TargetArtifactEnvironmentEvidence` must not be promoted into `TargetWheelCompatibilityEvidence` without stronger admitted evidence.
- Presence of a proposed source distribution does not prove source-build success or overall installability.
- Artifact-serviceability state is mechanism-specific technical evidence, not an overall maintainer recommendation.
- Independent CI, Python-support, package, and artifact evidence already earned by the investigation must not be erased by a later unrelated stop.
- Repository, pull-request revision, dependency identity, release versions, workflow source, and target evidence must remain exactly aligned across composition.
- Framework experimentation remains deferred until richer real product pressure earns re-entry; the detailed trigger and proof history live in the framework closure working memory rather than here.

## Current evidence pointers

- Active integration reasoning/evidence: `working-memory/2026-09-06_artifact-serviceability-public-investigation-integration-session.md`
- Framework closure/proof inventory: `working-memory/2026-09-06_1853_framework-experiment-deferral-and-core-capability-return.md`
- LangGraph value/cost details: `working-memory/2026-09-06_1810_langgraph-framework-value-cost-findings.md`
- Real LangGraph pydantic proof: `working-memory/2026-09-06_1752_real-pydantic-python-support-langgraph-executable-proof.md`

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
