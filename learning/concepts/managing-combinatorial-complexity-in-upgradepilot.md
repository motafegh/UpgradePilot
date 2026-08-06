# Managing Combinatorial Complexity in UpgradePilot

**Purpose:** Reusable learning note for understanding how UpgradePilot can handle many packages, repositories, evidence states, impact types, and case-specific combinations without writing one rule per case.

This file is educational context. It does not define product behavior, runtime contracts, or accepted architecture by itself.

## 1. The core concern: combinatorial explosion

**Combinatorial explosion** means that when several variables can each take several values, the total number of possible combinations grows very quickly.

UpgradePilot appears vulnerable to this because real dependency-update cases can vary across:

- repositories;
- packages;
- old and proposed versions;
- dependency-file formats;
- CI workflows and jobs;
- upstream release-note wording;
- API/configuration usage;
- supported Python/platform environments;
- evidence availability and authority;
- repository policies;
- impact and uncertainty states.

The engineering answer is not to enumerate every possible combination. The goal is to discover stable concepts, normalize variable input into those concepts, and reason through general relationships.

## 2. High value count does not imply high behavior count

Thousands of package names do not require thousands of package-specific code paths.

For example:

```text
soupsieve 2.6 -> 2.8.4
pytest 9.0.2 -> 9.0.3
httpx 0.27.2 -> 0.28.1
```

can all be different **data values** represented through one stable concept such as:

```text
DependencyVersionChange
├── package
├── old_version
├── proposed_version
└── evidence describing where the change was established
```

A central principle is:

> A high number of concrete values does not necessarily imply a high number of distinct behaviors.

## 3. Three kinds of variation

### 3.1 Value variation

Examples:

- repository;
- package name;
- PR number;
- commit SHA;
- old/new version;
- API symbol;
- Python version.

These may have enormous or effectively unbounded value spaces, but usually remain **data**, not separate architectural branches.

### 3.2 State variation

Examples:

```text
available
unavailable
conflicting
malformed
unsupported
```

or later impact-related states such as:

```text
potential
applicable
not_applicable
unresolved
contradicted
```

The number of meaningful semantic states is usually much smaller than the number of concrete input values.

### 3.3 Structural variation

Different representations may genuinely require different mechanisms:

```text
requirements.txt
pyproject.toml
uv.lock
poetry.lock
```

The correct pattern is normally not package-specific parsing. It is representation-specific extraction that converges on a shared domain object.

```text
many external forms
        ↓
specialized extractors/adapters
        ↓
shared trusted representation
```

## 4. Abstraction

**Abstraction** means representing many concrete things through only the characteristics that matter for the current problem.

For one responsibility, `soupsieve`, `pytest`, and `httpx` may differ only in:

```text
package identity
old version
new version
```

The irrelevant differences disappear behind a domain abstraction such as `DependencyVersionChange`.

Good abstraction reduces accidental complexity without erasing distinctions that genuinely matter.

## 5. Normalize early

**Normalization** means converting different external representations that express the same underlying fact into one trusted internal form after validation.

Example:

```text
uv.lock
requirements.txt
pyproject.toml
        ↓
representation-specific parsing + validation
        ↓
trusted dependency-version change
        ↓
shared downstream reasoning
```

Without normalization, every later responsibility would need to understand every input format, producing multiplicative complexity.

## 6. Decomposition

**Decomposition** means splitting one large problem into smaller responsibilities with clear inputs and outputs.

A useful conceptual shape for UpgradePilot is:

```text
Dependency identity
↓
Upstream changes
↓
Impact candidates
↓
Activation conditions
↓
Target applicability
↓
Coverage / evidence
↓
Open questions
↓
Investigation selection
↓
Stopping / sufficiency
↓
Maintainer-facing result
```

Each component owns a smaller question instead of one giant function owning all combinations.

## 7. Predicates and domain rules

A **predicate** is a general question about domain state, often producing true/false or a richer bounded result.

Bad case-specific rule:

```text
if repository == pydantic
and package == soupsieve
and Python drop == 3.8:
    ignore
```

General domain rule:

```text
if upstream impact is Python-support removal
and the target's declared Python range excludes the affected Python line:
    applicability = outside_target_range
```

The second rule can transfer across repositories and packages.

The goal is to write **domain rules**, not fixture rules.

## 8. Activation conditions and pruning

An **activation condition** is the condition that must hold for a potential upstream change to matter to the target.

Examples:

```text
upstream: Python 3.8 support removed
activation condition: target supports/runs Python 3.8
```

```text
upstream: foo() removed
activation condition: target reaches/uses foo()
```

Activation conditions allow **pruning**.

**Pruning** means discarding branches that can no longer affect the answer.

Example:

```text
30 meaningful upstream changes
├── 10 Windows-only changes; target has no required Windows surface -> close
├── 6 Python <3.10 changes; target requires >=3.11 -> close
├── 5 API changes for symbols target does not use -> close
└── 9 plausibly applicable changes -> investigate further
```

The system therefore does not need to deeply investigate every possible branch.

## 9. State-space explosion and independent dimensions

**State-space explosion** is the rapid growth of possible combinations of internal states.

Suppose we have:

```text
5 CI states
× 6 impact states
× 5 evidence states
× 4 policy states
× several impact categories
```

We should not manually enumerate every global combination.

Instead, evaluate relatively independent dimensions separately:

```text
Identity evaluator -> identity state
Python applicability evaluator -> Python-impact state
CI evaluator -> CI state
Policy evaluator -> policy state
```

Then combine only the interactions that actually matter.

## 10. Composition rules

Some dimensions genuinely interact. These interactions should be expressed through general **composition rules**.

Example:

```text
support_removed(3.8)
+
target_supports(3.8)
→ applicable support impact
```

This is still general logic. It is not one rule for one repository.

## 11. Graph-like reasoning

A graph becomes conceptually useful when relationships are many-to-many:

```text
one upstream change -> several target usages
one target usage -> several tests
one test -> several CI jobs
one policy requirement -> several impact types
```

UpgradePilot may therefore benefit from a conceptual impact graph even if the implementation never uses a graph database.

The important idea is the relationship model, not the storage technology.

## 12. Decision tables

A **decision table** makes policy combinations explicit and inspectable.

Example:

| Applicability | Coverage | Contradiction | Result |
|---|---|---|---|
| not applicable | any | no | closed |
| applicable | sufficient | no | covered |
| applicable | insufficient | no | unresolved |
| applicable | any | yes | conflicted |

Tables can be clearer and more testable than deeply nested `if` statements.

## 13. Finite State Machines (FSMs)

**FSM = Finite State Machine.**

Practical meaning: a system has a bounded set of meaningful states and explicit allowed transitions.

A possible impact lifecycle could conceptually look like:

```text
detected
↓
candidate
↓
applicability evaluated
├── not_applicable
├── applicable
└── unresolved
```

Then:

```text
applicable
↓
coverage evaluated
├── adequately_covered
├── insufficient
└── conflicting
```

The external world can be huge while the internal lifecycle remains finite and understandable.

## 14. Unknown, unresolved, and unsupported are useful states

A robust system does not need to force every input into a confident answer.

Legitimate states include:

```text
unknown
unresolved
unsupported
insufficient evidence
```

These states reduce complexity because the system does not need endless heuristics for cases it cannot responsibly interpret.

Abstention is therefore not only a safety property. It is also a complexity-control mechanism.

## 15. Equivalence classes in testing

An **equivalence class** is a group of inputs expected to exercise the same behavior.

If package identity itself should not affect a version-comparison rule, then:

```text
pytest 1 -> 2
httpx 3 -> 4
soupsieve 5 -> 6
```

may belong to the same behavioral class for that responsibility.

Tests should emphasize dimensions that actually change behavior:

```text
one dependency vs several dependencies
supported representation vs unsupported representation
matching identity vs conflicting identity
impact applicable vs not applicable
CI sufficient vs unresolved
```

This avoids trying to test every real package.

## 16. Property-based testing

**Property-based testing** tests general invariants across many generated inputs rather than only a few manually chosen examples.

Example invariant:

> Changing only the package name should not alter a target-Python range-comparison result when all relevant semantic inputs remain equivalent.

This is a powerful way to test generality later.

## 17. Reducing uncertainty through the pipeline

The recent S001 path illustrates a useful systems pattern:

```text
arbitrary repository/package/versions/changelog text
↓
DependencyVersionChange
↓
AuthoritativeUpstreamIntervalEvidence
↓
BoundedChangelogWindow
↓
GroundedPythonSupportDropClaim
↓
TargetPythonDeclaration
↓
TargetPythonRelevance
```

Each stage narrows a larger messy possibility space into a smaller trusted structured state.

Informally, the pipeline is reducing uncertainty or "entropy" as evidence becomes more structured and trustworthy.

## 18. Avoid over-abstraction

Generality can become harmful when names lose real responsibility.

Avoid vague components such as:

```text
EvidenceProcessor
GenericManager
ContextHandler
```

Prefer domain-specific reusable responsibilities such as:

```text
extract_uv_lock_changes
acquire_exact_pypi_release
validate_support_drop_candidates
evaluate_target_python_relevance
```

The useful middle is:

```text
not package-specific
not fixture-specific
not meaningless generic machinery
but domain-specific reusable responsibility
```

## 19. A compact architecture mental model

The real world may contain effectively unlimited concrete variation:

```text
repositories
packages
versions
files
APIs
release-note sentences
CI workflows
platforms
```

But the system can reason through a much smaller semantic model:

```text
IDENTITY
Is this the exact proposal/dependency/version we think it is?

AUTHORITY
Can this evidence support this kind of claim?

CHANGE
What changed upstream?

IMPACT
What could that change affect?

APPLICABILITY
Does the activation condition exist in the target?

COVERAGE
What evidence exercises or checks it?

CONFLICT
Does other evidence oppose it?

UNCERTAINTY
What remains unknown?

POLICY
What does this repository require?

INVESTIGATION
What question would be useful next?

STOPPING
Can more investigation still materially change anything?
```

The number of concrete real-world values can be enormous while the number of stable reasoning dimensions remains manageable.

## 20. Central takeaway

The engineering problem is not:

```text
How do we write rules for every possible dependency-update case?
```

It is:

```text
Which differences matter?
Which differences are only data?
Which representations can be normalized?
Which decisions can be decomposed?
Which interactions require general composition rules?
Which branches can be pruned?
Which uncertainty should remain explicit?
```

A useful overall pattern is:

```text
Real-world variation
↓
representation-specific acquisition
↓
validation + normalization
↓
stable domain concepts
↓
independent evaluators
↓
general predicates / composition rules
↓
conditional activation + pruning
↓
finite semantic states
↓
investigation/decision synthesis
```

This is one of the central architecture lessons exposed by UpgradePilot: good engineering is largely the process of deciding which differences must remain visible and which differences should disappear behind a trustworthy abstraction.
