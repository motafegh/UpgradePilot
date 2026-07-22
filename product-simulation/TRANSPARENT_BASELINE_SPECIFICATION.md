# Product Simulation Transparent Baseline Specification

**Status:** Controlling local comparative baseline  
**Current version:** `simulation-transparent-baseline-v0.1`  
**Purpose:** Test the UpgradePilot technical thesis against a simple reproducible comparator

## 1. Why this baseline exists

The UpgradePilot charter claims that repository-specific usage, dependency-path
evidence, upstream behavior, and CI history can produce more useful and
better-calibrated decisions than a transparent baseline using only:

- version-change category;
- current CI conclusion;
- dependency directness;
- release-note keywords.

A scenario does not test that thesis merely by producing a detailed report. It
must run the same restricted baseline and compare the baseline result with the
full investigation.

## 2. Baseline boundary

The baseline may use only the four input families below.

### 2.1 Version-change category

One of:

- `patch`;
- `minor`;
- `major`;
- `pre_release`;
- `replacement_or_unknown`;
- `unclassifiable`.

For ecosystems where SemVer interpretation is uncertain, record
`unclassifiable` rather than guessing.

### 2.2 Current CI conclusion

One of:

- `passing`;
- `failing`;
- `mixed`;
- `missing`;
- `unknown`.

The baseline sees the overall current conclusion only. It does not inspect:

- workflow triggers;
- job conditions;
- commands;
- path relevance;
- environment identity;
- logs;
- flaky history;
- exact revision alignment beyond the supplied current conclusion.

That deliberate blindness is part of the comparison.

### 2.3 Dependency directness

One of:

- `direct`;
- `transitive`;
- `unknown`.

The baseline does not inspect functional use, selected extras/groups, dependency
paths, build/test/runtime distinctions, or deployment installation.

### 2.4 Release-note keyword signals

The baseline may perform literal case-insensitive keyword or phrase presence
checks only. It must not interpret sentence meaning, negation, scope, target
relevance, timing, or source truth.

#### Caution keywords

Starting signals include:

- `breaking`;
- `removed` or `removal`;
- `dropped support`;
- `deprecated` or `deprecation`;
- `incompatible`;
- `requires python`;
- `minimum python`;
- `platform support`;
- `operating system`;
- `architecture`;
- `compiler`;
- `build system`.

#### Benefit/security keywords

Starting signals include:

- `security`;
- `vulnerability`;
- `CVE`;
- `advisory`;
- `fixed`;
- `bug fix` or `bugfix`.

Keyword presence is not proof that the update is breaking, secure, compatible,
relevant, or beneficial.

## 3. Ordered decision rules

Apply the first matching rule.

### Rule B01 — Failing or mixed CI

If `ci_conclusion` is `failing` or `mixed`:

- outcome: `investigate_or_block`;
- reason: current CI is not clean;
- limitation: cause and relevance are unknown.

### Rule B02 — Missing or unknown CI

If `ci_conclusion` is `missing` or `unknown`:

- outcome: `run_targeted_checks`;
- reason: no passing current CI conclusion is available;
- limitation: the baseline cannot select the relevant check.

### Rule B03 — Unknown dependency relationship

If dependency directness is `unknown`:

- outcome: `run_targeted_checks`;
- reason: the baseline cannot determine whether the package belongs to the
  repository's supported path;
- limitation: no dependency-path or usage analysis is permitted.

### Rule B04 — Major, pre-release, replacement, or caution keyword

If the version category is `major`, `pre_release`, or `replacement_or_unknown`,
or at least one caution keyword is present:

- outcome: `run_targeted_checks`;
- reason: the update carries a coarse compatibility-change signal;
- limitation: the baseline cannot determine whether the signal is relevant.

### Rule B05 — Passing ordinary patch/minor update

If CI is `passing`, the dependency directness is known, the version category is
`patch` or `minor`, and no caution keyword is present:

- outcome: `merge_after_normal_review`;
- reason: ordinary-size update with passing current CI and no coarse breaking
  signal;
- limitation: the baseline does not know whether CI exercised the dependency or
  whether release-note claims are relevant or true.

Benefit/security keywords may be included as an additional favorable reason, but
they must not independently change the outcome.

### Rule B06 — Residual uncertainty

Otherwise:

- outcome: `abstain`;
- reason: the restricted inputs do not match a stronger rule.

## 4. Baseline output requirements

Each `BASELINE_RESULT.json` must preserve:

- baseline version;
- exact restricted inputs;
- how version category was derived;
- CI conclusion supplied to the baseline;
- dependency directness supplied to the baseline;
- literal keyword matches and source text identity;
- matched rule ID;
- outcome;
- reasons;
- limitations;
- full-investigation outcome;
- comparison dimensions;
- reviewer status.

## 5. Comparison dimensions

Compare the baseline with the full investigation on:

1. **Action:** Did the bounded maintainer action change?
2. **Reasoning:** Did the full investigation remove unsupported reasons or add
   decisive reasons?
3. **Uncertainty:** Did uncertainty become narrower, broader, or better located?
4. **Targeted action:** Did the full investigation identify a more specific and
   useful check?
5. **Evidence authority:** Did the full investigation show that a baseline input
   had less or more authority than assumed?
6. **Failure behavior:** Did the full investigation reveal missing, inaccessible,
   stale, conflicting, skipped, or irrelevant evidence?
7. **Cost:** What additional acquisition or reasoning was required?
8. **User value:** Did the result become materially more actionable or auditable?

## 6. Comparative classifications

Use one or more:

- `baseline_wrong_action`;
- `baseline_same_action_weaker_reasons`;
- `baseline_same_action_miscalibrated_certainty`;
- `baseline_same_action_less_actionable`;
- `baseline_sufficient`;
- `full_investigation_added_no_material_value`;
- `full_investigation_required_for_safe_abstention`;
- `comparison_unresolved`.

Do not force the full investigation to win. A deliberately simple case where the
baseline is sufficient is required coverage.

## 7. Version control

- Do not change baseline rules during an active case.
- If real cases show that the baseline is incoherent or unfair, preserve the
  current case result, create a new baseline version between cases, and rerun old
  cases only as an explicitly labeled comparison.
- A baseline version is a comparator, not accepted product architecture.
- Keyword additions made merely to improve known cases are prohibited.

## 8. Current expected retrospective application

Before S003:

- apply `simulation-transparent-baseline-v0.1` retrospectively to S001 and S002;
- label the execution as retrospective baseline reconstruction;
- use only information that belongs to the four permitted baseline inputs;
- do not use the full case findings to choose the baseline outcome;
- preserve any ambiguity in SemVer category, CI conclusion, directness, or
  keyword extraction.

S003 and later cases must create the baseline artifact during the active case,
before the full comparison is finalized.