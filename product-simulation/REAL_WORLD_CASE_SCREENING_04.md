# Real-World Case Screening 04 — Post-Implementation Controls and Artifact Availability

**Date:** 2026-08-11  
**Status:** Completed bounded screening pass; non-controlling discovery/evaluation evidence  
**Branch:** `agent/product-simulation-case-screening-01`  
**Main product revision used for context:** `6202548eeff8c76405b8b53e0e35f0caeef53ef3`

## 1. Purpose

This pass resumes real-world case discovery after the first A/B impact/applicability runtime foundation became implemented and verified on `main`.

It deliberately accepts three useful outcomes:

- **challenge/extension** — a case exposes a materially underrepresented mechanism or evaluation boundary;
- **confirmation/control** — a case independently reproduces an accepted reasoning rule in another real repository;
- **rejection/defer** — target-side evidence does not establish the headline upstream mechanism strongly enough for deeper work.

A candidate does not need to be exotic to be useful. It does need enough exact real-world evidence to justify the amount of simulation work spent on it.

## 2. Candidate summary

| Candidate | Real-world shape | Screening result |
|---|---|---|
| `carla-simulator/scenario_runner#1111` — `opencv-python 4.2.0.32 -> 4.8.1.78` | native binary/distribution availability changes; Python-3.6 wheel path disappears while source-build fallback remains; target source-install path plus direct `cv2` runtime use; CI does not establish Python-3.6 coverage | **PROMOTE TO S008 ADMISSION** |
| `Coded-Vision-Design/jarvis-local-agent#28` — `pydantic-settings 2.14.2 -> 2.15.0` | dependency directly used, but clearest changed mechanism does not activate on target construction/configuration path; nominal required CI gate is ecosystem-irrelevant | **KEEP AS NEGATIVE/CI-RELEVANCE CONTROL** |
| `lucabro/recall-osint#7` — grouped Dependabot update | one PR contains many independent dependency transitions | **KEEP AS INPUT-BOUNDARY CONTROL** |
| `python-dotenv` search candidates | exact repositories/PR evidence unavailable through checked interfaces | **REJECT FOR EVIDENCE FEASIBILITY** |
| exact `h2 4.3.0 -> 4.4.0` search | no clean real Dependabot candidate established | **NO CASE ADMITTED** |

## 3. Candidate A — CARLA ScenarioRunner #1111

### Frozen proposal identity

Repository: `carla-simulator/scenario_runner`  
PR: `#1111`  
Base branch: `master`  
Base SHA: `7758d066080f180f8296887ed89b7c723a54706a`  
Head SHA: `f32ad2d23a9abee47c566dfbed2b822d953a09e2`

Exact changed requirement:

```text
opencv-python==4.2.0.32
→
opencv-python==4.8.1.78
```

Only `requirements.txt` changes in the Dependabot proposal.

Primary source:

- https://github.com/carla-simulator/scenario_runner/pull/1111

### Target dependency/use relationship

At the exact PR base:

- `requirements.txt` pins `opencv-python==4.2.0.32`;
- ScenarioRunner source-install documentation tells Python-3 users to install `requirements.txt` with `pip3`;
- `srunner/scenariomanager/actorcontrols/visualizer.py` imports `cv2` and uses runtime OpenCV functions including `VideoWriter`, `cvtColor`, `vconcat`, drawing/text functions, `imshow`, and `waitKey`;
- `simple_vehicle_control.py` can instantiate that `Visualizer` path.

This establishes a real package installation/runtime relationship. It does **not** establish that every OpenCV release-note mechanism activates.

Sources:

- https://github.com/carla-simulator/scenario_runner/blob/7758d066080f180f8296887ed89b7c723a54706a/requirements.txt
- https://github.com/carla-simulator/scenario_runner/blob/7758d066080f180f8296887ed89b7c723a54706a/Docs/getting_scenariorunner.md
- https://github.com/carla-simulator/scenario_runner/blob/7758d066080f180f8296887ed89b7c723a54706a/srunner/scenariomanager/actorcontrols/visualizer.py

### Exact target Python-3.6 evidence

The exact target base includes a `Dockerfile` built from:

```text
python:3.6-slim
```

That Dockerfile manually installs only a subset of ScenarioRunner dependencies and does **not** by itself establish that `opencv-python` is installed in that container. Therefore it must not be used as proof that this exact Docker build is affected.

It is useful only as exact repository evidence that Python 3.6 remained an explicit target environment at this revision.

The stronger affected installation path is the source-install documentation that directs Python-3 users to install the full `requirements.txt`.

Source:

- https://github.com/carla-simulator/scenario_runner/blob/7758d066080f180f8296887ed89b7c723a54706a/Dockerfile

### Upstream distribution transition

The old PyPI release `opencv-python 4.2.0.32` published interpreter-specific CPython-3.6 wheels, including Linux `manylinux1_x86_64` and `manylinux1_i686` wheels.

Source:

- https://pypi.org/project/opencv-python/4.2.0.32/#files

The proposed `opencv-python 4.8.1.78` release still declares:

```text
Requires-Python >=3.6
```

and its source package build configuration retains Python-3.6 build dependencies.

But its published binary wheels are `cp37-abi3` artifacts labeled for **CPython 3.7+**. PyPI also provides a source distribution, and the package documentation explicitly states that when no compatible wheel exists, `pip` will attempt a source build.

Sources:

- https://pypi.org/project/opencv-python/4.8.1.78/#files
- https://github.com/opencv/opencv-python/blob/78/setup.py
- https://github.com/opencv/opencv-python/blob/78/pyproject.toml

Therefore the bounded established transition for CPython-3.6 Linux is:

```text
4.2.0.32
compatible prebuilt CPython-3.6 Linux wheel available

→

4.8.1.78
no published CPython-3.6-compatible binary wheel
+ source distribution available
+ package metadata/build configuration still permits Python 3.6

→

installation mode can change from prebuilt-wheel acquisition
into source-build fallback
```

This does **not** establish that the source build will fail.

### Existing CI boundary

At the exact target base:

- `.github/workflows/unit_test.yml` installs `requirements.txt` on `ubuntu-20.04` and runs only `srunner/tests/test_xosc_load.py`;
- no explicit `setup-python` version or Python-3.6 matrix is present;
- `.github/workflows/static_code_check.yml` similarly lacks a Python-3.6 matrix;
- no checked combined status or pull-request workflow run was returned for the exact Dependabot head through the available GitHub interfaces.

Interpretation:

```text
CI installs the dependency somewhere
!=
CI proves the CPython-3.6 wheel-to-source-build transition is covered
```

and:

```text
no checked public CI result obtained
!=
CI failed
!=
no testing occurred elsewhere
```

Sources:

- https://github.com/carla-simulator/scenario_runner/blob/7758d066080f180f8296887ed89b7c723a54706a/.github/workflows/unit_test.yml
- https://github.com/carla-simulator/scenario_runner/blob/7758d066080f8296887ed89b7c723a54706a/.github/workflows/static_code_check.yml

### Why this differs materially from S001

S001 asks whether an explicit upstream Python-support drop intersects an exact target declared Python range.

CARLA/OpenCV adds a different mechanism:

```text
package metadata still permits interpreter P
+
old release supplied binary artifact for P
+
new release does not supply binary artifact for P
+
new release still supplies source distribution
→
installation pathway/prerequisites change for P
```

The possible consequence is not simply `unsupported interpreter`.

It is:

```text
binary install
→ source build fallback
→ additional native build/toolchain/prerequisite/time/failure surface
```

Whether that source build actually succeeds is a separate proposition.

### Screening disposition

**Promote to formal S008 admission.**

The owned case question should center on artifact availability, installation-path change, target-environment relevance, CI coverage, and whether static artifact evidence is sufficient to stop before an expensive source build.

Do not turn S008 into a general OpenCV-4.8 compatibility or CVE review.

---

## 4. Candidate B — jarvis-local-agent #28 / pydantic-settings

Repository: `Coded-Vision-Design/jarvis-local-agent`  
PR: `#28`  
Transition: `pydantic-settings 2.14.2 -> 2.15.0`

The exact target imports `BaseSettings`, so package use is real.

However the target constructs its configuration as `Settings()` with no init kwargs, explicitly disables env-file loading, and does not configure the clearest changed `case_sensitive`/init-source conditions from the crossed release.

The repository's required `verify` workflow also recognizes npm/composer dependency updates but has no Python dependency verification path; unsupported ecosystems reach the passing branch.

### Screening value

This independently confirms two existing guards:

```text
dependency presence
!=
affected mechanism activation
```

and:

```text
green/required CI label
!=
relevant coverage of the dependency-update mechanism
```

### Disposition

**Retain as a negative/CI-relevance control. No numbered scenario now.**

---

## 5. Candidate C — recall-osint #7 / grouped Dependabot update

This public Dependabot proposal groups many package transitions into one PR.

That is useful as a boundary case for the current UpgradePilot input model:

```text
one PR
!=
one dependency transition
!=
one technical impact candidate
```

The existing B2 implementation is intentionally bounded around one Python dependency update and must not be generalized to grouped multi-update proposals by silently collapsing all transitions into one candidate.

### Disposition

**Retain as an input-boundary control. No numbered scenario required.**

---

## 6. Search/evidence-feasibility failures

Several `python-dotenv` search hits were not resolvable through the checked repository/PR interfaces, and a tightened exact `h2 4.3.0 -> 4.4.0` search did not produce a clean real Dependabot candidate.

The correct response is to stop spending acquisition effort rather than fabricate a case from release notes alone.

```text
interesting upstream package
!=
real target case established
```

---

## 7. Cross-case findings

### 7.1 Package support and binary artifact availability are different propositions

CARLA/OpenCV demonstrates that a package may continue to declare an interpreter as installable from source while no longer publishing a prebuilt wheel for that interpreter.

Therefore:

```text
Requires-Python permits P
!=
prebuilt artifact exists for P/platform
```

and:

```text
no wheel for P
!=
package impossible to install on P
```

### 7.2 Installation-mode change can be a technical impact mechanism

The target does not need to call a changed OpenCV API for the dependency update to matter.

```text
wheel available
→ direct binary installation

vs

wheel unavailable
→ source-build fallback
```

changes the dependency/environment formation path before application runtime begins.

### 7.3 Static artifact evidence may be sufficient without executing a native build

For the bounded question:

> Did this update remove the CPython-3.6 prebuilt Linux wheel path and introduce source-build fallback?

exact PyPI artifact inventories plus package source/build metadata are already discriminating.

Running a full OpenCV source compilation would answer a **different**, deeper proposition:

> Does the fallback source build succeed in a particular exact environment?

Do not execute the expensive deeper investigation merely because it is technically possible.

### 7.4 CI relevance remains proposition-specific

A workflow that installs the dependency on an unpinned runner interpreter does not establish coverage of a Python-3.6-specific distribution transition.

### 7.5 Confirming and negative cases continue to matter

The jarvis case did not produce a new mechanism, but it independently validates existing activation and CI-relevance boundaries. The grouped Dependabot case validates an input-scope boundary.

These are useful external-validity results even without new S00x numbers.

## 8. Result

1. Admit CARLA/OpenCV #1111 as S008 with a bounded artifact-availability / source-build-fallback question.
2. Keep jarvis #28 as a real negative/CI-relevance control.
3. Keep grouped Dependabot proposals as input-boundary evidence, not as one-transition simulation fixtures.
4. Do not broaden current product implementation merely because S008 exposes a new future mechanism family.
5. Use S008 to test A/B proposition transfer and C investigation/stopping discipline, especially the difference between `artifact unavailable`, `source install still possible`, and `source build actually succeeds`.

No target mutation, native source build, maintainer action, product architecture change, or universal OpenCV compatibility claim is authorized by this screening.