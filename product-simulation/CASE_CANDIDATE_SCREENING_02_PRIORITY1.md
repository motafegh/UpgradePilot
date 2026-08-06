# Case Candidate Screening 02 — Priority-1 Behavior / Targeted-Check Discovery

- **Status:** completed screening record; non-controlling
- **Date:** 2026-08-06
- **Owner:** Ali Rajabi
- **Scope:** first calibrated Priority-1 search after the 2026-08-06 product-simulation recalibration
- **Authority:** discovery evidence only
- **Admission effect:** this file records the screening result; S006 admission is owned separately by `S006_CANDIDATE_SCREENING.md`

## 1. Question screened

The calibrated Priority-1 search asked for a case with the complete chain:

```text
real upstream behavior/API change
→ exact activation condition
→ affected target path demonstrably present
→ current test/CI evidence does not already close the question
→ one narrow additional check can discriminate materially different outcomes
```

The purpose was not to find the largest or scariest dependency update. The purpose was to test whether the selection framework can distinguish direct behavior impact from dependency-graph problems, ordinary regression coverage, and cases where existing tests are already sufficient.

## 2. Screening discipline

The pass applied the mandatory admission gates from `CASE_SELECTION_FRAMEWORK_V2.md` plus these practical rules:

1. **Target-owned activation only.** Vendored dependency source does not establish target usage.
2. **Configured coverage is not executed coverage.** A workflow definition shows intended coverage; it is not historical green/red proof when exact-head runs are no longer retained.
3. **One central uncertainty per case.** If another uncertainty dominates, reclassify the candidate rather than forcing it into the behavior-impact family.
4. **Existing discriminating evidence blocks a fake coverage-gap case.** If the target already has the exact check, the case becomes a control.
5. **Negative screening is valid evidence.** Do not lower the gates merely to assign a new case number.

## 3. Candidate register

| ID | Candidate | Result | Disposition |
| --- | --- | --- | --- |
| C01 | `eduardoklosowski/qldebugger#27`, Pydantic 1.10 → 2.x | exact upstream behavior intersects exact target validator, but target already contains the exact discriminating test | real control / external-validity anchor |
| C02 | qldebugger real-derived coverage-gap variant | same real behavior and target code, with exactly one controlled variable: the discriminating test is hidden from the simulated baseline | strongest Priority-1 design candidate |
| C03 | `kubernetes-client/python#2106`, urllib3 <2 → <3 | urllib3 is core transport, but a dependency-graph/installability constraint is the more immediate uncertainty | reserve for graph/authority family |
| C04 | `cobrateam/splinter#1160`, urllib3 <2 → <3 | direct transport customization exists, but no exact removed-API trigger was established; relevant integration coverage is configured | ordinary regression/control |
| C05 | `pypa/pip-audit#620`, urllib3 <2 → <3 | proposal removes an explicit compatibility bound and therefore duplicates the graph-constraint family | corroborator/reserve |
| C06 | changed-head/supersession controlled scenario | strong lifecycle/stale-evidence value, but not the Priority-1 behavior question | later lifecycle case |

## 4. C01 — qldebugger untouched real anchor

Repository: `eduardoklosowski/qldebugger`  
PR: `#27`  
Frozen head inspected: `a454b47b8e483dffc825a3c9998f38e7634ec93b`

The PR widens Pydantic from `^1.10` to `>=1.10,<3.0`.

At the frozen head, target-owned code contains a Pydantic V1 validator:

```python
@validator('handler', pre=True)
def _split_handler(cls, v: Any) -> Tuple[str, str]:
    if not isinstance(v, str):
        raise TypeError('should be a str')
```

Pydantic V2 changed validator exception handling so `TypeError` raised inside a validator is propagated directly rather than being converted into `ValidationError`.

The target also contains the exact discriminating test: pass a non-string handler and expect `ValidationError`, including the V1-style `type_error` result.

Therefore C01 proves a real behavior intersection but **does not** prove a missing-check gap. The correct interpretation is:

```text
affected behavior found
+ exact target coverage already exists
→ do not invent a redundant targeted check
```

This makes C01 an unusually strong external-validity control.

Historical exact-head check/status retention was unavailable through the inspected public interfaces, so the screening does not claim that the old PR workflow was green or red.

## 5. C02 — qldebugger real-derived coverage-gap variant

C02 preserves the real anchor but controls one variable only:

> The exact target test that asserts non-string `handler` input becomes `ValidationError` is absent from the simulated visible baseline.

Everything else remains anchored in real evidence:

- real Dependabot proposal;
- real Pydantic behavior change;
- real target validator;
- real non-string activation condition;
- real surrounding project/test structure.

The untouched C01 test becomes **withheld evaluation truth**, not visible planning evidence.

The intended inference is:

```text
Pydantic V2 validator TypeError behavior
→ target validator deliberately raises TypeError
→ visible ordinary/happy-path evidence does not close exception-shape compatibility
→ one discriminating check is non-string ConfigLambda.handler validation
```

This is the strongest Priority-1 design because it separates discovery from memorization: the system must derive the check from upstream behavior + target activation + visible coverage, then the recommendation can be evaluated against independently preserved real repository evidence.

## 6. C03 — Kubernetes Python / urllib3

`kubernetes-client/python#2106` is highly relevant to urllib3 at runtime: the Kubernetes Python client constructs urllib3 pool/proxy managers, passes TLS/retry configuration, sends requests through urllib3, handles urllib3 SSL failures, and wraps urllib3 responses.

However, the preceding merged change had intentionally established the `<2.0` boundary for dependency compatibility/installability. The Dependabot PR immediately proposed widening that boundary.

That means the first material question is dependency-graph compatibility, not downstream API behavior.

Correct disposition: **reserve for dependency-graph / authority / conflicting-evidence work**.

## 7. C04 — Splinter / urllib3

`cobrateam/splinter#1160` contains real target-owned urllib3 transport customization and a Selenium Remote integration path. The workflow is configured to exercise Selenium Remote across multiple Python versions.

But the screening did not establish target-owned use of a concrete urllib3 2.0 removed API or an exact changed behavior predicate. Direct dependency use plus a major update is not sufficient case admission evidence.

Correct disposition: **ordinary regression/control**.

## 8. C05 — pip-audit / urllib3

`pypa/pip-audit#620` proposed widening an explicit urllib3 upper bound whose source comment documented CacheControl/requests compatibility concerns.

This strongly corroborates the dependency-graph family, but does not add a new Priority-1 behavior uncertainty.

Correct disposition: **reserve/corroborator**.

## 9. C06 — changed-head / supersession controlled scenario

Changed proposal head, stale evidence, rerun identity, and supersession remain materially useful future lifecycle questions.

They should not be mixed into the first behavior/targeted-check case because they would introduce a second central uncertainty.

Correct disposition: **later lifecycle case**.

## 10. Bounded search conclusion

The bounded untouched-real search did **not** find a public candidate that simultaneously supplied:

1. exact real upstream behavior change;
2. exact target activation;
3. insufficient target coverage;
4. a single clear discriminating check;
5. a clean enough uncertainty boundary for Priority 1.

That negative result is accepted. The gates were not weakened.

The search instead found something more useful for controlled evaluation:

```text
untouched real C01
→ proves real behavior + target activation + real repository expectation

real-derived C02
→ removes one coverage fact from the visible baseline
→ tests whether the system can derive the missing check

withheld C01 test
→ independently scores the C02 recommendation
```

This directly validates the hybrid evidence model adopted in the recalibration: untouched real cases provide external validity; real-derived variants isolate a product question without pretending the artificial condition was historical truth.

## 11. Claim boundaries

This screening supports claims about:

- case-selection discrimination;
- whether a real-derived variant can isolate targeted-check planning;
- differences among behavior impact, graph constraints, and ordinary regression controls;
- bounded negative-search findings within the inspected evidence.

It does **not** support claims about:

- population frequency of these scenarios;
- universal Pydantic or urllib3 compatibility;
- production reliability of UpgradePilot;
- correctness of any future final maintainer action;
- the artificial qldebugger coverage gap being real historical qldebugger behavior.

## 12. Result carried forward

C02 is the only candidate from this screening advanced to a separate admission review.

The admission decision, frozen identity, controlled mutation, oracle, and prospective checkpoints are owned by:

- `S006_CANDIDATE_SCREENING.md`
- `scenarios/S006-qldebugger-pydantic-validator-coverage-gap/artifacts/CASE_IDENTITY.json`
- `scenarios/S006-qldebugger-pydantic-validator-coverage-gap/artifacts/BASELINE_RESULT.json`

No target repository is mutated by this screening.