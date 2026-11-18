# Literal Matrix CI Evidence Implementation and Qualification Plan

**Artifact status — Prepared for review before Build.**

**Responsibility —** Deliver the complete supported path from literal matrix definitions and exact-attempt runtime records through scoped dependency evidence, native recovery and maintainer reports.

**Architecture —** [ADR-0014](../docs/architecture/ADR-0014-literal-matrix-specialization-and-scoped-ci-evidence.md). The ADR owns expansion, specialization, association and shell-method direction. This plan owns implementation order, proof and completion.

**Other owners —** [Evidence and recovery invariants](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md), [decision propositions](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md), [package-state composition](../docs/architecture/ADR-0010-package-manager-semantic-facts-and-runtime-dependency-state-composition.md), [native reconstruction](../docs/architecture/ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md), [report behavior](MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md). Live selection belongs only in MEMORY.md.

## Acceptance scope

The required real-case input is MapProxy #1559 at head ac01b8901935bfc16a0195277b4aec1c43275897, workflow .github/workflows/test.yml, run 43457921398, attempt 1. Freeze exact payloads and their hashes from [the retained case](../product-simulation/scenarios/S018-mapproxy-soupsieve-matrix-coverage/CASE_EVIDENCE.json). Preserve the original reports and observations.

The final acceptance inventory contains eight job instances.

| Declared instance | Recorded job ID | Required result under the frozen successful input |
| --- | ---: | --- |
| test, Python 3.12, Pillow 13.0.0 | 131996881880 | Separate context, reported correspondence, step 6 install and step 7 test outcomes, and the exact requirements-command assessment. |
| test, Python 3.13, Pillow 13.0.0 | 131996881564 | The same evidence dimensions with its own context and runtime ID. |
| test, Python 3.14, Pillow 13.0.0 | 131996881411 | The same evidence dimensions with its own context and runtime ID. |
| test, Python 3.15, Pillow 13.0.0 | 131996881633 | The same evidence dimensions with its own context and runtime ID. |
| coverage | 131996881258 | Ordinary context, install step 6 and test step 7, with the requirements command assessed under the qualified sequential rule. |
| doc | 131996881440 | Ordinary context and reported outcomes. No Soup Sieve consumption credit from installing documentation tools. |
| lint | 131996881382 | Ordinary context and its sole-command requirements install at step 4. |
| typechecking | 131996881059 | Ordinary context and its sole-command requirements install at step 4. |

Final supported sequential-command qualification must establish the admitted requirements-command execution result in all four successful test variants and coverage. Lint/typechecking use the existing sole-command family. If a real evidence or method defeater prevents a required positive, preserve it and revisit the method or accepted scope before calling this feature complete. An earlier-stage result that merely expands coordinates or lists reported steps does not satisfy this acceptance target.

Installed package-state results may remain unresolved where the existing manager/environment/source premises are incomplete. Each context must show its own result and reason. A successful pytest step does not establish that a Soup Sieve behavior was exercised. These are expected proposition boundaries, not missing rows to remove from the acceptance inventory.

The supported literal/expression and shell classes are those qualified under ADR-0014. Runtime-generated matrices, indistinguishable combinations and unsupported syntax remain explicit unresolved outcomes with retained input scope. They are part of negative acceptance coverage.

## Remaining method decisions and resolutions

| Method issue | Resolution for implementation | Qualification obligation |
| --- | --- | --- |
| Association versus full step completeness | Establish a job/variant association from sufficient unique source-defined witnesses, then match and assess individual steps. Keep scoped problems when a step is missing. | Erasing an install row may preserve a different unique identity witness, but must remove install success. Erasing the distinguishing witness must leave competing variants unresolved. |
| Competing or incomplete origins | Compare against the complete admitted static instance set and exact-attempt records. Preserve unknown competitors and contradictions. | A unique-looking positive edge cannot override an indistinguishable variant, unsupported competing origin or conflicting runtime record. No association from list position or unexplained elimination. |
| Scoped identities | Use one immutable provider job-context identity and referenced specialized-script evidence throughout the existing consumers. Preserve original job keys. | Identical generated script bytes, offsets and command order across variants must produce distinct execution/dependency identities. |
| Missing historical scope | Preserve historical scope and method limits explicitly. Infer an ordinary context only where the retained representation/method supports it. | An old matrix capture without variant scope must not decode into an ordinary or newly correlated matrix success. |
| Later sequential commands | Parser-owned whole-script structure plus a supported Bash/sh profile, material startup/environment premises and factual step outcome. Shell-control effects stay with the shell owner. | Qualify early-exit, altered fail-fast, builtin/context mutation, startup-file/trap overrides and masking defeaters before enabling later-command positives. A visible unresolved startup effect blocks the stronger result. |
| Scalar and substitution limits | Preserve the ADR's typed literal contract and original/generated text distinction. | Characterize ambiguous numeric/string spellings, comparison kinds, case collisions and one-pass substitution. Unsupported forms cannot enter a positive interpretation. |
| Unnamed step display identities | Retain the existing runner-defined display rule only where its use on the specialized source is qualified. Explicit source-defined names remain the MapProxy witnesses. | A matrix expression in an unnamed run step cannot acquire a guessed display identity from generated text. Leave that witness unresolved until the provider rule is established. |
| Aggregation | Compute per-context outcomes before workflow or overall summaries. | Existential supported consumption remains distinguishable from all-variant completeness. Every required instance and unresolved reason is retained. |
| Reports and native records | Reuse existing report records and native family/version owners, adding scoped states and references deliberately. | Review report decoder state admission, native family/codec selection and material-basis validation as coordinated changes. |

These decisions refine execution inside the accepted architecture. A newly discovered change to its evidence or responsibility boundary returns to that owner with a concrete finding. Routine record naming and helper placement remain implementation judgments.

## Identity and producer-to-consumer migration

Treat the scope tuple as one coherent address. It includes the exact source identity, original job/step, ordinary or expanded context, and occurrence within the original or specialized script as appropriate. Runtime run/attempt/job/step coordinates remain a separately joined observation.

| Producer or consumer | Required migration |
| --- | --- |
| GitHub static definition and specialization companion | Preserve original source, typed coordinates, distinct expansion slots, specialized fields and transformation method. |
| workflow_command_analysis and workflow_command_location | Make the generated-script coordinate space explicit and retain original template/replacement provenance. |
| workflow_commands and consumption | Keep each command's context when deriving static consumption, package operations, version requests and invocation evidence. |
| dependency_exercise candidate deduplication | Include the context reference. Equal source spans or script digests do not merge variants. |
| workflow_runtime_correlation | Retain scoped job associations and independent per-step outcomes/problems, including incomplete and skipped cases. |
| runtime_strengthening and runtime_execution | Require the same context for lookup and assessment. Remove first-job-key selection from matrix-capable paths. |
| dependency_state | Extend ExactCICommandIdentity and semantic-evidence joins. Resolve the specialized command from its retained context. Do not compare generated text directly to the original template. |
| Same-step and later exercise composition | Require the same variant and ordered command/step scope before combining consumption and exercise. |
| Target artifact/environment consumer | Keep its existing declaration/runtime boundary. Reuse specialization only through its admitted consumer contract, with explicit unchanged or newly supported outcomes. |
| investigation_inputs and normal orchestration | Feed one shared prepared source/context basis to the CI owners. Avoid separate model, CLI or report-side expansion. |
| native_capture, CI/input codecs and native_codecs | Retain the new material closure, association basis and versions. Keep old layouts readable within their original meaning. |
| native_projection and checkpoint recovery | Validate cross-record context/reference consistency without re-expanding, parsing shell code, acquiring or re-evaluating. |
| report_projection, report and report_file | Deliver all per-instance results and unknowns through full/CI-only and saved views, with decoder-supported states and actual source links. |

Choose the smallest representation that supplies this address at each supported boundary. An immutable parent context with references is preferred to copying coordinate maps into every record. The Build preflight must name every affected identity comparison and family layout before connecting matrix evidence to normal consumers.

## Dependency-ordered implementation sequence

Every milestone is an interim engineering result until the final acceptance gate passes. Keep the ordinary product valid between milestones. A failed required gate leaves the capability unfinished.

### Freeze baseline and acceptance oracles

Freeze source revision, supported method versions, retained MapProxy material and old report/native fixtures. Record the current ordinary, server-nexe, ApplyPilot and matrix outputs at their own declared proof boundaries. Specify expected changes and semantic parity before editing behavior.

Prepare a complete final-run provider input manifest. The previous CI design replay's synthetic PyPI-unavailable result is diagnostic evidence only. Final normal-product qualification must use actual retained or freshly acquired responses for every reached branch, including genuine unavailable responses where they occurred. Neither a fabricated full investigation nor a fabricated provider failure qualifies the final run.

Exit evidence is a frozen inventory, expected outcome table and executable-check selection. It establishes the comparison basis.

### Establish scoped provider expansion and transformation provenance

Implement the companion and immutable context identities before migrating runtime consumers. Cover all admitted Cartesian/include/exclude combinations, typed values, direct matrix lookups, context-valid field specialization, unchanged ordinary jobs and explicit unsupported results.

Keep the original YAML and command template intact. Retain generated text, its digest, replacement references and generated byte spans. Verify Unicode, repeated coordinates and equal generated scripts in different contexts. Bound expansion work and retain incomplete status when a limit is reached.

Exit evidence is component proof for all four MapProxy variants and supported/refused literal forms. Runtime command support remains an unfinished responsibility.

### Migrate scoped evidence and persistence contracts

Propagate the context through static consumption, candidate identities/deduplication, command addresses and package-semantic joins. Update native family layouts and capture contracts alongside their new values, with historical decoding controls.

Remove assumptions that one job key or one raw command text identifies a single matrix instance. Verify ordinary-path parity and rejects for cross-variant reference substitution before a matrix value reaches an existing positive execution or package-state path.

Exit evidence is complete identity propagation and cold representation proof for this material. The final feature still requires runtime association, execution and public delivery.

### Implement scoped job association and per-step evidence

Use admitted source-defined names and ordered step witnesses against the full competing set. Reuse complete-step matching where applicable, and factor the missing-step early return into scoped association and per-step results.

Preserve duplicates, conflicts, unmatched declared instances and unassigned runtime rows. A failed or skipped runtime result is an observed outcome. It is not a positive command-execution result. A skipped unnamed matrix record may retain an unresolved assignment while remaining visible as a reported skip.

Exit evidence is all eight frozen MapProxy associations plus controlled failure, missing-match, skip and ambiguity results. This milestone establishes reported correspondence within its recorded basis.

### Qualify later-command execution and compose dependency results

Implement the new structural relation in the shell analyzer, with the existing profile/eligibility and runtime-composition owners. Preserve the prior sole/first-command families. Qualify the new relation before it returns positive later-command support.

Freeze the admitted launch/profile and material declared environment sources used in that qualification. Record inherited or ambient assumptions at the declared-profile boundary. A visible unresolved startup source cannot be treated as absent, and a direct claim about the actual initialized process requires evidence appropriate to that claim.

Apply a demonstrated shared profile defeater at its earliest sufficient owner for both existing and new execution families. Record any resulting correction to a former positive as an intentional evidence correction, alongside parity for unaffected ordinary cases. Existing positivity is not authority to preserve a false inference.

Use the scoped result to assess the second requirements command in every MapProxy test variant and coverage. Interpret package state only through the existing manager/environment/source composer. Keep direct test-step success, dependency consumption, installed state and package behavior as distinct results.

Exit evidence includes the required successful command assessments and all semantic/shell defeaters. A hidden unsupported first-command fallback or step-success shortcut fails this milestone.

### Connect normal orchestration, reports and offline recovery

Wire the qualified result through the ordinary investigation and the shared report mapping. Full reports, the CI-only consumer and saved reports must expose each declared/ordinary instance, its actual association basis, reported outcomes, command/dependency results and material unknowns.

Keep mandatory per-instance outcomes visible even when optional raw step detail exceeds its existing report budget. Omission of optional detail carries an explicit reason. File-size failure remains an explicit publication failure rather than silently dropping semantic rows.

Retain and cold-open the normally captured native boundary through the existing checkpoint host/store route. New context validation must reject cross-variant references and incompatible material. Offline recovery restores historical facts with zero provider, model, shell-parser or evaluator calls.

Exit evidence is the integrated normal-path candidate and its saved/native offline views. Final completion still depends on the final artifact and regression gate.

### Qualify the final installed product and decide completion

Build the final candidate package in an isolated environment. Verify imported module origin, package/check-out parity and dependency consistency. Run the actual installed public CLI through production parsing, evaluation, capture, synthesis and reporting on the frozen MapProxy provider observations. Controls may intercept provider transport to replay immutable responses, but must not inject precomputed analysis or a prebuilt investigation result.

An instrumented fixture-driven CLI invocation is recorded as retained-input normal-product execution. A live invocation is recorded separately with its exact identity and observation horizon. When live acquisition is selected, verify the observed base/head and complete attempt before and after; preserve drift or unavailability rather than substitute a new case. Final qualification of the frozen eight-instance case remains mandatory. No target workflow rerun or target-code installation is needed for this evidence interpretation feature.

Reopen the saved report in a fresh guarded process and compare substantive results. Cold-open the captured native checkpoint independently and compare the material scoped evidence. Preserve any interrupted or failed publication and its recoverable boundary under the existing store contract.

Run the complete maintained product regression suite from the final installed artifact, using the repository's full unittest discovery over tests. Run the CI/native/report consumers in experiments that the changed contracts actually affect, including investigator CI presentation, plus applicable architecture/import checks already owned by those areas. The hosted product-verification workflow is an additional publication class if separately selected. A prior test count or a focused pass cannot discharge this full gate.

## Adversarial and regression acceptance

| Contrast | Required observation |
| --- | --- |
| All four successful variants and all four ordinary jobs | Eight distinct contexts with the correct job IDs, per-instance outcomes and unchanged original source identity. |
| Failure in one variant with successful siblings | The failing variant's owning step reports failure. The exact internal command gets only its justified state, and sibling success cannot complete its premises. |
| Matrix fail-fast cancellation with queued or absent siblings | Apply the dedicated cancellation control below. Distinguish failed, cancelled and explicitly skipped outcomes, observed unstarted lifecycle state, and missing runtime evidence without borrowing install results across variants. |
| Tests skipped after an install-step failure | Preserve both reported outcomes. Do not report test execution or dependency behavior from the successful workflow siblings. |
| Explicitly identified skipped job with zero steps | Preserve its job skip and independent association basis, with no step or command-success credit. |
| Unnamed matrix skip with insufficient witnesses | Preserve the reported skip and unresolved variant assignment. Do not synthesize a unique coordinate from array position or an undocumented display convention. |
| Missing install step with surviving unique identity witnesses | Keep the admitted job association and make install execution unknown. |
| Missing distinguishing witness, repeated witnesses or indistinguishable variants | Retain the competing contexts and mark association unresolved. No guessed success. |
| Conflicting or duplicate runtime records, wrong head/run/attempt, extra/missing rows | Reject the invalid join or preserve the affected scoped problem. No silent winner or incomplete-as-complete input. |
| Swap a runtime outcome, semantic fact, generated-script reference or checkpoint record across variants | Reject the inconsistent context, or keep the required proposition unresolved. Same command bytes do not license the join. |
| Same-step or different-step consumption/exercise from different variants | No composed exercise or installed-state witness. |
| Early successful exit or exec before the target | A successful containing step cannot establish the later target. |
| Disabled fail-fast, traps, sourced/evaluated text, shell state mutation, BASH_ENV or another material startup override | Command support is refused or unresolved when the execution-profile premise is not established. A launch flag alone cannot discharge that premise. Review existing execution-family parity against the same actual evidence. |
| Status lists, inversion, pipes, nesting, background commands, dynamic executable, custom profile, continue-on-error | Preserve the exact reported result and block unsupported command strengthening. |
| Literal substitution introduces shell syntax or replacement text contains expression syntax | Analyze actual inserted text once with correct provenance. No sanitization or recursive interpretation. |
| Historical ordinary and matrix captures | Preserve historical facts and method limits, including old unscoped matrix uncertainty. No fresh positive interpretation during decode. |
| Unchanged ordinary paths, ApplyPilot failure and server-nexe skip | Semantic parity where the selected method adds no evidence. Record expected changed explanations or identities separately from changed conclusions. |
| Optional detail budget, missing material, damaged saved report or incompatible native version | Explicit omission/failure and truthful available boundary. All required semantic outcomes remain accounted for. |

At least one mixed-outcome control must contain successful, failed, skipped and unresolved observations together, so an aggregate success cannot hide a missing variant. Controlled modifications are labeled and kept separate from original public observations. Pure shell controls use self-authored commands, without executing the target workflow.

### Matrix fail-fast cancellation control

Use the exact retained MapProxy test strategy. It omits strategy.fail-fast and job continue-on-error, so GitHub's default fail-fast value is true. A matrix failure can cancel in-progress or queued matrix siblings. Already completed jobs may retain their outcomes, and a captured snapshot may still show unstarted work. Treat the configuration as scheduling context, with actual outcomes established by their own records. The original captured attempt succeeded. Label the following adversarial inputs as controlled contrasts. [GitHub fail-fast semantics](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idstrategyfail-fast)

1. In one four-variant contrast, record a failing variant, a sibling cancelled after starting, a sibling with supported queued/unstarted evidence at the observation horizon, and a declared variant with no runtime row. Preserve all four declared contexts and the four ordinary jobs.
2. Add companion contrasts for an explicitly skipped job, cancellation before execution where a qualified provider lifecycle witness is available, and cancellation whose start phase is unknown. Cancellation outcome and started/unstarted phase are separate facts. A queued observation establishes unstarted state at that capture, while a final claim that a job never started requires evidence covering that stronger horizon.
3. Missing rows, absent timestamps and empty step lists alone cannot establish that a job never started. If the captured provider fields do not support a lifecycle distinction, preserve the phase as unknown. Qualify only the minimal needed lifecycle evidence through the existing provider/native/report path.
4. A job-level failed or cancelled conclusion alone supplies no installation success or failure. For cancelled or unstarted variants, retain unknown installation outcomes unless the same scoped record supplies admissible command/step evidence. A successfully completed install before a later cancellation keeps only its independently earned command-boundary evidence.
5. Verify the distinctions through per-variant assessments, aggregation, saved-report reopening and native recovery. The failure or cancellation of one variant cannot erase another variant's evidence or manufacture results for an unstarted or unobserved sibling. The ordinary jobs retain their own outcomes, since matrix fail-fast applies to its matrix.

This control is required at scoped association, execution composition and final integration qualification. Its oracle must distinguish all five requested categories, retain unresolved lifecycle/assignment premises and avoid attributing a cancellation cause from configuration alone.

Predeclare the oracle for each control from the source/observation contract. For matched positive rows, verify the selected command and context, not only a top-level supported flag. For partial and negative rows, assert the exact missing or conflicting premise and the surviving reported observations. Use the unchanged real captures to verify identity and output fidelity, with separately labeled controls for defects absent from those captures.

## Final completion gate

Matrix support within this accepted scope is complete only when all of the following have evidence from the final candidate.

1. All eight required declared/ordinary contexts are represented, and the frozen input supplies the four distinct matrix associations and required requirements-command assessments.
2. Identity/provenance survives every migration boundary, and adversarial cross-context substitution fails safely.
3. Failures, cancellations, explicit skips, supported unstarted lifecycle observations, missing runtime evidence and unsupported forms remain distinct. The matrix fail-fast control passes through the full delivery/recovery path. Per-instance coverage and existential aggregate support remain distinguishable.
4. The actual normal installed CLI produces the result through its production entry point. Its saved report reopens offline with substantive parity.
5. The normally produced native material survives guarded cold checkpoint recovery and historical compatibility checks at the declared codec/method boundaries.
6. Static interpretation, reported correspondence, command execution, installed-state interpretation and behavior exercised by tests retain their separate proof strengths and unknowns.
7. Expected unchanged paths retain semantic parity, all relevant contract consumers pass, and the complete maintained product regression suite passes on the final artifact.
8. The receipt names the input/artifact revisions, executed commands, outcomes, retained failures, remaining limitations and exact supported scope.

If a required gate fails or cannot be executed, preserve the proof debt and keep the feature unfinished. An unavoidable real limitation can justify a scope revision only through a visible owner decision with its product consequences. It cannot be renamed a passing final gate.

## Risks, change boundary and handoff

The principal risks are scope loss in existing identities, ambiguous partial matches, false later-command positives, and decoded records that silently acquire new meanings. The stages and contrasts above directly target those risks. Literal typing and shell effects deserve narrow-to-broad tests before integrated positives. The existing normal code, active tests, frozen real inputs and independently transcribed control outcomes are the proof sources.

Build may change the existing GitHub/CI/dependency interpretation boundaries, native codecs/recovery validators, report/CLI delivery and their tests as required by this plan. Prefer existing owners and standard-library representations. Additional dependencies, a general expression interpreter, human-graph acquisition, target workflow mutation and new action permissions require a separate concrete need and owner decision.

Ali requested method review and planning before Build. Present the implementation sequence, residual risks and gates for that review. Completing this planning artifact does not activate Build or establish product acceptance. Interim engineering completion and final capability completion must be reported separately throughout execution.
