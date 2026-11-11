# AV-Tracer maintainer-task review and evidence checkpoint plan

**Responsibility:** Coordinate one bounded, read-only maintainer-task review of the qualified AV-Tracer caller/signature result, then make the existing combined-evidence/runtime-applicability and evidence-grounded AI design decisions in their correct order.

**Artifact status:** Planning contract; execution and any later Build/inference/target execution require their own selection and proof. `MEMORY.md` alone owns the current live handoff. This plan does not replace the controlling plans or grant action permissions.

**Primary outcome:** A source-backed answer to the maintainer's question, a truthful assessment of report/navigation value against the available deterministic source baseline, a proposition-level CI/runtime applicability disposition, and a recorded **select / narrow / reject / defer** decision at the AI explanation checkpoint. Do not require a model run to finish the checkpoint.

## Owners and boundaries

- [Project Charter](../PROJECT_CHARTER.md) and [Product Decision Model](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md): evidence truth, candidate-specific applicability, stopping and claim limits.
- [Caller/signature native adoption and qualification §§14–16](CALLER_SIGNATURE_NATIVE_ADOPTION_AND_QUALIFICATION_PLAN.md#14-maintainer-task-baseline-and-acceptance): exact task/source-only admission and combined-evidence/runtime-applicability checkpoint.
- [Maintainer report usefulness plan §5](MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md#5-independent-usefulness-evaluation): report access, equal-information comparison, independently measured usefulness and its prerequisites.
- [Evidence-grounded AI explanation comparison plan](EVIDENCE_GROUNDED_MAINTAINER_EXPLANATION_COMPARISON_PLAN.md) and [project route's AI design checkpoint](UPGRADEPILOT_90_DAY_PLAN.md#evidence-grounded-ai-design-checkpoint): conditional model-comparison eligibility, frozen baseline and evaluation, and required disposition.
- [Maintainer action synthesis specification](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md): non-abstention requires positive action-specific permission. Existing product synthesis remains explained abstention.
- [Security](../SECURITY.md): read-only external-evidence, privacy, credential and target-code safeguards. The case report and owner-only Workspace may contain source bodies kept outside Git.

**In scope:** inspection of the already retained exact saved report/Workspace/source citations, cross-checks against already retained public-safe case evidence and historical CI records, a bounded deterministic baseline/maintainer-task review, and planning dispositions. Small **proposed** presentation corrections may be described, not implemented.

**Out of scope:** new live GitHub/PyPI collection, fresh source acquisition, target-code execution or CI reruns, new runtime instrumentation, an automatically combined evidence profile, repository/PR mutation, new action authorization, default inference, product/experiment code edits, broad source-syntax expansion, new architecture, and independent human-usefulness claims without a qualified study.

## Frozen development case and entry evidence

Case: [ivaronkun-Ahey/AV-Tracer PR #11](https://github.com/ivaronkun-Ahey/AV-Tracer/pull/11), exact base `527a004918c0f825e97c3583404242605fd58ec2`, head `25e7205f39103456e7efbc4e9f503f3debc7b5d8`, HTTPX **0.25.2 → 0.28.1**. This is already exposed development evidence, **not** a protected transfer or independent validation case.

The [qualified source receipt](../working-memory/evidence/2026-11-11-av-tracer-exact-version-allocation/qualification.json) records Workspace report revision `80a58d494a8c46009aab8dc72b94b447`, the retained source IDs/digests, the old `httpx.Client.__init__` named `app` parameter, the proposed `unexpected_keyword(app)` result, partial acquisition and offline reopening. The [engineering cycle](../working-memory/2026-11-11_caller-signature-exact-version-allocation_build-cycle.md) records the normal CLI proof and budgets. The [earlier case screening](../working-memory/2026-11-09_targeted-check_cross-case-qualification_cycle.md) has separately scoped historical CI observations. Neither its public failed-job conclusion nor the source-only report proves the CI failure cause.

**Private artifact admission:** Before reviewing *report presentation*, actually open the exact saved report and/or acknowledged Workspace revision in the authorized private location using the product's existing offline reader. Verify the selected target, revision, cited material and delivery route against the public-safe receipt. Do not infer the report text, original-source access cost or navigation quality from `qualification.json`. If the private report is inaccessible, record the precise access blocker and stop report-utility acceptance; a receipt-only source reasoning review may proceed under a clearly different label. No refresh or synthetic report replacement.

## Ordered checkpoint work

### 1. Recover the exact source-only maintainer view

Task: **“Could the proposed HTTPX upgrade break `TestClient(app)` in this PR, when would that mismatch apply, and what specific observation would confirm or refute it in the relevant execution?”**

Record the actual default report opening, exact old/proposed assessments, relevant source IDs and original-source reads. Trace the target call through FastAPI's re-export, Starlette's forwarding call, and both exact HTTPX constructors. Explicitly identify the rejected `app` keyword and the remaining accepted forwarded arguments. Preserve the sampled FastAPI/Starlette release assumption and source-coverage omissions.

Capture: evidence identity → what it directly establishes → its conditional premise → what it does **not** establish. Distinguish source-level argument rejection from actual installed dependency, invoked callable, test dispatch, observed error and CI failure attribution. The source-only profile has **not evaluated** CI/runtime evidence.

### 2. Compare the maintainer experience with the strongest transparent baseline

Use the same **eligible saved material** for the inspected product view and the simple source-backed explanation; do not give either arm private additional observations or mix separately acquired CI into the source-only product output. Count exact report sections/source opens and necessary navigation operations; identify required facts hidden, omitted or misleading in the real view. Record any deterministic summary rearrangement that would answer the task without additional acquisition or inference.

Assess **separately**: (a) factual/citation fidelity, (b) clarity and navigation burden, (c) a concrete decision-relevant next check or benefit. Report count/reading-operation proxies without claiming human time savings or independent usefulness. If the transparent baseline already answers the task with acceptable effort, record that as a strong reason to defer a model comparison on this task.

**Gate:** Record a source-only adoption/pilot/defer/reject disposition under the caller/signature plan, the observable maintainer-task answer, and any exact report/presentation gap. Report inaccessibility blocks presentation acceptance, not the pre-established static signature witness.

### 3. Complete the existing combined-evidence and runtime-applicability design checkpoint

Only after Step 2's task/adoption disposition, compare **separately identified** retained CI/runtime sources with the caller/signature proposition. Record their repository/base/head, run/attempt/job/step, command, observation time/environment and source identities wherever available; never silently join captures with different scopes or claim source-only CI results.

Use the [existing §16 proposition/owner table](CALLER_SIGNATURE_NATIVE_ADOPTION_AND_QUALIFICATION_PLAN.md#reconstruct-the-exact-missing-proposition-and-reuse-its-owner) to distinguish: relevant command execution; version/requirement state at the relevant boundary; actual imported callable/loaded file correspondence; affected-path execution; observed behavior or cause. Use only the strongest existing evidence for each, classify missing and unavailable states, and identify the **earliest decision-changing unknown** rather than demanding universal runtime proof.

For the historical failed backend pytest job, an existing exact-job traceback **if retained and attributable** may clarify cause; missing or inaccessible logs remain unknown. A traceback mentioning `app` still needs the appropriate version/source correspondence before stronger installed-runtime attribution. A different traceback must not erase the separately established conditional source mismatch.

Compare existing-evidence composition, static reasoning, retained target-owned observations, a narrowly proposed additional observation and explicit unresolved/defer. New acquisition/execution is **not** selected by this checkpoint.

**Gate:** Produce the owner-based §16 disposition: answered with existing evidence; design a combined-profile composition; design one specifically justified observation; remain unresolved with re-entry condition; or reject/defer added capability. If a design is selected, identify its concrete owner, join/proof rules, budget, alternatives and separate Build authorization requirement.

### 4. Reach the scheduled AI explanation checkpoint

Use the exact task and Step 3 disposition to classify any residual limitation as **evidence unavailable**, **retrieval/selection**, **semantic interpretation**, or **presentation/navigation**. Missing primary evidence is not repaired by a model. Prefer the strongest transparent deterministic explanation as comparator.

Record **select / narrow / reject / defer** with a task-specific rationale. If an AI comparison is justified, hand off to its existing plan to freeze source excerpts, equal-information inputs, deterministic baseline, answer/rubric, citation entailment and forbidden claims, exposed-case status, one local-model configuration and cost/stop/cleanup limits **before** inference. AV-Tracer is development-exposed; an independent/protected contrast is required for any later transfer claim. This plan authorizes no inference or agent orchestration.

**Gate:** A reasoned checkpoint disposition is sufficient; an executed model experiment is neither automatic nor required.

### 5. Prioritize one follow-up responsibility

Based on the recorded gaps and value evidence, select only one warranted next owner: targeted report/presentation repair, CI/runtime evidence design, action-synthesis eligibility proof, a bounded AI comparison design/execution under separate approval, independent maintainer usefulness preparation, or reasoned deferral. Specify the precise decision impact, simpler baseline, expected proof, present limits and re-entry condition. Reconcile `MEMORY.md` **only when** the live selected responsibility changes.

## Record and acceptance

Keep the detailed progression, source and learner reasoning in one dated `working-memory/` cycle record for the activated review; place a public-safe **case review** (question; exact input/report identity; observed product output and citations; source-backed answer; navigation/baseline observations; CI/runtime proposition matrix; dispositions and proof limits) in that cycle or its directly linked `working-memory/evidence/` record. Link existing receipts instead of copying private source bodies, credentials or lengthy reports.

The review and checkpoints pass only when:

1. All facts and comparisons are tied to the exact admitted identities and observed artifacts; inaccessible material is reported as inaccessible, not imagined.
2. The source-only pilot/task disposition is explicit; unsupported runtime/CI/action conclusions are not promoted.
3. The §16 checkpoint names the selected proposition, existing owner/baseline, available evidence, missing proof, proportional alternative and disposition.
4. The AI checkpoint records its select/narrow/reject/defer decision **before** optional AI expansion.
5. The next responsibility has a justified owner, stop/proof boundary and separate authorization status; the plan does not produce a merge/safety conclusion.
6. One meaningful Learning-by-Doing ownership check tests the ability to trace a cited claim or distinguish a conditional source mismatch from execution evidence. Independent mastery is reported only when actually demonstrated.

**Stop:** If the saved report cannot be accessed, do not score its presentation. If the case/task is already adequately served by a transparent baseline, do not manufacture an LLM need. If evidence is insufficient to identify a justified new observer or action, preserve unresolved/defer instead of adding general infrastructure. Keep all earlier frozen captures unchanged.
