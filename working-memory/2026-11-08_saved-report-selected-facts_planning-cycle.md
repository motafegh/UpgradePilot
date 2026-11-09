# Saved report selected-facts inspection design

Ali selected the follow-up to the [maintainer report onboarding](2026-11-08_maintainer-report-first-view_build-cycle.md#rendered-maintainer-task-review), asking that the solution work beyond the first retained case. Reconciled `dc6be359` with `origin/main`. The [existing report plan](../plans/MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md#inspect-selected-facts-from-saved-reports) owns the proposed slice and proof. The [Core report requirements](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md#61-evidence-reports-and-saved-result-boundaries) own the offline and evidence boundaries.

```text
A0 — DONE: reconciled Git, the report plan, validated reader, CLI routes and two saved inputs.
A1 — DONE: prior turn covered the first view and the saved OpenCV gap. Ali selected the follow-up with reusable behavior.
A2 — CURRENT FOR BUILD: explain what the shared view admits and the proof that would establish reuse.
B — DONE FOR DESIGN: recorded the proposed CLI/renderer responsibility and scope in the existing plan. Build awaits its gate.
Verification — GREEN FOR BASELINE: both saved records decode, preserve their selected values, and correctly refuse original-text inspection.
D/E — HANDOFF: review the design and select implementation separately.
C — CONTINUOUS: preserve decisions and proof across this responsibility.
```

Reused the previous turn's onboarding for this directly selected bounded design. The orientation map separates a saved fact record from raw original text, then follows the same source ID from saved JSON through the reader and CLI to a proposed renderer. The consequential decision is which saved record types to display. Ali's generality constraint applies to the renderer and its proof, including a contrasting package and record shape.

## Baseline and design decision

- OpenCV `source-13` is `selected_facts` with 37 values, including 27 removed tags, eight added tags and the two version values. Its source inventory entry omits exact tags. The original-text view correctly refuses.
- The saved Soup Sieve report's `source-15` is a package metadata record with 12 saved values. Its inventory entry omits distribution filenames and digests. An initial diagnostic expected the digest to be absent from the entire inventory. It failed because separate publisher-provenance records can show the same digest. The corrected check compares the selected source entry, preserving evidence identity and testing the real access gap.
- The same report has workflow selected-fact records with up to hundreds of repeated job fields. Publisher provenance fields already appear in the inventory. A global dump would expand the first task into bulk evidence navigation. A wheel-only command would duplicate the existing record abstraction and would leave the package-metadata task unresolved.

Use one proposed saved-report facts selector and shared renderer with evidence-kind admission. Begin with artifact capabilities and package metadata, and exercise both on the real saved inputs. Reuse the existing decoder and inert display. Keep full-report output and original-text access compatible. The design neither infers target applicability from the inspected facts nor changes the files that produced them. The proof will compare values and binding, cover refusal and compatibility paths, and verify offline behavior. No product code or schema changed. UP-SKILL:upgradepilot-planning-design. UP-SKILL:upgradepilot-working-memory.

## Build continuation

Ali selected full implementation of the previously explained design and asked for onboarding after verification. Reconciled `8709d1c0` with `origin/main`. The prior onboarding and explicit selection complete the pre-B gate for this continuous responsibility. Continued the same record because the input, scope and proof route carry directly into Build.

The CLI admits `--show-facts` on `--open-report` and makes it mutually exclusive with `--show-source`. The existing reader still validates the saved envelope before dispatch. The report renderer reuses exact source-ID lookup, admits the two selected-fact kinds, refuses empty records, and prints provenance and each field's label, key and value in order. The key distinguishes repeated labels such as “Distribution file.” The existing terminal-safe display handles external values. Product code has no case-specific IDs, names, counts or tag values.

The focused CLI checks passed. Real offline invocation with socket, fresh investigation and credential access guarded matched all 37 OpenCV values and all 12 Soup Sieve values in order against the saved JSON. Both input files were unchanged. These are historical report inputs and the proof concerns access to their saved facts.

Compared CLI output against a clean archived source tree at `8709d1c0`. Both ordinary saved reports and the HTTPX `--show-source source-27` view matched byte for byte. Unknown, empty, unadmitted and original-text sources refused selected-fact inspection with exit 7. Malformed report input returned exit 6 and conflicting flags returned exit 2. The full product suite passed all 1,080 tests, and governance and whitespace checks passed. UP-SKILL:upgradepilot-build-implement.

```text
A0/A1/A2 — DONE: reconciled the accepted design, current CLI and actual saved records.
B — DONE: implemented and documented the offline facts selector.
Verification — GREEN: real field parity, refusal controls, prior-view byte parity and full product suite.
D/E — GUIDED HANDOFF: teach the report-to-source flow and distinguish publication facts from target behavior. Independent practice remains unassessed.
C — DONE FOR BUILD: preserved implementation, proof and boundaries.
```
