# PR description/source inspection: design verification and Build handoff

Recorded October23,2026. Source horizon: `e35b5062`; design publication `85f92274` plus the bounded refinements recorded here. [Cycle](../../2026-10-23_pr-description-preservation-and-inspection_design-cycle.md). This is planning evidence, not implemented producer/native/viewer behavior.

## Selected design and why it earns a boundary

The [existing report plan §10](../../../plans/MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md#10-pr-description-preservation-and-offline-source-inspection-design) owns the full concrete design. The actual user is reopening one saved report offline and needs its observed PR description, rather than a link that may change. A normal PR page remains the simpler online alternative. This requirement justifies bounded source preservation/inspection; it does not establish semantic or broad maintainer usefulness.

| Decision | Selected method / avoided cost |
| --- | --- |
| Producer | New explicit richer observation call shares existing endpoint/parser, replacing the first normal identity call; no extra request, hidden response cache or caller-specific fallback |
| Trusted identity versus source | Separate provider description record, UTC observation time and decoded-text identity; existing identity and v1 layout unchanged |
| Retention | Seven precise source-field outcomes;256KiB UTF-8 cap; no prefix or forged empty value; copied/truncated upstream context is not reclassified |
| Canonical transfer | Additive description codec1 with only investigation-input basis; existing CI/Python closures unchanged |
| Consumer | Direct Workspace description projection; no second legacy result field or wholesale report migration |
| Saved report | Existing schema1 PR source/retained_text/content; generator2 and renderer2, not a new public schema |
| Access | Explicit saved-report `--show-source SOURCE_ID`; literal sanitized text with source context/limits; default report stays short |
| Failure | Preserve source-field problems versus not-recorded history, scoped unsupported source codec versus integrity refusal, and CLI2/6/7/8 outcomes |

This is source access, not a selected general interpreter. No source authority resolver, action rule or semantic prompt changes. New model/target execution, third capture, extra database/framework and broad provenance archive are outside scope. The Workspace plan's family ledger references this source contract; no new plan/specification/ADR was needed because Core/ADR0012/0013 already own these invariants/methods.

## Fresh bounded verification

**Existing native invariants:** two targeted unchanged tests pass in5.661s:

```text
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src:tests:. .venv/bin/python3 -m unittest \
  test_workspace_native_reconstruction.WorkspaceNativeReconstructionTests.test_v1_layouts_cannot_silently_fill_new_native_fields_from_defaults \
  test_workspace_native_reconstruction.WorkspaceNativeReconstructionTests.test_unrelated_unsupported_versions_preserve_every_unaffected_projection -v
```

They verify current v1 layout completeness and explicit affected-versus-unaffected version refusal. They do not implement the proposed description family or prove its new cold projection.

**Existing report schema:** [data-only recipe](compatibility_witness.py) and [receipt](compatibility-witness.json) demonstrate eight hypothetical source shapes across the two retained cases: actual decoded PR text, empty, null/unavailable and historical not-recorded representations. All encode/decode under the current schema1 reader; generator2 is already accepted as a recorded method string. Domain assessments/findings/unknowns/actions remain equal. Original report bytes remain unchanged. The receipt binds each original report and PR response hash. Description lengths are9,348 UTF-8 bytes (HTTPX) and5,902 (OpenCV), below the selected bound. This is representation feasibility, not new producer parsing, source-view execution or an official case rerun.

```text
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src .venv/bin/python3 \
  working-memory/evidence/2026-10-23-pr-description-design/compatibility_witness.py
```

The recipe uses explicit design-only report IDs/fixed synthetic generation time and does not publish product report files. It verifies the older renderer's existing metadata-only behavior without pretending the future availability cue/source view exists. The report source uses the diagnostic input's completion timestamp as witness data; no historical normal provider timestamp is invented.

**Access mock-ups:** [HTTPX](httpx-source-view.mock.txt) and [OpenCV](opencv-source-view.mock.txt) show selected original-source excerpts with attribution and a proposed invocation. They explicitly identify themselves as design mock-ups, not installed CLI output, whole-body previews, changed original reports or measured user results. The final source viewer is specified to show the whole bounded retained text on explicit request. No HTML engine, summarizer or automatic quote selector is proposed.

## Critical review and corrections

- Adding description to reused `PullRequestIdentity` would alter a shared v1 layout; rejected in favor of an independent family. A new layout/codec implementation and legacy/source projection tests remain Build obligations.
- Adding another description field to `PublicPullRequestInvestigation` would extend the staged legacy surface; rejected because `workspace_revision` already supplies the canonical consumer path.
- Populating JSON without a viewing path fails the named consumer. Automatic body dumping would bloat the ordinary report; the explicit source command makes access deliberate. Literal HTML is less polished than a PR page, but preserves exact observed text at lower complexity. It proves inspectability, not reduced review time. Re-enter formatting only on an actual source-inspection limitation.
- Null, absent, empty and historical not-recorded were separated. Byte-cap checks precede expensive encoding of clearly large strings; their first refusal does not assert validity of uninspected text. Neither transport truncation nor upstream quote truncation becomes a complete-source claim.
- A mutable body is bound to the first response/time/hash, even if the final identity read has the same head but a new description. No automatic body refresh or extra coherence read is added.
- Malformed description fields are valid recorded problems; they do not erase unrelated facts. Canonical corruption/target mismatch is a different fault and must not be swallowed as not recorded. Unsupported optional decoding is explicitly scoped.
- Empty source succeeds; a producer-result detail is not an original retained text. File validation precedes source selection, with no network/writes in inspection. Full report/action semantics remain owned by existing producers/synthesis.
- Schema1 can hold the chosen source shapes. Whole-envelope integrity is still not authenticity; source metadata cannot turn copied release text into independently verified meaning. New generator/renderer identities do not replace unrecorded model/config/semantic versions.
- Separate portable product/hosted fixtures from the full local retained-case proof. Public tests use reviewed minimal responses/excerpts and constructed controls; private frozen API dumps are not test dependencies or newly committed input archives. The complete original descriptions need their own local controlled composition receipt, with no reacquisition fallback if absent. This prevents a green public suite from silently substituting excerpt proof for the full case.

## Concrete implementation handoff

Implement one coherent producer → native → report → offline-access responsibility under the report plan. Likely anchors: `github/pull_request.py`, `investigation_inputs.py`, `investigation.py`, `workspace/native_inputs_codec.py`, `native_codecs.py`, `native_capture.py`, `native_projection.py`, `report_projection.py`, `report.py`, `cli.py`, focused active tests and CLI README. Retain existing family layouts and source owners; report_file/schema/storage changes are not expected. Scope changes return to the owner rather than broadening the design silently.

Focused acceptance: controlled normal composition with both real retained PR shapes and source-state/capacity controls; direct Workspace/cold source parity; old native/report compatibility; unchanged non-source domain/action results and request count; safe exact stored versus sanitized displayed text; explicit view/file/source/misuse/integrity failures; installed CLI path. Then full deterministic product regression and only affected experimental/diagnostic integrations. Existing frozen outputs remain unchanged and any new controlled outputs have their own identity. No new official live capture is required.

The implementation should end with an inspectable saved description, exact observed provenance/limits and explicit missing cases. It must not finish with a JSON-only hidden field, unsupported caller fallback, silent old-codec rewrite, default long-body dump, authority promotion or a claimed independent utility result. Design decisions are closed at this scope; no architecture decision remains deferred merely to a later implementation session. Actual source behavior/proof and learner ownership remain unestablished until their own work occurs.

UP-SKILL:upgradepilot-planning-design
