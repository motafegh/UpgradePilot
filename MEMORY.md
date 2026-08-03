# UpgradePilot Current Memory

**Last updated:** 2026-08-03  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, selected continuation, and current learning state.

Stable plans, specifications, ADRs, source, tests, and dated working records retain their own responsibilities. They must not mirror or compete with this file for live status.

## Single-live-state rule

`MEMORY.md` is replacement state, not append-only history. It alone answers what is selected now, what behavior is verified, what remains open, what happens next, and what learning depth is established.

## Live position

- **Execution branch:** `main`. No separate implementation branch is selected.
- **Route:** B2 — Public PR vertical slice.
- **Selected parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Behavior-validated:** parent-plan Steps 1–5.
- **Step 5 live validation record:** [`working-memory/2026-08-03_B2-step-5-live-s001-validation.md`](working-memory/2026-08-03_B2-step-5-live-s001-validation.md)
- **Current parent responsibility:** Step 6 — evaluate candidate extraction/model only where semantic interpretation is needed.
- **Selected focused Step 6 plan:** [`plans/B2_STEP_6_SUPPORT_DROP_EXTRACTION_EVALUATION_PLAN.md`](plans/B2_STEP_6_SUPPORT_DROP_EXTRACTION_EVALUATION_PLAN.md)
- **Current increment:** Step 6A — frozen narrow support-drop semantic corpus and deterministic oracle validation.
- **Current Step 6A state:** corpus and tests implemented; local validation required before LM Studio environment/model work begins.
- **Step 6A implementation record:** [`working-memory/2026-08-03_B2-step-6a-support-drop-corpus-implementation.md`](working-memory/2026-08-03_B2-step-6a-support-drop-corpus-implementation.md)

## Last behavior-validated executable boundary

Deterministic Step 5 behavior is validated through:

```text
2fff38d86be18d544249f45d7f19e82f9d78f8d6
```

The user reported:

```text
Ran 312 tests in 0.053s

OK
```

## Step 5 live closure

The scenario-specific proof runner:

```text
tools/live_s001_upstream_interval_proof.py
```

first stopped honestly because an environment-provided `GITHUB_TOKEN` produced GitHub HTTP 401. The user verified the variable was set, removed it from the current shell without exposing its value, and reran the public read-only proof anonymously.

Observed passing output established:

```text
package: soupsieve
interval: 2.6 → 2.8.4
PyPI source: https://pypi.org/pypi/soupsieve/json
crossed releases: 2.7, 2.8, 2.8.1, 2.8.2, 2.8.3, 2.8.4
ignored non-PEP-440 release keys: none

tag ref: refs/tags/2.8.4
direct tag object type: commit
direct tag object SHA: 28108ab805818c832d9568142a99844fd95a0d39
resolved commit: 28108ab805818c832d9568142a99844fd95a0d39
annotated-tag peel depth: 0

changelog path: docs/src/markdown/about/changelog.md
changelog blob SHA: 6f221b7398681a580fa199044b3d3f1e11b55493
reported bytes: 17370
decoded bytes: 17370

authority basis: tagged_changelog
GitHub Release bodies admitted: 0
```

Therefore parent Step 5 is **closed and behavior-validated** with both controlled and live public evidence.

The live proof establishes exact upstream interval authority only. It did not extract changelog meaning or compare target Python declarations.

## Step 6 responsibility

The current flow begins from trusted Step 5 authority:

```text
AuthoritativeUpstreamIntervalEvidence
→ untrusted semantic candidate extraction
→ CandidateUpstreamClaimResult
→ validate_support_drop_candidates(...)
→ GroundedPythonSupportDropClaim
   or explicit claim problem
```

The active scope remains only:

```text
category = support_boundary_change
change_state = support_dropped
python_line = explicit X.Y
introduced_in_version = exact trusted crossed release
```

Do not reopen general release-note summarization or the older four-category semantic proposal during this slice.

## Step 6 method constraint

Earlier B2 evidence remains relevant:

- schema-valid structured output does not prove semantic correctness;
- exact quotation does not prove correct interpretation;
- previously evaluated small local deployments produced material false support-drop claims;
- fixture/phrase-shaped regex repair is not accepted product semantics;
- manual claims remain test oracles, not automated product extraction.

The selected Step 6 **evaluation direction** is therefore a bounded structured LLM candidate extractor followed by the already-validated deterministic Step 2 trust boundary. Model/adapter adoption is not yet authorized.

## Existing grounding rule that Step 6 must respect

The Step 2 validator requires an accepted exact quote to contain the normalized Python line token itself.

Therefore:

```text
"Python 3.8 is no longer supported."
→ may ground python_line = 3.8
```

but:

```text
"Python 3.9 or newer is now required."
→ cannot by itself ground a dropped 3.8 claim
```

Step 6 must abstain rather than infer an unstated dropped line under the current contract.

## Step 6A implemented boundary awaiting validation

Frozen corpus:

```text
experiments/step6_support_drop_semantic_corpus.json
```

Deterministic oracle tests:

```text
tests/test_step6_support_drop_semantic_corpus.py
```

The corpus contains 15 controlled cases including direct/paraphrased drops, added/continued support, negation, future tense, ambiguity, raised-minimum-only ungroundable text, multiple distinct dropped lines, unrelated fixes, inert instruction-shaped text, and the exact S001 excerpt.

Three tests prove:

1. corpus identity/critical controls;
2. every positive oracle quote explicitly contains its claimed Python line;
3. every frozen expected semantic outcome maps through `validate_support_drop_candidates(...)` to the expected trusted/problem state.

No model or network call is involved.

The Step 6A corpus/test implementation boundary is:

```text
41b74eda85bbf554b746eac30e6c1a6ca39ddceb
```

Later working-memory/state commits do not alter that executable boundary.

## Exact continuation

From the real checkout:

```bash
git pull --ff-only

python -m unittest tests.test_step6_support_drop_semantic_corpus -v
python -m unittest discover -s tests -v
```

Derived expectations:

```text
focused: 3 tests
complete: 315 tests
```

Observed terminal output controls validation truth.

If Step 6A fails, repair only the corpus/oracle boundary unless evidence proves an older regression.

If Step 6A passes:

1. close the frozen semantic oracle as behavior-validated;
2. activate Step 6B current LM Studio/model/environment observation;
3. do not add OpenAI/Pydantic/Instructor dependencies yet;
4. prefer a direct-`requests` JSON-Schema smoke first unless a concrete missing capability appears;
5. freeze candidate/model configuration before scored semantic evaluation.

## Stop line

Until Step 6A validates, do not begin:

- LM Studio candidate scoring;
- model/adapter product adoption;
- target Python conditional activation;
- CLI orchestration changes;
- full S001 relevance execution;
- compatibility, safety, merge, defer, targeted-check, or recommendation logic.

## Explicitly not established

- passing Step 6A focused/full tests;
- current LM Studio transport/model inventory;
- an adopted support-drop extraction model;
- an adopted Instructor/OpenAI/Pydantic adapter;
- automated grounded S001 Python 3.8 support-drop extraction;
- conditional target-Python activation in CLI runtime;
- S001 automated end-to-end relevance result;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery of Steps 1–6.

## Learning state

Steps 1–5 are behavior-validated at product level. Step 6A concepts are introduced and implemented but not yet locally validated.

Current Step 6 concepts exposed:

- **semantic oracle:** frozen expected meaning used to score an extractor;
- **candidate extraction:** untrusted semantic proposal from prose;
- **structured generation:** output-shape compliance only;
- **mechanical grounding:** exact quote/span exists in trusted source text;
- **trust admission:** deterministic Step 2 validation decides whether a candidate becomes domain evidence;
- **semantic correctness:** separate from schema and grounding;
- **abstention boundary:** relevant prose can remain unresolved when the exact dropped Python line cannot be grounded.

Current depth:

```text
Steps 1–5 behavior validated
+ Step 6 method boundary introduced
+ Step 6A corpus/oracle implemented
but
Step 6A local execution not yet observed
no current model/environment proof
no user-owned Step 6 explanation recorded
no formal mastery assessment
not mastered
```

Product validation and learning mastery remain separate claims.

## State-maintenance rule

When route, selected responsibility, verified executable boundary, blocker, learning state, or exact continuation changes:

1. update `MEMORY.md` only for live state;
2. replace obsolete live statements instead of accumulating them;
3. change plans/specifications/ADRs only when their stable responsibility actually changes;
4. create dated working-memory only for material historical evidence or reasoning, never as another status owner;
5. keep navigation READMEs non-state-bearing.
