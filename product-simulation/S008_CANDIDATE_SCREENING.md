# S008 Candidate Screening — CARLA OpenCV Python-3.6 Artifact Availability

**Date:** 2026-08-11  
**Status:** **ADMITTED — prospective untouched real public case**  
**Candidate:** `carla-simulator/scenario_runner#1111`  
**Case ID:** `S008-carla-opencv-python36-artifact-fallback`  
**Role:** non-controlling product-discovery and evaluation evidence

## Owned question

> Does `opencv-python 4.2.0.32 -> 4.8.1.78` remove the prebuilt CPython-3.6 Linux wheel path for a target-relevant ScenarioRunner installation context, thereby changing the installation path from a prebuilt binary to source-distribution fallback, and does the inspected target CI cover that exact transition?

This case does not answer global OpenCV compatibility, source-build success/failure, product safety, or maintainer action.

## Frozen proposal identity

```text
repository: carla-simulator/scenario_runner
PR: 1111
base: master
base SHA: 7758d066080f180f8296887ed89b7c723a54706a
head SHA: f32ad2d23a9abee47c566dfbed2b822d953a09e2
changed file: requirements.txt
old: opencv-python==4.2.0.32
new: opencv-python==4.8.1.78
```

Primary source: https://github.com/carla-simulator/scenario_runner/pull/1111

## Admission evidence

### Target relationship

At the exact base revision:

- `requirements.txt` pins the old OpenCV package;
- source-install documentation directs Python-3 users to install the full requirements file;
- `visualizer.py` imports `cv2` and uses concrete OpenCV runtime functions;
- `simple_vehicle_control.py` can reach the visualizer path;
- the repository retains an explicit Python-3.6 environment artifact (`python:3.6-slim` Dockerfile).

The Dockerfile itself installs only a subset of dependencies, so it is not evidence that this exact container installs OpenCV. The stronger affected path is the documented Python-3 full-requirements installation.

Sources:

- https://github.com/carla-simulator/scenario_runner/blob/7758d066080f180f8296887ed89b7c723a54706a/requirements.txt
- https://github.com/carla-simulator/scenario_runner/blob/7758d066080f180f8296887ed89b7c723a54706a/Docs/getting_scenariorunner.md
- https://github.com/carla-simulator/scenario_runner/blob/7758d066080f180f8296887ed89b7c723a54706a/srunner/scenariomanager/actorcontrols/visualizer.py
- https://github.com/carla-simulator/scenario_runner/blob/7758d066080f180f8296887ed89b7c723a54706a/Dockerfile

### Old artifact state

PyPI `opencv-python 4.2.0.32` publishes CPython-3.6 Linux wheels, including `cp36-cp36m-manylinux1_x86_64` and `cp36-cp36m-manylinux1_i686` artifacts.

Source: https://pypi.org/project/opencv-python/4.2.0.32/#files

### New artifact state

PyPI `opencv-python 4.8.1.78` still declares `Requires-Python >=3.6`, and its source package retains Python-3.6 build metadata. Its published wheels are `cp37-abi3` artifacts labelled for CPython 3.7+, while a source distribution is also published. The package documentation states that when no compatible wheel exists, package installation can fall back to building from the source distribution.

Sources:

- https://pypi.org/project/opencv-python/4.8.1.78/#files
- https://github.com/opencv/opencv-python/blob/78/setup.py
- https://github.com/opencv/opencv-python/blob/78/pyproject.toml

Bounded transition:

```text
old release: CPython-3.6 Linux binary wheel available
new release: no CPython-3.6-compatible published wheel
             + source distribution available
             + Python-3.6 source metadata retained
```

Therefore the established concern is an **installation-mode/artifact-availability transition**, not proof that Python 3.6 installation is impossible.

## CI boundary

The exact target workflows install requirements on Ubuntu but do not pin or matrix Python 3.6. The unit workflow runs only `srunner/tests/test_xosc_load.py`. No checked status/workflow result was obtained for the exact Dependabot head through the inspected interfaces.

Therefore:

```text
CI installs the dependency somewhere
!=
CI establishes coverage of the Python-3.6 artifact transition
```

and missing checked CI evidence is not treated as failure.

## Existing-evidence gap

- **S001:** declared interpreter-support drop vs target range.
- **S003:** actual dependency-resolution/install failure.
- **S007:** coordinated package-family contradiction.
- **S008:** package metadata can still allow an interpreter while the binary artifact for that interpreter disappears, changing the installation path before application runtime.

That is a materially different mechanism.

## Admission gates

- **Named question:** PASS — exact artifact availability/install-mode transition.
- **Existing-evidence gap:** PASS — no prior case cleanly owns this mechanism.
- **Consequence:** PASS — may teach artifact availability, environment applicability, CI relevance, and investigation stopping.
- **Evidence feasibility:** PASS — exact public repository/package evidence is available.
- **Safe boundary:** PASS — the owned question is answerable through read-only evidence.
- **Negative result:** PASS — discovering a missed compatible wheel would directly refute the hypothesis and remain useful.
- **Claim limit:** PASS — no global compatibility or source-build-success claim.
- **Stop condition:** PASS — stop once artifact availability, source fallback, target relevance, and CI coverage are bounded.
- **Case form:** PASS — untouched real public evidence is sufficient initially.

## Provisional proposition map

These are simulation questions, not product schema.

```text
P1 old CPython-3.6 Linux wheel exists                      expected established
P2 new CPython-3.6 Linux compatible wheel exists           expected refuted
P3 new source distribution + Python-3.6 source path exists expected established
P4 target has relevant Python-3.6/full-requirements context expected bounded established
P5 inspected CI covers exact Python-3.6 artifact transition not established
P6 source fallback succeeds in exact target environment     unresolved / outside owned question
```

The important separation is:

```text
package permits interpreter
!=
binary artifact exists for interpreter/platform
!=
source fallback succeeds
```

## Investigation/stopping objective

For the owned artifact-transition question, exact package artifact inventories and build metadata are already potentially sufficient. A large native source-build observation would answer the deeper P6 proposition rather than the owned P1-P5 question.

S008 therefore tests whether investigation selection can stop after sufficient static evidence instead of escalating merely because a more expensive observation is possible.

## Minimal checkpoints

1. freeze exact proposal and target installation context;
2. freeze exact old/new artifact evidence;
3. evaluate P1-P6 and evidence/coverage boundaries;
4. decide whether any additional observation can still change the owned conclusion;
5. compare the result with S001, S003, S007, and the implemented A/B proposition model.

## Admission result

```text
S008 ADMITTED
primary novelty: binary artifact availability / installation-mode transition
primary confirmation: mechanism-specific proposition and coverage discipline
primary C value: static-evidence sufficiency and deliberate stopping
```

No product implementation or maintainer decision follows from this admission.