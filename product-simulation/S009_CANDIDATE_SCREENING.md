# S009 Candidate Screening — Published Analysis Reproducibility Contract

**Date:** 2026-08-11  
**Status:** **ADMITTED — prospective untouched real public case**  
**Candidate:** `jamisonhburks/cgm-chronobiological-features#12`  
**Case ID:** `S009-cgm-pandas-publication-reproducibility-contract`  
**Role:** non-controlling repository-context/provenance discovery evidence; future overall-sufficiency/maintainer-facing transfer case

## Owned question

> Can a real dependency update create a material repository-level reproducibility/provenance inconsistency even before technical compatibility or numerical-result impact is established, and what evidence must remain separate from mechanism-specific technical applicability?

This case does **not** ask whether pandas 3.0.5 changes the paper's metrics, whether the code runs, or what maintainer action should be taken.

## Frozen proposal identity

```text
repository: jamisonhburks/cgm-chronobiological-features
PR: 12
base: main
base SHA: 4a3459e27b2d7a8843a72c8e5a94333510fb5c49
head SHA: 9065f883c8c8d235018849b77ea43d89f36d600a
changed file: requirements.txt
old: pandas==2.2.2
new: pandas==3.0.5
```

Primary source: https://github.com/jamisonhburks/cgm-chronobiological-features/pull/12

## Exact repository reproduction contract

At the exact base revision, the repository README states that it contains the notebook and reusable analysis code that reproduce the figures/results for a 2025 PLOS Digital Health paper.

It documents the reported analysis environment as Python 3.11.9 with pandas 2.2.2 and the rest of the pinned scientific stack.

The base `requirements.txt` states:

```text
Versions pinned to those reported in the associated publication
```

and then pins pandas 2.2.2, NumPy, SciPy, scikit-learn, XGBoost, Matplotlib and statsmodels.

The same file separately labels extra notebook packages as packages for which `latest compatible releases are fine`.

Therefore the repository explicitly distinguishes:

```text
publication/reproduction environment pins
!=
ordinary flexible supporting dependencies
```

Sources:

- exact base `README.md`
- exact base `requirements.txt`

## Proposed-head inconsistency

At the exact Dependabot head:

- `requirements.txt` still says the analytical versions are pinned to those reported in the publication;
- the pandas line is now `pandas==3.0.5`;
- the unchanged README still states that the analysis was performed with pandas 2.2.2 and instructs readers to run the repository to reproduce the figures/metrics.

Therefore the proposed state deterministically contains:

```text
installation dependency contract: pandas 3.0.5

while

published/reproduction environment documentation: pandas 2.2.2
```

This establishes a repository-context/provenance inconsistency. It does **not** establish a numerical-result difference.

Sources:

- head `requirements.txt` at `9065f883c8c8d235018849b77ea43d89f36d600a`
- head `README.md` at the same revision

## Real technical relationship remains separate

The target code genuinely imports and uses pandas for:

- Parquet data loading;
- DataFrame/Series contracts;
- row/column filtering and dropping;
- feature construction and stratification inputs;
- feature-importance DataFrame construction/concatenation/sorting.

That means pandas technical-impact candidates are plausible.

However S009 does not need to select one pandas-3 breaking mechanism to establish its owned context claim.

Keep separate:

```text
repository reproducibility contract changed/inconsistent
!=
pandas 3 technically incompatible
!=
published metrics changed
```

## Automation/validation boundary

The repository enables weekly pip Dependabot updates for the root directory.

The exact tree contains no GitHub Actions workflow files; `.github/dependabot.yml` is the only `.github` file. The checked combined status for the Dependabot head returned no statuses.

Thus:

```text
automated dependency proposal
!=
automated reproduction validation
```

No-status evidence is not treated as proof of changed scientific output or failed validation.

## Why existing cases do not answer S009

S001-S008 primarily examine technical impact, applicability, evidence, investigation, installation, CI, and stopping.

S009 adds a different decision-context layer:

```text
TECHNICAL QUESTION
What mechanism changes and does it apply?

!=

REPOSITORY CONTEXT / PROVENANCE QUESTION
What object/purpose does this repository say it preserves,
and does the proposal remain consistent with that declared contract?
```

The second may matter even when technical behavior is compatible.

## Admission gates

- **Named question:** PASS — explicit reproduction/provenance consistency.
- **Existing-evidence gap:** PASS — no prior numbered scenario centers an explicit published-analysis environment contract.
- **Consequence:** PASS — tests separation of technical impact from repository-policy/provenance context relevant to later overall sufficiency/action synthesis.
- **Evidence feasibility:** PASS — exact PR/base/head/docs/requirements/source are public and frozen.
- **Safe boundary:** PASS — owned question requires only read-only repository evidence.
- **Negative result:** PASS — if head docs had been updated consistently, the inconsistency hypothesis would be refuted and remain useful.
- **Claim limit:** PASS — no numerical/scientific-result or maintainer-action claim.
- **Stop condition:** PASS — stop once the exact base/head contract and inconsistency are established and technical-result uncertainty is kept separate.
- **Case form:** PASS — untouched real public evidence is sufficient.

## Provisional proposition map

These are simulation questions, not runtime schema.

```text
P1 repository declares itself a reproduction artifact                         established
P2 pandas 2.2.2 is part of the documented/published analysis environment      established
P3 proposal changes the installed pandas pin to 3.0.5                         established
P4 proposal reconciles reproduction documentation with that change            refuted
P5 pandas 3.0.5 changes executable/numerical behavior for this exact analysis unresolved
P6 published figures/metrics differ under the proposed environment             unresolved
```

P1-P4 are sufficient for the owned repository-context inconsistency. P5-P6 are separate technical/scientific propositions.

## Stopping objective

Do not download the dataset or rerun the published analysis merely to establish P1-P4.

A reproduction run could become relevant only for a separately admitted question about P5/P6. It cannot retroactively change the fact that the proposed repository metadata/documentation is internally inconsistent about the reported analysis environment.

## Admission result

```text
S009 ADMITTED
primary novelty: repository reproducibility/provenance contract
primary boundary: technical applicability != repository-context consistency
future value: overall sufficiency / repository policy / maintainer-facing synthesis
```

No Conversation-D opening, product implementation, scientific-result claim, or maintainer recommendation follows from this admission.