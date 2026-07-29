# UpgradePilot Case Selection and Coverage Matrix

**Status:** Proposal-support decision aid — unadmitted and non-controlling  
**Owner:** Ali Rajabi  
**Recorded:** 2026-07-29  
**Scope:** Compare real, real-derived, synthetic, mocked, and generated case candidates for future `product-simulation/` work  
**Authority:** None. Scores do not select a case, activate a responsibility, change governance, or authorize implementation or target-repository actions.

## 1. Purpose

This matrix turns the case-program proposal, hybrid amendment, and prevalence catalog into a practical selection method.

It is designed to prevent three failure modes:

1. choosing a case only because it is easy to find;
2. choosing a rare or technically impressive case that has little product value;
3. creating a synthetic case that passes because it encodes the expected answer rather than testing a real responsibility.

The matrix should answer:

> Which case or controlled example gives UpgradePilot the most discriminating, reusable, and trustworthy evidence for the least unnecessary cost and ceremony?

## 2. Inputs

Use this matrix with:

- [`FULL_PROJECT_CASE_PROGRAM_PROPOSAL.md`](FULL_PROJECT_CASE_PROGRAM_PROPOSAL.md);
- [`FULL_PROJECT_CASE_PROGRAM_PROPOSAL_AMENDMENT_01_HYBRID_CASE_MODEL.md`](FULL_PROJECT_CASE_PROGRAM_PROPOSAL_AMENDMENT_01_HYBRID_CASE_MODEL.md);
- [`REAL_WORLD_SCENARIO_PREVALENCE_CATALOG.md`](REAL_WORLD_SCENARIO_PREVALENCE_CATALOG.md);
- existing S001–S005 cases and accepted synthesis;
- the route responsibilities and project boundaries;
- actual candidate evidence, not only imagined scenario descriptions.

## 3. Selection principles

### 3.1 Prevalence is not priority

A common case may deserve normal regression coverage but add no new discovery value. A rare case may deserve priority when it controls a severe product or security risk.

### 3.2 Current implementation is one factor

Near-term usefulness matters, but the case-selection horizon is the full production-oriented product.

### 3.3 Realism and control are separate dimensions

- real cases provide external realism;
- real-derived variants provide realistic isolation;
- synthetic cases provide controlled rare-condition coverage;
- generated cases provide systematic invariant coverage.

### 3.4 Written reasoning controls the result

Scores expose trade-offs. They do not replace judgment, evidence inspection, or Ali's decision.

### 3.5 Admit one bounded question

A candidate should normally be admitted for one central uncertainty even when it later supports several route stages.

## 4. Mandatory admission gates

Do not score a candidate as admissible until every mandatory gate has an adequate answer.

| Gate | Pass condition | Failure result |
|---|---|---|
| Named uncertainty | One precise product, evaluation, failure, recovery, or security question | Keep as an idea; do not admit |
| Existing-case gap | S001–S005 and synthesis cannot answer the question adequately | Reject as duplicate or use as regression only |
| Product consequence | Result can change behavior, contract, method, acceptance evidence, action, explanation, or stopping | Reject as decorative |
| Safe boundary | No unauthorized mutation, unsafe execution, credential exposure, or unnecessary private data | Stop or redesign |
| Evidence feasibility | Required identity and evidence can be preserved or simulated credibly | Reserve pending evidence |
| Honest negative result | A failed hypothesis still produces a useful bounded finding | Reject fragile showcase case |
| Stop condition | Investigation has an explicit sufficiency, failure, cost, or authorization stop | Define before admission |
| Claim boundary | What the case may and may not prove is explicit | Do not admit until clarified |
| Correct case form | Full real, multi-snapshot, real-derived, synthetic, mock/fake, or generated form is justified | Redesign proportionally |
| Synthetic realism basis | For artificial evidence, the condition is grounded in a real observation, official contract, or credible failure model | Reject imagination-only scenario |

## 5. Scoring scale

Each dimension uses a 0–5 score.

| Score | Meaning |
|---:|---|
| 0 | None, unsupported, or actively harmful |
| 1 | Very weak |
| 2 | Limited |
| 3 | Material |
| 4 | Strong |
| 5 | Exceptional or central |

Do not use half-points unless two candidates remain genuinely tied after written comparison.

## 6. Positive-value dimensions

| Code | Dimension | Weight | Scoring question |
|---|---|---:|---|
| `MR` | Material product or security risk | 3 | Could incorrect handling cause a wrong action, unsupported claim, stale decision, lost evidence, unsafe operation, or serious trust failure? |
| `RL` | Cross-stage route leverage | 3 | How many meaningful B2, B3, B4, B5, X1, or C1 responsibilities can reuse the evidence? |
| `DN` | Decision or explanation novelty | 2 | Does the case add a missing action, abstention, defer, supersession, authority, or explanation transition? |
| `NT` | Near-term usefulness | 2 | Does it clarify a responsibility close to current implementation without redefining the workspace around that increment? |
| `ER` | Evaluation reuse | 2 | Can it become a regression, replay, baseline comparison, property seed, temporal test, adversarial host, or held-out example? |
| `EF` | Evidence feasibility | 2 | Can exact identity, sources, and expected observations be preserved lawfully and reproducibly? |
| `RV` | Realism value | 2 | Does it expose genuine public-source, repository, package, CI, or maintainer behavior that artificial cases may miss? |
| `IC` | Isolation and control value | 2 | Can material variables be controlled well enough to diagnose behavior and compare counterfactuals? |
| `PR` | Prevalence relevance | 1 | Is this important normal-path or recurring behavior that representative coverage should include? |
| `LO` | Learning and ownership value | 1 | Does it support meaningful prediction, modification, testing, diagnosis, and explanation by Ali? |

### Positive subtotal

```text
positive =
  3×MR
+ 3×RL
+ 2×DN
+ 2×NT
+ 2×ER
+ 2×EF
+ 2×RV
+ 2×IC
+ 1×PR
+ 1×LO
```

Maximum positive subtotal: 100.

## 7. Penalty dimensions

| Code | Penalty | Weight | Scoring question |
|---|---|---:|---|
| `DP` | Duplication | 3 | How much of the question is already answered by S001–S005, synthesis, active tests, or another candidate? |
| `AC` | Acquisition and preservation cost | 2 | How expensive, fragile, rate-limited, ephemeral, or manual is the evidence? |
| `CB` | Ceremony burden | 1 | How much process or artifact overhead is required relative to capability unlocked? |
| `OA` | Oracle ambiguity | 2 | How uncertain is the expected result or recommendation, especially when authored by the same people designing the method? |
| `VD` | External-validation debt | 1 | How much important behavior remains untested against real systems after the case? |
| `SC` | Speculative complexity | 2 | Does the case pull in unadmitted architecture, universalization, or disconnected technology? |

### Penalty subtotal

```text
penalty =
  3×DP
+ 2×AC
+ 1×CB
+ 2×OA
+ 1×VD
+ 2×SC
```

Maximum penalty subtotal: 55.

## 8. Comparative score

```text
comparative score = positive − penalty
```

Suggested interpretation:

| Score | Interpretation |
|---:|---|
| 70–100 | Strong admission candidate if gates pass |
| 55–69 | Promising; compare with alternatives or narrow scope |
| 40–54 | Reserve, redesign, or use as a smaller variant/caselet |
| 20–39 | Low priority or regression-only |
| Below 20 | Reject unless a mandatory security obligation overrides the score |

These thresholds are provisional. A high score cannot override a failed mandatory gate. A severe security invariant may justify a small synthetic caselet even when prevalence and realism scores are low.

## 9. Case-form decision matrix

| Material question | Preferred form | Why | Required external validation |
|---|---|---|---|
| Does this condition genuinely occur and matter to a maintainer? | Untouched real public case | Real context and action are central | Additional cases before prevalence or generality claims |
| What changes when one evidence variable is unavailable, stale, or contradictory? | Real-derived controlled variant | Keeps real structure while isolating the variable | Live source behavior if integration semantics are claimed |
| How should multiple revisions and temporal states relate? | Synthetic repository or multi-snapshot case | Exact timing and history can be controlled | One or more real rebased/superseded PRs |
| How should a client behave across retries, pagination, timeouts, and partial success? | Mock or fake service | Request sequence and failure location are controlled | Bounded live integration and captured real responses |
| Does a deterministic invariant hold over combinations and orderings? | Generated/property-based cases | Systematic variation and failure shrinking | Representative real fixtures for domain realism |
| Does repository-specific code usage change the action? | Untouched real case, optionally with controlled check outcomes | Target context and maintainer usefulness are central | Additional repositories before generality claims |
| Can adversarial content cross a trust boundary? | Synthetic or generated caselet | Safe, precise, and repeatable | Real benign content integration; never publish malicious content externally |
| Is an expected recommendation useful or correct? | Real cases with transparent adjudication | Synthetic expected labels are too circular | Multiple reviewers/cases and explicit disagreement handling |
| Can a run recover from interruption without duplication? | Workflow-level synthetic case | Precise crash point and state can be controlled | Real process/runtime verification after implementation exists |
| Does PyPI/GitHub identity reconcile live? | Real integration case | A fake cannot prove external identity behavior | Captured fixtures for regression |

## 10. Coverage notation

Use the following markers in cross-stage matrices:

| Marker | Meaning |
|---|---|
| `P` | Primary evidence for the stage responsibility |
| `S` | Supporting or reusable evidence |
| `L` | Later evaluation value after the responsibility is implemented |
| `—` | Little direct value |

## 11. Scenario-family route coverage

| Scenario family | B2 vertical slice | B3 acquisition/replay | B4 context/decision | B5 persistence/evaluation | X1 experiments | C1 hardening/ownership |
|---|---:|---:|---:|---:|---:|---:|
| Ordinary single direct update with relevant green CI | P | S | S | L | L | S |
| Authority degradation and abstention | P | P | P | S | L | P |
| Changed head, rebase, and supersession | S | P | S | P | L | P |
| Direct behavior impact and missing coverage | S | S | P | P | P | P |
| Decision-time versus retrospective evidence | — | S | S | P | P | P |
| Artifact provenance or yanked release | S | P | P | P | P | P |
| Partial acquisition, rate limit, and retry | S | P | S | P | L | P |
| Dynamic/plugin usage and static-analysis limits | — | S | P | P | P | S |
| Adversarial evidence and prompt injection | S | P | P | P | P | P |
| Property-based decision laws | S | S | P | P | P | P |
| Worker interruption and idempotent recovery | — | P | — | P | P | P |
| Grouped update and failure attribution | S | S | P | P | P | P |

## 12. Coverage-gap urgency

Use urgency independently from prevalence.

| Urgency | Meaning |
|---|---|
| `U0` | Existing evidence is adequate; no new discovery case needed |
| `U1` | Useful later; preserve candidate only |
| `U2` | Material gap before a later stage can be accepted |
| `U3` | High-value gap that affects several stages or a central claim |
| `U4` | Immediate safety, trust, or correctness blocker |

Initial gap view:

| Gap | Urgency | Reason |
|---|---:|---|
| Honest defer/abstain under insufficient authority | U3 | Missing central action class and multi-stage relevance |
| Changed-head stale-evidence lifecycle | U3 | Revision identity exists, but complete supersession/replay evidence is weak |
| Direct behavior impact with targeted-check transition | U3 | Central product-value path and later method-evaluation host |
| Robust partial acquisition and retry variants | U2 | B3 and hardening need deterministic failure coverage |
| Decision-time versus retrospective comparison | U2 | Required for honest evaluation and leakage control |
| Adversarial content trust boundary | U2 now; U3 when semantic automation is admitted | Important but should attach to a real extraction responsibility |
| Persistent recovery after worker interruption | U1 now; U3 after persistence/run-state admission | Premature before the owning behavior exists |
| Private registry and private repository behavior | U1 | Outside initial public boundary |
| Kubernetes, multi-cloud, or multi-agent cases | U0 for current case program | No demonstrated product need yet |

## 13. Initial seeded candidate comparison

These rows compare case families, not actual selected PRs. Scores are provisional estimates and must be replaced with evidence-backed candidate scores.

| Candidate | Proposed form | MR | RL | DN | NT | ER | EF | RV | IC | PR | LO | DP | AC | CB | OA | VD | SC | Indicative result | Recommendation |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `FAM-A` Authority degradation and abstention | Real host + controlled variants | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 4 | 3 | 4 | 1 | 3 | 2 | 3 | 2 | 1 | 77 | Strong first-wave candidate |
| `FAM-B` Changed head and supersession | Synthetic repository + real validation | 5 | 5 | 5 | 3 | 5 | 5 | 3 | 5 | 3 | 5 | 1 | 2 | 2 | 2 | 3 | 1 | 78 | Strong first-wave candidate |
| `FAM-C` Direct behavior impact and targeted checks | Untouched real case + counterfactual variants | 5 | 5 | 5 | 3 | 5 | 3 | 5 | 3 | 4 | 5 | 2 | 4 | 3 | 4 | 2 | 2 | 66 | Strong but candidate acquisition is harder |
| `FAM-D` Decision-time versus retrospective | Real-derived temporal case | 4 | 5 | 4 | 1 | 5 | 3 | 4 | 4 | 2 | 4 | 1 | 4 | 3 | 3 | 3 | 2 | 58 | Reserve after first lifecycle case |
| `FAM-E` Yanked/provenance regression | Real host or temporal synthetic case | 5 | 4 | 4 | 2 | 4 | 2 | 4 | 4 | 1 | 4 | 1 | 4 | 3 | 3 | 3 | 2 | 52 | Valuable later or if unusually strong real evidence appears |
| `FAM-F` Prompt-injection corpus | Synthetic/generated caselets | 5 | 4 | 3 | 1 | 5 | 5 | 1 | 5 | 1 | 4 | 0 | 1 | 1 | 1 | 4 | 1 | 64 | Attach when semantic/LLM responsibility exists; do not make first standalone full case |
| `FAM-G` Worker interruption recovery | Workflow-level synthetic case | 5 | 4 | 4 | 0 | 5 | 5 | 1 | 5 | 1 | 5 | 0 | 2 | 3 | 1 | 5 | 4 | 49 | Defer until run-state and persistence are admitted |
| `FAM-H` Ordinary patch update with green CI | Untouched real case | 2 | 2 | 1 | 4 | 3 | 5 | 5 | 2 | 5 | 3 | 5 | 1 | 2 | 2 | 1 | 0 | 32 | Regression/normal-path coverage; no new full case needed |

### 13.1 Interpretation

- `FAM-A` and `FAM-B` remain the strongest first additions because they fill missing product responsibilities and support many later stages.
- `FAM-C` has exceptional product value but requires a carefully selected real repository and credible target behavior evidence.
- `FAM-F` scores well as a small evaluation asset, not as a standalone narrative case.
- `FAM-G` demonstrates why a technically impressive scenario can still be premature.
- `FAM-H` demonstrates why prevalence alone should not select a new case.

## 14. Actual candidate screening template

Copy one row per candidate during lightweight screening.

| Field | Candidate value |
|---|---|
| Candidate ID | `CAND-___` |
| Exact repository and PR |  |
| Dependency and old/new proposal |  |
| Scenario catalog IDs |  |
| Prevalence band and confidence |  |
| Named uncertainty |  |
| Existing-case gap |  |
| Material product consequence |  |
| Proposed case form |  |
| Real and synthetic components |  |
| Evidence sources |  |
| Prospective feasibility |  |
| Baseline expectation |  |
| Possible decision/explanation transitions |  |
| Useful negative result |  |
| Security and execution boundary |  |
| Evidence durability |  |
| Stop condition |  |
| External validation debt |  |
| Mandatory gates passed? |  |
| Positive and penalty scores |  |
| Admission recommendation | Admit / reserve / reject / screen further |

## 15. Synthetic variant template

Use this when a real host case is mutated.

| Field | Variant value |
|---|---|
| Variant ID | `VAR-___` |
| Host case and exact snapshot |  |
| Real evidence retained |  |
| Exact mutation |  |
| Variables held constant |  |
| Realism basis | Official contract / observed failure / existing case / captured response |
| Fidelity layer | Data / service / repository / workflow / temporal |
| Expected behavior authority | Invariant / accepted policy / source contract / hypothesis |
| Permitted claim |  |
| Claim prohibited |  |
| External validation required |  |
| Stop condition |  |

## 16. Candidate comparison table

After screening several candidates, use this compact table for Ali's decision.

| Candidate | Named uncertainty | Case form | Prevalence | Urgency | Score | Strongest evidence | Main risk | External validation debt | Recommendation |
|---|---|---|---|---:|---:|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |

Do not admit several cases merely because several candidates score well. Select the smallest sequence that answers the most consequential uncertainties.

## 17. Recommended initial sequence

```text
1. preserve proposal, hybrid amendment, prevalence catalog, and matrix
2. decide whether the case-program direction is accepted in principle
3. screen real candidates for authority degradation and direct behavior impact
4. design the minimum synthetic changed-head repository concept
5. compare actual candidate evidence and costs
6. admit only one bounded case or synthetic responsibility
7. freeze pedigree, baseline, permitted claim, and stop condition
8. investigate and preserve material checkpoints
9. validate later against real behavior where the selected form creates external-validation debt
```

## 18. Matrix revision rules

Revise the matrix only when:

- real candidate work shows an important dimension or penalty is missing;
- scores consistently conflict with defensible qualitative decisions;
- a route responsibility changes;
- a versioned corpus provides measured prevalence or evaluation evidence;
- synthetic validation debt proves larger or smaller than expected;
- case artifact cost becomes demonstrably disproportionate.

Do not tune weights merely to make a preferred candidate win.

## 19. Summary

```text
mandatory gates prevent invalid admission
+ prevalence catalog supplies occurrence context
+ positive dimensions measure product and evaluation value
− penalties expose duplication, cost, ambiguity, and speculation
+ case-form matrix chooses the least artificial adequate method
→ written comparison
→ Ali selects one bounded case
```

The matrix exists to make case selection disciplined without turning it into false numerical certainty.