# B2 Version and CI Evidence — Decision Cluster 3

**Local timestamp:** 2026-07-30 15:50 +03:30  
**Route:** B2 — Public PR vertical slice  
**Selected plan:** [`../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)  
**Downstream package plan:** [`../plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md`](../plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md)  
**Operation:** Learn and decide where exact dependency version observation ends, where PEP 440 semantics begin, and what exact-head CI may claim when dependency consumption is not proven  
**Result:** Decision Cluster 3 approved; both owning plans updated; no product source or tests changed

## Why this decision was required

The dependency evidence path reads version values such as:

```text
2.6 → 2.8.4
```

Several materially different questions can be asked about those values:

1. What exact text did the dependency files contain?
2. Are those values valid Python distribution versions?
3. Does the proposed version order after the old version?
4. Which official package releases fall inside the crossed interval?

Combining those questions inside dependency-file extraction would hide a real observed change when later Python package semantics are invalid or unsupported.

The current CI path also couples one exact requirements-file source path to one direct `pip -r` rule. That behavior is valid inside its admitted case, but it cannot be inherited by constraints files or `uv.lock` merely because they contain the same package version change.

## Approved exact version observation rule

Dependency-file extraction preserves:

```text
exact raw old version string
exact raw proposed version string
```

Extraction validates only the structure it directly observes:

- the version exists;
- it is textual;
- it is non-empty;
- it has no leading or trailing whitespace;
- old and proposed strings differ.

Extraction does not decide:

- whether the value follows PEP 440;
- whether the proposed version is newer;
- whether the version exists on PyPI;
- how releases are ordered;
- whether a crossed-version interval is valid.

This separation preserves observation from later interpretation.

## Why exact raw strings remain important

Different source strings may parse to equivalent Python versions. For example, a later PEP 440 method may treat forms such as:

```text
1.0
1.0.0
```

as equivalent for ordering.

UpgradePilot must still preserve the exact strings that each dependency file supplied. The approved extracted-change agreement rule remains:

```text
same normalized package
+
same exact raw old version
+
same exact raw proposed version
→ equivalent extracted changes
```

PEP 440 equivalence must not silently rewrite or merge different source observations.

## Approved PEP 440 responsibility

PEP 440 means **Python Enhancement Proposal 440**, the Python packaging standard for distribution version syntax and ordering.

PEP 440 validation begins in official package/upstream work before package release lookup and crossed-version ordering.

Selected implementation direction:

```text
packaging.version.Version
```

The package evidence stage preserves both:

```text
raw old/proposed strings
parsed old/proposed Version values
```

when parsing succeeds.

### Invalid Python package version

If either value cannot be parsed under the selected method:

```text
invalid_python_package_version
```

This means:

> A textual dependency version change was established, but at least one value cannot be used as a Python distribution version for official package release ordering.

It blocks package release interval and relevance work. It does not erase the observed `DependencyVersionChange` or relabel the case as “no dependency change.”

### Equivalent and non-forward versions

The package/upstream plan must also distinguish:

```text
raw strings differ but parsed Versions are equal
→ equivalent_python_package_versions

proposed parsed Version orders before old parsed Version
→ dependency_version_not_forward
```

These states prevent invalid forward-upgrade interval work without falsifying the source evidence.

### Dependency admission still required

The `packaging` runtime dependency is not yet installed or behavior-validated. Exact bounds and admission evidence remain required before implementation.

## Current CI responsibility inspected

The active source currently uses:

```text
CIAuthorityResult
sufficient / insufficient / unresolved
```

The supported successful rule requires one exact-head successful workflow path that visibly:

```text
pip install -r <changed requirements file>
+
directly invokes the changed package
```

The implementation already limits this claim to one proven path and does not claim complete test coverage, compatibility, safety, or merge readiness.

The terms “CI authority,” “sufficient,” and “insufficient” are broader than the exact responsibility and can be difficult to recall accurately.

## Approved clearer CI responsibility

Future shared result name:

```text
DependencyCIExerciseResult
```

Practical meaning:

> What exact-head CI evidence establishes about successful consumption and exercise of the changed dependency.

The implemented `CIAuthorityResult` remains current source truth until a tested migration replaces it.

## Approved CI exercise states

```text
proven
no_successful_ci
unresolved
```

### `proven`

At least one completed successful exact-head CI path satisfies an explicitly admitted dependency-consumption and package-exercise rule.

For the existing requirements-file rule:

```text
visible pip -r <exact changed requirements path>
+
direct changed-package invocation
+
completed successful exact-head job
→ proven
```

This proves one bounded CI path only.

### `no_successful_ci`

No completed successful exact-head CI job is available.

This is absence of the required successful execution evidence. It is not evidence of incompatibility or unsafety.

### `unresolved`

Successful exact-head CI exists, but UpgradePilot cannot prove through an admitted rule that the changed dependency was consumed and exercised.

Examples:

- workflow definition unavailable;
- workflow structure or commands outside the supported reader;
- several jobs that cannot be joined safely;
- script, tox, reusable-workflow, or custom-action indirection;
- changed-package invocation not visible;
- constraints-file consumption without a selected constraints-specific rule;
- `uv.lock` consumption without a selected bounded `uv` rule.

## Approved file-format-specific CI behavior

### Exact requirements files

The existing direct `pip -r` plus direct package-invocation rule may prove exercise when all current exact-head success conditions are met.

### Constraints files

Constraints files do not inherit requirements-file install semantics. A constraints file may limit a version without requesting installation.

Until a constraints-specific consumption rule is separately admitted:

```text
successful exact-head CI exists
+
change is established only through constraints evidence
→ unresolved
```

### `uv.lock`

A lockfile path does not prove how a workflow discovered or consumed it. `uv sync`, `uv run`, workspace roots, groups, extras, flags, and working directories can change the meaning.

Until a bounded `uv` consumption rule is separately admitted:

```text
successful exact-head CI exists
+
change is established only through uv.lock evidence
→ unresolved
```

### Equivalent evidence from several files

When several files prove the same `DependencyVersionChange`, one explicitly admitted evidence path may satisfy the narrow existential CI rule.

Example:

```text
requirements-dev.txt and uv.lock prove the same pytest transition
+
CI visibly installs requirements-dev.txt and invokes pytest
→ DependencyCIExerciseResult: proven
```

UpgradePilot does not need to prove that every supporting dependency file was consumed.

## Downstream behavior when CI is unresolved

An unresolved CI result:

- does not erase a trusted `DependencyVersionChange`;
- does not block package, upstream, or target evidence acquisition by itself;
- must remain visible to later sufficiency and decision work;
- must not be presented as successful dependency exercise or green compatibility evidence.

A later maintainer decision owns how unresolved CI affects action selection.

## Plan updates

Updated:

```text
plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md
```

The selected plan now owns:

- exact raw version preservation and structural validation;
- separation from PEP 440 semantics;
- `DependencyCIExerciseResult` terminology;
- `proven`, `no_successful_ci`, and `unresolved` meanings;
- requirements, constraints, and `uv.lock` CI distinctions;
- proof obligations and stop conditions for these rules.

Commit:

```text
8bbce1187427826fd49b47a20c915067da28ac19
```

Updated:

```text
plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md
```

The package/upstream plan now owns:

- PEP 440 validation with `packaging.version.Version`;
- raw and parsed version identity;
- invalid, equivalent, and non-forward version states;
- package release lookup only after valid forward version semantics.

Commit:

```text
3a61e9aa64dbaf99e9ed37b03eeb3f35038d942d
```

## Remaining design decisions

Decision Clusters 1–3 are approved. Before the ADR and product code, the remaining material decisions are:

1. exact S001 base/head `uv.lock` byte sizes;
2. contents endpoint versus exact-blob acquisition;
3. justified bounded maximum file size;
4. exact minimal fields used to prove an unchanged duplicate `uv.lock` group;
5. final clear source type, function, problem, module, and CLI names;
6. ADR alternatives, consequences, reversal, and reassessment triggers.

## No implementation performed

No product source, tests, runtime dependency, CLI behavior, or target repository was changed.

No claim is made that:

- `DependencyVersionChange` exists in runtime source;
- `DependencyCIExerciseResult` exists in runtime source;
- `packaging` is installed or admitted;
- PEP 440 validation is implemented;
- constraints or `uv.lock` CI consumption is understood;
- S001 passes through the product;
- Python support relevance exists;
- UpgradePilot is production-ready.