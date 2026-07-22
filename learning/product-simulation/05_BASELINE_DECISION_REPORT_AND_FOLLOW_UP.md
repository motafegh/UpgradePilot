# 05 — Baseline, Decision, Reports, and Follow-Up

**Depth target:** Operational and implementation-adjacent understanding.  
**Primary question:** How does UpgradePilot test whether deeper investigation adds value, construct a bounded action, and preserve what happens after the report?

## 1. Why a baseline is required

A detailed investigation can appear valuable merely because it is detailed.

The transparent baseline creates a reproducible comparator using only four input families:

- version-change category;
- overall current CI conclusion;
- dependency directness;
- literal release-note keyword signals.

It deliberately cannot inspect:

- target source usage;
- dependency paths or selected groups;
- workflow triggers and path filters;
- exact commands;
- environment identity;
- logs;
- semantic relevance;
- source truth;
- exploitability;
- cross-source contradictions.

The baseline tests the project thesis. It is not intended to be a good final product.

## 2. Restricted baseline discipline

The baseline must use only permitted inputs and ordered rules.

The full investigation must not leak information into baseline inputs.

For example, S002's baseline may see:

- minor update;
- passing overall CI;
- direct dependency;
- literal `deprecated`, `removed`, and `fixed` signals.

It may not see that:

- HTTPX is used through Starlette `TestClient`;
- Python tests were excluded by a path filter;
- Docker CI only installed and built;
- the historical resolver state is unavailable.

## 3. The full investigation does not need to change the action

Value can appear in several dimensions:

- action changes;
- unsupported reasons are removed;
- uncertainty becomes better located;
- evidence authority is corrected;
- a vague check becomes specific;
- failure states become explicit;
- follow-up transitions improve;
- explanation becomes repository-specific;
- audit and replay improve.

Both S001 and S002 currently belong to:

```text
same broad action
+
full investigation provides stronger reasons, calibration, authority,
actionability, or auditability
```

This supports one thesis class. It does not validate the complete thesis.

## 4. The baseline must sometimes win

The project still needs cases where:

- the baseline chooses the wrong action;
- the baseline is sufficient and deeper work adds little;
- comparison remains unresolved;
- full investigation costs more than the decision improvement justifies.

Do not select or interpret cases to make the full system look superior.

## 5. Decision construction

A bounded decision should contain:

- exact case identity;
- outcome;
- reason records linked to findings;
- limitations;
- unresolved questions;
- targeted checks;
- why stronger outcomes are unjustified;
- why weaker outcomes are unjustified;
- human judgment required;
- transition behavior;
- decision actor and review state;
- prior decision or supersession relationship.

Current project outcomes include:

- merge after normal review;
- run targeted checks;
- investigate or block;
- defer;
- abstain.

These outcomes support decision-making. They do not authorize automatic mutation or merge.

## 6. Decision sufficiency

The decision should choose the strongest action supported by evidence, but no stronger.

### S001

Why not stronger:

- complete exploitability and production publication were not proven;
- automatic merge is outside the product boundary.

Why not weaker:

- the old version was advisory-affected;
- target Python support was compatible;
- the dependency was bounded docs tooling;
- official artifacts aligned;
- exact-head relevant docs CI passed;
- another equivalent targeted check would add little.

Result:

> Merge after normal maintainer review.

### S002

Why not stronger:

- likely compatibility and a successful Docker build did not execute TestClient behavior;
- exact framework resolution was unavailable.

Why not weaker:

- primary tagged sources showed a fixed framework branch existed;
- focused existing tests could resolve the uncertainty proportionately.

Result:

> Capture the exact resolver state and run Ruff and pytest.

## 7. One decision axis may be insufficient

S003 must test whether these can diverge:

```text
dependency update assessment
≠
overall PR or repository action
```

A pre-existing or unrelated failing check may mean:

- the dependency update itself appears acceptable;
- the PR is still not mergeable because current CI is red.

Do not add a permanent two-axis schema before the case proves the distinction is necessary.

## 8. Machine report versus human report

Both reports derive from the same current decision state, but they serve different consumers.

### Machine report

Should support:

- stable external representation;
- exact identity;
- findings and evidence references;
- decision and reasons;
- limitations;
- targeted checks;
- follow-up state;
- review status;
- artifact links.

It is not the full internal operation history.

### Human report

Should provide:

- exact update and revision;
- concise repository relevance;
- material evidence;
- missing or conflicting evidence;
- bounded recommendation;
- exact next action;
- important limitations;
- useful provenance.

It is not the complete case diary.

## 9. Rendering must not upgrade authority

Suppose the decision says:

> Run targeted checks because compatibility is likely but unconfirmed.

Unsafe human rendering:

> The update is compatible; run tests as a precaution.

The word `compatible` converts a bounded finding into an unsupported fact.

Safer rendering:

> A compatible framework line existed, but the target's exact resolved environment and TestClient behavior were not preserved. Capture the resolution and run the existing tests before merge.

## 10. Follow-up is persistent product behavior

The report is not the end of the runtime.

`FOLLOW_UP_STATE.json` should preserve:

- current state;
- required user action;
- responsible actor;
- authorization required;
- evidence expected from the action;
- pass/failure/unavailable/inconclusive transitions;
- new-run conditions;
- user-action history;
- closure condition;
- unresolved state.

### S002 transitions

- checks pass under captured resolution → ready for normal review;
- relevant TestClient failure → investigate or block;
- checks unavailable/inconclusive → retain targeted-check or defer state;
- new head or changed resolution → do not silently reuse the decision.

## 11. Rerun, replay, and supersession

### Rerun

The responsibility is performed again because the evidence boundary changed or new evidence is required.

### Replay

A prior run is reproduced or re-rendered from preserved state without silently replacing it.

### Comparison

Two runs or evidence boundaries are evaluated together.

### Supersession

A later finding, decision, or run replaces the current authority of an earlier record while preserving history.

A changed head SHA normally requires a new run or explicit comparison because the target identity changed.

## 12. Baseline comparison exercise

For S002, explain the difference between these two outputs:

### Baseline

```text
removed/deprecated keyword
+ passing CI
+ direct dependency
→ run targeted checks
```

### Full investigation

```text
TestClient adapter path
+ HTTPX app-argument removal
+ old/fixed Starlette threshold
+ unavailable exact resolution
+ Docker build scope
+ skipped Python workflow
→ capture resolver + run Ruff + run pytest
```

The action label is the same. The second output is more useful because the cause, authority, exact check, and transitions are materially better specified.

## 13. Failure modes

### Baseline contaminated by full evidence

Correction: record input cutoff and permitted sources before comparison.

### Full investigation forced to win

Correction: permit baseline-sufficient and overreach outcomes.

### Decision has reasons but no limitations

Correction: limitations are part of the decision, not optional report decoration.

### Human report contains new conclusions

Correction: render only current identity, evidence/finding projection, decision, and limitations.

### Targeted check has no transition

Correction: define what pass, relevant failure, unavailable, inconclusive, rebase, and changed environment mean.

### Historical user action closes the case

Correction: merge or closure is user action history, not technical confirmation.

## 14. Read and inspect

- `TRANSPARENT_BASELINE_SPECIFICATION.md`;
- S001 and S002 `BASELINE_RESULT.json`;
- S001 and S002 `DECISION.json`;
- S002 `MACHINE_REPORT.json`, `HUMAN_REPORT.md`, and `FOLLOW_UP_STATE.json`;
- cross-case review sections on thesis, one-outcome decisions, and S003.

## 15. Ownership checkpoint

1. Why does a detailed report not prove that deeper investigation was useful?
2. Name the four baseline input families and three things it is forbidden to inspect.
3. Explain how full investigation can add value without changing the action.
4. For S001, explain why another targeted docs check was not justified.
5. For S002, explain why immediate merge and indefinite block were both unjustified.
6. Give one example where dependency assessment and PR mergeability may diverge.
7. Rewrite an overconfident human-report sentence into a bounded one.
8. Explain when a new run is required instead of updating the old decision.

## 16. Current demonstrated depth

Two baseline comparisons and two structured decisions exist. Wrong-action, baseline-sufficient, unresolved, excessive-cost, real rerun, and decision-axis separation cases remain untested.
