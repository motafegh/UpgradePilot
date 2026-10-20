# Current CI retained-input admission and existing-owner diagnostic plan

**Artifact:** Bounded retained/fresh diagnostic execution contract. Acceptance, activation, results and live continuation belong in [MEMORY.md](../MEMORY.md).
**Responsibility:** determine what the retained current-CI cohort can honestly supply to existing owners, exercise their admitted correlation/step-execution boundaries, and locate any demonstrated discrepancy at its earliest responsible owner.
**Entry evidence:** [main re-entry review](../working-memory/2026-10-20_2156_fresh-current-ci-reentry-and-owner-admission-review.md), [corrected cohort](../product-simulation/fresh-current-ci-diagnostic-2026-10-20/README.md), [readiness qualifications](../product-simulation/fresh-current-ci-diagnostic-2026-10-20/READINESS_MATRIX.md) and [cohort report](../product-simulation/fresh-current-ci-diagnostic-2026-10-20/FINAL_REPORT.md). These are exposed development cases, not protected evaluation or product acceptance.

## Purpose and bounded product contribution

The full product responsibility remains the [Charter's](../PROJECT_CHARTER.md) public-PR-to-evidence-backed-report flow. This diagnostic asks whether current real workflow/step evidence can be represented without inventing observations, whether supported identity shapes work, and whether unsupported/skipped evidence stays appropriately limited. Its observable deliverable is a three-case input-admission ledger, separately labelled retained and fresh owner results, source-backed paired review and one next-investment disposition.

The increment excludes complete public-PR investigation/replay, dependency-change re-derivation, exact-command/package-state proof, API compatibility, new interpretation/model methods, independent usefulness and maintainer action permission. Those require inputs/proof absent from these bundles. Testing existing correlation/step owners first is justified by the new real step evidence and the missing-field discrepancy; it does not make a component pass sufficient for the larger product thesis. Re-enter the excluded responsibilities only with an actual evidence need and their own accepted scope.

Stable trust and evidence-state semantics remain with the [Core specification](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md) and [Product Decision Model](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md). The plan coordinates their application; it changes no accepted semantics or architecture.

## Existing owners and modification boundary

| Responsibility | Existing owner / consequence |
| --- | --- |
| Raw/source fidelity and declared capture identity | Cohort manifests, authoritative artifact selectors and [verifier](../product-simulation/fresh-current-ci-diagnostic-2026-10-20/verify_bundle.py); preserve raw bytes and earlier flawed artifacts |
| Run/job/step field admission, exact heads and attempts | [GitHub Actions provider](../src/upgradepilot/github/actions.py); missing required data is an input refusal, not a reason to weaken the owner |
| Static source parsing and identity correlation | [Workflow definition](../src/upgradepilot/github/workflow_definition.py) and [runtime correlation](../src/upgradepilot/ci/workflow_runtime_correlation.py); supported names/order versus intentional missing-name/matrix limits |
| Correlated user-step success versus non-success | [Step execution assessment](../src/upgradepilot/ci/runtime_execution.py); skipped steps must not become successful execution |
| Stronger package-state and decision authority | [ADR-0010](../docs/architecture/ADR-0010-package-manager-semantic-facts-and-runtime-dependency-state-composition.md), [runtime-state plan](RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md) and [synthesis specification](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md); no stronger witness or permission is earned here |

Default executable home: one disposable `experiments/current_ci_owner_diagnostic.py` with meaningful proof under `experiments/tests/`. Reuse existing product parsers/types/functions; add no dependency, product enum, service, package layer, generic provenance/validator framework or product import from experiments. Dated results belong under `working-memory/evidence/`; original cohort raw/manifests remain unchanged. Recovered original-capture metadata, if any, is a separate evidence overlay with source identities, not an in-place raw repair.

A demonstrated defect in an already admitted contract may receive one bounded source/test repair under the separately accepted Build execution of this plan. Expected touched product owners are the Actions provider, correlation or step-execution owner, plus their responsibility-owned tests. Rule out missing inputs, experimental mapping mistakes and unsupported shapes first. New supported semantics, named/matrix expansion, package-state capability or consequential architecture require a separate owner/design decision; they are not routine defect repair.

## Two proof tracks and the input decision

**Strict retained-record admission.** Inventory every required field and its exact source path/hash/JSON pointer. A selected run's `workflow_id` may be joined only from its unique retained run-list entry with the same run ID; preserve both sources and refuse conflicts. Do not fill missing job `head_sha`, response totals, page envelopes or attempt-request details from expected values. Existing representation-parser methods may be used as narrow diagnostic probes with the saved context they require; direct internal callability does not create a supported public replay contract or justify a fabricated full PR.

Search only original-capture locations explicitly identified by cohort manifests/construction records, including their precise retained references or Git history, for at most 20 active minutes. Do not scan unrelated home/session/cache trees. Record a bounded non-recovery if no source is identified. A separately selected live acquisition is governed below; it never supplies missing observations to this frozen record.

**Conditional correlation-only projection.** This is the proposed fallback when original provider job heads cannot be recovered. It deliberately narrows the claim rather than repairing provider data:

- Construct experiment-owned typed inputs from the retained workflow, selected run, job names and step fields. Join retained run fields explicitly. Preserve every available runtime status/conclusion and the difference between null/missing steps and an empty list.
- If a `WorkflowJob` needs `head_sha`, supply the selected run head **only as a declared fixture scope premise**. Record the field, value, source relationship and `derived scope premise, not a provider job-head observation` beside every affected result. Do not inject it into saved provider JSON or pass augmented JSON off as faithful acquisition/parser replay.
- Call the existing correlator on that disclosed projection, followed by `assess_correlated_step_execution` only for returned user-step matches. No exact-command evaluator, dependency runtime-state producer, full investigation, native publication, report synthesis or maintainer-action evaluator is invoked.
- Such a result proves conditional owner behavior on retained names/order/statuses under its declared scope premise. It cannot independently qualify acquisition, job-head validation, exact-attempt transport, runtime dependency state or normal end-to-end integration. A result without that qualification is inadequate even if correlation succeeds.
- If any required premise cannot be stated consistently with the retained records, mark the projection input-unavailable. Do not silently invent another field or relax the owner to obtain an output.

Execution scope must explicitly cover the conditional track. In a strict-only selection, stop affected retained case work at input-unavailable; no fallback is implicit. The current missing-field observations are known entry evidence, not new discoveries or new product defects to claim again.

**Recommended execution choice:** retain strict admission and allow the disclosed conditional track. It tests real name/order/status behavior without new acquisition or a product-contract change. Its strongest limitation is that a successful match cannot independently validate the missing job-head observation or attempt-specific transport; where that independent acquisition claim is the actual decision, strict unavailability remains the correct result. This temporary component narrowing does not replace the eventual normal producer/integration proof.

## Separately fresh normal selected-CI acquisition

After retained admission and conditional results are preserved, acquire new observations through the existing public PR, Actions and repository clients. Use their normal parsing, pagination, exact-head and exact-attempt paths with an anonymous recording session that does not alter provider data or product policy. This is a selected-CI provider diagnostic, not a full public-PR/dependency investigation. Preserve actual request URLs/parameters, UTC/monotonic spans, status, safe response headers, response-body size/hash and body bytes outside Git before semantic parsing. Requests-decoded response entity bytes are not HTTP-wire archives.

Require the current normal PR identity to retain the frozen base/head. Find the exact selected run ID through the normal exact-head run query and require its captured attempt to equal the frozen attempt. Use normal `get_workflow_jobs` and `get_exact_head_workflow_file`, then recheck PR base/head/count. Preserve current run/job head fields, step availability/statuses and exact workflow source identities. If the PR, selected run, attempt or source binding drifts, retain that outcome without selecting another identity. Missing, inaccessible, forbidden/rate-limited, transport-failed and invalid data remain distinct; no retries, authenticated fallback or connector substitution.

Fresh evidence may support ordinary correlation/step assessment on normally acquired typed inputs, separately from conditional retained projections. Compare body-level field availability with product parser/output preservation, and compare the exact static/runtime source identities before interpreting a difference. A new job head observed now does not become a fact retained in the old bundle. If current evidence is unavailable, report the comparison limit rather than a product failure.

Source repair is considered **only after both stages and the paired review**, including any explicit unavailable live rows. A supported-contract defect independently demonstrated by those records may receive a bounded repair; legitimate unsupported shapes and transport/source absence do not justify policy expansion.

## Frozen cases and expected boundaries

Use exactly the authoritative inputs selected by the three [cohort manifests](../product-simulation/fresh-current-ci-diagnostic-2026-10-20/cases/). Freeze manifest/artifact hashes, original source identities, selected repository/base/head/run/attempt, executable/product source identities, field mapping/premises and review rules before producing owner outputs.

| Retained case | Selected run / attempt | Expected correlation and downstream limit |
| --- | --- | --- |
| OpenAI agents / mcp update (`FCI001`) | `39372679381` / `1` | Candidate `correlated` ordinary named-job identity path. Both user steps remain skipped; step execution must be `not_established` with non-success basis. No mcp install/exercise inference |
| mdformat-footnote / tox range update (`FCI002`) | `36798375619` / `1` | First expected `unresolved/static_job_name_missing` for `pre-commit`; later matrix is secondary, not a separately manufactured case. Two skipped publish jobs retain unavailable/null steps. No tox consumption/exercise inference |
| PasarGuard / FastAPI range update (`FCI003`) | `39445488948` / `1` | Expected `unresolved/static_job_name_missing` despite rich steps. Preserve the reported empty PR association. No invented YAML-key/name match or package-state claim from make targets |

These are predictions to test, not fixture answers to force. Do not modify the workflow, add static names, replace skipped statuses, isolate the later matrix as though it were the original workflow result, or choose different runs after seeing a refusal. Input admission and conditional correlation have separate denominators; 19 job records do not become 19 independent case successes.

## Execution and proof sequence

1. **Prepare immutable inputs and declare the seam.** Verify the corrected bundle and source selectors; freeze identities and the selected strict/conditional policy. Preserve field provenance, missing records, recovery limits and historical capture costs separately from new local CPU work.
2. **Implement and verify the disposable composition.** Test exact-ID joins/conflict refusal, no missing-field fabrication, truthful conditional-result labels, null/empty preservation, original immutability, first-refusal order, correlated skipped-step non-success, identity mismatch refusal and bounded failure retention. Use synthetic fixtures for machinery proof; any real-case exploratory output must be declared and counted rather than hidden before the freeze. Reuse the relevant Actions, correlation and step-execution test families; broaden only for a real changed seam or product repair.
3. **Execute one fixed three-case diagnostic.** In the table order, retain admission outcomes and any separately admitted conditional correlation/step assessments. Persist failures/partial outputs as they occur. No automatic row retry, method tuning or source repair during the frozen batch.
4. **Acquire the separately fresh selected-CI observations.** Use the normal providers and identity checks above, preserving every request/failure independently of the frozen batch. Store fresh outputs under a distinct stage and acquisition-time identity.
5. **Compare and review discrepancies at their owner.** Compare actual fields, workflow structure, runtime statuses and current contracts. Distinguish input-unavailable, operational failure, conditional expected refusal, admitted-shape defect and overstrong interpretation. If an existing-contract defect is proven, preserve the original result and minimal reproducer, make the bounded repair, and run appropriate regression proof within the engineering ceiling. Repair verification is separately labelled; it does not overwrite/regrade the frozen cohort or authorize another official cohort execution. If the defect cannot be fixed safely within the admitted scope, record the exact blocking defect and repair responsibility rather than dismissing it as unsupported.
6. **Hand off the investment decision.** Report what each track establishes, material supported positives/unknowns, costs, proof debt and whether a capture repair, specific owner repair, presentation investigation or explicit stop is best supported. Do not automatically begin that follow-on responsibility.

## Budget, retention and outcome contract

After explicit execution activation: at most **three active engineering hours**, including recovery/preparation, code, proof, any bounded repair, review, publication and handoff. Original-capture recovery is capped at 20 minutes within that total. Exactly one retained batch: at most 30 seconds per case, 90 seconds aggregate case work and 180 seconds whole batch including finalization. One separately labelled live batch: at most 90 seconds per case, 270 seconds aggregate and 300 seconds whole batch; at most 12 attempted GET sends per case and 36 total, including redirects/failures. A live body is capped at 2 MiB, total live body retention at 8 MiB, and all newly retained public/private diagnostic evidence at **15 MiB**. Watchdog/partial-output behavior must be proved before execution. Existing original input bytes are referenced rather than republished.

Use monotonic start/receipt/deadline spans. The whole-batch clock starts at process entry before final input revalidation/dispatch and includes startup/finalization. Preserve actual timeout/cancellation evidence; file age is not a deadline measurement. Preparation/proof outside that batch still consumes the three-hour engineering ceiling.

**Zero** project model/provider predictions, model/GPU loading, target commands/reproductions, dependency installation, extra cases or benchmark arms. Anonymous read-only target acquisition is permitted only for the bounded fresh selected-CI stage above. Isolate ambient token/proxy effects per ENVIRONMENT.md for the affected process; do not change global configuration or load credentials. Git metadata synchronization/publication remains separately authorized. Any exceeded ceiling preserves incomplete results and stops; it does not grant new budget, retries or inference. Earlier capture/model/human costs remain historical/unknown where unreconstructed, not zero.

The packet must retain all three requested cases and separate counts for admission availability, conditional/admitted-input attempts, completions, expected unresolved results, input failures, operational failures and source-review inadequacy. Include exact executable/input identities, source-aware implementer/reviewer overlap, field-level observed/joined/missing/premise provenance, output/failure hashes and elapsed spans. Store no credentials, hidden reasoning or unnecessary raw private material in Git.

| Observed outcome | Consequence and limit |
| --- | --- |
| Expected owner results on admitted original fields | Narrow supported owner behavior; transport/full-product/runtime/usefulness claims remain excluded unless independently proved |
| Expected conditional owner results while strict admission is unavailable | Conditional correlation/step behavior is evidenced; acquisition qualification remains unavailable, not three full-system passes |
| A supported-contract defect | Preserve the reproducer; prioritize its bounded owner repair and regression proof; no weakening semantics or rewriting the first result |
| Only missing inputs or legitimate unsupported shapes | Preserve exact gaps/refusals; propose justified capture/design work or stop. Do not modify a lower owner merely to make a case pass |
| Inadequate, timed-out or incomplete diagnostic | Preserve the failed/partial result and cost; narrow/inconclusive disposition, no automatic rerun |

Planning approval alone is not diagnostic activation. Execution selection must cover retained/conditional scope, the separately fresh probe, modification boundaries and budgets; MEMORY.md owns that activation. After sufficient verification, deliver evidence-backed learning, preserve learner ownership gaps honestly and stop at the cycle handoff. A passing fixture or a faithful typed report cannot supply independent semantic/usefulness acceptance or maintainer decision authority.
