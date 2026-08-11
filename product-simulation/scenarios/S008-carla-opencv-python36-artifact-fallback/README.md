# S008 — CARLA OpenCV Python-3.6 Artifact Fallback

**Status:** Completed bounded evidence analysis for the owned artifact-transition question  
**Case form:** Untouched real public Dependabot PR + authoritative public package metadata  
**Candidate screening:** [`../../S008_CANDIDATE_SCREENING.md`](../../S008_CANDIDATE_SCREENING.md)

## Owned question

> Does `opencv-python 4.2.0.32 -> 4.8.1.78` remove the prebuilt CPython-3.6 Linux wheel path for a target-relevant ScenarioRunner installation context, thereby changing the installation path from a prebuilt binary to source-distribution fallback, and does the inspected target CI cover that exact transition?

## Frozen identity

```text
repository: carla-simulator/scenario_runner
PR: 1111
base: master
base SHA: 7758d066080f180f8296887ed89b7c723a54706a
head SHA: f32ad2d23a9abee47c566dfbed2b822d953a09e2
old dependency: opencv-python==4.2.0.32
new dependency: opencv-python==4.8.1.78
```

See [`artifacts/CASE_IDENTITY.json`](artifacts/CASE_IDENTITY.json).

## Result

For the bounded CPython-3.6 Linux artifact question:

```text
old release
→ publishes CPython-3.6 manylinux wheels

new release
→ publishes CPython-3.7+ abi3 wheels
→ no CPython-3.6-compatible published binary wheel in the release inventory
→ publishes a source distribution
→ retains Requires-Python >=3.6 and Python-3.6 source-build metadata
```

Therefore the dependency update changes the available installation path for CPython 3.6 on Linux from a prebuilt wheel path to source-distribution fallback.

This is **not** evidence that source installation will fail.

## Target relevance

The exact target base:

- pins the old OpenCV package in `requirements.txt`;
- documents Python-3 installation of the full requirements file;
- contains direct `cv2` runtime use in the visualizer path;
- retains an explicit Python-3.6 repository environment artifact.

The repository Dockerfile does **not** install the full requirements set and is not treated as proof that this specific container installs OpenCV. The target-relevance claim stays bounded to the combined repository evidence recorded in [`artifacts/TARGET_INSTALLATION_CONTEXT.json`](artifacts/TARGET_INSTALLATION_CONTEXT.json).

## CI coverage result

The inspected target workflows install requirements but do not pin or matrix Python 3.6. The unit workflow executes a narrow XOSC loader test, not the OpenCV visualizer path.

Therefore the inspected CI evidence does not establish coverage of the Python-3.6 wheel-to-source-fallback transition.

This does not prove that no relevant testing existed outside the inspected public evidence boundary.

## Why no native build was performed

The owned question is artifact availability and installation-path transition. Exact package inventories already discriminate that question.

A native source-build observation would answer a different proposition:

> Does the fallback source build succeed in one exact environment?

That proposition remains unresolved and outside this scenario's bounded question. See [`artifacts/COVERAGE_AND_STOPPING_EVALUATION.json`](artifacts/COVERAGE_AND_STOPPING_EVALUATION.json).

## Main discoveries

1. **Interpreter support metadata and binary artifact availability are distinct.** `Requires-Python >=3.6` does not imply a CPython-3.6 wheel exists.
2. **No binary artifact does not imply impossible installation.** A source distribution can preserve a fallback path.
3. **Installation-mode change is a technical impact mechanism.** A dependency update can matter before application runtime or API behavior changes.
4. **CI relevance is proposition-specific.** Installing the dependency on an unpinned runner does not establish Python-3.6 artifact coverage.
5. **Static evidence can justify stopping.** Expensive execution is not automatically more useful than exact artifact metadata.

## Cross-case relationship

```text
S001
explicit upstream interpreter-support drop
+ target range
→ applicability can be refuted deterministically

S003
actual dependency-resolution failure
→ installability failure established

S007
package-family contradiction
→ static evidence can prune resolver/runtime work

S008
binary artifact disappears while source support remains
→ installation path changes
→ deeper source-build success remains a separate proposition
```

S008 therefore extends rather than duplicates the existing corpus.

## Claim limits

S008 does **not** establish:

- global ScenarioRunner/OpenCV 4.8 compatibility;
- Python-3.6 source-build success or failure;
- runtime correctness of the OpenCV visualizer;
- security exposure;
- performance;
- product safety;
- maintainer merge/block/defer action;
- a requirement for UpgradePilot to implement generic wheel analysis now.

## Reading order

1. [`../../S008_CANDIDATE_SCREENING.md`](../../S008_CANDIDATE_SCREENING.md)
2. [`artifacts/CASE_IDENTITY.json`](artifacts/CASE_IDENTITY.json)
3. [`artifacts/TARGET_INSTALLATION_CONTEXT.json`](artifacts/TARGET_INSTALLATION_CONTEXT.json)
4. [`artifacts/UPSTREAM_DISTRIBUTION_TRANSITION.json`](artifacts/UPSTREAM_DISTRIBUTION_TRANSITION.json)
5. [`artifacts/COVERAGE_AND_STOPPING_EVALUATION.json`](artifacts/COVERAGE_AND_STOPPING_EVALUATION.json)

## Evidence sources

Target:

- https://github.com/carla-simulator/scenario_runner/pull/1111
- exact target files at base SHA `7758d066080f180f8296887ed89b7c723a54706a`

Upstream/package:

- https://pypi.org/project/opencv-python/4.2.0.32/#files
- https://pypi.org/project/opencv-python/4.8.1.78/#files
- https://github.com/opencv/opencv-python/blob/78/setup.py
- https://github.com/opencv/opencv-python/blob/78/pyproject.toml
