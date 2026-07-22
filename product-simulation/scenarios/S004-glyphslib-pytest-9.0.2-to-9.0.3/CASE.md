# S004 Case Record — glyphsLib pytest 9.0.2 → 9.0.3

## Live state

**Run:** `s004-20260722T224500Z-r1`  
**Mode:** prospective manual simulation  
**State:** selected and frozen; transparent baseline executed; full sufficiency confirmation pending

## Why this case was selected

S001–S003 all produced the same broad action as the transparent baseline while the full investigation added materially stronger support. S004 must test the opposite possibility: a real case where the baseline already gives adequate decision support and deeper work should stop.

Candidate screening is preserved in [`../../S004_CANDIDATE_SCREENING.md`](../../S004_CANDIDATE_SCREENING.md).

## Frozen event

Dependabot proposed changing one pinned development dependency in `googlefonts/glyphsLib`:

```text
pytest==9.0.2
→ pytest==9.0.3
```

Frozen identity:

- PR `#1145`;
- base `044f19e4b1437bfc4343592486f4e3c6040306d9`;
- head `f3cda8a94600e58d27f1bc17c99b7693718b6350`;
- changed file `requirements-dev.txt`;
- observed merge commit `a007710184f634557e6524b7e3b115bf74c91b73`.

The historical merge is an observed maintainer action, not correctness evidence.

## Starting invocation

The simulated system receives the public PR locator. Exact revision identity, changed-file content, dependency role, upstream information, and CI responsibility must be acquired.

## Transparent baseline

Inputs frozen before full confirmation:

- version category: `patch`;
- current CI conclusion: `passing`;
- dependency directness: `direct`;
- caution keyword matches: none;
- favorable literal signals: `fixed`, `bug fix`, `CVE`.

Rule B05 selects:

> `merge_after_normal_review`

Baseline limitation:

> It does not know whether the current checks installed the proposed pinned pytest version or exercised pytest-owned responsibilities.

## Smallest full-investigation question

Only one authority-critical question remains:

> Did exact-head CI install `requirements-dev.txt` containing pytest 9.0.3 and then successfully run the repository's ordinary and regression pytest responsibilities?

If yes, and official upstream information presents the patch as a drop-in bug-fix release with no contradictory target evidence, stop. Do not activate broader conditional investigations.

## Inactive conditional work unless evidence changes

- advisory exploitability analysis;
- repository runtime-usage search;
- adapter or framework compatibility analysis;
- causal failure attribution;
- comparable-run environment analysis;
- local or container reproduction;
- targeted-check design;
- private evidence acquisition;
- platform/native/compiler analysis;
- post-merge publication analysis.

## Current stop rule

Stop the full investigation when all are true:

1. direct pinned development role is confirmed;
2. exact-head workflows triggered on the PR;
3. those workflows installed the changed requirements file;
4. pytest-owned ordinary and regression checks passed;
5. official upstream release identity and drop-in bug-fix status are confirmed;
6. no contradictory, missing, stale, or inaccessible decision-critical evidence appears.

## Next checkpoint

Acquire only the evidence needed for those six conditions, record cost and inactive stages, then either stop as baseline-sufficient or reopen the investigation if a condition fails.
