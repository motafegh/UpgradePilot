# PR-driven caller/signature evidence integration design

**Status:** concrete proposal for review, not implementation or product adoption.  
**Bounds reconciliation:** October30 §7 supersedes the initial unimplemented numerical proposals using qualified source/evidence; other proposal/adoption boundaries retain their own horizons.
**Owning plan:** [API-change/target-exposure feasibility](../../../plans/UPSTREAM_API_CHANGE_AND_TARGET_EXPOSURE_FEASIBILITY_PLAN.md).  
**Structural checker:** [existing child plan](../../../plans/DETERMINISTIC_API_CALL_AND_SIGNATURE_EVIDENCE_PLAN.md), [HTTPX result](../2026-10-28-caller-signature-build/REVIEW.md), [glyphsLib/pytest result](../2026-10-28-caller-signature-second-real-case/REVIEW.md).  
**Cycle:** [current design progression](../../2026-10-28_pr-driven-caller-signature-integration_design-cycle.md).  
**Workspace scope:** [third-subject discussion](../../2026-10-28_workspace-migration-scope-for-api-delivery_discussion.md).

## 1. Outcome and acceptance horizon

Input is a public repository and PR number. The system obtains the native dependency transition, bounded relevant source and justified source-level relationship candidates, runs the existing argument checker where its premises permit, saves a useful explanation and reopens it offline. Operator-supplied target paths, adapter versions, callable pairs, removed argument names and expected outcomes are forbidden ordinary inputs. Optional expected base/head values are identity guards, not source-selection answers.

The first proof stage is an ordinary-input experimental driver. It must show how evidence was discovered, not just generate the curated selection JSON automatically and keep its old proof label. Normal product delivery is a separate, explicitly named adoption stage under native Workspace/report owners. Neither a passing trial nor an all-unknown result completes the agreed maintainer-facing product milestone. Broader change meaning, artifacts/environments, CI/runtime state, actual dispatch and maintainer authority remain independently owned.

The real input varies in dependency version, target code, imports/aliases, module layout, re-exports, class/protocol shape and missing evidence. Source-link rules use Python syntax and existing provider/association contracts, never package names or known case paths. This remains a mechanical source-evidence responsibility; it does not replace the parent's general natural-language change interpretation with handcrafted release-note rules.

## 2. Current facts and selected reuse

| Responsibility | Reuse / integration consequence |
| --- | --- |
| Initial PR observation, complete changed-file validation and native transition | [acquire_dependency_inputs](../../../src/upgradepilot/investigation_inputs.py); retain its initial description and source contexts. Do not independently refetch/re-evaluate the prefix in another pipeline |
| Ordinary experimental composition | [acquire_public_pr_context](../../../experiments/api_target_context_smoke.py); refactor the prefix to shared acquisition or accept the already acquired native input explicitly. Preserve existing consumers/versioned records; do not run two investigations |
| Exact inventory and target files | [TargetContextAcquirer](../../../experiments/api_target_context.py); preserve declared source formats, exclusions, truncation and per-file problems |
| Import/reference associations | [api_python_bindings](../../../experiments/api_python_bindings.py); preserve established/conditional/unknown/unbound meanings and exact traces |
| Exact-release association, tag/tree and module inspection | [api_adapter_exploration](../../../experiments/api_adapter_exploration.py) and [api_change_source_acquisition](../../../experiments/api_change_source_acquisition.py); expose/reuse cohesive exact-release/module examination at that owner rather than copy its private implementation into a second resolver |
| Source observation versus release meaning | Keep declared release-window material separately available; it is not Python callable source and cannot name the answer for this checker |
| Argument/signature facts and binding | [api_call_signature](../../../experiments/api_call_signature.py); reuse the tested core unchanged until a demonstrated new requirement or defect justifies another method version |
| Saved fact integrity, offline view and source text | Reuse the [trial consumer](../../../experiments/api_call_signature_trial.py) and existing [source catalog](../../../src/upgradepilot/workspace/source_access.py), with an explicit ordinary-proof envelope rather than changing historical curated meaning |
| Product publication/consumer authority | [ADR0011](../../../docs/architecture/ADR-0011-explicit-source-association-bases-and-proposal-boundary.md), [ADR0012](../../../docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md), [ADR0013](../../../docs/architecture/ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md); product imports no experiments |

No CI success is a prerequisite for source examination. No model call, installer, target import, constructor execution or runtime reflection is selected. The stronger product upstream resolver retains its own contract. Missing, conflicted, inaccessible and unsupported publisher evidence cannot be flattened into weaker-source success.

## 3. Proposed ordinary source path

```text
repository + PR number (+ optional expected identity guards)
→ shared initial observation / native dependency analysis once
→ exact target inventory + bounded file/declaration observations
→ source-discovery needs from observed imports/calls and the changed dependency
→ qualified exact old/proposed package source; labelled adapter samples when needed
→ bounded intra-repository module / declaration / protocol candidate paths
→ retained source facts + explicit correspondence / receiver premises
→ existing checker for supported candidate comparisons
→ saved discovery, comparisons, coverage/problems and material source closure
→ ordinary experimental view and offline source inspection
```

After ordinary-source proof and explicit product adoption, admitted native inputs/results go into the canonical Workspace and direct report projection. The experimental bundle is not installed as a second canonical state owner or passed off as a Workspace checkpoint.

### One acquisition and observation horizon

Reuse AcquiredDependencyInputs identity/description/transition/source contexts. File reads remain pinned to that captured head; later PR drift cannot silently rebase them. New current acquisition is separately labelled from retained or controlled-provider evidence. If an expected base/head no longer matches, stop that target attempt and preserve the discrepancy; do not restore a desired historical result by injecting old source.

Shared exact-release/tag/tree/file caches belong to one run and preserve input identities. They avoid duplicate requests/registry observation drift, not establish persistent resolution or independent corroboration. Existing CI/runtime owners run only if separately selected; a structural trial must not accidentally invoke a model-bearing full product investigation as a baseline.

## 4. Source requests and version basis

The changed package's old/proposed versions come from the native transition. Request exact-release association/tag/inventory through existing owners for each needed role. A declared release window does not supply the old Python source automatically. Preserve a missing side, tag ambiguity or source conflict; do not infer an API removal from an unavailable old definition.

Adapter/framework exploration stays distinct: constraints/extras/markers are declarations; latest-stable satisfying samples are samples, not installed versions or exhaustive ranges. Never select a historical old/fixed framework merely because it produced a known HTTPX result. A normally discovered newer caller may not contain the old forwarding concern; that does not prove the actual target used it or eliminate other viable versions.

A source-discovery need contains the actual target/reference, observed origin alternatives and trace, package/declaration basis, requested source question and permitted examination scope. Conditional possible origins may justify explicitly labelled exploratory reads, not a positive lexical_import. Keep the existing positive-only explorer contract intact; expose a separately admitted conditional examination request at the source owner. Do not fabricate an established ReferenceFact to bypass the current guard.

Reuse flat/src module grammar, exact inventory and generic path reconstruction. An internal module in an already qualified repository can be examined through observed import syntax; `_pytest` is not guessed as a new PyPI distribution because it is reached inside the selected source repository. External distribution/module mapping still needs its own declaration/association basis. Ambiguous layouts, truncated inventories, local namespace collisions and absent metadata remain specific problems rather than a convenient path choice.

## 5. Correspondence is a source candidate, not runtime dispatch

The new owner is a bounded source-correspondence operation above acquisition and below the checker. It consumes immutable source units plus existing imported-origin evidence, produces evidence-linked candidates and omissions, and never edits the origin owner's conclusions. Use a small typed path of observed source steps; no universal graph engine, SAT system or second general variable-flow interpreter is needed.

The [explicit comparison with uv_reachability](UV_REACHABILITY_COMPARISON.md) supplies reuse/separation rationale. Reuse exact-identity joins, conditional diagnostics, state-aware bounded traversal, coverage-qualified negatives, shared structural admission and separate consumers. Keep UV types, selectors/markers, numeric limits and one-witness/one-diagnostic policies at their dependency owner; no private helper import or generic graph extraction is justified. A dependency path cannot supply a Python callable edge, and source discovery does not require positive UV/CI evidence.

Each candidate binds call/signature IDs, package/source roles, discovery family, exact source-step references, receiver mode and residual premises. A source step identifies the observed import, re-export, definition, base or protocol expression, its source/span and what remains conditional. The checker continues to report local rejected/bound/undetermined under those premises. Candidate generation is not applicability evaluation.

Keep source-candidate association, local comparison and discovery coverage separately inspectable. Premises stay attached to their path; alternatives are not merged into an asserted conjunction. Traversal/memoization must preserve material source/version/definition, binding context, operation/receiver and premise differences. Finding one candidate does not discharge old/proposed or meaningful-alternative obligations. Deterministic ordering/deduplication is not likelihood or applicability ranking. Useful candidates may survive partial discovery, while capped/unavailable/unsupported/unexamined work stays explicit; zero candidates then cannot mean no exposure. A bounded no-candidate statement applies only to the named examined supported domain.

When following calls inside a selected initializer/function, retain exact lexical containment and the condition that execution reaches that body/branch. A call nested in a different function, lambda or callback is not automatically executed by the enclosing call. Do not promote every same-library reference into target exposure merely because its file was acquired.

### Supported path families proposed for staged implementation

| Family | Source evidence / permitted candidate | Conditions and stopping |
| --- | --- | --- |
| Imported functions and re-exports | Follow observed absolute/relative module imports and aliases to complete declared function source | Bound traversal; cycles/ambiguous paths remain visible. A unique declared function is not actual runtime binding |
| Class calls and initializer relationships | Link a named declared class to its own initializer; inspect enclosing class/base evidence for parent-initialization calls | Explicit class-call→initializer/receiver premises; no metaclass/__new__/MRO solution. Multiple possible bases stay alternatives |
| Variadic protocol/factory candidates | From a captured module-level class-allocation expression and attribute-accessor return of a declared class, examine that class's __call__ | Conditional attribute-resolution/return-branch/receiver premises; no object execution, inferred activation or general heap/type solver |

The third family addresses the real pytest mark source pattern. It is a generic bounded Python source pattern, not a pytest/parametrize lookup. It requires source evidence for each allocation/getter/return/protocol step. Unsupported return expressions, branches, mutation or multiple candidates cannot be silently collapsed. This family can be a separate coherent Build increment; omitting it must remain a named loss for ordinary reachability of the demonstrated pytest interaction.

For repeated definitions, retain every identity/span and decorator context. A source-selection policy may examine the last unconditional declared definition while keeping overwritten/decorated alternatives and later writes as limitations; it must not call that choice effective runtime binding. Do not discard a real pass/ellipsis body merely because it resembles a typing stub. Do not use name-only first-match lookup. Overload annotations/decorators neither execute nor independently select the callable; declared-signature comparison stays conditional.

For star imports or dynamic exports, source inspection may identify an explicitly conditional candidate path. It cannot claim export visibility or actual import membership without evidence. Arbitrary scanning for a convenient same-named function across repositories is not a correspondence rule.

### Concrete source-only proof targets

- HTTPX case: observed target import/call → captured framework re-export → selected adapter class/base → exact old/proposed changed-package initializer candidate. Wrapper versions remain sampled if not established. Discovery is not allowed to inject the retained older Starlette source to manufacture app rejection.
- glyphsLib case: observed pytest usage → acquired package re-exports → exact old/proposed raises declarations; and, for the protocol family, acquired MARK_GEN allocation/getter/returned-class/__call__ source. Conditions stay explicit. ids reception is not semantic validity.
- If an admitted path cannot be discovered within source/association/budget limits, preserve the last justified step, unexamined material and needed premise. Do not count an all-unavailable output as completion of the selected ordinary-exposure capability.

## 6. Retention and ordinary consumer contract

Use an explicit version2 experiment envelope for ordinary discovery, while retaining version1 curated comparison opening unchanged. A candidate discovered by the driver is not emitted with the curated proof class. Share source-fact/span/comparison decoding and display through one responsibility-owned helper if needed; do not copy the full reader or add a generic serialization framework.

The ordinary envelope records exact initial observation/target/transition, available method/config/code identities, actual acquisition receipts and role selection, source-discovery requests/results/problems, candidate path/premises, core comparison records, coverage/omissions and procedural attempt disposition. Proof class distinguishes controlled normal-entry composition, retained component replay, fresh ordinary experimental acquisition and product execution. Expected review outcomes never enter this envelope's producer inputs.

Retain the minimum material closure: complete selected source files, declarations/association/tag evidence needed to explain roles, candidate traces, failed/refused/omitted requests and comparison basis. Reuse the catalog codec for text with explicit selected-source coverage; do not claim all acquired target text is retained. A hash-only legacy manifest cannot satisfy new offline inspection. No universal HTTP archive, hidden reasoning, credentials or full unrelated catalog is required.

Source collection and analysis have separate retained boundaries. Freeze actual acquired source identities before checker execution within the new attempt; source acquisition itself cannot be pre-frozen as if the future response were known. Reanalysis is an explicit successor attempt, never offline-open behavior. Interrupted/unknown-completion requests remain distinct from unattempted or completed observations.

Opening checks fixed formats, target/material/source references and integrity and renders saved data only: no provider/model/AST/checker/correspondence/synthesis reruns. Keep old curated bundles readable with their historical proof class. Missing method/codec/source text has an explicit supported inspection/refusal state, not fallback acquisition. Host storage remains private; publish reviewed facts/receipts rather than raw API/model content.

The ordinary view must explain what changed or stayed compatible at the declared boundary, where a candidate connects to target source, which evidence supports that candidate, remaining version/namespace/dispatch premises, and a justified next observation. It must show incomplete discovery coverage and independently keep the checker's local status separate from actual target applicability and action permission.

Render or link to retained source-step paths, exact path-local blockers and omissions. Test producer→saved→human-view completeness for these fields, not only parity between two consumers of one mapping. The UV comparison demonstrates an existing CI report omission despite retained native diagnostics; do not reproduce it in the API consumer or silently widen this design into a UV/report repair.

## 7. Bounds and work allocation — reconciled October30

This section replaces the initial unimplemented8-step/32-candidate/80-GET proposals
with the qualified experimental contract. It is a dated design reconciliation, not
new policy implementation or a retroactive claim about earlier attempts. See the
[staged qualification](../2026-10-30-staged-source-acquisition-policy/REVIEW.md) and
[pre-live contract](../2026-10-30-first-fresh-ordinary-pr-contract/CONTRACT.md).

| Earlier design value | Qualified implementation / selected contract | Why the earlier proposal is superseded or retained |
| --- | --- | --- |
| Proposed8 literal source steps per path |32 literal steps; separate8 resolver-depth identities |These are distinct units. Qualified saved protocol paths have11 steps (prior multi-package control) and10 (staged control).8 literal steps would reject those witnesses. Keep separate depth/path/state controls rather than reinterpret8 as32 |
| Proposed32 emitted candidates below checker256 |One existing AnalysisLimits.max_pairs ceiling256 bounds emitted candidates AND comparisons |No separate32 cap was implemented. Preserve material old/proposed/overload/receiver/path alternatives under the qualified shared bound; retained real discovery has68 comparisons (not68 independent cases). Exhaustion emits comparison_candidate_limit and preserves partial evidence, never coverage closure |
| Proposed80 aggregate provider GETs |Default/selected50 GitHub and100 all-provider attempts, independently counted |Separate GitHub work from PyPI; the controlled improvement fits41 GitHub/46 total, so no evidence requires raising the default. Explicit80 GitHub is only a tested finite configuration, not an active aggregate cap or automatic live selection |
| Proposed32MiB aggregate decoded body |32MiB aggregate, plus8MiB per HTTP response and stricter provider caps |Retained and enforced by opt-in staged transport before provider JSON decoding; response bytes differ from admitted source-text bytes |
| Proposed180s acquisition deadline |180s cooperative monotonic checks with remaining-time socket timeout bounds |Retained with explicit mechanism/proof limits; not hard preemptive elapsed cancellation. Separate existing60s/512MiB analysis worker |
| Anonymous-only initial design |Anonymous default; explicit token-env only when selected under existing public-read authorization |No ambient credential inheritance. The selected contract records prior authorization, auth mode and process-local credential handling without retaining values |

Unchanged source/analysis boundaries:4 exact Python release/sample identities,
2 external dependency hops,12 module questions,2MiB admitted library text;
target ceiling200 Python files/2MiB; binding32 origins/128 trace steps; retained
analysis32 files/4MiB,100,000 nodes/file,250,000 aggregate nodes,4096 facts,
256 pairs; correspondence4096 resolution states and256 diagnostic records plus
omitted count. Crossed-release metadata up to10 remains separate. A state count
may record the over-limit refusal check; it is not additional admitted work.

Staged policy selects16 total target file attempts,2 adapter candidate attempts and
protects24 GitHub requests from early target/window stages. These are additional
allocation choices beneath the unchanged capability ceilings, not equivalent units
or promises of complete coverage. Cache reuse stays per-run. Inventory-first
priority uses declarations/PR-observed changed paths; closure priority uses observed
names/source references and preserves omissions. No known answer paths or versions.

Any candidate/path/depth/state/source/provider/time limit preserves explicit gaps,
omissions or an incomplete/failed attempt. Valid retained comparisons may remain
locally useful; exhausted candidates cannot establish all affected paths examined.
No automatic cap enlargement, successful-subset regrade or quiet omission is allowed.

No fresh target request is activated by this design. The separately frozen contract
selects one attempt, exact identity guards, auth/policy/source/analysis bounds,
private retention and useful/partial/refusal/stop criteria. It requires an honest
fresh proof class and an outer acquisition-attempt record before any provider call.
Stop for Ali's inspection before live execution; earlier frozen captures remain
unchanged. Native adoption and runtime/semantic/maintainer authority stay separate.

## 8. Implementation and evidence sequence

1. **Shared prefix and acquisition contract:** prove one initial observation/native dependency evaluation; preserve description/identity and existing target/explorer failures. Expose reusable exact-release/module examination and caching at the existing owner, including explicit conditional-discovery basis. No hidden positive-origin coercion.
2. **Direct/re-export and initializer candidate closure:** add source-derived paths and unknowns, run the unchanged checker, save/open version2 ordinary evidence with full material closure. Use controlled PR/provider inputs without target path/pair answers. Prove failure and coverage behavior as well as useful relations.
3. **Protocol/factory closure:** add the generic limited source pattern needed by pytest mark candidates; qualify new forms and limits through renamed sources and real source-path evidence. This is a distinct proof-bearing increment, not permission to silently call the first slice complete for the broader ordinary target responsibility.
4. **Bounded ordinary experimental run:** after controlled composition and request allocation pass, select/freeze a fresh acquisition contract. Start with repository/PR identity only; keep current and retained captures separate. Observe at least useful structural evidence and specific unresolved/discovery boundaries; a procedural success/all-unknown output is insufficient.
5. **Native/product adoption:** after useful ordinary evidence and the Workspace scope decision, move admitted source/discovery/checker responsibilities into product owners, add explicit native codec/material closure and direct consumer projection, and prove normal CLI/report/saved compatibility. No runtime import of experiments or new parallel legacy truth fields.

Relevant proof classes: correct normal input and identity drift; alias/rebinding/conditional origins; relative/star re-exports; repeated/decorated definitions; exact old/proposed identities versus samples; direct/initializer/protocol candidates; conflicting/missing sources; multiple return/base alternatives and bounded cycles; budget starvation/unexamined work; immutable attempt/cold reopening/unsupported historical formats; terminal-safe text; unchanged action/strong-source/CI/runtime owners. Retain old curated controls and both real results. Protected semantic admission and independent report usefulness stay at their existing owners.

## 9. Workspace/product delivery and decision status

The recommendation is an ordinary experimental proof followed by explicit minimal native adoption, with a stop/reassessment gate if useful source reachability fails. Full Workspace migration first is not shown necessary. It is also unacceptable to label the trial a normal product feature or defer consumer migration indefinitely.

Product adoption requires native owner/type/version/material-input references, complete recoverable source/correspondence/checker closure, direct historical Workspace projection, compatible old saved reports, actual normal CLI proof and explicit unsupported role/codec states. Reports remain views, recovery remains separate from continuation/replay, and synthesis alone owns action permission. Existing producer/result fields may not become a new parallel API state store.

This design recommends source-path families, retention shape, staged sequencing and trial bounds for discussion. It changes no accepted specification/ADR and does not admit a broader semantic model role. Exact native family/layout and report-version choices belong to the separately selected adoption contract; they must be settled before product Build. The pending Workspace discussion is recorded separately, rather than hidden inside experiment implementation.
