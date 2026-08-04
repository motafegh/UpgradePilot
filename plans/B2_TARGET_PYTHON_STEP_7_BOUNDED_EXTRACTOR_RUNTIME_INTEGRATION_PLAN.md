# B2 Target-Python Step 7 — Bounded Extractor Runtime Integration Plan

**Status:** Bounded implementation plan for parent target-Python Step 7  
**Parent:** [`B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)  
**Architecture:** [`../docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md`](../docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md)  
**Prerequisites:** Parent Steps 1–6 behavior/evidence gates complete  
**First end-to-end proof:** S001 — Soup Sieve `2.6 → 2.8.4`

## Purpose

Move the Step 6 bounded extractor from experiment-only evidence into normal runtime **without expanding what was actually proven**.

The required target flow is:

```text
DependencyVersionChange
→ trusted upstream repository
→ authoritative old-exclusive/proposed-inclusive interval
→ deterministic bounded semantic source window
→ adopted contract-v2 local extractor
→ CandidateUpstreamClaimResult
→ validate_support_drop_candidates(...)
→ grounded support-drop claim?
    ├── no  → target Python acquisition NOT activated
    └── yes → exact-head pyproject.toml
              → TargetPythonDeclaration
              → evaluate_target_python_relevance(...)
```

This step owns integration and conditional activation. It does not broaden semantic scope or make compatibility, safety, merge, defer, or recommendation decisions.

## Why Step 7 needs more than copying experiment code

Step 6 proved a bounded semantic contract using bounded release text.

The real Step 5 S001 authority record contains a tagged changelog of 17,370 bytes. Step 5's live proof also supplied this exact changelog path manually:

```text
docs/src/markdown/about/changelog.md
```

Those were valid proof boundaries for Steps 5 and 6 separately, but normal runtime cannot silently assume either:

```text
known S001 changelog path
```

or:

```text
whole changelog == evaluated bounded model input
```

Step 7 must earn the two missing deterministic bridges:

1. bounded changelog-path discovery at the exact proposed-tag commit;
2. bounded crossed-release source-window construction from the exact changelog.

Only then may the adopted extractor be activated in the CLI.

---

## Increment 7A — exact-commit changelog-path discovery

### Owning question

> Given one trusted upstream repository and the immutable commit resolved from the proposed dependency-version tag, can UpgradePilot find one unambiguous admitted Markdown changelog path without package-specific constants or arbitrary web search?

### Method

Use the GitHub Git object API at the already trusted commit:

```text
exact commit SHA
→ exact commit object
→ exact root tree SHA
→ bounded recursive tree listing
→ deterministic admitted changelog basename filter
→ exactly one path or explicit problem
```

The initial admitted Markdown basenames are intentionally narrow and source-oriented:

```text
changelog.md
changes.md
history.md
release-notes.md
```

Matching is case-insensitive on the basename only. Directory location is not hardcoded.

This rule is a bounded discovery heuristic, not evidence authority by itself. The selected file still must be reacquired at the same immutable commit and pass the existing exact-file/tagged-changelog composition checks.

### Required outcomes

```text
DiscoveredChangelogPath
or
ChangelogPathDiscoveryProblem
```

Problem states must distinguish at least:

```text
source_unavailable
malformed_response
identity_mismatch
recursive_tree_truncated
no_candidate_path
multiple_candidate_paths
acquisition_failed
```

### Safety rules

- no GitHub code-search API;
- no default-branch search;
- no arbitrary documentation crawling;
- no model-selected path;
- no repository/package-specific path constants;
- truncated recursive tree cannot be treated as complete discovery;
- multiple admitted candidates remain ambiguous rather than ranked heuristically.

---

## Increment 7B — crossed-release Markdown source windows

### Owning question

> Can the exact tagged changelog be reduced deterministically to the release sections corresponding to the trusted crossed-release interval without assigning support-drop meaning?

### Initial structural grammar

Support only Markdown ATX headings (`#` through `######`) whose trimmed heading text is exactly either:

```text
<raw crossed version>
```

or:

```text
v<raw crossed version>
```

A matched version heading starts a release section. The section ends before the next heading at the same or higher heading level, or at end of file.

The raw trusted crossed-release identity remains the domain version. The optional `v` is only an admitted heading presentation form.

### Required output

For each trusted crossed release, preserve:

```text
release_version
heading line
exact section text
original global line IDs
original character offsets
```

The model must receive original line IDs so a selected candidate can be mapped back to the exact authoritative changelog.

### Completeness rules

- every trusted crossed release must map to exactly one admitted section;
- duplicate sections for one crossed release are unresolved;
- a missing crossed-release section is unresolved;
- source order must not contradict trusted crossed-release order;
- no section is omitted merely because it appears semantically irrelevant;
- section extraction may inspect Markdown structure only, not Python support meaning.

### Prompt bound

Concatenate only the admitted crossed-release sections.

Use a conservative explicit character bound before inference. If the complete required window exceeds the bound, return unresolved rather than truncate silently. The initial bound must be encoded and tested as an operational limit, not described as an exact token guarantee.

No tokenizer dependency is added merely for this step.

---

## Increment 7C — product local semantic adapter

### Selected method

Implement ADR-0006 directly in product source:

```text
LM Studio localhost HTTP
+ existing requests dependency
+ gemma-4-e4b-it-ud
+ contract v2 strict JSON Schema
+ temperature 0
+ seed 0
+ no automatic retry
```

### Loopback/proxy behavior

The product client should own its local transport boundary instead of requiring an experiment runner.

For the accepted local provider, use a dedicated `requests.Session` that does not inherit environment proxy settings. Reject non-loopback provider URLs under this ADR rather than silently sending authoritative source text to an arbitrary remote host.

### Model responsibility

The model returns only:

```text
candidates[]
  python_line
  introduced_in_version
  source_line_id
unresolved_if_no_candidates
detail
```

### Deterministic adapter responsibility

Derive/recover:

```text
candidate result state
package / normalized package
old / proposed version
category = support_boundary_change
change_state = support_dropped
source kind
exact source quote
exact quote offsets
```

### Failure behavior

Provider unavailable, HTTP failure, malformed outer/inner JSON, unsupported structured result, unavailable model, or bounded-window failure must become an explicit unresolved extraction result. They must not crash into a false positive or activate target-Python comparison.

Do not add automatic retries during this increment.

---

## Increment 7D — support-drop evaluation service

Add one narrow runtime function/service that owns:

```text
AuthoritativeUpstreamIntervalEvidence
→ source-window construction
→ local semantic extraction
→ CandidateUpstreamClaimResult
→ validate_support_drop_candidates(...)
→ UpstreamSupportDropClaimResult
```

The Step 2 validator remains the only trust-admission owner.

The service may return an unresolved Step 2 problem when semantic extraction could not be established, but it may not synthesize a grounded claim from provider errors or missing source windows.

---

## Increment 7E — conditional CLI orchestration

### Current orchestration defect

The existing CLI acquires target `pyproject.toml` immediately after canonical dependency identity, before a grounded upstream support-drop claim exists.

This violates the parent target-relevance activation order.

### Required order

For a supported dependency change:

```text
1. preserve existing CI dependency-exercise path independently;
2. acquire exact package release/provenance and trusted upstream repository;
3. acquire complete PyPI release index;
4. select crossed releases;
5. resolve accepted proposed-version tag;
6. discover one changelog path at the exact tag commit;
7. acquire exact changelog file;
8. assemble AuthoritativeUpstreamIntervalEvidence;
9. run bounded semantic extraction + Step 2 validation;
10. only if one GroundedPythonSupportDropClaim exists:
      acquire exact-head pyproject.toml
      interpret target declaration
      evaluate target Python relevance;
11. otherwise print target Python as not activated because upstream claim is unresolved.
```

### Existing behavior to preserve

CI dependency exercise remains independent of whether the upstream semantic claim is grounded.

Package/upstream evidence presentation must remain available when target-Python activation stops.

Unsupported canonical dependency identity still prevents downstream dependency-specific work as today.

### New presentation

Output must make these boundaries visible, for example:

```text
Upstream interval authority: available | <problem>
Support-drop claim: grounded | <problem-state>
Dropped Python line: 3.8            # only when grounded
Target Python declaration: not activated
```

or, when grounded:

```text
Target Python declaration: available
Target requires-python: >=3.10
Target Python relevance: outside_declared_python_range
```

No `safe`, `compatible`, `merge`, or recommendation vocabulary is allowed.

---

## Increment 7F — controlled and live S001 end-to-end proof

### Controlled proof

A deterministic CLI/service integration test must establish the full activation ordering with captured/fake source responses:

```text
soupsieve 2.6 → 2.8.4
→ tagged changelog path discovered generically
→ crossed-release sections windowed
→ model adapter candidate represented through controlled structured output
→ Step 2 grounds Python 3.8 @ 2.8
→ target pyproject acquired only after grounding
→ >=3.10
→ outside_declared_python_range
```

Model inference itself remains mocked/controlled in ordinary deterministic tests.

### Live proof

After deterministic validation, run S001 against public sources and the accepted local LM Studio deployment.

Expected bounded result:

```text
Dependency: soupsieve 2.6 → 2.8.4
Upstream authority: tagged_changelog
Grounded drop: Python 3.8 @ 2.8
Target requires-python: >=3.10
Target relevance: outside_declared_python_range
```

The live proof must not claim compatibility, safety, or merge readiness.

---

## Proof obligations

Before Step 7 closes, controlled tests must prove at least:

1. exact commit identity is preserved through changelog-path discovery;
2. recursive tree truncation stops discovery;
3. zero changelog candidates remains explicit;
4. multiple admitted changelog candidates remain ambiguous;
5. S001-shaped nested path is found without package/repository constants;
6. exact changelog file is reacquired and validated at the same resolved commit;
7. Markdown version sections preserve exact original lines and offsets;
8. every trusted crossed release must be represented exactly once;
9. missing/duplicate/out-of-order sections stop rather than silently reduce coverage;
10. source-window size overflow stops rather than truncates;
11. source-window code does not classify support semantics;
12. local model client rejects non-loopback base URLs;
13. local model HTTP does not inherit external proxy configuration;
14. provider/HTTP/JSON/schema failures become unresolved extraction, not exceptions that imply success;
15. contract-v2 candidate presence derives `candidates_available` mechanically;
16. exact line recovery preserves whitespace and offsets;
17. every positive candidate still passes Step 2 before target activation;
18. a support-added/negated/future/no-claim result never activates target Python;
19. target Python file acquisition is not called before a grounded support-drop claim;
20. CI dependency exercise remains independent of semantic-claim resolution;
21. S001 controlled flow produces only `outside_declared_python_range`;
22. ordinary deterministic suite remains green;
23. live S001 reacquires public evidence and produces the expected bounded relevance result.

---

## Modification boundary

Expected product modules may include:

```text
src/upgradepilot/upstream_changelog.py
src/upgradepilot/support_drop_source_window.py
src/upgradepilot/support_drop_extractor.py
src/upgradepilot/cli.py
src/upgradepilot/__init__.py
```

Existing Step 1–5 domain and validation modules should be reused rather than duplicated.

Do not weaken:

```text
src/upgradepilot/upstream_claim.py
src/upgradepilot/upstream_interval.py
src/upgradepilot/target_python_relevance.py
```

to accommodate model/provider mistakes.

No Instructor/Pydantic/new semantic framework is required by this plan.

---

## Stop line

Stop Step 7 when the bounded extractor is active in the normal read-only product path with deterministic source discovery/windowing and conditional target-Python activation, and controlled + live S001 evidence passes.

Do not proceed in this step into:

- compatibility or upgrade safety;
- merge/defer/recommendation output;
- cloud model fallback;
- automatic retry/correction loops;
- arbitrary documentation/RAG;
- general release-note summarization;
- new semantic categories;
- target repository mutation.

Any failure to find one unambiguous changelog, build a complete bounded crossed-release window, reach the local provider, or admit a candidate through Step 2 must remain an explicit unresolved stopping result.
