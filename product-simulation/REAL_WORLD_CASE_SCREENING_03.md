# Real-World Case Screening 03 — Diversity, Confirmation, and Conversation-C Pressure

**Date:** 2026-08-09  
**Status:** Completed bounded screening pass; non-controlling discovery evidence  
**Branch:** `agent/product-simulation-case-screening-01`  
**Purpose:** Screen untouched real public dependency-update pull requests for materially useful UpgradePilot evidence without requiring every useful case to be novel, exotic, or immediately aligned with the active main-branch conversation.

## 1. Screening posture

This pass deliberately uses a lower-friction discovery posture than full scenario admission.

Useful candidates may:

- expose a materially underrepresented dependency-update mechanism;
- challenge the current impact/applicability/investigation model;
- confirm that an existing reasoning pattern generalizes to another real repository;
- reveal that dramatic upstream release notes are irrelevant to the exact target;
- expose acquisition/evidence confounding even when no scenario is admitted.

The pass therefore does **not** treat confirmation as failure and does **not** require a candidate to satisfy a predetermined novelty category.

Full S00x promotion still requires the existing `CASE_SELECTION_FRAMEWORK_V2.md` admission gates.

## 2. Candidate summary

| Candidate | Real-world shape | Screening result |
|---|---|---|
| `microsoft/BiomedParse#96` — torch `2.6.0+cu124 -> 2.8.0` | coordinated PyTorch/CUDA artifact family, local-version identity, package-index/platform coupling, no visible PR CI | **PROMOTE TO S007 ADMISSION** |
| `carla-simulator/scenario_runner#1111` — opencv-python `4.2.0.32 -> 4.8.1.78` | direct target runtime use plus broad Python/platform/distribution/API interval | **KEEP — strong second deep-screening candidate** |
| `aws/aws-sdk-pandas#3332` — urllib3 `2.6.3 -> 2.7.0` | support-floor concern cleanly outside exact target Python range | **KEEP AS CONFIRMATION / STOPPING CONTROL** |
| `nathom/streamrip#862` — pycares `4.5.0 -> 4.9.0` | native/network resolver package plus large Poetry lock-format regeneration | **DEFER — useful confounding case, mixed-variable overload** |
| `microsoft/DCVC#141` — protobuf `4.25.8 -> 5.29.6` | release interval appears rich, but obvious target codegen/proto path not established | **DEFER — target mechanism insufficiently established** |
| `google-research/language-table` torch/OpenCV Dependabot updates | potentially large framework/distribution intervals | **DEFER — indexed target-use evidence weak; do not infer absence** |

## 3. Candidate A — BiomedParse #96

### Frozen proposal identity

Repository: `microsoft/BiomedParse`  
PR: `#96`  
Base branch: `v2`  
Base SHA: `ac054c43b0f6cb579e00fe7d28bfbf29716c62b3`  
Head SHA: `b8e53d5232ebb3e8068fed4fe79450f720665603`

Exact changed requirement:

```text
torch==2.6.0+cu124
→
torch==2.8.0
```

The same requirements file keeps:

```text
--extra-index-url https://download.pytorch.org/whl/cu124

torchvision==0.21.0+cu124
torchaudio==2.6.0+cu124
```

Sources:

- PR: https://github.com/microsoft/BiomedParse/pull/96
- exact base requirements: https://github.com/microsoft/BiomedParse/blob/ac054c43b0f6cb579e00fe7d28bfbf29716c62b3/assets/requirements/requirements.txt
- exact head requirements: https://github.com/microsoft/BiomedParse/blob/b8e53d5232ebb3e8068fed4fe79450f720665603/assets/requirements/requirements.txt

### Exact target context

The exact base README says the requirements file assumes **CUDA 12.4** and shows model inference using `torch`, selecting CUDA when available, moving the model to the device, and executing inference under `torch.no_grad()`.

Source:

- https://github.com/microsoft/BiomedParse/blob/ac054c43b0f6cb579e00fe7d28bfbf29716c62b3/README.md

Therefore this is not merely a declared or test-only dependency. PyTorch and the CUDA-family installation are target-relevant runtime/environment responsibilities.

### Upstream family evidence

Official PyTorch previous-version instructions pair:

```text
PyTorch 2.6.0
+ torchvision 0.21.0
+ torchaudio 2.6.0
+ CUDA 12.4 installation option
```

while PyTorch 2.8.0 is documented with:

```text
torch 2.8.0
+ torchvision 0.23.0
+ torchaudio 2.8.0
+ CUDA 12.6 / 12.8 / 12.9 wheel families
```

and not the earlier CUDA-12.4 family.

Sources:

- https://pytorch.org/get-started/previous-versions/
- https://github.com/pytorch/vision

The PyTorch issue `pytorch/pytorch#157476` also preserves extracted metadata for an official `torchvision-0.21.0+cu124` wheel showing:

```text
Requires-Dist: torch (==2.6.0+cu124)
```

Source:

- https://github.com/pytorch/pytorch/issues/157476

This is strong evidence of an exact coordinated-package constraint that directly conflicts with the proposed standalone `torch==2.8.0` pin if that CUDA-12.4 torchvision artifact is selected.

### Public CI state

No public pull-request workflow run or combined status was returned for the exact PR head through the checked GitHub interfaces during this screening.

This is evidence of **unavailable/not-observed checked CI through those interfaces**, not evidence that no testing occurred elsewhere.

### Why this is materially useful

This case adds a Python packaging shape not represented cleanly by S001–S006:

```text
one package pin changes
+
coordinated framework-family pins remain old
+
local-version / platform artifact identity matters
+
package index is platform-family-specific
+
target documentation declares CUDA-family intent
```

It also provides a strong Conversation-C question:

> When exact static package metadata can already expose a coordinated-version contradiction, should UpgradePilot recommend or execute a broader runtime check, run only a bounded resolver/installability check for confirmation, or stop the deeper runtime investigation until the package-family contradiction is repaired?

The key distinction is:

```text
static authoritative incompatibility evidence
!=
need to execute expensive runtime semantics
```

### Screening disposition

**Promote to formal S007 admission.**

The scenario must stay bounded to package-family/artifact/environment applicability and investigation ordering. It must not expand into a general PyTorch 2.8 migration review.

---

## 4. Candidate B — CARLA ScenarioRunner #1111

### Frozen proposal identity

Repository: `carla-simulator/scenario_runner`  
PR: `#1111`  
Base SHA: `7758d066080f180f8296887ed89b7c723a54706a`  
Head SHA: `f32ad2d23a9abee47c566dfbed2b822d953a09e2`

Change:

```text
opencv-python==4.2.0.32
→
opencv-python==4.8.1.78
```

Source:

- https://github.com/carla-simulator/scenario_runner/pull/1111

### Exact target coupling

At the exact Dependabot base revision, `srunner/scenariomanager/actorcontrols/visualizer.py` imports `cv2` and uses concrete OpenCV runtime behavior including:

- `cv2.VideoWriter_fourcc`;
- `cv2.VideoWriter`;
- `cv2.cvtColor`;
- `cv2.vconcat`;
- `cv2.circle`;
- `cv2.putText`;
- `cv2.imshow`;
- `cv2.waitKey`.

Source:

- https://github.com/carla-simulator/scenario_runner/blob/7758d066080f180f8296887ed89b7c723a54706a/srunner/scenariomanager/actorcontrols/visualizer.py

This direct runtime path was itself historically introduced as an OpenCV camera-display capability in merged PR `#609`.

### Upstream interval pressure

The Dependabot release evidence includes materially different mechanisms in one interval, including:

- dropped Python 3.6 support / added Python 3.11 support;
- macOS and Musl/Alpine distribution fixes;
- Python binding fixes and additions;
- GPU-memory `GpuMat`/`Stream` binding work;
- WebP security remediation.

Therefore the target's direct `cv2` usage is established, but applicability must still be evaluated **per mechanism**, not as one aggregate `opencv_4_8_risk`.

### Screening disposition

**Keep as a strong second deep-screening candidate.**

It is valuable both as a confirmation of direct exposure reasoning and as a test of whether UpgradePilot can avoid treating a rich release interval as one undifferentiated impact candidate.

Do not admit it as S008 merely because S007 exists. Revisit after S007 or if Conversation C/D needs a direct-runtime contrast.

---

## 5. Candidate C — AWS SDK for pandas #3332

Repository: `aws/aws-sdk-pandas`  
PR: `#3332`  
Base SHA: `919aa1e068183aee9ddc6139f34be629f9d11302`  
Head SHA: `7393b2171d4fc7a2f6f682fe56433c07a9fba1cf`  
Disposition: merged.

Change:

```text
urllib3 2.6.3
→
urllib3 2.7.0
```

Upstream 2.7.0 drops Python 3.9 support among several unrelated mechanisms.

Exact target `pyproject.toml` declares:

```text
requires-python = ">=3.10, <4.0"
```

Sources:

- https://github.com/aws/aws-sdk-pandas/pull/3332
- https://github.com/aws/aws-sdk-pandas/blob/919aa1e068183aee9ddc6139f34be629f9d11302/pyproject.toml

### Why this matters despite low novelty

For the specific Python-3.9 support-drop candidate:

```text
upstream concern: Python 3.9 no longer supported
+
exact target declaration: Python >=3.10
→
bounded target applicability refuted
```

This independently confirms the S001-style proposition/refutation pattern in a different real repository and release interval.

It does **not** establish that every other urllib3 2.7 mechanism is irrelevant or that the update was safe merely because the PR merged.

### Screening disposition

**Retain as a confirmation/stopping control; no full scenario required now.**

---

## 6. Candidate D — streamrip #862 / pycares

Repository: `nathom/streamrip`  
PR: `#862`  
Base SHA: `5bcadd3c6a375ef432a78e371800b97f18f6daa3`  
Head SHA: `7c610fc85a9930e1b0f1b84859d551db1c6d58ed`

Change:

```text
pycares 4.5.0
→
4.9.0
```

The upstream interval contains native/platform and concurrency material such as Windows ARM64 support and a shutdown-race fix.

However, the Dependabot diff also contains a very large Poetry lock-format/regeneration rewrite, including lock metadata/group/marker changes unrelated to pycares semantics.

### Screening disposition

**Defer as a mixed-variable/confounding-evidence candidate.**

Potential future value:

```text
dependency-specific change
+
large lock-generator/tooling churn
→
how should evidence attribution avoid treating every changed lock detail as dependency impact?
```

That is useful, but it is not the cleanest first post-B scenario.

---

## 7. Candidate E — DCVC #141 / protobuf

Repository: `microsoft/DCVC`  
PR: `#141`  
Change: protobuf `4.25.8 -> 5.29.6` in `DCVC-family/EVC/requirements.txt`.

The upstream interval appears rich enough to suggest code-generation/schema/runtime-contract questions.

But repository-tree screening did not establish an obvious `.proto` or generated `*_pb2.py` path in the affected target subtree. That absence is **not** proof that protobuf is unused; it simply removes the easiest generated-artifact applicability story.

### Screening disposition

**Defer until a concrete target mechanism is established.**

This is a useful negative screening result:

```text
rich upstream release interval
!=
target-relevant mechanism established
```

---

## 8. Candidate F — language-table torch/OpenCV updates

Real Dependabot updates in `google-research/language-table` cross large Torch/OpenCV intervals, but repository code-search attempts did not establish indexed `torch.*`, `torch.load`, or `cv2` target usage.

Search non-observation is not global evidence of absence, so the correct result is neither `unused` nor `not applicable`.

### Screening disposition

**Defer.**

A stronger source would be required to establish the dependency's target role before deeper release-mechanism analysis is justified.

---

## 9. Cross-case discoveries from this screening pass

### 9.1 Confirmation cases are useful evidence

The AWS/urllib3 case shows that a known reasoning pattern can generalize cleanly to another real repository. A case need not invent a new domain concept to improve confidence in a product rule.

### 9.2 Release-note richness is a poor proxy for case quality

DCVC/protobuf and the language-table candidates looked attractive from upstream change volume. Target-side screening weakened them.

BiomedParse became stronger because exact target requirements and platform intent exposed a concrete package-family contradiction.

### 9.3 Distribution/artifact identity can be part of applicability

BiomedParse demonstrates that the relevant object is not always only:

```text
package name + public version
```

Local-version/platform artifacts, index selection, and coordinated package families can materially define the proposed environment.

This is discovery evidence only; no product runtime identity schema is implied.

### 9.4 Static evidence can outrank execution in investigation order

A resolver/install test may be useful confirmation, but an expensive runtime check is not the first investigation when exact declared pins and authoritative package metadata already expose a contradiction that prevents the intended environment from coherently forming.

This is a strong Conversation-C pressure point:

```text
investigation value
includes sequencing and pruning,
not only selecting the smallest executable check
```

### 9.5 Direct usage still does not collapse mechanism-specific reasoning

CARLA directly uses OpenCV, yet one broad OpenCV release interval still contains multiple independent mechanisms. Direct target use establishes a relationship, not applicability of every crossed upstream change.

---

## 10. Result and next action inside this simulation workspace

This pass is complete enough to act on.

1. **Admit BiomedParse #96 as S007** with a bounded package-family/artifact/environment and investigation-order question.
2. Preserve CARLA #1111 as the strongest direct-runtime contrast for later deep screening.
3. Preserve AWS #3332 as a confirmation/stopping control without creating a full scenario.
4. Do not spend more acquisition effort on deferred candidates unless a later question reactivates them.
5. Use S007 alongside S006/Kedro/Buildtest/pip-audit when pressure-testing Conversation-C investigation-selection semantics.

No maintainer action, target mutation, compatibility claim, or product architecture decision is authorized by this screening.