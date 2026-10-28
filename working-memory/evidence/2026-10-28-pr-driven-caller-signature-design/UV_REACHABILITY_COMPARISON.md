# Source correspondence compared with uv selected-root reachability

**Scope:** design review against maine32c764e, October28. Source correspondence is proposed, not implemented. This dated comparison supports the [integration proposal](DESIGN.md) and its [single cycle](../../2026-10-28_pr-driven-caller-signature-integration_design-cycle.md); it does not supersede specifications or activate Build.

## Different questions, similar evidence discipline

`uv_reachability` asks: **Does one explicitly selected root in this exact lock have an unconditional lock-backed path to the changed package?**

Source correspondence will ask: **Which captured Python declarations can be linked to this observed call through supported source steps, and which premises remain?** The existing checker then asks whether the supplied argument shape fits each selected declared signature under stated receiver/pairing premises.

These questions must not share a result type. Neither establishes installed versions, execution, behavioral compatibility or maintainer-action permission. A source-correspondence candidate is also not yet a Product Decision Model technical-impact/applicability candidate: consequences and target activation require their own evaluation.

## Producer → consumer ownership

| Stage | UV implementation | Consequence for source design |
| --- | --- | --- |
| Exact source identity | Repository acquisition → dependency context/exact lock; [input validation](../../../src/upgradepilot/dependency/uv_reachability.py) joins repository/revision/source path | Reuse acquisition/catalog identity; keep target, old/proposed dependency and sampled adapter identities distinct |
| Shared structural facts | [uv_lock_structure](../../../src/upgradepilot/dependency/uv_lock_structure.py) admits schema/package records for transition and reachability consumers | Reuse existing scoped bindings and caller/signature extraction; add only needed source-step facts. No second import-flow interpreter or source resolver |
| Narrow interpretation | [uv_reachability](../../../src/upgradepilot/dependency/uv_reachability.py) projects edges/roots, binds the selected local package and traverses | Source correspondence owns candidate paths, without taking over origin assessments, acquisition, checker outcomes or activation |
| Normal composition | [workflow_commands](../../../src/upgradepilot/ci/workflow_commands.py) derives selection from actual workflow commands; [consumption](../../../src/upgradepilot/ci/consumption.py) composes without strengthening | Ordinary PR discovery derives requests/candidates from observed inputs; it cannot inject curated answers or fabricate positive bindings |
| Later proof | [dependency_exercise](../../../src/upgradepilot/ci/dependency_exercise.py) retains static/runtime/direct-exercise axes; runtime state is separately owned | Source paths and local argument results stay separate from target activation/version/runtime evidence |
| Retention/display | [CI codec](../../../src/upgradepilot/ci/native_codec.py) retains conditional paths/blockers; [report projection](../../../src/upgradepilot/report_projection.py) currently omits them | Reuse explicit reconstruction/consumer separation as a pattern. Do not copy the omission or use the CI codec for API data |

The completed [B2 reconciliation plan](../../../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md) explains historical membership→selected-root narrowing and shared-parser separation. It is provenance, not an active sequence to reopen; current source/tests independently confirm the boundaries. The [Product Decision Model](../../../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md) §§6–8 owns broader applicability/coverage rules without requiring a universal graph/SAT engine.

## Reuse and separation decisions

| Concept/pattern | Disposition and reason |
| --- | --- |
| Exact identities before relational joins | Reuse. UV resolves repeated package names with available version/source discriminators; Python needs source-unit identity, span/definition, import context and old/proposed/sample role. A function name is not an identity |
| Conditional path alongside stronger result | Reuse. UV marker-bearing paths remain diagnostic/unresolved; source paths retain branch/re-export/base/receiver/decorator/version premises. Structural paths do not establish actual dispatch |
| Conditions attached to the route | Reuse with source-specific representation. UV strings record encountered markers without solving their conjunction. New premises need operation/source/span links; alternatives must not be flattened into one alleged conjunction |
| State-aware traversal and cycle bounds | Reuse the principle with local standard containers. UV visited keys include record index, activated extras and conditions. Source traversal must distinguish source/version, binding context, operation/receiver and material premises without erasing candidate provenance |
| Unknown versus justified bounded negative | Reuse. UV not_established requires exhaustion of its represented bound-project roots; workspace non-exhaustion, ambiguity or limits stay unresolved. Source output must distinguish no candidate in an examined supported domain from unavailable/unsupported/unexamined work |
| Shared parsing, separate semantic consumers | Reuse ownership. Share existing AST/binding/fact responsibilities and bounded admission; source steps may require additional facts. Do not move Python analysis into the lock parser or make all facts one universal model |
| One-way composition and cold reconstruction | Reuse. Retain material paths/premises and open without recomputation. Product API adoption still needs its own admitted family/codec, not extra CI fields |
| One witness is enough; return immediately | Keep UV-specific. Its positive proposition is existential. Source comparison must preserve materially different old/proposed declarations, receiver possibilities and routes within bounds |
| One diagnostic chosen by fewest conditions/shortest path | Keep UV-specific. `_prefer_candidate` chooses a reproducible diagnostic, not the most probable/applicable route. Source output must not discard another version/base/signature because a path sorts first |
| UV selectors/extras/markers and numeric limits | Keep separate. Source/path/request/byte/time costs differ. Reuse explicit bounds/failure handling, not UV's10,000 states/100-depth values or group/extra activation rules |

**Executable reuse decision:** do not import UV's result, private traversal/edge/condition helpers or parser into the source owner; do not extract a generic graph/premise framework now. Their contracts differ, and sharing a deque or small deduplication loop does not justify an abstraction. Reuse the already identified API/source/binding/checker/catalog owners. Reassess a shared helper only if two admitted consumers later need identical semantics and proof, with a simpler-baseline comparison.

## Source-candidate policy refined by this review

1. Keep **candidate association/path**, **local comparison under premises**, and **discovery coverage/omissions** separately inspectable. A complete local argument check does not complete discovery or prove dispatch.
2. Keep exact steps and path-local premises. Ordering/deduplication controls work/presentation, not probability or applicability. Equivalent work may share parsing/cache entries; different version/definition/receiver/premise paths remain distinguishable.
3. Candidate/path caps retain explicit truncation and unexamined work. Useful positives can survive incomplete discovery, without an exhaustive-coverage claim. Zero candidates under a cap, ambiguity or unsupported syntax is not no exposure/not applicable.
4. Preserve checker rejected/bound/undetermined independently. Conditional mismatch remains useful despite unresolved dispatch; unresolved receiver may coexist with observed keyword reception. Do not translate these into UV states.
5. Summary/offline detail must expose paths, exact blockers and omissions with retained source references. A compact summary may link to complete detail; generic unresolved prose alone is insufficient.
6. UV/static CI may contribute separately attributed environment context later, but cannot gate source examination or substitute for callable correspondence. A dependency path cannot fill a missing Python edge; a Python path cannot establish environment membership.

The simplest credible implementation remains a local bounded source-step operation between existing acquisition and checker owners. Type layout and exact supported constructs remain implementation-entry decisions, not an accepted general graph contract.

## Real-case contrast

The historical [Soup Sieve case](../../../product-simulation/scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/CASE.md) records:

```text
selected docs roots → mkdocs-llmstxt → beautifulsoup4 → soupsieve
```

This relates lock records. Even an unconditional witness does not show a call to `soupsieve.select`, step execution or an installed version. The current S001-shaped test is a controlled reconstruction, not a fresh historical-case replay. Historical case prose about installation is not proof supplied by this owner.

The [retained HTTPX comparison](../2026-10-28-caller-signature-build/REVIEW.md) instead relates:

```text
target TestClient call
→ selected Starlette initializer
→ its super().__init__(..., app=..., ...) call
→ selected old/proposed HTTPX Client.__init__ declaration
```

These arrows carry class-call, parent/receiver and source-version premises. The older captured forwarder binds against old HTTPX and rejects app against proposed HTTPX; the newer forwarder binds against proposed HTTPX. A first-candidate-only search or name-only deduplication would lose a meaningful contrast. This remains existing curated proof: automatic discovery must earn each arrow and cannot inject older Starlette to recover a known mismatch.

The [glyphsLib/pytest result](../2026-10-28-caller-signature-second-real-case/REVIEW.md) adds declared function candidates for `pytest.raises` and allocation/getter/returned-class/__call__ steps for `pytest.mark.parametrize`. The binder observes ids entering **kwargs while withholding complete binding with unresolved receiver mode. A dependency/import path alone cannot supply those protocol steps.

## Exposed presentation omission and disposition

**Observed:** `_project_ci` copies consumption state/reason/detail and witness_path, omitting conditional_candidate_path and unresolved_conditions. The [diagnostic](uv-composition-diagnostic.json) supplies controlled exact workflow/project/lock records to the ordinary static collector, without a precomposed uv answer:

```text
CI consumption: unresolved
retained path: mkdocs-llmstxt → beautifulsoup4 → soupsieve
retained blocker: edge marker to soupsieve: python_version >= '3.12'
native CI value-codec round-trip: equal
report: general reason/detail present; exact path/blocker absent
```

This loses diagnostic usefulness at presentation. It is not a demonstrated acquisition/UV/runtime-state defect or false positive. Full/partial report parity can pass while both omit a producer field; parity alone does not prove consumer completeness. The probe is not full canonical Workspace reconstruction or real target execution.

**Recommended disposition:** separately select a bounded report-projection repair that displays conditional paths/conditions as diagnostics, preserves unresolved state and adds producer→rendered-view regression coverage. No UV algorithm or saved-schema change is indicated by this evidence. Include the repair in the next Build-scope discussion; do not hide it behind the new capability or automatically implement it during this comparison. No repair occurred. This need not become dependency redesign or a full Workspace migration prerequisite.

The first probe incorrectly looked for the per-consumption reason in the workflow assessment reason. Inspection showed it survives as a fact; the corrected probe isolates the two-field omission. No frozen evaluation or producer result changed.

## Verification and remaining proof

Fresh27 existing tests pass/0.012s:16 selected-root tests,5 shared-structure tests,1 package-scope test,4 CI composition tests and1 report parity test. Additional probes establish unresolved on traversal-bound exhaustion, preservation of an unconditional route after a conditional route through the same nodes, and the composition/codec/report omission above. The [receipt](uv-comparison-verification.json) records exact selectors, inspected hashes and preservation checks.

This verifies current owners, not the proposed source owner. Implementation needs controls for old/new role isolation, repeated definitions/alternatives, path-local premises, receiver contexts, cycles, truncation, unsupported source forms, path/blocker display and cold opening without analysis. Both frozen HTTPX/pytest attempts remain unchanged. No fresh acquisition, model, third-party execution, compatibility/usefulness claim or product adoption follows.
