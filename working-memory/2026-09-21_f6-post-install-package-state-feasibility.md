# F6 post-install package-state evidence feasibility — 2026-09-21

**Session status:** ACTIVE — bounded Planning/Design + Learning-by-Doing. No F6 product implementation is authorized merely by this selection.
**Prior:** F5 target wheel-tag evidence-source feasibility CLOSED; F4 CI-consuming job → Target composition CLOSED.
**Controlling route:** `plans/END_TO_END_PRODUCT_FLOW_LEARNING_AND_EVIDENCE_TO_ACTION_EXECUTION_PLAN.md`; accepted synthesis semantics remain unchanged.

## A — orientation: DONE

The current product admits exact dependency transitions. Requirements evidence requires an exact `package==version` pin, and the supported pyproject optional-dependency path also requires exactly one non-wildcard `==version` transition. Therefore current normal F6 value is **not** discovering the proposed version from a range.

The actual question is narrower:

> Can the read-only normal evidence path establish that the exact proposed dependency version is actually present in the selected dependency-consuming CI environment after the relevant install/sync step?

This proposition is separate from wheel/sdist identity, exact supported wheel tags, behavioral compatibility, test-path exercise, and maintainer-action permission.

## B — source/proof-boundary inspection: DONE for initial design slice

- `dependency/change.py` promotes only exact old/proposed versions across admitted sources.
- `dependency/requirements.py` admits conventional requirements/constraints changes only as exact `package==version` transitions.
- `dependency/pyproject.py` admits the current optional-extra rule only when both sides use one exact non-wildcard `==version` specifier.
- `ci/dependency_exercise.py` explicitly states that `supported_runtime_correlated` does **not** prove exact resolved versions, wheel selection, or compatibility.
- `github/actions.py` acquires exact-head run/job/step metadata only; it has no job-log acquisition or package-state evidence surface.
- `dependency/direct_install.py` observes that an admitted parsed `pip install` occurrence directly names the independently established requirements source. It does not establish execution, success, or installed versions and does not interpret every install modifier as installation-state semantics.
- No existing UpgradePilot source path was found for target-owned `pip freeze`, `pip show`, `pip list`, or `importlib.metadata` package-state output.

### Refined F6 responsibility

A useful F6 producer, if feasible, should establish a **post-install package-state witness** bound to:

```text
repository
+ exact PR head revision
+ exact workflow/run attempt
+ exact selected dependency-consuming job/environment
+ normalized package identity
+ observed installed version
```

For the current bounded goal, artifact filename, wheel/sdist type, wheel tags, and behavior/test execution are intentionally outside the contract unless a later selected proposition requires them.

## C — decision value established: DONE

The witness would support the bounded proposition:

> The exact proposed dependency version is present in this exact CI environment.

It can refute the narrower concern:

> The proposed exact version was not actually installed/present in this environment.

It does **not** prove:

- the affected behavior was exercised;
- behavioral compatibility;
- success in other supported environments;
- wheel versus source installation;
- merge/block/targeted-check permission by itself.

## D — learner ownership check: DONE at current conceptual depth

Ali correctly distinguished:
- successful unrelated tests from proof of exercising the affected behavior;
- exact installed-version evidence from artifact-mechanism evidence;
- and installation evidence from maintainer-action permission.

A source-grounded correction was also made during the slice: the earlier range-resolution example was useful conceptually but is not representative of UpgradePilot's current admitted normal dependency-change model, which is exact-version based.

## E — next bounded action: SELECTED

Assess one concrete truthful source for post-install package-state evidence before any implementation. Prefer target-owned explicit package-state output over generic install-log parsing. If no normal public/read-only evidence source is available, record F6 feasibility as unresolved rather than building generic log ingestion or manufacturing runtime state.

**Procedures:** `UP-SKILL:upgradepilot-learning-by-doing`; Planning/Design; canonical A→B→C→D→E.
