# Maintainer report development review results

- **Date:** 2026-11-22
- **Finding:** AUDIT-016 F4
- **Completion:** both assigned reviews and key adjudication received. Independent maintainer usefulness remains unestablished.
- [Packet preparation](../../2026-11-22_maintainer-usefulness-pilot-preparation.md) · [Frozen inputs and assignments](PACKET_RECEIPT.json) · [Evaluation criteria](../../../plans/MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md#5-independent-usefulness-evaluation)

## Submitted evidence

| Submission | SHA-256 |
|---|---|
| [Corrected answer key](review-submissions/adjudicator/review.md) | `d1fba1dbf026ae84e155f0070d67f0b58235139d1bb64c550a81b3c03d6a6431` |
| [Reviewer 1](review-submissions/reviewer-1/review.md) | `a1e6f59641a70ca8195b1cc7a4e5382fc225e6dac3b8d1fc59997fc8a5273e42` |
| [Reviewer 2](review-submissions/reviewer-2/review.md) | `6e415c91beba9dc5376caecf73a56050067b0578344cadd15ad5446ff1b48641` |

The three submissions were published together at `e18e409b` after completion. Reviewer 1's repository copy matches the original Windows checkout byte-for-byte. The corrected key matches the operator's archived copy. Verification matched both reviews to the assigned order, all version transitions and revision identities, the five requested answer elements per case, and the exact assisted reports. The corrected key admits well-supported alternatives to its lead findings. The checks of advisory, API, CI, and provenance references used the retained packet.

Both reviewers disclosed prior UpgradePilot involvement or case exposure. Reviewer 2 explicitly identified itself as an AI reviewer. Ali allowed the assigned reviews to proceed after disclosure. Both reviewers reported limiting their evidence to their assigned ZIP. Public delivery and self-reported access supply an exposed development comparison. The corrected key and both reviews are now public, so treat these cases as exposed development material when preparing a future independent pilot.

## What the reviews support

| Case | Sources-only observation | Report-assisted observation | Product implication |
|---|---|---|---|
| OpenCV #1111 | Reviewer 1 used the package inventories and captured CI result to identify potential coverage loss and a target-dependent installation check. | Reviewer 2 credited the report for separating published wheel-tag changes from target applicability. The review still cited the raw inventories and proposed a target check. | Keep publication evidence and target applicability visibly distinct. Both conditions reached a defensible next observation. |
| MapProxy #1559 | Reviewer 2 used workflow, job, and changelog sources to identify successful exact-head CI and a conditional selector-compatibility concern. | Reviewer 1 recovered the same CI and compatibility limits. Repeated pip-environment explanations and the oversized changelog-window stop impeded scanning. The tagged changelog supplied the concrete selector concern. | Improve the CI summary and preserve access to variant evidence. The report's `window_too_large` result leaves change interpretation unresolved even though the retained text is useful to a reviewer. |
| Dashboard API HTTPX #20 | Reviewer 1 found the copied release notes' API removals and proposed checking the actual client or test-client call sites. | Reviewer 2 credited the report's interpretation of the empty exact-head CI query and used the PR body for the same API concern. | Preserve precise CI uncertainty. Attributed PR-source notes are meaningful even when publisher-backed interpretation is unavailable. Their reported change still needs target-use evidence. |

Both reviews supplied exact change identities and concrete next checks and kept the decision within the recorded proof boundary. The adjudicator also identified release-level advisory evidence in the retained OpenCV and Soup Sieve metadata. Both task reviewers chose other supported leads. The reviewed reports did not surface those advisory entries as findings. Consider whether presenting structured advisory facts would improve prioritization after the presentation comparison. Target exposure and mitigation require separate evidence.

The submitted elapsed times in seconds were OpenCV **77 source-only / 53 assisted**, MapProxy **142 / 113**, and HTTPX **60 / 74**. Reviewer 1 started at the source index and Reviewer 2 started at the first saved JSON body or report. The two conditions used different reviewers in each case. These times are descriptive and cannot establish speed differences attributable to the report. Future timing instructions should explicitly identify the common start event before a trial.

## Disposition

Record F4's exposed development review as complete. The case notes show useful interpretation of evidence limits and a concrete MapProxy navigation problem. The assisted MapProxy output had 1,141 lines, with 35 occurrences of the same missing pip-selector explanation.

The strongest follow-up is a bounded offline comparison of the existing MapProxy report and one concise deterministic CI summary using the same saved report. The comparison should check whether a reader can identify the successful consuming step, find the exact run, attempt, job, and step, and explain why installed version remains unresolved. Group only shared limits, preserve differences and failed or skipped cases, and keep the full per-variant evidence and saved-source access available. Check the ApplyPilot failed step as a contrasting control. A stable sketch can support a later implementation decision if it reduces navigation friction without weakening those distinctions. [Existing first-view comparison method](../../../plans/MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md#first-view-comparison-on-saved-reports)

Retain advisory visibility and attributed PR-note navigation as distinct product opportunities. Independent human usefulness remains open and requires eligible reviewers, appropriate exposure controls, and equivalent access and timing.
