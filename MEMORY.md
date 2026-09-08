# UpgradePilot Current Memory

**Last updated:** 2026-09-08  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** integrate existing artifact-serviceability and target artifact-environment responsibilities through normal `PublicPullRequestInvestigation` and human-facing output while preserving proof strength and mechanism-specific semantics.
- **Mode:** Build/Implement + Learning-by-Doing.
- **Selected plan:** `plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md`.
- **Active working memory:** `working-memory/2026-09-07_2149_target-artifact-environment-composition.md`.
- **Previous execution record:** `working-memory/2026-09-07_1748_artifact-serviceability-candidate-composition.md`.
- **Contract/design record:** `working-memory/2026-09-06_artifact-serviceability-public-investigation-integration-session.md`.
- **Framework status:** bounded ordinary-Python / LangGraph / LangChain investigation is closed for now; re-entry evidence lives in `working-memory/2026-09-06_1853_framework-experiment-deferral-and-core-capability-return.md`.

## Current checkpoint

Plan Slices 1–3 are closed through the canonical A–E Learning-by-Doing cycle at the currently available source/test structural-evidence boundary.

Current implementation state:

```text
result contract                                  → implemented
old release acquisition                          → implemented
artifact-serviceability candidate composition    → implemented
initial unresolved artifact assessment           → implemented
target artifact-environment composition          → implemented for supported direct-requirements relations
exact target compatibility composition           → not admitted from current static evidence
artifact applicability re-evaluation             → not performed; remains unresolved
CLI / human-facing artifact explanation          → not implemented
```

The current application path preserves:

```text
proposed exact PackageReleaseEvidence
→ exact old PackageReleaseResult
→ artifact-serviceability candidate/problem/no-candidate
→ for a real candidate, initial unresolved assessment
→ reuse CI-owned exact workflow definitions
→ select only supported direct-requirements consumption relationships
→ exact join to one RequirementsFileDependencyContext
→ TargetArtifactEnvironmentEvidence | TargetArtifactEnvironmentProblem
→ preserve dependency-source ↔ Target association
```

The first Target-composition gate deliberately excludes unresolved CI relationships and project-environment/uv consumption. It does not create workflow × source cross-products, does not use CI `job_key` to bypass current Target multi-job abstention, and does not manufacture `TargetWheelCompatibilityEvidence` from static runner/Python/install declarations.

## Current proof boundary

Focused source/test work has been committed and diff-inspected for:

- positive/no-candidate/artifact-problem/provider-problem candidate composition;
- independence from unrelated upstream stops;
- supported direct-requirements Target composition;
- no-candidate Target inactivity;
- unresolved CI relation exclusion;
- multi-job Target ambiguity preservation;
- static Target facts leaving exact wheel compatibility/applicability unresolved.

**Executable proof debt:** normal WSL access remains unavailable by user constraint. The typed-contract, candidate-composition, and Target-composition changes are **not executable-proven**. No focused/full PASS claim exists. When WSL access returns, resume from focused investigation tests, then Target/artifact regressions, nearest affected tests, and finally the full deterministic suite according to the plan.

## Slice-3 learning closure and deferred capability re-entry

Slice 3 D/E is complete. The key ownership distinction is:

```text
artifact candidate formation
≠ CI relevance
≠ Target artifact-environment interpretation
≠ exact target wheel compatibility
≠ artifact applicability conclusion
```

Four limitations were preserved as **deferred re-entry candidates, not current blockers**:

1. **Multi-job Target selection** — revisit only if real candidate cases are materially blocked by recurring `ambiguous_target_job_selection`.
2. **uv/project-environment Target formation** — revisit when real repositories make direct-requirements-only Target coverage materially insufficient; reuse existing CI/dependency uv evidence rather than reimplementing it.
3. **Static declaration ↔ runtime execution correlation** — revisit only when a product proposition requires proof that the relevant static install/exercise step itself executed successfully.
4. **Exact target wheel compatibility** — revisit when the product needs to strengthen artifact applicability from `unresolved` to established applicable/not-applicable; broad runner/Python labels are not sufficient evidence.

Detailed reasoning and triggers remain in the active working memory.

## Immediate continuation

The next bounded cycle is plan **Slice 4 — human-facing explanation**.

```text
Slice 4
A — NEXT: inspect `_print_investigation` + current CLI tests and orient the human-facing proof-strength vocabulary
B — pending
C — pending
D — pending
E — pending
```

Slice-4 purpose:

```text
already-earned artifact candidate/problem/no-candidate state
+
Target environment evidence/problem where present
+
unresolved applicability / explicit proof limits
→ concise human-facing explanation
```

The presentation must let a user distinguish observed/established fact, candidate, blocked/unavailable/insufficient evidence, and applicable/not-applicable state **without** inventing an overall maintainer recommendation.

Do not deepen Target/CI, add exact-wheel heuristics, or begin final cross-responsibility proof before the Slice-4 A–E cycle earns those steps.

## Active engineering constraints

- Provider/domain truth stays with its owner; `investigation.py` coordinates rather than reimplementing PyPI, wheel, workflow, Target, or applicability semantics.
- Candidate discovery and target applicability remain separate propositions.
- Static workflow facts do not establish runtime execution or exact target wheel compatibility.
- Supported CI static consumption establishes a workflow/source relationship only at its own proof strength; unresolved relationships are not silently promoted.
- Existing uv/project-environment CI evidence is real but is not rebound into a Target interpreter that does not own that mechanism.
- Presence of an sdist does not prove source-build success or overall installability.
- Artifact-serviceability is mechanism-specific technical evidence, not an overall maintainer recommendation.
- Independently earned CI, Python-support, package, artifact, and Target evidence survives unrelated later stops.
- Repository, PR revision, dependency identity, release versions, workflow source, source path, and Target evidence must remain exactly aligned.
- Deferred local validation is proof debt, never a pass claim.
- Framework experimentation remains deferred until richer real product pressure earns re-entry.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`