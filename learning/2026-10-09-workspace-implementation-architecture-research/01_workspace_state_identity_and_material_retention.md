# Workspace state, identity and material retention

**Snapshot:** research `7ae80a07d5fb9180ddb30145ea389bebe6553c5f`, 2026-10-09. Read the [package horizon and authority map](README.md) first. The code here is experimental; native facts come from existing product owners.

## The responsibility and mental model

A frozen final investigation result answers what one acquisition/evaluation sequence returned. An evolving Workspace must also explain which revision a view came from, what a request depended on, how an assessment changed, and which material content remains available. A report is another projection of that knowledge; its omissions cannot define what canonical state is allowed to remember.

Think of a published revision as an immutable index into immutable records. A successor adds records and relationships without changing what earlier records meant. A checkpoint then retains the declared material dependency closure for named consumers. These are three different mechanisms: publication, dependency selection and encoding.

The research does not make this graph a universal evidence model. A dependency edge says that a consumer needs another record retained. It does not establish that the referenced evidence is true, sufficient, relevant to every consumer, or a complete semantic premise set.

## Read the actual records and publication path

Open [workspace_revision_representation.py](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/experiments/workspace_revision_representation.py). Its important units are:

| Unit | Role in the experiment |
| --- | --- |
| `TraceRecord` | Explicit ID, owner, kind, scope, immutable payload bytes, named dependencies, or an explicit missing-content gap. |
| `PublishedRevision` | Lineage, revision/predecessor, opaque target bytes, consumer roots, record index and material triggering records. |
| `_admit` | Reject inconsistent reuse of an ID and different bytes for one exact source-text scope. |
| `ImmutableSuccessorHistory.publish` | Copy the previous index, add admitted records, validate/freeze a successor, then append it to history. |
| `material_closure` | Traverse roots and declared dependencies, rejecting broken references. |
| `encode_checkpoint` / `decode_checkpoint` | Preserve and validate the declared closure as opaque records; do not hydrate trusted native objects. |

The publication order matters. `_admit` first builds candidate additions. `records = dict(previous.records)` creates an owned successor dictionary. `_freeze` validates its graph and exposes it through `MappingProxyType`. Only after that succeeds does `history.append(revision)` advance history. If admission or reference validation fails, the previous publication remains the current revision.

`MappingProxyType` prevents mutation through the proxy, but it does not freeze the dictionary behind it. `_freeze` itself does not copy the dictionary. Historical stability depends on the callers handing it an owned dictionary that is no longer mutated. The executed negative control wrapped a shared mutable index and leaked 15 new IDs into an old view. The lesson is about ownership of the backing collection, not merely choosing a read-only API.

Frozen dataclasses also do not recursively freeze arbitrary contents. Here, `bytes`, immutable dependency tuples and an owned index make sharing safe. Copying the index is a shallow copy: the immutable payload bytes can be shared without duplicating them at each publication. This is not an event store; complete revision indexes remain in memory.

## Trace a native consumer's material needs

The [retention corpus](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/experiments/workspace_retention_corpus.py) runs existing native owners on constructed offline inputs. Its CI path retains a `RequirementSatisfiedAtCommandCompletion` beside a different command's unresolved environment. Both are legitimate bounded native results; a single generic success flag would erase their distinction.

Trace one root:

```text
ci:runtime
  → supplied coverage/source inputs and native coverage
  → supplied workflow definition/run/jobs/steps and source context
  → exact dependency source bytes and target identity
```

Inspect the actual dependencies in the corpus rather than infer them from this sketch. Orchestration composes material `coverage_inputs` and `source_contexts` before the native owners run. A final result alone does not necessarily retain those local arguments. Capture must occur at the boundary where the material input is still available.

The support path preserves the earlier unresolved assessment, the selected investigation need, target declaration/relevance, the later applicable assessment and a lineage relationship. The successor does not overwrite the earlier result. Optional-extra selection stays unresolved because marker truth is not evaluated. New view/request/attempt/proposal records in this corpus are explicitly simulated lifecycle pressure.

The encoded final closure contains 36 of 37 addressable records. The unreferenced debug record is omitted; material annotation and lineage remain. This proves the experiment can distinguish discardable diagnostics from its declared material graph. It does not select production garbage collection or prove all native premises were declared.

## Identity is more than matching bytes

There are several identities to keep separate:

| Identity | Question it answers |
| --- | --- |
| Investigation target/lineage | Which exact repository, PR, base and head does this historical investigation belong to? |
| Record identity and scope | Which owner-produced observation, request or assessment is this, and where does its meaning apply? |
| Content digest | Do these retained payload bytes match? |
| Host annotation identity | What later navigation/history information was attached without changing the original payload? |

Two empty reads can have the same SHA-256 digest while belonging to different source scopes. One exact source scope cannot legitimately acquire inconsistent bytes under different record IDs. `_admit` checks both same-ID consistency and exact-source scope consistency. Content deduplication can save bytes, but it cannot create independent support or erase observation provenance.

Target semantics require extra care. The initial E1 corpus target encodes its full fixed PR/dependency fixture; it is an experiment token, not the final identity codec. Later public grounding exposed that including title/state/ref metadata overbound the continuation token. Grounding and E4 use the four exact repository/PR/base/head keys and retain descriptive metadata separately. Historical SHA-bound evidence remains about the old target if the PR moves; deliberate follow-head behavior would need a new exact lineage and admitted reuse rules.

## Why a correct round trip can still be wrong

Suppose encoding and decoding produce the same result, but the checkpoint never included the workflow text consumed by a native evaluator. Equality says that serialization preserved what it received. It cannot say that capture supplied everything required.

The result-only negative control round-tripped structurally while missing five independently required CI/source inputs. This is why the test suite enumerates expected material IDs separately from the graph traversal. The graph can detect a declared broken reference; it cannot discover an undeclared edge by itself. Two implementations can also agree because they share the same missing-input assumption.

`affected_dependents` follows declared links to identify records potentially affected by changed inputs. It does not reevaluate native facts or establish semantic refutation. Broad historical-retention edges can overapproximate semantic dependence. E3 consequently introduces explicit material slot bindings; storing history and deciding current validity need different relationships.

`encode_fields` tags inspected dataclass fields and selected values such as versions/timestamps. Unknown types fail rather than become arbitrary strings. The decoder returns opaque `TraceRecord` payloads, not trusted imported classes. Byte fidelity is useful evidence, but typed recovery remains a separate problem taught in note 4.

## Comparison, corrections and evidence limits

The mutable alternative stages unpublished changes in `draft`/`pending`, freezes a copied index on publication and rolls back an invalid draft. Its old revisions stay stable too. The comparison therefore asks whether extra staging responsibility earns its complexity, not whether mutation is inherently forbidden.

[E1 evidence](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/working-memory/evidence/2026-10-08-workspace-revision-representation/README.md) reports identical checkpoint bytes across representations, with small mixed timing differences. At 1,850 starting records, medians for 30 unbatched updates were 14.555 ms for immutable successors and 13.025 ms for drafts; batching changed cost more strongly. The allocation measurement excluded prebuilt payload bytes and was not process RSS. There was no disk I/O or throughput requirement. Immutable successors are a provisional simpler baseline, not a proven universally faster design.

An independent fixture probe also found two different project texts at one repository/revision/path after early differential tests passed. The correction shared one exact source binding and added a collision regression. This was a fixture contradiction, not a contradiction in main's semantics. Later real grounding found much larger source content; the small E1 source-size rationale cannot be generalized to all PRs.

Read [representation tests](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/experiments/tests/test_workspace_revision_representation.py), especially `test_historical_views_remain_stable_when_successors_are_published`, `test_native_owners_produce_distinct_results_and_material_basis_survives` and `test_basis_changes_identify_affected_successors_without_native_reinterpretation`. The recorded 15 tests establish bounded native meanings, stability, closure, rollback and negative controls. They do not establish full capture, a trusted codec, durability, semantic adequacy or production adoption.

## Learning depth and fast return

**Own:** index ownership, immutable identity, independent capture completeness and the difference between history links and current premises. **Understand operationally:** dataclass freezing, shallow copying, graph traversal and encode/decode validation. **Lookup:** exact JSON/tag syntax and incidental serialization helpers. **Defer:** scalable delta storage, production retention policy and a complete native codec.

For a fast return: explain why a proxy can leak updates; open `publish` and `_freeze`; trace `ci:runtime` through the corpus; inspect the independent required-ID assertion. Then distinguish a broken declared edge from a missing undeclared premise.

### Transfer questions

1. Where must a successor obtain its owned dictionary? What breaks if `_freeze` receives a dictionary that another caller later mutates?
2. If two empty reads hash equally, what must remain distinct before either can support a proposition?
3. What independent assertion would expose a checkpoint that round-trips but omitted evaluator inputs?
4. Why does a title-only refresh preserve the exact target while a changed head requires another lineage?
5. When does dependency traversal identify potential revalidation work without proving an old native assessment false?
