# S011 — Dictare MLX Optional-Extra Activation / CI Coverage

**Status:** Complete at admitted depth after bounded static evidence review  
**Form:** untouched real public Dependabot proposal + exact target/config/workflow evidence  
**Target repository:** `dragfly/dictare`  
**Pull request:** `#34`

## 1. Owned question

> Can a dependency update inside a real platform-specific optional extra be target-relevant while the repository's standard PR tests and dedicated platform test workflow remain non-discriminating because neither workflow installs the affected extra?

S011 is about **optional dependency activation and CI coverage**.

It is not a NumPy-2 compatibility verdict.

## 2. Frozen proposal

Base:

`9921be73b4a55ba54b7b1f46ba424ada0d38aaa7`

Head:

`62d65da86f902d4b54a9d87e9ced5ff2e1f61e55`

Exact changed dependency inside `[project.optional-dependencies].mlx`:

```text
numpy==1.26.4
→
numpy==2.4.6
```

## 3. Optional dependency context

The `mlx` extra is an exact-pinned Apple-Silicon stack containing MLX, mlx-whisper, NumPy, Numba, SciPy, Torch and related packages.

The repository explicitly explains that the Apple-Silicon stack is kept on coordinated resolved versions because loose specifiers can drift into combinations that break transcription.

This means the changed NumPy pin belongs to a conditional, coordinated runtime family rather than the default install.

## 4. Real activation path

The exact target has a real `MLXWhisperEngine`.

Its runtime code imports `mlx.core`, `mlx_whisper`, and NumPy when loading/transcribing.

The engine factory chooses MLX only when:

```text
config.stt.hw_accel
AND
is_mlx_available()
```

and `is_mlx_available()` requires:

```text
macOS
AND
arm64 Apple Silicon
AND
mlx_whisper package discoverable
```

The README explicitly instructs Apple-Silicon developers to install:

```text
uv sync --python 3.11 --extra mlx
```

Therefore the optional dependency path is a real user/runtime path, not dead packaging metadata.

## 5. CI coverage boundary

The normal PR test/typecheck workflow installs:

```text
pip install -e ".[dev]"
```

on Ubuntu.

The dedicated macOS test workflow also installs only:

```text
pip install -e ".[dev]"
```

It does not install `.[mlx]`.

Therefore the inspected workflows do not form the dependency environment changed by PR #34.

The correct bounded conclusion is:

```text
standard test workflow exists
+
macOS test workflow exists
!=
MLX optional-extra dependency path exercised
```

Do not broaden this into a claim about every automation/release workflow in the repository.

## 6. Why this differs from skipped tests

S002 showed a behavior whose relevant tests were skipped.

S011 is earlier in the activation chain:

```text
optional dependency family not installed
→ MLX dependency environment absent
→ affected runtime path cannot be exercised by those workflows
```

The distinction is useful because no amount of interpreting the test result can recover coverage for dependencies that were never installed.

## 7. Coordinated-family context

Adjacent Dependabot PR #35 independently attempted to update `mlx` inside the same optional family.

The maintainer later described the family as hand-frozen/coordinated and said PR #34's standard checks did not exercise the Apple-Silicon path.

That is corroborative context. S011's core evidence remains the frozen target files and workflow definitions.

## 8. Evidence bundle

Read:

1. [`CASE_IDENTITY_AND_OPTIONAL_EXTRA.json`](artifacts/CASE_IDENTITY_AND_OPTIONAL_EXTRA.json)
2. [`OPTIONAL_ACTIVATION_PATH.json`](artifacts/OPTIONAL_ACTIVATION_PATH.json)
3. [`CI_COVERAGE_BOUNDARY.json`](artifacts/CI_COVERAGE_BOUNDARY.json)
4. [`COORDINATED_FAMILY_CONTEXT.json`](artifacts/COORDINATED_FAMILY_CONTEXT.json)
5. [`DISCOVERY_AND_STOPPING.json`](artifacts/DISCOVERY_AND_STOPPING.json)
6. [`../../S011_POST_CASE_SYNTHESIS.md`](../../S011_POST_CASE_SYNTHESIS.md)

Admission:
[`../../S011_CANDIDATE_SCREENING.md`](../../S011_CANDIDATE_SCREENING.md)

## 9. What was not executed

No target mutation, workflow rerun, Apple-Silicon execution, MLX installation, or NumPy compatibility experiment occurred.

Those would answer different behavioral questions. Static exact evidence is sufficient for the owned activation/coverage question.

## 10. Claim limits

Do not infer that:

- NumPy 2.4.6 is incompatible with Dictare's MLX backend;
- a macOS workflow automatically means Apple-Silicon MLX coverage;
- every repository workflow omits the MLX extra;
- a successful standard test run proves the optional stack works;
- the coordinated family cannot be updated;
- the historical maintainer closure is product ground truth.

## 11. Stop

S011 stops once the optional dependency identity, real runtime activation chain, and bounded non-coverage of the two relevant test workflows are established.

Further on-device compatibility testing requires a different admitted question.