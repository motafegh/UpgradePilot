# S005 Post-Case Synthesis

**Status:** Completed AI-authored synthesis; Ali review pending  
**Date:** 2026-07-23  
**Scenario:** [`S005`](scenarios/S005-modelarrayio-pytest-9.0.3-to-9.1.1/README.md)  
**Run:** `s005-20260723T123700Z-r1`

This synthesis does not authorize target mutation, freeze production schemas, or establish Ali-owned capability.

## 1. Case result

S005 investigated `PennLINC/ModelArrayIO#85`, pytest 9.0.3 → 9.1.1.

Transparent baseline v0.1 selected:

```text
run_targeted_checks
```

The completed full simulation selected:

```text
merge_after_normal_review
```

Classification:

```text
baseline_wrong_action
```

This is the first S001–S005 case where the full evidence changed the broad maintainer action.

## 2. Why the baseline was wrong

The baseline observed a minor update, passing CI, direct dependency status, and literal `breaking`, `removals`, and `deprecations` language. Rule B04 therefore required targeted checks.

That was coherent under the baseline boundary but wrong for the frozen target because it could not inspect:

- exact dependency resolution;
- workflow and tox runner behavior;
- the scope of the upstream breaking statement;
- frozen repository configuration and API usage;
- matrix test selection;
- whether an additional check had a named unresolved question.

The full result established:

- the PR changed only pytest in `uv.lock`;
- tox's latest environments used `uv-venv-lock-runner`;
- exact pytest 9.1.1 jobs passed on Python 3.11–3.14;
- the Python 3.12 latest job included downloaded-data tests;
- the official breaking behavior required `--doctest-modules`, which the target did not use;
- the listed deprecated APIs and patterns were absent or used in a supported form;
- every parametrization site used a concrete Collection;
- no remaining target-specific uncertainty identified a useful additional check.

## 3. Product lesson

S005 supports this operating principle:

> Release-note caution is a screening signal, not a final action. The system must map each material upstream change to exact dependency identity, target configuration, repository usage, and relevant exact-head checks before deciding whether caution requires additional work.

This complements S004:

- S004: confirm the baseline's authority-critical assumptions and stop when the baseline is sufficient;
- S005: inspect target-specific relevance and overturn the baseline when its coarse caution creates an unnecessary gate.

The future runtime therefore needs both **stopping discipline** and **action-revision authority**.

## 4. CI-authority lesson

Candidate screening exposed three distinct false-green patterns:

1. a workflow runs a dependency tool but installs it independently of the changed lock;
2. tox resolves a broad dependency constraint rather than the proposed version;
3. a workflow hard-codes the old dependency version despite the PR changing a requirements file.

S005 qualified because exact identity traversed:

```text
PR patch
→ pytest 9.1.1 in uv.lock
→ test extra
→ uv-venv-lock-runner
→ exact-head tox environments
→ pytest commands
→ matrix conclusions
```

This strengthens the rule that relevant CI authority must include dependency identity, not only workflow, command, and result.

## 5. Upstream-to-target mapping

A caution signal must be decomposed into concrete predicates. For pytest 9.1:

```text
upstream statement
→ activation condition
→ target configuration or source surface
→ exact execution coverage
→ unresolved question or closure
```

The breaking statement was not globally applicable. It required a specific combination of doctest collection and fixture placement. Deprecations likewise concerned named private APIs or patterns.

This is a reusable responsibility for supported Python cases:

- preserve official upstream scope;
- extract activation conditions without converting them into universal claims;
- inspect target evidence;
- record absent, present, unresolved, or externally mediated states;
- select an additional check only when one can answer a remaining question.

## 6. Artifact implications

### `CHECK_EXECUTIONS.jsonl`

Disposition after S003 and S005:

> **Repeated conditional stable candidate** for material matrix, rerun, base/head, adjacent-PR, or local/CI comparisons.

S005 used it to preserve which matrix cells were exact-lock pytest 9.1.1 executions and which minimum-dependency cell had a different comparison role.

### `FAILURE_ATTRIBUTION.json`

Correctly inactive. No failing or conflicting execution existed.

### Separate dependency and PR decision dimensions

Not required. Both the dependency assessment and current PR action support normal review. S003 remains the only case where the split added value, so it remains a conditional decision shape rather than a universal schema.

### `STOPPING_EVALUATION.json`

Not required. The stop was represented through operations, findings, decision, and follow-up because investigation cost was not the primary case question.

## 7. Stable candidates strengthened

- exact identity freeze before decision authority;
- baseline execution before final full-result interpretation;
- dependency identity as part of CI authority;
- official upstream source and activation-condition extraction;
- target configuration and source mapping;
- exact matrix execution representation when material;
- bounded negative evidence with temporal and search limits;
- findings that can overturn, not merely annotate, a baseline action;
- reports generated from the same decision state;
- explicit new-run and supersession boundaries;
- conditional artifact and stage activation;
- structural validation with degraded method state preserved.

## 8. Assumptions contradicted or narrowed

- release-note `breaking` language always requires another check;
- passing a tool-named CI job proves the proposed tool version was exercised;
- a changed lockfile automatically controls tox or test execution;
- negative code search alone is sufficient without a temporal comparison boundary;
- full investigation value is limited to stronger reasons for the same action;
- targeted checks are useful even when no unresolved target question names one.

## 9. Automation implications

### Strong deterministic candidates

- freeze PR/base/head/change identity;
- parse a simple lock mutation and artifact hashes;
- determine whether a runner consumes the lock;
- extract workflow, job, command, matrix, revision, and conclusion;
- preserve per-execution comparison roles;
- literal baseline execution;
- search for named configuration and API surfaces;
- validate IDs and references;
- render machine and human projections.

### Tool-assisted interpretation

- convert upstream prose into activation conditions;
- decide whether a search pattern adequately represents a behavior;
- assess whether external plugins create a material unresolved path;
- determine whether excluded tests are relevant;
- decide whether an additional check has information value;
- revise the bounded action proportionately.

### Human authority

- accept residual risk;
- apply repository policy;
- approve or merge the PR;
- accept D1 synthesis and the B1 implementation responsibility.

## 10. Learning implications for Ali

S005 exposes, but does not prove mastery of:

- why dependency identity is part of CI authority;
- release-note keyword signal versus semantic target relevance;
- activation-condition reasoning;
- negative evidence and its limits;
- matrix-cell comparison roles;
- why a targeted check requires a named unresolved question;
- how a baseline can be wrong in the cautious direction;
- how full evidence may legitimately weaken an action;
- how to preserve the baseline after it is superseded.

Ali review should include explaining why `pyvista-wasm#250` and `eRechnung#4` were rejected despite green tests, and why ModelArrayIO's lock-backed tox path is materially different.

## 11. Validation

The terminal scenario record reports:

- 16 JSON files;
- 4 JSONL files;
- 10 operations;
- 7 evidence records;
- 7 claims/interpretations;
- 5 execution records;
- 7 findings;
- 4 decision reasons;
- zero structural errors under connector-backed inspection.

The retained validator could not be executed from a clean clone because the local environment could not resolve GitHub. Validation is therefore `passed_with_method_degradation`, not clean-checkout proof.

## 12. D1 consequence

S005 completes the required action-changing contrast.

Current comparative coverage:

| Class | Cases |
|---|---|
| Same action, materially stronger support | S001, S002, S003 |
| Baseline sufficient; deeper work adds no material decision value | S004 |
| Baseline wrong action | S005 |
| Dependency/PR action divergence | S003 trial only; not repeated |
| Unresolved comparison | Not represented as a final case |

The technical discovery evidence is now sufficient to state a minimum credible runtime responsibility. D1 still requires Ali review before the project may treat that responsibility as accepted and enter implementation planning under B1.

## 13. Review and ownership

- AI contribution: screening, evidence acquisition, analysis, artifacts, decision, validation profile, and synthesis.
- Ali contribution: authorized full S005 execution and continuation.
- Ali review: pending.
- Target mutation: none.
- Capability conclusion: none.