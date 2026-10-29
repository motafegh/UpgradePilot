# Independent experiment-subsystem reconstruction — before repair selection

Inspected main97983da3 after fetching the audit40994b0d and activation97983da3. Both are documentation-only deltas from629ede16; experiment/product code is identical. This analysis is recorded BEFORE any executable repair or organization selection. [AUDIT-013](../../../audits/2026-10-29_AUDIT-013_experiment-architecture-lifecycle-and-dependency-boundaries.md) is the selected question, not its answer.

## Inventory, graph and source boundary

[independent-inventory.json](independent-inventory.json) enumerates all127 git-tracked experiment files recursively:120 Python modules including44 under tests,3 Markdown protocols and4 JSON assets.124 ignored bytecode-cache files are separately counted and not treated as research artifacts. No nonignored untracked experiment file existed. Every Python file was AST-parsed without importing/executing it. Module docstrings, entrypoints, definitions, imports, private imports and non-test consumers are retained. The report does not infer module lifecycle from age alone.

The static graph has no cycles. Highest non-test fan-in includes workspace_revision_representation11, api_change_source_acquisition9, api_python_bindings7, evidence_gap_planner_model_boundary7, and investigator_workspace_trial5. Experimental shared infrastructure predates the new API code and is not limited to it. No non-test experiment imports tests/ or experiments/tests/. Six test-only imports intentionally borrow existing native test fixtures; they confer no production contract or runtime dependency.

There are39 private imported symbols across9 non-test source/target pairs. Eight are the new ordinary runner's imports from the curated signature trial. The other31 belong to Step6 legacy transports/evaluation, the Investigator supplied-evidence admission charge, and the Workspace volume harness's old runner fixture. Those relationships need explicit scope, not an automatic generic helper extraction across research eras.

All96 src/upgradepilot Python files were parsed. There is no static import of experiments/tests/tools and no observed eval/exec/import_module/__import__/runpy/spec-from-file/sys.path mutation call site. Raw src text search agrees; importlib.metadata in report_projection only reads distribution metadata. pyproject packages find from src and declares upgradepilot.cli:main; LangGraph is an experiment dependency group, not a native runtime dependency. No workflow config supplies another product entry into experiments. This is absence under complete checked-in Python/config inspection, not a proof about arbitrary generated/future code.

Actual dynamic operations in experiments are inspected separately: two explicit optional model-SDK site append operations and migration diagnostic imports of native operation modules for patch/oracle instrumentation. The checker's test-only exec creates locally authored syntax oracles. None is a hidden product→experiment loader. An initial overbroad text probe also matched SQL execute calls; those false positives were removed before preserving the inventory.

## Lifecycle and roles reconstructed independently

[independent-role-map.json](independent-role-map.json) classifies all127 entries with source/consumer and named owner evidence. Role and maintenance state are separate and may overlap. No historical source is declared obsolete solely because it is old, and no executable result is called frozen merely because its source hash appears in a receipt.

| Family | Actual responsibility and evidence | Classification / limits |
| --- | --- | --- |
| API source/interpretation/signature | Native input reuse, declared source acquisition, bindings, checker, candidate paths, curated/ordinary consumers; parent API plan and current retained control | Maintained experimental components/runner/reader surfaces. Possible future adoption is conditional, not native authority or an admitted new product family |
| Investigator | Workspace adapter, packing/protocol, model interface, deadline, qualification, prepared/supplied-evidence and semantic runners | Qualified experiment method plus immutable historical run evidence; no current model execution selected. Family-local protocol reuse already exists |
| CI diagnostics | current_ci_owner_diagnostic, retained_native_ci_baseline_comparison, investigator_ci_presentation | Retained/disposable diagnostic and presentation proofs, never a general product replay interface |
| Workspace research | Revision/retention representation, seam, checkpoint stores, migration/public-grounding runners | Historical architecture/proof implementations; accepted native Workspace owners now live under src. These files remain mutually reused research substrate/readers, not canonical product state |
| Evidence-gap / LangGraph | Planner boundaries, admission, transitions, local transport, framework control, historic probes | Historical bounded research with family-local reuse and explicit compatibility aliases. Language/framework comparison is not product adoption |
| Step6 support-drop | Old smoke/semantic corpus, v2 adapter, saved assessment/replay/evaluation | Historical evaluation method and fixed assets; its reused helpers are legacy scope, not default shared infrastructure for new API work |
| Report-usefulness protocols/assets | Three Markdown/JSON development/calibration contracts across report/Investigator work | Documentation/expected labels are not runtime inputs, independent utility, or semantic acceptance |
| Tests |44 modules including init, curated/ordinary/source controls, optional SDK tests and old source-hash guards | Proof roles vary. Current conformance, historical snapshot checks and optional environment checks cannot be summarized by one green API count |

Already explicit compatibility aliases include five b2_x1_evidence_gap_* modules and langgraph/r4a_control_adapters. Investigator also has local mechanical/model qualification documents. This contradicts any reading that lifecycle information is wholly absent; the missing owner is a coherent subsystem-wide index and enforceable dependency contract.

## Retention, identities and compatibility

[references-and-identities.json](references-and-identities.json) searches2,191 tracked owner/evidence text candidates. It records461 exact JSON code-hash bindings covering60 experiment source/test paths, plus exact path/module navigation references for every inventory entry. A different current source hash is historical method divergence, not automatic corruption. Existing fixed assets include source-bound recipes, case/rubric manifests and corpus hashes; leave their bytes unchanged.

API v1 currently binds five method files; ordinary v2 binds twelve. The saved reader checks exact source-key sets and saved companion/attempt/reference closure while preserving historical hash VALUES; it does not require those values to equal today's implementation. New extraction MUST bind the new support source for future production and explicitly admit the historical key sets for cold opening. Merely moving helpers while leaving their new source untracked in method identity would create a real proof gap.

Two private HTTPX/pytest v1 bundles and tracked ordinary v2 controls supply concrete compatibility obligations. Original files/results/attempts/code hashes must remain byte-identical. Fixed-data opening is allowed verification, not a reanalysis/regrade. Moving root modules would additionally break with_name/path-relative hashing, subprocess -m commands, source-bound preparation freezes and dozens of owner links. Keeping their paths is the simplest adequate baseline.

Investigator preparation and runtime/canary freezes compare current code hashes before execution. Their files are not immutable source, but changing them invalidates future execution under an old freeze. No refactor of those families or model requalification is necessary to repair the selected API sharing boundary.

## Duplication versus accidental shared infrastructure

[duplicate-body-candidates.json](duplicate-body-candidates.json) finds12 exact AST-body candidate groups (minimum12 nodes, excluding names/parameters/docstrings). These are primarily old local-model transport/extraction/JSON helpers and two Workspace statistics functions. Identical syntax is not semantic equivalence or a new reusable responsibility. Consolidating historical model methods merely to remove duplicates would expand hash/qualification scope without improving the selected consumer.

The active API issue is different: ordinary v2 intentionally consumes the SAME analysis limits, fixed source/fact/comparison decoding, terminal/source rendering and bounded IO from curated v1. Eight private helper imports plus public shared record/display functions establish a concrete two-consumer ownership need. The current shared implementation avoids duplication but is owned by a named curated runner. Extracting this one cohesive evidence-support responsibility can remove the new runner→old runner dependency. Do not extract the whole acquisition stack, all workers, or a generic serialization framework.

api_target_context_smoke already contains the coherent native-input/target orchestration reused by interpretation and ordinary source work. api_adapter_exploration contains cohesive qualified release/module examination and bounded exploration. Their names understate reuse, but explicit role/public API documentation is cheaper than relocation. api_call_signature is already an accurate checker name; being shared does not itself make it misleading.

## Test baseline — new material finding

Unchanged full experiment discovery runs591 tests, with1 failure,25 errors and11 optional-SDK skips. [baseline-tests.json](baseline-tests.json) preserves exact IDs/tracebacks/skip reasons. Initial run35.548s had truncated tool output; an unchanged second run captured structured evidence rather than inventing missing diagnostics.

Failures are existing compatibility/proof debt: the Phase3B fixture expects an old native-test blob; evidence-gap/LangGraph fixtures omit runtime_dependency_state_result or use the old segment_index constructor; Workspace replacement capture instruments removed investigation-module aliases, and one test then references an unset summary. These are not evidence the native product is broken. No failure occurs in the204-test API family. Do NOT change native owners, freeze expectations or old result verdicts just to make all research pass. Preserve the debt and explicit re-entry owner/trigger; do not silently skip, delete, relabel as green or hide it behind a new profile.

## Observation and finding adjudication

| Audit input | Independent disposition | Consequence |
| --- | --- | --- |
| O1 product boundary | CONFIRMED within full96-file AST/config search, stronger than initial bounded search | Protect mechanically; no product promotion/repair indicated |
| O2 mixed flat namespace | CONFIRMED, NARROWED: existing langgraph grouping, qualification docs and compatibility aliases already explain some roles | Add coherent index/role membership; no evidence mass folders improve ownership |
| O3 material reuse | CONFIRMED and BROADENED to older Workspace/Investigator/planner families; graph is acyclic | Document role/layer direction; no global dependency-cycle defect found |
| O4 names/lifecycle drift | NARROWED: smoke/exploration/trial modules often explicitly describe reuse; api_call_signature is well named | Reclassify/document stable path APIs; only curated-trial shared support has a concrete extraction need |
| O5 private reuse | CONFIRMED, BROADENED:39 symbols/9 pairs, not just API | Remove the8 new active API private imports through shared evidence ownership; explicitly bound the31 historical/family-local exceptions |
| O6 frozen cleanup risk | CONFIRMED, NARROWED: result bytes are immutable; source may evolve with new method closure and old reader admission | Preserve paths/assets/results, version identity-key admission explicitly and test actual historical readers |
| F1 high lifecycle gap | CONFIRMED but NARROWED to missing subsystem-wide role/dependency owner, not universal absence of lifecycle | Durable index plus complete membership/maintenance contract |
| F2 high implicit/inverted boundary | NARROWED: a runner-ownership/private API smell, not a cycle, product leak or proof that every reused module must move | One cohesive API evidence-support extraction; source-only boundary check and explicit legacy exceptions |
| F3 navigation | CONFIRMED; physical reorganization not established as useful | Goal/family navigation and explicit public surfaces; keep stable modules |
| F4 evidence risk | CONFIRMED with concrete5/12-file identity schemas and path-sensitive producers | Historical and current source closures supported deliberately; no rewriting freezes |
| F5 product guardrail | CONFIRMED | Shared experimental substrate remains outside src; separate native adoption still required |
| Additional finding | Broad research suite has existing compatibility failures and optional proof gaps | Retain exact baseline; name owners/triggers and require no new failures, without gratuitous historical repair |

Independent gate is complete: inventory, graph, lifecycle/role evidence, identities/navigation, dynamic/package boundary, duplication and test debt are preserved. No executable repair preceded this artifact. Next is bounded design selection under Ali's combined authorization; the analysis does not itself silently select a folder layout or accept source/API changes.
