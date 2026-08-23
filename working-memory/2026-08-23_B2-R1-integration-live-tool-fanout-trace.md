# Working Memory — B2 R1 Integration + Live-Tool Exact-File Fan-Out Trace

**Date:** 2026-08-23  
**Status:** TRACE COMPLETE; IMPLEMENTATION AUTHORIZED  
**Execution branch:** `agent/r1-exact-file-contract-migration`  
**Current plan:** `../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`

## 1. Scope

This slice reviews the remaining exact-file contract pressure in the application-integration and developer live-proof surfaces:

```text
tests/test_investigation.py
tests/test_step7f_end_to_end.py
tools/live_s001_upstream_interval_proof.py
tools/live_s001_support_drop_extractor_proof.py
```

The purpose is not to redesign application orchestration or live-proof semantics. It is to determine whether the historical provider metadata still establishes any proposition owned by these surfaces after R1 strengthened the exact-file contract.

## 2. Normal application path protected by the integration tests

```text
PullRequestIdentity + admitted dependency transition
→ upstream release interval + repository authority
→ exact tag commit
→ exact changelog acquisition
→ TaggedChangelogEvidence
→ authoritative crossed-release source window
→ bounded semantic candidate extraction
→ deterministic source grounding
→ grounded support-drop claim/problem
→ conditional exact target pyproject.toml acquisition
→ TargetPythonEvidence
→ target relevance
→ impact applicability
```

`tests/test_investigation.py` protects application sequencing and conditional activation. `tests/test_step7f_end_to_end.py` additionally protects the real Step-7B/7C/7D/7E product path while replacing only the external provider/model responses with controlled fixtures.

The semantic questions are therefore orchestration/trust questions, not transport-metadata questions.

## 3. Residual stale integration fixtures

The two integration suites still fabricate retired exact-file fields:

```text
returned_path
blob_sha
reported_byte_count
decoded_byte_count
retrieved_at
```

Some Target-Python fixtures also omit the now-required repository identity.

These fields do not participate in the tests' asserted propositions. They are construction baggage inherited from the old weak exact-file model.

Decision:

```text
RepositoryTextFile integration fixtures
→ use repository + path + revision + content only

orchestration assertions
→ KEEP unchanged

LLM candidate/trust boundary assertions
→ KEEP unchanged

conditional target activation assertions
→ KEEP unchanged
```

## 4. Live-proof tooling responsibility

The two `tools/live_s001_*` files are developer validation tooling, not product authority. They consume product evidence and print selected diagnostics.

Important ownership rule:

```text
diagnostic convenience
!= product evidence-retention requirement
```

A live tool must adapt when the product evidence contract becomes narrower. It must not pressure production to retain provider transport metadata solely so the tool can print it.

### `live_s001_upstream_interval_proof.py`

The tool currently prints `TaggedChangelogEvidence.blob_sha` and reported/decoded byte counts, fields intentionally removed from the durable tagged-source contract.

Those diagnostics are replaced by the durable source locator already owned by the tagged evidence:

```text
repository + resolved_commit_sha + path
```

Tag-resolution internals printed from `GitHubTagCommitEvidence` remain because that tool explicitly demonstrates tag resolution and those fields still belong to that acquisition evidence type.

### `live_s001_support_drop_extractor_proof.py`

The tool currently prints `CrossedReleaseSourceWindow.blob_sha`, which no longer exists.

The source window already carries:

```text
repository
resolved_commit_sha
path
```

That exact source locator is the correct diagnostic replacement. Character-count/window-bound diagnostics remain because they are actual source-window facts used by the bounded semantic adapter.

## 5. KEEP / REMOVE decisions

### KEEP

```text
integration orchestration assertions
exact repository/revision/path construction
conditional target acquisition
upstream authority sequence
bounded local-model candidate path
deterministic grounding/trust admission
source-window character bounds
live tag-resolution diagnostics
durable repository@commit:path diagnostics
```

### REMOVE from fixtures/tool output

```text
returned_path
blob_sha
reported_byte_count
decoded_byte_count
retrieved_at
fixture-only byte-size calculations
```

## 6. Learning point

Three different surfaces can consume the same source object but own different propositions:

```text
provider
→ proves external response/acquisition truth

application integration
→ proves sequencing + activation + coherent evidence flow

developer live tool
→ observes/demonstrates the product path
```

Therefore:

```text
provider fact is useful for debugging
!= integration contract must carry it
!= durable domain evidence must preserve it
```

The right question is always: **what proposition does this layer own after the source object leaves the provider boundary?**

## 7. Authorized implementation

Modify only the four scoped files unless static review exposes a directly coupled stale consumer:

1. migrate integration `RepositoryTextFile` fixtures to the strong four-field contract;
2. remove no-longer-used byte-size fixture calculations;
3. replace live-tool blob/count output with durable exact source locator output;
4. preserve every orchestration, trust, activation, source-window, and bounded-model assertion;
5. perform static diff review;
6. record implementation and next residual R1 pressure.

No production source redesign is authorized by this trace.
