# S007 Candidate Screening — BiomedParse PyTorch/CUDA Family Resolution

**Date:** 2026-08-09  
**Status:** **ADMITTED — prospective untouched real public case**  
**Candidate:** `microsoft/BiomedParse#96`  
**Case ID:** `S007-biomedparse-torch-cuda-family-resolution`  
**Role:** product-discovery / evaluation / Conversation-C pressure-test evidence; non-controlling

## 1. Admission question

> Given a real Dependabot PR that changes only `torch==2.6.0+cu124` to `torch==2.8.0` while the target keeps `torchvision==0.21.0+cu124`, `torchaudio==2.6.0+cu124`, a CUDA-12.4 package index, and documentation stating that the requirements assume CUDA 12.4, can UpgradePilot correctly distinguish **environment/package-family formation** from later runtime semantics and choose the smallest sufficiently discriminating investigation in the right order?

The case is **not** admitted to answer:

> Is BiomedParse globally compatible with PyTorch 2.8?

That broader question is outside the case boundary.

---

## 2. Frozen proposal identity

```text
repository: microsoft/BiomedParse
pull request: 96
base branch: v2
base SHA: ac054c43b0f6cb579e00fe7d28bfbf29716c62b3
head SHA: b8e53d5232ebb3e8068fed4fe79450f720665603
changed file: assets/requirements/requirements.txt
```

Exact proposal:

```text
# PyTorch (CUDA 12.4)
-torch==2.6.0+cu124
+torch==2.8.0
 torchvision==0.21.0+cu124
 torchaudio==2.6.0+cu124
```

The file also retains:

```text
--extra-index-url https://download.pytorch.org/whl/cu124
```

Sources:

- https://github.com/microsoft/BiomedParse/pull/96
- https://github.com/microsoft/BiomedParse/blob/ac054c43b0f6cb579e00fe7d28bfbf29716c62b3/assets/requirements/requirements.txt
- https://github.com/microsoft/BiomedParse/blob/b8e53d5232ebb3e8068fed4fe79450f720665603/assets/requirements/requirements.txt

---

## 3. Real target relevance already established for admission

The exact target README at the PR base states:

- create a Python `3.10.14` environment;
- install `assets/requirements/requirements.txt`;
- the requirements file assumes **CUDA 12.4**;
- inference imports `torch`;
- inference selects CUDA when available;
- the model and inputs are moved through PyTorch execution.

Source:

- https://github.com/microsoft/BiomedParse/blob/ac054c43b0f6cb579e00fe7d28bfbf29716c62b3/README.md

Therefore this is not merely package presence. The proposed dependency participates in the documented target runtime/environment contract.

---

## 4. Upstream package-family evidence already established for admission

Official PyTorch previous-version instructions describe coordinated families.

For PyTorch `2.6.0`, the official CUDA-12.4 installation family is:

```text
torch 2.6.0
+ torchvision 0.21.0
+ torchaudio 2.6.0
+ CUDA 12.4 index
```

For PyTorch `2.8.0`, the official family is:

```text
torch 2.8.0
+ torchvision 0.23.0
+ torchaudio 2.8.0
```

with documented CUDA wheel families `12.6`, `12.8`, and `12.9`, not the earlier `12.4` family.

Sources:

- https://pytorch.org/get-started/previous-versions/
- https://github.com/pytorch/vision

A PyTorch release-engineering issue also preserves extracted metadata from an official `torchvision-0.21.0+cu124` wheel showing:

```text
Requires-Dist: torch (==2.6.0+cu124)
```

Source:

- https://github.com/pytorch/pytorch/issues/157476

This is strong admission evidence for a coordinated-package constraint. The case must still distinguish what is established directly by authoritative metadata from what should be confirmed by a resolver observation.

---

## 5. Public CI/evidence boundary at admission

The screening checked the exact PR head through available GitHub combined-status and pull-request workflow-run interfaces. No public status/check or pull-request workflow run was returned.

Interpretation:

```text
no checked public CI observation obtained
!=
no testing happened anywhere
```

No target workflow is rerun or mutated by this scenario.

---

## 6. Why S001–S006 and existing challenge evidence do not already answer this case

### S001

Covers an upstream Python-support drop refuted by an exact target `requires-python` declaration.

S007 instead centers on a **coordinated binary/distribution package family** and whether the intended environment can resolve coherently.

### S003

Covers a real npm peer-dependency install failure and causal attribution.

S007 intentionally tests whether a similar high-level responsibility generalizes into a materially different Python packaging shape:

- PEP 440 public/local-version identity;
- CUDA-specific wheel indexes;
- coordinated Torch/TorchVision/TorchAudio release families;
- platform/native artifact intent;
- direct target runtime use.

A successful S007 may therefore **confirm** some S003 reasoning while still broadening external validity.

### S006

Covers selection of an old/new behavioral differential reproduction after a target behavior-path coverage gap.

S007 tests a different investigation-order question:

> If an earlier package-family/environment proposition can be established or refuted before runtime behavior is reachable, should deeper semantic/runtime checks be pruned?

### Buildtest/OpenSSL challenge evidence

Buildtest shows an environment-mediated candidate that remained unresolved because exact historical SSL state was unavailable.

S007 gives a complementary environment case with substantially stronger exact target package declarations and upstream package-family evidence.

---

## 7. Admission gates

### Q — Named question: PASS

The question is bounded to coherent formation of the target's declared package/platform family and investigation ordering before runtime semantics.

### G — Existing-evidence gap: PASS

Existing cases do not adequately cover Python local-version/platform artifact identity plus coordinated CUDA package-family constraints in a directly used ML runtime stack.

### C — Product/evaluation consequence: PASS

Possible consequences include learning whether UpgradePilot needs to preserve:

- artifact/distribution identity separately from public package version;
- coordinated-package constraints as applicability evidence;
- resolver/static-metadata checks before expensive runtime checks;
- explicit pruning when an earlier necessary environment proposition fails.

These are discovery implications only, not pre-authorized product fields/classes.

### E — Evidence feasibility: PASS

Exact public PR/base/head, target requirements, target documentation, official upstream version-family instructions, and package metadata evidence are available read-only.

### S — Safe boundary: PASS

The case can be investigated with public read-only evidence and isolated non-target-mutating resolution checks if later justified. No target code execution is required for the initial question.

### N — Negative result remains useful: PASS

If a controlled resolver does **not** reproduce the expected contradiction, that result would challenge the current interpretation of package-index/local-version semantics or package metadata and would be valuable evidence rather than a failed scenario.

### L — Claim limit: PASS

The case may establish only bounded facts about:

- exact declared package constraints;
- exact documented environment intent;
- package-family metadata/compatibility;
- whether a bounded resolver observation can or cannot form the proposed environment;
- investigation ordering/pruning for this question.

It must not establish:

- global BiomedParse compatibility with PyTorch 2.8;
- GPU runtime correctness;
- model-output correctness;
- performance;
- update safety;
- maintainer merge/block/defer action;
- universal PyTorch packaging behavior across every OS/Python/index configuration.

### T — Stop condition: PASS

Stop when the scenario can answer:

1. what exact proposition controls whether the intended package environment can form;
2. which exact static evidence establishes/refutes/supports it;
3. whether one bounded resolver observation adds material discriminating value;
4. whether deeper runtime checks should be inactive until package-family formation is coherent;
5. what remains unresolved after that bounded result.

Do not continue into general PyTorch migration/runtime testing merely because more checks are possible.

### F — Case form: PASS

Use the untouched real public PR as the primary case. Add only narrowly controlled resolver observations if they are needed to discriminate the frozen proposition.

No synthetic target repository is necessary at admission.

---

## 8. Provisional mechanism-specific candidates

These are **questions to evaluate**, not frozen product taxonomy.

### Candidate P — package-family resolution

```text
upstream/package-family reality
TorchVision 0.21 CUDA-12.4 belongs to the Torch 2.6 family

+

target exposure/path
exact target requirements install Torch + TorchVision + TorchAudio together

+

activation
proposal selects Torch 2.8 while retaining TorchVision/TorchAudio 2.6 CUDA-12.4 pins

+

possible consequence
requirements cannot resolve into one coherent environment
```

This is the first owned candidate because failure here can prune deeper runtime semantics.

### Candidate Q — intended CUDA-family preservation

```text
exact target documents CUDA 12.4 assumptions
+
proposal removes +cu124 from the Torch pin
+
PyTorch 2.8 official binary families no longer include CUDA 12.4
→ does the proposal still represent the target's documented environment intent?
```

This may overlap with package-family resolution evidence but is conceptually a distinct proposition. Do not collapse them merely because one observation may inform both.

### Candidate R — later runtime/API behavior

PyTorch 2.8 contains many runtime and behavioral changes.

This candidate is intentionally **inactive initially**.

It earns investigation only if the earlier environment/package-family question becomes coherent enough that runtime execution is meaningful.

---

## 9. Conversation-C pressure-test objective

S007 should test this general investigation-order hypothesis:

```text
unresolved proposition
↓
identify candidate observations
↓
prefer authoritative/deterministic evidence that can settle an earlier necessary proposition
↓
use a resolver check only if it materially confirms/discriminates remaining uncertainty
↓
prune expensive runtime/semantic investigation when the intended environment cannot yet form
```

Potential failure modes to watch:

- treating `pip install` as automatically superior to exact static metadata;
- treating one resolver failure as global PyTorch incompatibility;
- running GPU/model inference before package-family coherence is established;
- ignoring local-version/index/platform semantics;
- conflating Torch, TorchVision, and TorchAudio into one opaque `PyTorch risk` label;
- treating lack of public CI as evidence of failure;
- using historical eventual maintainer action as correctness proof.

---

## 10. Planned minimal checkpoints

The case should begin proportionately:

### S007-1 — identity and target contract

Freeze exact PR/base/head, requirements, documented Python/CUDA context, and public CI observation boundary.

### S007-2 — authoritative package-family evidence

Bind exact official PyTorch/TorchVision/TorchAudio version-family and artifact/metadata evidence relevant to the frozen requirements.

### S007-3 — proposition map

State the smallest exact environment/package-family propositions and what evidence would establish, refute, conflict, or leave each unresolved.

### S007-4 — investigation-choice freeze

Before executing any controlled resolver check, record:

- what remaining uncertainty the check targets;
- possible observable outcomes;
- how each outcome changes proposition state;
- why a cheaper/static observation is insufficient if execution is still selected.

### S007-5 — bounded resolver observation, only if justified

Use an isolated, non-target-mutating, package-resolution-only method. Do not execute BiomedParse code, model weights, CUDA kernels, or untrusted repository code.

### S007-6 — stopping / cross-case synthesis

Compare the result with S003, S006, Buildtest/OpenSSL, and Conversation-C investigation-selection semantics. Stop at the admitted claim boundary.

---

## 11. Admission result

```text
S007 ADMITTED
form: untouched real public PR + optional bounded resolver observation
primary novelty: coordinated CUDA package-family / artifact identity / investigation ordering
primary confirmation value: tests whether S003-style resolution reasoning generalizes into Python native/platform packaging
primary C value: tests static-evidence-first sequencing, resolver discrimination, pruning, and justified stopping
```

No product implementation, target mutation, maintainer decision, or general PyTorch compatibility claim is authorized by this admission.