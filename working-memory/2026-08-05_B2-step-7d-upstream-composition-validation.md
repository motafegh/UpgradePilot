# B2 Step 7D Upstream Composition Validation

**Date:** 2026-08-05  
**Scope:** Step 7D support-drop runtime evaluation / upstream composition  
**Implementation head:** `3ccd5464692d200e026248e2acc4989fac5e3836`  
**Result:** Passed

## Validated responsibility

```text
AuthoritativeUpstreamIntervalEvidence
→ complete crossed-release source-window construction
→ bounded semantic candidate extraction
→ deterministic support-drop candidate validation
→ UpstreamSupportDropClaimResult
```

The implementation owner is `src/upgradepilot/upstream/support_drop.py`.

## Reported validation

Ali reported the focused Step 7D regression and the full active product regression green in WSL after the Step 7D implementation tranche.

The focused coverage includes:

- positive candidate reaching grounding only through `validate_support_drop_candidates(...)`;
- no-claim and semantic-unresolved results remaining non-grounded;
- missing crossed-release evidence stopping before candidate extraction;
- missing exact tagged changelog stopping before candidate extraction;
- incomplete/oversized source windows stopping before candidate extraction;
- invalid composition inputs remaining explicit failures rather than synthesized claims.

## Boundary retained

Step 7D does not acquire target `pyproject.toml`, interpret target Python, evaluate target relevance, modify CI behavior, claim compatibility/safety, or recommend maintainer action.

## Continuation

Step 7D is closed. Continue with **Step 7E — conditional application orchestration** in `src/upgradepilot/investigation.py`:

```text
existing CI branch remains independent
+
trusted package/upstream/interval acquisition
→ Step 7D support-drop result
→ grounded claim?
    ├── no  → target Python remains inactive
    └── yes → exact-head pyproject.toml
              → target declaration
              → target-Python relevance
```
