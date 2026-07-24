# B2 Learning Snapshot — Public PR Through CI Authority

**Snapshot date:** 2026-07-24  
**Behavioral source/test commit:** `bdd178f38ad23e82a93cc5f3505932e5d0ef3b53`  
**Observed proof:** editable installation succeeded, 28 deterministic tests passed, and live `googlefonts/glyphsLib#1145` produced sufficient bounded CI authority.

## Purpose

This is a frozen educational snapshot of UpgradePilot at the end of today's session:

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

Later implementation changes should create a new learning snapshot instead of rewriting this one.

## Study order

1. [`01-flow-and-boundaries.md`](01-flow-and-boundaries.md)
2. [`02-module-map.md`](02-module-map.md)
3. [`03-evidence-trust-and-identity.md`](03-evidence-trust-and-identity.md)
4. [`04-dependency-and-ci-authority.md`](04-dependency-and-ci-authority.md)
5. [`05-ai-era-code-ownership.md`](05-ai-era-code-ownership.md)
6. [`06-tests-diagnosis-and-claims.md`](06-tests-diagnosis-and-claims.md)
7. [`07-smart-study-plan.md`](07-smart-study-plan.md)

Use the notes actively:

```text
read one section
→ close it
→ reconstruct it aloud
→ inspect the named source/test
→ predict one behavior
→ verify
```

Do not read every source line equally. Start with module docstrings, public records, public functions, invariants, result states, and tests. Inspect helper syntax only when it blocks understanding.

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

You do not need to memorize every GitHub field, Requests argument, regular-expression symbol, mock method, or YAML feature.

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

This snapshot is complete only when the observable readiness checks in `07-smart-study-plan.md` pass. Reading the files alone is not completion.