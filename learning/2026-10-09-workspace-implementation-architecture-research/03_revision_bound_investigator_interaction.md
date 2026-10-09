# Revision-bound Investigator interaction

**Snapshot:** research `7ae80a07d5fb9180ddb30145ea389bebe6553c5f`, 2026-10-09. See the [package horizon](README.md). This is a deterministic scripted interaction experiment; it establishes no Investigator superiority or general semantic evaluator.

## The seam's responsibility

An Investigator can read retained knowledge and submit attributed requests/proposals. The host admits effects using current policy and material bindings. A capability driver performs admitted work. Native owners establish domain results. Independent admitted evaluation would establish proposal correctness or adequacy; unavailable evaluation stays unsupported. Synthesis retains action authority.

The useful abstraction is therefore an interaction boundary, not a database API and not a model framework. Read [workspace_investigator_seam.py](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/experiments/workspace_investigator_seam.py) before its storage adapter.

| Experimental unit | What it supplies |
| --- | --- |
| `RevisionRef` | Originating lineage, revision number and opaque exact-target token. |
| `Binding` | A material slot mapped to the immutable record supplying it. |
| `AcquisitionRequest` | Request ID, origin revision/basis, capability, scope, method and proposition discriminator. |
| `Projection` | Delivered records, omitted-but-addressable IDs, origin basis/method, capability description and continuation/adequacy status. |
| `InvestigatorPort` | `read`, `request`, `request_bytes`, `propose`; no admission, execution, native publication or checkpoint control. |
| `WorkspaceHost` | Admission, attempts, observations/problems, view/proposal history and publication under supplied host policy. |
| `CheckpointPort` | Private `load`/`save` protocol with portable conflict/unconfirmed outcomes. |

Python private attributes express intended responsibility, not process isolation from hostile same-process code. `HostPolicy`, principals and relevance routing are disclosed offline controls, not a production authentication or authorization service. An owner string in a record does not itself authenticate its origin.

## Trace the supported native path

The [native fixture](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/experiments/workspace_seam_native.py) supplies an explicitly authored changelog candidate. Existing native grounding produces a support-drop claim; the native impact owner initially returns unresolved and its selector identifies a genuine target-declaration need. Exact-file delivery is simulated. Native declaration/relevance/impact processing then produces an applicable result.

```text
native unresolved assessment and selected need
→ host seed and explicit continuation validation
→ Investigator reads a view and creates an attributed request
→ host records request plus admission
→ separate driver starts an attempt
→ exact source result is observed and structurally revalidated
→ native owner evaluates selected inputs and publishes a successor
```

Walk this through the host methods:

1. **`seed` and `continue_current`:** restored/fresh hosts begin inactive. The latter checks exact target, supplied current authorization and missing content behind current bindings. Operations still perform their own method/capability/basis checks; this initial activation does not validate every future effect.
2. **`read`:** validate requested IDs, capture the current revision and material basis, compute delivered/omitted sets, then publish a view record. The returned view references the revision read before that publication. Reading retained state creates delivery history; it does not acquire another source or prove examination.
3. **`request`:** retain the attributed request and a separate admission outcome. Admission can reject the request while preserving why it was rejected. Valid structure is not execution permission by itself.
4. **`start`:** locate admission, revalidate the request under current policy and publish an attempt before an external result would be accepted. An existing incomplete attempt yields `completion_unknown_no_auto_retry`; a known completed attempt is not started again.
5. **`observe`:** require an attempt, validate current request/result bindings, retain the source and completion relation, and mark the need for native owner revalidation. Observation does not itself assert applicability.
6. **Native `evaluate`:** select owner-relevant inputs, execute supported declaration/relevance/impact processing, retain its assessment and derive whether the selector still identifies a need. A retired need is not overall investigation adequacy.

The host's state records retain all preceding records for this proof. That is conservative history retention, not a scalable premise graph or selective retention design. The fixture's exact-target token is supplied opaque data, including its fixed PR/dependency fixture; later public grounding/E4 explicitly correct target normalization. Do not treat the fixture token as a production identity codec.

## Original basis and current basis answer different questions

`_validate` checks exact target/lineage, revision range, method, capability, active current authority, current material basis, original revision bindings, retained content, current need and request meaning/scope. Its ordering produces explicit rejection outcomes; none is a semantic judgment of the source text.

The **original** check asks whether the request could actually have been made from its claimed revision. The **current** check asks whether that request's material premises still hold now. Both matter. An early adversarial regression used today's candidate binding while claiming an older revision; current equality alone accepted it. The repair checks the retained `workspace:state:<origin>` bindings and returns `basis_not_in_original_revision`.

A second regression showed that an old view could silently inherit a new method. `propose` now obtains/validates the originating view's method, and the consumer facade passes it explicitly. A newer method can change how a claim should be interpreted even if the cited bytes stayed equal. This is method provenance, not just content integrity.

| Change while a same-target request is outstanding | Experimental handling |
| --- | --- |
| Unrelated annotation for another candidate | Revalidate and admit the delayed result; preserve origin and later admission revisions. |
| Candidate/need/context material binding changes | Reject the old result basis; retain prior history and rejected-result content. |
| Current method/capability/authority withdrawn | Refuse effects under the old conditions. Historical admission is not current authority. |
| Operating an old lineage under another exact target | Return `target_changed`; never rewrite the old target or its SHA-bound evidence. |

Revision inequality alone is insufficient: reads themselves publish view history, and unrelated annotations may advance the revision without changing a request's meaning. Expected-revision publication detects competing writes; material-basis validation detects evidence staleness. Refresh after publication conflict disables active continuation, so the caller must explicitly revalidate before proposing another publication/effect.

Future follow-head behavior would need a new exact target/lineage and explicit evidence reuse rules. A new PR commit does not retroactively change historical exact-SHA facts.

## Delivery, citations and independent evaluation

The omission test first retains target evidence, then delivers only the need. The source remains addressable but was not delivered in that view. Citing it from that view is rejected. A later explicit read delivers it and permits an attributed proposal, whose semantic evaluation remains unsupported.

The distinctions are:

```text
available → delivered → examination/use evidence → cited → evaluated support → sufficient
```

These are different relationships, not automatic implications. A view records delivery and `examined_or_used = unknown`. A proposal records a consumer assertion of use; it does not prove actual cognitive examination or correctness. `propose` binds citations to a delivered view and retains a separate `unsupported_no_admitted_evaluator` outcome with no invented assessment. The prototype's restricted view-citation rule demonstrates this seam; it does not forbid every possible future admitted access channel.

Evaluation inputs must not be restricted to proposer citations. `retain_evidence` adds candidate-relevant counterevidence to the host context, changes that context binding and marks owner revalidation necessary. `evaluation_inputs` selects relevant source/counter/gap records even when omitted from the consumer's view.

The existing target-Python native API accepts one `pyproject.toml`. When the fixture supplies a contrary README or an unavailable relevant counterobservation, the bridge retains/selects those inputs but returns `unsupported_owner_input_set`. It neither silently drops the extra input nor invents a conflicted proposition. The earlier assessment remains historical; general conflict semantics and adequacy have not been implemented.

An early counter-source helper failed to retain the supplied contrary content, while status-string assertions still looked plausible. The corrected test asserts the actual selected IDs and scope/content. Test the stimulus as well as its reported outcome.

## Duplicates, unknown completion and storage independence

Exact duplicate requests/results do not create new independent support. Same-scope source aliases can acknowledge already known data while keeping one evidence basis. A second admitted attempt may acknowledge exact retained evidence historically; the special case does not waive current target/method/capability/authority checks. Inconsistent same-ID or exact-scope content is an ingestion problem, not automatically semantic conflict.

Known capability failure is an attempt problem. Unknown completion is retained with no retry permission. A failed read is not an empty successful observation, and neither establishes a global negative domain fact.

The [private checkpoint adapters](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/experiments/workspace_seam_checkpoints.py) translate stale publication to `False` and storage faults to `CheckpointUnavailable`. `_publish` returns portable `publication_conflict` or `publication_unconfirmed`, leaves the candidate out of local canonical state and disables continuation. A refresh may reveal committed state after lost acknowledgement; it does not authorize re-execution. The SQLite adapter deliberately refuses damaged-head fallback for active use rather than silently selecting an older head.

No Investigator value exposes SQL tables, transactions, WAL or engine exceptions. `Protocol` specifies the small host persistence interface without requiring inheritance; storage implementations satisfy it through their methods. The encoded-memory baseline also serializes/restores checkpoints, making comparison stronger than retaining a shared live revision object.

The strict serialized request has bounded bytes, exact fields/types and duplicate-key refusal. `object_pairs_hook` catches repeated JSON keys that ordinary dictionary parsing would overwrite. The parser cannot accept supplied admission/principal/truth fields. Typed Python and serialized requests meet the same admission logic; serialization is an optional transport choice, not another authority path.

## Reachability and proof

The [scenario classification](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/working-memory/evidence/2026-10-08-workspace-experiment3-grounding/README.md) distinguishes overlapping roles:

| Role | Example and limit |
| --- | --- |
| Intrinsic to proposed Workspace mechanics | Immutable views, original/current provenance, honest delivery and recovery status. |
| Concrete current native path | `investigate_public_pull_request` selects a target read and reevaluates support impact. It does not implement the Workspace request ledger. |
| Future/adaptive pressure | Outstanding delayed results, concurrent publishers, live counterevidence or capability changes during a request. Current orchestration is synchronous. |
| Defensive invariant | Forged authority/basis, inconsistent identity, corruption and invented retry permission. Keep protection even if normal producers cannot emit the stimulus. |

[E3 evidence](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/working-memory/evidence/2026-10-08-workspace-investigator-seam/README.md) reports 21 scenarios × two backends × two transports = 84 traces and 74 seam test executions. Read [seam tests](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/experiments/tests/test_workspace_investigator_seam.py), especially the original-basis and old-view-method regressions, delayed-result tests and `test_counterevidence_omitted_from_view_is_selected_and_invalidates_basis`. Equal traces supplement independent status/selected-ID/native assertions; they cannot prove semantic correctness or real adaptive behavior.

## Learning depth and fast return

**Own:** lifecycle/authority separation, original versus current basis, material versus revision staleness, delivery versus support, and unsupported versus unresolved outcomes. **Understand operationally:** typed values, strict parsing, private persistence translation, duplicate handling and restoration activation. **Lookup:** dataclass conversion/JSON syntax and incidental transport costs. **Defer:** general relevance discovery, semantic conflict/adequacy evaluators, production authentication, adaptive scheduling and H1 mechanisms.

Fast return: trace `read` through `request`, `start`, `observe` and native `evaluate`; open `_validate`; inspect the old-revision/new-basis regression; add the contrary-source test mentally and predict unsupported evaluation.

### Transfer questions

1. Why does a read advance history without making a delayed request materially stale?
2. How can a request match today's basis and still lie about its original revision?
3. Why must omitted counterevidence enter native input selection even when a proposal never cites it?
4. What can be reported after an unconfirmed checkpoint acknowledgement, and what still cannot be retried automatically?
5. Which parts of this normal trace exist in current product orchestration, and which require future Workspace/adaptive capabilities?
