# B2 First A→B Impact/Applicability Implementation — Session Record

**Date:** 2026-08-11  
**Type:** Dated implementation/baseline/validation evidence  
**Live-state authority:** `../MEMORY.md` only

## Session purpose

Resume implementation under the approved `../plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md` after the A/B/C product-model reconciliation and the seven-concept learning handoff.

This session intentionally implemented only the smallest A→B foundation around the already-proven Target-Python support-drop mechanism. Conversation C orchestration and Conversation D final-action semantics were not implemented.

## Step 1 baseline inspection

Baseline head before source edits:

`c2595e79ca16b10c14446ab093f61815d0c18155` — `Resume A-C implementation with learning in parallel`

Inspected as the immediate implementation evidence surface:

- `src/upgradepilot/investigation.py`
- `src/upgradepilot/target/relevance.py`
- `tests/test_target_python_relevance.py`
- `tests/test_investigation.py`
- `docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`
- the selected A→C foundation plan and `MEMORY.md`

Key finding:

The existing code already owns the narrow deterministic relation:

```text
grounded upstream Python support-drop claim
+
exact target requires-python evidence
→ TargetPythonRelevanceResult
```

but it does not yet own explicit A/B objects for:

```text
impact candidate
→ propositions
→ applicability path(s)
→ path-model coverage
→ candidate applicability
```

Therefore the first implementation should compose the existing evaluator rather than replace or duplicate it.

## Implemented bounded slice

Implementation commit:

`fa75caa70c578daf436580fe1151e163455a36f0` — `Add first A-B impact applicability foundation`

Added a new implemented responsibility package:

- `src/upgradepilot/impact/__init__.py`
- `src/upgradepilot/impact/applicability.py`
- `src/upgradepilot/impact/python_support.py`

Added active product tests:

- `tests/test_impact_applicability.py`
- `tests/test_python_support_impact.py`

### A — mechanism-specific candidate

`PythonSupportDropImpactCandidate` preserves:

- exact pull-request/target revision identity;
- exact dependency transition identity;
- the grounded upstream support-drop claim;
- mechanism status as established;
- exposure and activation as still requiring evaluation;
- consequence as possible rather than established.

The constructor rejects an upstream claim whose interval does not match the exact dependency transition.

### B — proposition/path/applicability semantics

The first composition model represents:

- proposition state: `established | refuted | unresolved | conflicted`;
- proposition evidence coverage: `sufficient | insufficient | unresolved`;
- conjunctive path state;
- path-model coverage: `sufficient | insufficient | unresolved`;
- candidate applicability: `established_applicable | established_not_applicable | unresolved | conflicted`.

The critical negative-inference rule is explicit:

```text
all represented paths refuted
+
path-model coverage sufficient
→ established_not_applicable
```

but:

```text
all represented paths refuted
+
path-model coverage insufficient/unresolved
→ unresolved
```

The path-level results remain attached to the candidate assessment so a scalar candidate state does not erase unresolved/conflicted alternative-path information.

### Target-Python adapter

`evaluate_python_support_drop_impact(...)` reuses `TargetPythonRelevanceResult` rather than reimplementing PEP 440/specifier behavior.

For the first bounded candidate it separates these propositions:

1. upstream Python support-drop mechanism crossed — established by the grounded upstream claim;
2. exact target Python declaration established — established or unresolved from target evidence;
3. declared target range intersects dropped Python line — established/refuted/unresolved from the existing deterministic relevance result.

The bounded candidate models exactly one declared-installation-range applicability path, so path-model coverage for that candidate family is explicitly `sufficient`. This does not claim candidate-discovery completeness or transition-level absence of all material impact.

## Validation performed in this session

The assistant execution environment could not clone GitHub because outbound DNS/network access from the local container failed. The repository also has no GitHub commit statuses/CI attached to the new commit.

Therefore no full installed-project regression is claimed here.

A locally reconstructed isolated harness executed the new logic under Python 3.13.5:

- applicability composition tests: **9 passed**;
- Python-support candidate/adapter tests: **7 passed**;
- combined isolated new-logic result: **16 passed**.

The executed cases include the plan-required pressure shapes:

- one complete path established;
- all represented paths refuted with sufficient coverage;
- all represented paths refuted with unresolved coverage;
- necessary proposition unresolved;
- genuine conflict;
- established path plus conflicted alternative;
- unresolved alternative plus conflicted alternative;
- refuted necessary proposition eliminating a conjunctive path;
- target evidence unavailable;
- comparison unsupported despite target evidence being present;
- exact dependency/revision identity mismatch rejection.

These tests validate the new logic itself, not its installed integration with the repository.

## Learning reinforced through implementation

This slice directly exercised three of the seven current learning concepts:

1. **Evidence vs inference:** the target declaration can be established while the activation comparison still remains unresolved.
2. **Open-world/completeness:** path refutation is not enough for candidate non-applicability without path-model coverage.
3. **Necessary/sufficient and AND/OR paths:** one refuted necessary proposition eliminates a conjunctive path, while one established alternative path is sufficient for candidate applicability.

It also reinforces the A/B boundary: creating an impact candidate does not establish target exposure or activation.

## Stop line respected

Not implemented in this session:

- C investigation selection or retry semantics;
- generic investigation planner;
- candidate-discovery completeness;
- transition-level absence claim;
- numerical scoring/VoI;
- D sufficiency/policy/action semantics;
- maintainer recommendation or merge decision.

## Next technical continuation

The next bounded source step should wire the new A/B result into `PublicPullRequestInvestigation` after the existing Target-Python relevance evaluation and add focused orchestration tests for:

- overlap → `established_applicable`;
- bounded non-overlap → `established_not_applicable`;
- target evidence problem/comparison problem → `unresolved`;
- unresolved upstream claim → no grounded A candidate.

After integration, run narrow relevant tests and then the full active product regression in the normal project WSL/Python environment before upgrading the implementation proof state.

Only after the integrated B state is behavior-tested should Step 5 introduce the first real C activation, preserving the distinction between target evidence **not yet acquired** and acquisition **already attempted and failed/unavailable**.
