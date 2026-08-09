# Conversation-C Handoff — S007 Investigation Pruning

**Date:** 2026-08-09  
**Status:** Non-controlling simulation-to-design handoff  
**Source evidence:** `REAL_WORLD_CASE_SCREENING_03.md`, S007, and `CONVERSATION_C_INVESTIGATION_SELECTION_PRESSURE_TEST_01.md`  
**Target discussion:** Conversation C — investigation selection

## Purpose

Carry only the parts of S007 that materially sharpen the current Conversation-C model.

This handoff does **not** ask main to reopen Conversations A/B, adopt S007 artifact schemas, create a planner/runtime type, or change product behavior.

The reviewed Conversation-C exploration already correctly recognizes:

- proposition-specific discrimination;
- static versus dynamic evidence as proposition-relative;
- sequencing and conditional activation;
- pruning power;
- redundant-evidence avoidance;
- legitimate no-further-investigation outcomes;
- cost/risk/invasiveness only as part of a broader evidence-value judgment.

S007 largely **confirms** those directions.

## Real-world evidence — BiomedParse #96

Frozen proposal:

```text
microsoft/BiomedParse#96
base: ac054c43b0f6cb579e00fe7d28bfbf29716c62b3
head: b8e53d5232ebb3e8068fed4fe79450f720665603

-torch==2.6.0+cu124
+torch==2.8.0
 torchvision==0.21.0+cu124
 torchaudio==2.6.0+cu124
```

The target keeps the CUDA-12.4 extra index, explicitly documents that the requirements assume CUDA 12.4, and directly uses PyTorch/CUDA at runtime.

Official upstream evidence establishes:

```text
Torch 2.6 family
→ TorchVision 0.21
→ TorchAudio 2.6
→ CUDA 12.4 available

Torch 2.8 family
→ TorchVision 0.23
→ TorchAudio 2.8
→ CUDA 12.6 / 12.8 / 12.9 documented
```

More importantly, official TorchVision v0.21 release build source establishes:

```text
setup.py:
PYTORCH_VERSION supplied
→ exact torch==PYTORCH_VERSION dependency

release/2.6 Linux wheel workflow:
install Torch release dependency
→ export installed Torch release version as PYTORCH_VERSION
→ build TorchVision wheel
→ verify wheel contains pinned Requires-Dist: torch (==...)
```

Therefore the retained TorchVision 0.21 release contract requires a Torch 2.6-family version and cannot share a Torch version with BiomedParse's direct `torch==2.8.0` requirement.

The owned package-family formation proposition is therefore refuted through authoritative static evidence plus deterministic constraint reasoning.

No resolver or target runtime execution was required.

## Refinement 1 — candidate checks can lose value before execution

At S007 admission, these were reasonable candidate observations:

```text
I1 exact target-relevant wheel metadata
I2 isolated resolver dry-run
```

Further authoritative source evidence then resolved the proposition before either execution was needed.

Preserve explicitly enough:

> **Investigation selection is conditional on the current admitted evidence state. A check that was sufficiently useful when generated may become unnecessary before execution when newly admitted evidence resolves the targeted proposition or closes its path.**

Conceptually:

```text
check generated at T1
+
new evidence at T2
→ re-evaluate check value
→ execute only if it can still materially change the owned state
```

This protects against turning a generated investigation plan into an execution obligation.

## Refinement 2 — distinguish why there is no next check

Conversation C already supports `no additional supported investigation is justified` while preserving unresolved state.

Cross-case evidence suggests preserving the **reason** because at least three situations differ materially:

### A. Resolved before further check

S007:

```text
new evidence resolves/refutes proposition
→ further execution redundant
→ stop
```

### B. Still unresolved, but no worthwhile supported check remains

Buildtest/OpenSSL if authentic historical environment evidence cannot be recovered:

```text
proposition unresolved
+
available checks fail scope/authority/discrimination/proportionality
→ preserve unresolved
→ stop
```

### C. Necessary path closed; deeper branch pruned

S001/AWS Python-support candidate or a complete plugin-absence result:

```text
necessary proposition/path refuted
→ deeper semantic investigation cannot change that path's result
→ prune
```

These may eventually share one operational surface such as `no next check`, but the knowledge state and explanation are different.

No runtime enum is requested by this distinction.

## Supporting contrast — S006

S006 gives the opposite valid outcome:

```text
static evidence leaves exact behavior unresolved
+
bounded old/new differential execution directly activates implicated branch
+
possible outcomes materially change the behavior proposition
→ SELECT TARGETED CHECK
```

Together:

```text
S006 → execution has unique discriminating value
S007 → execution loses unique value after stronger static evidence arrives
```

This supports Conversation C's existing rejection of both cheapest-first and strongest-test dogma.

## Bounded handoff conclusion

No foundational redesign is requested.

The current Conversation-C model survives S007 well. The only recommended sharpening is:

```text
1. re-evaluate planned investigations whenever admitted evidence changes;
2. preserve the reason behind no-further-check outcomes because
   resolved, path-pruned, and unresolved-with-no-supported-check are not equivalent.
```

S007 is also real-world evidence that static package/build metadata can be sufficient to prune a resolver/runtime investigation when it deterministically closes an earlier necessary proposition.

No S007 product schema, PyTorch-specific rule, or automatic runtime architecture follows from this handoff.