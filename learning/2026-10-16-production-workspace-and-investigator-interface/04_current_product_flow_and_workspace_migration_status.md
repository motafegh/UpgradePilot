# Current product flow and Workspace migration status

**Educational snapshot:** repository horizon **`5187f40ba974341eb29d765363f093922a881803`**, 2026-10-16. Product `src/` and `tests/` at this horizon preserve the verified production Workspace implementation while later records/plans prepare—without starting—the next Investigator adapter responsibility.

**Responsibility:** understand what UpgradePilot actually does today end to end, which part of the canonical Workspace migration is already real, why the legacy `PublicPullRequestInvestigation` path still exists, and what remains future work.

## Core mental model: the product is intentionally transitional

The most accurate current architecture is **not**:

```text
legacy investigation only
```

and it is also **not**:

```text
all consumers are Workspace-native now
```

It is:

```text
public PR/providers
        ↓
existing domain/native owners
        ↓
NativeInvestigationCapture
        ↓
canonical Workspace revision + lifecycle host
        ↓
workspace_revision exposed on the investigation result

AND, during migration:

same normal orchestration
        ↓
PublicPullRequestInvestigation legacy compatibility result
        ↓
maintainer-action synthesis
        ↓
report projection
        ↓
CLI render/save
```

So UpgradePilot already has a canonical evolving Workspace for the admitted implemented scope, while several user-facing/product consumers still depend on the older typed final-result surface.

That coexistence is migration state, not architectural confusion.

## 1. The normal application now produces Workspace state during the real investigation

Open [`investigation.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/investigation.py).

The normal application still begins from the real public-PR/provider/domain sequence. It now uses the shared dependency/CI preparation path and starts a `NativeInvestigationCapture` plus an `InvestigationWorkspaceHost`.

The top-level shape is:

```text
exact PR / changed files
→ dependency owner
→ shared CI preparation / native owners
→ package/upstream/impact owners
→ conditional target read through generic host
→ native reassessment when needed
→ completed native capture
→ final Workspace publication
→ procedural termination record
```

The function returns:

```python
PublicPullRequestInvestigation(...,
    workspace_revision=workspace_host.current,
    ...legacy fields...
)
```

This is a central migration fact:

> **The Workspace is no longer only research or a disconnected prototype. It is produced by the normal application path.**

But the legacy result fields are still populated because downstream consumers have not all been cut over yet.

## 2. `workspace_revision` is canonical state, not a resumable legacy report

The `investigate_public_pull_request(...)` docstring explicitly says the immutable Workspace revision is the canonical boundary during migration.

That does not make `PublicPullRequestInvestigation` itself the canonical recovery owner.

Keep the roles separate:

```text
Workspace revision
→ canonical evolving native/lifecycle state for admitted support

PublicPullRequestInvestigation
→ transitional typed result still consumed by existing synthesis/report code
```

The result's `workspace_revision` field is therefore a bridge/exposure point during migration, not evidence that every legacy field is already reconstructed from Workspace or that the result is the user-facing recovery contract.

## 3. Why the legacy result cannot simply be deleted today

`PublicPullRequestInvestigation` still contains evidence/results used by downstream code, including families not yet completely migrated into direct Workspace consumer projections.

The migration plan therefore requires accounting for every admitted legacy field/material producer before default cutover.

Deleting the result simply because the Workspace exists would risk this pattern:

```text
new canonical state exists for some families
        ↓
old result removed immediately
        ↓
consumer silently loses unsupported/unmigrated facts
```

That would be **fake migration**: the type changed, but product meaning regressed.

Correct migration instead requires:

```text
complete admitted family/input retention
→ supported Workspace-native projections
→ direct consumer parity/proof
→ cut consumer over
→ remove obsolete bridge only after its purpose ends
```

## 4. Maintainer synthesis is still explicitly legacy-result based

Open [`maintainer_action.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/maintainer_action.py).

Current synthesis is:

```python
synthesize_maintainer_action(
    investigation: PublicPullRequestInvestigation,
)
```

and it actively type-checks that input.

Current action authority is also intentionally narrow:

```text
MaintainerAction = "abstain"
```

The evaluator preserves material uncertainty from the investigation but does not infer a positive action from technical evidence merely because some evidence looks favorable.

This means two independent migration facts remain true:

```text
synthesis input type is still legacy
```

and:

```text
positive maintainer-action permission is still not established
```

Workspace migration must preserve the synthesis specification and action boundary; changing the state container cannot silently strengthen action permission.

## 5. Report projection still consumes the legacy investigation and invokes synthesis

Open [`report_projection.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/report_projection.py).

Its entry point is still:

```python
project_investigation_report(
    result: PublicPullRequestInvestigation,
    ...
)
```

It copies available owned facts into the report contract and then calls:

```python
synthesize_maintainer_action(result)
```

The projection explicitly does not reacquire evidence or rerun domain interpretation.

But it is still a projection **from the legacy final investigation object**, not directly from recovered canonical Workspace records.

This is exactly the consumer boundary targeted by the later migration stage.

## 6. The current CLI remains investigation → legacy report projection → render/save

Open [`cli.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/cli.py).

The normal path is:

```text
investigate_public_pull_request(...)
        ↓
project_investigation_report(investigation)
        ↓
render_investigation_report(...)
        ↓
optional save_report(...)
```

`--open-report` is a separate offline saved-report path:

```text
read_report(path)
→ render saved InvestigationReport
```

It does not open a Workspace checkpoint, recover canonical investigation state, continue an investigation or reacquire evidence.

Therefore:

```text
--open-report
!= Workspace recovery
!= continuation
```

A saved report remains a durable presentation artifact, not the canonical investigation checkpoint.

## 7. What Stages 1–3 have actually delivered

The [Workspace implementation/migration plan](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/plans/INVESTIGATION_WORKSPACE_IMPLEMENTATION_AND_MIGRATION_PLAN.md) organizes six technical responsibilities.

The first three have production implementation/proof at the admitted scope.

### Stage 1 — native capture and cold reconstruction

Implemented:

```text
explicit native owner/family/version contracts
exact material/input capture
partial not_evaluated states
supported native reconstruction in a fresh process
explicit unsupported/missing/wrong-target/resource refusals
```

Initial support is bounded, especially around the admitted CI/runtime and Python-support closure; it is not every native family in the product.

### Stage 2 — immutable Workspace revisions and durable checkpoints

Implemented:

```text
immutable revision/predecessor lineage
SQLite checkpoint publication
expected-predecessor conflict
retained-history validation
unconfirmed acknowledgement
storage refusals
validated backup
cold durable reconstruction
```

This is canonical persistence infrastructure, not semantic reevaluation or user continuation.

### Stage 3 — lifecycle host, admission and current material validity

Implemented:

```text
typed purpose/request/admission lifecycle
intent before external interaction
observation/interruption truth
native-owner reassessment
original basis preservation
current material-validity checking
current execution authority
views/proposals/use/termination history
cold historical restoration with no live authority
```

The real Python-support selected-read/reassessment path is the first normal production caller/proof case of the generic host.

## 8. What remains in Stage 4 — complete admitted native-family coverage

The first production Workspace implementation deliberately proved a bounded native closure before expanding to everything.

That means later migration still has to account for product branches such as the remaining package/upstream/artifact/target/report-relevant material where no complete Workspace-native reconstruction/projection contract yet exists.

Stage 4 means:

```text
trace every currently admitted normal product family/input
→ capture enough original material
→ provide supported reconstruction/projection
or explicitly block affected use
```

It does **not** mean converting every internal Python object merely for symmetry.

Expansion is demand/consumer driven: if a required consumer or future Investigator claim needs a missing family, implement the exact proper family/input closure instead of inventing a shortcut.

## 9. What remains in Stage 5 — direct synthesis/report consumer migration

The current synthesis/report code proves why this stage is still real work.

Stage 5 must move from:

```text
Workspace exists
+
legacy PublicPullRequestInvestigation feeds synthesis/report
```

Toward:

```text
Workspace-native supported inputs
→ synthesis owner
→ retained synthesis/result basis
→ report projection/rendering
```

Historical rendering must consume retained historical conclusions rather than secretly rerunning synthesis during recovery.

The migration plan explicitly says the existing `report_projection.py` synthesis call must be refactored at this boundary.

The goal is not a new synthesis policy. The action/report contracts stay owned by their existing specifications.

## 10. What remains in Stage 6 — user-facing recovery, explicit continuation and legacy retirement

The product currently has low-level checkpoint recovery/host restoration proof, but not the final user-facing recovery/continuation experience.

Stage 6 must add explicit supported surfaces for:

```text
offline Workspace inspection/recovery
+
separately invoked validated continuation
```

Continuation must revalidate:

```text
exact target
material premises
supported method/capability
current authorization
```

before fresh work occurs.

Unknown completion remains unknown until deliberately reconciled.

Only after direct consumers and recovery/continuation are covered can obsolete compatibility plumbing be safely retired.

## 11. Why recovery, report opening and continuation must stay distinct

Three operations may all happen "later" but have different authority:

### Saved report opening

```text
open retained presentation artifact
→ no new investigation state
→ no execution
```

### Workspace recovery

```text
open/validate retained canonical state
→ historical native/lifecycle inspection
→ no current execution authority
```

### Explicit continuation

```text
recover historical state
→ validate current target/material/method/authority
→ separately admit new work
```

Collapsing them would create unsafe behavior such as:

```text
opening an old file
→ implicitly runs providers/evaluators again
```

or:

```text
historical admission
→ silently becomes current permission
```

Both are forbidden by the accepted architecture.

## 12. The future Investigator does not require full Stage 4–6 migration first

The common input/source-interface preparation established a bounded product-owned seam for a future Investigator:

```text
canonical host
+
qualified dependency/CI native views
+
frozen raw source catalog
+
delivery/citation/accounting
```

That is enough to test the selected bounded evidence-use mechanism without first completing every report/CLI/native-family migration responsibility.

This is an important sequencing principle:

```text
future Investigator comparison needs exact interface/family claims it consumes
not
"finish all migration before any AI experiment"
```

If the future experiment discovers that one missing native family is decision-critical, that becomes an exact Stage 4 expansion pressure with a named claim and proof requirement.

Full migration is not a generic prerequisite used to postpone the experiment indefinitely.

## 13. But the prepared future adapter cycle is not implemented yet

At this snapshot the [Investigator Integration and Comparative Evaluation Plan](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/plans/INVESTIGATOR_INTEGRATION_AND_COMPARATIVE_EVALUATION_PLAN.md) is an admitted future execution/proof owner.

The first successor record—[`2026-10-16_2045_investigator-adapter-and-mechanical-qualification_lbd-cycle.md`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/working-memory/2026-10-16_2045_investigator-adapter-and-mechanical-qualification_lbd-cycle.md)—is explicitly:

```text
PREPARED — NOT STARTED
```

Every real phase remains pending.

No adapter Build, prompt/tool bridge, model-interface canary, model inference or comparative result exists merely because the plan/record exists.

For this current architecture note, the only important future statement is:

> **the current Workspace/source/native interfaces are now ready to be consumed by a separately activated adapter responsibility; the adapter itself is not part of current implemented product truth.**

Model names/configurations belong to that future experimental protocol and are intentionally not taught here.

## 14. The Oct 9 research package remains the predecessor, not current implementation truth

The frozen [Oct 9 Workspace implementation-architecture research package](../2026-10-09-workspace-implementation-architecture-research/README.md) teaches why immutable revisions, SQLite checkpointing, a typed Investigator seam and direct migration were recommended.

At its horizon it correctly states that those mechanisms are experimental and not adopted production Workspace behavior.

Production has since implemented substantial parts of that direction.

So the relationship is:

```text
Oct 9 package
→ research alternatives, failures, corrections and recommendation

Oct 16 package
→ production implementation, verified current boundaries and migration state
```

Do not rewrite the Oct 9 notes to pretend the research already knew the final production mechanism. Both horizons are useful for different questions.

## 15. Current fact, accepted target and future work — keep them visually separate

### Current implemented fact

```text
normal product publishes canonical Workspace native/lifecycle state
Stages 1–3 implemented at admitted scope
shared source/native consumer interface implemented
legacy PublicPullRequestInvestigation still returned
synthesis/report/CLI still consume legacy result
saved-report opening remains separate
```

### Accepted target architecture

```text
native owners
→ canonical evolving Workspace
→ direct supported Investigator/evaluator/synthesis/report projections
→ coherent historical recovery
→ separately validated continuation
```

### Future/deferred work

```text
remaining native-family coverage
Workspace-native synthesis/report cutover
user-facing Workspace recovery/continuation
legacy retirement
future Investigator adapter/model comparison
replay / broader semantic or adequacy evaluation when separately admitted
```

A learning artifact becomes misleading if it mixes these three horizons into one present-tense diagram.

## 16. Migration correctness is about preserving meaning, not eliminating a class name

The engineering objective is not:

```text
number of references to PublicPullRequestInvestigation = 0
```

The objective is:

```text
all required current product meaning
+ uncertainty
+ provenance
+ historical conclusions
+ consumer behavior
survive through the canonical Workspace path
```

Only then is deleting the compatibility surface meaningful.

This is why the migration plan requires direct consumer parity/proof, relevant full product/report/CLI regressions and installed-package proof before default cutover.

A one-way compatibility projection may temporarily earn a named proof/caller purpose. It must never become a second writable/acquisition truth path.

## 17. Current maintainer-action boundary still matters during migration

The current deterministic synthesis admits only explained abstention.

That may look conservative, but it protects a critical product principle:

```text
technical evidence
!= positive action permission
```

Workspace migration cannot use richer retained state as an excuse to infer:

```text
merge
block
defer
targeted checks
```

without each action's accepted positive prerequisites.

Migration changes **where state lives and how it is recovered**, not the action-authority specification.

## 18. Proof and non-proof of the current transition

The production evidence across the implemented stages establishes:

```text
native capture/cold reconstruction
immutable checkpoint publication/backup
lifecycle host and material-validity integration
normal selected-read/native reassessment through host
common dependency/CI preparation
frozen source/native consumer delivery/citation interface
qualified real HTTPX/glyphsLib input snapshots
```

It does not yet establish:

```text
complete Workspace-native consumer cutover
all native families reconstructed
user-facing Workspace continuation
replay
positive maintainer action
Investigator usefulness/superiority
full semantic/adequacy competence
```

The transition is therefore substantial but deliberately incomplete.

## 19. What to own versus what to look up

### Must master / own

- canonical Workspace state versus legacy compatibility consumer surface;
- why normal orchestration can produce both during migration;
- current synthesis/report/CLI dependency on `PublicPullRequestInvestigation`;
- Stage 1/2/3 completed responsibility versus Stage 4/5/6 remaining responsibility;
- saved report versus Workspace recovery versus explicit continuation;
- why removing legacy before coverage/parity is fake migration;
- future Investigator integration versus migration completeness;
- current fact versus accepted target architecture versus future plan.

### Understand operationally

- `workspace_revision` exposure on the legacy result;
- direct consumer cutover sequence;
- historical synthesis retention versus fresh synthesis;
- family expansion triggered by real consumer claims;
- one-way compatibility bridge/removal condition.

### Lookup level

- every legacy result field;
- report rendering/source-field internals;
- exact future CLI flag names;
- exact future adapter/model protocol settings.

### Deferred deliberately

- Stage 4 implementation details until selected;
- Stage 5 synthesis/report refactor code;
- Stage 6 UX/continuation design;
- future Investigator adapter/model results.

## Fast relearning route

1. Open `investigation.py` and locate `workspace_revision=workspace_host.current` in the returned legacy result.
2. Open `maintainer_action.py` and verify synthesis still type-checks `PublicPullRequestInvestigation`.
3. Open `report_projection.py` and trace its legacy input to `synthesize_maintainer_action(result)`.
4. Open `cli.py` and distinguish normal investigation/report rendering from `--open-report`.
5. Recreate the stage map: **1 capture/reconstruction; 2 durable publication; 3 lifecycle host; 4 full family coverage; 5 direct synthesis/report cutover; 6 recovery/continuation + legacy retirement**.
6. Finish by explaining why the prepared Investigator adapter record is future work even though the product interfaces it will consume already exist.

## Transfer questions

1. If `workspace_revision` is already canonical, why would deleting `PublicPullRequestInvestigation` today still be unsafe?
2. Why does `--open-report` not count as Workspace recovery or continuation?
3. A future Investigator needs only the already qualified dependency/CI native families plus frozen raw sources. Must UpgradePilot finish every Stage 4–6 migration item before testing that mechanism? Why not?
4. What evidence would you require before changing synthesis from a legacy-result input to a direct Workspace-native input?
5. Why must positive maintainer-action permission remain unchanged even if Workspace retention becomes richer and more complete?

## Primary anchors

- [normal application orchestration](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/investigation.py)
- [current maintainer-action synthesis](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/maintainer_action.py)
- [current report projection](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/report_projection.py)
- [current CLI](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/cli.py)
- [Workspace implementation and migration plan](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/plans/INVESTIGATION_WORKSPACE_IMPLEMENTATION_AND_MIGRATION_PLAN.md)
- [future Investigator integration/comparison plan](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/plans/INVESTIGATOR_INTEGRATION_AND_COMPARATIVE_EVALUATION_PLAN.md)
- [prepared, unstarted adapter cycle](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/working-memory/2026-10-16_2045_investigator-adapter-and-mechanical-qualification_lbd-cycle.md)
- [Oct 9 research predecessor](../2026-10-09-workspace-implementation-architecture-research/README.md)

`UP-SKILL:upgradepilot-learning-artifact`
