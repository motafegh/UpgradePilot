# B2 Step 6 — Complete Semantic-Extraction Engineering Retrospective

**Date:** 2026-08-03  
**Scope:** Step 6 support-drop semantic extraction, from local inference bring-up through bounded adoption  
**Nature:** Dated historical engineering record; not live project authority

## Why this record exists

Step 6 was not a straight path from prompt to passing model. It exposed several different failure classes across networking, structured generation, semantic-contract design, exact grounding, experiment execution, evidence persistence, scoring, and reproducibility.

This record preserves those failures, why they happened, how they were diagnosed, what changed, and what must not be forgotten when the extractor is integrated or later replaced.

The final passing score is intentionally not allowed to erase the failed approaches that produced the design.

## Final bounded outcome

Accepted Step 6 disposition:

```text
adopt_bounded_extractor
```

Accepted deployment/method:

```text
LM Studio local HTTP
+ gemma-4-e4b-it-ud
+ model-facing contract v2
+ deterministic source-line recovery
+ mandatory validate_support_drop_candidates(...)
```

Final deterministic adoption assessment:

```text
strict oracle: 24 / 25
adoption safety: 25 / 25
all material critical repeats consistent: true
all 10 adoption-gate checks: true
```

Observed 25-call latency:

```text
mean:   8.852445 s
median: 8.414366 s
min:    5.355407 s
max:   12.549101 s
```

Final full deterministic suite reported by Ali:

```text
Ran 339 tests in 0.062s

OK
```

The accepted scope is only explicit current Python `X.Y` support-drop extraction. It is not general model trust.

---

## 1. Initial local HTTP failure — Privoxy intercepted localhost

### Symptom

The first Step 6C localhost smoke failed before useful model evaluation:

```text
HTTPError: 500 Server Error: Internal Privoxy Error
for url: http://127.0.0.1:12345/v1/models
```

### Root cause

The WSL project process inherited HTTP proxy environment variables. The Python `requests` client therefore attempted to route the LM Studio loopback request through Privoxy instead of treating `127.0.0.1` as a direct local endpoint.

This was not an LM Studio model failure and not a GitHub/network failure. It was a process-environment transport-boundary problem.

### Fix

A dedicated WSL runner was introduced that changes only the child-process environment:

```text
remove HTTP_PROXY / HTTPS_PROXY / ALL_PROXY
remove lowercase equivalents
set NO_PROXY=127.0.0.1,localhost,::1
set no_proxy=127.0.0.1,localhost,::1
```

The global shell/system proxy was not disabled.

### Why this fix was preferred

- preserves the user's normal proxy configuration;
- makes the loopback exception explicit and reproducible;
- avoids hidden dependence on machine-wide proxy settings;
- keeps WSL as the normal UpgradePilot control plane.

### Lesson

A local service can still be affected by inherited network middleware. A transport failure must be diagnosed before it is attributed to the model/provider.

---

## 2. First real model response — semantic meaning mostly right, representation wrong

After proxy isolation, Step 6C reached LM Studio successfully and produced the first real response from:

```text
gemma-4-e4b-it-ud
```

The model returned the intended support-drop meaning but failed the original candidate-mapping contract.

### Model output problems

The model produced roughly:

```text
state = unresolved
python_line = "Python 3.8"
introduced_in_version = "2.8"
source_quote = "- **NEW**: Drop support for Python 3.8."
```

The exact authoritative source contained:

```text
-   **NEW**: Drop support for Python 3.8.
```

### Failure A — non-canonical Python line

The model used:

```text
Python 3.8
```

instead of the domain token:

```text
3.8
```

### Failure B — exact source quote was normalized

The model normalized Markdown spacing. The meaning was unchanged, but exact quote matching correctly failed because the trusted source bytes differed.

### Failure C — incoherent result state

The model returned `unresolved` while also supplying a candidate. Under the trusted candidate contract, a non-available state cannot contain candidate claims.

### Failure D — completion limit

The response ended with:

```text
finish_reason = length
max_tokens = 512
```

A large proportion of completion tokens were reasoning tokens.

### What was deliberately NOT done

The deterministic Step 2 validator was not weakened.

UpgradePilot did not:

- fuzzy-match model quotes;
- normalize model text into trusted evidence;
- accept `Python 3.8` as equivalent domain state inside the validator;
- ignore state/candidate incoherence;
- treat the model's semantic intent as sufficient trust.

### Lesson

Correct natural-language understanding does not imply a trustworthy evidence representation. Exact grounding and semantic extraction are separate responsibilities.

---

## 3. Grounding redesign — line IDs instead of model text transcription

The quote failure revealed that asking an LLM to reproduce exact source bytes was the wrong responsibility split.

### Old model responsibility

The model was asked to emit fields including exact source quote text.

### New responsibility

Source text was deterministically indexed:

```text
L1 | ## 2.8
L2 |
L3 | -   **NEW**: Drop support for Python 3.8.
L4 | -   **NEW**: Add support for Python 3.14.
L5 | -   **NEW**: Deploy with PyPI's "Trusted Publisher".
```

The model then selected:

```text
python_line = 3.8
introduced_in_version = 2.8
source_line_id = L3
```

Deterministic code recovered:

- the exact original line;
- exact whitespace;
- exact `quote_start` and `quote_end` offsets;
- trusted/fixed source kind;
- trusted package and interval identity;
- fixed category/direction.

### Python-line vocabulary also became deterministic

Explicit source tokens such as:

```text
Python 3.8
Python 3.14
```

were scanned mechanically and converted to allowed schema values:

```text
3.8
3.14
```

The model could no longer legally return `Python 3.8`.

### Token budget adjustment

Because the first real run ended at the 512-token limit, the bounded completion limit was raised to:

```text
1024
```

No automatic retries were introduced.

### Result

The next Step 6C run completed successfully:

```text
structured candidate mapping: PASS
semantic oracle: PASS
Step 2 trust admission: PASS
finish_reason: stop
STEP 6C SMOKE: PASS
```

### Lesson

Let the model choose meaning. Let deterministic code own canonicalization, exact text, offsets, fixed identity, and trust invariants whenever possible.

---

## 4. Structured output success was kept separate from semantic correctness

A central Step 6 principle was established explicitly:

```text
transport
≠ structured generation
≠ semantic correctness
≠ grounding
≠ trust admission
≠ product activation
```

A model could choose a real exact line such as:

```text
Add support for Python 3.14.
```

and label it as a drop. Exact source grounding could still succeed because that line really exists.

Therefore the frozen semantic oracle remained separate from Step 2 grounding.

### Lesson

`grounded` means the evidence span exists and matches the proposed candidate identity constraints. It does not by itself prove that the model interpreted the sentence correctly.

---

## 5. Step 6D contract-v1 evaluation — 14/25 and why the raw score was misleading

The first full 25-call evaluation completed:

```text
passed: 14
failed: 11
all critical repeats consistent: true
```

At first glance this looked like a poor semantic model score. Detailed evidence showed two distinct failure classes.

### Seven candidate-bearing state contradictions

Cases included direct drops, paraphrases, a valid drop plus unrelated text, and all repeated S001 trials.

The model selected the correct candidate fields but emitted:

```text
state = unresolved
candidates = [correct candidate]
```

The model's reasoning often explicitly described the correct support-drop conclusion.

### Four actual zero-candidate classification disagreements

The remaining failures were:

```text
raised_minimum_without_explicit_dropped_line r1/r2/r3
ambiguous_support_wording r1
```

The model produced zero candidates and chose:

```text
no_relevant_claim
```

while the strict frozen oracle expected:

```text
unresolved
```

### Diagnosis

The first seven failures were largely caused by duplicated output design:

```text
candidate exists
AND
state must say candidates_available
```

Those two fields encoded the same fact independently.

### Lesson

When a model is asked to predict a value that deterministic code can derive from another returned value, the extra field is a new incoherence surface, not useful semantic information.

---

## 6. Contract v2 — remove redundant positive-state prediction

Contract v2 changed the model-facing result to:

```text
candidates: [...]
unresolved_if_no_candidates: bool
detail: string
```

The adapter derives:

```text
if candidates:
    candidates_available
elif unresolved_if_no_candidates:
    unresolved
else:
    no_relevant_claim
```

The distinction between `unresolved` and `no_relevant_claim` remains semantic only when there are zero candidates.

### Why this was not "fixing the model's answer"

Candidate-bearing state is logically implied by candidate presence. Deriving it is domain normalization, not changing semantic meaning.

Zero-candidate historical state choices were preserved exactly during replay, so genuine semantic disagreements could not be silently rescued.

---

## 7. Offline counterfactual replay — isolate the contract change before spending new model calls

Instead of immediately repeating 25 live calls, the exact committed v1 structured responses were replayed through contract v2.

### Replay result

```text
historical passed: 14
v2 replay passed: 21
v2 replay failed: 4
historical failures rescued: 7
new model calls: 0
```

All four remaining failures were the zero-candidate state mismatch described above.

### Why replay mattered

It isolated one variable:

```text
same model outputs
same source text
same semantic oracle
same deterministic validator
only contract interpretation changed
```

Without replay, a new model run could not distinguish contract improvement from ordinary model-output variation.

### Lesson

When experimental outputs are preserved, offline replay is a high-value way to test representation/scoring changes without confounding them with new inference behavior.

---

## 8. Experiment invocation bug — direct script execution broke package imports

The first replay command was run as:

```text
python experiments/step6_support_drop_contract_v2_replay.py
```

It failed with:

```text
ModuleNotFoundError: No module named 'experiments'
```

### Root cause

Executing a file by path placed the `experiments/` directory, rather than the repository root, at the relevant import boundary. Imports such as:

```python
from experiments.step6_support_drop_contract_v2 import ...
```

could not resolve as expected.

### Fix

Use Python module execution:

```text
python -m experiments.step6_support_drop_contract_v2_replay
```

Later runners that need to be executable from `tools/` were made self-contained or explicitly launched child modules with `-m`.

### Lesson

Repository package/import topology is part of executable behavior. A passing unit test does not prove that an operator-facing command uses the correct import root.

---

## 9. Evidence persistence problem — `/tmp` was useful but not durable

Early smoke/evaluation JSON was written under `/tmp`.

This was appropriate for disposable experiment output, but the scored Step 6 evidence became decision-relevant and needed durable repository provenance.

### Fix

Important evidence was copied/committed under:

```text
working-memory/evidence/2026-08-03-step6d/
```

Later live-v2 evaluation and assessment defaulted directly to durable evidence paths in the checkout.

### Lesson

Transient output is appropriate during exploration. Once an output supports a consequential decision, it needs a durable evidence owner and immutable Git history.

---

## 10. Contract-v2 live evaluation — 24/25 strict, 25/25 safety

The actual v2 model-facing schema was then evaluated live with the same model deployment and no retries.

### Result

```text
strict_oracle_passed: 24
strict_oracle_failed: 1
adoption_safety_passed: 25
adoption_safety_failed: 0
```

### Important change in raised-minimum behavior

Unlike the historical v1 outputs, all three live-v2 raised-minimum trials correctly returned:

```text
unresolved
→ candidate_unresolved
```

The v2 prompt/contract therefore improved not only representation coherence but also the model's behavior on that boundary.

### Single remaining strict miss

`ambiguous_support_wording` returned:

```text
no_relevant_claim
```

instead of strict-oracle:

```text
unresolved
```

There were zero candidates and no grounded claim, so downstream target-Python activation still stopped.

### Why two metrics were retained

The strict oracle remained unchanged to avoid moving the goalposts.

A separate adoption-safety projection asked the product-relevant question:

- are positive claims exactly correct and grounded?
- do negative/ambiguous cases avoid producing a grounded support-drop claim?

This preserved both diagnostic truth and product-safety meaning.

### Lesson

A strict semantic metric and a downstream safety metric can legitimately differ, but they must both remain visible. A looser metric must never rewrite or hide the original oracle.

---

## 11. Repeat-consistency scoring bug — free-text detail was treated as semantic identity

The first live-v2 summary reported the raised-minimum critical repeat as inconsistent, even though all three trials had:

```text
candidate state = unresolved
trust state = candidate_unresolved
zero candidates
```

### Root cause

The repeat signature serialized the full candidate result, including free-text explanatory `detail`. The model phrased the same explanation differently across runs.

### Fix

A deterministic post-run assessment introduced a **material trusted-outcome signature** that compares:

- candidate state;
- candidate identities;
- trusted result kind/state;
- trusted Python line/release when grounded;
- adoption-safety result;

and deliberately excludes explanatory prose from identity.

### Result

All five critical repeated cases became materially consistent.

### Lesson

Reproducibility must be defined at the level of behavior that matters. Byte-identical explanatory prose is not required when the domain state and trusted evidence are identical.

---

## 12. Instructor/Pydantic discussion — useful tool, wrong time to introduce it

Instructor was considered during Step 6 because it can provide Pydantic-backed structured outputs, validation feedback, and retry loops.

### Why it was deferred

UpgradePilot already had:

```text
LM Studio strict JSON Schema
+ deterministic mapping
+ exact line reconstruction
+ Step 2 validation
```

The principal failures were contract-design and semantic-evaluation issues, not absence of schema tooling.

Automatic validation retries would also have changed the research question from:

```text
How does this deployment behave on first pass?
```

to:

```text
How does model + validation feedback + retry behave?
```

That could hide the very failures Step 6 needed to observe.

### Decision

No Instructor/Pydantic dependency was added. Direct `requests` remains the adopted baseline. Instructor can be evaluated later only as an explicit adapter-maintainability or correction-loop experiment.

### Lesson

A framework should not be introduced merely because it can repair symptoms. First determine whether the problem is transport, representation, semantics, grounding, or orchestration.

---

## 13. LM Studio Gemma chat-template warning

LM Studio repeatedly logged:

```text
detected an outdated gemma4 chat template,
applying compatibility workarounds.
Consider updating to the official template.
```

### Handling

The warning was recorded but the deployment/template was not changed in the middle of scoring.

### Why

Changing the chat template would change the evaluated deployment and invalidate direct comparison with the earlier smoke/evaluation evidence.

### Ongoing implication

Any future template update is a deployment change and must trigger re-evaluation against the frozen corpus/adoption gate.

### Lesson

A warning can be a reproducibility caveat without being an immediate failure. Changing an experimental variable to silence a warning can make evidence less interpretable.

---

## 14. Test-count progression and what it means

Observed full-suite checkpoints during this work included:

```text
320 tests in 0.057s — OK
322 tests in 0.062s — OK
332 tests in 0.059s — OK
336 tests in 0.059s — OK
339 tests in 0.062s — OK
```

These counts prove deterministic behavior of the code/tests present at those points. They do not prove model semantics by themselves and do not establish user mastery.

---

## 15. Final adoption-gate result

The deterministic post-run assessment established:

```text
1. every accepted candidate survives Step 2                 true
2. no wrong direction on frozen controls                    true
3. no negated/future drop admitted                          true
4. no unstated line inferred from raised minimum            true
5. S001 correct and grounded                                true
6. ambiguous/no-claim cases abstain                         true
7. critical trusted outcomes materially consistent          true
8. latency recorded for all calls                           true
9. material improvement over rejected local baseline        true
10. deployment identity recorded                            true
```

Disposition:

```text
adopt_bounded_extractor
```

The user explicitly approved the bounded adoption after reviewing the evidence and architectural recommendation.

---

## 16. Important limitation discovered at the integration boundary

Step 6 validated bounded release text, including the exact S001 release section. The real authoritative tagged changelog acquired in Step 5 is approximately 17 KB and contains many releases.

Therefore Step 7 must not silently equate:

```text
bounded evaluated excerpt
```

with:

```text
entire upstream changelog
```

The next runtime integration must deterministically produce bounded source windows tied to trusted crossed-release structure before invoking the model.

This source-windowing layer may perform structural segmentation and identity preservation, but it must not itself decide that prose means `support_dropped`.

This is the main remaining engineering obligation between Step 6 experimental adoption and normal-runtime activation.

---

## Durable conclusions

1. **Model output is not evidence authority.** Source authority is selected before inference.
2. **Exact grounding is deterministic.** The model selects line identity; code recovers exact text and offsets.
3. **Do not ask a model to predict derivable state.** Contract v2 removed duplicated positive-state encoding.
4. **No automatic retry in baseline scoring.** First-pass behavior must remain observable.
5. **Strict semantics and product safety are separate metrics.** Neither should hide the other.
6. **Material repeatability excludes prose variation.** Compare domain/trust identity, not wording.
7. **Experiment execution paths matter.** `python -m` versus direct script execution can change imports.
8. **Localhost is still a network boundary.** Proxy environment can break loopback.
9. **Transient evidence becomes durable when it informs architecture.** Preserve decision-grade JSON.
10. **Passing Step 6 does not authorize whole-changelog prompting.** Runtime source-windowing still needs proof.

## Evidence references

Durable JSON:

```text
working-memory/evidence/2026-08-03-step6d/support-drop-evaluation.json
working-memory/evidence/2026-08-03-step6d/contract-v2-replay.json
working-memory/evidence/2026-08-03-step6d/contract-v2-live-evaluation.json
working-memory/evidence/2026-08-03-step6d/contract-v2-adoption-assessment.json
```

Architecture decision:

```text
docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md
```

Step 6 experiment/support code and tests retain the executable details of the evaluation path.
