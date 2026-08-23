# UpgradePilot Naming Clarity Engineering Standard

**Status:** Accepted project-wide engineering standard  
**Owner:** Ali Rajabi  
**Responsibility:** Keep names and technical terms in active UpgradePilot source, tests, commands, plans, specifications, ADRs, and user-facing output concrete enough that a competent maintainer can recover their purpose and boundary with minimal project-specific decoding

## 1. Boundary and core rule

This file is a cross-cutting engineering standard, not a system-behavior technical specification. It constrains naming and terminology quality across active artifacts without defining product capabilities, runtime contracts, stage activation, implementation truth, or learner-teaching procedure.

> Prefer the clearest concrete name that communicates the owned fact, action, or responsibility without requiring the reader to remember an internal vocabulary lesson.

A technically valid name is not sufficient when a more direct name would reduce cognitive load, explanation cost, or misuse risk.

This requirement applies especially to central product contracts, evidence states, source modules, public output labels, plans, and architecture decisions.

Project-wide learner-facing explanation, term introduction, required learning depth, and deferred depth are owned by `../../OPERATING_GUIDE.md` and the applicable Learning Skill/package contract. This standard may require a durable term to be clear or locally defined; it does not define how a teaching session must introduce that term.

## 2. Naming requirements

| ID | Requirement |
|---|---|
| `NAME-001` | A name SHOULD let a reader predict the component's main responsibility without reading its implementation or project history. |
| `NAME-002` | Functions SHOULD use a concrete action plus object, such as `extract_uv_lock_changes`, `compare_extracted_changes`, or `acquire_exact_repository_file`. |
| `NAME-003` | Data types SHOULD name the fact or evidence they contain, such as `DependencyVersionChange`, `DependencyChangeSourceEvidence`, or `DependencyChangeProblem`. |
| `NAME-004` | Broad labels such as `manager`, `processor`, `handler`, `interpreter`, `reconciler`, `context`, `canonical`, and `foundation` SHOULD NOT be used in new project-owned names when a more concrete responsibility can be stated. |
| `NAME-005` | Standard technical terms MAY be used when their standard meaning is important. A project-specific, overloaded, or non-obvious term MUST be defined at the narrowest durable owner when misunderstanding its meaning would materially affect implementation, evidence interpretation, maintenance, or user-facing output. |
| `NAME-006` | User-facing CLI/report labels SHOULD prefer plain terms such as `evidence source and exact identity` over unexplained specialist shorthand such as `provenance`, unless the specialist term is materially useful to the supported user and its meaning is made clear. |
| `NAME-007` | One concept SHOULD have one primary project term. Synonyms MUST NOT alternate casually when they could suggest different meanings. |
| `NAME-008` | Plan and document titles SHOULD state the exact owned responsibility, not merely a broad layer, phase, or architectural category. |
| `NAME-009` | Before an ADR, public contract, source type, module, or CLI label is frozen, apply the recall test: can a competent maintainer infer its purpose and boundary from the name with little or no project-specific decoding? |
| `NAME-010` | A shorter name is not automatically better. Prefer precise length over ambiguous brevity. |
| `NAME-011` | Renaming MUST preserve or deliberately migrate public diagnostics, imports, tests, documentation links, and evidence records where applicable. |
| `NAME-012` | Historical records SHOULD NOT be mass-rewritten solely to use newer vocabulary. Active controlling files and implementation SHOULD be corrected before new terms become durable. |

## 3. Artifact-local terminology rule

When an important project-specific or non-obvious technical term remains necessary in a durable artifact, define only the semantic context that artifact needs to prevent ambiguity, normally:

1. the practical meaning of the term in UpgradePilot;
2. the exact responsibility/fact the term names;
3. what nearby meaning it must not be confused with when that distinction is material;
4. the canonical owner when the term's full semantics live elsewhere.

Prefer one strong owning definition plus precise references over repeating a glossary entry in every artifact.

For learner-facing explanation—such as full-form expansion, why a term is named that way, relationship to the real product flow, and depth required now versus deliberately deferred—follow `../../OPERATING_GUIDE.md` and the applicable Learning-by-Doing/Learning-Only/package-local procedure rather than duplicating that teaching contract here.

A glossary may support recall, but it must not compensate for names that are unnecessarily vague.

## 4. Dependency-version-change vocabulary

For dependency evidence responsibilities, prefer this level of concrete vocabulary:

| Prefer | Practical meaning | Avoid as the primary new label |
|---|---|---|
| `DependencyVersionChange` | The trusted record that one package changed from one exact version string to another | `canonical contract` |
| `ExtractedDependencyVersionChange` | A possible change extracted from one supported dependency file | `candidate contract` when no contract is involved |
| `DependencyChangeSourceEvidence` | The file, revision, blob, and extraction method that support a change | `provenance` as an unexplained field or heading |
| `extract_exact_requirement_changes` | Read exact `package==version` patch evidence | `ExactPinDependencyInterpreter` |
| `extract_uv_lock_changes` | Compare exact base/head `uv.lock` files | `UvLockDependencyInterpreter` |
| `compare_extracted_dependency_changes` | Check whether extracted changes agree, conflict, or contain several package changes | `reconciler` or `reconciliation engine` |
| `DependencyChangeProblem` | An explicit reason a trusted change could not be established | broad `unsupported result` when a more exact reason exists |

Exact source names may evolve with implementation, but replacements should preserve equivalent responsibility clarity rather than treating this table as an immutable source-layout contract.

## 5. Active-file audit policy

Apply naming review proportionally:

- correct selected plans, new ADRs, active source, tests, and public output before freezing new architecture;
- update related active references when a central file or concept is renamed;
- leave dated historical files intact unless a broken link or factual error requires maintenance;
- do not launch a repository-wide rename merely for stylistic uniformity;
- revisit older active names when they are touched or when they materially obstruct understanding, testing, diagnosis, or ownership.

## 6. Change control

Change this standard only when the project-wide naming/terminology quality standard, artifact-local terminology rule, active-file migration policy, or historical-name preservation rule changes.

Do not update it for one ordinary variable, one temporary implementation name, routine progress, or a single stylistic preference.
