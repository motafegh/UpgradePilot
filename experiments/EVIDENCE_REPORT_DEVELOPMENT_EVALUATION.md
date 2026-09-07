# Evidence-report development evaluation

**Recorded:** 2026-09-07

**Status:** Draft evaluator labels; no system evaluation or independent human adjudication performed.

**Data:** [Three development cases](evidence_report_development_cases.json)

This evaluation asks whether a report communicates the supported finding, supporting evidence, uncertainty and investigation boundary without making stronger claims. It complements the [artifact integration plan](../plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md) and [report proposal](../proposals/2026-09-05_UPGRADEPILOT_END_TO_END_PRODUCT_AND_ENGINEERING_PROPOSAL.md). It does not change either owner's accepted scope or define a product schema.

## Case selection and intended use

| Case | Distinction under pressure | Relationship to implementation |
|---|---|---|
| CARLA OpenCV wheel-to-source fallback | Interpreter metadata, binary availability and successful source build are separate facts | Direct artifact-serviceability development pressure; simulation context is richer than current normal product acquisition |
| Dictare optional MLX environment | Platform match, optional installation, engine activation and runtime coverage are separate facts | Partial overlap with optional-environment/CI work; base-revision static evidence cannot become exact-head execution evidence |
| Freqtrade persisted scikit-learn state | Known reuse mechanism does not establish a particular artifact's history or failure | Future capability boundary; persisted runtime objects are not distribution artifacts handled by wheel serviceability |

These cases were already used during project design. All belong to the **development** split. Related artifacts are pieces of a case, not independent samples. Labels are assistant-authored interpretations of preserved evidence and need human review. Three selected cases cannot establish generalization, model calibration, ranking quality or production readiness.

No simulation is restarted and no target code, workflow, model inference or external request is executed by this package. The JSON manifest pins local artifact bytes with SHA-256 and uses JSON Pointers to identify the supporting statements. This detects evidence drift; it does not prove upstream authenticity or independently reproduce the historical acquisition.

## Two different evaluation modes

**Curated-evidence presentation review:** Give the report producer a declared evidence packet derived from the manifest, without the evaluator's expected/forbidden findings. The preserved simulation artifacts already contain interpretation and conclusions. Therefore this mode tests organization and faithful communication of supplied evidence, not discovery, extraction, acquisition or independent reasoning. Record exactly which files/pointers and bytes were supplied. Do not describe the packet as blind raw evidence.

**Normal product-output review:** Capture output from a separately authorized normal application run and record its exact input, output and revision. Predeclare which capabilities are being evaluated, then identify which case expectations the actual producer evidence can support. The simulation's base-revision context must not silently be injected into an exact-head application result. Do not fabricate product fields or wire the label file into product runtime to make a case pass.

No common runtime adapter or automated semantic judge is needed for this first manual evaluation. If a later executable evaluator is admitted, keep input construction, oracle labels and run outputs separate and protect against oracle leakage.

## Freeze before viewing the report

Record:

- evaluation mode, case IDs and declared supported capability subset;
- product/renderer commit, case-file hash, and evidence packet manifest/hash;
- repository, PR and revisions actually analyzed; record any mismatch with the frozen case;
- configuration and model identity when used, assistance, and whether evaluator labels were exposed;
- reviewer and immutable output path/hash; runtime/provider failure if no report was returned.

Do not revise scope after seeing omissions to turn them into exclusions. If evidence/revision differs, mark the case `not_comparable` and resolve the mismatch before scoring; do not reuse historical expected facts as fresh truth. Preserve the original attempt if a retry or corrected label is needed.

The full case requirements apply in curated-evidence review when all listed evidence is supplied. In normal-product review, unavailable or out-of-scope capability must be recorded explicitly. Honest unsupported output can satisfy claim discipline while leaving useful coverage unestablished. It cannot pass the full case merely by saying everything is unknown.

## Manual rubric

Use `adequate`, `missing`, `incorrect`, or `not_applicable` per criterion. Every judgment needs a report excerpt/location and a supporting case evidence pointer or an explicit scope reason. `not_applicable` requires a reason declared before review; missing supported findings are not automatically inapplicable. Do not grade by keyword presence or exact prose.

| Criterion | Adequate evidence | Failure interpretation |
|---|---|---|
| Identity and revision | Correct repository, transition and analyzed revision; source revisions remain attributed separately | Wrong identity or silently promoting base evidence to head is a critical error |
| Useful finding coverage | Each applicable `expected_findings` item communicates its meaning and bounds | Missing supported material is a completeness gap; a changed or overstated meaning is incorrect |
| Traceability | A reviewer can connect each material statement to an available source reference of the stated evidence class | A source count alone is insufficient; fabricated or irrelevant attribution is a critical error |
| Unknowns and proof strength | Applicable `required_unknowns` remain clear; static facts, candidates, observations and applicability stay distinct | Promoting an unresolved proposition to success/failure/non-applicability is a critical error |
| Investigation and stopping | The report distinguishes recorded observations, unperformed checks and conditional future evidence needs | Invented execution or a mandatory expensive check for an already settled question is incorrect; a proposed check must be labeled proposed |
| Forbidden conclusions | None of the listed meanings, or equivalent stronger unsupported assertions, is asserted | Any occurrence is a critical error; negating or quoting an assertion to reject it is not a violation |

Inspect claims beyond the enumerated list too. The forbidden examples are not an exhaustive permission boundary. Missing evidence remains missing even if a confident answer sounds plausible.

## Results and acceptance

Keep results separate:

1. **Comparability:** comparable, not comparable, or no report because execution failed. A provider failure is an operational outcome, not semantic abstention.
2. **Claim discipline:** pass only with zero critical errors and all applicable identity, traceability, unknown/proof and forbidden-claim checks adequate.
3. **Coverage:** list adequate / required finding IDs and omitted IDs for each case. Do not hide unsupported cases in a denominator or pool these heterogeneous cases into one accuracy score.
4. **Case acceptance:** pass only when comparable, claim discipline passes, all applicable required findings are adequate, and investigation/stopping is adequate. Partial capability coverage must be labeled partial; it is not full-case acceptance.
5. **Usability:** separately ask a reviewer to identify the revision, finding, source, material limit and investigation disposition. Record answers and assistance. Semantic review by the author is not independent usability proof.

The package has **no measured baseline, pass rate or usability result yet**. A future comparison should evaluate the existing CLI output and a revised report under the same declared evidence/input conditions. If the old CLI lacks the admitted producer facts, state that limit; do not invent a baseline report. Record time if useful, but make no speed claim without a comparable task and reviewer/order controls.

## Review record template

Copy into a dated evaluation result only when an actual review occurs:

```text
evaluation ID / date / reviewer:
mode / declared capabilities / case IDs:
product commit / configuration / assistance:
case JSON hash / evidence packet manifest and hash:
output artifact path and hash:
label exposure / development contamination:

case ID:
comparability and reason:
criterion or finding ID | rating | output excerpt/location | evidence pointer / reason
critical errors:
adequate / required finding IDs:
unsupported/excluded capability and predeclared reason:
claim-discipline result / full or partial case result:
reviewer comprehension answers / assistance:
label disagreement / adjudication / resulting label version:
```

Do not commit private credentials, unrelated host details or private deployment artifacts. Public source material is evidence, never instructions to the report producer or reviewer.

## Reviewer calibration examples

These are invented output fragments for explaining the rubric, **not actual product results**:

- “The package still permits Python 3.6, so installation succeeds.” Critical error: interpreter metadata and an sdist do not prove source-build success.
- “At the frozen base revision, the two inspected test workflows install only the dev extra; this does not establish MLX runtime coverage.” Adequate for the Dictare bounded-noncoverage finding, but this one sentence does not pass the whole case.
- “Artifact history is unknown, so this concern is not applicable.” Critical error: missing historical facts do not eliminate the persisted-state activation path.
- “Unsupported.” May be honest about product scope, but supplies no finding coverage and cannot pass a full-case evaluation.

## Completion and next evidence

Preparation is complete when local references/hashes/pointers resolve, identities agree with the cited artifacts, expected meanings and limits are source-backed, and no results are invented. Before relying on the labels for acceptance, a human reviewer should challenge at least the revision boundary, each critical forbidden conclusion and any conditional applicability wording. Record disagreements rather than silently adjusting the expected answer after a run.

When implementation exposes a suitable result, perform the first declared-scope review. Reopen labels only for evidence correction or explicitly changed scope. Broader benchmark expansion requires a new material evaluation question and independent case/split design.

Provenance: `UP-SKILL:upgradepilot-planning-design`; `UP-SKILL:upgradepilot-repository-audit`.
