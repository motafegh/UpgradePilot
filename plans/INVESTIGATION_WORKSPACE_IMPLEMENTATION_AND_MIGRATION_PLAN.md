# Investigation Workspace Implementation and Migration Plan

**Status:** prepared execution/proof plan under accepted architecture and reconstruction/storage methods; production implementation requires separate activation.
**Responsibility:** replace the fixed investigation snapshot with a canonical evolving Workspace, preserve native meanings and material basis, prove cold recovery/explicit continuation and cut over supported consumers.
**Live selection:** [MEMORY.md](../MEMORY.md) alone.

## 1. Full target, boundaries and owners

The supported product responsibility is a provenance-backed, uncertainty-aware dependency-update investigation for public Python maintainers. Implement the coherent target:

```text
normal native acquisition/producers/evaluators
→ canonical evolving Workspace and host-controlled publication
→ explicit Investigator/evaluator/synthesis/report projections
→ historical checkpoint recovery
→ separately invoked validated continuation
```

Native owners retain their bounded facts/evaluations. Workspace owns composition, lifecycle, revisions and recovery. Maintainer synthesis retains action permission; unsupported semantic/adequacy evaluation cannot become justified stopping. Existing report/save/open behavior remains its separate consumer contract. [ADR-0012](../docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md) owns the architecture; [Core §6.4](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md#64-canonical-investigation-recovery-and-explicit-continuation) owns recovery semantics.

| Owner | Execution consequence |
| --- | --- |
| [Charter](../PROJECT_CHARTER.md), [project route](UPGRADEPILOT_90_DAY_PLAN.md) | Public Python/Dependabot decision support, lawful read-only evidence and stage claim limits; no target mutation. |
| [Core](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md) | Trust/retention/representation, earliest sufficient validation and coherent recovery; plans cannot redefine these invariants. |
| [Product Decision Model](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md) | Discovery versus proposition-relative investigation, applicability, counterevidence, material validity and adequacy obligations. |
| [Maintainer Action Synthesis](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md) | Preserve the admitted action boundary and residual uncertainty during migration; no new permission. |
| [ADR-0010](../docs/architecture/ADR-0010-package-manager-semantic-facts-and-runtime-dependency-state-composition.md), [ADR-0011](../docs/architecture/ADR-0011-explicit-source-association-bases-and-proposal-boundary.md) | Preserve independent native command/semantic facts and distinct source-association/proposal effects. |
| [Accepted reconstruction/storage method](../docs/architecture/ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md) | Explicit owner codecs, immutable revisions and provisional local SQLite publication/backup with stated support/refusal and durability limits. Apply the accepted method during separately activated Build. |
| [Minimum Useful Generality](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md), [Naming Clarity](../docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md) | Representative actual input forms/variants and expressive responsibility names; no fixture-derived semantic answers or historical step-code architecture. |
| [Report/usefulness plan](MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md#5-independent-usefulness-evaluation), [Security](../SECURITY.md) | Independent utility/semantic proof and deliberate local/public capture/authorization boundaries. |

Includes material native capture/reconstruction, immutable cross-domain state, relevant lifecycle/view/basis records, synchronous in-process host integration, local checkpoint publication/backup/restoration, explicit continuation and replacement consumer migration. Model-free fixtures isolate mechanical boundaries; representative normal-path evidence supports broader capability claims.

Separately activated responsibilities: deterministic replay; new semantic/adequacy evaluators; Investigator policy/model/framework/topology; broader discovery/runtime/impact coverage; autonomous actions; private/multi-ecosystem inputs; hybrid blobs, services/queues and general query infrastructure. Retain named limitations/entry triggers for these responsibilities rather than silently satisfying them with codecs or fixtures.

## 2. Entry reconciliation and decisions

Read the accepted owners, [implementation research synthesis](INVESTIGATION_WORKSPACE_IMPLEMENTATION_ARCHITECTURE_RESEARCH_PLAN.md#cross-experiment-recommendation-for-main--evidence-dated-2026-10-09), [migration capture/cutover evidence](../working-memory/evidence/2026-10-09-workspace-replacement-migration/README.md), relevant current producer/consumer source and tests. Reconcile changes from those dated source horizons before choosing the actual Build slice. Research code is non-controlling evidence, not the production implementation to copy.

Entry requires: explicit implementation activation; A-phase orientation under the canonical cycle; accepted affected method decisions; an owner/type/version and consumer inventory for the selected slice; no unresolved material authority/retention conflict; proof resources for fresh-process recovery and the required negative controls. If a genuinely unresolved method would change the implementation, perform its smallest discriminating check; another broad research spike is not a default prerequisite.

| Decision | Implementation baseline / disposition |
| --- | --- |
| Native representation | Explicit family/type/version codecs with separate capture envelopes and actual material-input references; no generic native-object hydration. |
| Revision/storage | Immutable published successors; private standard-library SQLite WAL/FULL adapter with conditional predecessor publication. |
| Publication/loss | Durable acknowledgement per canonical transition, including attempt intent before execution; unpublished staging and lost acknowledgement disclosed. |
| Retention/backup/versioning | Retain all declared local investigation revisions/material closure initially; explicit validated online backup; supported version 1 and incompatible-version refusal. No pruning or automatic migrations. |
| Projection/migration | Direct supported native consumers derived from Workspace. A one-way legacy projection earns only a named parity/compatibility purpose. |
| Initial source scope | Local host-owned checkpoints outside Git; capture relevant public evidence and available public-safe provenance, with missing identities explicit. |
| Routine Build details | Choose concrete modules, SQL columns, CLI spellings and bounded parser/resource limits from actual owner inputs; document and test their supported boundaries without another ADR per helper. |

ADR-0013 owns the accepted consequential method above. Existing Core/decision specifications already own the required meanings: no new specification is needed merely to restate recovery or proposal authority. If implementation design changes a stable semantic/compatibility contract, update its existing owner before coding that change. Review any independently required byte/schema compatibility promise at the codec boundary; Python dataclass layout is not that promise.

## 3. Native material and supported-family ledger

Trace producer → composition → consumer. For every admitted family, identify encoded variants/nested values, exact input/content basis, method/source identity, material references, capture boundary, decoder compatibility and consuming projection. Keep a checked ledger in the active cycle/evidence; this plan supplies its initial source-grounded map.

| Native family / current anchor | Material capture and consumer obligations |
| --- | --- |
| PR/changed files and dependency analysis: [investigation](../src/upgradepilot/investigation.py), [dependency analysis](../src/upgradepilot/dependency/analysis.py) | Exact repository/PR/base/head and dependency transition; changed-file/patch evidence, admitted base/head source contexts and source problems. Preserve `source_contexts` before the final legacy result loses them. Unsupported transition still supports an honest partial report. |
| CI/runtime: [coverage](../src/upgradepilot/ci/dependency_exercise.py), [dependency state](../src/upgradepilot/ci/dependency_state.py) | Full supplied workflow run/jobs/steps/definition/project-environment inputs (`coverage_inputs`), consumptions, correlation, command identity, independent package-manager facts and state results/blockers. Command completion cannot become fresh installation/later use/compatibility. |
| Package/upstream acquisition: [PyPI](../src/upgradepilot/pypi/release.py), [upstream interval](../src/upgradepilot/upstream/interval.py) | Old/new package metadata, release index/crossed selection, repository/tag/changelog discovery and authority/results/problems. Preserve supplied exact content/provenance; do not claim unrecorded raw response capture. |
| Upstream interpretation: [support-drop bridge](../src/upgradepilot/upstream/support_drop.py), [claim owner](../src/upgradepilot/upstream/claim.py) | Actual source window, attributed candidate, validation inputs/results and available method/model/configuration identity; unavailable prompt/response/provenance has an explicit recovery limitation. Capture does not repair semantic-role failures. |
| Python target/impact: [support applicability](../src/upgradepilot/impact/python_support.py), [target relevance](../src/upgradepilot/target/relevance.py) | Candidate and pre/post assessment, need/selection, exact acquired declaration and relevance basis, retired/open follow-up and native unresolved/not-applicable states. |
| Artifact/environment: [serviceability](../src/upgradepilot/impact/artifact_serviceability.py), [target environment](../src/upgradepilot/target/artifact_environment.py) | Distribution candidate/problems, dependency-associated static target environments and assessment/not-evaluated state. Never hydrate unsupported artifact history or source-build success. |
| Workspace interaction/assessment history | Actual discovery objectives/needs, views/delivery/omissions/observable use, proposals/admissions, attempts/results/problems, evaluator outcomes and material basis/history. No simulated interaction may be described as a production observation. |
| Synthesis/report: [synthesis](../src/upgradepilot/maintainer_action.py), [projection](../src/upgradepilot/report_projection.py), [report codec](../src/upgradepilot/report_file.py) | Retain generated synthesis with its method/material basis; one-way projection preserves findings, sources, uncertainty and action limits. Recovery/rendering uses retained conclusions without evaluator calls; fresh synthesis is a separate admitted operation. Report identity/digest is distinct from Workspace identity/integrity; saved report is never recovery input. |

The first technical increment exercises the CI/runtime and Python-support families plus their shared identity/dependency/upstream/source inputs. It proves cold reconstruction and consumer parity for those supported variants, not all rows. Include positive and problem/unresolved/not-evaluated variants that the selected consumer normally encounters; do not support only a known happy path.

Before default full-path cutover, account for every legacy field and material producer input across all currently admitted normal product/report branches, including uv/optional-extra/group, provider failures and artifact/environment variants. Either provide native reconstruction/projection or an explicit staged limitation that blocks affected use. An unsupported codec must not silently suppress an already supported report fact. A partial-path milestone cannot claim complete replacement; narrower supported operation requires a visible scope decision and product-cost review.

## 4. Ordered implementation responsibilities

### Technical stages and cycle boundaries

Keep these six responsibilities as implementation/proof stages. A stage is not a prescribed full Learning-by-Doing cycle; one coherent cycle may cover several connected stages, with explicit internal verification and learning stops.

| Stage | Implementation / proof responsibility |
| --- | --- |
| 1 | Concrete capture/consumer contracts and supported native capture/cold reconstruction. |
| 2 | Immutable Workspace revisions and coherent durable checkpoint publication. |
| 3 | Lifecycle, host admission and material-basis validity integration. |
| 4 | Complete reconstruction/projection coverage across currently admitted native families. |
| 5 | Direct synthesis/report consumer migration with retained historical conclusions. |
| 6 | User-facing offline recovery/explicit continuation and final obsolete-plumbing retirement. |

The Workspace native-foundation cycle groups stages 1 and 2: retained native meaning and its coherent durable publication form one responsibility. Its internal stops are:

1. Verify supported native capture and fresh-process reconstruction, including missing/corrupt/wrong-target/unsupported-version refusals; review the actual result and learner gaps before durable publication work.
2. Verify immutable publication, interruption/conflict/storage-refusal and validated-backup behavior; review the actual result and claim limits before the combined recovery proof.
3. Prove fresh-process native reconstruction from a declared durable checkpoint, then complete evidence-backed D/E for the combined responsibility.

These stops preserve focused proof and learning inside the same cycle and record. They do not close a separate full cycle per stage. Reassess subsequent cycle boundaries from the resulting engineering evidence, unresolved responsibilities, proof cost and learner ownership before semantic integration or product cutover. Later stage ordering may overlap where interface proof requires it; default cutover still requires the admitted family/consumer closure below. [MEMORY.md](../MEMORY.md) owns actual selection and phase position.

### Define the concrete capture and consumer contracts

Resolve the selected codec family/version matrix and native-input closure against the ledger. Define the minimal Workspace identity/revision/record/basis and projection interfaces with explicit supported outcomes. Trace all 24 current legacy fields and hidden material inputs; classify retain/move/remove by admitted responsibility rather than constructor compatibility. Apply ADR-0013's accepted cadence/retention/backup/trust method; reconcile any material proposed departure at its owner before code depends on it.

Deliverable: reviewable mappings and owner interfaces sufficient for the first capture/reconstruction action, plus a remaining-family/consumer ledger. Deepen this design only when a material question blocks execution. Keep field layouts/version handling with their responsible implementation and method owner.

### Capture native material and prove cold reconstruction

Instrument the production path at explicit native/composition boundaries; do not adopt experiment monkeypatch hooks as a permanent capture system. Preserve native processing once, with actual inputs/results and gaps, into storage-independent immutable encoded records. A fresh child process reads only the retained boundary, reconstructs supported native projection values and produces comparable native/consumer summaries without a live-value map.

Independent re-entry refusal must cover provider, model and evaluator calls in the recovery child, including synthesis/adequacy; flat counters alone are insufficient. Compare complete supported native values, scope/basis/unknowns and native-consumer meanings against the original sequence. A full synthesis/report comparison requires every material codec and retained evaluated conclusion used by that exercised historical consumer; until then the first gate proves CI/impact projections only and retains full report parity as a later obligation. Test any freshly generated synthesis separately as admitted evaluation, not recovery. Never fill unsupported fields from a live cache or defaults to obtain a complete report. At fixed report time normalize only declared generated IDs. Corrupted, missing, wrong-target and unsupported-version material must refuse affected projection. Stop for result/learning review before broadening the supported codec set or claiming canonical production recovery.

### Publish immutable Workspace revisions and local checkpoints

Build host-controlled identity/reference/allowed-effect admission and coherent publication around the native capture path. Apply accepted domain evaluations at their owner; do not force established native facts through a model proposal. Implement the private SQLite store/backup boundary and supported version handling. Keep logical material basis, content deduplication, scoped record identity and transaction predecessor distinct.

Prove process interruption before/after intent, content, commit and acknowledgement; competing writers; damaged references/catalog; missing closure; unsupported schema; busy/read-only/full refusal; validated backup and explicit earlier-boundary loss. Ensure failed publication leaves a truthful outcome and never triggers an external retry. Review supported durability claims against actual environment proof; power-loss behavior is not inferred from SIGKILL.

### Integrate lifecycle and direct consumer projections

Replace orchestration's final snapshot construction with native/Workspace publication. Provide small typed in-process views/requests/proposals and host admission/attempt/result/evaluation boundaries for the admitted capabilities; no generic scheduler or model policy is required. Preserve pre-candidate discovery versus genuine proposition-relative needs and unsupported evaluator outcomes.

Use a real native selected-read/reassessment path where possible. Exercise same-target unrelated/material changes, counterevidence/unsupported conflict, target movement, capability/method withdrawal, duplicate delivery and scoped empty/failed reads with their correct proof class. Unsupported native conflict/adequacy remains unsupported; lifecycle bookkeeping cannot invent its evaluation. Evaluator projections include owner-relevant counterevidence/unknowns independently of proposer citations.

Cut synthesis/report to explicit Workspace-native inputs and keep their action/report contract unchanged. Normal synthesis runs through its owner and publishes its result/basis; historical rendering consumes the retained conclusion. Refactor the existing report-projection synthesis call at this boundary rather than treating it as permissible during recovery. Update CLI wiring and add distinct offline Workspace inspection and explicitly invoked continuation surfaces with truthful supported/refused outcomes; exact flags are routine Build choices. Current report `--open-report` remains its separate offline path. Recovery is side-effect-free; continuation revalidates target/material/method/authority and only then admits available capabilities/evaluation. Ambiguous completion remains unresolved until deliberate reconciliation.

### Complete supported-family cutover and retire obsolete plumbing

Extend capture/reconstruction and projections across the admitted family ledger before default cutover. Preserve meaningful source/provider/domain/CLI/report assertions through the canonical path; remove adapter-only plumbing/tests only after their independent proof/compatibility obligations end. Review actual diagnostic/experiment callers without retaining a product type solely for dated tooling.

Prove one normal acquisition/native sequence, complete source/meaning/unknown/action parity for supported branches, new lifecycle/recovery retention and installed CLI behavior. Update active documentation to describe the Workspace path and actual limitations. Any temporary legacy bridge is one-way from Workspace, never a second writable/acquisition path, and has a named caller/proof purpose, loss boundary and removal trigger. Preserve new canonical history during rollback.

## 5. Evidence and verification gates

Run focused owner/codec tests before cross-owner/CLI tests, then the justified full product and fresh-installed regression. Use native source tests as semantic oracles; move them only when the owning interface changes. Add independent boundary proofs rather than duplicating implementation shape. Keep experiment/developer-tool results separate from product proof.

| Claim / boundary | Required discriminating proof | Stronger claim not earned |
| --- | --- | --- |
| Capture completeness | Independent named-consumer input inventory plus encoded reference closure; missing-input negative control survives even when round-trip passes. | Every future native family or evaluation premise captured. |
| Cold native reconstruction | Fresh process; no live cache; provider/model/evaluator re-entry forbidden; native scope/unknown/historical-consumer parity and refusal variants. | Fresh source truth, compatibility or deterministic replay. |
| Immutable revision identity | Prior views/checkpoints stable; scope/content collisions and duplicates distinguished; annotations cannot mutate originals. | Event sourcing or unlimited history performance. |
| Coherent durable publication | Real process interruption, expected-revision conflicts, unconfirmed acknowledgement, storage refusal and explicit recoverable boundary. | Device/power-loss guarantees or exactly-once capability effects. |
| Offline restore/backup | Restore declared revisions/material closure from supported backup; damaged/version-incompatible state refused; zero external/evaluator execution. | Current execution authority or untrusted-import authenticity. |
| Lifecycle/basis validity | Original basis retained; unrelated later revision can remain valid; material/head/method change discriminated; unknown attempts and duplicate observations handled. | General semantic invalidation/conflict solver. |
| Evaluation/stop authority | Native assessments preserve owner meaning; unsupported proposal/adequacy stays explicit; procedural finish cannot admit stop/action. | New evaluator competence or Investigator superiority. |
| Direct consumer cutover | One native producer path; normal and recovered projection parity for admitted families; full relevant product/report/CLI regressions and installed package. | Independent usefulness or broader ecosystem coverage. |
| Representative variation | Real retained-input native cases and controlled identity/source/problem variants; supplied extractor answers disclosed; fresh live/model proof only if separately admitted. | Unseen semantic acceptance from development cases. |

Use the [migration tests](../experiments/tests/test_workspace_replacement_migration.py) and [public grounding tests](../experiments/tests/test_workspace_public_grounding.py) as evidence/oracle ideas, not imported production contracts. Product tests belong under `tests/`; product runtime must not import `experiments/`, `tests/` or `tools/`. Build proof must cover appropriate dependency/CI/impact/synthesis/report/investigation tests, not only codec tests or Ruff.

## 6. Evaluation and later handoff triggers

| Responsibility | Concrete activation/readiness condition | Owning next action |
| --- | --- | --- |
| Independent report utility | Exact normal outputs, equivalent ordinary-review evidence and reviewed labels/reviewer protocol are ready. Existing output may qualify before Workspace completion. | Freeze/run the separately authorized [usefulness study](MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md#5-independent-usefulness-evaluation); do not make code parity its utility baseline. |
| Post-migration utility regression | Direct/recovered consumers pass parity and equivalent case outputs can be produced. | Reassess added/lost user value under the same protocol; snapshot inputs and disclose changed evidence modes. |
| Investigator mechanism comparison | Product-facing typed views/native facts and admitted request boundaries have reproducible contract tests; laboratory protocol can bind exact target/basis/authority. | Explicit joint selection under the laboratory's own protocol/local-only authorization; no automatic inference launch. |
| Semantic/adequacy method | A decision-critical unsupported owner prevents a useful proposition/stop/check; additional acquisition cannot resolve missing evaluation capability. | Select a bounded method/evaluation responsibility with baseline, protected evidence and rejection criteria. |
| Deterministic replay | Required retained inputs/method identities and an independently useful re-execution boundary can be specified. | Activate its own scope/equivalence plan under Charter §6; never claim recovery as replay. |
| Additional coverage/storage policy | A representative case or measured loss/volume defeats the declared native/retention boundary. | Review exact expansion, pruning/migration or storage alternative at its owner; preserve excluded capability and product cost. |

At each satisfied handoff, MEMORY must select the follow-up or record an explicit evidence-backed defer/reject/reschedule disposition. Open advanced-method responsibilities cannot silently disappear behind more ordinary implementation. Independent reviewer availability does not block unrelated mechanical work, but usefulness remains unproved until its actual gate passes.

## 7. Completion, stop and modification boundary

Completion requires the selected supported family ledger, canonical native path and direct consumers to pass their declared native/retention/lifecycle/recovery/continuation/installed proof, with explicit residual limitations and legacy retirement/compatibility disposition. The complete target remains unfulfilled when a staged increment delivers only capture or opaque recovery. Report independent utility, semantic competence and replay separately, including truthful debt.

When activated, allowed Build changes are the necessary product native/capture/Workspace/persistence/consumer interfaces, their active tests, relevant CLI/docs and directly affected evidence/owner records. Add a responsibility-owned package only if concrete code needs it under ADR-0007; standard-library SQLite needs no new dependency. No framework, policy/model replacement, target execution/write, private capture, general raw archive, automatic migration/pruning or action permission is authorized by this plan.

Each coherent action ends with its verification, evidence-backed learning, gap disposition and commit/push under the standing cadence. Stop on material contract/method conflict, missing required proof, unsupported reconstruction of a required branch, or the next separately owned responsibility. Plans may be challenged under the Smart Situational Override Rule; reconcile material changes before implementation rather than following stale steps or silently redefining completion.
