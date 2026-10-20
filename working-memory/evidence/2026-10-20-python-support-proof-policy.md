# Python packaging compatibility versus hosted qualification — audit-branch disposition

**Date:** 2026-10-20  
**Branch:** `audit/project-wide-system-audit-2026-10-20`  
**Status:** audit/correction disposition; user-facing owner reconciliation pending before integration  
**Related:** AUDIT-016, AUDIT-018, AUDIT-019 and Stage-7 remediation

## Current facts

`pyproject.toml` declares:

```toml
requires-python = ">=3.12"
```

The current Product verification job installs and tests the product with Python 3.12 on Ubuntu 24.04. Historical quickstart/hosted evidence also uses Python 3.12.

Therefore two different statements must remain separate:

1. **Packaging compatibility/admission boundary:** package metadata does not reject Python versions at or above 3.12.
2. **Hosted qualification boundary:** the repository currently has deterministic hosted product proof for Python 3.12 only.

The first statement is not proof of the second for every future/newer minor version.

## Decision

Do **not** narrow `requires-python` merely to make the current test matrix match the metadata. No evidence currently establishes that newer Python minors are incompatible, and an artificial upper bound would be a product/package claim without technical justification.

Also do **not** describe every `>=3.12` interpreter as equally qualified by current hosted evidence.

Use this claim model until a broader matrix is deliberately selected and passes:

```text
package metadata admits Python >=3.12
current hosted qualified line = Python 3.12
later Python minors = packaging-admissible but not yet covered by the repository's hosted compatibility matrix
```

This distinction is about evidence strength, not a custom runtime state or package enum.

## Required owner reconciliation before integration

### README / installation guidance

Replace wording that can be read as “3.12+ is verified” with wording equivalent to:

> UpgradePilot's package metadata requires Python 3.12 or newer. The current hosted product-verification path qualifies Python 3.12; later Python minors are not yet part of the hosted compatibility proof.

Quickstart may still tell users that Python 3.12+ satisfies package metadata, but the verified reference path should name 3.12 explicitly.

### Product verification documentation

State that the workflow currently qualifies Python 3.12 only. Do not call that a full `>=3.12` compatibility matrix.

The audit branch has already changed the workflow triggers to manual + PR-to-main + push-to-main, but that changed workflow still needs its own hosted execution proof after integration/appropriate trigger.

### Future matrix expansion

Do not add Python versions merely because they exist. Expand the matrix when one of these is selected:

- public/release support commitment for named Python minors;
- a real compatibility issue needs cross-version diagnosis;
- portfolio/release evidence requires a broader supported matrix;
- dependency support changes make another minor materially relevant.

For each newly claimed line, run the same installed-package/CLI/deterministic-product responsibility unless a documented reason requires a different job.

## Non-claims

This disposition does not establish that:

- Python 3.13+ fails;
- Python 3.13+ passes;
- all dependencies publish compatible artifacts for every future Python version;
- the project should pin an upper Python bound;
- a green interpreter matrix proves live acquisition/model behavior.

## Integration gate

Before this audit branch's proof/documentation changes are integrated into `main`:

1. reconcile README wording with this distinction;
2. retain `requires-python = ">=3.12"` unless separate compatibility evidence justifies changing it;
3. obtain hosted proof for the selected Product verification workflow revision;
4. record exact interpreter(s) actually proven.
