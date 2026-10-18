# AUDIT-011 — Investigator experiment validity, bottlenecks and useful progress

**Audit date:** October 18, 2026, Asia/Tehran.

**Inspected main revision:** `e0a6de39` (`Finalize immutable retention and incomplete B evidence handoff`).

**Mode:** independent, source-backed Audit / Review.

**Authority:** non-controlling evidence and recommendations. Implementation, another inference batch, experiment redesign and adoption require a subsequent decision. Lifecycle selection is recorded in the [audit indexes](README.md); [MEMORY.md](../MEMORY.md) owns live continuation.

## 1. Assessment

There is evidence for Ali's concern that the present route is spending too much effort on experiment machinery relative to useful investigation output. The evidence does **not** establish that these models cannot handle dependency-update analysis, that native evidence is ineffective, or that the accepted hybrid architecture should be abandoned.

The immediate problem is a combination of:

1. **A controller that permits discovery to consume the capacity needed to publish an evidenced result.** This affected an actual complete report attempt and constrains the observed native navigation path.
2. **Insufficiently specified navigation and decision guidance.** Qualification gives exact actions and path syntax; real investigation receives a generic goal and schema-only tools. A qualified model repeatedly failed a routine addressing operation.
3. **A costly evidence interface.** Whole native JSON records need many character pages; inventories and repeated history consume substantial input and local runtime. More evidence can make completion harder under the same limits.
4. **Real semantic failures.** The complete reports make unsupported low-risk judgments and confuse unexamined evidence with unavailable evidence. Citation repair does not address these failures.
5. **An experiment that combines too many possible failure causes to efficiently identify the next useful change.** It compares autonomous discovery plus interpretation plus stopping plus reporting before the simpler interpretation capability has been isolated under the current conditions.
6. **Incomplete run control and evidence.** The batch was interrupted by an erroneous operator measurement; the SDK does not enforce a hard total prediction deadline, and an additional interruption-state defect is reproducible offline.

The evidence-preservation and strict reference work is valuable and should be retained. It has made this audit possible. However, additional qualification rounds, fixtures or model candidates are useful only if they discriminate a particular cause or protect a necessary boundary. They are not progress toward a useful report merely because they pass.

**Engineering recommendation:** first make a bounded run reliably controllable and affordable to complete; then select a small diagnostic experiment that separates evidence interpretation from discovery. Use the current cases as development material, and require new evidence before claiming an improvement. Do not automatically repeat the full 12-assignment batch or add agents/models/native families.

## 2. Scope, evidence and independent checks

### Included

- The current Investigator adapter, trial driver, stateless model boundary, interface qualification and semantic comparison orchestration.
- Their product Workspace source/native delivery boundary and relevant focused tests.
- The reference-v2 freeze, actual qualification artifacts, every attempted semantic request and its complete response or incomplete-call metadata, reports, refusals and resource receipts.
- Both common retained source catalogs, decision-relevant source passages and native payload shapes.
- The preceding qualification/budget/reference lineage where needed to understand expenditure and why current gates exist.
- Experimental validity, bottlenecks, report quality, useful fixtures, simpler alternatives and the next decision.

This is not an exhaustive audit of every historical experiment, all product modules, the older planner, replay/recovery, or maintainer usefulness. Those are separate responsibilities. Historical source-interpretation and report-evaluation machinery was inspected for reuse context; it was not rerun or treated as a control for the new freeze.

### Main implementation chain

| Layer | Actual owner and responsibility |
| --- | --- |
| Product purpose | [Charter](../PROJECT_CHARTER.md): useful, provenance-backed dependency-update decisions with uncertainty; no automatic target action |
| Experiment question | [Integration/comparison plan](../plans/INVESTIGATOR_INTEGRATION_AND_COMPARATIVE_EVALUATION_PLAN.md), [three-deployment amendment](../plans/INVESTIGATOR_SEMANTIC_COMPARISON_THREE_DEPLOYMENT_AMENDMENT_2026-10-17.md) |
| Common input | Qualified retained checkpoints/catalogs; fresh assignment composition in `load_case_assignment` |
| Product evidence delivery | [consumer_access.py](../src/upgradepilot/workspace/consumer_access.py), [source_access.py](../src/upgradepilot/workspace/source_access.py) |
| Tool/reference/report wire | [investigator_workspace_adapter.py](../experiments/investigator_workspace_adapter.py): `InvestigatorAssignment` |
| Packing, operations and termination | [investigator_workspace_trial.py](../experiments/investigator_workspace_trial.py): `pack_input`, `run_scripted_trial` |
| Render, grammar, model usage and retained calls | [investigator_model_interface.py](../experiments/investigator_model_interface.py): `measure_input`, `SDKBinding.predict`, `StatelessInvestigatorModel` |
| Synthetic admission | [qualify_investigator_model_interface.py](../experiments/qualify_investigator_model_interface.py): `canary_protocol`, `assess_canary` |
| Frozen batch execution | [run_investigator_semantic_comparison.py](../experiments/run_investigator_semantic_comparison.py): `verify_freeze`, `require_qualification`, `execute_comparison` |
| Semantic judgment | Offline review; neither grammar, adapter publication nor procedural finish performs entailment/adequacy evaluation |

### Fresh verification in this audit

The [offline audit program](../working-memory/evidence/2026-10-18-investigator-independent-audit/offline_audit.py) and its [results](../working-memory/evidence/2026-10-18-investigator-independent-audit/offline-results.json) are new audit derivatives. They do not overwrite an experiment output.

| Check | Fresh result | Limit |
| --- | --- | --- |
| Original reference-v2 retention | All **1,111 files / 35,347,347 bytes** match indexed membership, size, SHA256 and file modes; directory modes also pass. Index SHA256 `2444de93ddff7a3d061aae1273983f37a561bd56769f0495cdbe45a35a99e9a3` | Local integrity; not an off-machine backup or proof of semantic truth |
| Current freeze and admission | Existing offline verifiers revalidate **60 bound files**, **17 common input files**, product source basis and immutable qualification admission | Reuses the experiment's verifier; complemented by independent artifact checks |
| Independent call reconciliation | **60 qualification + 45 semantic requests** examined; all **104 known-usage** calls agree on retained input/rendering hashes, actual prompt tokens, usage totals, applied settings, instance, visible response/prefix and offered typed references | No fresh tokenization/model execution; one semantic usage remains unknown |
| Experiment/nearest seam suite | **123 tests pass**, 4.719 seconds | Deterministic substitutes; no actual model competence claim |
| Nearest product Workspace suite | **65 tests pass**, 20.623 seconds | Focused integration proof; not the full product suite |
| Deadline counterexample | Fake binding returns at monotonic **1801 seconds** after receiving `timeout=1800`; wrapper records `returned` | Demonstrates wrapper behavior, not a historical model overrun |
| Actual Python interruption counterexample | `KeyboardInterrupt` leaves `usage_complete=True` and receipt `usage:null`; direct object reuse permits another call | Actual CLI unwound; no subsequent historical call is alleged |
| Independent source review | Read actual declarations, consumer/test-client paths, HTTPX/Starlette source, workflow/tox/regression routes, historical CI captures and changelog availability | Static/capture evidence; no target installation or execution |

Commands actually run:

```bash
PYTHONPATH=src:. .venv/bin/python -m unittest experiments.tests.test_investigator_workspace_trial experiments.tests.test_investigator_model_interface experiments.tests.test_workspace_investigator_seam -q
PYTHONPATH=src:tests:. .venv/bin/python -m unittest test_workspace_consumer_access test_workspace_lifecycle_publication test_workspace_host_integration -q
PYTHONPATH=src:. .venv/bin/python working-memory/evidence/2026-10-18-investigator-independent-audit/offline_audit.py --output working-memory/evidence/2026-10-18-investigator-independent-audit/offline-results.json
```

Also invoked `verify_freeze`/`require_qualification` directly against the retained private semantic freeze with SHA256 `d9ec5c86f341f095cece29f9717c2fb1f9c9fb29f9661293e34a509d4b65bbe1`. These checks make no model or acquisition calls.

No new inference, model loading, target execution, dependency installation, product/experiment repair or full-suite/hosted validation was performed. Original private roots were read only. No hidden reasoning was inspected. Review is AI-assisted and source-aware; this is an independent pass over evidence, not independent human or blinded acceptance.

## 3. What the latest results actually establish

### Sequence of material changes

The previous deployment/interface cycle closed through E. A successor added model-visible budget metadata and qualified the intended real-case settings. That cohort failed two strict citation sequences: **10/12 passed; 62 calls; no semantic assignments**. The failed outcomes were retained.

Reference-v2 then constrained citations to request-local offered `(kind,id)` pairs and made uncitable observations explicit. Its **12/12 qualification sequences passed in 60 calls**. This repair improved wire reliability at those exact points. It did not test or repair discovery, entailment, calibration or useful stopping.

The semantic comparison attempted the first four assignments before interruption:

| Assignment | Actual result | Calls / known input / known generated | Independent assessment |
| --- | --- | --- | --- |
| Gemma12 HTTPX Raw | Operation limit; no report | 12 / 144,345 / 550 | Seven dispatched reads use a redundant source prefix; an eighth requested read is refused. This is failed navigation and completion, not evidence exhaustion. |
| Gemma12 HTTPX Structured | Complete published report | 9 / 86,125 / 990 | Correct declaration transition; unsupported basic-request/low-risk premise; falsely says changelog was outside the source universe. No native reads occurred. |
| Qwen27 glyphsLib Raw | Complete report attempt; publication refused | 12 / 212,257 / 1,571 | Correct pin/lower-bound facts; insufficient report reserve; unsupported low-risk statement; false broad claim that execution results are unavailable. |
| Qwen27 glyphsLib Structured | External interruption during report call | 12 attempts / 121,085 known input / 469 known generated | Eleven returned calls plus one unknown-usage attempt. Native evidence was delivered. No complete report exists to grade. |
| Remaining eight assignments | Unattempted | No calls | Includes **all E4B semantic assignments**; no semantic E4B conclusion is available. |

“Three completed assignments” means three terminal trial outcomes, **not three completed reports**. There is **one published complete report**, one complete unpublished report attempt, one terminal run without a report, and one interrupted run without a complete report. The published report is not semantically accepted.

The two complete report texts each address only **one of six preregistered obligations** at the recorded supported-coverage level. This is an obligation-coverage result, not 16.7% factual accuracy. Qwen's report contains several correct factual statements. The existing reviews enumerate 41 atomic proposition occurrences across both reports; repetitions and multiple surfaces are not independent samples.

The incomplete matrix cannot establish Raw/Structured benefit, deployment ranking, reliability, or usefulness. Gemma's report-completion difference cannot establish native benefit because it never used native tools. The changed tool menu could itself affect behavior, but that is unmeasured.

### Cost and progress

Reference-v2 alone spent **105 attempts**: 60 qualification and 45 semantic. Known totals are **1,318,536 input / 24,417 target-generated tokens**, with one additional unknown-usage attempt. Earlier cohort costs remain separate in their own evidence records.

Historical accounting from [r8](../working-memory/evidence/2026-10-17-investigator-model-interface-r8/final-accounting.json), the [62-call predecessor](../working-memory/evidence/2026-10-18-investigator-semantic-comparison/completed-matrix-checkpoint.json), and reference-v2 yields **460 qualification attempts plus 45 semantic attempts** in this recorded lineage. Approximately **91.1% of attempts were qualification**. Known reported usage across that lineage is 6,003,253 input / 129,760 target-generated tokens; two attempts have unknown usage. Older raw cohorts were not comprehensively reaudited here, so this is reconciled historical accounting rather than a fresh audit of all 505 calls.

This does not mean qualification was worthless or all earlier effort was avoidable. Runtime changes, rendering defects and reference failures were real. It does show that the present bottleneck is converting valid interfaces into useful investigation, and that another full requalification cycle needs a clear information benefit.

## 4. Findings

Priorities describe project consequence: **P1** materially blocks useful or interpretable progress; **P2** is a consequential limitation or repair prerequisite. They are not claims of deployed production incidents.

### AUDIT-011-F1 — P1: completion affordability is disclosed but not protected

**Observed:** `trial_budget_observation` discloses finish=3, report=4+unique references, termination=1. `run_scripted_trial` reserves only termination. Discovery remains admissible while it can make an evidenced report impossible. Report cost is checked only **after the model generates it**.

For Qwen Raw, ten discovery operations cost 40, finish cost 3, leaving 5. Five unique report citations cost 4+5, plus termination=1: **10 required versus 5 available**. The 914.83-second client report call produced content the controller then refused before publication. Reducing the report to zero citations could fit the numeric remainder; that would not provide the intended evidenced output.

The existing `test_spare_calls_do_not_make_read_plus_completion_affordable` correctly proves refusal. It does **not** prove a useful controller prevents reaching that state. The protection is currently a loss-containment boundary, not completion planning.

**Consequence:** a high-evidence run can fail more readily than a shallow report. Unpublished reports also lack ordinary trial-level publication/evaluation state, though their original bytes remain available for review.

**Disposition:** design an explicit completion allowance across operations, calls, token reserve and deadline. Credible options are a declared citation allowance, a bounded intended-reference set, or reserving all eligible references. Reserving all seen references is simple but can prematurely stop discovery because inventories/repeated reads also create references. A chosen subset needs an honest procedure and must not suppress inconvenient evidence. Forced resource termination must remain distinct from a claim of adequate investigation. Do not silently change the old freeze or lower citation standards.

**Evidence:** `investigator_workspace_trial.py:122`, `:266`, `:404`; original Qwen Raw calls 11–12 and assignment charges; offline results.

### AUDIT-011-F2 — P1: timeout does not enforce total prediction or trial elapsed bounds

**Observed:** `SDKBinding.predict` sets the SDK synchronous timeout, then blocks in `wait_for_result`. Installed SDK 1.5.0 `SyncChannel.rx_stream` gives each received-message wait that timeout. Continuous activity can therefore extend a prediction beyond it. The wrapper has no monotonic cancellation watchdog; the trial checks elapsed time before and after a consumer call, not during it.

The deterministic 1801-second late-return probe is accepted. Installed-source behavior agrees with the [official SDK timeout documentation](https://lmstudio.ai/docs/python): synchronous timeout measures inactivity. [Official cancellation guidance](https://lmstudio.ai/docs/python/llm-prediction/cancelling-predictions) documents explicit cancellation and the importance of finishing stream iteration to obtain available partial/final metadata.

**Historical correction:** the interrupted actual call's retained monotonic duration is **1740.471 seconds**, below 1800. The operator used file-timestamp request age and stopped too early. This audit confirms a missing hard control, **not an actual historical timeout**. The clock-domain discrepancy's cause remains unknown.

**Disposition:** use one authoritative monotonic deadline, explicit cancellation, a bounded cleanup/drain phase, and separate fields for request preparation, prediction, assignment and batch elapsed time. A cancellation request is not confirmation that server work stopped. Preserve unknown usage if no trustworthy receipt arrives. Test both continuous fragments and silence; checking only fragment callbacks cannot enforce a deadline during silence.

**Evidence:** `investigator_model_interface.py:300`, `:551`, `:606`; installed SDK `sync_api.py:217`, `:227`, `:983`; interruption receipt and fresh counterexample.

### AUDIT-011-F3 — P2: real interruption bypasses usage-state and terminal-result bookkeeping

**New independently reproduced defect:** `StatelessInvestigatorModel.__call__` updates `usage_complete` in `except Exception`. Python `KeyboardInterrupt` bypasses it. `finally` writes an attempted receipt with `usage:null`, but the object still reports `usage_complete=True`. Direct reuse permits another prediction. The existing interruption fixture raises `RuntimeError`, which exercises a different path.

**Important boundary:** the current CLI propagates the interruption and unloads the owned model; it did not reuse this object or continue the batch. Direct reuse is a counterexample to the state invariant, not an independently admitted retry route or evidence of a historical extra call. The defect matters particularly when implementing graceful deadline/cancellation handling.

`execute_comparison` writes assignment/checkpoint results only after normal trial return. `run_scripted_trial` likewise reaches its termination publication only after its `try/except Exception`. Consequently the actual interruption has no final assignment/termination record; a separate operator disposition reconstructs it. Original requests/prefix/receipt survive, so this is incomplete terminal accounting rather than missing evidence being turned into success.

**Disposition:** ensure interrupted state is conservatively finalized before re-raising, with a distinct interruption outcome and truthful terminal/cleanup status. Preserve the original receipt; do not rewrite it into a normal failed or completed prediction. The per-call receipt is persisted only in `finally`, despite the class docstring's broader pre-dispatch wording. Requests are already persisted before dispatch, and the existing cost collector discovers missing receipts from request files; do not invent a silent-underreporting incident. Prove abrupt-exit/orphan reconciliation if that capability is selected, without expanding into power-loss recovery.

**Evidence:** `investigator_model_interface.py:590–683`; `investigator_workspace_trial.py:365–486`; `execute_comparison`; `test_interrupted_stream_keeps_visible_prefix_and_unknown_usage_without_salvage`; fresh counterexample.

### AUDIT-011-F4 — P1: the real tool contract omits guidance supplied by qualification

**Observed:** real tool entries are argument JSON schemas without descriptions, path-address examples, default-page semantics or recovery guidance. `read_source` requires separate `source_id` and `path`, but the real task does not explain that a path is relative to that source. The canary explicitly says “path without the source prefix” and gives exact valid arguments.

Gemma Raw requested `source_id=target-proposed`, `path=target-proposed/requirements.txt` repeatedly. The source exists as `requirements.txt`. Its problem observation says only that the path is unavailable in this capture. This is correctly cautious about source absence, but does not explain the addressing convention or distinguish a likely address mistake. These are data-bearing `problem` outcomes, so they do not consume the adapter's malformed/refused correction allowance. Seven such reads were dispatched before the next request was refused by operation admission.

**Disposition:** provide concise tool descriptions, source-relative path semantics, defaults and a generic example outside these cases. Return structured error categories plus valid recovery information where it is known. Repeated identical failed requests should produce an observable stagnation signal or bounded recovery/stop opportunity; do not prohibit all repeated reads, which may be justified after omission or for distinct pages. A common interface improvement must apply to both treatments and be frozen before comparison.

**Evidence:** adapter `TOOL_ARGUMENTS`; `canary_protocol:295–308`; actual Gemma Raw requests and `RetainedSourceCatalog._read`. No model-internal explanation for the repetition is established.

### AUDIT-011-F5 — P1: native pagination and report costs are poorly matched

**Observed:** the semantic freeze selects `max_native_bytes=4096`; native whole-record selection leaves 2048 bytes for payload items. In glyphsLib the native payloads are 8,389 bytes (`ci_inputs`), 11,331 (`ci_coverage`) and 5,350 (`runtime_dependency_state`). Full text delivery requires **3+3+2 pages**. The actual Structured trace follows exactly that path after its initial inventory/native request.

Its observed sequence costs `list_sources 4 + read_native 4 + eight pages 32 + finish 3 = 43`, again leaving 5 for report plus termination. It has **ten eligible typed references**. Even one cited reference would require 6 units at report time; an eight-page citation set would require more. This is a structural completion constraint on that path, independent of whether the interrupted report would have been semantically good.

This is not proof that all native investigation is impossible within 48 units. A model could select fewer pages, omit initial source listing, or stop with a narrower specific uncertainty. It does prove that the natural full-record route actually taken is not compatible with an evidenced report under these charges.

**Disposition:** test a better matched offering: a fit-qualified larger native view, compact typed projections with preserved premises/unknowns, or semantic pages that align with meaningful evidence units. Simply increasing a byte limit trades page calls for larger inputs and still needs measurement. Do not compress away unresolved/counterevidence fields or present a partial page as a complete record. Determine the smallest adequate change before adding another native family or retrieval framework.

**Evidence:** frozen `max_native_bytes`; `consumer_access.py:native_view/native_page`; retained native payloads; Structured calls 2–11. Synthetic long Structured qualification reads a small native record; it never exercises `read_native_page`.

### AUDIT-011-F6 — P2: full stateless history is expensive and can displace the evidence needed to finish

**Observed:** complete stateless requests retransmit selected history. `pack_input` favors recent whole events; token repacking removes whole events rather than retaining source text silently. This is honest and preserves authority boundaries, but makes repeated inventories/searches/read failures costly.

Qwen Raw's input grows from 2,232 to **24,306 rendered tokens**. Its `list_paths` step precedes a jump from 3,973 to 14,305 tokens; the code repeats scope/capture metadata in file descriptors. Two later requests omit the oldest event. Gemma Raw grows from 2,387 to 16,779 tokens while repeatedly failing the same address. These are observed amplification and omission facts, not evidence that a particular model cache behaved badly.

Known final-report native telemetry is also slow: Gemma's report has 714 generated tokens at **3.66 tokens/sec**, and Qwen Raw's 1,274 at **1.57 tokens/sec**. Qwen's reported time to first token is **188.02 seconds** for its report. Native timings and client durations differ; their clock relationship is not established.

**Disposition:** first reduce unnecessary descriptor repetition, duplicate identical observations and arbitrary paging while preserving exact originals and visible omission/provenance. Consider a compact trusted evidence index alongside selected payloads, with explicit retrieval for omitted material. Do not substitute model notes for evidence or silently restore source authority through `trial_event` readback. Measure prompt bytes/tokens, time to first token, generation time and omission of decision-critical material. A transport/cache change is a separate choice, not an assumed fix.

**Evidence:** `pack_input`, `StatelessInvestigatorModel.pack`, `RetainedSourceCatalog.descriptor`, actual requests/metadata and offline rows.

### AUDIT-011-F7 — P1 evaluation gap: interface qualification is substantially easier than real investigation

**Observed:** canaries prescribe exact ordered actions, exact paths, explicit continuation after failure, a known positive marker, and a report of at most 350 words. The near-envelope task is made long using repeated calibration text. `assess_canary` checks sequence/outcomes and the presence of eligible citations, not discovery quality or entailment. The successful native canary does not require paginated native reconstruction.

These are legitimate interface tests. Their limitations are mostly stated accurately in current records. The problem is relying on them as the practical readiness boundary for a much harder workload without a capability-localizing intermediate diagnostic.

**Disposition:** retain a small interface smoke test for wire/runtime validity. Separately exercise generic source discovery, recovery, relevant multi-page material, decision-making under missing evidence, and an affordable report. Use semantic diversity and decoys rather than padding alone. A new diagnostic must not rewrite earlier canary grades or become a backdoor acceptance test trained on these two cases.

**Evidence:** `canary_protocol`, `representative_inputs`, `assess_canary`; current complete qualification outputs and actual semantic differences.

### AUDIT-011-F8 — P1: the task supplies a report format more clearly than an investigation strategy

**Observed:** the real goal is “Investigate update-relevant evidence, uncertainty and justified next work.” It includes exact target/transition, evidence rules and a report schema, but does not explicitly ask the Investigator to trace a consumer path, distinguish declaration from runtime binding, examine relevant upstream behavior, assess CI relevance, or identify the next decision-critical unknown. Those concepts live in the product purpose and reviewer obligations; case-specific reviewer labels correctly stay hidden.

The first three traces spend their evidence work on inventories and dependency declarations. None reads native material; neither complete report traces a useful consumer/CI chain. Providing a valid schema does not create a method for deciding which evidence to obtain.

**Disposition:** introduce a concise, case-independent investigation brief: what changed, where it is consumed, what upstream behavior could matter, what execution/CI actually establishes, what remains unbound, and what would change the recommendation. A model-visible gap/evidence ledger may help if it demonstrably directs work and stays attributed, but a generic instruction is the simpler baseline. Do not reveal solved paths, expected case answers or reviewer-only obligations, or add a planner/critic before testing the simpler brief.

**Uncertainty:** this audit cannot establish that prompting alone will repair the observed behavior. Compare it under a new declared protocol rather than making the next run an unlabelled prompt-tuning exercise.

### AUDIT-011-F9 — P1 semantic failure: correct declarations are being promoted into risk judgments

**Observed:** Gemma's complete report infers standard/basic HTTPX use and low risk after reading only requirement pages. Qwen correctly identifies a numerical patch update and a satisfied lower bound, then calls it likely low-risk without establishing runtime/CI applicability or upstream behavior. Both include cautions; those cautions do not supply the missing affirmative premise.

Independent retained-source review confirms that HTTPX target tests instantiate FastAPI `TestClient` (`tests/test_routes.py:2–7`); captured old HTTPX accepts `app`, captured new HTTPX removes it, and the two captured Starlette test clients differ in forwarding it. The target's `fastapi[standard]` is unpinned. A useful result should identify the candidate mechanism and the missing actual framework/runtime binding. It cannot assert either safety or actual breakage solely from these reference versions.

In glyphsLib, main CI invokes tox; `tox.ini:8–15` installs `requirements-dev.txt` and runs pytest. A separate regression workflow creates/activates environments. Historical successful job observations are present, but exact installed pytest/process binding is not thereby established. Useful advice should target that discriminator rather than broadly say that no execution results exist.

**Disposition:** evaluate evidence-to-claim reasoning and calibration directly, including plausible but unsupported risk language. Preserve correct observations and specific uncertainty. Keep attribution validation strict, but do not claim a syntactic validator can prove these semantic judgments. A subsequent semantic check must earn its own evidence; adding a second model is not an automatic solution.

### AUDIT-011-F10 — P2 evidence boundary: availability, examination and historical provenance need more usable presentation

**Observed:** Gemma says the changelog was not provided, but `httpx-new/CHANGELOG.md` is present. Qwen says test execution results are unavailable, although the glyphsLib catalog includes a bounded historical CI-results capture. Those are source-universe mistakes. Neither mistake means missing full logs or exact installed-runtime facts have been resolved.

An additional important scope check is HTTPX `ci-observations/E16-actions-run-and-job.json`: its content explicitly labels itself **`manual_simulation` / `illustrative_non_binding`**, reconstructed retrospectively. It may support reasoning about a fixture scenario at that declared strength; it is not a fresh live CI receipt. Native preparation observations are separately acquired and retain their own time/scope. The current audit found no basis to pool these into one production execution claim.

**Disposition:** make source class, capture time, revision and material limitation visible at discovery, and preserve the distinction through reports. Test “available but unexamined”, “retained historical result”, “illustrative/manual reconstruction”, “current capture contains no runs”, and “exact runtime binding missing” as separate states. Do not solve an availability mistake by weakening provenance or manufacturing new evidence.

### AUDIT-011-F11 — P1 experimental-design limitation: the comparison is a weak diagnostic of why the system fails

**Observed:** Raw/Structured changes a representation-and-native-analysis access bundle. Outcomes also depend on discovery, path use, pagination, history packing, citation cost, stopping and inference configuration. The accepted plan already acknowledges the treatment is not serialization alone. The current run cannot distinguish “could not find the evidence” from “could not reason with relevant evidence” with the efficiency needed for the next decision.

**Disposition:** select a separate diagnostic ladder, preserving current results as an incomplete development experiment:

1. **Scripted feasibility:** a trusted script traverses actual interfaces and can publish a properly attributed report within the proposed resource contract. This proves route feasibility only.
2. **Supplied-evidence interpretation:** the same qualified deployment receives a frozen packet of actual relevant source passages, without answers/labels, and must produce scoped conclusions/uncertainty. This removes discovery as a cause and measures interpretation/reporting.
3. **Discovery with the improved generic interface:** restore navigation and compare delivery/use/support, with the same semantic criteria and adequate completion allowance.
4. **Paired mechanism comparison:** only then invest in the broader model/treatment matrix when it can discriminate the selected hypothesis.

Each step needs a named question and stop/reject condition. Do not add all of them as arms to the existing freeze: interpretation-only packets are explicitly excluded there. A future diagnostic requires a new bounded design decision. Reuse existing source-interpretation/report-review machinery where appropriate, but not old outcomes as new controls.

If supplied evidence still produces unsupported conclusions, target semantic method/model adequacy. If supplied evidence works but discovery fails, target navigation/evidence selection. If neither can finish, fix the controller before judging either capability.

### AUDIT-011-F12 — P1 proof limitation: available results cannot support a winner or independent acceptance

**Observed:** two exposed cases, one sample per condition, one published report, partial assignment coverage and source-aware AI review. Frozen global/per-case treatment-first balance is validated, but interruption leaves a biased completed subset. Masking cannot hide native tools or erase prior exposure. E4B has no semantic observations. Exact active/human review effort is not measured.

The audit independently agrees with the main negative findings after reading originals/source. It does not convert the review into blind/human acceptance. Agreement between AI passes is supporting examination, not a new independent sample of user benefit.

**Disposition:** report the complete denominator and execution causes; review complete attempted content even when publication fails; keep no-report states ungraded semantically. For future acceptance, freeze an unseen sample with varied evidence states and an independent source review/adjudication procedure. One successful repeat on these repaired development cases is diagnostic regression evidence, not generalization. Maintainer usefulness remains separately owned and need not wait for an autonomous agent to succeed.

### AUDIT-011-F13 — P2 process/efficiency judgment: versioning is disciplined, but the feedback loop is too expensive

**Observed:** repeated contract/runtime/presentation changes require preparation, freezing, canaries, evidence publication and retention. The current plan's large amendment history records these changes honestly, but also makes the current operative contract harder to locate. The qualification-heavy cost distribution is measurable.

**Disposition:** after the next design decision, use one compact current experiment-contract view plus immutable revision references, rather than expanding several competing instructions. Tie requalification scope to what changed and the claim at risk. A controller-only deterministic change does not automatically require re-running every model's long canary; a prompt/tool/schema/configuration change may require representative real-model requalification. That distinction must be explicitly designed prospectively, not used to bypass the currently frozen full-matrix gate.

Keep deterministic proof, model-wire smoke, behavioral diagnostic, semantic comparison and usefulness acceptance as separate evidence layers. Prefer one coherent repair with a useful discriminating result over many tiny canary-only revisions. The design target is less work per resolved product question, not fewer integrity controls.

## 5. Independent recheck of complete report content

The table covers the substantive surfaces of both complete outputs, including the unpublished Qwen attempt. “Correct” describes what the retained material supports; it is not report acceptance.

| Report surface | Independent result and source basis |
| --- | --- |
| Gemma claims 1–2 and transition summary | Correct declaration values in base/proposed `requirements.txt`. Declaration does not establish installed versions. |
| Gemma claim 3 and basic-use premise | Manifest inclusion does not establish actual HTTPX request use or ordinary/basic usage. Target tests show a framework TestClient route worth investigating. |
| Gemma missing-observation fields | Fair only as statements about what this investigation did not identify; they do not prove source-universe absence or low risk. |
| Gemma source-only condition | Correct; no dynamic compatibility execution occurred. |
| Gemma recommendation | Checking relevant changes before merging is reasonable proposed work. Numerical minor-component change and assumed basic use do not support low breaking-change risk. |
| Gemma stopping/summary risk language | Transition established; material usage/upstream/CI discriminators remain unexamined. Their absence from the report does not justify the reassuring conclusion. |
| Gemma unexamined changelog | Not examined is true; not provided is false. The retained HTTPX changelog exists. |
| Qwen claim 1 and transition summary | Correct: only requirements-dev.txt line 65 changes, from pytest 9.0.2 to 9.0.3. Exact identities match the target. |
| Qwen claim 2 and lower-bound summary | Correct for proposed `requirements-dev.in`: `pytest>=2.8`; both named versions satisfy it. This does not prove resolution/execution. Base input was not read. |
| Qwen claim 3 / visible-file comparison | Actual retained base/head declarations differ only at line 65. Unchanged named dependencies are correct. Per-claim citation/page coverage is narrower than the full set of inspected ranges; separate truth from attribution strength. |
| Qwen conditions | Source scope, no execution by this investigation, and unverified compatibility are accurately limited. |
| Qwen recommendation and missing execution evidence | Targeted test verification is reasonable proposed work. “Likely low-risk” lacks evidence; broad no-results availability language is false. Historical results still do not prove exact installed pytest. |
| Qwen stopping reason | “Budget exhausted or sufficient evidence” conflates two different causes. Completion capacity was already inadequate; sufficiency was not established. |
| Qwen unexamined list | The trace confirms unread source ranges/base input/CI/test/changelog material. Relevant available workflow and CI evidence should have influenced investigation or a specific limitation. |

Neither “inferred” status nor a caution elsewhere licenses an unsupported factual premise. Conversely, a correct declaration or well-scoped unperformed-check statement should not be marked false merely because the overall report fails.

## 6. Which fixtures are worth adding

The goal is independent proof responsibilities, not a test-count target. Reuse/extend current fixtures where they already protect the same seam. The following are recommended **future** additions or stronger assertions; none was added to the implementation suite by this audit.

| Priority / fixture | Distinct proof obligation | Cheapest useful layer |
| --- | --- | --- |
| P1 continuous stream past monotonic deadline, plus silence | Deadline enforced while messages continue and while no message arrives; bounded cancellation/cleanup | Fake clock/channel controller test, then one charged transport qualification if selected |
| P1 late success/cancellation race | Distinguish complete trustworthy usage, unknown usage, cancellation request and confirmed termination; no false timeout attribution | Deterministic transport seam |
| P1 actual `KeyboardInterrupt`, selected signal/exit handling | Conservative usage state and terminal accounting on real exception classes; no implicit continuation | Model wrapper/orchestrator integration; process probe only for the admitted signal contract |
| P1 report with 0/1/several distinct references near budget limit | Discovery preserves an affordable completion allowance; already generated report is not predictably rejected for unavoidable cost | Trial/controller fixture, including reference growth/omission |
| P1 actual large native shape with 3+3+2 pages | Material native uncertainty and final supported citations survive traversal within declared resources | Real product/native adapter composition fixture; scripted consumer proves feasibility |
| P1 source-relative path error and recovery | Generic tool help/error semantics allow recovery; source problem is not confused with global absence | Adapter/source fixture plus separate behavioral canary if contract changes |
| P1 plausible semver reassurance contradicted or unsupported by sources | Model preserves declaration/runtime/applicability separation and does not manufacture low-risk advice | Frozen supplied-evidence semantic diagnostic; unit tests cannot prove model judgment |
| P1 available but unread CI/changelog versus genuinely absent material | Specific uncertainty, accurate availability and useful next work | Catalog/delivery fixture plus semantic diagnostic |
| P2 relevant evidence among decoys and varied file ordering | Search strategy reaches material evidence rather than merely a dependency string or first inventory page | Small development discovery cases with frozen source obligations |
| P2 long relevant history plus omitted earlier source | Honest omission, affordable re-read and correct citation authority; no promotion of notes/readback into original evidence | Existing packing/reference tests extended at composition seam |
| P2 historical/manual/current evidence with different scopes | Capture class and time remain visible; simulation does not become observed execution | Source/projection/report provenance fixtures |
| P2 orphan request without final receipt | Attempt remains visible and usage unknown; existing request-based cost collection retains the attempt | Offline accounting fixture; no power-loss promise |
| P2 reviewer disagreement on a material proposition | Source-reasoned adjudication and preserved initial labels; independent reviewer claim is truthful | Review procedure/example, not a runtime unit test |

For semantic cases, vary outcomes deliberately: a supported issue, evidence of non-applicability, a specific unresolved binding, conflicting observations, and adequate scoped stopping. Include a novel dependency/repository relationship before generalization claims. More cases that all reward “unknown” or the same HTTPX answer would conceal failure rather than improve the evaluation.

## 7. Recommended decisions, alternatives and trade-offs

These are proposed responsibilities, not an activated plan.

| Choice | What it buys | What it leaves unresolved | Assessment |
| --- | --- | --- | --- |
| Resume/repeat the existing broad matrix immediately | More outcomes under a familiar setup | Control/affordability defects, poor localization, high cost; old batch cannot be silently resumed | Not recommended |
| Add more models or a critic/multi-agent system | More candidate outputs | Existing failures remain confounded; more resource/coordination cost | No present evidence justifies it |
| Only increase call/token/operation ceilings | May permit longer traces and reports | Repetition, irrelevant evidence and unsupported advice can consume the extra budget | Useful only after feasibility measurements, not as the main repair |
| Improve generic tools and completion/control, then run a narrow diagnostic | Makes a bounded useful output possible and identifies discovery versus interpretation limits | Still needs future semantic evidence and unseen validation | Recommended next direction |
| Replace the entire Workspace/hybrid architecture | Could remove some current machinery | Discards integrity/retention gains without evidence they cause semantic failure | Not justified |
| Prefer deterministic preparation plus bounded interpretation if discovery adds no value | Simpler candidate architecture and clearer capability boundary | Full adaptive discovery remains deferred; a method comparison must earn adoption | Credible alternative to keep open |

### First decision: controllable and affordable completion

The relevant full responsibility is evidence-backed investigation leading to useful, calibrated advice. The proposed first repair includes monotonic control/cancellation, conservative interrupted usage/terminal accounting, and a report allowance that survives meaningful discovery. It should be proven against a real multi-page evidence shape and generic malformed-path recovery.

It temporarily excludes new semantic methods, model selection, new native families and user-benefit claims because those cannot be discriminated while the controller can prevent completion. This narrowing is technically justified by observed failures, not by an easier acceptance target. Re-enter semantics as soon as the existing evidence route can finish under a coherent contract; do not make controller work an open-ended infrastructure program.

### Second decision: locate the capability bottleneck

Freeze the smallest diagnostic that can answer whether these deployments can interpret a supplied relevant packet correctly. The packet must preserve actual source/capture/runtime uncertainty and contain no desired answer. Judge materially supported conclusions, false confidence and specific useful next work, not JSON or keyword presence. Then test generic discovery separately if interpretation is adequate.

This adds a diagnostic responsibility excluded by the current comparison plan; it therefore requires explicit design selection and protocol reconciliation. It is not an extra untracked arm. If supplied-evidence performance is inadequate, compare a simpler interpretation method or deployment before expanding autonomous discovery. If adequate, improve and compare navigation without calling that an interpretation failure.

### Later decision: useful generality and maintainer value

After the development bottleneck is understood, use a separately frozen unseen case set with independent source review. Compare with a transparent simpler ordinary-review/report baseline. Keep machine results and independent maintainer usefulness separate. Existing report evaluation obligations can be reused; no reviewer contact or external action is authorized here.

## 8. What should be retained, simplified or deferred

**Retain:** product-owned evidence/material authority; frozen common inputs; strict request-local typed references; requested/applied runtime checks; exact original and rejected outputs; whole-event omission honesty; separate semantic review; immutable negative/incomplete results and actual cost accounting. These directly serve provenance, measurement and review.

**Improve or simplify:** generic tool guidance and recovery, completion allowance, native delivery shape, repeated descriptor/history cost, monotonic run control, exception-safe terminal accounting, and a compact current experiment contract. Each needs the smallest focused proof that protects its actual responsibility.

**Defer pending a discriminating result:** additional candidate sweeps, more agents/frameworks, stateful transport replacement, broad runtime optimization, new native families, automatic semantic judges, productization and whole-experiment harness migration. Prior code and spent effort are not retention authority; equally, unfamiliar complexity is not evidence it should be deleted.

The independent audit supports retaining the hybrid direction as a candidate while changing the development route. It does not establish that the final product must depend on an autonomous Investigator: if a simpler evidence-preparation plus interpretation method performs better, the Charter's usefulness responsibility should decide.

## 9. Evidence references and limits

- Latest originals and public navigation: [reference-v2 README](../working-memory/evidence/2026-10-18-investigator-reference-interface-v2/README.md), [analysis](../working-memory/evidence/2026-10-18-investigator-reference-interface-v2/ANALYSIS.md), [assignment disposition](../working-memory/evidence/2026-10-18-investigator-reference-interface-v2/final-results.json), [freeze](../working-memory/evidence/2026-10-18-investigator-reference-interface-v2/semantic-freeze.json).
- Complete output reviews, independently rechecked above: [Gemma Structured](../working-memory/evidence/2026-10-18-investigator-reference-interface-v2/gemma12-httpx-structured-review.json), [Qwen Raw](../working-memory/evidence/2026-10-18-investigator-reference-interface-v2/qwen27-glyphslib-raw-review.json); [Gemma Raw](../working-memory/evidence/2026-10-18-investigator-reference-interface-v2/first-semantic-review.json) and [interrupted Structured trace](../working-memory/evidence/2026-10-18-investigator-reference-interface-v2/qwen27-glyphslib-structured-interrupted-review.json).
- [Interruption correction](../working-memory/evidence/2026-10-18-investigator-reference-interface-v2/interruption-checkpoint.json), [costs](../working-memory/evidence/2026-10-18-investigator-reference-interface-v2/cost-accounting.json), [retention](../working-memory/evidence/2026-10-18-investigator-reference-interface-v2/completed-retention.json).
- Original private root, inspected read only: `/home/motafeq/.local/share/upgradepilot/investigator-runs/semantic-comparison-2026-10-18-reference-v2`. The freeze binds the common input root, checkpoints, source catalogs and installed SDK path. Raw bodies remain outside Git; this audit preserves locators rather than copying them into public artifacts.
- Fresh audit [program](../working-memory/evidence/2026-10-18-investigator-independent-audit/offline_audit.py), [results](../working-memory/evidence/2026-10-18-investigator-independent-audit/offline-results.json), and [cycle progression](../working-memory/2026-10-18_investigator-experiments-independent-audit_lbd-cycle.md).
- External primary corroboration: [LM Studio SDK timeouts](https://lmstudio.ai/docs/python), [cancellation](https://lmstudio.ai/docs/python/llm-prediction/cancelling-predictions), and [SWE-agent's interface study](https://arxiv.org/abs/2405.15793). The latter supports treating the tool/observation interface as a serious engineering variable; its different models/tasks do not prove any proposed UpgradePilot change will work. Recommendations here are inferences from local failures, not imported benchmark guarantees.

Unresolved: counterfactual quality of the interrupted report; intrinsic model competence or comparative ranking; exact unknown token usage; cause of the file-age/monotonic discrepancy; performance of proposed repairs; unseen reliability; independent user benefit. None is filled in by test success, a valid citation, an AI review, or a larger fixture count.

**Handoff:** the audit deliverable is complete; recommendations remain unselected. Decide the bounded controller/interface and diagnostic responsibilities before further inference or implementation. The existing semantic cycle is not closed or advanced through D/E by this audit.

Procedural provenance: `UP-SKILL:upgradepilot-repository-audit`; `UP-SKILL:upgradepilot-learning-by-doing`; `UP-SKILL:upgradepilot-working-memory`.
