# B2 Learning Snapshot — Public PR Through CI Authority

**Snapshot date:** 2026-07-24  
**Behavioral source/test commit:** `bdd178f38ad23e82a93cc5f3505932e5d0ef3b53`  
**Observed proof:** editable installation succeeded, 28 deterministic tests passed, and live `googlefonts/glyphsLib#1145` produced sufficient bounded CI authority.

## Purpose

This is a frozen educational snapshot of UpgradePilot at the end of the session:

```text
repository + Pull Request number
→ exact proposal identity
→ complete changed-file evidence
→ exact pinned dependency change
→ exact-head workflow and job evidence
→ exact-head workflow definition
→ bounded command interpretation
→ sufficient, insufficient, or unresolved CI authority
```

Later implementation changes should create a new learning snapshot instead of rewriting this one to describe different behavior. Educational corrections and guided explanations may be added only when they remain pinned to the same source/test state.

## The correct way to use this folder

The notes are not a substitute for source code. They prepare you to read the source with a purpose.

Use this loop:

```text
concept note
→ named source file and public function
→ matching test
→ close everything
→ explain input, output, invariant, and stopping state
→ predict one behavior
→ verify
```

Do not read the entire learning folder and only later open the code. Alternate between notes, implementation, and tests.

## Study order

### Mental model and reasoning

1. [`01-flow-and-boundaries.md`](01-flow-and-boundaries.md)
2. [`02-module-map.md`](02-module-map.md)
3. [`03-evidence-trust-and-identity.md`](03-evidence-trust-and-identity.md)
4. [`04-dependency-and-ci-authority.md`](04-dependency-and-ci-authority.md)
5. [`05-ai-era-code-ownership.md`](05-ai-era-code-ownership.md)
6. [`06-tests-diagnosis-and-design.md`](06-tests-diagnosis-and-design.md)

### Guided source and test reading

7. [`08-guided-source-walkthrough-core.md`](08-guided-source-walkthrough-core.md)
   - `cli.py`
   - `github_api.py`
   - `github_client.py`
   - `dependency_change.py`

8. [`09-guided-source-walkthrough-ci.md`](09-guided-source-walkthrough-ci.md)
   - `github_actions.py`
   - `github_repository.py`
   - `workflow_commands.py`
   - `ci_authority.py`

9. [`10-guided-test-reading-workbook.md`](10-guided-test-reading-workbook.md)
   - all six current test modules;
   - mock mechanism;
   - claims and failure localization;
   - Ali-owned normalized-package test.

### Session controller

10. [`07-smart-study-plan.md`](07-smart-study-plan.md)

Open the SMART plan first when beginning tomorrow. It tells you when to read each note and source file. The numerical order above represents subject progression, not a requirement to read everything continuously.

## How deeply to read source code

For each module:

```text
1. module docstring
2. public dataclasses and union result types
3. public functions and method signatures
4. main success path
5. failure, unsupported, insufficient, and unresolved branches
6. matching tests
7. private helpers only where they block understanding
```

After every module, record:

```text
This module owns:
Its main input is:
Its trusted output is:
It raises when:
It returns a bounded result when:
A failure would localize to:
```

## Learning-depth labels

- **Must master now:** explain, predict, safely modify, and diagnose with AI available.
- **Operationally understand:** read and make a small assisted change; memorization is unnecessary.
- **Introduced:** know the purpose and location.
- **Deferred:** intentionally outside the current responsibility; not completed.

## AI-era ownership standard

AI may write most implementation syntax. You still must own:

- the product question;
- input/output contracts;
- evidence identity and provenance;
- missing versus contradictory evidence;
- stopping and abstention conditions;
- test claims and failure localization;
- whether printed conclusions exceed the evidence;
- one meaningful test or rule modification plus explanation.

You do not need to memorize every GitHub field, Requests argument, regular-expression symbol, mock method, base64 detail, or YAML feature.

## Current bounded result

For S004:

```text
pytest 9.0.2 → 9.0.3
exact head: f3cda8a94600e58d27f1bc17c99b7693718b6350
Regression Tests: sufficient direct install-and-pytest evidence
Test + Deploy: unresolved because of multi-job/tox indirection
overall CI authority: sufficient
```

Permitted claim:

> At least one successful exact-head CI path directly exercised pytest.

Not established:

- complete test coverage;
- compatibility or upgrade safety;
- that every workflow exercised pytest;
- a merge recommendation;
- production readiness;
- independent ownership of the source.

## Completion definition

This snapshot is complete only when the observable readiness checks in `07-smart-study-plan.md` pass. Reading notes or source files without reconstruction, prediction, test modification, and diagnosis is not completion.