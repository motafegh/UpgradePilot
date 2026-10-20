# Retained CI comparison: limited additional information, no product-value verdict

Both frozen rows completed once. The HTTPX case adds no material CI information over the baseline. The glyphsLib case adds useful specificity about static workflow intent and unresolved runtime proof. That supports a bounded consumer-design question; it does **not** demonstrate a better maintainer action, independent usefulness, a native producer defect, or a reason to build a multi-role architecture.

This is a source-aware review by the same AI implementer, with exposed cases and known historical results. The frozen [rubric and source spans](freeze.json) preceded the [raw outputs](execution/results.json); the raw outputs remain unchanged with their original pending-review markers. This document and [review overlay](review.json) carry the later adjudication.

| Case at the October observation horizon | Restricted baseline | Retained native CI | Information-value judgment |
| --- | --- | --- | --- |
| HTTPX 0.27.2 → 0.28.1, PR #20 | B02, `run_targeted_checks`; no passing CI conclusion available. Literal caution matches: removed, deprecated, deprecation; B02 takes precedence | No workflows returned by the exact-head query; no admitted runtime-state candidate | **No material addition** in this component. Both locate the missing current observation. Neither selects a repository-specific check or establishes API compatibility |
| glyphsLib pytest 9.0.2 → 9.0.3, PR #1145 | B05, `merge_after_normal_review`; patch/direct/passing/no caution matches. CVE/fixed/bug fix matches do not change its action. It explicitly does not know whether CI exercised the dependency | Regression workflow has supported static installation/invocation declarations; exact runtime correlation remains unresolved. Both admitted command-state assessments remain unresolved at manager environment. Main Test + Deploy consumption is unresolved | **Limited useful specificity**: the generic exercise uncertainty is located at particular workflow/commands and evidence boundaries. No demonstrated action change or user benefit; baseline is not adjudicated wrong |

## What the source review establishes

Inputs are the same exact October 16 freeze/revisions declared before execution. Successful reconstruction establishes retained typed values and integrity, not a fresh CI evaluation. The native producer semantic-version marker remains unavailable. All 17 original indexed members and exact 96-file product-source correspondence revalidate before and after; the decoder used private owned copies.

HTTPX: the retained PR response and changed `requirements.txt` support the exact transition. Its captured exact-head workflow query has `total_count=0` and an empty run list. The result means the query returned no runs at that observation time. It does not erase the separate July simulation's CI evidence, establish that CI never ran, or prove anything about the installed FastAPI/Starlette/HTTPX relationship. The CI component supplies no caller/callee/API analysis.

glyphsLib: the changed `requirements-dev.txt` supports the pytest transition. The captured query contains two completed successful runs at head `f3cda8a94600e58d27f1bc17c99b7693718b6350`, IDs `24378200511` and `24378200519`. Attempt-specific job responses preserve successful test jobs and a skipped deploy job. Those facts do not independently establish installation or pytest step execution.

The regression definition at that exact revision declares two environments: `generate` for known-good test-file generation, and `regression` for the later checkout/test route. Its first checkout explicitly names `main`; the later checkout omits `ref`. The final test command activates `regression` and invokes pytest with `--run-regression-tests`. These are **static declarations**, not observations that the changed pytest version executed. In particular, do not assign the proposed requirement version to the earlier known-good checkout merely because the workflow file was captured at the proposed head.

The native aggregate's first runtime correlation blocker is the lack of an explicit static job display name. The source review adds an important limit: **every captured job's `steps` array is empty**, including the regression job `test`. Even admitting a job-name fallback would not create absent step evidence. Existing [correlation code](../../../src/upgradepilot/ci/workflow_runtime_correlation.py) requires matching runtime step summaries; [command execution](../../../src/upgradepilot/ci/runtime_execution.py) requires a correlated successful, unmasked command boundary. This review did not invoke either evaluator, test a new fallback, or infer why the API returned empty arrays.

Both native command-state assessments preserve `manager_environment_needs_lower_source_evidence`. That is an **unresolved admitted proof**, not evidence that pip selected the wrong environment. An activation command provides static intent; it does not supply every environment/configuration/executable premise required by the current command-completion proof family. This comparison neither validates that family against runtime reality nor selects its expansion.

Source identities for this review (decoded retained content, not freshly fetched):

| Source | SHA256 / observation |
| --- | --- |
| Regression workflow `.github/workflows/regression.yml` | `8ce672e72f10d1f7cfbe8727cf5808d6b0263fb3b4350f9bfc1f9fdfff4b3d89` |
| Test + Deploy workflow `.github/workflows/ci.yml` | `af09f984d02ffbf27b394eed97269c2b6ac779e7a712d89adf3aa38e48058811` |
| Attempt 1 regression job response | Job `71195942011`, name `test`, success, empty steps |
| Attempt 1 main workflow jobs response | Six jobs, all empty steps; five successful, deploy skipped |

These workflow hashes also match the definitions inside the newly retained full native projection. Public source responses and private projection payload identities are bound by the freeze/results; no original payload is copied into this packet.

## Comparison dimensions and fair credit

1. **Action:** unavailable. The baseline emits an action; this CI component does not synthesize one. Do not infer a product abstention, label the baseline's glyphsLib action wrong, or claim action superiority from an unresolved native assessment.
2. **Reasoning:** HTTPX adds no decisive reason. glyphsLib separates workflow success, supported static intent, and unestablished runtime execution/environment. Its facts are more specific than the baseline's deliberately generic limitation.
3. **Uncertainty:** the HTTPX gap is unchanged. glyphsLib uncertainty is better located, but not resolved. Missing display-name admission, absent captured runtime steps, and command-environment premises are separate gaps.
4. **Targeted evidence:** glyphsLib identifies the regression job and two installation commands. A justified question is whether exact-attempt step execution and effective environment/requirement evidence exist for the later regression route. No new evidence is acquired here, and job-name repair alone would be insufficient. This is a proof request, not a claim that installation failed or that every such premise must be reacquired for normal review.
5. **Authority:** passing workflows remain authoritative only for their captured workflow/run conclusions. The static definition is authoritative for declared commands. Neither becomes a changed-version/compatibility witness through decoding, citation shape or model agreement. The baseline already declares its exercise/release-claim limitation; it receives credit for that honesty.
6. **Failure behavior:** two operationally completed rows, no input-unavailable, operational failure, timeout, unattempted row or retry. The output retains supported positives alongside unknowns. Narrow review obligations pass for both rows; full-product semantic adequacy is unassessed, not two newly accepted product cases.
7. **Cost:** whole runner 0.586444 seconds, aggregate child work 0.484871 seconds; HTTPX/glyphsLib workers 0.044935/0.066517 seconds, inclusive children 0.230634/0.254237 seconds. These times include retrospective decoding/translation, **not** original acquisition/producer work. The original common preparation declared 14 public GET operations and six native-owner invocations. Earlier corpus/model and human preparation costs remain unreconstructed, not zero. Engineering effort and all new evidence sizes are recorded in [verification](verification.json).
8. **User value:** the regression-specific proof question is potentially more auditable and targeted. No maintainer assessed its usefulness, no improved outcome was observed, and no protected case was used. More specificity is the observed component gain; real actionability remains an untested interpretation.

The old glyphsLib no-added-value/stopping hypothesis remains a historical control rather than an obligatory October verdict. This review finds narrower information in the October native output; it does not regrade July or establish that a maintainer needed additional work. HTTPX provides the observed no-material-addition result in this cohort.

## Investment decision and exact next boundary

**Do not rewrite the CI producer, extend correlation semantics, run another model, or start a multi-role implementation from this result.** No producer defect or architectural cure was demonstrated. The most important information was already present in the retained native output before the failed interpretation trial; this run makes that comparison reproducible rather than supplying an independent new generalization result.

The [earlier completed interpretation review](../2026-10-19-investigator-evidence-first-build/COMPARISON_REVIEW.md) documented promotion of unresolved coverage to confirmed coverage. The [existing report projection](../../../src/upgradepilot/report_projection.py) already carries native states, separate static/runtime axes, per-command results and explicit claim limits. It was source-inspected here; no new complete report was fabricated or generated.

**Recommended next responsibility, requiring a new design decision:** determine how the experimental Investigator's final CI presentation can preserve the existing typed CI/report owner's facts and limits while allowing separately scoped interpretation. Start from the actual report/native delivery and final consumer seam. Compare direct reuse of the existing deterministic projection against a minimal constrained presentation change; reject a duplicate truth-state/validator framework unless a specific uncovered responsibility earns it. Acceptance must preserve supported positives as well as unknowns, prevent stronger runtime/compatibility claims, and still convey a useful next-evidence question. Native availability plus green tests is insufficient; a later execution needs its own frozen proof and budget. If existing presentation already satisfies the responsibility, stop rather than adding another mechanism.

The HTTPX caller/callee relation remains a distinct deferred capability. This CI result does not establish that fixing CI presentation will solve that relation or the other inadequate interpretation cases. No next experiment, new model, product action permission or architecture is selected automatically.

## Evidence-backed learning and remaining ownership

The expected outcomes were a possible HTTPX no-added-value result and more located glyphsLib uncertainty. Actual outputs support that narrow expectation. The source review sharpened it: empty runtime steps and separate checkouts/environments make a job-name-only repair inadequate. Native reconstruction preserved uncertainty rather than curing it.

The key distinction is **a successful workflow → a declared dependency/test route → proof that the changed requirement was exercised at an exact runtime boundary**. Each arrow needs evidence; a more detailed report cannot supply the missing arrow. The baseline need not know all those arrows to be an honest coarse comparator.

Implementation/review is AI-authored under Ali's scope approval. Written D explanation is delivered; Ali's ownership remains unassessed. D discussion and E repair/defer/closure are pending. A useful reasoning point is why two successful workflows cannot establish that pytest 9.0.3 was exercised, and why adding a job-name fallback would still leave this retained case unresolved. Predecessor learner debt remains separate.
