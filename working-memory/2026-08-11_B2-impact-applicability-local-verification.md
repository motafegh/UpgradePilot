# B2 Impact/Applicability Local Verification

**Date:** 2026-08-11  
**Type:** Dated local execution evidence  
**Live-state authority:** `../MEMORY.md` only

## Scope

Verify the first bounded Python-support-drop technical impact-candidate and candidate-specific applicability implementation in the normal UpgradePilot WSL/Python environment after the pre-acquisition unresolved-state extension.

Verified commits present on `main` before execution included:

- `fa75caa70c578daf436580fe1151e163455a36f0` — first bounded impact/applicability foundation;
- `9110a514311b1f66dcf54928290a8842731cfe05` — orchestration integration;
- `cf8529f3053b5e56e2b005cad811fb84ab3df837` — focused orchestration tests;
- `4bc5061c084640606435595c5d95978b8f7ea554` — explicit pre-acquisition target uncertainty;
- `0f57e7ab347a8d13c86991c44605178eac085570` — pre-acquisition applicability test.

## Environment

Observed local environment:

```text
branch: main
Python: 3.12.3
interpreter: /home/motafeq/projects/UpgradePilot/.venv/bin/python
```

The checkout was fast-forwarded to `origin/main` before testing.

## Focused implementation verification

Executed the three focused implementation layers:

```text
tests/test_impact_applicability.py
→ 9 tests passed

tests/test_python_support_impact.py
→ 9 tests passed

tests/test_investigation.py
→ 6 tests passed
```

Total focused result:

```text
24 tests passed
```

This directly verifies in the real installed project environment:

- proposition/path/candidate applicability composition;
- Python-support-drop impact-candidate identity and applicability mapping;
- explicit distinction between target evidence not yet acquired and an attempted target-evidence problem;
- overlap, bounded non-overlap, unresolved target evidence, unsupported comparison, and identity-mismatch behavior;
- integration into `PublicPullRequestInvestigation`.

## Nearest regression verification

The existing Target-Python interpretation and target-relevance regression tests were executed and reported green:

```text
tests/test_target_python.py
→ passed

tests/test_target_python_relevance.py
→ passed
```

These protect the lower-level exact-head `requires-python` interpretation and deterministic Python-line/specifier relation reused by the new applicability layer.

## Full active product regression

Executed:

```bash
python -m unittest discover -s tests -v
```

Result:

```text
Ran 384 tests in 0.068s

OK
```

Therefore the first impact/applicability source and orchestration changes do not currently introduce a detected regression in the active deterministic product suite.

## Installed/import smoke

Executed an import smoke for the installed package and new impact modules.

Result:

```text
installed imports: OK
```

## Proof boundary

This verification establishes that the current deterministic test suite and installed imports are green for the implemented first technical impact-candidate / candidate-specific applicability slice and the explicit pre-acquisition unresolved state.

It does **not** establish:

- correctness of not-yet-implemented discriminating investigation selection/stopping;
- candidate-discovery completeness;
- transition-level absence of impact;
- final overall evidence sufficiency;
- repository-policy/residual-risk interpretation;
- maintainer-facing recommendation or merge safety.

## Continuation

The previous verification blocker is cleared. The next bounded implementation responsibility may now proceed to the first real discriminating-investigation activation around the exact target Python declaration, while preserving the distinction between:

```text
not yet acquired
```

and:

```text
already attempted and failed/unavailable
```

Before adding more source, the implementation just verified can be reviewed in small learning-by-building steps as needed.
