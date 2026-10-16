# Production Workspace and Investigator Interface Learning Artifact Refresh Plan

**Responsibility:** maintain a current, evidence-grounded learning package for the production Workspace, lifecycle host, common Investigator evidence interfaces, experiment-side mechanical adapter, and current migration frontier—without letting the package become a live-state owner or authorizing product/model work.

**Plan type:** bounded learning-artifact refresh plan. `MEMORY.md` remains the sole live project-position owner.

**Branch:** `learning/production-workspace-artifact-refresh-2026-10-16`.

**Status:** EXTENDED after newer `main` work; substantive authoring is complete through the model-free Investigator mechanical adapter. Final branch-vs-main reconciliation and QA are pending before this plan can be marked merge-ready again. Merge remains explicitly prohibited until Ali asks for it.

## 1. Snapshot history and why the plan reopened

### Initial package horizon

The first package was authored from:

```text
main@5187f40ba974341eb29d765363f093922a881803
```

At that point:

```text
production Workspace/native/host/source-interface implementation was stable
common shared input snapshot was qualified
future Investigator adapter cycle was prepared but not started
```

The branch produced Notes 1–4, the package README and the root learning-index update, then passed a first merge-readiness check.

### New main delta

A later refetch reached:

```text
main@4545d5f0b8717fb58c91e2a470aee5367b8d6846
```

Compared with `5187f40`, product `src/` and normal `tests/` remain unchanged, but `main` now adds the experiment-owned Investigator mechanical bridge and proof:

```text
experiments/investigator_workspace_adapter.py
experiments/investigator_workspace_trial.py
experiments/qualify_investigator_workspace.py
experiments/tests/test_investigator_workspace_trial.py
experiments/INVESTIGATOR_WORKSPACE_MECHANICAL_QUALIFICATION.md
working-memory/evidence/2026-10-16-investigator-adapter-mechanical/*
updated Investigator cycle/plan records
parallel adapter D/E handoff
```

This is a material learning delta even though it is not a product `src/` change. The package therefore reopened rather than merging a stale “adapter not started” learning boundary.

## 2. Package structure and horizons

Use two explicit horizons rather than silently rewriting the stable product snapshot:

```text
Notes 1–4  → product-foundation snapshot at 5187f40...
Note 5     → experiment-adapter extension at 4545d5f0...
```

This is allowed because the package now explicitly distinguishes the horizons and because product `src/`/normal `tests/` did not change between them.

### Completed foundation notes

- [x] `01_native_capture_reconstruction_and_checkpoint_publication.md`
- [x] `02_lifecycle_host_material_validity_and_execution_truth.md`
- [x] `03_frozen_sources_native_views_delivery_and_citations.md`
- [x] `04_current_product_flow_and_workspace_migration_status.md`

Notes 1–3 remain stable product learning artifacts.

Note 4 remains the product migration snapshot at `5187f40`; its old adapter-status statement is explicitly historical and superseded by Note 5/package README rather than being silently rewritten as though the adapter existed at that earlier horizon.

### New extension note

- [x] `05_investigator_adapter_mechanical_contract_packing_and_qualification.md`

It teaches:

```text
fresh assignment isolation
raw versus structured treatment restriction over common evidence
closed request/tool schemas
laboratory reference → actual product delivery mapping
search preview versus source-line strength
native whole record versus native page
product delivery versus actual consumer-visible packed input
whole-event packing and explicit omission metadata
conservative admission charges versus actual access receipts
bounded correction/failure/no-retry behavior
attributed laboratory report and unsupported semantics
procedural termination versus adequacy
offline real-input qualification on HTTPX/glyphsLib
mechanical manifest versus still-unqualified model deployment
```

## 3. New evidence route

The extension is grounded primarily in:

- `experiments/investigator_workspace_adapter.py`;
- `experiments/investigator_workspace_trial.py`;
- `experiments/qualify_investigator_workspace.py`;
- `experiments/tests/test_investigator_workspace_trial.py`;
- `experiments/INVESTIGATOR_WORKSPACE_MECHANICAL_QUALIFICATION.md`;
- `working-memory/evidence/2026-10-16-investigator-adapter-mechanical/README.md`;
- `qualification.json` and `verification.json` in that evidence packet;
- `working-memory/2026-10-16_2045_investigator-adapter-and-mechanical-qualification_lbd-cycle.md`;
- `working-memory/2026-10-16_2215_adapter-d-e-parallel-supervision.md`.

The product host/source/native contracts from Notes 1–3 remain the authority for the underlying evidence mechanics. The experiment does not become a second canonical Workspace.

## 4. Mechanical proof that may be taught

The latest adapter evidence establishes only its declared scope:

```text
13/13 new experiment controls PASS
65/65 nearest product consumer/lifecycle/host tests PASS
four real retained-input scripted assignments complete
  HTTPX raw + structured
  glyphsLib raw + structured
17 retained artifacts reverified
96 product Python hashes unchanged
0 model calls
0 native producer calls during qualification
0 forbidden execution attempts in the bounded qualifier
semantic evaluation remains unsupported
```

The related older-planner entry review has:

```text
23 pass
4 errors caused by untouched fixtures using removed segment_index construction
```

Teach this as composition/re-entry debt, not a proved planner semantic failure.

Do not claim:

```text
full product suite rerun
fresh installed suite rerun
hosted CI
model load/inference
model transport correctness
semantic usefulness
raw-versus-structured superiority
maintainer usefulness
```

## 5. Current engineering boundary represented by the package

At the extension horizon:

```text
production Workspace Stages 1–3            implemented/proven at admitted scope
common input/source/native interface         implemented/proven
mechanical Investigator adapter B            DONE
adapter scoped Verification                  GREEN
adapter D                                    CURRENT
adapter E                                    PENDING
Deployment & Model-Interface Qualification   allowed to begin in parallel under its own gates
paired semantic comparison                   not started by this evidence
product Stages 4–6 migration                 still separate and incomplete
```

Parallel sequencing does not close the adapter cycle. A material D/E contradiction remains a blocker for affected later inference/qualification.

## 6. Completed extension edits

- [x] Added Note 5 for the mechanical adapter/trial/qualification responsibility.
- [x] Updated the package README to use explicit product-foundation and adapter-extension horizons.
- [x] Updated the package mental model to include the experiment adapter and trial packing/accounting layer.
- [x] Corrected the package boundary from “adapter prepared — not started” to the evidenced B/Verification/D/E state at `4545d5f0...`.
- [x] Preserved Notes 1–4 rather than rewriting their pinned historical product claims.

The root `learning/README.md` already points to this package as the current production Workspace/Investigator-interface relearning reference. A root-index wording change is optional unless final QA shows its existing description materially contradicts the now-five-note package.

## 7. Final QA before merge-readiness can be restored

- [ ] Refetch `main` once more after the extension authoring.
- [ ] Compare latest `main` against `4545d5f0...` and classify any newer changes.
- [ ] Verify product `src/`/normal `tests/` still have no newer material change relevant to Notes 1–4.
- [ ] Verify the learning branch diff contains only this plan plus learning-package/index work.
- [ ] Verify all six package files exist and package README links Note 5 correctly.
- [ ] Verify Note 5 does not promote scripted qualification into model/semantic/usefulness proof.
- [ ] Verify current adapter D/E wording is not stronger than its owning cycle/handoff.
- [ ] Recheck whether the root learning index needs a small wording update.

## 8. Merge-readiness condition

This refresh becomes merge-ready again when:

1. final main reconciliation finds no unincorporated material learning delta;
2. the two-horizon package structure remains explicit and internally consistent;
3. branch scope remains limited to learning artifacts/index plus this plan;
4. no product/spec/ADR source is changed by this branch;
5. the package accurately distinguishes product proof, experiment mechanical proof, model/deployment qualification and semantic/usefulness proof;
6. merge remains pending Ali's explicit instruction.

## 9. Stop line

Do not from this learning branch:

- merge to `main`;
- change production `src/` or normal product tests;
- modify accepted specifications/ADRs;
- enter/repair the active adapter D/E cycle;
- enter Deployment & Model-Interface Qualification;
- load/run models or perform the paired comparison;
- repair the older planner fixture drift;
- implement Workspace migration Stages 4–6.

This plan only refreshes learning material from already-produced repository evidence.
