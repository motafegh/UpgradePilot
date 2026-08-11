# Real-World Case Screening 06 — Candidate-Discovery Breadth

**Date:** 2026-08-12  
**Status:** Completed screening pass; S010 candidate selected  
**Branch:** `agent/product-simulation-case-screening-02`  
**Product context:** `main@538c5c1ae56ddcd60e1e9bcf0a8a2c6d22b90471`

## 1. Screening question

This pass follows [`CANDIDATE_DISCOVERY_COVERAGE_PRESSURE_TEST_01.md`](CANDIDATE_DISCOVERY_COVERAGE_PRESSURE_TEST_01.md).

The target shape was:

> an untouched real single-dependency Python Dependabot proposal where more than one independently grounded mechanism can enter consideration, ideally with different target-side states, so discovery cannot stop safely after the first plausible concern.

Novelty was preferred but not required. Confirming/pruning cases remain valid evidence.

This pass did **not** ask whether each dependency update was globally safe, mergeable, compatible, or fully understood.

## 2. Candidate summary

| Candidate | Transition/proposal | Discovery result | Disposition |
|---|---|---|---|
| Fasal-Pramaan #45 | NumPy `2.1.3 → 2.5.1` | multiple upstream mechanisms discovered; target grounding prunes them on normal container path | retain as broad-discovery/applicability-pruning control |
| Cactus #198 | cryptography `48.0.0 → 49.0.0` | one strong artifact mechanism, one lexical false friend, one real-but-unresolved X.509 mechanism | retain as mixed-state discovery control |
| Chia #21223 | cryptography `48.0.1 → 50.0.0` | one strong Intel-macOS artifact mechanism; several release mechanisms not established in target | retain as broad-release/pruning control |
| Flow Forecast #846 | NumPy `1.26 → 2.0.2` | target is NumPy-heavy, but bounded screening did not establish two distinct target-grounded mechanisms | do not promote |
| podcast-script #36 | NumPy requirement `<2.0,>=1.26 → >=1.26,<3.0` | multiple independently grounded NumPy-2 mechanisms exist on one real transitive runtime path with different target handling states | **select for S010** |

## 3. Fasal-Pramaan #45 — broad discovery correctly pruned by target evidence

**Repository:** `dhrrishitvdeka/Fasal-Pramaan`  
**PR:** `#45`  
**Base:** `352583a95cb3f6f3da88bc4d6d68589aac604392`  
**Head:** `90118e3a280b7704a2edf1101a89b37926927a4d`  
**Proposal:** `numpy==2.1.3 → numpy==2.5.1`

### Upstream mechanisms surfaced

The NumPy release evidence exposes at least two distinct structured concerns:

1. runtime/interpreter support — NumPy 2.5.1 supports Python 3.12–3.14;
2. source-build/toolchain support — the minimum supported GCC rises from 9.3 to 10.3.

Both are legitimate discovery candidates before target grounding.

### Target grounding

The exact AI Dockerfile uses:

```text
FROM python:3.12-slim
```

and installs the Python requirements without installing a compiler toolchain.

For the normal Python-3.12 Linux path, a compatible NumPy 2.5.1 wheel is available.

Therefore:

```text
Python-version mechanism discovered
→ target Python 3.12 remains supported
→ no target conflict established
```

and:

```text
GCC-floor mechanism discovered
→ source-build branch not established on normal wheel-backed path
→ no target conflict established
```

### Screening lesson

This is a strong control for:

```text
broad candidate discovery
+
independent target applicability pruning
```

Finding multiple upstream mechanisms does not mean the target is affected by multiple mechanisms.

**Disposition:** retain as a control; do not admit S010.

## 4. Cactus #198 — mixed candidate states from one cryptography transition

**Repository:** `Cactus-Network/cactus-blockchain`  
**PR:** `#198`  
**Base:** `030759c5416111c09ebd2111ad65c56863459351`  
**Proposal:** `cryptography 48.0.0 → 49.0.0`

The release interval contains several independent changes. Three were screened against exact target evidence.

### Mechanism A — x86_64 macOS wheel removal

cryptography 49 removes x86_64 macOS wheels.

The target actively builds an Intel macOS installer on `macos-15-intel` and installs the Python package during that workflow.

Therefore a real target artifact/serviceability relationship is established.

Do **not** infer that the fallback source build fails; that is a separate proposition.

### Mechanism B — ChaCha20 semantic change

The target uses `ChaCha20Poly1305`.

The breaking release change concerns the lower-level `ChaCha20` algorithm's nonce/counter interpretation.

Therefore:

```text
lexically related crypto primitive
!=
affected mechanism
```

This candidate is pruned rather than promoted merely because both names contain `ChaCha20`.

### Mechanism C — stricter X.509 certificate loading

The target genuinely loads X.509 certificates and can accept private CA material.

However:

- its default/generated CA path is RSA;
- the bundled CA inspected in screening is RSA;
- the cryptography-49 stricter behavior concerns malformed ECDSA/DSA signature `AlgorithmIdentifier` encodings with NULL parameters.

So the relation exists, but the exact narrow activation condition remains unresolved.

### Screening lesson

One release transition can yield:

```text
candidate A → strong target relevance
candidate B → false-friend / refuted relation
candidate C → real relation, activation unresolved
```

This is excellent discovery/applicability evidence even though it does not produce two positive applicable candidates.

**Disposition:** retain as mixed-state control; not the cleanest S010.

## 5. Chia #21223 — release richness must be target-filtered

**Repository:** `Chia-Network/chia-blockchain`  
**PR:** `#21223`  
**Base:** `9489b5a380f521aca9c666f46fc1229533feb7f8`  
**Proposal:** `cryptography 48.0.1 → 50.0.0`

The crossed release interval contains many security/parser/platform changes, including:

- x86_64 macOS wheel removal;
- PKCS#7 decryption changes;
- OCSP changes;
- SCT parsing changes;
- DER/public-key parsing changes;
- other cryptographic behavior changes.

Exact target screening established an active `macos-15-intel` installer workflow, so the x86_64 macOS artifact change is target-relevant.

Bounded repository searches did **not** establish target use of the screened PKCS#7, OCSP, SCT, FFDH, or strict DER-key mechanisms.

### Screening lesson

```text
large security-heavy release interval
!=
many target candidates
```

Candidate-discovery breadth must remain coupled to target evidence and must tolerate pruning most of a rich upstream release.

**Disposition:** retain as broad-release/pruning control; no S010.

## 6. Flow Forecast #846 — NumPy-heavy target, insufficient discriminating breadth

**Repository:** `AIStream-Peelout/flow-forecast`  
**PR:** `#846`  
**Base:** `9a2af06685db4a635eb21e57d8e522a355f85286`  
**Head:** `bf5137db2767ca392971dfd538bded130bd164f6`  
**Proposal:** `numpy==1.26 → numpy==2.0.2`

The repository uses NumPy throughout forecasting, preprocessing, evaluation, and model code.

NumPy 2.0 crosses several materially different upstream changes, including namespace removals, promotion changes, copy semantics, C-API/ABI changes, and other behavior changes.

However, bounded screening did not establish the specific high-signal namespace removals checked (`np.float_`, `np.complex_`, `np.mat`, `np.string_`, `np.Infinity`, `np.NaN`, `np.cast`, `np.lookfor`, `np.who`) in target code, and the exact repository tree does not expose a project-owned compiled NumPy extension surface.

That does **not** prove NumPy 2 is compatible with Flow Forecast. It only means this screening pass did not obtain the clean two-mechanism evidence required for S010.

**Disposition:** do not promote; useful reminder that direct NumPy use + major version jump still does not establish a particular changed mechanism.

## 7. Selected S010 candidate — podcast-script #36

**Repository:** `invaderDMG/podcast-script`  
**PR:** `#36`  
**Base:** `27a879ed2f215e88d4a617bd259e6595d524b79f`  
**Head:** `327196a5f628bfb3a7af47621d976425f9545171`  
**Proposal:** broaden only the NumPy requirement:

```text
numpy>=1.26,<2.0
→
numpy>=1.26,<3.0
```

This is a requirement-broadening proposal, not an exact lock transition to one NumPy-2 release. Its technical consequence is that a fresh supported resolution may now select NumPy 2.x.

### Exact target dependency path

At the base revision:

```text
podcast-script
→ runtime dependency inaSpeechSegmenter==0.7.6
→ NumPy-dependent feature/segmentation stack
```

`src/podcast_script/segment.py` lazily constructs and invokes `inaSpeechSegmenter.Segmenter` on the production segmentation path.

The target also explicitly records the NumPy `<2` cap as intentional compatibility control rather than a stale pin.

### Mechanism A — `numpy.lib.pad` removal

inaSpeechSegmenter `v0.7.6` exact upstream source calls:

```python
numpy.lib.pad(...)
```

inside its feature framing path.

NumPy 2.0's official migration guide states that `np.lib` was reduced to a small explicit public surface; `pad` is not one of the retained members and normal access should move to the main NumPy namespace.

The target explicitly cites this use as one reason for the `<2` guard.

This mechanism is therefore independently grounded by:

- exact target dependency/version contract;
- exact target runtime use;
- exact inaSpeechSegmenter `v0.7.6` source;
- NumPy 2 migration evidence.

### Mechanism B — generator input to `np.vstack`

The target documents another NumPy-2 incompatibility on the same runtime stack: vendored/transitive pyannote viterbi utilities pass generators to `np.vstack`.

Unlike Mechanism A, the target does **not** rely only on the NumPy version cap for this condition. Before constructing the heavy segmenter it runs a local compatibility shim:

```text
_patch_pyannote_viterbi_for_modern_numpy()
```

which replaces the affected pyannote helper functions with list-materializing variants before calling `np.vstack`.

The shim is explicit executable target evidence that this is a distinct compatibility mechanism and that the target handles it differently.

### Why this is stronger than a simple incompatibility case

The same proposed NumPy broadening exposes at least two real mechanisms along the same runtime path:

```text
Mechanism A
inaSpeechSegmenter uses np.lib.pad
→ target relies on NumPy <2 guard
→ broadening removes that protection

Mechanism B
pyannote passes generator to np.vstack
→ target has a local compatibility shim
→ mechanism is recognized but separately mitigated
```

Therefore:

```text
first valid NumPy-2 concern found
!=
discovery complete
```

and:

```text
same dependency transition
+ same transitive runtime path
!=
same candidate state or same mitigation
```

### Important claim boundary

Do not say:

- the PR installs NumPy 2 immediately in every environment;
- the application necessarily crashes on import;
- every NumPy-2 behavior change matters;
- the local `vstack` shim makes NumPy 2 globally compatible;
- historical closure of the PR proves our technical conclusion.

The owned S010 question is candidate-discovery breadth and per-mechanism state separation under a real requirement-broadening proposal.

**Disposition:** admit S010.

## 8. Cross-candidate result

Screening 06 gives four useful shapes:

```text
Fasal
multiple mechanisms discovered
→ both pruned on normal target path

Cactus
multiple mechanisms discovered
→ one strong / one refuted / one unresolved

Chia
release contains many mechanisms
→ only one target-relevant mechanism established

podcast-script
multiple mechanisms discovered
→ two independently grounded on same runtime path
→ target handles them differently
```

This is stronger evidence for candidate-discovery coverage than simply accumulating more mechanism categories.

## 9. S010 admission question

S010 should own:

> **Can a discovery/evaluation process preserve multiple independently grounded mechanisms from one real NumPy requirement-broadening proposal, keep their target handling states separate, and avoid treating discovery of the first valid concern as transition-level completeness?**

It should not own:

- all NumPy-2 migration behavior;
- all inaSpeechSegmenter compatibility;
- Apple-Silicon compatibility of future inaSpeechSegmenter releases;
- a maintainer merge/block recommendation;
- a universal candidate-discovery algorithm;
- a numerical completeness score.

## 10. Stop

Screening Pass 06 is complete.

Next action: admit S010 with a small purpose-built evidence bundle around exact identity, dependency/runtime path, mechanism A, mechanism B, candidate-state separation, coverage limits, and stopping.