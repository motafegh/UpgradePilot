# B2 Target Evidence Boundary — Adoption Decision

**Date:** 2026-08-13  
**Type:** Dated design-adoption / implementation-entry working memory  
**Live-state authority:** `../MEMORY.md` only

## Why this record exists

The earlier target-evidence checkpoint correctly stopped implementation while the evidence boundary was still undecided. Since then, the product-simulation branch was synchronized with current `main`, the expanded S001-S012 corpus and challenge cases were reviewed, and the branch handoff was merged into `main`.

The resulting gap is now an **adoption gap, not a research gap** for the first target-evidence increment.

The current corpus is sufficient to select a bounded first implementation without admitting another simulation case merely for breadth.

Primary simulation handoff:

- `product-simulation/TARGET_ENVIRONMENT_EVIDENCE_DESIGN_HANDOFF_2026-08-13.md`

## Adopted responsibility boundary

Keep the existing downstream contract:

```text
already-established exact target-supported wheel tags
→ TargetWheelCompatibilityEvidence
→ existing artifact-serviceability applicability evaluator
```

Add one bounded responsibility before it:

```text
exact repository + exact revision
→ one identified target environment / environment path
→ proposition-specific repository evidence
→ partial, provenance-carrying environment facts
→ enough exact compatibility evidence?
    ├── yes → exact TargetWheelCompatibilityEvidence
    └── no  → explicit insufficient / unresolved state
```

The first acquisition increment is allowed to succeed while exact wheel compatibility remains unresolved. It must not manufacture a complete tag set merely because some environment facts were acquired.

## Environment identity for the first slice

Do not create a universal repository environment identity model.

For the first bounded GitHub Actions slice, preserve scope using:

```text
repository
+ immutable revision
+ workflow source path
+ statically identified job scope
```

Runner, Python, and installation facts describe that scoped environment. They do not establish that the repository has one canonical environment.

## Facts and provenance

When literally and deterministically available, preserve:

- runner/platform declaration;
- Python-version declaration;
- evidence that the changed dependency source/environment is actually installed or formed in the scoped job;
- exact source path and job scope for each observation;
- explicit partiality or unresolved state when a required fact is absent or dynamic.

Reuse the existing `RepositoryTextFile` exact-file provenance. The interpretation layer must additionally preserve workflow/job scope and the source of each interpreted fact.

A partial observation such as Python version + Linux-family runner + changed-dependency installation must remain partial when architecture, ABI, or platform-tag detail is not established. It must not silently become an exact `packaging.tags.Tag` set.

## First real evidence family — adopted

The first supported family is **one statically readable GitHub Actions job**.

Bounded evidence shape:

```text
exact workflow file + job identity
+ literal runner/platform declaration, if present
+ literal setup-python version, if present
+ visible installation evidence showing whether the changed dependency environment is formed
→ partial target-environment evidence
```

Reuse the bounded deterministic parsing posture demonstrated by `src/upgradepilot/ci/workflow_commands.py`, but do not reuse its current final `installed + directly invoked` predicate unchanged. Artifact serviceability needs environment formation, not necessarily runtime invocation.

## Fixture-first implementation entry

Begin with a small set of focused deterministic workflow examples. The current test suite uses inline workflow strings rather than a dedicated fixture framework, so do not create generic fixture infrastructure unless actual reuse pressure earns it.

Required behaviors:

1. **Literal bounded positive formation** — one readable job, literal runner, literal setup-python, visible changed-dependency installation; preserve partial facts and provenance without inventing exact tags.
2. **S011-style non-formation guard** — platform/Python context exists but the affected dependency environment is not installed; do not claim formation, and scope any negative conclusion only to that job.
3. **Partial-but-insufficient evidence** — preserve known facts when a compatibility-critical fact is missing, dynamic, or unsupported; exact wheel compatibility remains unresolved.
4. **Unsupported/ambiguous shape** — richer, multiple, or dynamic shape outside the first parser boundary returns explicit unresolved/unsupported rather than guessed evidence.

## First implementation sequence

```text
focused behavioral fixtures/tests
→ minimal partial target-environment evidence contract
→ bounded static GitHub Actions interpretation
→ exact repository/revision/workflow/job provenance validation
→ explicit insufficient/unresolved behavior
→ only when exact tags are genuinely established, compose to TargetWheelCompatibilityEvidence
→ focused + nearest + full regression verification
→ transfer-test against existing simulation anchors
```

The exact source module and type names are not frozen here. Choose the smallest coherent boundary after inspecting neighboring CI and artifact-serviceability code.

## Required transfer/adversarial checks

Use existing evidence before admitting a new case:

- **S008** — composed static evidence must not overclaim a complete environment;
- **S011** — platform/CI presence must not imply the affected optional environment is formed;
- **Buildtest/C203** — missing exact environment detail must remain unresolved;
- **S006** — broad CI presence must not become discriminating evidence automatically;
- **S007** — stronger static evidence may prune deeper work;
- **S001** — authoritative bounded declarative evidence may close a necessary proposition when appropriate.

Only admit S013 if the concrete implementation exposes a behavior these anchors cannot discriminate.

## Explicit non-goals

Do not implement universal repository environment reconstruction, every workflow/matrix/reusable-workflow form, arbitrary Actions expressions, container/deployment unification, broad runner-label-to-tag conversion, repository-wide environment unioning, generic conflict resolution, historical producer-state reconstruction from S012, source-build success reasoning, or final maintainer recommendation.

## Adoption result

```text
PARTIAL PROVENANCE-CARRYING ENVIRONMENT FACTS → adopted
FIRST SOURCE FAMILY → one statically readable GitHub Actions job
BROAD LABEL → EXACT TAGS → forbidden
MISSING EXACT FACT → unresolved / insufficient
NEW SIMULATION CASE BEFORE IMPLEMENTATION → not justified
NEXT PRODUCT STEP → fixture-first bounded acquisition/interpretation implementation
```

This closes the previous design-selection question at the smallest defensible scope. Future expansion must be earned by concrete transfer failures or a new product responsibility.
