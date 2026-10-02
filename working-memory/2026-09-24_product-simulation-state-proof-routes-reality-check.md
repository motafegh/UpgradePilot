# Product Simulation — state-proof routes / where-when-use reality check

**Date:** 2026-09-24  
**Session status:** PAUSED AT OWNERSHIP CHECK  
**Primary operation:** independent, read-only-against-targets research and cross-case synthesis; no product implementation or main mutation.

**Previous research continuity:** [Product Simulation rebase and S013–S016 progress](2026-09-22_product-simulation-rebase-G1-G2-progress.md).  
**Main snapshot read:** `main@b27f0c8fc8e2e04746f715d779c0fa55d9878c03`, specifically `MEMORY.md`, `working-memory/2026-09-24_effective-package-manager-semantics-system-design.md`, and `working-memory/2026-09-24_r2_state-witness-scope-checkpoint.md`. This snapshot is not merged into the research branch by this session; refresh live owners before later transfer.

## Question and route correction

Initial intended research was to find a real update where a changed requirement was present in a consumed source but excluded by environment marker or uv scope. Before expanding the corpus, inspecting this branch's current research working memory showed that S015 already covers a real marker-scoped Dependabot pytest update and S016 already covers a real uv selector/extras-scoped Dependabot coverage update. Do **not** create S017 merely to reproduce those boundaries.

A supplemental `fastavro/fastavro#867` manually authored marker example was screened. Its added `backports.zstd ; python_version<'3.14'` is conditional while the exact-head matrix includes Python 3.14 and earlier versions; the relevant Python 3.14 job has success metadata, but job logs are HTTP 410 and no direct installer-state claim is allowed. It is a weaker mechanism control than S015, because it is not a Dependabot exact-version bump. Do not promote it into a numbered scenario.

The genuinely new session question became whether the current main candidate's two proof routes and added where/when/use relationships are empirically supported and whether a later inventory would add decision-relevant information or duplicate an already sufficient command-completion witness.

## Completed work

Created [cross-case reality check](../product-simulation/2026-09-24_STATE_PROOF_ROUTES_WHERE_WHEN_AND_EXERCISE_CROSS_CASE.md), comparing retained S013–S016 against the latest main's candidate **Command-Derived Requirement-State Proof** and **Direct Target-Owned Package-State Observation**.

Key distinction: requirement satisfaction in environment E at command C completion, package presence in E at observation time T, later command X use of that package, and successful exercise of changed behavior are four different propositions. A command-time witness needs no automatic redundant later inventory for its own proposition. Claims crossing time/environment/use boundaries need only the additional positively proven links material to that new proposition; an unresolved link remains unresolved.

Cross-case observations: S014 already-satisfied pip state need not be re-proven by later inventory; S016 shows selector-scoped environment identity; S013 illustrates earlier sync versus later no-sync test execution; S015 prevents borrowing successful CI between marker-different matrix rows. These cases support keeping state truth distinct from operation provenance and from later exercise, without selecting a generic temporal resolver.

No new numbered scenario was admitted, no target repositories/CI were mutated, no main files or product code/tests/specs/plans were changed. The cross-case artifact is research, not acceptance of main's candidate architecture.

## Learning-by-Doing slice state

A — DONE: oriented from new main owners; explained why marker/selection and what-where-when matter.  
B — DONE: real fastavro screening, retained-case deduplication, source-backed cross-case proof-route comparison.  
C — DONE: new research artifact and this dated handoff record.  
D — PENDING: brief owner check with Ali: distinguish command-completion state from later actual package use.  
E — PENDING: after that check, select a genuinely unaddressed real evidence relationship rather than another marker/selector scenario.

## Bounded next research route as of this session

1. Refresh main and this branch before acting; main has advanced beyond the last branch merge.
2. Prefer an untouched public dependency-update case where the exact changed-dependency consumer installs into a retargeted location and later operation's environment/use relation is observable. Existing retargeting controls only establish unrelated tooling installs, so this would add information.
3. In parallel keep exact wheel-tag witness bridge and uv resolution-marker-order limitation as open families, but do not force admission from mismatched revisions or unverified semantics.
4. Do not conflate the user's independent Product Simulation scope with the current main phase; the main proof design sharpens research, not restricts it.
