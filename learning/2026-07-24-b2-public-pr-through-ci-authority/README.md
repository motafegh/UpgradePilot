# B2 Learning Snapshot — Public PR Through CI Authority

**Snapshot date:** 2026-07-24  
**Behavioral source/test commit:** `bdd178f38ad23e82a93cc5f3505932e5d0ef3b53`  
**Observed environment:** WSL2, Python 3.12, editable installation  
**Observed proof:** 28 deterministic tests passed and live `googlefonts/glyphsLib#1145` produced sufficient bounded CI authority

## Why this folder exists

This is an immutable educational snapshot of UpgradePilot at the end of today's session. It teaches the system as it exists now:

```text
public repository + Pull Request number
→ exact proposal identity
→ complete changed-file evidence
→ exact pinned dependency change
→ exact-head GitHub Actions evidence
→ exact-head workflow definition
→ bounded command interpretation
→ sufficient, insufficient, or unresolved CI authority
```

Later source changes must not silently rewrite this folder. A later implementation state should receive a new learning snapshot.

## What this snapshot is designed to achieve

By the end of the study sequence, Ali should be able to:

1. reconstruct the complete request-to-authority flow without notes;
2. explain which module owns each responsibility and why that boundary exists;
3. distinguish acquisition, validation, interpretation, authority, and recommendation;
4. explain why exact commit identity is required at every evidence boundary;
5. predict the major supported, insufficient, unresolved, and error outcomes;
6. read and materially modify one central rule or test with AI assistance;
7. diagnose which boundary failed from a test name, exception category, or CLI output;
8. state honestly what the current system proves and what it does not prove.

These are SMART outcomes:

- **Specific:** they target the current B2 source path only;
- **Measurable:** each outcome has a reconstruction, prediction, modification, or explanation check;
- **Achievable:** syntax details are limited to what is required for current ownership;
- **Relevant:** they protect the actual product claims and next implementation work;
- **Time-bounded:** the main sequence is designed for two focused sessions totaling roughly 2.5–3 hours, with breaks.

## How to use the files

Study in this order:

1. [`01-system-mental-model.md`](01-system-mental-model.md)
2. [`02-module-map-and-call-flow.md`](02-module-map-and-call-flow.md)
3. [`03-evidence-acquisition-and-trust.md`](03-evidence-acquisition-and-trust.md)
4. [`04-dependency-and-ci-authority.md`](04-dependency-and-ci-authority.md)
5. [`05-code-and-syntax-to-own.md`](05-code-and-syntax-to-own.md)
6. [`06-design-reasoning-and-tradeoffs.md`](06-design-reasoning-and-tradeoffs.md)
7. [`07-tests-diagnosis-and-claims.md`](07-tests-diagnosis-and-claims.md)
8. [`08-smart-study-and-ownership-check.md`](08-smart-study-and-ownership-check.md)

Do not read all files passively in one sitting. For every file:

```text
read one section
→ close the file
→ reconstruct the idea aloud or in notes
→ inspect the named source
→ predict one behavior
→ check the source or test
```

## Learning-depth labels

This snapshot uses four levels.

### Must master now

You should be able to explain, predict, modify, and diagnose the concept with AI assistance available.

### Operationally understand

You should recognize the syntax or mechanism, follow its use, and make a small change safely. Memorizing every API detail is unnecessary.

### Introduced

You should know what it is and where it belongs, but no implementation ownership is expected yet.

### Deferred

The topic is intentionally outside the current responsibility. Deferral is not completion.

## AI-era ownership standard

AI may write most code, but you must own the following:

- the product question being answered;
- the input and output contract;
- the evidence identity and provenance rules;
- the difference between missing evidence and contradictory evidence;
- the stopping and abstention conditions;
- the claims that a test or live run does and does not establish;
- the ability to inspect a generated change and detect a broken invariant;
- one meaningful modification or test plus an explanation of its result.

You do **not** need to memorize:

- every Requests method argument;
- every GitHub JSON field;
- every regular-expression symbol;
- every `unittest.mock` call form;
- every YAML feature;
- code that can be safely regenerated after you specify the correct contract and tests.

## Current proof boundary

The real S004 run established:

```text
pytest 9.0.2 → 9.0.3
exact PR head: f3cda8a94600e58d27f1bc17c99b7693718b6350
Regression Tests: successful, direct install-and-pytest evidence
Test + Deploy: successful, but unresolved because of multi-job/tox indirection
overall CI authority: sufficient
```

This means at least one successful exact-head CI path directly exercised the changed dependency.

It does not mean:

- every CI path exercised the dependency;
- tests provide complete coverage;
- the version is compatible in every environment;
- the update is safe;
- the Pull Request should be merged;
- the project is production-ready.

## Snapshot completion definition

This learning snapshot is complete only when Ali can pass the final checks in `08-smart-study-and-ownership-check.md`. Reading every file is activity, not completion.