# UpgradePilot M2-S01 Technical Contract Amendment

**Session ID:** M2-S01  
**Owner:** Ali Rajabi  
**Recorded:** 2026-07-21  
**Status:** Approved, controlling, and active amendment  
**Authority:** Read with `UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md`; this amendment supersedes conflicting M2-S01 wording and stop lines only  
**Reason:** Pre-code discussion exposed a missing project-level technical-contract layer and showed that the original eight-field “case identity” conflated snapshot identity, dependency transition, and changed-file evidence.

## 1. Amendment effect

The original M2-S01 plan remains the controlling transition plan for:

- the selected real case;
- the accepted `src/upgradepilot/` source boundary;
- the learning and ownership method;
- test-first execution;
- bounded implementation and stop lines;
- installation, import, test, diagnosis, and evidence requirements.

This amendment changes only the conceptual contract, pre-code decision gate, representation-method decision, and conflicting framework/dependency prohibitions.

The controlling UpgradePilot technical specification is:

```text
UpgradePilot/docs/specifications/
UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md
```

## 2. Corrected M2-S01 outcome

Replace the original outcome with:

> Given a manually assembled eight-field input derived from the completed M1 evidence report, preserve the raw input, validate and normalize the activated fields, and construct one trusted initial case record that separates pull-request snapshot identity, dependency change, and changed-file evidence.

This remains the first bounded transformation in the eventual PR-to-report path. It is not the complete M2 vertical slice and not the eventual public maintainer input interface.

## 3. Corrected conceptual model

The eight fields map as follows:

```text
repository + pr_number + base_sha + head_sha
→ PullRequestSnapshotIdentity

dependency + old_version + new_version
→ DependencyChange

changed_files
→ ChangedFileEvidence

all components + preserved raw/manual source reference
→ InitialCaseRecord
```

Accepted correction:

- repository, PR number, base SHA, and head SHA identify the exact PR snapshot;
- dependency and version transition describe the proposed dependency change;
- changed files are snapshot-associated evidence;
- the complete trusted result is an aggregate initial case record;
- the original eight-field flat dictionary remains a provisional M2 manual adapter only.

## 4. M2 manual-input contract

Required supplied fields remain:

```text
repository
pr_number
base_sha
head_sha
dependency
old_version
new_version
changed_files
```

Provisional M2 rules:

- all fields are required;
- unknown top-level fields are rejected unless the representation decision explicitly changes that rule;
- values use exact accepted types and are not silently coerced;
- surrounding whitespace is removed only from declared strings and changed-file paths;
- repository uses basic `owner/name` form;
- PR number is a positive integer and not a boolean;
- base and head SHAs are exactly 40 hexadecimal characters;
- dependency and versions are non-empty;
- old and new versions differ;
- changed files is a non-empty list of non-empty strings;
- raw input and its nested mutable values remain unchanged;
- no partially accepted initial case record is returned when the bounded adapter fails.

This contract validates supplied values. It does not prove remote repository or commit existence.

## 5. Evidence-state boundary

The session must preserve this distinction:

```text
invalid manual input
≠ missing external evidence
≠ inaccessible source
≠ stale evidence
≠ conflicting evidence
≠ internal runtime/programmer failure
```

M2-S01 may use a small exception surface for the bounded manual adapter. It must not claim that one `ValueError` policy is the permanent project-wide failure model.

## 6. Replacement pre-code gate

Before package metadata, source, tests, or a runtime dependency are created, Ali and the AI must complete one connected review covering:

1. why the public acquisition request may contain less information than the complete initial case record;
2. which fields identify the exact PR snapshot;
3. why dependency transition and changed files are separate from snapshot identity;
4. why raw input/source form must remain separate from trusted normalized form;
5. when invalid input rejects a record versus when missing/inaccessible/conflicting evidence becomes an explicit state;
6. what the first tests prove and do not prove;
7. which representation/validation method best satisfies the activated M2 contract and later M3 needs.

This gate is a design comparison, not a memory quiz or a requirement to invent unfamiliar framework mechanics without explanation.

## 7. Representation and validation method decision

The method is Open until compared against the accepted specification.

Candidate methods include:

- plain dictionaries plus explicit validation functions;
- `TypedDict` plus runtime validation;
- standard-library dataclasses;
- Pydantic models;
- a purpose-specific combination.

The comparison must cover:

- required-field and exact-type enforcement;
- strict versus coercing behavior;
- normalization order;
- field and cross-field validation;
- nested conceptual composition;
- raw-input preservation and mutation resistance;
- structured errors;
- machine-readable serialization;
- later schema/version evolution;
- separation from persistence models;
- dependency/security/upgrade cost;
- test clarity and diagnosis;
- Ali ownership and reversal path.

A selected external framework or durable cross-project representation policy requires an accepted ADR before implementation. A reversible standard-library choice may be recorded in the active plan and working memory when it creates no wider architectural commitment.

## 8. Amended deliverables

Before source implementation, M2-S01 must now include:

1. accepted core pipeline and contract specification in UpgradePilot;
2. this controlling plan amendment;
3. updated active working memory and current-state files;
4. a completed representation-method comparison;
5. an ADR when the selected method introduces a durable framework or cross-project representation policy.

After that decision, the original implementation deliverables remain:

- minimal `pyproject.toml` appropriate to the selected method;
- `src/upgradepilot/__init__.py`;
- the smallest source module(s) required by the initial case contract;
- `tests/test_case_identity.py` or a renamed test module if the accepted terminology changes;
- editable installation and import-path verification;
- valid, invalid, non-mutation, Ali-directed modification, and diagnosed-failure evidence.

Do not pre-create all conceptual contracts from the specification.

## 9. Amended execution sequence

### Step A — Accept the technical-contract baseline

- inspect the core pipeline specification;
- verify alignment with the charter, roadmap, milestone plan, and M1 evidence;
- record accepted, provisional, open, deferred, and rejected statements;
- update the active working record.

### Step B — Compare representation methods

- define the exact activated M2 contract;
- compare candidate methods using Section 7;
- use small examples or documentation where necessary;
- identify the simplest credible baseline;
- identify costs, failure modes, reversibility, and M3 consequences.

### Step C — Select and record the method

- Ali challenges or approves the recommendation;
- record the selected method and rejected alternatives;
- create an ADR when required;
- amend exact class/function/test names only after selection.

### Step D — Resume test-first implementation

- create the minimal installable package boundary;
- verify editable installation and import location;
- write the first valid contract test before behavioral implementation;
- implement the smallest passing behavior;
- add malformed-head-SHA coverage;
- prove non-mutation;
- complete one Ali-directed change and one diagnosed failure;
- record actual evidence and update the tracker.

## 10. Changed prohibitions

The original blanket prohibitions on schema frameworks and external runtime dependencies are superseded by:

> Do not add a framework or runtime dependency unless the representation-method comparison demonstrates an authorized project need, a simpler baseline is considered, costs and failure modes are explicit, Ali challenges or approves the decision, and any required ADR is accepted.

Still prohibited during M2-S01:

- live multi-source acquisition beyond an explicitly authorized bounded example;
- full evidence hierarchy implementation;
- persistence/database/ORM implementation;
- recommendation policy beyond a separately authorized later M2 responsibility;
- report generation beyond a separately authorized later M2 responsibility;
- CLI/API framework adoption unless separately admitted;
- CI, containers, cloud, services, queues, ML, graphs, LLMs, or agents;
- speculative internal source layers;
- restoration or copying of the removed scaffold.

## 11. Amended pass condition

M2-S01 passes only when:

- the core contract specification and this amendment are accepted and synchronized;
- the representation method is selected through an explicit comparison;
- any required ADR exists;
- the implementation models the corrected conceptual boundary rather than treating all eight fields as one permanent identity object;
- installation/import verification succeeds;
- central tests pass;
- malformed input and raw preservation are proven;
- one Ali-directed change and one diagnosed failure are preserved;
- assistance and capability evidence are recorded conservatively;
- no unreviewed framework or broader architecture was introduced.

Passing M2-S01 still does not pass M2.

## 12. Exact continuation

1. Synchronize this amendment and the accepted UpgradePilot core specification into current state and the Career tracker.
2. Review the activated M2 contracts only.
3. Compare plain validation, dataclass/typing, Pydantic, and any justified combination.
4. Select and record the representation method.
5. Resume the minimum test-first implementation under the selected method.
