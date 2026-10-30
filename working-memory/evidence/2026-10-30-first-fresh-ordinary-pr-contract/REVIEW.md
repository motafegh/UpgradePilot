# Pre-live reconciliation — findings and proof

Entry fd836c56; final executable repair horizon96288584. [Cycle](../../2026-10-30_first-fresh-ordinary-pr-attempt_contract-cycle.md), [frozen contract definition](CONTRACT.md), [machine selection](contract.json).

## Independent disposition of the suggested work

| Suggestion | Actual finding / disposition |
| --- | --- |
|Any method2 protocol residue requires the full ordered witness and required premises |CONFIRMED. The consumer only triggered on allocation or factory_return; removing BOTH bypassed checks while getter/call remained. Three corruption subcases fail before/pass after. Trigger now covers all four operations; required ordering and existing minimum three premises stay unchanged |
|Keep valid producer/consumer behavior |An additional inconsistency was exposed: explicit Class.__call__/__getattr__ comparisons already emitted factory-only operation labels without allocation. New direct-declaration control fails after reader hardening, then passes with a small producer metadata fix: ordinary explicit methods use declaration; allocation-backed witnesses keep protocol labels. Same local argument comparisons, no new syntax/receiver inference |
|Reconcile old proposed bounds before execution |CONFIRMED. Original design §7 is explicitly amended:8 literal steps→32 literal steps with separate8 resolver depth;32 proposed candidates→existing shared256;80 aggregate requests→50 GitHub/100 all-provider defaults.32MiB/180s retained with actual cooperative enforcement semantics. This documents qualified implementation, not a policy redesign. Saved witnesses have10/11 steps; actual retained real discovery68 comparisons is not68 cases |
|Freeze fresh proof/attempt/contract |CONFIRMED as an entry gap already found before steering. Existing ordinary code admits only controlled/retained proof classes and has no before-acquisition outer record. Freeze fresh_ordinary_pr_acquisition and fresh-ordinary-pr-attempt/1 definition, exact case/auth/limits/retention/dispositions and implementation prerequisites. These definitions are not implemented/live proof |
|Stop before live |APPLIED. No token read, credential/quota check, provider request, fresh acquisition or private official attempt directory creation. No automatic retry or cap enlargement |

## Focused and broader proof

[Reader before](reader-before.txt): one discriminating test,3 failures because getter+call/getter-only/call-only corruption was admitted. [After](reader-after.txt):11 factory tests pass. [Direct declaration before](direct-declaration-before.txt):2 errors expose producer metadata inconsistency; [after](direct-declaration-after.txt):12 factory tests pass. These are development proof stages; none is silently discarded or presented as an old frozen evaluation result.

[Final API](api-regression.json):230 tests/2.903s pass; [architecture](architecture-regression.json):7/1.116s pass. [Static boundaries](static-boundaries.json) retain131 artifacts/122 Python modules/257 edges/31 legacy private exceptions/96 native files, no violations. No new module/framework/dependency or exception.

[Full regression](full-regression.json):624 tests/36.374s, exact previous1 failure/25 error identities AND terminal messages and11 optional skip identities. Full suite remains RED for old source-blob, planner/LangGraph fixture/result constructor and Workspace removed-alias debt. No skips/regrade/repair of that debt.

[Compatibility](compatibility.json): all11 actual saved curated/method1/method2 bundles open with AST/network/checker/discovery forbidden, including original real HTTPX/pytest and both retained real protocol successors.10 frozen private members and25 previous staged artifacts remain hash-identical. No old source/result/verdict regeneration. The edited integration DESIGN.md is an explicitly amendable proposal document, not a frozen evaluation; old numerical proposals remain recoverable in Git and visibly superseded in its table. Its old verification receipt remains dated evidence, not an assertion that updated documentation is byte-identical.

Only the ordinary reader, source-correspondence operation label and one responsibility-owned test file change executable behavior. Acquisition policy/providers, binder/checker, native src/tests/tools/package/specifications/ADRs have no diff. No new native product test run is claimed.

## Frozen selection and readiness boundary

Select HTTPX PR20 with exact retained base/head guards; use the prior explicitly authorized owner-only public-read token mode, not ambient credentials. Validity/current quota are unknown. Keep qualified50/100,8/32MiB,180s,24 reserved source requests,16 target file/2 sample attempts,4 release/12 question/2MiB library and existing worker/correspondence limits. No source path, adapter version or answer selector enters the ordinary producer.

The contract defines first-observation/partial/refusal/interruption retention before provider work, immutable outer/inner records, fixed offline admission and separate procedural/useful status. Candidate exhaustion yields partial coverage and no automatic enlargement even when useful comparisons survive. Native installation/dispatch/CI/action and product adoption remain separate.

Definition freeze binds the selected contract/docs, qualified reader code and test horizon. It does NOT pretend to bind unimplemented future entry code. After Ali's inspection, qualify the existing experiment owner's fresh label/outer attempt entry and bind a separate actual execution freeze before any live call. The user-requested stop remains in force; planning is not execution authorization.
