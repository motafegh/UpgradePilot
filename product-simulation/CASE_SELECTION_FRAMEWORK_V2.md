# Product Simulation Case Selection Framework V2

**Status:** Non-controlling discovery/evaluation aid  
**Owner:** Ali Rajabi  
**Scope:** Select and shape future real, real-derived, synthetic, mocked, or generated product-simulation work after the 2026-08-06 recalibration

## 1. Purpose

This framework helps answer:

> Which case or controlled example is most likely to produce new, discriminating evidence
> about UpgradePilot's product behavior, reasoning model, failure boundaries, evaluation needs,
> or future implementation responsibilities without unnecessary ceremony?

It is not an implementation roadmap and is not subordinate to the current implementation
slice or selected project plan. It should remain informed by current product/design evidence
while allowing cases to challenge or extend it.

## 2. Selection philosophy

A strong case is not necessarily:

- the most common case;
- the most technically difficult case;
- the case closest to current source code;
- the case with the most artifacts;
- the case that changes the final action;
- the case with the highest apparent risk.

A strong case is one that can **discriminate among materially different product
interpretations or behaviors**.

Examples:

- whether an upstream change actually activates on the target;
- whether existing CI covers the affected responsibility;
- whether one targeted check can close an unresolved question;
- whether deeper investigation adds any value;
- whether evidence degradation should produce unresolved/abstention rather than a guess;
- whether later evidence must supersede an earlier result;
- whether a failure belongs to the dependency update or another cause.

## 3. Mandatory admission gates

Do not admit a substantial case until these questions have credible answers.

| Gate | Required answer |
|---|---|
| `Q` — Named question | What exact discovery/evaluation question are we testing? |
| `G` — Existing-evidence gap | Why do S001–S005, current implementation/tests, and already-screened candidates not answer it adequately? |
| `C` — Consequence | What could this change about product understanding, evaluation, failure handling, explanation, stopping, or future implementation? |
| `E` — Evidence feasibility | Can exact identity and material evidence be obtained or simulated credibly? |
| `S` — Safe boundary | Can the case be investigated without unauthorized target mutation, unsafe execution, credential exposure, or unnecessary private data? |
| `N` — Negative result | If the preferred hypothesis fails, is the result still useful? |
| `L` — Claim limit | What may the case establish, and what must it not establish? |
| `T` — Stop condition | When is enough evidence enough for this question? |
| `F` — Case form | Why is real, real-derived, synthetic, mock/fake, or generated evidence the right level? |

A case may explore a question not named by `MEMORY.md` or current plans. Ali's authorization of
the product-simulation program is sufficient when these gates pass.

## 4. Recalibrated comparative dimensions

After the gates pass, compare candidates on these dimensions. Use `0–3` only when numerical
comparison helps; written reasoning controls the result.

| Code | Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|
| `IM` | Impact-model novelty | Already covered | Minor variant | Materially different | New central impact/problem shape |
| `AD` | Activation/applicability discrimination | None | Weak | Clear | Case strongly separates signal from target applicability |
| `IV` | Investigation information value | No useful next check | Generic work | Specific useful investigation | One/few checks clearly discriminate material alternatives |
| `ST` | Sufficiency/stopping value | None | Incidental | Useful | Case strongly teaches when to stop or remain unresolved |
| `RV` | Realism/external validity | Artificial only | Real-inspired | Real structure | Untouched real context is central |
| `CV` | Controlled-variant reuse | Hard to isolate | Limited | Several useful variants | Strong host for systematic counterfactuals |
| `EH` | Evaluation-horizon reuse | One-off | Narrow regression | Multiple future uses | Strong corpus/replay/property/temporal/security host |
| `GL` | Generalization challenge | Fixture-like | Similar to existing | Changed package/repo reasoning | Strong test against hidden case-specific assumptions |
| `LO` | Learning/ownership value | Low | Exposure | Meaningful explanation/testing | Strong prediction/diagnosis/transfer opportunity |

### Penalties

Use the same `0–3` scale where useful.

| Code | Penalty | Meaning |
|---|---|---|
| `DP` | Duplication | Existing evidence already answers most of the question |
| `OA` | Oracle ambiguity/circularity | Expected result depends heavily on designer preference or synthetic assumptions |
| `AC` | Acquisition fragility/cost | Evidence is ephemeral, inaccessible, expensive, or difficult to preserve |
| `SC` | Speculative complexity | Case drags in many unproven responsibilities or technologies at once |
| `MX` | Mixed-variable overload | Too many material unknowns prevent learning which one caused the result |
| `CB` | Ceremony burden | Documentation/process cost exceeds likely information gain |

Do not mechanically sum scores unless two or more candidates remain genuinely hard to
separate after written comparison.

## 5. Preferred case forms

### Untouched real public case

Prefer when the question depends on:

- whether a condition actually occurs;
- real repository irregularity;
- target usage/configuration;
- maintainer context;
- real CI/test relationships;
- external integration behavior;
- recommendation usefulness.

### Real-derived controlled variant

Prefer when:

- a real case already supplies the realistic host;
- one variable should be changed to isolate causality;
- counterfactual comparison is more useful than finding another unrelated PR.

Examples:

```text
real target usage present
→ controlled variant removes usage

real CI covers affected path
→ controlled variant marks that test skipped

real upstream statement is coherent
→ controlled variant introduces contradictory authority
```

### Synthetic repository/workflow case

Prefer when exact control of timing/state is the point:

- changed PR head;
- stale evidence;
- supersession;
- interruption/recovery;
- duplicate retries;
- multi-snapshot history;
- controlled repository-policy contrasts.

Anchor the synthetic condition in real observations or official behavior.

### Mock/fake external service

Prefer for:

- rate limits;
- timeout/partial acquisition;
- pagination failure;
- malformed responses;
- changing remote state;
- retry/idempotency branches.

Use real live validation before claiming external-service correctness.

### Generated/property-based cases

Prefer for:

- evidence ordering;
- missing/conflicting-state combinations;
- invariant enforcement;
- state-machine transitions;
- deterministic decision laws;
- shrinking complex failures.

Use real fixtures to preserve domain realism.

## 6. Current discovery priorities

These priorities are derived from the 2026-08-06 coverage rebase. They are not a fixed
roadmap and may change when the progressive design discussion or new cases reveal stronger
questions.

### Priority 1 — Real API/runtime behavior impact with target usage and incomplete coverage

Ideal shape:

```text
upstream behavior/API change
→ exact activation condition
→ target definitely uses affected path
→ available CI/test evidence does not clearly cover it
→ one specific check can discriminate compatibility/relevance
```

Why high value:

- materially different from the implemented Python-support slice;
- extends S002 with stronger real behavior evidence;
- exercises impact → activation → usage → coverage → investigation;
- gives a natural host for pass/fail targeted-check counterfactuals.

### Priority 2 — Activation/applicability contrast in another impact family

Ideal shape:

```text
same or similar upstream concern
+ target A activates condition
+ target B does not
```

or one real target plus a controlled variant.

Why high value:

- tests whether the S001/S005 reasoning pattern generalizes beyond Python support and pytest
  configuration;
- helps distinguish reusable reasoning from case-specific rules.

### Priority 3 — Targeted-check discrimination

Ideal shape:

```text
material open question
→ one concrete check
→ pass and fail imply materially different conclusions
```

Why high value:

- tests whether UpgradePilot can choose *what to learn next* rather than merely request more
  testing;
- provides an evaluation target for information value and stopping.

### Priority 4 — Sufficiency / deliberate non-investigation

Ideal shape:

- credible initial evidence;
- no activated material concern after minimal authority confirmation;
- several tempting but low-information investigations available;
- clear reason to stop.

S004 already provides one strong example. A second different-domain example would test
reusability without turning stopping into a pytest-specific rule.

### Priority 5 — Temporal/yanked/supersession sequence

Retained anchor:

`laramies/theHarvester#1735 → #1740`, Requests `2.31.0 → 2.32.0 → 2.32.2`.

Why retained:

- real corrective sequence;
- yanked upstream releases;
- decision-time versus later evidence;
- replay/supersession/persistence value;
- future temporal evaluation host.

Why not automatically first:

- current design uncertainty is more directly about impact/applicability/investigation than
  persistence/temporal state;
- the exact yank-visibility timeline remains partially unresolved.

### Priority 6 — Controlled robustness/security variants

Attach to real anchors where possible:

- missing upstream evidence;
- contradictory source authority;
- prompt-like/adversarial content;
- changed head;
- duplicate rerun;
- partial acquisition;
- interrupted workflow;
- stale report reference.

These often belong as compact evaluation assets rather than narrative full cases.

## 7. Case packet before full execution

Before a full new case is admitted, capture a compact screening packet:

```text
candidate identity
question
existing-case gap
impact/problem shape
activation-condition hypothesis
expected target surface
available coverage/evidence
possible discriminating investigation
case form
claim limits
stop condition
negative-result value
```

Do not create a large scenario bundle before the candidate passes this screen.

## 8. Real-derived variant design

When deriving variants from a real anchor, state explicitly:

```yaml
real_anchor: <case identity>
changed_variable: <one named condition>
unchanged_real_structure:
  - <identity/evidence retained>
expected_discrimination:
  - <what conclusion or behavior should differ if the variable matters>
claim_limit:
  - <what synthetic result cannot prove>
```

Prefer one material changed variable. Multiple changes require a reason because they reduce
causal interpretability.

## 9. Evaluation roles

Each case/variant should state one or more roles:

- `product_discovery`
- `integration_reality_check`
- `impact_model_contrast`
- `applicability_contrast`
- `targeted_investigation_contrast`
- `stopping_sufficiency`
- `failure_attribution`
- `temporal_supersession`
- `failure_recovery`
- `security_trust_boundary`
- `regression`
- `method_comparison`
- `property_invariant`

A case may serve several roles, but one role should normally be primary.

## 10. Rejection signals

Reject, reserve, or reduce a candidate when:

- the question is already answered by S001–S005 or active product tests;
- no evidence can distinguish the competing interpretations;
- the expected answer is simply the designer's preferred recommendation;
- the target surface is speculative rather than evidenced;
- the case requires many unrelated technologies/responsibilities at once;
- a simpler real-derived variant would answer the question;
- evidence cannot be preserved honestly;
- the only value is adding another action label;
- the case is interesting but has no plausible product/evaluation consequence;
- stopping cannot be defined.

## 11. Relationship to historical artifacts

Keep these roles distinct:

- S001–S005 — accepted historical discovery evidence;
- `CASE_CANDIDATE_SCREENING_01.md` — July 31 candidate-screening evidence;
- old case-program proposal branch — useful historical proposal material, not current branch
  authority;
- this V2 framework — current workspace selection aid, non-controlling to the wider product;
- progressive decision-model working record — current design context, not a ceiling on
  simulation discovery.

## 12. Selection principle

Use the **least artificial, least duplicative, most discriminating** case that can answer a
material question safely and reproducibly.

When two candidates are otherwise comparable, prefer the one that makes it easier to explain:

1. what could happen;
2. what condition makes it matter;
3. how the target proves or fails to prove that condition;
4. what evidence/check would change our understanding;
5. when to stop;
6. what remains unknown.
