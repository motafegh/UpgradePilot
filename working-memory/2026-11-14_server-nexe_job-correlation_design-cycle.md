# server-nexe job-level CI correlation investigation

**Opened:** 2026-11-14
**Scope:** Decide whether the exact Linux install step in server-nexe PR #62 can be safely correlated despite a skipped sibling job. Ali selected this investigation as the next cycle. [Previous repair](2026-11-14_ci-aggregate-explanation_build-cycle.md#e--closure) · [Maintainer-task plan](../plans/PRODUCT_DIRECTION_AND_MAINTAINER_UTILITY_INVESTIGATION_PLAN.md#task-first-reassessment-after-delivered-reports)

## Cycle status

- **A0 — DONE.** Fetched origin and reconciled local and remote main at `19fba76c` before documentation. Matched six retained server-nexe input and baseline digests to S019. Reproduced `supported_not_correlated` and the badge job's `runtime_step_match_missing` using checkout code in an isolated network namespace. Checked the workflow correlator, its consumers and the nearby missing/ambiguous match tests.
- **A1 — CURRENT.** The case contrasts ApplyPilot's missing evidence about the relevant step with server-nexe's available evidence about a relevant step in a workflow with an unmatched sibling. Continuity discussion is open.
- **A2 — PENDING.** Orient the proposed job-scoped investigation and what would falsify it.
- **B — PENDING.** Perform the retained-input comparison and decide whether a justified Build exists.
- **Verification — PENDING.** Inspect the exact attempt evidence, negative controls and implications for report and runtime consumers.
- **D — PENDING.** Teach from the observed round trip and decision.
- **E — PENDING.** Resolve or defer remaining questions and record the next selected responsibility.
- **C — CONTINUOUS.** Preserve evidence and meaningful decisions here.

## Orientation map

**A1 — Where the current system stops.** In the frozen `pull_request` run `32646873500`, attempt 1, all six job records match PR head `f1d2aea121eeb6e2abbc0b3fd151804207c4ca6e`. The Linux Unit Tests job `97212373207` lists successful install and test steps 4 and 5. The same attempt lists the Update Coverage Badge job as skipped with zero steps, and the exact workflow restricts it to pushes to main. The current correlator establishes the ordinary workflow's job-name bijection and then requires every static user step in every job to match. The missing badge checkout step makes it return an unresolved workflow result. The existing coverage state still preserves static consumption. This is a retained-input baseline and does not establish installed psutil identity or a Windows result. [S019 evidence](../product-simulation/scenarios/S019-server-nexe-psutil-skipped-sibling/README.md) · [Workflow correlator](../src/upgradepilot/ci/workflow_runtime_correlation.py#L64)

**A2 — What a possible repair must prove.** Determine whether one exact Linux job and its step can keep a trustworthy match while the badge job remains skipped. Keep revision, event, run, attempt, job-name uniqueness and step-order proof. Check how partial results would reach the current runtime execution and report consumers, which expect workflow-scoped correlation. Compare the smallest credible job-scoped design against the existing full match. Include target-job missing or ambiguous evidence as refusal controls. Keep matrix expansion, package/runtime identity and maintainer usefulness as separate questions. Use retained sources as data. A successful design check selects a possible Build and its proof. An ambiguous match earns unresolved. [Evidence semantics](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md#92-declarationconfiguration-evidence-is-not-execution-evidence)

Provenance: `UP-SKILL:upgradepilot-planning-design`, `UP-SKILL:upgradepilot-learning-by-doing`, `UP-SKILL:upgradepilot-working-memory`.
