# Parent Synthesis — End-to-End Evidence-Path Re-Audit

**Opened:** 2026-09-19, 18:25 (session-local time)  
**Session status:** ACTIVE  
**Primary operation:** cross-responsibility analysis/review (read-only product review)  
**Method:** canonical A → B → C → D → E Learning-by-Doing, composed with repository-audit and working-memory procedures  
**Repository:** `motafegh/UpgradePilot`, `main`; initial observed source head `0201069d91f2d2bc776b84616870fe0926386f3f`; documentary updates thereafter  
**Controlling parent plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Live-state owner:** [`../MEMORY.md`](../MEMORY.md)  
**Technical closure:** [`2026-09-18_cycle3-runtime-strengthening-build.md`](2026-09-18_cycle3-runtime-strengthening-build.md)  
**Parallel learning:** [`2026-09-19_cycle3-integrated-learning-review.md`](2026-09-19_cycle3-integrated-learning-review.md)

## Formal user decision and action boundary

Ali explicitly selected and STARTED the parent evidence-sufficiency and maintainer-action synthesis re-audit as the MAIN workstream on 2026-09-19. Closed Cycle-3 implementation must not be reopened without a demonstrated regression; remaining Cycle-3 integrated learning continues in another conversation independently and is not a main-product continuation gate. Use the product-flow reconstruction itself to learn actual source/types/data/control/evidence flow and learn each relevant gap as it appears, with real tests and representative real cases where available. Preserve important evidence, assumptions, reasoning, surprises, proof limits, decisions, and A/B/C/D/E progress progressively in this record.

**Authorization:** read-only product source/test review and explanation, plus requested working-memory and live-state coordination changes. No source/test, accepted plan/spec/ADR, simulation, or external-target mutation, and no automatic Build admission merely because a review identifies a candidate gap. `MEMORY.md` alone owns the current project position. Root governance/Charter/Operating Guide and accepted synthesis/decision-model specifications remain controlling.

## Session focus (not a second plan)

1. Reconstruct the *actually reachable* PR → application producer → typed investigation → standalone synthesis evaluator → current CLI/report flow, including source contexts, CI/runtime, Target, upstream, impact, conditional investigations, missing/unsupported/failure states, and normal-path coupling. Learn one coherent seam at a time, not a ceremonial file-by-file course.
2. Compare material action-relative prerequisites with real normal producers and composition. Classify each gap as false/misattributed evidence; missing evidence; available-but-lost/miscomposed evidence; deliberate conservative coverage; unimplemented synthesis permission; or operational failure outside typed result. Distinguish source observations from tests and from prior plan hypotheses.
3. Compare only evidence-supported next responsibilities: exact consuming-job → Target integration, precise runtime version/artifact evidence, exact target-wheel compatibility producer, and any newly demonstrated higher-priority gap. Evaluate alternatives, owner, proof, complexity and stopping conditions before selecting one.
4. Use the normal Planning/Design or Build route for any later proposed mutation; do not turn the parent re-audit itself into unapproved implementation.

## Progressive engineering record

### Entry and A — learning/orientation (DONE for first bounded trace)

- Read root governance, Charter, Operating Guide, current MEMORY, parent synthesis plan, accepted synthesis/decision-model specifications, relevant closed Cycle-3 and independent learning records, and Audit/Learning-by-Doing/Working-Memory Skills. Current `main` was `0201069d91f2d2bc776b84616870fe0926386f3f` before our documentary updates.
- Recorded prior hosted technical closure: Cycle 3 focused 76/76 and full deterministic suite 604/604, run `35448172928`. This is historical executable proof, not a fresh test performed in this review and not maintainer-action or update-safety proof.
- Orientation model: source identity/acquisition → dependency/source contexts → CI and Target and upstream/impact producers → typed `PublicPullRequestInvestigation` → *separate* action evaluator → current presentation. Primary learning/ownership responsibility is to trace what is actually joined, what is merely adjacent, and which proposition fails at which owner boundary. Detailed parser internals remain deferred absent contrary evidence.

### B — first real source/test trace (PARTIALLY DONE; further seams in progress)

**1. PR and dependency entry (`src/upgradepilot/investigation.py`, `PublicPullRequestInvestigation` and `investigate_public_pull_request`):** Application calls `get_pull_request` then `get_changed_files` then `analyze_dependency_change`. On an accepted `DependencyChangeAnalysis`, carries `DependencyVersionChange` and exact `source_contexts`; otherwise carries `DependencyChangeProblem` and empty contexts. Only the supported change enters the CI/PyPI/upstream/impact acquisition branches. The result is a typed `PublicPullRequestInvestigation` containing the fields collected, including possible `None`/empty states. Reading the source establishes the control path and typed return; it does not prove all exceptions are converted into that typed result.

**2. CI and Target composition (`investigation.py` and `target/artifact_environment.py`):** For a supported dependency change, acquire exact-head workflow runs/jobs and exact workflow definition; build `WorkflowDependencyCoverageInput` objects with shared dependency source contexts/project-environment sources and evaluate CI dependency coverage. For eligible artifact-serviceability candidate, `_compose_target_artifact_environments` takes CI-supported `direct_requirements` consumptions, checks exact workflow/source-context correspondence, then calls `interpret_target_artifact_environment(definition, dependency_source_file=...)`. It does **not** pass the already established `consumption.job_key` to Target. Target re-parses the static workflow and `_select_target_job` accepts only a workflow with exactly one job; multiple jobs yield `ambiguous_target_job_selection`. **Source-backed candidate composition bottleneck:** an exact supported CI consuming-job identity might not be transferred into Target's independent job selection; compare cases/tests and ownership before classifying a repair or selecting this as the next Build responsibility. This is not evidence that current emitted positive target facts are false.

**3. Investigation → synthesis evaluator (`src/upgradepilot/maintainer_action.py`; `tests/test_maintainer_action.py`):** `MaintainerAction = Literal["abstain"]`; standalone `synthesize_maintainer_action(investigation)` preserves the same `PublicPullRequestInvestigation` and returns reasons, residual uncertainty, limitations and claim limits. Focused tests build fixture investigations (including a synthetic/example repository and a runtime-correlated CI state) and assert abstention; these are contract tests, **not** normal public-PR action-permission integration proof.

**4. Current human CLI/presentation (`src/upgradepilot/cli.py`; `tests/test_cli.py`):** `main` calls `investigate_public_pull_request` then `_print_investigation` and returns exit code 0 for a returned investigation. It does **not** invoke `synthesize_maintainer_action`. Current CLI renders an evidence report, not a maintainer-action report; CLI tests explicitly assert the absence of `Maintainer recommendation` for an artifact case. The typed evaluator exists separately. Classify as **not-yet-integrated synthesis presentation / intentional incomplete product path** under the parent plan, not as proof that action permission should be loosened or that a new CLI feature must be built before the action premise review. Exception branches such as GitHub acquisition/response failures are operational error exits, not automatically typed semantic abstentions.

**5. Preliminary full-path correction:** The initial conceptual flow `investigation → synthesis → CLI` describes the *target product horizon*, not today's normal CLI control path. Current observed shape is `PR → investigation → CLI evidence report`, alongside a separately callable `investigation → abstention-only synthesis evaluator`. Do not silently write those as one already connected normal flow.

**Still unverified:** representative real case through this whole current seam; whether any other public interface invokes the evaluator; targeted CI→Target contrast with multiple jobs and exact job identity; other producer branches and their tests. Do not rank a next implementation direction from this first trace alone.

### C — progressive preservation (DONE for current material checkpoint)

- Created this distinct main workstream record and reconciled `MEMORY.md` to the user-selected main parent re-audit while preserving the Cycle-3 integrated-learning record as a parallel learning owner. The canonical memory was compressed to emphasize live position; detailed closed-cycle history remains in dated records and at prior Git commit `0201069d91f2d2bc776b84616870fe0926386f3f`.
- Recorded the first concrete correction: evaluator and CLI are currently separate, and exact CI job identity is not transferred into Target's independent job selection. These are observed code boundaries and possible product bottlenecks, not approved Build solutions or newly accepted design semantics.

### D — post-action learning / user-owned check (FIRST CHECK COMPLETED; depth bounded)

- First check was initially too early for Ali: he explicitly said he did not remember the CI/Target premises. We repaired the prerequisite by teaching the difference between CI identification of the dependency-consuming job, Target interpretation of declared runner/Python, and the current independent one-job selection rule. The teaching YAML with `test` and `lint` jobs was illustrative/synthetic, not a cited real product-simulation case.
- Ali then correctly predicted `ambiguous_target_job_selection` for two jobs and correctly rejected inferring an exact installed dependency version from successful job completion. His explanation of *why* Target loses the relation was directionally correct but uncertain. Clarified: Target sees the two jobs; its API does not receive the already-supported CI consuming-job identity. This demonstrates understanding of the outcome/non-proof, not yet full independent ownership of the actual source-level handoff or a repair design.
- Key corrected mental model: the proposed transfer is a supported dependency source → declaration → exact workflow job relationship, with workflow/revision coherence checks. Sending an arbitrary job key or equating successful job with installed version is not sufficient.

### E — repair and next-slice orientation (ACTIVE)

- The missing prerequisite was repaired locally without restarting Cycle-3 teaching or selecting Build. Next inspect the specific `consumption.job_key` producer/typed field, exact application use in `_compose_target_artifact_environments`, Target's job selector and nearest test or real case. Distinguish supported `direct_requirements` from unsupported/multiple candidate relationships and from mere runtime-step success. Then return to broader evidence-path reconstruction and action-relative gap comparison.

## Current session handoff

Main product re-audit ACTIVE. First conceptual CI→Target check completed after brief prerequisite repair; `ambiguous_target_job_selection` and installed-version non-proof understood, but actual source-level identity/provenance trace and real-case pressure are still open. Next perform one bounded real source/test trace of the supported CI consuming-job relationship through application to Target. Do not resume Cycle-3 learning here or begin product implementation. No product runtime tests were executed during this review, and no product source/tests/specs/plans were changed.

**Activated procedures:** `UP-SKILL:upgradepilot-repository-audit`; `UP-SKILL:upgradepilot-learning-by-doing`; `UP-SKILL:upgradepilot-working-memory`.
