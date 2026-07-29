# B2 Dependency File Rules — Decision Cluster 2

**Local timestamp:** 2026-07-30 01:27 +03:30  
**Route:** B2 — Public PR vertical slice  
**Selected plan:** [`../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)  
**Operation:** Learn, compare, and decide which dependency files may supply exact package-version-change evidence  
**Result:** Decision Cluster 2 approved; selected plan updated; no product source or tests changed

## Why this decision was required

The active dependency extractor scans every changed file for complete lines shaped like:

```text
-package==old_version
+package==new_version
```

That syntax can appear in a real requirements file, but it can also appear in a README, tutorial, fixture, migration note, copied diff, generated report, or other example text. Syntax alone therefore cannot establish that the file is an admitted dependency source.

The selected architecture requires two separate questions:

```text
1. Does this path identify an admitted dependency file?
2. What exact package version change does that file establish?
```

This prevents arbitrary changed-file text from becoming trusted dependency identity.

## Approved exact requirements and constraints path rules

### Descriptive filenames

A normalized relative path is eligible when its final lowercase filename is:

```text
requirements.txt
requirements.in
requirements-<description>.txt/.in
requirements_<description>.txt/.in
requirements.<description>.txt/.in

constraints.txt
constraints.in
constraints-<description>.txt/.in
constraints_<description>.txt/.in
constraints.<description>.txt/.in
```

Examples:

```text
requirements-dev.txt
requirements_test.in
requirements.docs.txt
constraints-ci.in
constraints_python310.txt
```

The rule excludes unrelated names such as:

```text
my-requirements-example.md
requirements_notes.md
README.txt
dependency-list.txt
```

### Dependency directories

A normalized relative `.txt` or `.in` file is also eligible when any directory component is named exactly:

```text
requirements
```

or:

```text
constraints
```

Examples:

```text
requirements/base.txt
config/requirements/test.txt
services/api/requirements/prod.in
constraints/python/py310.txt
```

### Nested paths

The same rules apply at any repository depth. UpgradePilot preserves the complete relative path and does not use repository-specific allowlists.

Examples:

```text
backend/requirements.txt
docs/requirements.txt
services/api/requirements/dev.txt
```

Path eligibility establishes only that the file is allowed to supply exact package/version evidence. It does not establish whether the file represents runtime, development, documentation, test, fixture, or example usage.

## Requirements versus constraints

A requirements file may request installation. A constraints file limits versions selected by another installation request and does not necessarily request installation itself.

Both may establish:

```text
package old_version → proposed_version
```

Neither filename alone establishes:

- package installation;
- CI consumption;
- dependency role;
- repository usage;
- compatibility;
- safety.

This preserves the previously approved separation:

```text
dependency change source evidence
≠
proven CI install or consumption evidence
```

## Why `uv.lock` duplicate names require conservative handling

Official uv documentation describes `uv.lock` as a universal, cross-platform lockfile that captures packages across Python and platform markers. uv's resolver can split resolution across marker regions, so the same package name can participate in multiple environment-specific resolution branches.

Relevant official references consulted:

- [uv structure and files](https://docs.astral.sh/uv/concepts/projects/layout/)
- [uv resolution](https://docs.astral.sh/uv/concepts/resolution/)
- [uv resolver internals](https://docs.astral.sh/uv/reference/internals/resolver/)

Package name alone may therefore be insufficient to pair changed duplicate records responsibly.

Three policies were considered:

1. reject every lockfile containing any duplicate name — safe but unnecessarily restrictive;
2. implement complete marker/source/resolution identity — broader than B2;
3. ignore duplicate groups proven unchanged and abstain when a duplicate group changes.

The third policy was selected.

## Approved `uv.lock` duplicate-group rule

```text
one package record in base + one record in head
→ compare normally

repeated-name group unchanged under the admitted identity comparison
→ does not block an unrelated clear package version change

repeated-name group differs between base and head
→ ambiguous_uv_lock_package_records
```

UpgradePilot must not:

- select the first duplicate record;
- pair records by list position;
- collapse different sources;
- ignore marker or resolution differences;
- claim complete uv resolution understanding.

The exact minimal fields used to prove a duplicate group unchanged remain to be frozen in the ADR and tests. Artifact URLs, hashes, wheel lists, sizes, and upload times must not create false dependency-version changes.

## Approved `uv.lock` file-status and path rule

The first supported boundary requires:

```text
GitHub status: modified
basename: uv.lock
same complete relative path at base and head
both exact files available
```

Nested paths such as:

```text
services/api/uv.lock
```

are eligible when the same full relative path exists at both exact revisions.

The first boundary excludes:

- added lockfiles — no prior lock state and usually many introduced packages;
- deleted lockfiles — no proposed lock state;
- renamed lockfiles — additional file-identity and project-scope questions.

## Plan update

Updated:

```text
plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md
```

The plan now records the selected rules and removes these matters from its unresolved-decision list.

Commit:

```text
69dd9040fb5e8265163f2d491a8d14f6d419b6f1
```

The plan also adds proof obligations for:

- rejecting arbitrary example files;
- accepting conventional root and nested paths;
- keeping constraints evidence separate from install authority;
- allowing unchanged duplicate `uv.lock` groups;
- rejecting changed duplicate groups as ambiguous;
- keeping added, deleted, and renamed lockfiles outside the first rule.

## Decisions still unresolved

1. exact raw-version validation and where PEP 440 parsing and ordering begin;
2. CI result behavior when a supported dependency file's consumption is not established;
3. exact S001 base/head lockfile sizes, endpoint, and bounded acquisition maximum;
4. exact identity fields used only to prove an unchanged duplicate `uv.lock` group;
5. final clear source type, function, problem, module, and CLI names;
6. ADR alternatives, consequences, reversal, and reassessment triggers.

## No implementation performed

No active source, test, runtime dependency, CLI behavior, or target repository was changed.

No claim is made that:

- exact path filtering is implemented;
- constraints files are supported in product code;
- `uv.lock` extraction exists;
- duplicate package records can currently be evaluated;
- S001 passes the dependency identity stage;
- CI understands requirements, constraints, or uv consumption beyond already validated behavior.

## Exact continuation proposed by this record

Proceed to one coherent operational-boundary discussion:

1. explain why raw version identity should remain separate from PEP 440 ordering;
2. decide where package/version validation and release ordering begin;
3. define the honest CI result when dependency-file consumption is not proven;
4. then measure S001 lockfile size and select a bounded exact-file acquisition method;
5. finalize duplicate-group identity fields and source/output names;
6. create the ADR only after those decisions are complete.
