# B2 Step 6A — Support-Drop Semantic Corpus Implementation

**Date:** 2026-08-03  
**Parent:** `plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`  
**Selected Step 6 plan:** `plans/B2_STEP_6_SUPPORT_DROP_EXTRACTION_EVALUATION_PLAN.md`  
**State:** corpus/oracle implemented; local validation pending

## Why Step 6A exists

Step 5 now provides trusted exact upstream text. Step 2 already provides the deterministic trust boundary:

```text
CandidateUpstreamClaimResult
+ AuthoritativeUpstreamIntervalEvidence
→ validate_support_drop_candidates(...)
→ GroundedPythonSupportDropClaim
   or explicit problem
```

Before a model is scored, the semantic oracle itself must be frozen and proven compatible with that trust boundary.

## Focused Step 6 direction

The current slice admits only:

```text
support_boundary_change
+ support_dropped
+ explicit Python X.Y line
+ exact introduced release
+ exact grounded source quote/span
```

Historical four-category semantic work remains background evidence only. Step 6 does not reopen general release-note semantics.

## Important grounding constraint discovered before corpus freeze

`validate_support_drop_candidates(...)` requires the exact accepted source quote to contain the proposed Python line token.

Therefore:

```text
Python 3.8 is no longer supported.
→ may ground 3.8
```

but:

```text
Python 3.9 or newer is now required.
→ cannot ground a dropped 3.8 claim under the current contract
```

The focused Step 6 plan was corrected before corpus creation so the model is not rewarded for inferring an unstated Python line.

## Frozen corpus

Created:

```text
experiments/step6_support_drop_semantic_corpus.json
```

It contains 15 cases covering:

- direct support-drop wording;
- paraphrased `no longer supported` wording;
- paraphrased `support removed` wording;
- explicit dropped line plus raised minimum;
- raised minimum without an explicit dropped line — unresolved control;
- support added;
- continued support;
- negated support drop;
- future/planned support drop;
- ambiguous support wording;
- irrelevant fix-only text;
- two distinct dropped Python lines;
- one support drop plus unrelated fix;
- inert instruction-shaped documentation text near a legitimate drop;
- exact S001 2.8 changelog excerpt.

The expected candidate state and expected Step 2 validator result are frozen before any model scoring.

## Corpus safety/authority rule

Known S001 wording is an oracle/calibration case, not production extraction logic.

No phrase table, regex extractor, package-specific semantic rule, or expected result was added to `src/`.

## Deterministic oracle tests

Created:

```text
tests/test_step6_support_drop_semantic_corpus.py
```

Three tests establish:

1. case IDs are unique and critical controls are present;
2. every positive oracle quote explicitly contains its claimed Python line;
3. every frozen oracle outcome maps through the existing Step 2 validator to the expected grounded/problem state.

For positive cases, quote offsets are derived from a quote that must occur exactly once in the frozen source text. The test then constructs only the already-defined Step 2 candidate dataclasses and calls `validate_support_drop_candidates(...)`.

No model, network request, LM Studio endpoint, Instructor, Pydantic, OpenAI client, or new runtime dependency is involved.

## Implementation boundary

The Step 6A corpus/test implementation ends at:

```text
41b74eda85bbf554b746eac30e6c1a6ca39ddceb
```

Relevant commits:

```text
399f99065a94a0d787c9e20eb674c82179358ef8  freeze semantic corpus
41b74eda85bbf554b746eac30e6c1a6ca39ddceb  validate corpus oracle
```

The selected Step 6 plan was added/refined immediately beforehand. No production `src/` file changed in Step 6A.

## Validation gate

Run:

```bash
python -m unittest tests.test_step6_support_drop_semantic_corpus -v
python -m unittest discover -s tests -v
```

Derived expectations:

```text
focused: 3 tests
complete: 315 tests
```

Observed terminal output controls truth.

Do not begin model/environment scoring until the oracle boundary is green.

## Learning depth

Step 6A introduces the difference between:

```text
semantic oracle
model candidate
mechanical grounding
deterministic trust admission
```

Implementation exposure exists, but no user-owned explanation or mastery assessment is recorded.
