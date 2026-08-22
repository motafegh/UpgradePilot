# AUDIT-006 — Internal Evidence Type Strength and Revalidation Boundaries

**Date:** 2026-08-21  
**Inspected revision:** `f87119ce3311224bc8fdedfc132d71a075773d7f`  
**Trigger:** Plan-02 learning exposed repeated exact-file/provenance validation in downstream dependency membership code and raised the broader question of whether UpgradePilot is protecting genuine trust/join boundaries or repeatedly defending against invalid internal states that stronger contracts could prevent.  
**Disposition:** keep current checks until a dedicated refactor strengthens the owning contracts; later reassess project-wide and remove only redundant internal-invariant revalidation while preserving external-boundary, semantic, and relational/rebinding checks.  
**Authority:** non-controlling audit evidence. This audit does not authorize immediate source changes, remove existing validation, select a concrete replacement type design, or change live continuation.

## 1. Question and scope

The audit asks:

> Across current and future UpgradePilot source code, are repeated checks protecting genuinely independent evidence boundaries, or are some checks repeated because internal types do not encode guarantees that were already established upstream?

The question arose while studying:

```text
src/upgradepilot/dependency/uv_membership.py
```

especially:

```python
evaluate_uv_selected_environment_membership(...)
_validate_exact_source_identity(...)
```

The issue is broader than uv membership. Representative exact-file/provenance consumers also exist in:

```text
src/upgradepilot/dependency/uv_lock.py
src/upgradepilot/dependency/pyproject.py
src/upgradepilot/upstream/interval_evidence.py
src/upgradepilot/upstream/interval.py
src/upgradepilot/target/artifact_environment.py
```

and direct evidence-object construction is common in tests and some verification tooling.

This audit therefore concerns a cross-cutting design principle for **current and future source code**, not a request to simplify one function.

## 2. Existing real runtime trust path

The supported application path already has strong external acquisition boundaries.

### 2.1 Pull-request identity

`src/upgradepilot/github/pull_request.py` owns real PR acquisition:

```text
user repository + PR number
→ locator syntax validation
→ GitHub API /repos/{repository}/pulls/{number}
→ response validation
→ PullRequestIdentity
```

The real response establishes repository/PR identity plus immutable base/head SHA boundaries. A nonexistent repository/PR does not naturally become a successful `PullRequestIdentity` through this provider path.

### 2.2 Exact repository-file acquisition

`src/upgradepilot/github/repository.py` then acquires exact files using the trusted repository/revision context:

```text
PullRequestIdentity.repository
+ PullRequestIdentity.head_sha/base_sha
+ repository-relative path
→ GitHub contents API at exact ref
→ response/path/blob/size/encoding checks
→ UTF-8 RepositoryTextFile
```

The provider already validates material structural facts including:

- repository-relative path admission;
- requested path versus returned path;
- regular-file response type;
- non-empty Git blob SHA;
- bounded reported size;
- base64 structure;
- decoded byte count versus reported byte count;
- bounded decoded size;
- UTF-8 decoding.

Therefore, on the normal provider-produced runtime path, many low-level file-integrity facts have already been established before dependency/upstream/target consumers see the file.

## 3. Central design observation

The key problem is not that GitHub acquisition is weak. The key problem is that **the Python type does not fully encode the strength of the acquisition contract**.

Current `src/upgradepilot/github/repository.py` exposes:

```python
@dataclass(frozen=True, slots=True)
class RepositoryTextFile:
    path: str
    revision: str
    blob_sha: str
    content: str
    repository: str | None = None
    returned_path: str | None = None
    reported_byte_count: int | None = None
    decoded_byte_count: int | None = None
    retrieved_at: datetime | None = None
```

and currently retains:

```python
ExactRepositoryTextFile = RepositoryTextFile

type ExactRepositoryFileEvidence = (
    RepositoryTextFile | UnavailableRepositoryFile
)
```

The class documentation explicitly admits older/manually constructed fixtures and tells downstream strict boundaries to revalidate strong fields.

Consequently the same nominal `RepositoryTextFile` type can mean either:

```text
A. real provider-produced evidence whose strong invariants were checked
```

or:

```text
B. a directly constructed Python record whose fields merely claim those facts
```

This is a **type-strength / provenance-expression issue**, not primarily a GitHub security failure.

## 4. Why direct construction matters — and why tests are not the root cause

Tests commonly construct evidence directly for focused unit scenarios, for example:

```python
RepositoryTextFile(
    repository="example/project",
    path="uv.lock",
    returned_path="uv.lock",
    revision="a" * 40,
    blob_sha="c" * 40,
    reported_byte_count=size,
    decoded_byte_count=size,
    content=content,
)
```

Some tests deliberately manufacture combinations that cannot arise from one real immutable GitHub repository/revision/path, such as a dependency context bound to lock blob A and a replacement lock object claiming the same repo/revision/path but blob B.

The causal chain is:

```text
permissive/manually constructible internal evidence type
→ impossible or untrusted states are representable
→ strict downstream consumers cannot rely on the type alone
→ defensive revalidation is required
→ tests correctly exercise those representable states
```

It is **not**:

```text
tests need fake objects
→ therefore production code should contain duplicate validation
```

Tests reveal the contract weakness; they do not create it.

## 5. Important correction: same repo + commit + path cannot naturally produce two blobs

For real Git/GitHub evidence:

```text
repository R
+ immutable commit C
+ path P
→ one tree entry
→ one blob identity/content
```

Therefore the illustrative state:

```text
same real repository
same exact commit
same exact path
but graph/content blob A in one place and blob B in another
```

cannot naturally arise from correct GitHub acquisition.

It can arise only when:

- an internal object was manually fabricated or incorrectly reconstructed;
- evidence from different acquisitions/investigations was accidentally mixed while fields were copied/overridden;
- a bug violates the intended construction path;
- a legacy/manual fixture lacks the strong provider guarantees.

This makes blob/byte/path revalidation downstream useful today as **program-level impossible-state defense**, but it also strengthens the argument that the long-term contract should make those invalid states harder to represent rather than requiring every consumer to defend against them independently.

## 6. Validation taxonomy

Future review/refactoring should classify checks before changing them.

### Class A — External trust-boundary validation — KEEP STRONGLY

Examples:

```text
GitHub/HTTP JSON shape
repository/PR locator syntax
returned path identity
file/blob/size/encoding validation
UTF-8 decoding
model structured output
YAML/TOML parsing
```

These validate untrusted external input as it enters UpgradePilot.

They belong at provider/parser boundaries and should not be weakened merely to reduce line count.

### Class B — Semantic/domain validation — KEEP STRONGLY

Examples:

```text
uv.lock schema version is admitted
pyproject contains required project structure
selected dependency group/extra exists
workflow declaration has one supported semantic form
package records can be interpreted conservatively
```

These are not duplicates of provider validation. They establish domain meaning from structurally valid data.

### Class C — Relational / rebinding validation — KEEP STRONGLY

Examples:

```text
lock evidence belongs to the same dependency-change context
project and lock belong to the same repository/revision/project root
workflow selector is bound to the project being evaluated
CI static evidence matches the exact workflow/job/step/segment being composed
upstream source belongs to the exact release/tag/repository proposition
```

Two objects can each be internally valid and still be the wrong pair. These checks are essential evidence-composition logic.

### Class D — Repeated internal-invariant validation — REASSESS

Examples that are already guaranteed by the normal exact-file provider but may be rechecked downstream:

```text
blob SHA is non-empty
reported byte count is a non-negative integer
reported byte count equals decoded byte count
returned path equals requested path
basic exact-file provenance fields are populated
```

These checks are currently defensible because `RepositoryTextFile` permits weaker/manual construction. They are the primary candidates for elimination **only after** a stronger internal contract exists.

### Class E — Impossible-state defense — REASSESS STRUCTURALLY

Examples:

```text
same purported exact repo/revision/path with inconsistent blob identity
manually created "trusted" object with internally plausible but externally unauthenticated fields
partially populated exact-evidence records entering strict consumers
```

The preferred question is not only “should we keep an if-statement?” but:

> Should this state be representable by the trusted internal type at all?

## 7. Findings

### AUDIT-006-F1 — Current provider validation is appropriately strong — GREEN

The normal GitHub acquisition path validates real PR identity and exact repository-file evidence at immutable revisions. The project should not remove these controls.

The concern is downstream representation, not insufficient external validation.

### AUDIT-006-F2 — `RepositoryTextFile` conflates record shape with strong exact evidence — YELLOW

The current type carries fields used as strong provenance but also admits legacy/manual construction and optional strong fields. The alias `ExactRepositoryTextFile = RepositoryTextFile` does not add a stronger invariant.

Consequences:

- exact-evidence strength is partly procedural rather than type-expressed;
- downstream consumers must remember which fields to revalidate;
- tests can create states that normal production acquisition cannot;
- the name `ExactRepositoryFileEvidence` can appear stronger than what the type alone proves.

This is manageable today but becomes increasingly costly as more consumers join exact evidence.

### AUDIT-006-F3 — Repeated defensive validation is a compensation mechanism, not automatically bad code — YELLOW

Current downstream revalidation should not be deleted in isolation. It compensates for F2.

Removing checks first would weaken correctness because downstream functions would then trust invariants the type does not actually enforce.

However, allowing this pattern to scale indefinitely would create a maintainability burden:

```text
provider validates
→ extractor revalidates
→ membership revalidates
→ target/upstream consumer revalidates
→ CI/application may revalidate again
```

The danger is not just code volume. Multiple independently maintained copies of “what counts as strong exact evidence” can drift.

### AUDIT-006-F4 — Relational/rebinding validation must not be mistaken for duplication — GREEN

Checks such as:

```text
lock identity == dependency-source identity
project revision == dependency-context revision
declaration project root == exact pyproject root
static CI evidence == exact workflow/job/step/segment
```

must remain even after stronger evidence types are introduced.

They establish relations between independently valid objects and therefore protect stronger propositions.

### AUDIT-006-F5 — Test convenience must not define production trust contracts — YELLOW

Direct construction is valuable for focused tests, but production types should not remain weak merely because fixtures are easy to create that way.

If stronger trusted types are introduced later, tests should adapt through:

- validated test builders/factories for normal trusted evidence;
- provider-boundary tests for malformed/untrusted input;
- explicit low-level unsafe/raw fixture helpers only where testing an impossible-state guard is the actual responsibility.

Membership/CI/domain tests should primarily test their own semantics rather than repeatedly testing provider integrity through manually malformed trusted objects.

### AUDIT-006-F6 — The concern likely extends beyond `RepositoryTextFile` — YELLOW / PROJECT-WIDE REASSESSMENT

`PullRequestIdentity` is also a directly constructible dataclass even though the normal provider establishes it through real GitHub acquisition. Other provider/domain evidence records may have similar “fields imply trust, constructor does not enforce trust” properties.

This audit does **not** conclude that every dataclass requires a private constructor or a new validation layer. It establishes a future project-wide review question:

> For each high-authority internal object, are its guarantees structural/type-level, provider-path assumptions, or merely field conventions?

Only materially consequential cases should be strengthened.

## 8. Preferred future design direction

The preferred direction is:

```text
RAW / EXTERNAL / UNTRUSTED
        ↓
validate at owning provider/parser boundary
        ↓
STRONG TRUSTED STRUCTURAL EVIDENCE
        ↓
interpret at owning domain boundary
        ↓
DOMAIN EVIDENCE
        ↓
validate relations when composing objects
        ↓
STRONGER PROPOSITIONS
```

The key rule is:

> **Validate what this boundary uniquely owns; do not continuously revalidate guarantees already encoded by a stronger upstream contract.**

### Candidate stronger exact-file shape

A future design may distinguish a generic/manual/raw file record from a strong exact file, conceptually:

```python
@dataclass(frozen=True, slots=True)
class ExactRepositoryTextFile:
    repository: str
    path: str
    revision: str
    blob_sha: str
    byte_count: int
    content: str
    retrieved_at: datetime
```

Important properties would be:

- strong fields are not optional;
- creation normally occurs only through a validating provider/factory boundary;
- downstream code may rely on invariants explicitly guaranteed by that type/constructor contract;
- unavailability remains a distinct typed result.

This exact class/interface is **not selected by this audit**. It is a design direction to compare during the future refactor.

### Candidate exact identity value object

A small reusable identity object may further reduce repeated field-by-field rebinding:

```python
@dataclass(frozen=True, slots=True)
class ExactFileIdentity:
    repository: str
    revision: str
    path: str
    blob_sha: str
    byte_count: int
```

Then evidence records could preserve the identity directly and relational checks could compare:

```python
lock_file.identity == source_evidence.head_identity
```

instead of independently comparing several fields.

Again, this is a candidate, not an accepted architecture decision. It is justified only if it measurably reduces duplication/drift without creating a generic evidence-framework abstraction.

## 9. What not to build

Do not respond to this audit by introducing an abstract trust-type framework such as:

```text
Validated[T]
Trusted[T]
Verified[T]
Evidence[T, State]
ProvenanceGraph[T]
```

merely for theoretical purity.

UpgradePilot should prefer precise domain/evidence types whose names correspond to actual responsibilities, for example:

```text
ExactRepositoryTextFile
ExactFileIdentity
DependencyVersionChange
UvLockDependencyContext
WorkflowDefinition
```

The cure for defensive duplication must not become a larger generic abstraction burden.

## 10. Recommended future refactor sequence

When this audit is explicitly selected for implementation/reassessment, use this order:

1. **Inventory repeated invariant checks project-wide.**
   - classify each as external, semantic, relational, repeated invariant, or impossible-state defense;
   - do not search-and-delete duplicate conditions mechanically.

2. **Identify the real owner of each invariant.**
   - GitHub response integrity → GitHub provider;
   - exact repository-file identity → exact-file evidence contract;
   - TOML/YAML meaning → owning parser/domain;
   - cross-object consistency → composing domain.

3. **Choose the smallest stronger contract.**
   - compare a dedicated strong exact-file type, validated constructor/factory, or compact identity value object;
   - avoid a generic validation framework.

4. **Migrate one central path first.**
   - dependency exact-file extraction/membership is a good pressure candidate because it already demonstrates repeated checks and strong rebinding needs;
   - preserve existing evidence semantics and problem states.

5. **Move tests to the correct responsibility boundary.**
   - malformed GitHub/file invariants at provider/constructor tests;
   - valid trusted builders for domain tests;
   - explicitly malformed domain relations only where the domain must detect a genuine relational mismatch.

6. **Remove only checks made redundant by the stronger contract.**
   - retain semantic and relational/rebinding validation.

7. **Pressure a second materially different consumer.**
   - e.g. upstream interval evidence or target artifact/environment evidence;
   - prove the stronger primitive is genuinely shared rather than dependency-specific.

8. **Validate focused + nearest integration + full deterministic suite.**

9. **If the new contract is consequential and cross-cutting, record the durable architecture in an ADR.**
   - do not create an ADR merely for renaming a dataclass or consolidating one helper.

## 11. Future source-code rule

For new code written before this audit is formally implemented, use this review discipline:

```text
Before adding a repeated validation, ask:

1. Is this untrusted input entering a trust boundary?
2. Is this domain syntax/meaning being interpreted here?
3. Am I joining two independently valid evidence objects?
4. Or am I rechecking an invariant that an upstream trusted contract should already guarantee?
```

If the answer is (4), do not automatically omit the check while current types remain permissive. Instead:

- keep the safety needed by the current contract;
- avoid spreading another variant of the invariant unnecessarily;
- prefer a shared narrow helper where appropriate;
- record pressure toward the future strong-type refactor if the repetition grows materially.

This preserves correctness now without normalizing indefinite duplication.

## 12. Relationship to existing audits and plans

### AUDIT-001

`audits/2026-08-01_AUDIT-001_exact-pr-file-acquisition-evidence-contract.md` examined the exact PR-file acquisition contract and helped establish the strong provider behavior that exists today.

AUDIT-006 does not reopen the need for exact acquisition. It examines the **downstream representation and repeated-consumer consequences** after that provider boundary became shared across more responsibilities.

### Current dependency/CI plan

`plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md` remains the owner of the current dependency/environment/CI capability sequence. This audit does not alter its semantics.

### Current learning route

The active Plan-02 learning route should continue. The repeated-validation/type-strength concern is an engineering finding discovered through learning; it is not a reason to derail mastery of the implemented membership behavior.

### Future agentic checkpoint

`plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md` will consume typed evidence if selected later. That future work makes strong internal evidence contracts potentially more valuable, but this audit must not pre-build a generic evidence framework for an agent.

## 13. Reassessment triggers

Reassess this audit before or during a substantial source refactor when one or more of these occurs:

- another domain starts copying the same exact-file integrity checks;
- exact-file provenance comparison grows across more consumers;
- tests increasingly require impossible “trusted” fixture states;
- an agent/controller or persistence/replay boundary requires serializing/deserializing trusted evidence;
- legacy/manual optional provenance fields are no longer needed;
- a bug appears because two consumers disagree about what constitutes valid exact evidence;
- field-by-field rebinding becomes difficult to review or maintain;
- source-clarity work shows validation noise materially obscuring business/evidence logic.

## 14. Proof required before accepting a refactor

A future change should not be accepted merely because it removes lines.

Required proof should include:

- normal real GitHub acquisition still establishes all current strong invariants;
- unavailable/inaccessible evidence remains explicit;
- malformed external evidence still fails/degrades safely;
- direct manual fabrication cannot silently acquire trusted/exact status through the normal public contract;
- dependency/upstream/target consumers retain the same or stronger domain semantics;
- relational/rebinding mismatches still fail/degrade explicitly;
- tests are redistributed to appropriate responsibility boundaries rather than simply deleted;
- representative real-case behavior remains unchanged unless separately intended;
- full deterministic regression validation passes.

## 15. Final disposition

Current state:

```text
EXTERNAL / PROVIDER VALIDATION        GREEN
EVIDENCE / PROOF DISCIPLINE           GREEN
RELATIONAL REBINDING VALIDATION       GREEN
INTERNAL TRUST-TYPE STRENGTH          YELLOW
REPEATED DEFENSIVE REVALIDATION       YELLOW
LONG-TERM MAINTAINABILITY IF EXPANDED YELLOW → risk increases with growth
```

The current redundant-looking checks are **not the preferred final architecture**, but they are presently part of the correctness envelope because strong acquisition guarantees are not fully carried by the internal type contract.

Therefore:

```text
DO NOT:
remove downstream checks first
or weaken exact evidence discipline

DO:
strengthen the owning trusted contracts first
→ migrate consumers/tests
→ preserve semantic + relational checks
→ remove only genuinely redundant internal revalidation
```

The long-term goal is not “fewer checks.” It is:

> **each important invariant is validated once by its real owner, carried explicitly by a strong internal contract, and revalidated only when a new semantic or relational proposition actually requires it.**
