# S004 — Baseline Sufficiency and Technical Stopping

**Related case:** [`../../product-simulation/scenarios/S004-glyphslib-pytest-9.0.2-to-9.0.3/`](../../product-simulation/scenarios/S004-glyphslib-pytest-9.0.2-to-9.0.3/)  
**Related synthesis:** [`../../product-simulation/S004_POST_CASE_SYNTHESIS.md`](../../product-simulation/S004_POST_CASE_SYNTHESIS.md)  
**Depth:** Operational and implementation-adjacent understanding; ownership not established

## 1. The responsibility

A decision-support system must know both:

```text
when more evidence is required
and
when more investigation should stop
```

Stopping is not laziness or omission. It is a technical decision that additional work is unlikely to change:

- the bounded action;
- material uncertainty;
- the required check;
- the user-facing explanation;
- a product-model conclusion.

## 2. What S004 tested

The transparent baseline saw:

- a patch update;
- passing overall CI;
- a direct dependency;
- no caution keyword.

It selected:

```text
merge_after_normal_review
```

The baseline could not know whether CI actually installed pytest 9.0.3 or exercised pytest-owned responsibilities.

S004 therefore asked only:

> Did exact-head CI install the changed development requirements and then pass ordinary and regression pytest responsibilities?

The answer was yes.

## 3. Why green CI was not enough by itself

A green status is a conclusion without responsibility context.

Useful authority required this chain:

```text
changed file: requirements-dev.txt
→ exact pin: pytest 9.0.3
→ tox environment installs requirements-dev.txt
→ tox command invokes python -m pytest
→ pull-request workflow runs that tox environment
→ exact-head jobs pass
```

A separate regression workflow also:

```text
checks out proposed head
→ reinstalls changed requirements
→ invokes pytest directly
→ passes
```

Only after this chain was confirmed could the baseline's green-CI assumption receive decision authority.

## 4. The rejected control teaches the same point

`tkoyama010/pyvista-wasm#340` looked simpler:

- tox patch update;
- broad green test matrix;
- jobs named as tox tests.

But the workflow installed an unpinned `tox` directly from the package index rather than consuming the changed `uv.lock` for the tox executable.

Therefore:

```text
green tox-based job
≠ proof that changed locked tox version executed
```

The candidate was rejected because it could not serve as a clean baseline-sufficiency control.

## 5. Precommitted stop conditions

S004 defined its stop rule before full evidence:

1. direct pinned development role confirmed;
2. exact-head PR workflows confirmed;
3. changed requirements installed by the owning path;
4. ordinary and regression pytest checks passed;
5. official drop-in bug-fix status confirmed;
6. no contradictory or missing decision-critical evidence.

Precommitment matters because it reduces hindsight expansion. Without it, an investigator can always invent another question after each answer.

## 6. Conditional-stage non-activation

S004 did not activate:

- failure attribution;
- adapter analysis;
- dynamic reproduction;
- targeted checks;
- exploitability analysis;
- platform analysis;
- private evidence acquisition.

This was not incomplete work. None of those stages had an unresolved question to answer.

A conditional stage should activate only when:

```text
current evidence exposes a material question
+
the stage can discriminate among decision-relevant alternatives
```

## 7. Why the CVE keyword did not require exploitability analysis

The release notes included CVE language. Literal keyword presence was visible to the baseline as a favorable signal.

But S004 did not need target exploitability analysis because:

- pytest was a development/test dependency;
- upstream described the patch as a drop-in replacement;
- exact relevant target tests passed;
- no decision depended on whether glyphsLib was exploitable through the fixed pytest behavior.

Security vocabulary does not automatically activate a security investigation. The target decision question controls relevance.

## 8. Baseline sufficient does not mean baseline infallible

S004 produced:

```text
baseline_sufficient
full_investigation_added_no_material_value
```

This means the full process added only a narrow authority confirmation. It did not change action, required checks, or material uncertainty.

It does not mean:

- every patch update is simple;
- green CI is globally authoritative;
- release notes are always trustworthy;
- no repository context is needed;
- the update is objectively safe.

## 9. Cost model at the covered depth

S004 used:

- four initial freeze/baseline operations;
- four full-confirmation operations;
- six bounded evidence groups;
- seven evidence records;
- zero dynamic executions;
- zero additional targeted checks;
- zero activated diagnostic artifacts.

These are descriptive burden proxies, not a universal budget.

The reusable principle is:

> Buy only enough additional evidence to validate or reject the baseline's authority-critical assumptions.

## 10. Product implication

A future runtime may need a stage gate like:

```text
baseline result
→ identify authority-critical assumptions
→ perform minimum confirmation
→ evaluate stop conditions
→ either stop or activate a conditional stage
```

The exact production representation is not selected. `STOPPING_EVALUATION.json` is currently a conditional simulation artifact, not a mandatory future schema.

## 11. Ownership exercises

### Exercise A — Explain the candidate rejection

Explain why the green `pyvista-wasm` tox jobs were insufficient evidence for the changed locked tox version.

Required distinction:

```text
command uses package name
versus
command executes proposed package identity
```

### Exercise B — Trace authority

Starting from the S004 human-report statement that ordinary tests passed with the proposed pytest version, trace backward through:

```text
human report
→ decision reason
→ finding
→ interpretation
→ evidence
→ raw workflow and tox source
→ frozen head
```

### Exercise C — Challenge the stop

Name one concrete new fact that would reopen S004 and explain which outcome might change.

Examples include:

- changed head;
- relevant test failure;
- workflow no longer installing `requirements-dev.txt`;
- upstream withdrawal or contradiction;
- new incompatible plugin constraint.

### Exercise D — Avoid false certainty

State why `merge_after_normal_review` is justified while “pytest 9.0.3 is safe for glyphsLib” remains unjustified.

## 12. Deferred depth

Not covered here:

- quantitative optimal-stopping algorithms;
- statistical value-of-information estimation;
- organization-specific risk tolerances;
- automated semantic relevance of arbitrary upstream changes;
- universal CI responsibility inference;
- production persistence or stage orchestration.

Those enter only when the implementation or evaluation responsibility requires them.
