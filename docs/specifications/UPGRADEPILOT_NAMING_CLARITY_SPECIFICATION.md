# UpgradePilot Naming Clarity Specification

**Status:** Accepted controlling technical specification  
**Owner:** Ali Rajabi  
**Responsibility:** Keep names and technical terms in active UpgradePilot source, tests, commands, plans, specifications, ADRs, and user-facing output concrete enough that their purpose can be recalled with minimal project-specific decoding

## 1. Core rule

> Prefer the clearest concrete name that communicates the owned fact, action, or responsibility without requiring the reader to remember an internal vocabulary lesson.

A technically valid name is not sufficient when a more direct name would reduce cognitive load, explanation cost, or misuse risk.

This requirement applies especially to central product contracts, evidence states, source modules, public output labels, plans, and architecture decisions.

## 2. Naming requirements

| ID | Requirement |
|---|---|
| `NAME-001` | A name SHOULD let a reader predict the component's main responsibility without reading its implementation or project history. |
| `NAME-002` | Functions SHOULD use a concrete action plus object, such as `extract_uv_lock_changes`, `compare_extracted_changes`, or `acquire_exact_repository_file`. |
| `NAME-003` | Data types SHOULD name the fact or evidence they contain, such as `DependencyVersionChange`, `DependencyChangeSourceEvidence`, or `DependencyChangeProblem`. |
| `NAME-004` | Broad labels such as `manager`, `processor`, `handler`, `interpreter`, `reconciler`, `context`, `canonical`, and `foundation` SHOULD NOT be used in new project-owned names when a more concrete responsibility can be stated. |
| `NAME-005` | Standard technical terms MAY be used when their standard meaning is important, but the first material use MUST include a plain practical meaning and why the term is needed. |
| `NAME-006` | User-facing CLI labels and learning explanations SHOULD prefer plain terms such as `evidence source and exact identity` over specialist shorthand such as `provenance`, unless the specialist term is being taught deliberately. |
| `NAME-007` | One concept SHOULD have one primary project term. Synonyms MUST NOT alternate casually when they could suggest different meanings. |
| `NAME-008` | Plan and document titles SHOULD state the exact owned responsibility, not merely a broad layer, phase, or architectural category. |
| `NAME-009` | Before an ADR, public contract, source type, module, or CLI label is frozen, apply the recall test: can Ali infer its purpose and boundary from the name with little or no extra explanation? |
| `NAME-010` | A shorter name is not automatically better. Prefer precise length over ambiguous brevity. |
| `NAME-011` | Renaming MUST preserve or deliberately migrate public diagnostics, imports, tests, documentation links, and evidence records where applicable. |
| `NAME-012` | Historical records SHOULD NOT be mass-rewritten solely to use newer vocabulary. Active controlling files and implementation SHOULD be corrected before new terms become durable. |

## 3. Explanation rule

When an important technical term remains necessary, explain:

1. the full term;
2. its practical meaning;
3. why that name fits;
4. the exact responsibility it owns;
5. what it does not mean;
6. the depth required now and the depth deferred.

A glossary may support recall, but it must not compensate for names that are unnecessarily vague.

## 4. Dependency-version-change vocabulary

For the selected B2 dependency evidence responsibility, prefer this vocabulary:

| Prefer | Practical meaning | Avoid as the primary new label |
|---|---|---|
| `DependencyVersionChange` | The trusted record that one package changed from one exact version string to another | `canonical contract` |
| `ExtractedDependencyVersionChange` | A possible change extracted from one supported dependency file | `candidate contract` when no contract is involved |
| `DependencyChangeSourceEvidence` | The file, revision, blob, and extraction method that support a change | `provenance` as an unexplained field or heading |
| `extract_exact_requirement_changes` | Read exact `package==version` patch evidence | `ExactPinDependencyInterpreter` |
| `extract_uv_lock_changes` | Compare exact base/head `uv.lock` files | `UvLockDependencyInterpreter` |
| `compare_extracted_dependency_changes` | Check whether extracted changes agree, conflict, or contain several package changes | `reconciler` or `reconciliation engine` |
| `DependencyChangeProblem` | An explicit reason a trusted change could not be established | broad `unsupported result` when a more exact reason exists |

The exact source names may change during implementation review, but they must preserve this level of clarity.

## 5. Active-file audit policy

Apply naming review proportionally:

- correct selected plans, new ADRs, active source, tests, and public output before freezing new architecture;
- update related active references when a central file or concept is renamed;
- leave dated historical files intact unless a broken link or factual error requires maintenance;
- do not launch a repository-wide rename merely for stylistic uniformity;
- revisit older active names when they are touched or when they materially obstruct understanding, testing, diagnosis, or ownership.

## 6. Change control

Change this specification only when the project-wide standard for naming clarity, terminology teaching, active-file migration, or historical-name preservation changes.

Do not update it for one ordinary variable, one temporary implementation name, or routine progress.