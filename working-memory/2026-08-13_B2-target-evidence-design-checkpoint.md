# B2 Target Evidence Design Checkpoint

**Date:** 2026-08-13  
**Type:** Dated continuation / evidence-design working memory  
**Live-state authority:** `../MEMORY.md` only

## Why this checkpoint exists

The existing Increment-2 working memory records the artifact-applicability implementation but predates several material decisions from the current learning/build session. The GitHub connector refused replacement writes to that existing record, so this dated checkpoint preserves the continuation state without rewriting history.

## Current implementation position

Artifact Serviceability Increment 1 is verified green.

Increment 2 currently implements only:

```text
artifact candidate
+ already-established target wheel compatibility evidence
→ compare old and proposed published wheel compatibility for that target
→ bounded applicability
```

Commit `a37edf3b8941d085427c276a68496da2b3282555` added the target compatibility evidence/problem contracts and artifact applicability evaluator.

This is **not yet target-environment acquisition**. UpgradePilot still cannot derive that evidence from a real repository automatically.

The evaluator compares complete old/proposed wheel-tag inventories against the target-supported tags. It does not decide from removed old tags alone because a different proposed tag may still serve the same target.

## Verification state

A retained developer verification area now exists:

```text
tools/verification/
```

- `449d25b7fd03e9b9ab52fcdf70913b8f77685e6a` defines its purpose in `tools/verification/README.md`.
- `eaa4abd029a1c100e00582d43219a6fa98418717` adds `tools/verification/2026-08-13_b2_artifact_serviceability_increment2_smoke.py`.

The responsibility split is:

```text
permanent product regression → tests/
retained developer verification procedure → tools/verification/
observed run result → working-memory/
```

The retained Increment-2 procedure has **not yet been run by the user** in this session, and permanent focused regression coverage for the new evaluator is not yet present. Increment 2 therefore remains unverified/incomplete.

## Evidence-design reasoning established in the session

The target facts we need must be derived from the technical claim, not from whichever repository file is easiest to read:

```text
owned claim
"Did this repository/revision lose a prebuilt-wheel path across OLD → NEW?"
↓
wheel compatibility semantics
↓
required target facts
facts sufficient to resolve old/new compatibility
↓
evidence question
which exact repository-owned evidence may justify those facts?
```

This is a claim → required facts → evidence process.

The earlier plan phrase `smallest admitted exact target environment evidence` is now clarified as:

```text
BROAD EVIDENCE / DESIGN HORIZON
+
SMALLEST SUFFICIENT, DEFENSIBLE IMPLEMENTATION INCREMENT
```

It must not mean selecting one convenient evidence source and ignoring realistic alternatives.

Before selecting the first acquisition/interpretation method, the design horizon should consider realistic repository-owned evidence families and the facts each may establish. Candidate families include CI/workflow environment declarations, container definitions, Python/project metadata, test/runtime configuration, deployment/runtime declarations, and other exact operational evidence. These are candidates for investigation, not yet accepted sources or implementation requirements.

The decision also needs pressure from:

- partial environment evidence;
- exact revision/provenance;
- multiple legitimate target environments;
- composition of multiple evidence items;
- conflicting evidence sources;
- sufficient versus insufficient evidence for exact wheel compatibility;
- broad CI/package exercise versus exercise of the exact artifact-selection branch.

No universal environment reconstruction architecture is accepted by this checkpoint.

## Immediate continuation

Before further implementation, inspect the existing real `product-simulation/` cases specifically for evidence relevant to this target-environment decision.

Review question:

> Which real-case evidence shapes help determine what target environment facts matter, which sources can legitimately establish them, how partial/multiple/conflicting environment evidence appears, and when static evidence is sufficient to stop deeper investigation?

Use the cases as transfer/adversarial evidence, not as a sequential implementation backlog or hardcoded fixtures.

After this case review, discuss and decide the first defensible target-evidence implementation slice.
