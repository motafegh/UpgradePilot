# Learning-discovered acquisition and binding refinements — planning preservation

**Recorded:** 2026-10-04, Asia/Tehran.

**Operation:** Learning-Only discussion followed by expressly authorized Planning/Design preservation; executable Build remains paused.

**Source baseline:** `main` at `2cd2c264`; local/remote alignment checked before this documentation increment.

**Planning owner:** [API change and target exposure feasibility plan](../plans/UPSTREAM_API_CHANGE_AND_TARGET_EXPOSURE_FEASIBILITY_PLAN.md).

**Related evidence:** [closed acquisition cycle](2026-10-04_target-context-and-adapter-discovery_lbd-cycle.md), [declared-source acquisition cycle](2026-10-04_declared-source-window-acquisition_lbd-cycle.md), [distinct acquisition attempts](evidence/2026-10-04-target-context-adapter-discovery/README.md).

## Request, method and preservation boundary

Ali resumed learning about the recent acquisition implementation, then asked to place discoveries and future modifications in their proper planning owners so that returning to Build would consider them alongside existing work. This authorizes the plan and directly necessary continuity records, not implementation.

Apply a proportionate adaptation rather than opening a second full teaching cycle for recording already discussed findings: ongoing Learning-Only discussion → normal substantive Planning LbD cycle → duplicating orientation/approval would interrupt the expressly requested preservation → compress the documentation admission into this record and the existing plan/live owner. Scope is documentation only; no technical proof or learner mastery is inferred. Reconcile `MEMORY.md` because its learning-deferral and immediate interpretation handoff had become stale. Preserve the closed acquisition cycle as historical; do not reopen or rewrite its proof.

Provenance: `UP-SKILL:upgradepilot-planning-design`; `UP-SKILL:upgradepilot-working-memory`. Existing ADR-0011 and Minimum Useful Generality govern the retained evidence, authority and variation boundaries. No new specification, ADR, plan family or graph dependency is admitted by this refinement.

## Learning covered and ownership actually demonstrated

The discussion connected ordinary PR identity to independent upstream-source and exact-target acquisition, then conditional adapter exploration. It covered crossed-release windows, declaration-based association versus publisher evidence, pinned text/hash identity, inventory/truncation limits, AST imports/references and conservative binding uncertainty. CFG (possible control-flow paths) and DFG (value producer/consumer relationships) were introduced as concepts relevant to improving static analysis, not as implemented UpgradePilot graphs.

Ali's reasoning demonstrated these bounded distinctions:

- Upstream and target acquisition are related but independent evidence branches; failure of one does not erase useful scoped facts from the other.
- Missing evidence for a crossed release leaves the relevant conclusions unresolved rather than supplying an invented account of that release.
- Failure to find `TestClient` in examined files of a truncated inventory proves neither presence nor absence in the unexamined part.

Alias questions exposed the next distinction: rebinding is a new binding, not automatically an unbound name; the new value may itself originate from the imported object, and a later assignment may restore that origin. Those possibilities motivated future precision work. Independent code/test ownership, a control-flow/data-flow solver and complete Python semantics were not assessed. Approval of a plan is not mastery.

Remaining learning includes declaration constraints/extras/markers and import-to-distribution candidates; adapter sample/version selection, caches and budgets; failure categories; and end-to-end proof. Detailed source-trace and scope-analysis ownership remain to be developed. This is a dated learning snapshot; live continuation belongs only in `MEMORY.md`.

## Findings grounded in the inspected implementation

### Partial release evidence can be discarded inside an otherwise preserved result

`experiments/api_change_source_acquisition.py::select_release_sections` returns an `AcquisitionProblem` on a missing/duplicate required section. The acquired file and already recovered sections are not included in that result. `DeclaredReleaseWindowAcquirer` propagates the problem. The upstream problem projection in `experiments/api_target_context_smoke.py` retains stage/reason/detail, not the usable partial source/section evidence.

This is narrower than the transport/budget partial-result repair already verified in the closed acquisition cycle. Independent target/adapter results can survive while usable evidence inside the incomplete upstream window is lost. Existing rejection tests do not establish preservation of that partial evidence. The future increment must separate retention from complete-window admission; it must not weaken the missing-section guard.

### Whole-file blocking loses ordered and scoped associations

`experiments/api_target_context.py::extract_python_facts` walks the AST, blocks names on stores/deletions, parameters and other binding constructs, and admits only unique unblocked top-level imports. Thus a later rebind can suppress an earlier valid reference, and an unrelated function parameter can suppress a module reference of the same spelling. Assignment aliases and restoration are not tracked.

Read-only synthetic probes during the preceding learning discussion illustrated the limitation: alias copy back to `C`, a call before and after `C` is reassigned, saved-alias restoration, and a module call alongside an unrelated function parameter all lose the otherwise recoverable association. These are development diagnostics, not committed regression tests, normal-path acceptance or runtime observations. Source inspection was refreshed for this planning increment; the live acquisition and prior test suites were not rerun.

An important consumer constraint is that adapter candidate admission uses associated reference origins; `ReferenceFact` records are also serialized and decoded by adapter replay. Improving producer precision therefore needs producer → manifest/replay → adapter-consumer proof, not merely an internal AST test. Possible origins cannot be promoted to established relations by those consumers.

The local Sentinel comparison was conceptual and read-only: its extractor contains control-flow edges and scoped IR definition/use edges. No completeness audit, code adoption or equivalence to Python analysis was established. General data-flow reasoning is reusable; its implementation is not automatically the method for UpgradePilot.

## Accepted planning refinement and return-to-Build handoff

The existing feasibility plan now owns the detailed scope, construct/design entry, sequence, consumer responsibilities and discriminating proof:

1. Preserve bounded partial release-window evidence with source identity and coverage/problem attribution, keeping complete admission separate.
2. Improve ordered/scoped bindings, alias copying, rebinding and restoration, with branch alternatives and precise unknown/unbound states. Freeze exact construct and result contracts before implementation; unsupported dynamic/interprocedural/loop behavior remains explicit.
3. Continue the already planned bounded API-change interpretation and conditional-proposal work. Independent source-only contract/case preparation need not wait for unrelated advanced analysis.

The initial binding method is structured AST state propagation. Explicit CFG/fixed-point or interprocedural analysis is conditional on real decision-critical cases and proportional proof; a DFG may project the same evidence. This avoids treating one synthetic alias example as the entire product horizon while keeping dynamic Python and runtime identity honestly outside this first proof.

The plan also requires partial-evidence manifest/recovery checks, positive-versus-uncertain consumer checks, varied binding/scope controls and relevant real target evidence before broader claims. Installed versions, activation, execution, model semantic quality, independent usefulness and product adoption remain separate obligations. The refinements are planned, not implemented or proven.

## Documentation verification and closure

Reviewed the plan/live-owner/dated-record diff; checked authored local Markdown links, whitespace and the exact publication scope. This increment changes no product, experiment or test code. No executable tests or live/model runs are required for these planning-only changes; the previous 41 focused trial tests and preceding 743 product tests remain historical evidence, not fresh validation of either refinement.

At this record's handoff, the documentation preservation responsibility is complete and learning remains active. Implementation awaits the explicit return to Build with the plan's design/proof entry. The unrelated untracked broad-audit cycle record was preserved outside this increment.
