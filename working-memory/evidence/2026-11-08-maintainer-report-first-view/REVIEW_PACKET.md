# Saved report first-view comparison packet

November 8, 2026. Prepared for exposed development review under the [first-view comparison](../../../plans/MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md#first-view-comparison-on-saved-reports). The baseline is the complete saved-report rendering. The left column below points to the relevant places in that view. The right column sketches what the reviewer would see first, with the same full report and source access behind it. Read the complete View A for a review. These pointers are navigation aids, not substitute baseline inputs.

For each pair, ask what changed, which finding is material for this task, where it is supported, what limits it, and what evidence would resolve an important unknown if that can be stated. The normal report is reproducible via `upgradepilot --open-report PATH`. Use `--show-source SOURCE_ID` with that report where retained original text is available. A producer result or reference-only source remains inspectable at its existing level. The sketch does not grant access to extra material.

## HTTPX caller and signature fit

**Exact report.** `Aidan-Wallace/kubernetes-dashboard-token-api` PR 20, `httpx 0.27.2 → 0.28.1`, base `b065646e4b7b894964567950f9ad770b02c136c2`, head `391508134b083b8f54461c0b576e8f7985c6ecb4`. Caller/signature profile. Report `4eea103d-dbb6-4fa2-89e4-5d28a1a47ea3`, SHA-256 `ae8bb734d6d2be78a0fc6f248747572cb68238f7ea6b840c0ac6e1e24ef691d1`. The owner-local file is `report.json` in `destinations.product_attempt` of the [successor binding](../2026-11-07-pypi-route-repair/successor-binding.json). The [saved qualification review](../2026-11-07-native-proxy-successor/RESULTS.md) documents the original source and report read. The raw report stays in its local store.

| View A · Current saved report | View B · Concise first view |
| --- | --- |
| Open the exact report above. The 1,185-line render lists the dependency transition, branches marked not evaluated, bounded source coverage, individual conditional witnesses, unresolved applicability and action. The source inventory follows. | **HTTPX 0.27.2 → 0.28.1.** Both versions accept the five arguments forwarded on the sampled Starlette `TestClient` fallback path. **Condition:** the sampled `httpx` fallback and recorded dispatch assumptions must apply. The target's loaded client remains unknown. This source-only invocation did not evaluate CI or runtime. **Sources:** target call `source-27`, FastAPI re-export `source-37`, Starlette branch and forwarding `source-39`, old HTTPX `source-35`, proposed HTTPX `source-31`. **Action status:** abstain. **Details:** open this same report and source inventory. |

**Editorial inference for review, separate from the renderer-only sketch.** A test-process observation at the affected call identifying the loaded client and linking its file to the analyzed source would resolve the dispatch premise for that invocation. The saved finding and unknown support the explanation of why this matters. The proposed observation is analyst wording and carries no `run targeted checks` permission. Keep the historical Docker result and empty CI query outside this source-only packet.

## OpenCV published artifacts and target applicability

**Exact report.** `carla-simulator/scenario_runner` PR 1111, `opencv-python 4.2.0.32 → 4.8.1.78`, base `7758d066080f180f8296887ed89b7c723a54706a`, head `f32ad2d23a9abee47c566dfbed2b822d953a09e2`. Normal report `8152f014-e86a-401f-9f48-9e67ecb8cabb`, SHA-256 `9f6b2d79a08421db5c113a9a0e38d34176728352d8644c52ddc86a2acea88116`. [Saved JSON](../2026-10-22-opencv-matched-report-source-capture/report.json) · [Original normal report text](../2026-10-22-opencv-matched-report-source-capture/report.txt) · [Capture review](../2026-10-22-opencv-matched-report-source-capture/REVIEW.md)

| View A · Current saved report | View B · Concise first view |
| --- | --- |
| Reopen the saved JSON above. The 286-line render separates the publication candidate, target environment status, applicability, unknown source-build outcome, action, and source inventory. | **OpenCV 4.2.0.32 → 4.8.1.78.** The published artifacts lost 27 exact wheel tags and gained eight. A proposed source distribution is available. **Open question:** the target installer environment is not established, so wheel compatibility and the source-build outcome remain unresolved. **Evidence:** tag comparison `source-13`, publication assessment `source-14`, target environment `source-15`, applicability `source-16`. **Action status:** abstain. **Details:** open this same report and source inventory. |

**Editorial inference for review, separate from the renderer-only sketch.** The relevant installer environment and policy would help distinguish a compatible wheel from a possible source fallback. Successful source build would need a separate observation. Do not count these proposed checks as existing structured action fields.

## Soup Sieve support-drop evaluation blocked by upstream lookup

**Exact report.** `pydantic/pydantic` PR 13432, `soupsieve 2.6 → 2.8.4`, base `652a61ce4f9d7d76eaada31535807a485ece0e21`, head `aa2dc024d33f61cdef50bf1973ab5adf0a974f5a`. Historical partial normal report `b6ba653a-51f1-4f63-9ce8-8b9146c4eaef`, SHA-256 `19bbe7e31715abd22fb9773f70fe62f270e81496a0c7340be6e7359f325a595a`. Selected as the scoped no-finding control for the support-drop task. The separate successful Soup Sieve report is a different observation. [Saved report](../2026-10-03-report-model-recovery/rate-limited-investigation-report.json) · [Retained inventory and scope](../2026-10-22-maintainer-utility-readiness/READINESS.md)

| View A · Current saved report | View B · Concise first view |
| --- | --- |
| Open the exact partial report above. The 698-line render records the supported dependency transition, the failed proposed-version tag lookup, support-drop evaluation as unperformed, and the abstention. Other evaluated branches remain available. | **Soup Sieve 2.6 → 2.8.4.** The dependency transition was established. **Support-drop finding unavailable:** the proposed-version tag lookup failed, so this report has no evaluated support-drop result or target Python applicability result. The recorded reason is a provider refusal or rate limit. **Evidence:** tag and interval assessments `source-22` and `source-23`, support-drop assessment `source-24`. **Action status:** abstain. **Details:** open this same report and source inventory. |

The concise control makes the stopped branch visible without borrowing the later interpretation or treating the blocked lookup as evidence of an unchanged support policy. It retains a scoped stop reason and offers no formal check recommendation.

## Review boundary

All three saved bytes matched their recorded hashes and decoded through the current report reader. The displayed line counts describe full offline renders, not task effort. The concise text is manually prepared. Source links, material claims, conditions and explicit editorial inferences are available for review. The cases were already exposed to the author. No timed or independent review, executable layout change, report refresh or new evidence acquisition has taken place.
