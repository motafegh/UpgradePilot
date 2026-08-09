# S007 Post-Case Synthesis — Package-Family Coherence and Investigation Pruning

**Status:** S007 complete at its admitted simulation depth  
**Date:** 2026-08-09  
**Case:** `S007-biomedparse-torch-cuda-family-resolution`  
**Role:** product-discovery / evaluation / Conversation-C pressure-test evidence; non-controlling

## 1. Question answered

S007 asked:

> Given a real Dependabot PR that changes only `torch==2.6.0+cu124` to `torch==2.8.0` while the target keeps TorchVision/TorchAudio 2.6-family CUDA-12.4 pins and explicitly documents a CUDA-12.4 environment, what evidence is actually needed to decide whether the declared package family can form, and should UpgradePilot run a resolver/runtime check merely because one is available?

At the bounded simulation level, the answer is:

> **Authoritative static package/build evidence plus deterministic constraint reasoning is sufficient to refute coherent formation of the exact declared package set. A resolver run would be corroborative, not necessary, and runtime/API investigation should be pruned until the package family is repaired or otherwise made coherent.**

No target code, model weights, CUDA kernels, or package resolver were executed to reach this conclusion.

---

## 2. Real case

Target: `microsoft/BiomedParse#96`

Frozen proposal:

```text
# PyTorch (CUDA 12.4)
-torch==2.6.0+cu124
+torch==2.8.0
 torchvision==0.21.0+cu124
 torchaudio==2.6.0+cu124
```

The requirements file retains the CUDA-12.4 extra index, while the exact base README says the requirements assume CUDA 12.4 and demonstrates direct PyTorch/CUDA runtime use.

The target relevance of the environment is therefore concrete.

---

## 3. Evidence chain

### Target evidence

```text
exact PR/base/head
→ exact changed requirement
→ unchanged TorchVision/TorchAudio CUDA-12.4 pins
→ exact README Python-3.10.14 / CUDA-12.4 installation intent
→ direct target PyTorch/CUDA runtime use
```

### Upstream family evidence

Official PyTorch guidance establishes:

```text
Torch 2.6.0
+ TorchVision 0.21.0
+ TorchAudio 2.6.0
+ CUDA 12.4 supported family
```

while the official 2.8 family is:

```text
Torch 2.8.0
+ TorchVision 0.23.0
+ TorchAudio 2.8.0
+ CUDA 12.6 / 12.8 / 12.9 wheel families
```

Official TorchVision 0.21 release/build source additionally establishes:

```text
setup.py
PYTORCH_VERSION present
→ Requires-Dist torch==PYTORCH_VERSION
```

and the official Linux binary workflow for the 2.6 release line:

```text
installs Torch 2.6 release dependency
→ exports that release version into PYTORCH_VERSION
→ builds TorchVision wheel
→ smoke-checks wheel contains pinned Requires-Dist: torch (==...)
```

Therefore the retained TorchVision 0.21 release contract is pinned to the Torch 2.6 family and cannot share one Torch version with the independent `torch==2.8.0` requirement.

---

## 4. Main discovery A — artifact/package-family coherence can precede runtime semantics

The tempting analysis path was:

```text
PyTorch 2.8 has many behavior changes
→ inspect BiomedParse model code
→ run targeted runtime/GPU checks
```

S007 shows that ordering can be wrong.

The actual first dependency is:

```text
Can the declared package/environment family form coherently?
```

If the answer is already no for the exact proposal, deeper runtime semantics are not yet the next useful question.

This is not because runtime behavior is unimportant. It is because it is **downstream of an earlier necessary condition**.

---

## 5. Main discovery B — a useful check can become unnecessary

At admission time, two reasonable next observations were considered:

1. inspect exact Linux wheel metadata;
2. run an isolated resolver dry-run.

Further authoritative source acquisition then exposed the TorchVision release build contract strongly enough to settle the proposition.

Therefore:

```text
check looked useful at time T1
+
new cheaper authoritative evidence arrives at T2
→ check can be pruned at T2
```

This is important for Conversation C.

Investigation-selection state is **sequential**. A planner must be able to reconsider and cancel an investigation when newly admitted evidence makes its expected information redundant.

---

## 6. Main discovery C — `no further check` is a positive technical result

The final S007 result is not:

```text
we did not test
```

It is:

```text
owned proposition resolved
+
resolver result would mostly corroborate
+
runtime investigation is downstream
→ no further supported check needed for this question
```

That is materially different from unresolved due to unavailable evidence.

Compare:

```text
Buildtest/OpenSSL
exact historical SSL state unavailable
→ unresolved
```

versus:

```text
S007
exact static package/build contract closes package-family proposition
→ stop without execution
```

The same absence of an executed dynamic check therefore has very different meanings depending on proposition state.

---

## 7. Main discovery D — one contradiction can prune redundant family evidence

TorchAudio 2.6.0+cu124 is also retained by the proposal, and its exact dependency contract could be investigated.

But that evidence is unnecessary for the owned package-family question once TorchVision alone establishes an unsatisfiable Torch constraint.

```text
one sufficient contradiction
→ package set cannot resolve coherently
→ second independent contradiction not required
```

This is a concrete example of **decision-relative evidence sufficiency** and protects UpgradePilot from collecting evidence simply because more evidence exists.

---

## 8. Main discovery E — package version identity may require artifact/context awareness

The target starts from:

```text
torch==2.6.0+cu124
```

and proposes:

```text
torch==2.8.0
```

while retaining a CUDA-specific index and local-version sibling packages.

This exposes an important product-discovery point:

```text
package name + public version
```

may be insufficient to understand a real dependency-update environment when local-version/build/artifact family and index/platform intent are material.

S007 does **not** authorize a universal artifact-identity schema. It establishes that future product design must not erase such distinctions when the evidence makes them decision-relevant.

---

## 9. Relationship to S003

S003 proved a real npm install failure caused by a peer-dependency incompatibility.

S007 confirms a broader responsibility:

> Dependency-update impact can become decisive at the **environment-formation/resolution layer before runtime execution**.

But S007 is materially different:

| S003 | S007 |
|---|---|
| npm / TypeScript ecosystem | Python/PyTorch binary ecosystem |
| peer dependency incompatibility | coordinated version-family / wheel-build dependency contract |
| observed failing install evidence central | authoritative static build/package evidence sufficient; install execution pruned |
| sibling same-base comparison aided attribution | exact target requirements + upstream build contract close the question |

So S007 is both **confirmation** and **generality expansion** rather than mere duplication.

---

## 10. Relationship to S006 / Conversation C

S006 selected a dynamic differential reproduction because visible evidence left one target behavior unresolved and the check had high discriminating value.

S007 reaches the opposite outcome:

```text
S006
static/visible evidence insufficient
→ targeted execution selected

S007
static authoritative evidence sufficient
→ targeted execution pruned
```

Together they are a useful paired contrast for Conversation C.

A future investigation-selection method must therefore be capable of both:

```text
SELECT CHECK
```

and:

```text
NO FURTHER CHECK
```

based on the proposition and admitted evidence, not on a general preference for more testing.

---

## 11. What S007 established

### Established at bounded simulation depth

- exact BiomedParse proposal and target environment intent;
- direct target relevance of PyTorch/CUDA;
- official PyTorch 2.6 versus 2.8 coordinated release-family differences;
- official TorchVision 0.21 release build contract pins its Torch dependency to the release/2.6 family;
- exact proposal's direct `torch==2.8.0` requirement cannot be satisfied simultaneously with that retained TorchVision 0.21 family contract;
- the exact declared package set is therefore incoherent at the owned package-family layer;
- a resolver dry-run is not needed to answer that bounded question;
- deeper runtime/API analysis is currently inactive for the exact proposal;
- additional TorchAudio-family evidence is redundant for this specific conclusion.

### Not established

- byte-for-byte Linux wheel METADATA was directly downloaded in this simulation;
- a pip/uv resolver was executed;
- corrected PyTorch-2.8-family requirements would or would not work with BiomedParse;
- GPU/model runtime behavior under PyTorch 2.8;
- global compatibility or safety;
- final maintainer action;
- universal behavior across every platform/index/Python combination.

---

## 12. Stopping decision

S007 stops now at its admitted depth.

Further work such as:

- executing a resolver only to reproduce the expected contradiction;
- downloading a second sibling package's metadata;
- running BiomedParse imports;
- running CUDA/model inference;
- cataloguing all PyTorch 2.8 changes;

would not materially improve the owned package-family conclusion.

A new question may reactivate those investigations only after the proposal changes or a distinct evaluation objective is explicitly admitted.

---

## 13. Bounded result

```text
S007
real public Dependabot PR
+
coordinated CUDA package-family mismatch
+
authoritative static build/package evidence
+
deterministic constraint contradiction
→ exact declared package family cannot form coherently
→ resolver execution pruned
→ runtime semantic investigation pruned
→ stop
```

This is non-controlling discovery/evaluation evidence. Main product design may adopt, modify, reject, or defer its implications through the normal owner for that responsibility.