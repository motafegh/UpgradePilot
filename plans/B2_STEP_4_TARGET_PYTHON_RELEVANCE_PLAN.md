# B2 Step 4 — Target Python Relevance Mapping Plan

**Parent plan:** [`B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)  
**Status:** Position-neutral implementation plan; `../MEMORY.md` alone owns live activation and continuation.  
**Owning responsibility:** Map one Step 2 support-drop result and, when activated, one target Python declaration result through the accepted Step 3 specifier method into one bounded target-Python relevance state.

## Purpose

Implement the smallest pure deterministic boundary required by parent-plan Step 4:

```text
UpstreamSupportDropClaimResult
├── problem
│   └── no target evidence is admitted
│       → upstream_claim_unresolved
│
└── GroundedPythonSupportDropClaim
    + TargetPythonEvidence
      ├── target problem
      │   → target_declaration_unresolved
      │
      └── TargetPythonDeclaration
          → evaluate_python_line_specifier(...)
             ├── contains stable X.Y.Z
             │   → declared_python_overlap
             ├── contains no stable X.Y.Z
             │   → outside_declared_python_range
             ├── unsupported admitted method semantics
             │   → comparison_unsupported
             ├── invalid/unsatisfiable target specifier
             │   → target_declaration_unresolved
             └── invalid Python line from a purported trusted claim
                 → upstream_claim_unresolved
```

This result is only about whether the target's declared `requires-python` range overlaps the dropped Python major/minor line. It is not a compatibility, safety, merge, defer, or recommendation result.

## Naming

Use one concrete module and public vocabulary:

```text
src/upgradepilot/target_python_relevance.py

TargetPythonRelevanceState
TargetPythonRelevanceResult
evaluate_target_python_relevance
```

The phrase **target Python relevance** is retained because it is the parent plan's established product term: practically, it means “does this dropped Python line matter to the target's declared Python installation range?”

Do not introduce broad names such as `processor`, `manager`, `handler`, `context`, or `reconciler`.

## Input contract

The public function accepts:

```text
upstream_result: UpstreamSupportDropClaimResult
target_evidence: TargetPythonEvidence | None
```

Activation rule:

1. If `upstream_result` is an `UpstreamSupportDropClaimProblem`, `target_evidence` must be `None` and the result is `upstream_claim_unresolved`.
2. If `upstream_result` is a `GroundedPythonSupportDropClaim`, one `TargetPythonEvidence` value is required.
3. Passing target evidence beside an unresolved upstream result is a caller sequencing error rather than a product relevance state.
4. Omitting target evidence after a grounded claim is a caller sequencing error rather than invented target evidence.

This API shape supports the parent plan's later conditional orchestration without implementing CLI changes during Step 4.

## Trust-boundary rule

Step 4 consumes successful Step 2 and target-parser records as trusted outputs of their owning boundaries.

It does **not**:

- re-ground upstream source quotes;
- re-check crossed-release membership;
- re-parse `pyproject.toml`;
- re-establish exact-head GitHub identity;
- infer target Python support from workflows, classifiers, docs, tox, or tool configuration.

There is no shared identity field available at this boundary that Step 4 can honestly reconcile between the upstream claim and target declaration. Therefore Step 4 preserves both exact input records but does not invent a cross-source provenance check.

A malformed Python line reaching the Step 3 method from a purported `GroundedPythonSupportDropClaim` is mapped defensively to `upstream_claim_unresolved`; normal Step 2 behavior should prevent that state.

## Output contract

Create one immutable result record:

```text
TargetPythonRelevanceResult
├── state: TargetPythonRelevanceState
├── upstream_result: exact Step 2 result
├── target_evidence: exact target result or None
├── specifier_result: exact Step 3 method result or None
└── detail: concise bounded explanation
```

The nested records deliberately preserve the evidence and method result instead of copying package, version, path, revision, blob, witness, and problem fields into a second representation that could drift.

States:

```text
declared_python_overlap
outside_declared_python_range
target_declaration_unresolved
upstream_claim_unresolved
comparison_unsupported
```

## Step 3 problem mapping

`evaluate_python_line_specifier` can return four problem states. Step 4 owns this exact product mapping:

| Step 3 method problem | Step 4 state | Reason |
|---|---|---|
| `invalid_python_line` | `upstream_claim_unresolved` | The purported trusted upstream claim violated the canonical `X.Y` invariant. |
| `invalid_requires_python_specifier` | `target_declaration_unresolved` | Target text exists, but it cannot establish a valid PEP 440 declaration. |
| `unsatisfiable_requires_python_specifier` | `target_declaration_unresolved` | The declaration is syntactically parseable but contradictory, so it cannot establish an honest target range. |
| `unsupported_requires_python_specifier` | `comparison_unsupported` | Both domain inputs exist, but the deliberately bounded Step 3 method does not admit this valid form. |

Do not collapse invalid target evidence into `comparison_unsupported`: unsupported means the accepted method is intentionally narrower than an otherwise existing input, while invalid/contradictory target declarations fail to establish a usable target range.

## Implementation structure

Keep the implementation intentionally linear and educational:

```text
1. validate the two public argument types
2. stop early for unresolved upstream evidence
3. require target evidence only after a grounded claim
4. stop early for a target evidence problem
5. evaluate claim.python_line against declaration.requires_python
6. translate the method result into one relevance state
7. return the exact nested evidence/method records
```

Use module, class, and function docstrings to explain this data flow and its authority boundary. Add comments only where they explain a non-obvious responsibility or mapping; do not narrate obvious Python syntax line by line.

## Controlled proof cases

Add focused deterministic tests for at least:

1. S001-shaped manual trusted input: dropped `3.8` + `>=3.10` → `outside_declared_python_range`.
2. Dropped `3.8` + `>=3.8` → `declared_python_overlap`, preserving the Step 3 witness.
3. Each target parser problem state → `target_declaration_unresolved` without invoking a successful comparison.
4. Upstream claim problem + no target evidence → `upstream_claim_unresolved`.
5. Target evidence supplied when upstream is unresolved → sequencing error.
6. Grounded claim without target evidence → sequencing error.
7. Unsupported target specifier form → `comparison_unsupported`.
8. Invalid target PEP 440 specifier → `target_declaration_unresolved`.
9. Unsatisfiable target declaration → `target_declaration_unresolved`.
10. Invalid Python line on a manually constructed purported grounded claim → `upstream_claim_unresolved`.
11. Package-level exports expose the new Step 4 contracts.
12. Existing complete deterministic suite remains green.

The tests may construct `GroundedPythonSupportDropClaim` directly because Step 4 is intentionally testing the downstream trusted-input boundary, not repeating Step 2 grounding.

## Architecture decision

No new ADR is required for this step.

ADR-0005 already controls the consequential standards method. Step 4 introduces a bounded domain mapping around already accepted contracts and no new dependency, framework, service boundary, persistence rule, network authority, or cross-cutting mechanism.

Create an ADR only if implementation reveals a consequential method choice not already owned by ADR-0005 or the parent plan.

## Stop line

Stop Step 4 after:

- the result contract and mapping exist;
- focused tests cover the controlled cases;
- package-level exports are updated;
- the complete deterministic suite passes locally.

Do not add during this step:

- model or Instructor integration;
- upstream network acquisition;
- release-index or tagged-changelog acquisition;
- CLI reordering;
- conditional target acquisition in runtime orchestration;
- S001 live network execution;
- compatibility, safety, merge, defer, targeted-check, or recommendation logic.
