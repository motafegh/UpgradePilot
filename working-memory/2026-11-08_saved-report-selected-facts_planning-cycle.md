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
