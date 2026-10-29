# Experiment organization and dependency repair — evidence and disposition

## Independent analysis preceded selection

The selected [AUDIT-013](../../../audits/2026-10-29_AUDIT-013_experiment-architecture-lifecycle-and-dependency-boundaries.md) was not treated as established truth. Fetch found two audit-only commits after629ede16 and fast-forwarded to97983da3. [Independent analysis](INDEPENDENT_ANALYSIS.md), full127-file recursive inventory, static graph, role evidence,461 historical identity bindings across60 paths, duplicate-body candidates and the actual broad test baseline were preserved/pushed ata1d994cb BEFORE design or source repair. [Bounded selection](../../../plans/EXPERIMENT_ORGANIZATION_AND_DEPENDENCY_BOUNDARY_REPAIR_PLAN.md) was then published atc5601c7e; implementation followed at59625ff2.

Every observation and finding is explicitly adjudicated in the analysis. Important corrections: product direction is intact; the graph is acyclic; reuse/private helpers predate API work; existing qualification docs/compatibility aliases already provide some lifecycle information; api_call_signature is accurately named. Neither a mass folder move nor automatic product promotion was justified.

## Explicit subsystem model now implemented

- [README](../../../experiments/README.md) owns family navigation, role meanings, public reuse, maintenance versus execution/frozen authority, dependency rules and historical debt.
- [Role inventory](../../../experiments/role_inventory.json) classifies all131 resulting artifacts and names family/owner/maintenance/roles. It is complete recursive membership, not a dated imported graph or another live-state owner.
- [Static checker](../../../tools/check_experiment_boundaries.py) parses the actual tree/config and checks inventory/owners, family/layer/private direction, cycles, runtime-test separation and product/package boundary. New metadata/source requires deliberate classification. It imports no inspected code, repairs nothing and is not a semantic/security sandbox.
- [Boundary controls](../../../experiments/tests/test_experiment_dependency_boundaries.py) include negative controls and an actual-repository check, so ordinary experiment test discovery exercises the real registry/graph as well as the verifier's rejection behavior.
- Stable module/CLI/asset paths remain. No new generic framework, product dependency, native family, folder migration, re-export migration forest or source-association authority was introduced.

There are31 deliberately scoped pre-existing private-symbol exceptions in legacy Step6, Investigator protocol charging and Workspace volume controls. Each exact source/target/name is recorded; new or stale exceptions fail. This is documented family-local debt with a re-entry requirement, not endorsement for new consumers. Existing B2/X1 and LangGraph compatibility aliases remain historical-name surfaces.

The first draft classifier wrongly treated api_adapter_context_replay as only a runner. Source inspection established decode_adapter_seed as the public retained-binding decoder used by interpretation. Its substrate/reader role and API are now explicit; no gratuitous extraction or rewrite was needed. Conversely, the signature runner's private-helper coupling had a concrete identical two-consumer responsibility and was repaired.

## Shared evidence repair and historical identity

[api_signature_evidence](../../../experiments/api_signature_evidence.py) owns the limits, bounded IO/digests/text/spans, fixed record/source/comparison decoding and terminal/source display shared by curated v1 and ordinary v2. Its public names replace the ordinary runner's8 private imports. The curated runner retains selection/attempt/CLI and existing public imports for compatibility; ordinary now depends directly on evidence support. Parsing, source relationships, argument comparison, acquisition and each attempt protocol remain at their existing owners.

[Structural and saved compatibility evidence](shared-support-compatibility.json) confirms19 moved definitions have identical AST after public-name/docstring normalization. Actual original HTTPX/pytest v1 bundles and three retained v2 controls open with AST/network/checker forbidden. The ten private frozen members are byte-identical. Current/future producers bind the support hash: curated current6 keys versus historical5; ordinary current12 replaces the curated runner key with support, while historical12 remains admitted. Fixed variants do not allow arbitrary missing/extra method sources. No old hash values, source text, result, label, recipe, freeze or verdict were rewritten.

[The newly labelled controlled attempt](controlled-post-repair/view.txt) is compared with the prior ordinary saved control in [controlled-behavior-comparison.json](controlled-behavior-comparison.json). Exact target, source/fact records, pairs/comparisons, work, coverage, module roles, discovery paths/premises and proof class are identical. Its source companion is byte-identical. Only method identities and ordinary attempt/acquisition metadata differ as expected. Sampled wrapper remains bound, native old app reception bound, proposed app reception rejected under the same saved premises. One initial observation, no identity-only refetch. This is controlled-provider composition and fixed-data contrast, not a fresh real-PR acquisition or independent semantic evaluation.

## Verification and explicitly retained debt

API suite:206 tests pass, including2 new current-method closure controls. Boundary suite:7 tests (six focused policy controls plus actual repository conformance). Static current graph:131 artifacts,122 Python modules,255 unique internal import edges,31 exact legacy private symbols,96 inspected native Python files; check passes with no cycles/reverse product dependency.

[Baseline](baseline-tests.json):591 tests,1 failure,25 errors,11 optional-SDK skips. [First post-repair](post-repair-tests.json):599 tests, same failure/error/skip identities, eight added tests. [Final broad receipt](final-regression-tests.json):600 tests/39.387s, adding the real-repository gate, with exact failure/error identities AND messages and skip identities matching that same baseline. Neither a green full suite nor repaired historical conformance is claimed. [Final verification](verification.json) binds source/test/model/control identities, boundary results, compatibility and unchanged old artifacts.

Named debt remains: Phase3B old source blob; planner/LangGraph obsolete native result/CI fixture constructors; Workspace replacement capture of removed investigation aliases and subsequent unset-summary failure;11 optional SDK cases unproven without separately selected SDK. Re-enter their planner-comparison or Workspace research/migration owners before current-contract reuse. Do not weaken product contracts, delete/skip old tests, change the original expected result or rerun frozen model work to hide the debt. This bounded organization repair is not their requalification.

No src, native tests, product packaging, specification or ADR changed. No new full product run is claimed. No real provider acquisition, model loading/inference, target code/workflow execution, old analysis replay/regrade or external-target mutation was performed. Git publication and controlled unit/worker/static-reader operations are the exercised actions.

## Finding resolution and expansion gate

| Finding | Disposition / stronger owner |
| --- | --- |
| F1 missing subsystem role/lifecycle model | ABSORBED as narrowed: README plus full role registry; existing local lifecycle documentation retained |
| F2 implicit/private/inverted ownership | ABSORBED as narrowed: explicit acyclic family/layer model, direct shared signature evidence, exact legacy exceptions and static rejection controls |
| F3 navigation/physical grouping | ABSORBED: goal/family navigation and public API table; physical relocation rejected on actual compatibility cost, not deferred cosmetic work |
| F4 reproducibility risk | ABSORBED: stable paths/assets, current/historical source-key schemas, actual frozen cold-reader checks and unchanged original hashes |
| F5 product-promotion guardrail | ABSORBED: explicit reusable experiment category, src-only direction/packaging check, native adoption still separately owned |
| Additional historical test debt | PRESERVED explicitly with baseline, owners and re-entry trigger; no concealment or automatic archaeology |

The selected gate is satisfied: an engineer can identify each artifact's purpose,
maintenance/role, allowed reuse, authority and affected historical evidence. No substantial
protocol/factory expansion occurred during this repair. Future API work must follow the
explicit public support/model and maintain membership/dependency checks; it still needs
its own scope/proof, then live allocation and native-adoption decisions. Audit absorption
does not establish semantic usefulness, installed/runtime compatibility, full Workspace
migration, maintainer action permission or independent learner mastery.

## Later learning route

Use the [single cycle](../../2026-10-29_experiment-lifecycle-and-dependency-repair_cycle.md) to reconstruct why source inspection changed the audit interpretation, why an acyclic graph can still have poor API ownership, why a source file and its frozen result have different lifecycle, how fixed identity variants preserve old reading while binding new code, and why baseline research failures must remain visible without blocking unrelated verified repairs. Follow ordinary runner→shared evidence→unchanged checker/native primitives and compare old/new controlled data. Independent practice/learning remains deferred; this record does not certify mastery.
