# S009 — CGM Pandas Publication Reproducibility Contract

**Status:** Completed bounded repository-context/provenance analysis  
**Case form:** Untouched real public Dependabot PR  
**Candidate screening:** [`../../S009_CANDIDATE_SCREENING.md`](../../S009_CANDIDATE_SCREENING.md)

## Owned question

> Can a real dependency update create a material repository-level reproducibility/provenance inconsistency even before technical compatibility or numerical-result impact is established?

## Frozen identity

```text
repository: jamisonhburks/cgm-chronobiological-features
PR: 12
base SHA: 4a3459e27b2d7a8843a72c8e5a94333510fb5c49
head SHA: 9065f883c8c8d235018849b77ea43d89f36d600a
pandas: 2.2.2 -> 3.0.5
```

## Result

The exact base repository states that it reproduces the figures/results of a published 2025 analysis and documents pandas 2.2.2 as part of the analysis environment.

Its requirements file explicitly says the analytical package versions are pinned to those reported in the publication, while separately allowing latest-compatible versions for supporting notebook packages.

At the Dependabot head, only the pandas pin changes:

```text
pandas==2.2.2
→
pandas==3.0.5
```

The requirements comment remains unchanged and still says those pins are the publication-reported versions. The README also remains unchanged and still names pandas 2.2.2 as the analysis environment.

Therefore the proposed state is internally inconsistent about the repository's declared reproduction environment.

## What is established

```text
repository purpose = reproduce published ML figures/results        established
reported/published pandas environment = 2.2.2                     established
proposal installation pin = 3.0.5                                established
proposal reconciles docs/provenance with the changed pin           refuted
```

## What remains unresolved

```text
pandas 3.0.5 changes executable behavior for this exact analysis   unresolved
pandas 3.0.5 changes published metrics/figures                     unresolved
```

Those unresolved questions do not weaken the owned context conclusion because they are different propositions.

## Why this case matters

S009 demonstrates:

```text
technical compatibility
!=
repository-purpose / provenance consistency
```

A dependency update can require maintainer context even if the code eventually proves compatible, because the repository may intentionally preserve a historically exact environment rather than simply seek the newest compatible stack.

This is especially important for scientific/reproducibility repositories, benchmark repositories, archival fixtures, conformance suites, or other repositories where exact versions are part of the artifact being preserved.

## Automation boundary

The repository enables weekly pip Dependabot updates, but the exact tree contains no GitHub Actions workflows. The existence of automated update proposals therefore does not establish automated reproduction validation.

This also exposes a useful automation-policy tension:

```text
broad update automation configured
+
exact historical environment intentionally pinned
```

The simulation does not infer which one the maintainer wants to dominate. That is maintainer/repository-policy context, not something technical evidence alone can decide.

## Why no reproduction run was performed

The owned question is whether the proposal creates a repository-contract inconsistency. Exact base/head repository evidence already settles that.

Running the large published analysis would answer a different question about behavioral or numerical reproducibility under pandas 3.0.5.

The dataset is external and approximately 331 MB. No such execution is necessary for the owned question.

## Main discoveries

1. **Exact dependency versions can be part of the repository artifact, not merely installation constraints.**
2. **A technically compatible update can still conflict with declared repository purpose/provenance.**
3. **Repository context must not be silently collapsed into mechanism-specific applicability.**
4. **Automated update generation is not proof that updating every dependency is semantically appropriate.**
5. **Technical uncertainty and repository-context inconsistency can coexist.**

## Cross-case relationship

```text
S001-S008
primarily technical mechanism/applicability/investigation evidence

S009
repository purpose/provenance context
that can matter independently of technical applicability
```

This makes S009 useful future evidence when UpgradePilot eventually opens overall evidence sufficiency, repository-policy/residual-risk, and maintainer-facing synthesis.

It does not justify opening that responsibility now.

## Claim limits

S009 does not establish:

- pandas 3.0.5 incompatibility;
- changed scientific metrics;
- invalidity of the published paper;
- that maintainers must reject the PR;
- that dependency pins can never be modernized;
- a universal rule that publication repositories must never update dependencies;
- current product support for repository-policy interpretation.

## Reading order

1. [`../../S009_CANDIDATE_SCREENING.md`](../../S009_CANDIDATE_SCREENING.md)
2. [`artifacts/CASE_IDENTITY.json`](artifacts/CASE_IDENTITY.json)
3. [`artifacts/REPRODUCIBILITY_CONTEXT.json`](artifacts/REPRODUCIBILITY_CONTEXT.json)
4. [`artifacts/BOUNDARY_AND_STOPPING.json`](artifacts/BOUNDARY_AND_STOPPING.json)
