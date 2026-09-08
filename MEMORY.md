# UpgradePilot Current Memory

**Last updated:** 2026-09-08  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** integrate existing artifact-serviceability and target artifact-environment responsibilities through normal `PublicPullRequestInvestigation` and human-facing output while preserving proof strength and mechanism-specific semantics.
- **Mode:** Build/Implement + Learning-by-Doing.
- **Selected plan:** `plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md`.
- **Active working memory:** `working-memory/2026-09-08_artifact-serviceability-cli-rendering.md`.
- **Previous Slice-3 record:** `working-memory/2026-09-07_2149_target-artifact-environment-composition.md`.
- **Previous Slice-2 record:** `working-memory/2026-09-07_1748_artifact-serviceability-candidate-composition.md`.
- **Contract/design record:** `working-memory/2026-09-06_artifact-serviceability-public-investigation-integration-session.md`.
- **Framework status:** bounded ordinary-Python / LangGraph / LangChain investigation is closed for now; re-entry evidence lives in `working-memory/2026-09-06_1853_framework-experiment-deferral-and-core-capability-return.md`.

## Current checkpoint

Plan Slices 1–4 are closed through the canonical A–E Learning-by-Doing cycle at the currently available source/test structural-evidence boundary.

Current implementation state:

```text
result contract                                  → implemented
old release acquisition                          → implemented
artifact-serviceability candidate composition    → implemented
initial unresolved artifact assessment           → implemented
target artifact-environment composition          → implemented for supported direct-requirements relations
exact target compatibility composition           → not admitted from current static evidence
artifact applicability re-evaluation             → not performed; remains unresolved
CLI / human-facing artifact explanation          → implemented at typed proof strength
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
→ render artifact/Target/applicability state through CLI without inventing stronger evidence
```

## Current CLI presentation boundary

The terminal distinguishes:

```text
old package artifact evidence
→ not evaluated | provider problem | available

artifact candidate
→ not evaluated | not observed | evidence problem | established

Target artifact environment
→ not activated | not established from selected CI relationships | evidence | explicit Target problem

artifact applicability
→ not evaluated | typed applicability state

exact target wheel compatibility
→ not established | typed problem | available
```

For an established candidate, the CLI shows removed/added wheel-tag capability **counts**, proposed source-distribution availability, Target provenance/facts/limitations, and applicability proof strength. It deliberately does not dump full wheel-tag inventories and does not print an overall maintainer recommendation.

The CLI remains presentation-only: provider/domain/application orchestration stays outside `cli.py`, and focused CLI tests patch the investigation function with constructed typed results.

## Slice-4 learning closure

Slice 4 D/E is complete.

The key presentation-model ownership points are:

```text
candidate=None
→ meaning depends on whether exact old/proposed release prerequisites were established

TargetArtifactEnvironmentEvidence
→ may establish runner/Python/install declaration
→ does NOT establish the exact target-supported wheel-tag set

therefore
artifact applicability may correctly remain unresolved
```

Ali correctly identified the contextual meaning of `None` and the need for concise human-readable CLI output. The remaining gap was repaired: exact artifact applicability requires target-supported wheel-tag evidence strong enough to compare against old/proposed published wheel tags; broad Target labels do not establish that proposition.

## Current proof boundary

Focused source/test work has been committed and diff-inspected for:

- positive/no-candidate/artifact-problem/provider-problem candidate composition;
- independence from unrelated upstream stops;
- supported direct-requirements Target composition;
- no-candidate Target inactivity;
- unresolved CI relation exclusion;
- multi-job Target ambiguity preservation;
- static Target facts leaving exact wheel compatibility/applicability unresolved;
- artifact CLI rendering for inactive, no-candidate, evidence-problem, established-candidate, Target-evidence, Target-problem, and unresolved-applicability states;
- explicit absence of raw wheel-tag dumps and maintainer-recommendation presentation in the focused CLI case.

**Executable proof debt:** normal WSL access remains unavailable by user constraint. The typed-contract, candidate-composition, Target-composition, and CLI changes are **not executable-proven**. No focused/full PASS claim exists. The latest Slice-4 source/test commit has no remote commit statuses.

When WSL access returns, resume according to Slice 5 from the narrowest focused tests through the full deterministic suite.

## Deferred capability re-entry from Slice 3

These remain deferred candidates, not current blockers:

1. **Multi-job Target selection** — revisit only if real candidate cases are materially blocked by recurring `ambiguous_target_job_selection`.
2. **uv/project-environment Target formation** — revisit when real repositories make direct-requirements-only Target coverage materially insufficient; reuse existing CI/dependency uv evidence rather than reimplementing it.
3. **Static declaration ↔ runtime execution correlation** — revisit only when a product proposition requires proof that the relevant static install/exercise step itself executed successfully.
4. **Exact target wheel compatibility** — revisit when the product needs to strengthen artifact applicability from `unresolved` to established applicable/not-applicable; broad runner/Python labels are not sufficient evidence.

## Immediate continuation

The next bounded cycle is plan **Slice 5 — cross-responsibility and end-to-end proof**.

```text
Slice 5
A — NEXT: re-orient on the accumulated diff and exact proof obligations
B — pending: execute focused → nearest → full deterministic validation on the normal WSL control plane
C — pending
D — pending
E — pending
```

Slice-5 A should establish exactly what must be validated and in what order, without pretending the assistant-side sandbox or absent remote statuses are equivalent to the project control plane.

Current planned proof sequence remains:

```text
focused CLI + investigation tests
→ tests/test_artifact_serviceability.py
→ tests/test_target_artifact_environment.py
→ nearest affected package/interface/integration tests selected from actual diff
→ full deterministic suite
→ safe live read-only proof only if a product claim requires it and the environment permits it
```

Do not close the integration plan until the required executable proof exists or the remaining proof debt is explicitly carried forward by an authorized project decision.

## Active engineering constraints

- Provider/domain truth stays with its owner; `investigation.py` coordinates rather than reimplementing PyPI, wheel, workflow, Target, or applicability semantics.
- CLI rendering consumes typed state; it does not manufacture evidence or recommendation semantics.
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
