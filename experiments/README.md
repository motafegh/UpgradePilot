# Experimental methods, evidence and supported reuse

This directory owns non-product research/evaluation implementations. It contains
reusable experimental components as well as runners, retained readers, source-bound
assets and historical compatibility surfaces. An old result, a reusable module and
an adopted product capability are different things. Native implementation authority
belongs to `src/upgradepilot/`; [MEMORY](../MEMORY.md) alone selects live work.

[role_inventory.json](role_inventory.json) is the exact artifact/family/role/maintenance
index. This README owns the meaning and dependency policy, rather than a second live
roadmap. The [independent reconstruction](../working-memory/evidence/2026-10-29-experiment-lifecycle-and-dependency-repair/INDEPENDENT_ANALYSIS.md)
records the pre-repair evidence and corrections to AUDIT-013; the
[repair plan](../plans/EXPERIMENT_ORGANIZATION_AND_DEPENDENCY_BOUNDARY_REPAIR_PLAN.md)
owns this bounded transition and proof.

## Navigation by responsibility

| Family | Start here / normal responsibility | Authority and lifecycle limit |
| --- | --- | --- |
| API source and comparison | [ordinary driver](api_ordinary_call_signature_trial.py), [target/source composition](api_target_context_smoke.py), [correspondence](api_source_correspondence.py), [shared evidence](api_signature_evidence.py) | Maintained experimental path; controlled/retained proof is distinct from fresh acquisition and native adoption |
| API interpretation | [source interpreter](api_change_interpretation.py), [ordinary interpretation composition](api_change_interpretation_trial.py), [evaluation runner](api_change_interpretation_evaluation.py) | Attributed proposals, not product findings; old semantic outputs/freezes are not automatically rerunnable |
| Investigator qualification | [adapter](investigator_workspace_adapter.py), [protocol/driver](investigator_workspace_trial.py), [interface](investigator_model_interface.py), [deadline](investigator_run_control.py), [qualification contract](INVESTIGATOR_MODEL_INTERFACE_QUALIFICATION.md) | Family-local experimental APIs; qualification, supplied-evidence, semantic acceptance and usefulness are separate. No model execution is selected by this index |
| CI diagnostics | [owner diagnostic](current_ci_owner_diagnostic.py), [retained baseline](retained_native_ci_baseline_comparison.py), [presentation](investigator_ci_presentation.py) | Disposable retained/fresh diagnostic contracts, not a public product replay interface |
| Workspace research | [revision representation](workspace_revision_representation.py), [seam](workspace_investigator_seam.py), [checkpoint stores](workspace_checkpoint_stores.py), [replacement capture](workspace_replacement_migration.py) | Historical design/proof substrate. Accepted native Workspace implementations/ADRs are the product owners; these modules are not canonical state |
| Evidence-gap planner / LangGraph | [model boundary](evidence_gap_planner_model_boundary.py), [admission](evidence_gap_action_admission.py), [transition](evidence_gap_investigation_transition.py), [workflow](langgraph/evidence_gap_workflow.py) | Historical bounded comparison; old B2/X1 re-export modules and r4a_control_adapters preserve names, not new reuse permission |
| Support-drop evaluation | [old smoke](step6_support_drop_smoke.py), [contract v2](step6_support_drop_contract_v2.py), [assessment](step6_support_drop_contract_v2_assessment.py) | Historical source-bound evaluation method/corpus. Do not merge it into another family's transport or rerun a freeze to make cleanup green |
| Report development evaluation | [protocol](EVIDENCE_REPORT_DEVELOPMENT_EVALUATION.md), [cases](evidence_report_development_cases.json), [calibration](evidence_report_rubric_calibration.json) | Expected/forbidden labels and exposed development evidence; never inject them into a normal producer or call them independent utility |

## Roles and safe dependency direction

Roles overlap: `substrate` is a family-owned reusable implementation; `composition`
joins existing responsibilities; `runner` owns an attempt/CLI; `reader` opens fixed
historical data; `compatibility_alias` preserves an old import; `diagnostic` is a
bounded developer proof; `protocol` and `retained_data` describe non-code contracts
and assets; `test` owns proof. `component` covers an experiment-local implementation
that is not a separately supported reusable API. Maintenance describes historical
research, qualified experiment methods, maintained development, retained diagnostics
or assets. It does not claim live execution selection, semantic acceptance, immutable
source files or product admission. No product-adoption candidate is admitted by
multiple consumers; the API plan's future adoption remains a separate contract.

```text
family runner → family composition/substrate → native product primitives
family saved reader → family evidence support → native source/representation primitives
experiment tests → experiment/product code and explicitly borrowed test fixtures
product runtime ↛ experiments / tests / tools
```

Runtime imports stay within the named experiment family or use native/external
libraries. New cross-family reuse requires an explicit responsibility and dependency
review; the current registry admits none. API substrate cannot depend on its runner,
and an API runner must not import another runner unless that module explicitly owns
a reusable composition or substrate responsibility. Existing historical paths are retained when
their public role is coherent; a `smoke` suffix is not an instruction to duplicate it.

Private names are module implementation details. New cross-module private imports
are rejected. The registry lists31 exact pre-existing private-symbol exceptions in
historical Step6, Investigator protocol charging and Workspace volume controls.
They are closed compatibility debt, not permission to extend or expose those helpers.
Re-enter their owner before new consumers or semantic changes. Tests may inspect
private behavior for a specific boundary without making it a supported runtime API.

## Explicit reusable API surfaces

| Owner | Supported experimental responsibility | Not supplied |
| --- | --- | --- |
| [acquisition policy/session](api_change_source_acquisition.py) | TrialAcquisitionPolicy, TrialPublicSession.stage/acquisition_receipt/finish_acquisition: explicit local transport work, reserved stages, decoded-body accounting and cooperative deadline | GitHub account quota, hard preemptive cancellation, useful complete coverage or permission for a live attempt |
| [api_signature_evidence](api_signature_evidence.py) | AnalysisLimits; bounded IO/digest/text/span admission; fixed source/fact/comparison decoding; terminal/comparison/source projection; explicit method-source sets | Acquisition, call pairing, checking, attempt execution or product truth |
| [api_call_signature](api_call_signature.py) | extract_python_source, compare_arguments and source/argument/signature records | Effective runtime dispatch, installed versions or whole-update compatibility |
| [api_python_bindings](api_python_bindings.py) | analyze_python_bindings, facts/assessments/traces and their fixed representation | General interprocedural/object-flow resolution or condition activation |
| [api_target_context_smoke](api_target_context_smoke.py) | PublicPRContextTrial, acquire_public_pr_context, observed changed-module requests and manifest projections | A second native investigation, source correspondence or general replay interface |
| [api_adapter_exploration](api_adapter_exploration.py) | AdapterSourceExplorer/source_run, exact module requests/results, bounded samples and per-run work | Installed namespace, effective dependency resolution or release-artifact byte equivalence |
| [api_change_source_acquisition](api_change_source_acquisition.py), [target context](api_target_context.py), [window projection](api_release_window_manifest.py) | Existing qualified source/target providers, problems and source-window projection | Stronger product source authority or automatic interpretation |
| [adapter saved-input reader](api_adapter_context_replay.py) | decode_adapter_seed admits the existing saved binding/target representation for interpretation and component replay | No fresh PR execution, semantic authenticity or new binding inference; its replay CLI is a separate use of these decoded facts |
| [curated signature runner](api_call_signature_trial.py) | prepare/run/read/open curated v1, existing public limits/render imports for compatibility | Shared-owner placement for new consumers; use api_signature_evidence directly |

Other families' reuse is scoped to their declared protocol and owner; consult the
inventory, module docstring, family plan and qualified method before depending on
them. A public Python name alone is not qualification for a new responsibility.

## Ordinary acquisition attempt lifecycle

The ordinary driver owns `prepare_fresh_execution_freeze`,
`run_fresh_ordinary_pr_attempt` and `open_fresh_ordinary_pr_attempt`. The first
returns code/config/runtime/contract snapshot bytes without reading a credential
or activating execution. The runner requires the frozen operational contract and
matching execution snapshot. Its selected destination must be unused under an
existing owner-only directory; an explicit owner-only credential file is read only
after immutable outer start retention. Ambient credentials are not inherited.

`controlled_qualification` exercises the same lifecycle with the controlled proof
class. `live_activation` requires explicit caller activation as well as matching
code/configuration; this interlock never grants user authorization. There is no
automatic retry, cap enlargement or live CLI shortcut. The existing analysis
worker remains separate in `comparison/`. Completed stage captures and returned
module text survive handled acquisition failures; abrupt process loss may leave
unknown completion and lost intermediates, which are never reconstructed as facts.

Offline CLI `open-attempt --result DIRECTORY` admits outer identities, retained
digests, initial observation, input and inner worker relations without acquisition,
AST parsing, discovery or checking. It exposes incomplete/unknown states. Useful
paired native-version comparisons, useful partial evidence and insufficient
evidence are separate from procedural completion and complete coverage. These
experimental artifacts are not native Workspace checkpoints or action authority.

## Historical identity and frozen evidence

Keep result/source/attempt/freezes/labels bytes unchanged. Source code may evolve,
but a source-bound old freeze does not authorize new execution after its code changes.
Read supported saved records without AST/provider/model/checker/synthesis reruns.
Matching hashes show integrity, not authenticity or semantic entailment.

Signature v1 supports its historical five-source closure and current six-source
closure. Ordinary v2 supports the historical twelve-source set and current twelve-source
set with shared evidence replacing the curated runner. New producer/attempt hashes
include api_signature_evidence.py. These fixed variants do not admit arbitrary missing
or extra method sources. The runner/module paths and old format/proof classes remain
stable; method values in historical results are never silently refreshed.

Correspondence method1 retains direct/re-export/initializer source paths. Method2
adds the bounded module-allocation/getter/returned-class/call-protocol family at
api_source_correspondence. Its source steps and constructor/attribute/branch/receiver
premises remain conditional; no object is executed or generally typed. The ordinary
reader admits both fixed versions and refuses protocol steps labelled as method1.

Staged acquisition is opt-in through a shared TrialPublicSession(policy=TrialAcquisitionPolicy(...)).
Legacy sessions retain local50 behavior. New policy defaults are50 GitHub/100 all-provider
attempts,8MiB decoded response/32MiB aggregate,180s cooperative elapsed limit,24 GitHub
requests reserved from early target/window stages,16 target file attempts and2 adapter
candidate attempts. These are experimental work selections, not immutable product limits
or GitHub/token quotas. Explicit finite qualification ceilings are200/400 requests,8/64MiB,
300s,200 target files and12 adapter candidates. A larger selection is not live authorization.
Source-run4-release/12-module/2MiB and checker limits remain separate.

Inventory-first selection prioritizes declarations and PR-observed changed Python paths;
direct native-version sources precede adapter samples. Internal closure prioritizes observed
target names and acquired source call/base references; it remains a heuristic with visible
unexamined alternatives. Policy receipts bind auth mode (never values), stages, attempted
requests, decoded body bytes, status/failure and elapsed work. Response streaming is charged
before provider JSON decoding; complete bounded bytes remain readable through Requests'
normal Response API. Oversize/late/failed reads remain charged and close their responses.
The deadline clamps socket timeouts and checks monotonic time before/after/chunk reads;
it refuses late acceptance but is not a hard preemptive total-runtime cancellation guarantee.
No policy or source-selection improvement establishes installation, dispatch or compatibility.

Do not relocate modules/assets merely to group files: with_name lookups, subprocess
module commands, frozen code lists and historical links are real compatibility costs.
No generic common framework or src promotion follows from this organization model.

## Verification and explicit historical debt

Run the static inventory/import/package check from the repository root:

```sh
.venv/bin/python3 tools/check_experiment_boundaries.py
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src:tests:. .venv/bin/python3 -m unittest discover -s experiments/tests -p 'test_api*.py' -q
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src:tests:. .venv/bin/python3 -m unittest experiments.tests.test_experiment_dependency_boundaries -q
```

The checker parses source; it does not import experiments, execute a model/target,
authenticate, repair files, enforce semantic truth or provide a security sandbox.
Membership/private exceptions are exact; new artifacts or dependencies require a
deliberate registry/owner update. Keep the registry and actual graph aligned.

Full discovery remains visible:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src:tests:. .venv/bin/python3 -m unittest discover -s experiments/tests -q
```

At the independently recorded97983da3 baseline this runs591 tests with1 failure,
25 errors and11 optional preserved-SDK skips. [Exact baseline](../working-memory/evidence/2026-10-29-experiment-lifecycle-and-dependency-repair/baseline-tests.json):
Phase3B old source-blob guard; evidence-gap/LangGraph old native result/CI constructor
fixtures; Workspace replacement instrumentation of removed investigation aliases
and a resulting unset-summary error. These are explicit current compatibility debt,
not healthy conformance and not native product failures. They are not skipped,
deleted or regraded here. Re-enter the planner comparison or Workspace research/
migration owner before reusing those paths against current product contracts.
Current API/boundary proof must pass, and broad regression must have no unexplained
new failures. Optional SDK proof remains unavailable unless separately selected.
