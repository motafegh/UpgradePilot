# Group 4B — Upstream Evidence Authority and Bounded Semantic Extraction

**Learning-artifact date:** 2026-09-02  
**Source/test evidence horizon:** `main@5c3036cddf88e1eec9bef02e91ae38fcbbe6f534`  
**Landing context:** Note A landed after unrelated `main@7cce5ebc65b3a6120aea9ab63aa452b99b42b64`; neither the R4-B proposal nor this learning work changes the source/test horizon taught here  
**Roadmap responsibility:** Group 4B from `../plans/UPGRADEPILOT_WHOLE_PROJECT_LEARNING_ARTIFACT_ROADMAP_PLAN.md`  
**Artifact role:** frozen reusable learning snapshot; not project-state, implementation, or execution authority  
**Target depth:** **must master** upstream authority / attribution / grounding / deterministic-vs-model boundaries; understand the current support-drop path operationally; keep provider/prompt mechanics at lookup depth

This note answers one question:

> **Once UpgradePilot knows the exact dependency release interval, how does it establish which upstream text is authoritative enough to inspect, let a model perform only the irreducible language task, and then deterministically decide whether the proposed semantic claim is actually grounded?**

The central pattern is:

```text
authority before semantics
+
bounded model proposal
+
deterministic admission after the model
```

The model is not asked to discover what repository to trust, what releases were crossed, what source text counts as authoritative, or whether its own answer should be accepted.

---

## 1. The whole upstream flow

Starting after Group 4A has established one exact dependency transition and crossed-release interval:

```text
DependencyVersionChange
        ↓
DependencyReleaseInterval = (old, proposed]
        ↓
exact proposed PyPI release evidence
        ↓
PyPI project URL candidates
+
PyPI publisher provenance
        ↓
trusted upstream GitHub repository | explicit problem
        ↓
exact crossed-release index
+
GitHub release bodies / exact tagged changelog / package metadata
        ↓
AuthoritativeUpstreamIntervalEvidence | explicit problem
        ↓
exact tagged changelog + trusted crossed releases
        ↓
deterministic bounded Markdown source window
with exact sections + stable line IDs
        ↓
local semantic model selects candidate meaning
        ↓
CandidateUpstreamClaimResult
        ↓
deterministic identity/category/release/source/quote validation
        ↓
GroundedPythonSupportDropClaim | explicit problem
        ↓
later target relevance / impact reasoning
```

Three boundaries must stay separate:

```text
source authority
!=
semantic interpretation
!=
target applicability
```

---

## 2. First establish the upstream repository — do not let the model choose it

File:

```text
src/upgradepilot/upstream/repository.py
```

Current resolver:

```python
UpstreamRepositoryResolver.resolve(release)
```

Its job is intentionally narrow:

> **Can PyPI metadata plus PyPI publisher provenance establish one trusted GitHub repository identity for this exact package release?**

It does not interpret changelog prose and does not require a GitHub Release object.

### Evidence input 1: PyPI project URL candidates

PyPI may publish labels such as:

```text
Source
Repository
Source Code
GitHub
Homepage
```

The resolver normalizes the labels using the PEP 753 consumer-side style used by the current implementation, then accepts only the bounded repository-association family.

For the current GitHub-supported boundary, the candidate URL must reduce to one canonical HTTPS `github.com/owner/repository` identity.

### Evidence input 2: PyPI publisher provenance

The resolver also inspects exact distribution-file provenance from PyPI.

The important comparison is:

```text
project metadata says repository R
+
publisher provenance says GitHub repository R
        ↓
trusted upstream repository identity
```

not:

```text
project homepage looks plausible
        ↓
trust it
```

---

## 3. Repository identity problems remain explicit

Current upstream-repository problem states include:

```text
source_unavailable
unsupported_source
identity_mismatch
ambiguous_source
malformed_response
acquisition_failed
```

Representative behavior:

```text
Homepage → GitHub repo A
publisher provenance → repo A
→ available

Homepage → GitHub repo A
publisher provenance unavailable
→ source_unavailable

project URL → repo A
publisher provenance → repo B
→ identity_mismatch

Source → repo A
Repository → repo B
→ ambiguous_source
```

The key rule is:

> **A convenient upstream candidate does not become authority while conflicting or missing identity evidence remains unresolved.**

This is the same evidence discipline used earlier for dependency-source reconciliation.

---

## 4. Upstream interval authority is not “whatever release note we found”

File:

```text
src/upgradepilot/upstream/interval.py
```

The current source-authority order is explicit:

```text
github_release_body
tagged_changelog
package_metadata
```

But these sources do not all have the same role.

Current role mapping:

```text
GitHub release body → release authority
exact tagged changelog → interval authority
package metadata → corroboration
```

Unsupported examples include:

```text
Dependabot-copied release-note text
arbitrary documentation
model-selected text
```

### Must-master distinction

```text
text is relevant-looking
!=
text has admitted upstream authority
```

The source must first be tied to the exact package/repository/release interval through deterministic evidence.

---

## 5. Why one proposed release body is often insufficient

Suppose the dependency changes:

```text
2.6 → 2.8.4
```

and the crossed releases are:

```text
2.7
2.8
2.8.4
```

Looking only at the `2.8.4` release body can miss a material change introduced in `2.7` or `2.8`.

Therefore current behavior rejects:

```text
proposed release body only
+
no complete interval coverage
```

as:

```text
interval_incomplete
```

A complete ordered release-body series can establish interval authority.

An exact tagged changelog tied to the trusted repository/revision/interval may also establish interval authority.

### Important consequence

```text
latest release note
!=
complete change interval
```

Upstream analysis is interval-based, not only endpoint-based.

---

## 6. Missing intermediate evidence cannot hide behind available evidence

Current tests explicitly cover:

```text
crossed releases: 2.7, 2.8, 2.8.4
available release bodies: 2.7, 2.8.4
missing: 2.8
```

Without another admitted interval-authority source, the result remains:

```text
interval_incomplete
```

This embodies a project-wide principle:

> **Available positive evidence does not erase a material completeness gap.**

If an exact tagged changelog independently covers the interval, the authority bundle can still be established while preserving the missing release-body problem for traceability.

---

## 7. Package metadata is corroboration, not prose authority

PyPI package metadata can support useful propositions such as release/package identity and metadata fields.

But current upstream semantics deliberately do not allow package metadata alone to establish interval prose authority.

Current behavior:

```text
package metadata only
→ no_interval_authority
```

And later claim grounding does not admit:

```text
source_kind = package_metadata
```

as the source of a natural-language Python support-drop claim.

### Why?

Different sources are authoritative for different propositions.

```text
metadata proposition
!=
release/change prose proposition
```

This is **proposition-relative authority**, not a universal source ranking.

---

## 8. Before model inference, deterministic code builds an exact source window

File:

```text
src/upgradepilot/upstream/changelog.py
```

Entry point:

```python
build_crossed_release_source_window(...)
```

Its responsibility is structural only.

It does **not**:

- interpret release prose;
- identify support drops;
- call an LLM;
- decide target relevance.

It receives:

```text
trusted crossed-release index
+
exact tagged changelog evidence
```

and attempts to produce:

```python
CrossedReleaseSourceWindow
```

---

## 9. The source window is identity-bearing, not a loose text chunk

The current window preserves:

```text
repository
interval
path
resolved_commit_sha
trusted_ordered_versions
complete release sections
source_ordered_versions
exact text
character_count
max_characters
```

Each source line gets stable structural identity:

```python
ChangelogSourceLine(
    line_id="L4",
    line_number=4,
    text="...",
    start_offset=...,
    end_offset=...,
)
```

Each release section records its release identity, heading, source lines, and exact offsets.

### Why this matters

The model is not handed an anonymous blob and later trusted to quote it correctly.

Instead:

```text
exact source
→ deterministic section boundaries
→ deterministic line IDs
→ bounded model selection
```

This dramatically narrows what the model is responsible for.

---

## 10. The structural selector refuses to invent or truncate authority

Current explicit source-window problems include:

```text
identity_mismatch
malformed_source
missing_release_section
duplicate_release_section
source_order_conflict
window_too_large
```

Representative rules:

- every trusted crossed release must map to one admitted Markdown heading;
- duplicate matching release sections are not guessed away;
- source release order must match trusted order or its exact reverse;
- overlapping section boundaries stop;
- fenced-code headings are not mistaken for release headings;
- if the complete admitted window exceeds the character bound, it is **not truncated** to make inference convenient.

That last rule is important:

```text
complete authority too large
→ unresolved / stop
```

not:

```text
silently cut source
→ pretend completeness survived
```

---

## 11. The model enters only after source authority and source shape are fixed

Current adapter:

```text
src/upgradepilot/upstream/support_drop_extractor.py
```

Accepted method owner:

```text
docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md
```

Current adopted model identifier at this frozen horizon:

```text
gemma-4-e4b-it-ud
```

served through local LM Studio loopback.

But the important lesson is not the model name.

The important contract is:

```text
CrossedReleaseSourceWindow
→ bounded semantic selection only
→ CandidateUpstreamClaimResult
```

The model does not receive authority to change the source boundary.

---

## 12. What the model is allowed to select

The current bounded support-drop task asks the model to identify an explicit **current dropped Python support line** from the already admitted source window.

The structured selection is essentially constrained to:

```text
python_line
introduced_in_version
source_line_id
```

Examples of semantic distinctions the prompt asks it to preserve include:

```text
current drop
!= future/planned drop
!= added support
!= continued support
!= negated drop
```

It must not infer a dropped Python line merely from a raised minimum when the line itself is not explicit.

### Constrained identity fields

The request schema constrains:

- `introduced_in_version` to trusted crossed releases;
- `source_line_id` to deterministic selectable line IDs;
- `python_line` to explicit Python `X.Y` tokens observed in the source where available.

If there is no explicit Python-line token in the bounded source, the candidate array is constrained to zero items.

This is not proof of semantic correctness. It is a reduction of the model's allowed output space.

---

## 13. The model does not write the authoritative quote

This is one of the strongest design improvements compared with a looser extraction architecture.

The model selects:

```text
source_line_id = L4
```

Then deterministic code recovers:

```text
exact source_line.text
exact source_line.start_offset
exact source_line.end_offset
```

and constructs the candidate quote/span from the trusted source record.

So:

```text
model chooses a bounded source identity
```

but:

```text
model does not author or normalize the source quote
```

### Must-master equation

```text
semantic proposal by model
+
deterministic source recovery
!=
model-created evidence
```

The source evidence existed before inference.

---

## 14. Provider failure becomes unresolved, not semantic truth

Current adapter behavior converts expected provider/contract problems into an unresolved candidate result.

Examples include:

- request timeout;
- unsuccessful HTTP status;
- malformed outer JSON;
- malformed inner structured output;
- unexpected contract fields;
- completion stopped by token limit;
- inconsistent source-window structure;
- source window above the adopted inference guard.

The adapter does not retry automatically in this bounded path.

Conceptually:

```text
model/provider failed
→ we do not know
```

not:

```text
model produced no claim
→ no relevant upstream risk exists
```

This directly preserves `AUTH-004` from the Core specification.

---

## 15. Candidate state is explicit

Current semantic adapter output has three states:

```text
candidates_available
no_relevant_claim
unresolved
```

These mean different things.

### `candidates_available`

The semantic method proposed one or more bounded candidates that still require deterministic validation.

### `no_relevant_claim`

Within the admitted bounded semantic task, the model reported no current explicit support-drop candidate.

This is **not** proof that the update has no risk or no other relevant upstream change.

### `unresolved`

The semantic method could not produce a bounded answer, including provider/contract ambiguity/failure.

The system preserves the uncertainty rather than guessing.

---

## 16. Candidate output is still untrusted after valid JSON

File:

```text
src/upgradepilot/upstream/claim.py
```

The deterministic admission boundary is:

```python
validate_support_drop_candidates(authority, candidate_result)
```

This boundary does not call a model.

It asks whether the untrusted semantic proposal is compatible with the exact authority bundle.

### It first checks echoed identity

Candidate-result package/normalized package/old/proposed values must match the trusted interval exactly.

A model/provider result cannot quietly redirect the analysis to another package or interval.

---

## 17. The current semantic category is deliberately narrow

For this slice, deterministic admission accepts only:

```text
category = support_boundary_change
change_state = support_dropped
python_line = canonical major.minor, e.g. 3.8
```

Unsupported category/direction becomes an explicit problem rather than being coerced.

Examples:

```text
compatibility_assurance
→ unsupported_claim_category

support_added
→ unsupported_change_state

python_line = 3.8.1
→ invalid_python_line
```

The semantic model's structured output format does not grant permission to expand the accepted product domain.

---

## 18. The introduced release must belong to the trusted interval

A candidate claiming:

```text
introduced_in_version = 2.9
```

cannot be grounded when the trusted crossed releases are:

```text
2.7, 2.8, 2.8.4
```

Current result:

```text
claim_outside_interval
```

This is another example of deterministic evidence constraining semantic interpretation.

The model may interpret language, but it cannot manufacture a release relationship outside the trusted interval.

---

## 19. Source identity must resolve exactly

Two current groundable prose source kinds are:

```text
github_release_body
tagged_changelog
```

### GitHub release-body candidate

The candidate must identify the exact same release as `introduced_in_version`, and the authority bundle must contain exactly one matching admitted release body.

### Tagged-changelog candidate

The candidate uses the one exact tagged-changelog authority record. It may not invent a separate release-body selector.

Package metadata is not admitted as prose claim grounding.

If source identity is not exact, current outcomes include:

```text
source_not_admitted
source_identity_unresolved
```

---

## 20. Exact quote grounding is deterministic

For a candidate to become grounded:

```text
quote_start >= 0
quote_end > quote_start
quote_end <= source length
source_text[quote_start:quote_end] == source_quote
```

The quote must also contain the claimed Python line as an exact major/minor token.

Failure becomes:

```text
source_quote_not_grounded
```

### What grounding means

A successful result means approximately:

> This admitted source text at this exact identity/span supports attributing this bounded support-drop interpretation to the source.

It does **not** mean:

> The statement is independently confirmed real-world truth.

That distinction is required by:

```text
AUTH-002
CLAIM-001
GROUND-001
```

from the Core specification.

---

## 21. Equivalent candidates may combine evidence; distinct claims do not collapse

If a release body and tagged changelog independently ground the same claim identity:

```text
Python 3.8 support dropped
introduced in 2.8
```

current logic can preserve both source records under one grounded claim.

Exact duplicate candidates are deduplicated so repetition does not masquerade as extra independent proof.

But if the candidate result establishes several distinct support-drop identities, current behavior stops with:

```text
multiple_support_drop_claims
```

rather than arbitrarily choosing one.

---

## 22. The runtime bridge keeps deterministic and semantic responsibilities visible

File:

```text
src/upgradepilot/upstream/support_drop.py
```

Current composition:

```text
AuthoritativeUpstreamIntervalEvidence
        ↓
build_crossed_release_source_window(...)
        ↓
SupportDropCandidateExtractor.extract(...)
        ↓
validate_support_drop_candidates(...)
        ↓
UpstreamSupportDropClaimResult
```

This gives a clean mental model:

```text
DETERMINISTIC
source/release authority
        ↓
DETERMINISTIC
bounded source window
        ↓
SEMANTIC MODEL
candidate selection
        ↓
DETERMINISTIC
candidate grounding/admission
```

Or more compactly:

> **The model proposes; deterministic boundaries admit.**

---

## 23. What the model does not own

At this frozen horizon, the support-drop model does **not** own:

```text
package identity
exact dependency transition
PEP 440 interval
crossed release ordering
upstream repository identity
source authority
changelog path/revision identity
release-section selection
source-line identity
exact source quote text/offsets
final candidate grounding
target Python declaration
target relevance
technical applicability
compatibility
safety
maintainer recommendation
```

This list is more important to master than the exact prompt wording.

A bounded LLM method is useful precisely because the surrounding deterministic ownership remains clear.

---

## 24. Why this does not contradict the earlier M2-S02 rejection

Group 3 taught that the historical M2-S02 local-model deployments were rejected for the then-owning normal extraction responsibility.

Later ADR-0006 does not silently reactivate that old architecture.

The later path differs materially:

```text
M2-S02 historical pressure
broader known-text extraction responsibility
+ observed semantic/decision-effect failures
→ tested methods rejected
```

Later:

```text
current deterministic upstream pipeline
already owns identity + interval + source authority + bounded exact source
        ↓
concrete residual language-understanding gap
        ↓
new bounded support-drop candidate-selection experiment
        ↓
method evaluated and independently admitted through ADR-0006
```

So:

```text
old model method rejected
!= all future LLM use prohibited
```

and:

```text
later LLM admitted
!= old method restored by inheritance
```

The project re-admitted a narrower method for a newly evidenced responsibility.

This is exactly the clean-slate/non-reuse discipline from Group 3 working as intended.

---

## 25. Real S001 mental walkthrough

Historical real-case substrate:

```text
pydantic/pydantic#13432
soupsieve 2.6 → 2.8.4
```

The frozen S001 code-flow note shows an earlier source snapshot where the package/upstream branch already followed the conceptual path:

```text
exact package release
→ trusted upstream repository
→ dependency release interval
→ tagged changelog
→ Python support-drop claim
→ later target relevance
```

For current Group 4 mastery, stop the walkthrough at the grounded upstream claim boundary:

```text
soupsieve exact dependency interval
        ↓
trusted upstream repository + crossed releases
        ↓
exact admitted changelog authority
        ↓
bounded crossed-release source window
        ↓
semantic support-drop candidate
        ↓
deterministic grounding
        ↓
GroundedPythonSupportDropClaim
```

Even a fully grounded upstream support-drop claim does **not** yet establish that Pydantic is affected.

The next question is target-specific:

> Does the target repository actually support/use the dropped Python line under the relevant evidence boundary?

That belongs to Groups 6 and 9, not this note.

---

## 26. Failure-state map

| Boundary | Representative state | Meaning |
|---|---|---|
| upstream repo resolution | `source_unavailable` | required publisher/source evidence unavailable |
| upstream repo resolution | `ambiguous_source` | more than one admitted repository candidate/identity |
| upstream repo resolution | `identity_mismatch` | project metadata and provenance disagree |
| interval authority | `interval_incomplete` | crossed releases are not fully covered by admitted authority |
| interval authority | `no_interval_authority` | available material does not establish an admitted interval source |
| interval authority | `conflicting_source_identity` | nominally same release has conflicting source identity |
| changelog window | `missing_release_section` | trusted crossed release has no matching source section |
| changelog window | `source_order_conflict` | source structure conflicts with trusted release order |
| changelog window | `window_too_large` | complete source cannot enter admitted inference bound without truncation |
| model adapter | `unresolved` | provider/contract/semantic selection could not yield a bounded candidate result |
| candidate validation | `identity_mismatch` | model result echoes a different trusted interval |
| candidate validation | `unsupported_claim_category` | candidate outside admitted semantic slice |
| candidate validation | `claim_outside_interval` | introduced release not in trusted crossed interval |
| candidate validation | `source_quote_not_grounded` | quote/span does not match exact source |
| candidate validation | `multiple_support_drop_claims` | several distinct claims cannot be collapsed into one |

These are evidence/semantic outcomes unless an actual unexpected implementation exception occurs.

---

## 27. Proof and non-proof boundaries

### Current source/tests support

- PyPI/project-provenance reconciliation for the admitted upstream-repository boundary;
- explicit source identity ambiguity/unavailability/conflict states;
- interval authority requiring complete release-series evidence or an admitted exact tagged changelog;
- package metadata as corroboration rather than prose authority;
- exact structural changelog windows over trusted crossed releases;
- line/offset identity preserved before inference;
- bounded local structured candidate selection;
- explicit model/provider unresolved behavior;
- deterministic post-model identity/category/release/source/quote grounding;
- duplicate/equivalent candidate evidence combination without silent claim collapse.

### This Group 4B path does not prove

```text
all upstream change categories can be extracted
all release-note formats are supported
all Python packages use GitHub
all changelogs fit the bounded Markdown method
local-model semantics are universally reliable
absence of support-drop candidate means no risk
grounded upstream claim is independently corroborated truth
grounded upstream claim applies to the target
update is compatible or safe
maintainer should merge
```

Those claims would exceed the current responsibility and evidence.

---

## 28. Current fact, evidenced rationale, engineering judgment

### Current fact

At the pinned horizon:

- upstream GitHub repository identity is deterministically reconciled from admitted PyPI metadata/provenance;
- interval source authority is established before semantic extraction;
- the default current support-drop runtime requires trusted crossed releases and an exact tagged changelog to construct the semantic source window;
- the source window owns complete deterministic Markdown selection and stable line identity;
- the local model selects bounded semantic candidates only;
- exact quote/source/release/category/identity admission occurs deterministically afterward;
- unresolved/no-relevant/candidate-available remain distinct states.

### Evidenced rationale

ADR-0006 records adoption of a bounded local semantic extractor only after deterministic methods had established the surrounding authority and a residual natural-language interpretation gap remained. The Core and Minimum Useful Generality specifications require model-derived meaning to stay attributed, source-traceable, deterministically validated, and unable to manufacture authority.

### Engineering judgment

The architecture deliberately spends deterministic code on propositions machines can establish exactly and spends model capability only on the irreducible language distinction. This reduces—but does not eliminate—semantic risk and makes failures easier to localize.

---

## 29. What to master vs what to look up

### Must master / own

Be able to explain:

1. why upstream repository/source authority must be established before model interpretation;
2. why the dependency interval, not only the proposed release, owns the upstream search horizon;
3. why package metadata is corroboration rather than natural-language release authority;
4. why deterministic code selects exact changelog sections/line IDs before inference;
5. the difference between candidate extraction and deterministic grounding;
6. why valid structured model output is still untrusted;
7. why grounding proves correspondence to source, not independent truth;
8. why `no_relevant_claim` and `unresolved` are different and neither means “safe”;
9. what the current model is and is not allowed to own;
10. why ADR-0006's later narrow LLM admission is compatible with Group 3's M2-S02 rejection.

### Understand operationally

- `UpstreamRepositoryResolver`;
- `AuthoritativeUpstreamIntervalEvidence`;
- `build_crossed_release_source_window(...)`;
- `CrossedReleaseSourceWindow` / source-line identity;
- `LocalSupportDropExtractor`;
- `CandidateUpstreamClaimResult`;
- `validate_support_drop_candidates(...)`;
- `GroundedPythonSupportDropClaim`;
- `evaluate_support_drop_runtime(...)`.

### Lookup-level

- exact model identifier/provider constants;
- full system prompt;
- JSON-schema construction code;
- exact HTTP/session helpers;
- every Markdown parser regex;
- full problem-state vocabularies;
- individual test fixture offsets and response mocks.

### Deliberately deferred

- target Python/environment evidence — Group 6;
- artifact serviceability — Group 7;
- CI authority/exercise — Group 8;
- impact/applicability/investigation and target relevance — Group 9;
- full public-PR composition — Group 10;
- later B2/X1 agentic method comparison — Group 12.

---

## 30. Fast relearning route

1. Read Sections **1–7** to recover authority-before-semantics.
2. Read Sections **8–13** for deterministic source-window → bounded model selection.
3. Read Sections **16–22** for deterministic admission/grounding.
4. Read Section **24** to reconnect the later LLM admission to Group 3.
5. Rehearse:

```text
upstream candidate ≠ trusted source
complete interval ≠ proposed release only
model candidate ≠ trusted claim
grounding ≠ corroboration
no model claim ≠ no risk
model proposes; deterministic boundaries admit
```

6. Use the historical S001 note only as the real-case anchor; use current source/tests for current mechanics.

---

## 31. Evidence anchors

Accepted method owner:

- [`ADR-0006 — Bounded Local Support-Drop Semantic Extractor`](../docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md)

Earlier interval/version method owners:

- [`ADR-0004 — Dependency Version Change Evidence`](../docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- [`ADR-0005 — Packaging Version and Python Line Method`](../docs/architecture/ADR-0005-packaging-version-and-python-line-method.md)

Stable constraints:

- [`UpgradePilot Core Invariants`](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md)
- [`Minimum Useful Generality Specification`](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md)

Current source at the pinned horizon:

- `src/upgradepilot/pypi/release.py`
- `src/upgradepilot/upstream/repository.py`
- `src/upgradepilot/upstream/interval.py`
- `src/upgradepilot/upstream/changelog.py`
- `src/upgradepilot/upstream/claim.py`
- `src/upgradepilot/upstream/support_drop.py`
- `src/upgradepilot/upstream/support_drop_extractor.py`

Current proof surface:

- `tests/test_upstream_source.py`
- `tests/test_upstream_interval.py`
- `tests/test_support_drop_extractor.py`
- `tests/test_upstream_claim.py`

Frozen historical learning reused by reference rather than silently modernized:

- [`Group 3 — Early Implementation, M2 Experiments, and the Clean-Slate B2 Reset`](2026-09-02-group3-early-implementation-experiments-b2-reset.md)
- [`M2-S02 Historical Experiment`](m2-s02/README.md)
- [`S001 Real-Case Code Flow`](2026-08-15-tranche1-real-case-code-flows/01_S001_NORMAL_APPLICATION_END_TO_END.md)

No bounded Audit was required for this note: current specifications, accepted ADRs, source, tests, and frozen history provide a coherent explanation of why the model boundary is narrow and how deterministic authority surrounds it.
