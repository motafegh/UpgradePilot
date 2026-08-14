# S010 Candidate Screening — NumPy Requirement Broadening and Candidate-Discovery Breadth

**Date:** 2026-08-12  
**Status:** Admitted prospective real-world simulation case  
**Branch:** `agent/product-simulation-case-screening-02`  
**Source screening:** [`REAL_WORLD_CASE_SCREENING_06.md`](REAL_WORLD_CASE_SCREENING_06.md)  
**Product context:** `main@538c5c1ae56ddcd60e1e9bcf0a8a2c6d22b90471`

## 1. Candidate identity

**Target repository:** `invaderDMG/podcast-script`  
**Pull request:** `#36`  
**Base revision:** `27a879ed2f215e88d4a617bd259e6595d524b79f`  
**Head revision:** `327196a5f628bfb3a7af47621d976425f9545171`  
**PR state at observation:** closed, not merged  
**Changed file:** `pyproject.toml`

Exact proposal:

```text
numpy>=1.26,<2.0
→
numpy>=1.26,<3.0
```

This is a **requirement-broadening proposal**. It does not assert that every environment immediately installs one exact NumPy 2 release. It allows a fresh compatible resolution to select NumPy 2.x.

## 2. Owned question

S010 owns one discovery/evaluation question:

> **Can a discovery/evaluation process preserve multiple independently grounded mechanisms from one real NumPy requirement-broadening proposal, keep their target handling states separate, and avoid treating discovery of the first valid concern as transition-level completeness?**

This is a candidate-discovery coverage case, not a general NumPy-2 migration audit.

## 3. Why existing cases are insufficient

Existing cases establish related but different facts:

- S001/S008 show that one mechanism can be evaluated precisely without proving transition-wide completeness;
- S007 shows package-family contradiction and pruning;
- Cactus/Chia controls in Screening 06 show one rich release can yield strong, refuted, unresolved, and absent target mechanisms;
- `CANDIDATE_DISCOVERY_COVERAGE_PRESSURE_TEST_01.md` establishes conceptually that finding one candidate does not prove discovery completeness.

S010 adds the missing real-world contrast:

```text
one exact proposal
+ one real transitive runtime path
+ at least two independently grounded NumPy-2 mechanisms
+ materially different target handling states
```

That makes it useful for testing candidate splitting, per-candidate state preservation, and discovery stopping.

## 4. Exact target runtime relationship

At the frozen base:

```text
podcast-script
→ runtime dependency inaSpeechSegmenter==0.7.6
→ NumPy-dependent segmentation / feature stack
```

`src/podcast_script/segment.py` implements the production `InaSpeechSegmenter` path. It lazily builds `inaSpeechSegmenter.Segmenter` and then invokes it against a temporary WAV during segmentation.

The target's `pyproject.toml` explicitly documents the NumPy `<2` cap as deliberate compatibility control for `inaSpeechSegmenter 0.7.6`, not a stale arbitrary pin.

## 5. Mechanism A — removed `numpy.lib.pad` path

### Upstream/transitive evidence

Exact `inaSpeechSegmenter v0.7.6` source is pinned by tag commit:

`877a3a46cf6a77784ded03d6edf36ddc0cdc9573`

Its `inaSpeechSegmenter/sidekit_mfcc.py` feature-framing code calls:

```python
numpy.lib.pad(sig, c, 'constant', constant_values=(0,))
```

NumPy 2.0's official migration guide states that the `np.lib` namespace was reduced to a small explicit public surface; `pad` is not retained there and normal public access is through the main NumPy namespace.

### Target handling state

The target explicitly cites this incompatibility as a reason for:

```text
numpy>=1.26,<2.0
```

No target-local rewrite of the transitive `numpy.lib.pad` call was found in the inspected path.

The proposal broadens away the version guard that currently prevents selection of NumPy 2.x.

### Bounded consequence

If a fresh resolution selects NumPy 2.x and the production segmentation feature-framing path reaches the exact upstream `numpy.lib.pad` call, that mechanism is incompatible with the NumPy-2 public namespace.

Do **not** restate this as "the application necessarily crashes on import": the target uses lazy heavy imports and the exact call lives in the segmentation/feature path.

## 6. Mechanism B — generator input to `np.vstack`, locally mitigated

### Dependency relation

Exact `inaSpeechSegmenter v0.7.6` package metadata declares `pyannote.algorithms` as a runtime dependency.

### Target executable evidence

Before importing/constructing `inaSpeechSegmenter`, the target calls:

```text
_patch_pyannote_viterbi_for_modern_numpy()
```

The target implementation patches `pyannote.algorithms.utils.viterbi` functions `_update_emission` and `_update_constraint` so generator-style inputs are materialized into a list before `np.vstack`:

```python
return np.vstack(
    [np.tile(e, (c, 1)) for e, c in zip(matrix.T, consecutive, strict=False)]
).T
```

The code explicitly documents the underlying compatibility reason: the transitive pyannote implementation passes generators to `np.vstack`, which current NumPy behavior rejects.

### Target handling state

Unlike Mechanism A, this concern is not handled only by the NumPy `<2` guard. The target has a local runtime shim for this mechanism.

Therefore:

```text
Mechanism A
→ protected by version guard; no local transitive-call rewrite observed

Mechanism B
→ explicit target-local runtime shim
```

The two mechanisms must not be collapsed merely because both originate on the same NumPy transition and transitive segmentation stack.

### Evidence limitation

This screening did not independently reconstruct the exact resolved `pyannote.algorithms` version from the large target lockfile. That does not erase the target's executable patch or inaSpeechSegmenter's declared dependency, but it limits any stronger claim about the exact historical pyannote source revision.

S010 does not need that stronger claim to test candidate-discovery breadth and target handling separation.

## 7. Contextual finding — Dependabot requirement broadening

The PR discussion explains that the repository attempted to ignore NumPy semver-major version updates, yet Dependabot still proposed a **requirement update** broadening `<2` to `<3`.

This is useful repository/automation context:

```text
version-update guard
!=
requirement-broadening guard
```

But this is **not** a third technical NumPy impact candidate. Keep it separate from the two mechanism-specific technical concerns.

## 8. Admission gates

### Gate A — real-world proposal

**Pass.** Public Dependabot PR with frozen base/head and exact one-file requirement change.

### Gate B — supported target boundary

**Pass.** Public Python project, pip-style dependency declaration, read-only evidence.

### Gate C — distinct discovery/evaluation question

**Pass.** Existing cases do not yet provide one proposal with multiple independently grounded mechanisms on the same runtime path and different target handling states.

### Gate D — target relationship

**Pass.** Production segmentation code uses `inaSpeechSegmenter==0.7.6`; inaSpeechSegmenter declares NumPy and pyannote dependencies; exact target code contains mechanism-specific compatibility handling.

### Gate E — evidence feasibility

**Pass.** Exact PR identity, target source, target dependency contract, exact inaSpeechSegmenter tag/source, official NumPy migration evidence, and target compatibility shim are public and read-only.

### Gate F — honest negative/alternative path

**Pass.** A mechanism may be discovered and then shown mitigated, non-activating, unresolved, or duplicate. S010 does not require every candidate to become an active incompatibility.

### Gate G — bounded stop

**Pass.** Stop once the two mechanisms are independently grounded enough for the owned discovery-breadth question, their target handling states are separated, and discovery blind spots are explicit.

## 9. Claim limits

S010 does **not** establish:

- that every resolution after the PR selects NumPy 2;
- that the whole application crashes on import;
- that every NumPy-2 change matters to podcast-script;
- that the local pyannote shim makes the full stack NumPy-2 compatible;
- that no third material NumPy-2 mechanism exists;
- that the exact historical pyannote source revision has been reconstructed;
- that the PR should be merged, blocked, or closed;
- that historical PR closure proves technical correctness;
- that UpgradePilot already implements broad candidate discovery.

## 10. Planned evidence bundle

Purpose-built records only:

1. `CASE_IDENTITY_AND_PROPOSAL.json`
2. `TARGET_RUNTIME_AND_GUARD_CONTEXT.json`
3. `MECHANISM_DISCOVERY_MAP.json`
4. `DISCOVERY_COVERAGE_AND_STOPPING.json`
5. scenario `README.md`

No D1-style full artifact bundle is required because S010 owns a narrower discovery/evaluation question.

## 11. Stop line

Do not expand S010 into:

- exhaustive NumPy 2 migration analysis;
- full dependency graph reconstruction;
- lockfile archaeology for every transitive package;
- Apple-Silicon analysis of future inaSpeechSegmenter versions;
- full application execution;
- maintainer recommendation;
- candidate-discovery runtime architecture.

Static exact evidence is already sufficient to test the admitted discovery-breadth question. Dynamic execution would answer additional behavioral propositions rather than this admission question.

## 12. Admission decision

**S010 admitted.**

Next: freeze the small evidence bundle, evaluate discovery breadth/state separation, synthesize only durable findings, and stop when the owned question is resolved.