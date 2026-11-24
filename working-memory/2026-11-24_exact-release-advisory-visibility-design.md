# Exact-release advisory visibility design

- **Base revision** `84911c0e0cd4b50c937646eed27ac44dab9cfc56`
- [F4 development decision](2026-11-23_f4-development-acceptance.md)
- [Bounded design and implementation proof](../plans/MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md#preserve-advisory-observations-for-an-exact-release)
- UP-SKILL:upgradepilot-planning-design
- UP-SKILL:upgradepilot-working-memory

Ali selected the next design step and asked for teaching after the work. The usual pre-work teaching gates were deferred to honor that order. The design and verification were carried out first, with the evidence and its limits retained here for the walkthrough. This increment establishes the design and its feasibility.

## Loss point and design decision

The ordinary investigation asks PyPI for the proposed release and queries the old release after the proposed one is available. The [release parser](../src/upgradepilot/pypi/release.py#L231) accepts an exact package and version and preserves files and project URLs. It currently leaves `vulnerabilities` behind. The [report projection](../src/upgradepilot/report_projection.py#L1028) therefore has no advisory facts to pass to the existing [offline viewer](../src/upgradepilot/report.py#L571). The viewer can already display arbitrary named selected facts with their source and observation time. A renderer-only change cannot recover information that the producer discarded.

Select typed optional observation in the existing release producer, followed by additive report facts on each exact package source. Use the existing offline detail view to open IDs. This gives a maintainer a release-specific lead without asking for more network traffic or implying an installed dependency, an affected target path, or a verified remedy. A generic scanner would require a different evidence and product contract. A new interpretation layer would add complexity to a field PyPI already structures. [PyPI JSON API](https://docs.pypi.org/api/json/#known-vulnerabilities)

## Offline design check

Reused the three frozen F4 ledger indexes and verified their response body digests. The private probe associated the old and proposed PyPI responses with the six exact package sources by response locator, package, and version. It projected only candidate selected facts into copies of the saved reports, then passed all copies through the current installed report codec and launched the existing `--show-facts` command in a network-isolated process. All three original reports reopened with their old view and unchanged bytes. All three prototype copies preserved the recorded action.

| Case | Old release | Proposed release |
|---|---|---|
| OpenCV #1111 | `opencv-python 4.2.0.32`, `source-8`, two reported IDs | `4.8.1.78`, `source-6`, explicit empty list |
| MapProxy #1559 | `soupsieve 3.0.4`, `source-33`, one reported ID | `4.0`, `source-31`, explicit empty list |
| Dashboard API HTTPX #20 | `httpx 0.27.2`, `source-8`, explicit empty list | `0.28.1`, `source-6`, explicit empty list |

The MapProxy ledger also included Soup Sieve 4.1.1 along an upstream lookup path. It supplied no proposed-release facts for 4.0. The sample contained three reported IDs and four empty release lists. In fifteen constructed controls the private sketch distinguished empty from missing, rejected malformed or oversized input, kept withdrawal distinct, collapsed repeats, and refused conflicting states on one ID. The draft bounds are 32 input entries and a 128-character ID. They keep the saved display small and cover the sample without truncation. No representative distribution of list sizes was measured, so the build must expose its over-limit reason and can revisit the limits with evidence.

The prototype mutated only copied report objects. It verified the selected-facts representation and viewer, plus a separate parsing sketch. The ordinary producer still discards the field, and the planned compact source-inventory status has yet to be implemented. Design evidence is retained locally under `~/.local/share/upgradepilot/release-advisory-design-20261124.cPm5LBuB/`.

## Handoff

Carry the agreed admission rules into the ordinary report path and prove them with actual installed source-to-report replay and cold reopening. Advisory exposure, mitigation, priority changes and independent maintainer usefulness remain separate evidence questions. No changes were made to runtime code or the report codec.
