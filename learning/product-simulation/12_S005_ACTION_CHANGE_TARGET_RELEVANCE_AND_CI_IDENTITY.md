# S005 — Action Change, Target Relevance, and CI Dependency Identity

**Status:** AI-produced learning artifact grounded in completed S005; Ali ownership exercises pending  
**Depth:** Operational and implementation-adjacent explanation, not mastery proof  
**Evidence:** [`../../product-simulation/scenarios/S005-modelarrayio-pytest-9.0.3-to-9.1.1/`](../../product-simulation/scenarios/S005-modelarrayio-pytest-9.0.3-to-9.1.1/)  
**Synthesis:** [`../../product-simulation/S005_POST_CASE_SYNTHESIS.md`](../../product-simulation/S005_POST_CASE_SYNTHESIS.md)

## 1. Central lesson

S005 is not merely a case where tests were green. It is a case where the transparent baseline selected the wrong broad action because literal upstream caution was not target-specific.

```text
baseline: run_targeted_checks
full evidence: merge_after_normal_review
classification: baseline_wrong_action
```

The action changed only after two separate questions were answered:

1. Did CI actually execute the proposed pytest 9.1.1 resolution?
2. Did the upstream breaking/deprecated behavior exist in the frozen target?

## 2. CI dependency identity

A successful job has authority only when the changed dependency identity can be traced into the executed responsibility.

S005 path:

```text
PR changes pytest in uv.lock
→ pytest is in the test extra
→ tox latest environments use uv-venv-lock-runner
→ those environments consume the changed lock
→ pytest commands run on the exact head
→ Python 3.11–3.14 jobs pass
```

Compare rejected candidates:

- `pyvista-wasm#250`: tox ran, but `tox.ini` allowed `pytest>=7.0`; exact proposed pytest identity was not proven.
- `eRechnung#4`: the PR changed a pinned requirements file, but CI hard-coded the old pytest version.

Therefore:

> Tool name, workflow name, and green color are insufficient. The proposed dependency version must be connected to the actual environment and command.

## 3. Keyword signal versus semantic relevance

The baseline sees words such as `breaking` and `deprecations`. This is useful screening, but it cannot answer:

- What exactly changed?
- Under what activation condition?
- Does the target use that configuration or API?
- Did relevant tests exercise the proposed version?
- What unresolved question would another check answer?

S005 decomposed the official pytest changelog into concrete predicates.

Example:

```text
upstream: inline non-function autouse fixtures may run twice
condition: --doctest-modules is enabled
frozen target: --doctest-modules absent
result: breaking behavior inactive
```

This is more accurate than either extreme:

- “release notes say breaking, therefore block or test more”; or
- “minor release and green CI, therefore safe.”

## 4. Negative evidence

Negative search is not proof by itself. Credible negative evidence needs:

- named upstream surfaces;
- explicit search/config patterns;
- frozen or temporally bounded source identity;
- inspection of ambiguous matches;
- limitations for external plugins or unindexed content.

S005 inspected all discovered parametrization sites and confirmed concrete list/tuple values. It also compared the frozen head with a later branch state and found no source/test changes, preventing a later negative search from hiding a frozen-head use that was subsequently deleted.

## 5. When a targeted check is justified

A targeted check needs a named unresolved question.

Bad reasoning:

> The release notes contain caution, so run something extra.

Better reasoning:

> The repository uses `--doctest-modules` with an inline session autouse fixture; run the exact doctest-enabled suite under pytest 9.1.1 to determine whether the fixture executes twice.

In S005, no such unresolved target condition remained. Requesting another test would add ceremony rather than information.

## 6. Why the full action became weaker

Full analysis does not always make the action stricter.

S005 showed:

- the baseline's uncertainty was coarse and misplaced;
- exact repository evidence removed that uncertainty;
- relevant exact-head tests already existed and passed;
- no useful check remained;
- normal review was proportionate.

This is evidence that UpgradePilot must be allowed to weaken, strengthen, preserve, or abstain from a baseline action.

## 7. Conditional artifacts

`CHECK_EXECUTIONS.jsonl` activated because the distinction among:

- Python 3.11–3.14 latest lock-backed environments; and
- Python 3.11 minimum-dependency resolution

was material to evidence authority.

`FAILURE_ATTRIBUTION.json` did not activate because no failure existed. Separate dependency/PR action dimensions did not activate because both supported normal review.

## 8. Important boundaries

S005 does not prove:

- pytest 9.1.1 is universally safe;
- external plugin internals contain no incompatible behavior;
- excluded S3 tests are irrelevant to every future change;
- negative search is complete in all repositories;
- the baseline is generally too cautious;
- the full method is automated;
- Ali independently owns this reasoning.

## 9. Ali review tasks

### Prediction

Before reopening evidence, explain what baseline v0.1 must output and which rule applies.

### CI trace

Trace:

```text
uv.lock patch
→ tox runner choice
→ environment dependency identity
→ pytest command
→ matrix result
```

Explain why `py311-min` is not exact pytest 9.1.1 proof.

### Rejection diagnosis

Explain why green tests did not qualify:

- `pyvista-wasm#250`;
- `eRechnung#4`.

### Upstream mapping

Choose three pytest 9.1 caution surfaces and state:

- upstream condition;
- target search/config evidence;
- conclusion;
- limitation.

### Challenge

Argue the strongest case for retaining `run_targeted_checks`. Then explain whether that argument identifies a concrete useful check.

### Ownership-bearing B1 transfer

During B1, identify which parts of this reasoning should be deterministic runtime behavior in B2 and which must remain prepared fixture interpretation until later evidence supports automation.

## 10. Depth record

Current demonstrated state:

- concepts and mechanism: AI-produced operational explanation;
- case application: AI-controlled;
- artifact inspection: available for Ali review;
- independent transfer: not demonstrated;
- implementation ownership: not demonstrated.

Do not mark this lesson mastered merely because the case and note are complete.