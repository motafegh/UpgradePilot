# UpgradePilot B2 Evidence-Pipeline Mastery — 2026-08-02 Main Delta Intake

**Purpose:** Dated learning-impact review of production changes synchronized into `agent/learning-current-implementation`.  
**Previous synchronized main boundary:** `52d56773342f5dfe31c41fb0e39e58cc745ef5bf`  
**Main revision reviewed:** `9d09a669fe8f7ba31fdd326baa119f6ec2e1559a`  
**Synchronization merge commit on learning branch:** `0864723d25026e52e0ba50faa8f44ba152b74ba9`  
**Synchronization PR:** #15 (`main` → `agent/learning-current-implementation`)  
**Learning-plan update commit:** `4b3e2d3113a86bc338a6fd3a447265cd45f6e2c2`

## Boundary

This file records why the learning plan changed after synchronization. It is not live project authority and does not replace root `MEMORY.md`.

The review asks only:

```text
What changed on main?
→ Does it alter an existing learning unit?
→ Does it create a new learning responsibility?
→ Can it be deferred without harming the current sequence?
```

It does not re-audit every production change or authorize new product work.

## Delta overview

Between the previous learning sync and the reviewed main revision, the material changes were:

```text
Step 3 packaging/version method
→ implementation record added
→ local validation completed
→ Step 3 closed

Step 2 support-drop quote grounding
→ one token-boundary regression test added
→ regex boundary corrected
→ validated complete suite includes the fix

repository review system
→ durable non-controlling audits/ area added
→ AUDIT-001 records a proportionality review of exact PR file acquisition evidence

Step 4 target-Python relevance
→ focused plan added
→ pure mapping module implemented
→ focused tests added
→ package exports added/corrected
→ implementation record added
→ live state advanced to Step 4 validation gate
```

Documentation/navigation changes also occurred in specification and ADR indexes. They do not create a separate learning unit.

## Classification 1 — Step 2 quote-token regression

**Learning classification:** locally relevant to existing Unit 10.

The change corrected the distinction between:

```text
"Python 3.8."
→ may contain the canonical Python line token 3.8

"Python 3.8.1"
→ must not let the prefix 3.8 masquerade as the line token 3.8
```

The implementation changed the right-hand regular-expression boundary from rejecting any following dot to rejecting a following digit or a dot followed by a digit.

Why this matters educationally:

- exact token grounding is not the same as substring search;
- punctuation can terminate a legitimate major/minor token;
- patch-version continuation must remain excluded;
- tiny regular-expression boundary changes can alter evidence semantics.

**Plan action:** add this regression to Unit 10 rather than create a new unit.

## Classification 2 — Step 3 packaging/version method

**Learning classification:** material new bounded responsibility.

Step 3 is no longer hypothetical. The synchronized source now contains a concrete pure method layer for:

```text
raw dependency versions
→ PEP 440 parsing / forward interval

already selected crossed releases
→ deterministic parsed ordering while preserving raw identity

Python line X.Y + requires-python
→ exact stable X.Y.Z witness / non-overlap
```

Important learning concepts introduced by the real implementation:

- `packaging.version.Version`;
- `packaging.specifiers.SpecifierSet`;
- raw identity versus parsed semantic value;
- equivalent versions versus forward versions;
- exact stable three-component witness meaning;
- boundary-derived candidates instead of arbitrary patch enumeration;
- valid-but-unsupported specifier semantics;
- runtime dependency bounds as part of an accepted method.

At the reviewed main snapshot, the complete locally observed suite recorded in `MEMORY.md` included Step 3 and passed 251 tests.

**Plan action:** concretize Unit 11A around the actual Step 3 source, tests, plan, and ADR.

## Classification 3 — Step 4 target-Python relevance mapping

**Learning classification:** material new bounded responsibility.

Step 4 introduces a pure downstream mapping:

```text
UpstreamSupportDropClaimResult
+ conditionally admitted TargetPythonEvidence
→ one TargetPythonRelevanceResult
```

States:

```text
declared_python_overlap
outside_declared_python_range
target_declaration_unresolved
upstream_claim_unresolved
comparison_unsupported
```

Important new concepts:

- conditional activation of target evidence;
- early return as an authority boundary rather than only an optimization;
- caller sequencing misuse versus ordinary product evidence states;
- preserving nested owning records instead of copying provenance fields;
- invalid/contradictory target evidence versus valid-but-unsupported method semantics;
- downstream mapping that consumes trusted boundaries without re-validating their internal evidence.

At the reviewed main snapshot, Step 4 source and controlled tests existed, but root `MEMORY.md` still required local focused and complete validation before Step 4 could close. No passing Step 4 result is invented by this learning record.

**Plan action:** concretize Unit 11B around the actual Step 4 plan/source/tests and retain the validation-status distinction.

## Classification 4 — `audits/` and AUDIT-001

**Learning classification:** supporting design-review material, not a prerequisite or independent core unit.

`audits/` is explicitly non-controlling. AUDIT-001 examines whether parts of the exact PR file acquisition record are proportionate and where validation metadata may be over-preserved.

The useful learning opportunity appears only after the underlying exact base/head acquisition path is understood.

Examples of audit questions worth revisiting then:

```text
returned_path
→ required equality validation, but does it need long-lived successful-state storage?

decoded_byte_count
→ needed for bounded acquisition, but derivable after successful UTF-8 content preservation?

GitHub-reported size
→ unique provider metadata, but weak downstream domain evidence?

blob SHA
→ currently not independent integrity proof, but plausible replay/cache/persistence identity?

repository identity
→ validated upstream yet absent from DependencyFileEvidence; is enclosing PR scope sufficient?
```

**Plan action:** attach AUDIT-001 to Unit 6 as a post-understanding design-review exercise. Do not treat its findings as authorized refactoring requirements.

## Classification 5 — navigation/governance documentation changes

**Learning classification:** no separate learning unit.

Changes to architecture/specification navigation improve authority clarity but do not materially alter the source-code mastery sequence.

They should be noticed when navigating the repository, not taught as a separate technical concept unless a later governance question makes them relevant.

## Resulting learning-plan decision

No restart is justified.

The correct sequence remains:

```text
finish current Unit 2 mechanics
→ Unit 3 decision order/aggregation
→ workflow command reader
→ reverse trace dependency identity and multi-format acquisition
→ integration
→ upstream authority and grounding
→ Step 3 packaging method
→ Step 4 relevance mapping
→ later implementation intake
→ ownership assessment
```

Changes made to `LEARNING_SESSION_PLAN.md`:

1. preserve the original learning baseline and add a dated 2026-08-02 intake snapshot;
2. extend the implementation map with concrete Step 3 and Step 4 boundaries;
3. attach AUDIT-001 to Unit 6;
4. add the Python `3.8.` versus `3.8.1` quote-token regression to Unit 10;
5. replace the hypothetical Unit 11 topics with concrete Unit 11A Step 3 and Unit 11B Step 4;
6. retain Unit 11C for genuinely future implementation;
7. preserve Unit 12 ownership assessment and branch-integration requirements;
8. update the learning-depth checkpoint without claiming mastery beyond recorded evidence.

## Exact learning continuation after this intake

Do not jump to Step 3 or Step 4 immediately merely because they are newer.

The current unfinished learning point remains Unit 2:

```text
tuple(...) materialization
→ generator expression
→ ordered immutable per-workflow results
→ next(..., None) as existential witness selection
→ complete one-path proven source trace
```

Then continue through the existing sequence.

This preserves learning continuity while guaranteeing that the newer implementation is now explicitly scheduled and will not be forgotten.
