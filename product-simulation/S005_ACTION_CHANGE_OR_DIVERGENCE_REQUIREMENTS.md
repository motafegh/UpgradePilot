# S005 Action-Change or Dependency/PR-Divergence Requirements

**Status:** Controlling S005 candidate and execution requirements  
**Date:** 2026-07-23  
**Route position:** Final required D1 contrast before focused synthesis and possible B1 entry  
**Parent route:** [`../plans/UPGRADEPILOT_90_DAY_PLAN.md`](../plans/UPGRADEPILOT_90_DAY_PLAN.md)

## 1. Purpose

S005 must test a decision contrast not covered by S001–S004.

Preferred outcome classes, in order:

1. **Baseline wrong action:** joined repository, upstream, dependency-path, or CI evidence changes the transparent baseline's broad action.
2. **Dependency/PR divergence:** the dependency update assessment and current PR action differ materially—for example, the update appears acceptable but an unrelated or pre-existing failure still blocks the PR.

The candidate must not be selected or interpreted merely to manufacture either result. If the strongest qualifying case ends unresolved, preserve that result and reconsider D1 evidence rather than forcing a classification.

## 2. Product-boundary preference

Prefer a public Python repository and a real Dependabot pip/uv/poetry dependency-update PR so S005 directly informs the supported charter boundary.

A cross-ecosystem case may be used only when:

- no sufficiently accessible Python case is available after documented screening;
- the tested responsibility is clearly transferable;
- the scenario remains labeled discovery evidence rather than supported-scope expansion.

## 3. Candidate admission criteria

A candidate must provide:

- exact repository, PR, base, head, dependency, and changed-file identity;
- enough retained public CI detail to identify workflow, run, job, step, command, revision, and result;
- a baseline result that can be frozen before full evidence;
- at least one material evidence source hidden from the baseline that could plausibly change the broad action or separate dependency assessment from PR action;
- credible competing explanations where a failure is involved;
- enough comparison evidence to distinguish update-caused, pre-existing, unrelated, flaky, environmental, mixed, or unresolved causes at a justified depth;
- a bounded public-safe investigation surface;
- a credible stopping or abstention point.

A candidate is stronger when it has one or more of:

- base/head or before/after check comparison;
- unchanged-head reruns;
- adjacent same-base dependency PRs;
- known pre-existing main-branch failure;
- workflow/path/command evidence showing a failure is irrelevant to the dependency;
- repository usage or dependency-path evidence contradicting directness-based baseline caution;
- a target-specific compatibility break hidden by broad green CI;
- a major or caution-keyword update whose target path is demonstrably unaffected;
- a patch/minor green update whose relevant responsibility was not exercised and evidence supports a stronger action.

## 4. Rejection or deferral rules

Reject or defer a candidate when:

- exact case identity cannot be frozen;
- current CI cannot be tied to the proposed head;
- only overall color is available and command responsibility cannot be established;
- the apparent divergence depends only on historical merge or closure;
- no credible evidence can discriminate among causal explanations;
- the update is so broad or grouped that individual responsibility cannot be bounded;
- the case requires private credentials, unauthorized mutation, or unsafe untrusted-code execution;
- the result duplicates S001–S004 without testing the required contrast;
- the case is chosen only because its apparent outcome supports the thesis.

## 5. Prospective execution checkpoints

S005 must be prospective.

### Checkpoint 0 — Candidate screening

Preserve:

- candidate criteria;
- screened candidates;
- material rejection reasons;
- why the selected candidate is the strongest available contrast.

Do not assign a run ID before selection.

### Checkpoint 1 — Selected, frozen, and baseline executed

Create or update:

- scenario `README.md` and `CASE.md`;
- `RUN_MANIFEST.json`;
- `INVOCATION.json`;
- `CASE_IDENTITY.json`;
- initial `OPERATION_EVENTS.jsonl`;
- `BASELINE_RESULT.json` using only permitted inputs;
- initial `REVIEW_AND_OWNERSHIP.json`;
- explicit investigation questions and stop/switch conditions.

### Checkpoint 2 — Material contrast evidence acquired

Preserve:

- exact workflow/run/job/step/command evidence;
- dependency path and role evidence;
- comparison executions or main/base evidence;
- relevant upstream and repository sources;
- inaccessible, expired, conflicting, or failed methods;
- live competing explanations.

### Checkpoint 3 — Attribution or action-change assessment

Produce:

- findings that distinguish baseline-visible facts from action-changing evidence;
- causal classification or explicit unresolved state when failure is involved;
- separate dependency and PR decision dimensions when they genuinely differ;
- evidence for why a broader or weaker action is justified.

### Checkpoint 4 — Decision, reports, follow-up, and validation

Complete:

- bounded decision;
- machine and human reports;
- transition and new-run rules;
- review/ownership state;
- structural validation;
- baseline/full comparison;
- post-case synthesis and D1 gate assessment.

## 6. Conditional artifacts

### `CHECK_EXECUTIONS.jsonl`

Activate when the case contains material comparisons among:

- base and head;
- main and PR;
- attempts or reruns;
- matrix cells;
- local and CI executions;
- adjacent PRs.

Each record should preserve revision, workflow/run/job/step/command, responsibility, environment, conclusion, failure signature where applicable, source refs, and comparison relationships.

### `FAILURE_ATTRIBUTION.json`

Activate when failing evidence has more than one credible cause.

Preserve:

- candidate causes;
- supporting and contradicting evidence;
- comparison executions;
- current classification and support level;
- unresolved discriminating questions;
- superseded attribution states;
- effects on dependency assessment and PR action.

### Separate decision dimensions

Use these when the evidence supports distinct answers:

```text
dependency_update_assessment
repository_or_pr_action
```

Do not add the split merely because S003 trialed it. S005 should determine whether real divergence makes it necessary.

### Stopping evaluation

Activate a dedicated stopping/cost artifact only when cost, sufficiency, or overreach is materially part of S005. Otherwise preserve the stop condition through operations, decision, and follow-up.

## 7. Failure-attribution classifications

Where applicable, use:

- `update_caused`;
- `pre_existing`;
- `unrelated`;
- `flaky`;
- `environmental`;
- `mixed`;
- `unresolved`.

A red check alone is insufficient for any causal classification.

### Normally sufficient support for `update_caused`

At least one strong discriminating relationship such as:

- comparable base passes and head fails;
- reverting or isolating the update removes the failure;
- an explicit dependency constraint or changed API directly explains the failing command;
- equivalent same-base evidence materially rules out broader causes.

### Normally sufficient support for `pre_existing` or `unrelated`

Evidence such as:

- the same failure exists on base or current main;
- the failed command does not consume the changed dependency or path;
- a comparable update-independent execution reproduces the same failure;
- failure provenance identifies another revision, service, fixture, or infrastructure boundary.

Record comparability limitations. No single pattern guarantees certainty.

## 8. Baseline comparison

Run `simulation-transparent-baseline-v0.1` before full evidence.

Preserve:

- exact restricted inputs;
- matched rule and action;
- full action and reasons;
- action change or dimensional divergence;
- changed uncertainty and authority;
- added checks and recovery;
- investigation burden;
- whether the baseline was wrong, weaker, sufficient, unresolved, or the full process overreached.

S005 should ideally materialize one of:

- `baseline_wrong_action`;
- real dependency/PR action divergence;
- `comparison_unresolved` when evidence cannot support the preferred contrast.

## 9. Decision requirements

The decision must answer separately when relevant:

1. What does the evidence say about this frozen dependency proposal?
2. What should happen to this PR under current repository evidence or policy?
3. Which unresolved issue belongs to the dependency, the repository, CI, infrastructure, or maintainer policy?
4. What exact evidence would change each answer?

Do not label an update unsafe merely because a PR is blocked. Do not label a PR mergeable merely because the dependency itself appears acceptable.

## 10. Completion condition

S005 is complete only when:

- candidate screening and selection history are preserved;
- identity and baseline were frozen prospectively;
- material action-changing or divergence evidence is traceable;
- competing explanations are compared at justified depth;
- decision dimensions are clear rather than collapsed;
- machine and human reports agree;
- transitions and new-run rules exist;
- JSON/JSONL structure and references validate;
- baseline/full classification is honest;
- cross-case synthesis determines whether D1 can close;
- no unsupported correctness, safety, or capability claim is made.

## 11. D1 gate consequence

After S005:

1. compare S001–S005 across stable, conditional, contradicted, unresolved, and cost/stopping findings;
2. decide whether the minimum credible runtime responsibility is sufficiently evidenced;
3. if yes, enter B1 and reconcile existing source/tests with that responsibility;
4. if no, authorize only the smallest additional case needed to resolve a named planning uncertainty.

Implementation remains paused until that synthesis explicitly passes D1.
