# Experiment 3: revision-bound Investigator interaction

**Result for review, 2026-10-08.** Retain a small typed, storage-independent consumer boundary around host admission and native owners. The provisional SQLite WAL/FULL adapter and encoded-memory baseline produce identical declared interaction checkpoints across **21 scenarios × two backends × two transports = 84 traces**. This is lifecycle fidelity on disclosed fixtures, not semantic correctness, adequate investigation, Investigator superiority or production adoption.

**Subsequent grounding qualification:** [scenario reachability and known-public native trial](../2026-10-08-workspace-experiment3-grounding/README.md) distinguish intrinsic/current/future/defensive roles. Here, “head/target change” means refusing continuation of an old exact-target lineage under a different target; it does not mutate historical SHA-bound evidence. Following a moved head would require a new lineage and explicit reuse/revalidation rules. The historical synthetic results below are unchanged.

[Progressive cycle history](../../2026-10-08_workspace-implementation-architecture-research_lbd-cycle.md#experiment-3--authorization-question-and-setup) preserves assumptions, failures and reasoning changes. [Results](results.json) pin outcomes, selected inputs, checkpoint hashes, code/native-tree hashes, runtime/settings and parser costs. The [normal interaction checkpoint](interaction-checkpoint.json) retains the full experiment trace. [Main's ADR](../../../docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md) and the [research plan](../../../plans/INVESTIGATION_WORKSPACE_IMPLEMENTATION_ARCHITECTURE_RESEARCH_PLAN.md) retain their authority; this evidence does not promote them.

## Setup and decomposition

A deterministic consumer reads the actual native support-drop selector's unresolved need on synthetic repository/dependency/release inputs. A separate driver simulates exact target-file delivery; existing target declaration, relevance and impact owners produce `unresolved → established_applicable`. No provider/model calls, source extraction, target-code execution or production mutation occur. Candidate meaning is supplied and grounded through existing native validation. Contrary README relevance is fixture-routed; no semantic discovery or conflict normalization is claimed.

| Responsibility | Executable owner and direction |
| --- | --- |
| Consumer values, views, attributed requests/proposals | [Typed seam](../../../experiments/workspace_investigator_seam.py): `InvestigatorPort → WorkspaceHost`. Consumer surface has `read`, `request`, `request_bytes`, `propose`; it cannot admit, execute, publish native truth, change policy or manipulate checkpoints. |
| Admission, attempts, observations, problems and basis/history | Same module's host; exact original and current bindings, target, scope/discriminator, method, capabilities and current authority precede effects. Capability driver calls host `start`/`observe` separately. |
| Native need and domain meaning | [Native bridge](../../../experiments/workspace_seam_native.py) → existing upstream, impact and target owners. Opaque retained bytes are compared with this live fixture; restoration never constructs trusted native objects from them. |
| Persistence/recovery | [Private adapters](../../../experiments/workspace_seam_checkpoints.py) → experiment-2 store and experiment-1 checkpoint encoding. SQLite details stay here. Consumer values contain no tables, transactions, WAL or engine exceptions. |
| Scripted pressure and independent oracles | [Runner](../../../experiments/run_workspace_seam_trials.py), [tests](../../../experiments/tests/test_workspace_investigator_seam.py) → experimental modules and native source. Product runtime imports none of these. |

Material slot bindings distinguish candidate/need/context dependencies from historical retention links. This registry and relevance routing are host-controlled fixture inputs, not a general premise-discovery algorithm. All trace records and earlier state indexes remain retained for this experiment; checkpoint-internal state is excluded from Investigator evidence/views. Selective retention, publication cadence and scalable indexing remain separate questions.

## Discriminating results

| Pressure | Observed result |
| --- | --- |
| Delayed result after unrelated revision | Admitted after current validation; original revision and later admission revision remain distinct. |
| Changed material premise or relevant counterevidence, same head | Old request basis rejected. Prior assessments and rejected-result content remain historical. |
| Contrary README and missing counterobservation | Both enter owner-selected inputs even when omitted from a consumer view. The native target API admits one `pyproject.toml`; enlarged input sets stay `unsupported_owner_input_set`, with no invented conflict or adequacy result. |
| Head, method, capability or authority change | Old result rejected under its binding; old target/history is retained. A changed target requires a separate lineage/store, rather than in-place rebinding. |
| Native final assessment | Native selector's old need is retired. Procedural completion and native applicability do not establish adequacy or action permission. |
| Exact duplicate, second admitted attempt or source alias | Delivery history can acknowledge known data, but only one evidence basis remains. Identity/content inconsistency is a problem before semantic evaluation. Identical bytes in different scopes keep distinct identities. |
| Retained but omitted content | Addressability is disclosed. A citation to an undelivered item is rejected; a later explicit read permits an attributed proposal, whose evaluation remains unsupported. A view records delivery, with examination/use unknown; a proposal records a consumer assertion of use. |
| Recovery and unknown completion | Restored host starts historical-only. Explicit current validation precedes continuation; each operation separately validates method/capability. An unknown attempt cannot be restarted automatically. Known capability failure is a problem, never a negative domain observation. |
| Competing publication | Portable publication conflict leaves the local revision unchanged. After refresh/revalidation, unrelated changes permit delayed admission; material changes reject it. SQLite cases use independent connections. |
| Unconfirmed checkpoint acknowledgement | Injected failures before publication and after committed publication both produce a portable unconfirmed outcome; refresh reveals which state exists. Neither grants execution retry permission. |

**74 seam tests**, repeated against memory and SQLite, plus **32 inherited storage/representation regressions** and **58 native/report anchors** pass. The matrix independently checks expected statuses, actual selected identities, immutable prior assessment bytes and restored checkpoint fidelity before comparing four hashes per case. Broader product/experiment suites, models and hosted verification were not run.

## Failed approaches and reasoning changes

- [Initial check](initial-check.json): 21/22 tests passed, but the SQLite fixture used an existing directory with `create=True`. That run established no SQLite comparison; a fresh subdirectory repaired setup.
- After an early green run, [two adversarial tests failed](binding-correction.txt): current basis was accepted at an older claimed revision, and a proposal silently inherited a changed method. Original-revision bindings and view/proposal method provenance now have separate checks. Current equality and retained references alone were insufficient.
- [Counter setup failure](counter-setup-correction.json): a helper ignored supplied contrary content and retained a gap. Matching outcome strings missed incorrect stimulus coverage; an independent selected-ID assertion exposed it. Both content cases now assert actual identity, and the entire matrix was rerun.
- Broad input dispatch was rejected: the existing native evaluator cannot consume arbitrary contradictory sources/unknowns. Selecting those inputs and preserving unsupported evaluation is preferable to silently dropping them or inventing a general evaluator.
- Automatic retries, revision-number-only rejection and checkpoint-derived authorization were rejected. A private consumer facade and portable unconfirmed-publication outcome make the responsibility boundary executable. Python private attributes are not process isolation against hostile code.

## Transport comparison and minimum H1 projection

Typed Python is the simpler baseline for an in-process consumer. The strict request envelope adds bounded non-executing parsing, exact fields/types, duplicate-field refusal and rejection of supplied admission/principal/permission/truth fields. It produces the same request and trace; the scripted wire consumer also reads a serialized projection rather than host policy/native fixture objects. No RPC service, framework or H1 mechanism is selected.

The representative request is **1,431 bytes**. Seven warm batches of 1,000 iterations measure median typed construction at **2.469 µs** and encode/decode at **28.216 µs**; all samples are retained. These exclude host admission, native work, persistence and scheduling. They support optional transport validation, not a throughput requirement or technology preference.

An H1-facing projection needs exact target/lineage/revision and view identity; stable evidence IDs with owner, exact scope, content or explicit gap and material references; delivered versus omitted-but-addressable identities; current material bindings; native need/discriminator and limitation records; method/capability descriptions and historical/current continuation status. Requests/proposals must carry their originating revision, basis, method and attribution/citations. Delivery is not examination, citation is not evaluated support, and capability description is not permission. Independent evaluator selection must include relevant counterevidence and unknowns beyond proposer citations. Actual H1 integration, pre-candidate discovery policy and broader capability schemas remain outside this experiment.

## Limits and review boundary

The support-drop path is one bounded native witness. General proposal semantics, arbitrary conflict evaluation and adequacy remain unsupported. Capture completeness and the tagged-field/native-object codec are still incomplete; explicit graph relationships cannot discover missing material premises. The host registry, authentication principal, driver and counterevidence relevance are supplied offline controls. Concurrency covers conditional publication and revalidation, not distributed operations or exactly-once external effects. No hidden model state, rerunning/replay guarantee, full recovery implementation or legacy migration is demonstrated.

Carry SQLite **WAL/FULL provisionally**, with the [file-store comparison](../2026-10-08-workspace-checkpoint-stores/README.md), power-loss/OS-crash limits, retention policy debt and unavailable physical-write-amplification measurement intact. Hybrid is still unjustified. No new storage benchmark or stronger durability claim is made here.

**Stop for experiment 3 review.** Provisional recommendation: retain typed consumer values, separate host/native/persistence responsibilities, explicit original/current basis checks and portable failure outcomes; serialize only when a consumer needs transport. Main owns final decisions. Experiment 4 migration feasibility remains unactivated. Review should distinguish mechanical basis invalidation from semantic refutation, and an unsupported evaluator from an unresolved proposition or adequate stop.

Reproduce:

```bash
PYTHONPATH=src .venv/bin/python3 -m unittest experiments.tests.test_workspace_investigator_seam experiments.tests.test_workspace_checkpoint_stores experiments.tests.test_workspace_revision_representation
PYTHONPATH=src .venv/bin/python3 -m experiments.run_workspace_seam_trials --output /tmp/upgradepilot-seam-review
PYTHONPATH=tests:src .venv/bin/python3 -m unittest test_ci_dependency_state test_conditional_pyproject_consumption test_python_support_impact test_impact_applicability test_report test_report_file
```
