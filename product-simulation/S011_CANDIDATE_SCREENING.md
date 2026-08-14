# S011 Candidate Screening — Dictare MLX Optional-Extra Activation and CI Coverage

**Date:** 2026-08-12  
**Status:** Admitted prospective real-world simulation case  
**Branch:** `agent/product-simulation-case-screening-02`  
**Product context:** `main@538c5c1ae56ddcd60e1e9bcf0a8a2c6d22b90471`

## 1. Candidate identity

**Target repository:** `dragfly/dictare`  
**Pull request:** `#34`  
**Base revision:** `9921be73b4a55ba54b7b1f46ba424ada0d38aaa7`  
**Head revision:** `62d65da86f902d4b54a9d87e9ced5ff2e1f61e55`  
**PR state at observation:** closed, not merged  
**Proposal:** NumPy `1.26.4 → 2.4.6` inside the optional `mlx` dependency group.

Exact diff:

```text
[project.optional-dependencies].mlx
numpy==1.26.4
→
numpy==2.4.6
```

## 2. Owned question

S011 owns one applicability/coverage question:

> **Can a dependency update inside a real platform-specific optional extra be target-relevant while the repository's standard PR tests and dedicated platform test workflow remain non-discriminating because neither workflow installs the affected extra?**

This is not a NumPy-2 compatibility case and does not claim that NumPy 2.4.6 breaks Dictare's MLX backend.

## 3. Why existing cases are insufficient

Related cases exist, but the activation shape is distinct:

- S002 had a relevant target behavior with tests present but skipped;
- S006 showed broad coverage is not discriminating behavior-path coverage;
- S008 showed same-package CI does not imply the same artifact-selection branch;
- S010 showed dependency constraints can encode compatibility/mitigation intent.

S011 adds a different prerequisite composition:

```text
optional dependency group installed
AND
Apple-Silicon environment
AND
MLX package discoverable
AND
hardware acceleration enabled
→ MLXWhisperEngine selected
→ affected optional dependency family becomes part of the real runtime environment
```

The interesting CI failure mode is earlier than skipped behavior tests: the optional dependency environment itself is not formed by the inspected test workflows.

## 4. Exact optional dependency contract

At the frozen base, the `mlx` optional group is a coordinated exact-pinned stack containing, among others:

```text
mlx==0.30.4
mlx-metal==0.30.4; sys_platform == 'darwin'
mlx-whisper==0.4.3
mlx-audio==0.3.0
mlx-lm==0.30.5
scipy==1.16.3
numba==0.61.0
numpy==1.26.4
torch==2.0.1
```

The repository comment says to keep the Apple-Silicon stack on the versions resolved by the release because loose specifiers can drift into combinations that break transcription.

Therefore the changed NumPy pin is not merely a core dependency used everywhere; it belongs to a deliberately coordinated optional family.

Adjacent real Dependabot PR #35 independently proposes an `mlx` version update against the same family, supporting the observation that bot-generated independent updates can target individual members of a coordinated stack.

## 5. Real user/runtime activation path

The target contains a real `MLXWhisperEngine` implementation for Apple Silicon.

Its runtime behavior includes:

- importing `mlx.core` and `mlx_whisper` when loading the model;
- importing `mlx_whisper` and `numpy` during transcription;
- using NumPy for audio dtype handling.

The engine factory selects the MLX engine only when:

```text
config.stt.hw_accel is enabled
AND
is_mlx_available() is true
```

`is_mlx_available()` requires:

```text
macOS
AND
platform.machine() == arm64
AND
mlx_whisper package is discoverable
```

The repository development instructions explicitly tell Apple-Silicon developers to install:

```text
uv sync --python 3.11 --extra mlx
```

So the optional group has an independently established real installation and runtime path.

## 6. CI coverage boundary

### Standard PR workflow

`.github/workflows/ci.yml` runs on Ubuntu for pushes and pull requests and installs:

```text
pip install -e ".[dev]"
```

It does not install `.[mlx]`.

### Dedicated macOS workflow

`.github/workflows/ci-macos.yml` runs on `macos-latest` on a schedule/manual dispatch and also installs:

```text
pip install -e ".[dev]"
```

It likewise does not install `.[mlx]`.

Therefore, for these two test workflows:

```text
platform test exists
!=
affected optional dependency environment exists
```

and:

```text
workflow success, if observed
!=
evidence that NumPy 2.4.6 works in the MLX optional stack
```

S011 does not claim that no repository automation anywhere ever installs the `mlx` extra; the bounded coverage statement concerns the inspected standard PR test/typecheck workflow and the dedicated macOS test workflow.

## 7. Maintainer context — corroborative, not sole evidence

The maintainer later closed PR #34 with an explanation that the `mlx` extra is hand-frozen, standard CI does not install it, and the dependencies move as a coordinated family tested on-device.

That statement is useful corroboration.

The core S011 conclusion does **not** depend on trusting the comment alone because the exact frozen repository independently establishes:

- the optional group and exact pins;
- the Apple-Silicon runtime path;
- the explicit Apple-Silicon development install command;
- the standard PR workflow installation set;
- the dedicated macOS workflow installation set.

## 8. Admission gates

### Gate A — real public proposal

**Pass.** Exact public Dependabot PR with frozen base/head and one NumPy pin change.

### Gate B — supported boundary

**Pass.** Public Python dependency-update proposal; evidence is read-only.

### Gate C — distinct question

**Pass.** Existing cases do not isolate optional-extra installation as a necessary activation proposition while showing that even a platform-specific test workflow can remain non-discriminating because it never installs the extra.

### Gate D — target relationship

**Pass.** MLX is a real Apple-Silicon STT backend selected by production engine logic, not dead packaging metadata.

### Gate E — evidence feasibility

**Pass.** Exact target dependency declaration, runtime code, hardware detection, development installation instructions, and workflow definitions are public and sufficient for the owned question.

### Gate F — honest negative path

**Pass.** This case can conclude only that inspected CI does not exercise the optional environment. It does not require proving NumPy 2.4.6 incompatible.

### Gate G — bounded stop

**Pass.** Stop once optional activation prerequisites and the two inspected workflow boundaries are established. Do not expand into on-device MLX execution unless a later question specifically requires behavioral compatibility evidence.

## 9. Claim limits

S011 does **not** establish:

- that NumPy 2.4.6 breaks MLX, mlx-whisper, NumPy dtype handling, or Dictare transcription;
- that every macOS runner is Apple Silicon;
- that no workflow or release process anywhere in the repository ever installs `mlx`;
- that required/observed PR checks were green unless independently retrieved;
- that the coordinated family must never be updated;
- that the maintainer's closure decision is technical ground truth;
- that the final maintainer action should be block/defer;
- that UpgradePilot already supports optional-extra applicability generally.

## 10. Planned evidence bundle

Purpose-built records:

1. `CASE_IDENTITY_AND_OPTIONAL_EXTRA.json`
2. `OPTIONAL_ACTIVATION_PATH.json`
3. `CI_COVERAGE_BOUNDARY.json`
4. `COORDINATED_FAMILY_CONTEXT.json`
5. `DISCOVERY_AND_STOPPING.json`
6. scenario `README.md`

## 11. Stop line

Do not extend S011 into:

- full NumPy 1→2 MLX compatibility analysis;
- Apple-Silicon hardware execution;
- exhaustive CI/release-workflow audit unrelated to the owned test-coverage question;
- every adjacent MLX-family Dependabot PR;
- a generic extras/platform runtime schema;
- a maintainer recommendation.

## 12. Admission decision

**S011 admitted.**

Next: freeze the small evidence bundle, evaluate the optional-activation/CI-coverage distinction, synthesize durable findings, and stop.