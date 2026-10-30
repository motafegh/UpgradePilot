# Bounded protocol/factory source evidence

This increment implements the protocol/factory family of [the integration design](../2026-10-28-pr-driven-caller-signature-design/DESIGN.md#8-implementation-and-evidence-sequence), after the experiment-architecture gate. It adds conditional source relationships, not object execution, effective runtime typing or native product adoption.

## Delivered path and scope

```text
target import/reference
→ qualified module/re-export
→ captured module Name allocation to a declared-class call
→ that class's own __getattr__ declaration
→ direct returned-class allocation in a lexical return
→ that returned class's own __call__ declaration(s)
→ unchanged argument checker under one-receiver/source premises
→ retained steps, comparisons, limitations and offline view
```

[The existing correspondence owner](../../../experiments/api_source_correspondence.py) reuses the same qualified source/name/re-export resolver; no framework, heap/type engine, package-specific mapping or second binding evaluator was added. Classes/aliases/modules/attributes can be renamed. Relative/module-level imported classes and annotated module allocations are supported. Competing allocations, branch returns and repeated/overload declarations remain distinct paths. Constructor/getter arguments, effective exports/attributes, branch activation, allocation success and receiver remain explicit premises.

General factory functions, return-variable propagation, arbitrary local types, inherited protocols, multi-attribute chains and dynamically computed class expressions remain unsupported. Async/generator getters explicitly refuse this direct-instance pattern: their lexical return does not make the attribute a callable instance. Nested callback returns do not become the getter's return. Mutation/deletion and missing/unsupported alternatives remain visible even when another path yields a useful candidate. No argument/default/annotation/decorator is evaluated.

The unchanged checker may establish partial keyword reception while full binding stays undetermined for starred arguments. A declared __call__ receiving ids through **kwargs does not establish that the marker, ids values or target execution are valid.

## Versioned retention and public consumer

Ordinary envelope format2 now emits correspondence method2. Four new operations retain literal allocation/getter/return/protocol spans. The fixed reader supports method1 with its original operation vocabulary and method2 with the new vocabulary. It checks source text/span/endpoints, ordered factory steps and minimum factory premises; it never reruns the source analyzer/checker. Downgrading a protocol path to method1, dropping a required step/premise or altering saved return text refuses.

The ordinary view now shows retained qualified callable/decorator strings as syntax, alongside paths and premises. This makes overload-decorated declarations visible rather than silently choosing one or representing every rejection as an effective API incompatibility. Shared evidence codec, curated v1 reader, source acquisition, binder, checker and native product are unchanged. Existing method-source sets continue to bind the changed correspondence/ordinary producer files.

## Controlled ordinary-entry result

[The saved controlled view](controlled-ordinary/view.txt), [result](controlled-ordinary/result.json) and [summary](controlled-review.json) exercise the actual repo/PR entry through bridge→mediator→changed-package re-exports, then allocation/getter/return/call protocol. All provider contents are locally authored and HTTP is forbidden. No callable pair, source path, expected result or known adapter version is an ordinary runner argument.

One initial observation, zero identity-only refetches, one changed-file read;4 release identities/6 module questions/416 admitted library bytes.8 retained files/493 bytes/66 AST nodes/9 facts produce2 comparisons: native old source receives app, proposed source rejects app under the saved source/receiver premises. Bounded worker, immutable result and AST/network/discovery-forbidden cold opening are protected by the responsibility-owned controls.

## Actual retained real-source discovery

New retained_component_discovery successors analyze the original selected12-file glyphsLib/pytest catalog without supplied callable selectors or expected outcomes. Raw source/results remain private. This inherits the OLD CAPTURE'S selected material scope; it is not an ordinary fresh acquisition or complete target inventory. Native transition labels remain pytest9.0.2→9.0.3 at the recorded original target revisions.

[Initial review](retained-case-initial-review.json) binds the first20caa23d attempt1/1.899609s. After async-getter/shape guards and explicit decorator display, [final review](retained-case-final-review.json) binds a separately named cec964d2 successor attempt2/2.005175s over the same input bytes. Both remain immutable. The first was a completed development observation, not a failed case retried to rescue a verdict; the final method qualification is explicitly separate. No original frozen curated result was rerun/repaired/regraded.

Final analysis:12 retained files/205,876 bytes,20,917 AST nodes/1,113 facts,68 source-candidate comparisons. It retains152 discovery gaps and0 omitted gap records; that does not imply complete repository/discovery coverage.

It automatically connects two target pytest.mark.parametrize calls through:

```text
pytest.mark re-export
→ MARK_GEN re-export
→ MarkGenerator allocation
→ __getattr__ return of MarkDecorator
→ all declared MarkDecorator.__call__ alternatives
```

| Direct protocol observations | Count | Local meaning |
| --- | --- | --- |
| Target call sites | 2 | Two source locations in one retained target/library scenario |
| Old/proposed × all3 declarations × two call sites | 12 | Distinct conditional comparisons, not12 independent cases |
| Undecorated implementation declarations | 4 | ids received through **kwargs, locally bound under one-receiver/source premises |
| Overload-decorated declarations | 8 | Both rejecting and binding syntax alternatives retained; no effective-overload selection |

The remaining comparisons are other directly observed/rooted source candidates, including descendants of the protocol body. They are not additional independent protocol examples. Marker semantics, installed versions, actual dispatch/test exercise, whole-update compatibility and the historical glyphsLib CI/model limitations remain unproved or separately owned.

## Verification and preservation

- API216 tests/2.675s pass:10 protocol controls added over206, covering renamed/imported/annotated allocations, alternative returns/overloads/allocations, unsupported values/nested returns/functions/missing protocol, async/generator getters, source/pair limits, mutation gaps, starred arguments, version/source/order/premise corruption and ordinary worker/cold-view composition.
- Architecture7 tests/1.119s and static131-artifact/122-module/255-edge/31-exception/96-native-file check pass. No new module, dependency, private exception or layer inversion.
- [Full regression](full-regression.json):610 tests/40.004s versus previous600; exact pre-existing1 failure/25 error identities AND messages and11 optional skip identities match. No new failure; full historical suite remains RED for documented compatibility debt.
- [Compatibility](compatibility.json): nine actual saved bundles (original v1, old method1/v2 controls and new method2 controls/development successors) open with AST/network/checker forbidden. All10 original frozen private member hashes and prior tracked evidence manifests remain unchanged. No analysis or result regeneration occurs during opening.
- [Final receipt](verification.json) binds source/tests/control/profile identities and proof limits. Product src/tests/tools/package/specifications/ADRs have no diff from858f5f31. No fresh product regression is claimed; no fresh provider/model/third-party target/workflow execution or action permission occurred.

From the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src:tests:. .venv/bin/python3 -m experiments.api_ordinary_call_signature_trial open --result working-memory/evidence/2026-10-30-protocol-factory-source-correspondence/controlled-ordinary
```

Use a printed unit ID with --source/--start-line/--line-count for literal retained source. Original/raw real-case successor bundles stay in owner-only storage, not this public control directory.

## Handoff and later learning

[The single cycle](../../2026-10-30_protocol-factory-source-correspondence_build-cycle.md) records qualification, design choices, first proof, generator/async boundary correction, saved schema/presentation and immutable method-horizon distinctions. Later learning should trace the actual re-export→allocation→getter→return→__call__ path, explain receiver versus argument expansion, distinguish overload declarations from effective dispatch, inspect gaps/partial coverage, and open saved data without rerunning it. Independent learner mastery is not established.

Next responsibility is actual live acquisition orchestration/allocation qualification: target/source selection and reservations, provider/body/deadline bounds and controlled traces before selecting one separately frozen fresh ordinary PR attempt. In particular, the12-module source budget and target scan may starve a real route; retained selected sources do not prove those providers will discover/retain the same closure. Do not hide that with known paths, enlarged caps or another parser family. Useful fresh ordinary evidence then leads to the separately selected native API/Workspace/report contract and product delivery. No such live run or product adoption is performed by this cycle.
