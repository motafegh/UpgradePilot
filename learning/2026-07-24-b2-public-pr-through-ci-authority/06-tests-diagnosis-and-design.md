# 06 — Tests, Diagnosis, and Design Reasoning

## SMART objective

In 30–40 minutes, map each test file to its protected boundary, diagnose six failures, and defend four current design choices with costs and revisit conditions.

## Test map

### `test_github_client.py`

Protects PR identity, ambiguous `404`, changed-file validation, pagination, and count reconciliation.

### `test_dependency_change.py`

Protects exact-pin support and explicit missing, incomplete, mismatched, range, and ambiguous outcomes.

### `test_github_actions.py`

Protects exact-head/event binding, empty evidence, pagination, job/run/SHA linkage, and step summaries.

### `test_github_repository.py`

Protects exact run identity, workflow path, exact-head file retrieval, decoding, and unavailable definitions.

### `test_workflow_commands.py`

Protects the narrow supported `run` command forms.

### `test_ci_authority.py`

Protects direct sufficiency, tox/multi-job/unavailable unresolved states, and unsuccessful-job insufficiency.

## Deterministic versus live evidence

Deterministic mocked tests prove behavior for controlled inputs. They do not prove GitHub currently returns the same real evidence.

The live S004 run proved one real public path in Ali's WSL2 environment:

```text
28 tests passed
pytest 9.0.2 → 9.0.3
exact-head Actions evidence acquired
Regression Tests → sufficient
Test + Deploy → unresolved
overall → sufficient
```

It does not prove broad repository support, safety, recommendation correctness, or independent ownership.

## Diagnose the earliest failed boundary

- `Input rejected` → local locator validation.
- timeout/HTTP reason → transport/acquisition.
- successful response cannot establish evidence → shape/type/identity/completeness.
- dependency unsupported → patch interpretation.
- no exact-head workflows → absent CI evidence, not green CI.
- workflow definition unavailable → execution-definition linkage.
- authority unresolved → current interpretation cannot prove enough.
- authority insufficient → evidence supports a bounded negative conclusion.

## Failure drill

1. Different-head workflow run is accepted.
2. Patch count disagreement returns supported dependency.
3. Multi-job workflow returns sufficient by combining commands.
4. Workflow-definition `404` crashes instead of becoming unresolved.
5. Unit tests pass; live command is rate-limited.
6. Real workflow command changes and now becomes unresolved.

Expected diagnosis:

1. exact-head Actions invariant broken;
2. incomplete patch can contaminate identity;
3. unsafe cross-job inference;
4. unavailable evidence state lost;
5. deterministic logic works; live acquisition capacity/authentication failed;
6. shallow grammar no longer matches or evidence genuinely changed.

## Review an AI-generated test

Reject or revise if it:

- asserts only that no exception occurred;
- duplicates implementation logic;
- changes multiple variables unnecessarily;
- mocks away the invariant being tested;
- checks green status without exact SHA;
- hardcodes S004 into runtime rules;
- treats unresolved as error without justification;
- verifies output text while ignoring the result contract.

A strong test names one protected rule and one meaningful defect class.

## Design decisions to understand

### Requests, not async HTTP

Current need is one bounded synchronous PR flow. Async complexity has no measured benefit yet.

Revisit when concurrent PR processing or latency is a demonstrated blocker.

### Immutable dataclasses, not Pydantic

Current runtime validation is explicit and small. Dataclasses provide clear records without another dependency/model system.

Revisit when nested schemas, public serialization, or repeated validation creates real burden.

### Shallow workflow reader, not full YAML dependency

Current grammar is narrow and fails closed to unresolved.

Cost: valid complex workflows remain unresolved.

Revisit when richer YAML materially blocks supported cases or ad hoc parsing becomes fragile.

### No tox tracing now

S004 already has one direct sufficient workflow. Tracing tox would not change the current existential result.

Revisit only when indirect evidence blocks a required decision or reveals material risk.

## General tradeoff template

For any proposed tool/framework:

```text
responsibility served:
simplest credible baseline:
risk controlled:
costi/failure modes:
reversal path:
evidence needed to admit:
```

Do not defend a choice only with “simpler” or “more production-grade.” Connect it to the active responsibility.

## Claims discipline

Permitted:

> One exact-head workflow directly exercised pytest in S004.

Not permitted:

- every workflow exercised it;
- the tests are complete;
- the version is safe;
- merge is recommended;
- the project is production-ready.

## Pass condition

Diagnose all six failures, map every test file correctly, and defend the four design choices with both benefits and costs.