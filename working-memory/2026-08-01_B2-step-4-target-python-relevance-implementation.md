# B2 Step 4 — Target Python Relevance Implementation Record

**Date:** 2026-08-01  
**Responsibility:** Dated implementation evidence for parent-plan Step 4.  
**Live-state authority:** None. `../MEMORY.md` alone owns current position and continuation.

## Why this record exists

Step 4 introduced a new domain result boundary, a non-trivial five-state mapping, and an activation rule between upstream evidence and target evidence. Those decisions are useful historical implementation evidence, but they must not become a second live tracker.

## Product/test revision represented

```text
cceb8da55e5908f346141545eacdca4672f7d977
```

Later documentation or memory commits do not alter this source/test boundary unless they explicitly change source or tests.

## Plan

Created:

```text
plans/B2_STEP_4_TARGET_PYTHON_RELEVANCE_PLAN.md
```

The plan freezes the narrow Step 4 data flow:

```text
UpstreamSupportDropClaimResult
├── problem
│   └── target comparison not activated
│       → upstream_claim_unresolved
│
└── GroundedPythonSupportDropClaim
    + TargetPythonEvidence
      ├── target problem
      │   → target_declaration_unresolved
      │
      └── TargetPythonDeclaration
          → evaluate_python_line_specifier(...)
             ├── witness exists
             │   → declared_python_overlap
             ├── no witness
             │   → outside_declared_python_range
             └── method problem
                 → explicit unresolved/unsupported mapping
```

No new ADR was created because ADR-0005 already owns the consequential PEP 440/specifier method. Step 4 adds only a bounded domain mapping around accepted contracts.

## Source implementation

Created:

```text
src/upgradepilot/target_python_relevance.py
```

Public names:

```text
TargetPythonRelevanceState
TargetPythonRelevanceResult
evaluate_target_python_relevance
```

The result preserves the exact nested Step 2 result, target evidence, and Step 3 method result instead of copying their identity/provenance/witness fields into a second representation.

### Activation contract

```text
unresolved upstream result
+ target_evidence must be None
→ upstream_claim_unresolved
```

```text
grounded upstream claim
+ one TargetPythonEvidence value required
→ target problem or Step 3 comparison
```

Supplying target evidence beside an unresolved upstream result or omitting target evidence after a grounded claim is treated as caller sequencing misuse (`ValueError`), not as an invented product evidence state.

This does not yet reorder CLI acquisition. It gives the later orchestration step an API that can preserve the required conditional activation order.

### Trust-boundary decision

Step 4 does not re-ground upstream source spans or re-parse target TOML.

Those responsibilities already belong to:

```text
Step 2 validate_support_drop_candidates
and
target_python.interpret_target_python_declaration
```

Step 4 preserves those records and owns only the downstream mapping. No shared cross-source identity exists at this boundary that could be honestly reconciled without adding new evidence.

### Step 3 problem mapping

```text
invalid_python_line
→ upstream_claim_unresolved
```

This is defensive because normal Step 2 grounding should already guarantee canonical `X.Y`.

```text
invalid_requires_python_specifier
unsatisfiable_requires_python_specifier
→ target_declaration_unresolved
```

The target text exists but does not establish a usable PEP 440 target range.

```text
unsupported_requires_python_specifier
→ comparison_unsupported
```

Both domain inputs exist, but the intentionally bounded accepted method does not admit the version form.

## Educational source structure

The module contains:

- a top-level data-flow diagram;
- a responsibility-boundary explanation;
- a result docstring explaining why nested evidence is preserved;
- a function docstring explaining why target evidence is optional only before activation;
- a focused comment on the early upstream stop as an authority rule rather than an optimization;
- a helper docstring explaining the ownership-based Step 3 problem mapping.

Comments intentionally explain non-obvious responsibility and data-flow choices rather than narrating ordinary Python syntax.

## Controlled tests

Created:

```text
tests/test_target_python_relevance.py
```

The focused tests cover:

- S001-shaped `Python 3.8` + `requires-python >=3.10` → `outside_declared_python_range`;
- overlap and preservation of the exact stable witness;
- all five target parser problem states → `target_declaration_unresolved`;
- unresolved upstream result stopping before target comparison;
- invalid activation sequencing in both directions;
- arbitrary equality (`===`) → `comparison_unsupported`;
- invalid PEP 440 target specifier → target unresolved;
- globally unsatisfiable target declaration → target unresolved;
- malformed Python line on a manually constructed purported grounded claim → upstream unresolved;
- public argument type checks.

The Step 4 tests construct `GroundedPythonSupportDropClaim` directly because they test the downstream trusted-input boundary. Step 2 source grounding remains covered by its own test modules.

Updated:

```text
tests/test_package_interface.py
```

to protect the new package-level Step 4 exports.

## Package interface

Updated:

```text
src/upgradepilot/__init__.py
```

Exports:

```text
TargetPythonRelevanceState
TargetPythonRelevanceResult
evaluate_target_python_relevance
```

Importing the package remains network-free.

A transient connector edit accidentally placed two existing CI names in the wrong import block while adding the new exports. It was detected immediately and corrected in `d3c079975808b86b271d27e97489543522887245` before validation. The final diff contains no such duplicate import ownership.

## Validation state at record creation

No local Step 4 test execution has been observed yet. The GitHub connector cannot execute the user's checkout, so no passing result is claimed.

Recommended focused validation:

```bash
python -m unittest \
  tests.test_target_python_relevance \
  tests.test_package_interface \
  -v
```

Derived focused count at this revision:

```text
17 tests
```

Recommended complete validation:

```bash
python -m unittest discover -s tests -v
```

The previous validated complete count was 251. Step 4 adds 11 focused test methods plus one package-interface test, so the derived new total is 263. The observed local result, not this derived count, controls validation truth.

## Stop line preserved

No Step 4 commit changed:

- CLI orchestration;
- target acquisition order;
- upstream network acquisition;
- release-index or tagged-changelog acquisition;
- model/Instructor integration;
- S001 live execution;
- compatibility, safety, merge, defer, targeted-check, or recommendation behavior.
