# S005 Case Record — ModelArrayIO pytest 9.0.3 → 9.1.1

## Live state

**Run:** `s005-20260723T123700Z-r1`  
**Mode:** prospective manual simulation  
**State:** selected and frozen; transparent baseline executed; full action-change assessment pending

## Why this case was selected

S001–S003 showed the same broad action with materially stronger full support. S004 showed the baseline could be sufficient. S005 must now test whether target-specific evidence can change the broad action.

Candidate screening is preserved in [`../../S005_CANDIDATE_SCREENING.md`](../../S005_CANDIDATE_SCREENING.md).

## Frozen event

Dependabot proposed changing one resolved direct test dependency in `PennLINC/ModelArrayIO`:

```text
pytest 9.0.3
→ pytest 9.1.1
```

Frozen identity:

- PR `#85`;
- base `915781a6c967f22b9236ecba072300932c2f41f0`;
- head `b590cfe93fbe49235f0f68d2b87102672f8a0aa0`;
- changed file `uv.lock`;
- observed merge commit `f7f58496507477c7ebaba40921859c18c771c1e4`.

The observed merge is maintainer action, not correctness evidence.

## Transparent baseline

Restricted inputs:

- version category: `minor`;
- current CI conclusion: `passing`;
- dependency directness: `direct`;
- literal caution signals: `breaking`, `removals`, `deprecations`, `deprecated`.

Rule B04 selects:

> `run_targeted_checks`

Baseline limitation:

> It cannot interpret whether the upstream caution surfaces exist in the frozen repository, whether the changed lock supplied pytest to the successful jobs, or whether an additional check can answer a remaining target-specific question.

## Full-investigation questions

1. Did exact-head CI execute pytest 9.1.1 from the changed `uv.lock`?
2. Which pytest 9.1 breaking and deprecated surfaces are actually present in the frozen target?
3. Did relevant ordinary and data-backed test responsibilities pass across the supported Python matrix?
4. Does any unresolved target-specific compatibility question remain that an additional targeted check could answer?
5. Should the full action remain `run_targeted_checks`, change to `merge_after_normal_review`, or abstain?

## Evidence mapping required

The official pytest 9.1.1 changelog must be mapped to the frozen repository for:

- `--doctest-modules` with inline module/package/session autouse fixtures;
- class-scoped fixture instance methods;
- teardown-time `request.getfixturevalue()`;
- non-Collection parametrization values;
- private `config.inicfg`;
- private fixture-registration `baseid`/`nodeid` and `FixtureDef.has_location`;
- hook configuration markers;
- `--pastebin`;
- `pytest.console_main`;
- `yield_fixture`.

## Stop and switch rules

Change the action to `merge_after_normal_review` only when:

1. pytest 9.1.1 identity is tied to the exact successful head jobs;
2. the upstream breaking behavior is not activated by frozen configuration/usage;
3. deprecated surfaces are absent or used in a non-deprecated form;
4. ordinary relevant tests pass across Python 3.11–3.14;
5. the broader Python 3.12 job includes downloaded-data tests and passes;
6. no unresolved evidence gap identifies a useful additional check.

Retain `run_targeted_checks` if any material surface remains untested or unresolved. Abstain if exact identity or repository usage cannot be established. Do not create failure-attribution state unless a real failure or conflicting execution appears.