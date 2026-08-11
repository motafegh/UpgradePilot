# Real-World Case Screening 05 — Reproducibility Contract and Major Data-Stack Updates

**Date:** 2026-08-11  
**Status:** Completed bounded screening pass; non-controlling discovery/evaluation evidence  
**Branch:** `agent/product-simulation-case-screening-01`  
**Main product revision used for context:** `6202548eeff8c76405b8b53e0e35f0caeef53ef3`

## Purpose

This pass looked for real Python dependency updates that could add data/schema/analysis-contract diversity beyond the current runtime-focused corpus.

A major-version release was not enough by itself. The candidate needed a concrete target-side relationship or repository contract.

## Candidate A — FAIR-DM/fairdm #65 / pandas 2.3.3 -> 3.0.2

Exact proposal:

```text
repository: FAIR-DM/fairdm
PR: 65
base SHA: 796e5d5aa977c75c54274407f2e9f69509cf1d69
head SHA: d362be02e46c9b3cf4d8fe00356fb1cdee5f7168
pandas: 2.3.3 -> 3.0.2
```

The crossed pandas release contains major behavior changes, including default string dtype, Copy-on-Write, datetime-resolution changes, and removal of deprecated behavior.

But the exact target weakens the obvious applicability story:

- project `requires-python` is `>=3.13,<4.0`, so pandas 3's Python-3.11 floor does not matter;
- pandas is declared in the development dependency group, not production dependencies;
- checked repository search did not establish direct pandas imports/use.

### Disposition

**NEGATIVE / GENERALIZATION CONTROL. No numbered scenario.**

Useful confirmation:

```text
major release + many breaking changes
!=
material target mechanism established
```

and:

```text
dependency declaration
!=
runtime/applicability path established
```

Sources:

- https://github.com/FAIR-DM/fairdm/pull/65
- exact `pyproject.toml` at base SHA `796e5d5aa977c75c54274407f2e9f69509cf1d69`

---

## Candidate B — jamisonhburks/cgm-chronobiological-features #12 / pandas 2.2.2 -> 3.0.5

Exact proposal:

```text
repository: jamisonhburks/cgm-chronobiological-features
PR: 12
base SHA: 4a3459e27b2d7a8843a72c8e5a94333510fb5c49
head SHA: 9065f883c8c8d235018849b77ea43d89f36d600a
pandas: 2.2.2 -> 3.0.5
```

The PR changes one dependency line in `requirements.txt`.

### Exact target contract

The repository README says it contains the machine-learning notebook and reusable analysis package that reproduce the figures/results for a published 2025 PLOS Digital Health paper.

It documents the analysis environment as:

```text
Python 3.11.9
pandas 2.2.2
numpy 1.26.4
scipy 1.13.1
statsmodels 0.14.2
matplotlib 3.8.4
xgboost 2.1.2
scikit-learn 1.5.0
```

The exact `requirements.txt` makes the distinction even stronger:

```text
Versions pinned to those reported in the associated publication
```

followed by pandas and the other analytical-stack pins.

It separately labels additional notebook packages as versions for which `latest compatible releases are fine`.

Therefore the repository itself distinguishes:

```text
publication/reproduction environment pins
!=
ordinary flexible supporting dependencies
```

Sources:

- https://github.com/jamisonhburks/cgm-chronobiological-features/blob/4a3459e27b2d7a8843a72c8e5a94333510fb5c49/README.md
- https://github.com/jamisonhburks/cgm-chronobiological-features/blob/4a3459e27b2d7a8843a72c8e5a94333510fb5c49/requirements.txt

### Real pandas relationship

The analysis package directly imports pandas and uses it for:

- loading the archived processed dataset with `pd.read_parquet`;
- `DataFrame`/`Series` data contracts;
- column dropping/selection;
- feature-matrix construction;
- stratification inputs;
- construction/concatenation/sorting of feature-importance DataFrames.

Sources:

- `src/data.py` and `src/plots.py` at exact base SHA.

This establishes direct analytical use. It does not yet establish which pandas-3 behavior changes alter the published numerical result.

### Proposal-induced repository inconsistency

The Dependabot PR changes:

```text
pandas==2.2.2
→
pandas==3.0.5
```

but does not update:

- the requirements comment saying these versions are pinned to the publication;
- the README analysis-environment statement naming pandas 2.2.2;
- the repository's stated purpose of reproducing the paper's figures/results.

Thus the proposed repository state contains a deterministic context inconsistency:

```text
dependency installation contract says pandas 3.0.5
while
reproduction documentation still identifies pandas 2.2.2
as the reported/published analysis environment
```

This does **not** prove the new environment produces different scientific results. It proves that the proposal changes the declared reproduction environment without reconciling the repository's own provenance/context statements.

### Automation/validation boundary

The repository has weekly pip Dependabot configuration for the root dependency file.

The exact tree contains no GitHub Actions workflow files; the only `.github` file is `dependabot.yml`. The checked combined status for the Dependabot head returned no statuses.

Interpretation:

```text
automated update proposal exists
!=
automated scientific-reproduction validation exists
```

and:

```text
no checked status
!=
scientific result changed
```

Source:

- https://github.com/jamisonhburks/cgm-chronobiological-features/blob/4a3459e27b2d7a8843a72c8e5a94333510fb5c49/.github/dependabot.yml

### Why this is distinct

This candidate exposes a responsibility explicitly outside the current A-C implementation boundary:

```text
TECHNICAL IMPACT/APPLICABILITY
Does a changed dependency mechanism affect target behavior/environment?

!=

REPOSITORY CONTEXT / POLICY / PROVENANCE
Does the proposal conflict with the repository's declared purpose or reproducibility contract?
```

The second question can matter even when technical compatibility remains unresolved or eventually proves acceptable.

### Disposition

**PROMOTE TO S009 ADMISSION.**

Owned question:

> Can a real dependency update be technically unproven either way yet already create a material repository-level reproducibility/provenance inconsistency, and what evidence should remain separate from technical impact/applicability until a later overall-sufficiency/maintainer-facing responsibility is admitted?

Do not turn S009 into a full pandas-3 numerical reproducibility experiment or open Conversation D on main.

---

## Screening result

1. FAIR-DM #65 remains a useful negative control: major-release severity alone is not target applicability.
2. CGM Chronobiological Features #12 is admitted as S009 because the proposal conflicts with an explicit publication-reproduction dependency contract before any numerical-result claim is needed.
3. S009 should remain a repository-context/provenance simulation, not be forced into the technical A/B applicability model.
4. Any later claim that pandas 3 changes the paper's metrics would require separate execution/data/evaluation evidence.
