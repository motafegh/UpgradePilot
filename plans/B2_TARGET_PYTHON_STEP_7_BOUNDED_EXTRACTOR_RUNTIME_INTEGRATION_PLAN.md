# B2 Target-Python Step 7 — Bounded Extractor Runtime Integration Plan

**Status:** Position-neutral bounded implementation plan  
**Parent:** [`B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)  
**Semantic architecture:** [`../docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md`](../docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md)  
**Source-layout architecture:** [`../docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](../docs/architecture/ADR-0007-responsibility-based-python-subpackages.md)  
**Prerequisites:** Parent Steps 1–6 behavior/evidence gates satisfied before this plan is selected

## Purpose

Integrate the accepted bounded semantic extractor into the normal read-only product path without expanding its proven scope.

Target flow:

```text
DependencyVersionChange
→ trusted upstream repository and crossed-release interval
→ exact authoritative changelog
→ deterministic crossed-release Markdown source window
→ ADR-0006 bounded candidate extraction
→ validate_support_drop_candidates(...)
→ grounded support-drop claim?
    ├── no  → target Python not activated / unresolved
    └── yes → exact-head pyproject.toml
              → TargetPythonDeclaration
              → target-Python relevance
```

This plan owns the missing runtime bridges and orchestration. It does not re-decide the accepted model/provider contract, source-layout architecture, version method, compatibility, safety, or recommendation policy.

## Accepted owners to reuse

Do not duplicate or weaken:

- ADR-0006 → model/provider/contract/trust boundary;
- ADR-0007 → product/experiment/tool placement and internal package ownership;
- `src/upgradepilot/upstream/claim.py` → deterministic claim admission;
- `src/upgradepilot/upstream/interval.py` and interval-evidence owner → crossed-release authority;
- `src/upgradepilot/target/python.py` and `target/python_specifier.py` → target declaration/version semantics;
- `src/upgradepilot/target/relevance.py` → bounded relevance mapping;
- GitHub exact-revision acquisition owners → immutable source identity.

Expected implementation ownership remains:

```text
7A changelog discovery     → src/upgradepilot/github/changelog.py
7B source windows          → src/upgradepilot/upstream/changelog.py
7C local semantic adapter  → src/upgradepilot/upstream/support_drop_extractor.py
7D upstream composition    → smallest clear upstream-domain function/module boundary
7E application sequencing  → src/upgradepilot/investigation.py
CLI rendering/exit policy  → src/upgradepilot/cli.py
```

Do not recreate deleted flat compatibility paths, generic `services/`/`adapters/` layers, or future modules before their increment introduces real implementation.

## Why integration requires deterministic bridges

The semantic experiment evaluated bounded release text. Normal runtime cannot silently assume either:

```text
known repository-specific changelog path
```

or:

```text
whole changelog == bounded evaluated model input
```

Step 7 therefore must establish two deterministic bridges before normal model invocation:

1. exact-commit bounded changelog-path discovery;
2. complete crossed-release Markdown source-window construction.

## Increment 7A — exact-commit changelog-path discovery

### Question

Given a trusted upstream repository and immutable proposed-tag commit, find one unambiguous admitted Markdown changelog without repository/package constants or arbitrary search.

### Method

```text
exact commit SHA
→ exact commit object/root tree
→ bounded recursive tree listing
→ deterministic basename filter
→ exactly one path or explicit problem
```

Initial case-insensitive admitted basenames:

```text
changelog.md
changes.md
history.md
release-notes.md
```

Directory location is not hardcoded. Discovery is not evidence authority by itself; the selected file must still be reacquired and validated at the same immutable commit.

Stop explicitly on source failure, malformed/identity-mismatched responses, truncated recursive tree, zero candidates, or several candidates. Do not rank multiple candidates heuristically, use code search/default-branch search, crawl arbitrary documentation, or let a model select the path.

## Increment 7B — crossed-release Markdown source windows

### Question

Reduce the exact tagged changelog deterministically to the complete release sections corresponding to the trusted crossed-release interval without assigning support-drop meaning.

### Initial structural grammar

Support Markdown ATX headings (`#` through `######`) whose trimmed heading text is exactly:

```text
<raw crossed version>
```

or:

```text
v<raw crossed version>
```

A matched version heading starts a section that ends before the next heading at the same or higher level, or end of file.

The trusted raw version remains the domain identity; optional `v` is only presentation syntax.

### Required output

For every trusted crossed release preserve:

- exact release version identity;
- heading line;
- exact section text;
- original global line identifiers;
- original character offsets.

### Completeness and bound rules

- every crossed release must map to exactly one admitted section;
- missing or duplicate release sections are unresolved;
- source ordering must not contradict trusted release ordering;
- no required section may be omitted because it appears semantically irrelevant;
- extraction may inspect Markdown structure only, not support semantics;
- concatenate only complete required sections;
- enforce an explicit conservative character bound before inference;
- if the complete window exceeds the bound, return unresolved rather than truncate silently.

Do not add a tokenizer dependency merely for this structural bound.

## Increment 7C — product local semantic adapter

Implement the accepted ADR-0006 method in product source. The ADR owns provider/model identity, contract v2, no-auto-retry baseline, strict structured generation, loopback/local trust boundary, and deterministic reconstruction/validation requirements.

This increment owns product adapter mechanics only:

- bounded source-window request assembly;
- local transport invocation;
- strict response parsing into the candidate domain boundary;
- exact line/source recovery;
- explicit unresolved result for provider/HTTP/JSON/schema/runtime failures.

Do not duplicate model authority, add fallback/cloud providers, add automatic retries, or introduce a framework merely to wrap this boundary.

## Increment 7D — support-drop runtime evaluation

Create the smallest clear upstream-domain composition that owns:

```text
AuthoritativeUpstreamIntervalEvidence
→ source-window construction
→ ADR-0006 candidate extraction
→ CandidateUpstreamClaimResult
→ validate_support_drop_candidates(...)
→ UpstreamSupportDropClaimResult
```

The deterministic validator remains the only trust-admission owner. Provider/window failures may produce unresolved state but may not synthesize grounded claims.

## Increment 7E — conditional application orchestration

Application sequencing belongs in `investigation.py`, not `cli.py`.

Required order:

```text
1. preserve existing CI dependency-exercise path independently;
2. establish trusted package/upstream repository identity;
3. establish crossed-release interval and authority;
4. resolve the accepted proposed-version tag/commit;
5. discover and reacquire exact changelog;
6. build complete deterministic source window;
7. run bounded semantic extraction + deterministic validation;
8. if grounded support-drop claim exists:
      acquire exact-head target pyproject.toml
      interpret target declaration
      evaluate relevance;
9. otherwise:
      return target Python as not activated/unresolved.
```

Package/upstream evidence must remain available even when semantic/target activation stops. Unsupported dependency identity still prevents dependency-specific downstream work.

`cli.py` renders typed application state and exit policy; it must not duplicate orchestration.

## Increment 7F — controlled and live end-to-end proof

### Controlled proof

Use captured/fake source responses and controlled semantic adapter output to prove the full activation order deterministically, including that target acquisition does not occur before a grounded claim.

Ordinary product tests must not require live model inference.

### Live proof

After deterministic validation, run the selected public proof against real public evidence and the accepted local LM Studio deployment using the normal CLI or a developer-operated tool when explicitly required.

The result may establish only the bounded support-drop/target-relevance outcome. It must not claim compatibility, safety, or merge readiness.

## Proof obligations

Before Step 7 can close, evidence must establish at least:

### Changelog discovery

- exact commit identity preserved;
- truncated tree stops discovery;
- zero/multiple candidates remain explicit;
- nested path discovered without package/repository constants;
- selected file reacquired at the same immutable commit.

### Source windows

- exact original lines/offsets preserved;
- every trusted crossed release represented exactly once;
- missing/duplicate/out-of-order sections stop;
- size overflow stops rather than truncates;
- windowing performs structural selection only, not semantic classification.

### Semantic adapter/trust

- ADR-0006 local/provider boundary preserved;
- provider/HTTP/JSON/schema failures become unresolved rather than success;
- candidate presence/state remains mechanically coherent under contract v2;
- exact source recovery is deterministic;
- every positive candidate passes claim validation before target activation;
- negative/negated/future/support-added/no-claim controls do not activate target Python.

### Application integration

- target file acquisition is not called before a grounded claim;
- CI dependency-exercise behavior remains independent;
- controlled selected-case flow yields only the bounded relevance result;
- active product regression remains green;
- experiment regression remains separately executable when affected;
- selected live proof reacquires public evidence and reproduces the bounded result.

## Modification boundary

Product code/tests for the increments above belong under `src/upgradepilot/` and `tests/` according to ADR-0007.

New method comparison/calibration remains under `experiments/` with `experiments/tests/`. Developer-operated live proofs/diagnostics remain under `tools/`.

Product runtime must not import `experiments/` or `tools/`.

No new semantic framework, cloud provider, retry architecture, or generic service layer is authorized by this plan.

## Stop line

Stop when the bounded extractor is connected to the normal read-only product path through deterministic source discovery/windowing and conditional target-Python activation, with required controlled and live evidence.

Do not continue in this plan into:

- compatibility/update safety;
- merge/defer/recommendation output;
- cloud fallback;
- retry/correction loops;
- arbitrary documentation/RAG;
- general release-note summarization;
- new semantic categories;
- target repository mutation.

Failure to obtain one unambiguous changelog, build a complete bounded window, reach the accepted local provider, or admit a candidate through deterministic validation remains an explicit unresolved stopping result.
