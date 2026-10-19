# Capability diagnostic r4 — supplied-evidence interpretation

**Date:** 2026-10-19, Asia/Tehran
**Source horizon:** `13643c99` (unchanged during execution)
**Executed freeze:** `c5e06b1b759b8cacaacf1c59bfaedf1556254f81ad709f615c64adf8c61c27b0`
**Activation:** [gpu-release activation](../2026-10-19-investigator-successor-build/gpu-release-activation.json) in the successor-build evidence folder
**Private run root:** `/home/motafeq/.local/share/upgradepilot/investigator-runs/supplied-evidence-2026-10-19-diagnostic-r4`
**Status:** executed once, complete; review and disposition delivered. No retry, no tuning, no semantic feedback into later cases.

This is the first complete semantic observation in the Investigator lineage. It executes the
[successor plan](../../../plans/INVESTIGATOR_RUN_CONTROL_COMPLETION_AND_CAPABILITY_DIAGNOSTIC_PLAN.md)
capability-localizing diagnostic: supplied, provenance-preserving evidence with a fixed,
affordable report-only contract, so that **discovery is removed as a cause** and interpretation
is what gets measured.

## 1. Operational outcome

The cohort completed all five roles with complete known usage — the first cohort in this lineage
with no unknown-usage attempt.

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

Operational result: **the run-control, completion-affordability and fit work delivered.** The
previously unmeasurable loop is now measurable, cheap (19 minutes, 67k input tokens) and
complete.

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

Full obligation-level verdicts with source locators: [review.json](review.json).

## 3. Review against the 20 frozen obligations

Reviewed against the protocol frozen before any output
(`supplied-evidence-2026-10-19-review-r1/review-protocol.json`).

| Case | Supported | Partially supported | Unsupported/omitted | Contradicted | Classification |
| --- | ---: | ---: | ---: | ---: | --- |
| packet-a HTTPX (6) | 0 | 3 | 3 (1 decision-critical) | 0 | semantically inadequate |
| packet-b newer consumer (4) | 0 | 0 | 2 | 2 (1 decision-critical) | semantically inadequate |
| packet-c glyphsLib (6) | 1 | 2 | 2 | 1 (decision-critical) | semantically inadequate |
| packet-d older consumer (4) | 0 | 0 | 2 | 2 (1 decision-critical) | semantically inadequate |

**Cohort: 0 adequate, 4 inadequate, 0 inconclusive, 0 control failures.**

Correct statements are preserved and were not discounted for the cases failing overall: the
`verify` typing really did change from `VerifyTypes` to `ssl.SSLContext | str | bool`; the
pytest declaration is correct; the target does import FastAPI's `TestClient`; the Dockerfile
does install from `requirements.txt`; both workflows exist with historical successful job
captures.

## 4. Two contract-level findings

1. **The report schema admits unsupported recommendations.** `recommendation_status: "inferred"`
   with `recommendation_evidence: []` is structurally legal, and three of four reports used it
   to state a decision-critical reassurance. The failure is therefore not only model behaviour;
   the interface permits it. A successor protocol should decide whether a recommendation
   requires at least one eligible support reference or must be expressed as a scoped/unresolved
   conclusion.
2. **Adjacent-detail displacement.** Packets b/d supplied the decisive `app` removal and the
   consumer's `app=self.app`, yet both reports substituted the adjacent real `verify` change and
   asserted consumer behaviour the supplied lines do not show. This is an
   interpretation/selection failure under **complete** evidence — discovery improvements cannot
   address it.

## 5. Disposition under plan §7

All four comparable cases are **semantically inadequate**: complete reports with
decision-critical unsupported or contradicted advice. That selects the plan's branch:

> **Do not fund the next increment as autonomous-discovery optimization for this result.**
> Select a bounded interpretation-method or simpler evidence-preparation plus interpretation
> comparison.

Consequences recorded, not activated:

- Discovery/navigation work (pagination, tool guidance, history cost) remains unattempted but is
  **not the current bottleneck**; it stays deferred behind an interpretation decision.
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
