# PR-description preservation and inspection design

Date: October23,2026 (Asia/Tehran). Primary operation: Planning/Design. Starting revision `e35b5062`; fetched main matches. Previous: [maintainer-task review and milestone](2026-10-23_maintainer-benefit-review-and-milestone_cycle.md). Owner: [existing report plan](../plans/MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md).

## Authorization and method

Ali's "Go on fully" follows the explicitly selected concrete design before product implementation. Complete that design, compatibility/failure/access decisions and reviewable Build handoff. No product/test implementation, fresh case/model/target execution, participant outreach or third capture is selected in this design responsibility. Continue authorized progressive publication. The unrelated untracked October3 file is untouched.

Situational adaptation: ongoing context and Ali's instruction to learn elsewhere justify compressed A1/A2 teaching stops. Explain material decisions briefly, preserve learning topics, and perform the planning now; learner understanding/mastery remains unassessed. This does not change source truth or independent acceptance requirements.

## Cycle and orientation map

- A0 — DONE: reconcile live position, report plan, provider/application/native/report source, native compatibility owners and existing test seams.
- A1 — COMPRESSED: prior review established acquired copied context lost at the identity-only DTO.
- A2 — COMPRESSED: preserve an untrusted observation, carry it without domain evaluation, support explicit offline inspection, distinguish old/not-recorded/problem states.
- B — DONE: concrete source/native/report/CLI/failure/compatibility/acceptance design closed in existing report plan §10.
- Verification gate — GREEN at planning scope: static end-to-end trace,2 existing compatibility tests and8 data-shape witnesses; final document checks below. New source/native/viewer implementation is unproved.
- D — DEFERRED elsewhere: preserve learning questions without claiming ownership.
- E — engineering handoff delivered; learner D/E deferred elsewhere: one bounded Build responsibility, with no remaining design decision disguised as later planning.
- C — preserved through this handoff in one record.

## Source findings and decisions under refinement

`PullRequestIdentity` is a codec-v1 input reused by CI/Python families and real developer/experiment callers. Adding description to that layout would change unrelated consumers and historical decoding. Select a separate provider-owned description observation and additive native family instead. Existing generic boundary validation permits unrelated families; current native projections decode only their required family closure. No v1 layout or old blob needs rewriting.

The normal result already carries `workspace_revision`; the full report can project the new source directly from that canonical boundary. Avoid a second description field/authority in `PublicPullRequestInvestigation`. `AcquiredDependencyInputs` and initial native capture carry the provider observation once. Existing identity-only `get_pull_request` callers retain their method; a richer observation method is selected for normal input preparation, sharing acquisition/parsing rather than making extra requests.

`ReportSource(kind="pull_request", retention="retained_text", content=...)` is already decodable under report schema1. Enrich the existing PR source without new findings or action. Current renderer shows source metadata only, so select an explicit saved-report source view rather than claim JSON population makes text accessible. Proposed CLI: `upgradepilot --open-report PATH --show-source SOURCE_ID`.

A 256KiB decoded-description UTF-8 retention cap is a bounded initial choice, not a GitHub transport-size or public-prevalence claim. Preserve the exact valid text below the cap; over-limit/problem outcomes retain no misleading prefix. Observation time and hash bind mutable PR text, not commit immutability or copied upstream authority. The final contract must define empty/null/missing/malformed states, old records, unsupported codecs and viewer failures precisely.

## Concrete design checkpoint

Report plan §10 now defines the complete provider-owned representation, seven source-field states, size/hash/time semantics, additive native capture and old-record behavior, direct Workspace-to-report projection, schema1 compatibility and explicit viewer. The chosen richer provider call replaces the first normal identity call; the final coherence read and existing identity-only callers remain supported, with shared acquisition and no last-response cache/fallback. No second legacy description field is added.

User flow: investigate with optional `--save-report`, then `--open-report PATH --show-source SOURCE_ID`. Source view is deliberately literal, including original HTML/Markdown, with display controls sanitized and stored text unchanged. This refines the earlier ambiguous "avoid raw HTML dumps" instruction to the ordinary summary: an explicit source inspector needs exact text, while a new HTML reader adds formatting/maintenance without a demonstrated need. Scope effect: offline inspectability, not a polished web-equivalent reader or a utility claim. The concrete plan owns this choice and its rejection criteria.

Errors are explicit: argument misuse2, bad saved file6, unknown/unretained source7 and canonical integrity projection failure8. Empty retained text succeeds; reference-only and producer-result sources are not misrepresented as original retained text. Unsupported optional source decoding is scoped unavailability; corrupted/target-mismatched material is not hidden as absence. Source-field problems and canonical corruption remain different faults.

No new specification/ADR is required: Core6.1/6.2 and ADR0012/0013 already own preservation, untrusted content, one-way projections and explicit codecs. Added the source family to the Workspace plan ledger by reference. Independent utility, semantic-role adoption, action permission, third capture and replay remain separate.

Fresh existing compatibility checks:2 targeted tests pass in5.661s (`test_v1_layouts_cannot_silently_fill_new_native_fields_from_defaults`, `test_unrelated_unsupported_versions_preserve_every_unaffected_projection`). They establish current schema-drift protection and scope of refusal, not implementation/proof of the proposed new family/viewer. The full899-test suite remains prior evidence, not rerun here.

## Design verification and final handoff

[Design review](evidence/2026-10-23-pr-description-design/DESIGN_REVIEW.md), [bounded data recipe](evidence/2026-10-23-pr-description-design/compatibility_witness.py), [receipt](evidence/2026-10-23-pr-description-design/compatibility-witness.json) and two clearly labeled source-view mock-ups preserve the result. Eight in-memory hypothetical shapes pass the unchanged report schema1 decoder across the two original report records, preserving domain/action fields and original files. Text sizes9,348/5,902 UTF-8 bytes fit the chosen256KiB limit. Synthetic IDs/generation time and diagnostic source completion timestamps are explicitly design data, not fabricated normal provider output or an official rerun.

Critical review retained three practical constraints: the original HTML stays literal only in explicit source inspection; saving is opt-in and a failed/omitted save cannot imply durable access; the first sufficient size/type/encoding refusal does not claim validity of uninspected text. Generator/renderer2 are prospective method identities with schema1 unchanged. Rollback must preserve retained bodies and explicit unsupported capability rather than rewrite old layouts.

Further proof clarification separates portable reviewed public-safe fixtures from two full-description local controlled checks using private frozen inputs. No hosted/private-path dependency, raw API archive in Git, false excerpt-as-full-case proof or reacquisition fallback. One attempted documentation context edit failed atomically; corrected it with exact context, without changing implementation or frozen evidence.

No new specification/ADR or master plan is needed; Core6.1/6.2 and ADR0012/0013 cover the meanings/methods. Only the report plan's execution contract and Workspace family ledger changed. The named offline consumer defeats the simpler mutable URL baseline for this narrow responsibility; it does not defeat the ordinary PR page for unrestricted online review or establish general usefulness.

Next responsibility is one source-to-offline-access Build with the exact scope/proof in report plan §10, not another planning checkpoint. Product/source/test implementation was not performed in this design cycle. Controlled normal composition, new native cold reconstruction, all source states/capacity and CLI errors, exact stored versus safe displayed content, old records, unchanged non-source behavior, full regression and installed CLI remain Build proof. No fresh acquisition/model/target execution/third case follows from this design.

Learning topics for the separate session: immutable identity versus mutable observation; decoded-field hash versus wire-response digest; additive family versus changing a shared codec; explicit source access versus semantic interpretation; record shape compatibility versus executed behavior; scoped unsupported versions versus integrity failure; retaining exact data while sanitizing display. Learner ownership remains unassessed.

Final document/data qualification is preserved in [validation receipt](evidence/2026-10-23-pr-description-design/validation.json): links/anchors/syntax/whitespace, original report/source hashes, evidence/design identities and exact proof/non-proof. No product, tests, tools, experiments, hosted workflow or package declaration changed. Original capture paths and unrelated untracked October3 file remain outside the publication delta.

UP-SKILL:upgradepilot-planning-design
UP-SKILL:upgradepilot-working-memory
