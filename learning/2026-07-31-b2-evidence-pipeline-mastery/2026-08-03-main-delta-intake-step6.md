# 2026-08-03 — Main Delta Intake: Step 5 Closure and Step 6 Activation

**Learning package:** `2026-07-31-b2-evidence-pipeline-mastery`  
**Status:** dated implementation-intake snapshot; non-controlling  
**Previous synchronized main baseline:** `0971ab7ee7e20fedbfaa2de1bc069a19fc5f00c4`  
**Current inspected main:** `7db6a6b6f0f6c261d98c6df66d51e14eb99359cd`  
**Learning-branch sync PR:** #19  
**Learning-branch merge commit:** `3be4ff047493697218ba451f1b2797823c2ae750`

## 1. Why this intake exists

`main` advanced by nine commits after the prior learning sync. The delta materially changes the forward product-learning map but does not alter the CI/workflow-reader source currently being studied.

Observed main-side changed files since the prior synchronized baseline:

```text
MEMORY.md
experiments/step6_support_drop_semantic_corpus.json
plans/B2_STEP_6_SUPPORT_DROP_EXTRACTION_EVALUATION_PLAN.md
tests/test_step6_support_drop_semantic_corpus.py
working-memory/2026-08-03_B2-step-5-live-s001-validation.md
working-memory/2026-08-03_B2-step-6a-support-drop-corpus-implementation.md
working-memory/2026-08-03_B2-step-6a-support-drop-corpus-validation.md
```

Notably absent from this delta:

```text
src/upgradepilot/ci_dependency_exercise.py
src/upgradepilot/workflow_commands.py
```

Therefore the current source-learning path remains valid and should not restart.

---

## 2. Main progression now established

The nine commits move the live product state through:

```text
live S001 Step 5 proof observed
→ parent Step 5 closed
→ focused Step 6 extraction-evaluation plan created/aligned
→ Step 6A semantic corpus frozen
→ Step 6A oracle tests behavior-validated
→ Step 6B environment observation activated
```

Current `MEMORY.md` states:

```text
Steps 1–5 behavior-validated
Step 6A behavior-validated
current responsibility = Step 6B environment observation
```

This is product progress, not evidence of user learning mastery.

---

## 3. Step 5 is no longer future learning intake

Step 5 is now a concrete implemented and live-validated acquisition boundary.

Observed S001 authoritative interval facts include:

```text
package: soupsieve
interval: 2.6 → 2.8.4
crossed releases: 2.7, 2.8, 2.8.1, 2.8.2, 2.8.3, 2.8.4

tag: refs/tags/2.8.4
resolved commit: 28108ab805818c832d9568142a99844fd95a0d39
changelog path: docs/src/markdown/about/changelog.md
changelog blob: 6f221b7398681a580fa199044b3d3f1e11b55493

authority basis: tagged_changelog
GitHub Release bodies admitted: 0
```

Learning implication:

```text
Step 5A release-index acquisition
+ Step 5B exact tag → immutable commit
+ Step 5C exact changelog file/evidence
+ Step 5D authoritative interval composition
+ live S001 public-source proof
```

must become a concrete later learning unit rather than remaining under a generic “future implementation intake” placeholder.

---

## 4. Step 6 is now a concrete semantic-extraction/evaluation boundary

The new focused plan owns only:

```text
AuthoritativeUpstreamIntervalEvidence
→ untrusted candidate semantic extraction
→ CandidateUpstreamClaimResult
→ validate_support_drop_candidates(...)
→ GroundedPythonSupportDropClaim
   or explicit claim problem
```

Only the narrow semantic form is currently in scope:

```text
category = support_boundary_change
change_state = support_dropped
python_line = explicit X.Y
introduced_in_version = exact trusted crossed release
```

The selected evaluation direction is:

```text
bounded structured LLM candidate extraction
→ existing deterministic Step 2 grounding/validation
```

but no model or adapter has been adopted.

---

## 5. Step 6A concrete learning intake

New artifacts:

```text
experiments/step6_support_drop_semantic_corpus.json
tests/test_step6_support_drop_semantic_corpus.py
```

The 15-case frozen corpus includes:

```text
direct support drops
paraphrased drops
support-added/continued controls
negation
future tense
ambiguity
raised-minimum-only ungroundable wording
multiple distinct drops
unrelated fixes
instruction-shaped text
exact S001 excerpt
```

Key architecture distinction to learn later:

```text
semantic oracle
≠
model output
≠
deterministic grounding
```

The oracle establishes expected meaning for evaluation. It is not the extraction algorithm.

---

## 6. Step 6B current product responsibility

Current live implementation work is environment observation before any model adapter is added.

The planned evidence layers are:

```text
LM Studio/server identity
model inventory
GPU state
WSL2 → model-server reachability
Python/environment identity
```

This is not yet a learning-session detour. The current CI lesson should finish its bounded ownership boundary first unless a new main change directly invalidates it.

Later Step 6 learning should explicitly separate:

```text
transport
structured generation
semantic correctness
grounding
trust admission
product adoption
```

---

## 7. Delta classification

```text
Current CI/workflow-reader lesson impact:
UNRELATED TO CURRENT SOURCE MECHANICS

Forward B2 architecture/learning impact:
MATERIALLY RELEVANT
```

Reason:

- no studied CI-reader source changed;
- Step 5 moved from pending live proof to closed;
- Step 6 moved from future concept to active bounded product responsibility;
- learning-plan forward units therefore require revision;
- no reason exists to replay Unit 1 or restart the current command-reader trace.

---

## 8. Learning-plan changes required

The refreshed plan should:

1. retain the current CI-first learning strategy;
2. record the exact current source continuation at `_command_invokes_package(...)`;
3. mark demonstrated concepts with checkboxes without overclaiming mastery;
4. keep Unit 2/3 ownership gates open even where mechanics have been covered;
5. make Step 5 acquisition a concrete later learning unit;
6. make Step 6A corpus/oracle and Step 6B–6D model-evaluation layers concrete later learning units;
7. preserve product validation versus learning mastery as separate claims;
8. continue to use `MEMORY.md` only for live product continuation.

---

## 9. Exact learning continuation after this intake

Do not switch to Step 6 yet.

Continue from:

```python
_command_invokes_package(...)
```

Then complete the remaining bounded workflow-reader mechanics and ownership evidence before reverse-tracing to canonical dependency identity.

This preserves continuity while keeping the forward learning map synchronized with current implementation reality.