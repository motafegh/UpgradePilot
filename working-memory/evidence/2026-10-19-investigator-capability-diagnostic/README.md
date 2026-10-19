# Capability diagnostic r4 — supplied-evidence interpretation

**Date:** 2026-10-19, Asia/Tehran
**Source horizon:** `13643c99` (unchanged during execution)
**Executed freeze:** `c5e06b1b759b8cacaacf1c59bfaedf1556254f81ad709f615c64adf8c61c27b0`
**Activation:** [gpu-release activation](../2026-10-19-investigator-successor-build/gpu-release-activation.json) in the successor-build evidence folder
**Private run root:** `/home/motafeq/.local/share/upgradepilot/investigator-runs/supplied-evidence-2026-10-19-diagnostic-r4`
**Status:** executed once, complete; initial review preserved with an explicit later adjudication. No retry, tuning or semantic feedback into later cases.

This is the first completed four-case supplied-evidence diagnostic. Earlier Investigator report texts already provided semantic evidence. It executes the
[successor plan](../../../plans/INVESTIGATOR_RUN_CONTROL_COMPLETION_AND_CAPABILITY_DIAGNOSTIC_PLAN.md)
capability-localizing diagnostic: supplied, provenance-preserving evidence with a fixed,
affordable report-only contract, so that **discovery is removed as a cause** and interpretation
is what gets measured.

## 1. Operational outcome

This supplied-evidence cohort completed all five roles with complete known usage. This statement is scoped to this cohort; it is not a first-ever zero-unknown claim across older qualification work.

| Role | Case | Execution | Input | Generated | Citations | Report |
| --- | --- | --- | ---: | ---: | ---: | --- |
| probe-report | reference canary (synthetic) | completed | 3,277 | 608 | 2 | published |
| packet-a | HTTPX PR context | completed | 22,364 | 1,089 | 5 | published |
| packet-b | newer captured consumer | completed | 7,880 | 857 | 3 | published |
| packet-c | glyphsLib PR context | completed | 25,527 | 957 | 3 | published |
| packet-d | older captured consumer | completed | 7,872 | 862 | 3 | published |

Aggregate: **5 attempts, 5 completed, 66,920 input / 4,373 generated tokens, 180 admission
units, 1,028.44 prediction seconds, 1,034.63 batch seconds, 0 unknown usage**, owned model
unloaded and client released ([accounting](run-accounting.json)). Exact requests, renderings,
receipts, fragments and publications are retained in the owner-only root
([retention identity](retention-summary.json)).

Operational result: **the selected run-control, completion-affordability and fit path delivered at this point.** Recorded batch elapsed time is17.24 minutes. Cost/usefulness comparisons are not established by completion or by calling the run cheap.

## 2. What the model actually produced

All four semantic reports were published with valid strict citations. Their semantics are the
finding:

- **packet-a (HTTPX):** correct declarations, TestClient use and Docker install; the supplied
  `app`-keyword removal is **never mentioned**; recommendation says the change is
  "likely safe" with **empty recommendation evidence**.
- **packet-b (newer consumer):** substitutes a real but non-required `verify` type-hint change;
  asserts the TestClient "passes the verify parameter directly to the super() constructor" —
  the supplied call passes `base_url/headers/transport/follow_redirects/cookies` and no
  `verify`; concludes the change "maintains functional compatibility".
- **packet-c (glyphsLib):** correct pytest transition; names both workflows but never traces
  the supplied `tox -e py` dependency route or the regression environment distinction;
  recommends the update is "**verified as covered** by both CI pipelines" from historical
  captures.
- **packet-d (older consumer):** same `verify` displacement; concludes the change is
  "**structurally compatible**" — the inverse of the supplied relation, where this caller
  passes `app=self.app` and the new callee removed `app`.

Read the immutable [initial review](review.json) together with the explicit [review adjudication](review-adjudication.json). The latter records the four qualifications, five obligation-label changes, source reasons and unchanged case-level failures; it does not replace original evidence.

## 3. Review against the 20 frozen obligations

Reviewed against the unchanged20-obligation protocol frozen before any output (`supplied-evidence-2026-10-19-review-r1/review-protocol.json`). The table below applies the adjudication overlay. Original labels/counts remain in `review.json` and the adjudication records the exact changes. These counts are neither factual-accuracy percentages nor independent samples.

| Case | Supported | Partially supported | Unsupported/omitted | Contradicted | Classification |
| --- | ---: | ---: | ---: | ---: | --- |
| packet-a HTTPX (6) | 0 | 3 | 3 (1 decision-critical) | 0 | semantically inadequate |
| packet-b newer consumer (4) | 0 | 1 | 2 (1 decision-critical) | 1 | semantically inadequate |
| packet-c glyphsLib (6) | 1 | 2 | 2 | 1 (decision-critical) | semantically inadequate |
| packet-d older consumer (4) | 0 | 1 | 1 | 2 (1 decision-critical) | semantically inadequate |

**Cohort: 0 adequate, 4 inadequate, 0 inconclusive, 0 control failures.**

Correct statements are preserved and were not discounted for the cases failing overall: the
`verify` typing really did change from `VerifyTypes` to `ssl.SSLContext | str | bool`; the
pytest declaration is correct; the target does import FastAPI's `TestClient`; the Dockerfile
does install from `requirements.txt`; both workflows exist with historical successful job
captures.

## 4. Qualified findings

1. **Empty recommendation attribution is a structural limitation, not a semantic explanation.** Three reports use `recommendation_status: "inferred"` with empty `recommendation_evidence`. A prospective support-reference requirement may improve attribution, but packet-c has two recommendation references and still overstates CI support. A nonempty list cannot establish entailment, source selection, runtime scope or useful advice. Publication was intentionally a structural/reference boundary, not semantic approval; this review does not change it.
2. **The older/newer source contrast matters.** Both captured-consumer packets contain the old/new HTTPX signatures. Only packet-d's older caller forwards `app=self.app`; packet-b's newer caller does not. Neither supplied caller forwards `verify`. Both reports substitute the adjacent real `verify` type-hint change and invent that forwarded argument. This supports an interpretation/selection failure in this deployment/task/presentation under delivered evidence.
3. **Discovery is excluded from this diagnostic, not solved globally.** Missing autonomous discovery does not explain these failures because the decisive sources were delivered. Prior navigation weaknesses remain separate evidence. The result prioritizes interpretation-method/deployment diagnosis; it does not prove navigation is never useful or cannot improve a different configuration.

The [adjudication](review-adjudication.json) distinguishes partially correct generic identities from contradicted call behavior and unsupported versus contradicted consequences. Case classifications remain unchanged. Its AI-assisted second pass is not blinded or independent human acceptance.

## 5. Disposition under plan §7

All four comparable cases are **semantically inadequate**: complete reports with
decision-critical unsupported or contradicted advice. That selects the plan's branch:

> **Do not fund the next increment as autonomous-discovery optimization for this result.**
> Select a bounded interpretation-method or simpler evidence-preparation plus interpretation
> comparison.

Consequences recorded, not activated:

- This diagnostic does not evaluate autonomous discovery/navigation. Earlier weaknesses remain; do not fund that optimization as the immediate response to these supplied-evidence failures. Interpretation is the dependency to investigate first.
- Candidate next responsibilities (each needs its own bounded decision): a stricter
  recommendation-support contract; a supplied-evidence comparison of one simpler interpretation
  method or deployment; or returning to the product-level deterministic baseline evaluation.
- No model ranking, reliability estimate, maintainer usefulness, product adoption or learner
  ownership follows from one sample per case on exposed material.

## 6. Limits

One deployment, one operating point, one sample per case; two cases derive from the same
exposed HTTPX material and are not independent generalization samples. The review is AI-assisted
and source-aware with prior case exposure — not masked independent human acceptance. No target
execution, installed-version verification or maintainer usefulness evidence exists here.
Semantic adequacy was never an execution-admission criterion; it is a separate offline verdict.

## 7. Explicit correction history

Ali authorized the four qualifications after a source-aware second pass. The initial `review.json`, frozen reviewer protocol, original outputs, execution accounting and private retention entries remain unchanged. Initial README wording is recoverable at commit `5d412679`; its pre-correction hash and all changed labels are bound in [review-adjudication.json](review-adjudication.json). The four corrections concern semantic-observation scope, older/newer caller contrast, obligation-specific labels, and the scope of conclusions about discovery. No new experiment result, successful case or automatic inference authorization is introduced.
