# S010 — podcast-script NumPy Requirement Broadening / Candidate-Discovery Breadth

**Status:** Complete at admitted depth after bounded static evidence review  
**Form:** untouched real public Dependabot proposal + exact target/upstream source evidence  
**Target repository:** `invaderDMG/podcast-script`  
**Pull request:** `#36`

## 1. Owned question

> Can a discovery/evaluation process preserve multiple independently grounded mechanisms from one real NumPy requirement-broadening proposal, keep their target handling states separate, and avoid treating discovery of the first valid concern as transition-level completeness?

This scenario is about **candidate discovery breadth and candidate-state separation**.

It is not a general NumPy-2 compatibility audit.

## 2. Frozen proposal

Base:

`27a879ed2f215e88d4a617bd259e6595d524b79f`

Head:

`327196a5f628bfb3a7af47621d976425f9545171`

Changed file:

`pyproject.toml`

Exact change:

```text
numpy>=1.26,<2.0
→
numpy>=1.26,<3.0
```

This broadens the allowed resolution range. It does not mean every environment immediately installs one exact NumPy-2 release.

## 3. Real target path

At the exact base:

```text
podcast-script
→ inaSpeechSegmenter==0.7.6
→ NumPy-dependent segmentation/feature stack
```

The production `InaSpeechSegmenter` implementation in `src/podcast_script/segment.py` lazily imports/builds the external segmenter and invokes it while processing audio.

The target explicitly documents the NumPy `<2` constraint as a compatibility guard for this runtime stack.

## 4. Candidate A — `numpy.lib.pad`

Exact `inaSpeechSegmenter v0.7.6` source calls:

```python
numpy.lib.pad(sig, c, 'constant', constant_values=(0,))
```

inside the feature framing path.

NumPy 2.0's official migration guide reduces `np.lib` to a small explicit surface and does not retain `pad` there.

Target state:

```text
mechanism exists
+ target runtime path reaches affected transitive package
+ target explicitly protects stack with NumPy <2 guard
+ proposal removes that guard
→ concern remains unmitigated by target-local rewrite within inspected boundary
```

Claim boundary:

This does not mean the application fails on import. The relevant upstream call lives in the segmentation/feature path and the target uses lazy heavy imports.

## 5. Candidate B — generator passed to `np.vstack`

`inaSpeechSegmenter v0.7.6` declares `pyannote.algorithms` as a runtime dependency.

The target explicitly patches `pyannote.algorithms.utils.viterbi` before constructing the heavy segmenter. The replacement materializes generator-style values into a list before `np.vstack`.

Target state:

```text
mechanism recognized
+ target runtime relation established
+ target-local compatibility shim exists
→ separately mitigated mechanism
```

The exact historical resolved pyannote source revision was not independently reconstructed in this bounded case. The target's executable compatibility patch and inaSpeechSegmenter's declared dependency are preserved as the evidence boundary.

## 6. Why the two candidates must remain separate

They share:

- one NumPy requirement broadening;
- one transitive segmentation stack;
- one broad compatibility theme.

But they do not share the same mechanism or target state:

```text
A — removed np.lib.pad access
    target protection = NumPy <2 guard
    proposal weakens/removes that protection

B — generator input to np.vstack
    target protection = local runtime shim
    proposal does not remove that shim
```

Therefore:

```text
same dependency transition
+ same transitive path
!=
one impact candidate
```

and:

```text
first valid incompatibility discovered
!=
discovery complete
```

## 7. Context finding kept separate

The PR discussion indicates Dependabot's semver-major ignore did not prevent this requirement-broadening proposal.

That is useful automation/repository context, but it is not a third NumPy technical mechanism.

## 8. Evidence bundle

Read in this order:

1. [`CASE_IDENTITY_AND_PROPOSAL.json`](artifacts/CASE_IDENTITY_AND_PROPOSAL.json)
2. [`TARGET_RUNTIME_AND_GUARD_CONTEXT.json`](artifacts/TARGET_RUNTIME_AND_GUARD_CONTEXT.json)
3. [`MECHANISM_DISCOVERY_MAP.json`](artifacts/MECHANISM_DISCOVERY_MAP.json)
4. [`DISCOVERY_COVERAGE_AND_STOPPING.json`](artifacts/DISCOVERY_COVERAGE_AND_STOPPING.json)
5. [`../../S010_POST_CASE_SYNTHESIS.md`](../../S010_POST_CASE_SYNTHESIS.md)

Admission record:

[`../../S010_CANDIDATE_SCREENING.md`](../../S010_CANDIDATE_SCREENING.md)

Source screening:

[`../../REAL_WORLD_CASE_SCREENING_06.md`](../../REAL_WORLD_CASE_SCREENING_06.md)

## 9. What was not executed

No target repository mutation or external action occurred.

No NumPy-2 application run, resolver experiment, segmentation execution, or transitive-package modification was performed.

Those observations could answer additional behavioral questions but are unnecessary for the owned discovery-breadth question because exact source already establishes the two distinct mechanism/handling shapes.

## 10. Claim limits

Do not infer that:

- every allowed fresh resolution chooses NumPy 2;
- every NumPy-2 change matters;
- Candidate B is proven harmless in every NumPy-2 environment;
- Candidate A is the only remaining incompatibility;
- the full transitive graph is reconstructed;
- the historical PR closure proves the analysis;
- a maintainer action is established;
- UpgradePilot already implements general candidate discovery.

## 11. Stop

S010 stops once:

- the proposal and runtime path are frozen;
- Candidate A is independently grounded;
- Candidate B's distinct target-local mitigation is preserved;
- the two candidates are not collapsed;
- transition-level discovery blind spots remain explicit.

Further NumPy-2 migration work would be a different case/question.