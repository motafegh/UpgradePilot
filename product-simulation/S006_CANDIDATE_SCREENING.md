# S006 Candidate Screening — Targeted-Check Coverage Gap

**Status:** Selected and admitted for separately authorized future simulation; execution not started  
**Date:** 2026-08-06  
**Owner:** Ali Rajabi  
**Case ID:** S006  
**Case form:** real-derived controlled variant  
**Target anchor:** `eduardoklosowski/qldebugger#27`  
**Purpose:** Isolate whether UpgradePilot can identify an upstream behavior change that activates on exact target code, recognize that the simulated visible test evidence does not directly cover that behavior, and recommend the narrowest useful targeted check without overclaiming a final maintainer action.

## 1. Authority and live-state boundary

Ali explicitly authorized continuation of the S006 admission review on 2026-08-06 after the bounded candidate-screening pilot identified the qldebugger real-derived coverage-gap design as the strongest Priority-1 candidate.

This file is a **simulation admission and prospective execution record** only.

It does **not**:

- change the live project route or immediate continuation;
- replace or update `../MEMORY.md`;
- modify the active whole-product decision-model reconciliation;
- approve a new product architecture or decision contract;
- change source code or active product tests;
- mutate the public target repository;
- treat historical simulation action labels as current product truth;
- prove production readiness, representative frequency, or general targeted-check reliability.

The S006 branch was created from UpgradePilot `main` commit:

`5ef46e4352814528080cc179d91b58c1e54b45c8`

The earlier broad screening and hybrid-case proposal remain separately preserved on branch `agent/product-simulation-case-program-proposal`. S006 does not require that old proposal branch to be merged.

## 2. Exact unresolved question

S006 owns one central uncertainty:

> When authoritative upstream behavior changes intersect exact target-owned code, but the simulation-visible target test evidence lacks the exact discriminating assertion, can UpgradePilot identify the remaining coverage gap and recommend a narrowly targeted check that can distinguish materially different outcomes?

This is a **check-selection** question.

It is not primarily a question about:

- whether Pydantic V2 is globally safe;
- whether the real historical qldebugger PR should have been merged;
- whether every Pydantic V1-to-V2 update needs this check;
- dependency-graph conflicts;
- changed-head lifecycle;
- final maintainer action vocabulary;
- general CI sufficiency.

## 3. Why S001–S005 do not already answer it

The accepted S001–S005 cycle established that required checks, target relevance, CI authority, activation conditions, stopping, and action changes can matter.

However, the prior cases do not isolate **targeted-check selection quality** as the central variable:

- S001 strengthened authority around a transitive/advisory case;
- S002 identified adapter-mediated risk and missing relevant test coverage, but did not isolate whether a planner can derive one exact discriminating check from an upstream behavior/target-code intersection;
- S003 centered on failing-install causal attribution;
- S004 centered on baseline sufficiency and stopping;
- S005 centered on evidence overturning an over-cautious baseline action.

The current whole-product reconciliation separately identifies **Best next investigation/check** as an unresolved product-model conversation. S006 is therefore admitted as discovery/evaluation evidence for that question, not as extra case count.

## 4. Real anchor identity

The untouched real anchor is:

- repository: `eduardoklosowski/qldebugger`;
- repository visibility: public;
- PR: `#27`;
- PR title: `Update pydantic requirement from ^1.10 to >=1.10,<3.0`;
- PR state: closed, not merged;
- base branch: `main`;
- frozen base SHA: `b9e24267507d29c364d32e60f2bdc6075d91c395`;
- frozen head branch: `dependabot/pip/pydantic-gte-1.10-and-lt-3.0`;
- frozen head SHA: `a454b47b8e483dffc825a3c9998f38e7634ec93b`;
- changed file: `pyproject.toml`;
- dependency: `pydantic`;
- old requirement: `^1.10`;
- proposed requirement: `>=1.10,<3.0`;
- dependency role in the PR body: direct production dependency.

The exact PR mutation is:

```diff
-pydantic = "^1.10"
+pydantic = ">=1.10,<3.0"
```

The real PR history is context only. Historical closure or non-merge is **not** treated as correctness proof or as the expected S006 decision.

## 5. Authoritative upstream behavior anchor

Pydantic V2 documents a behavior change relevant to validators:

- raising `TypeError` inside a validator no longer produces a Pydantic `ValidationError`;
- the `TypeError` is raised directly instead.

This behavior is independently documented by Pydantic's V2 migration material and is also surfaced in the Dependabot PR's upstream release information.

S006 treats that rule as the upstream behavior signal to be mapped to the target.

The case does not ask an LLM or UpgradePilot to invent this behavior from nothing. Upstream authority must remain separately attributable.

## 6. Exact target activation surface

At frozen head `a454b47b8e483dffc825a3c9998f38e7634ec93b`, target-owned code contains:

```python
class ConfigLambda(BaseModel):
    handler: NameHandlerTuple
    environment: Dict[str, str] = Field(default_factory=dict)

    @validator('handler', pre=True)
    def _split_handler(cls, v: Any) -> Tuple[str, str]:
        if not isinstance(v, str):
            raise TypeError('should be a str')
        if '.' not in v:
            raise ValueError('should have a module and function names')
        module, function = v.rsplit('.', maxsplit=1)
        return module, function
```

This establishes a concrete activation chain:

```text
Pydantic V2 TypeError propagation change
→ target uses a Pydantic validator
→ target validator deliberately raises TypeError for non-string handler input
→ externally observable exception behavior may change under the proposed dependency range
```

This is target-owned source. Vendored library code does not count as the activation surface.

## 7. Untouched real coverage and withheld oracle

The untouched real repository also contains an exact test for the activated behavior:

```python
def test_hander_should_raise_erro_on_receive_non_str(self) -> None:
    handler_name = randint(0, 99)

    args = self.DEFAULT_ARGS.copy()
    args['handler'] = handler_name
    with pytest.raises(ValidationError) as exc_info:
        ConfigLambda(**args)

    assert {
        'type': 'type_error',
        'loc': ('handler',),
        'msg': 'should be a str',
    } in exc_info.value.errors()
```

That real test is crucial for S006 because it provides **independent withheld evaluation truth**:

- the repository expected non-string `handler` input to surface through `ValidationError`;
- the target code deliberately raises `TypeError` inside the validator;
- Pydantic V2 changes how such `TypeError` propagates.

The untouched real case therefore already has unusually strong coverage. It is **not** itself the S006 uncertainty.

## 8. The one controlled mutation

S006 changes exactly one evidence variable:

> The test `test_hander_should_raise_erro_on_receive_non_str` is withheld from the simulation-visible baseline and coverage evidence.

Everything else used by the scenario remains anchored to the frozen real repository state unless a later checkpoint explicitly records another unavoidable acquisition limitation.

The controlled variant must not silently change:

- target source behavior;
- dependency declaration;
- PR identity;
- base/head identity;
- unrelated tests;
- workflow configuration;
- upstream Pydantic behavior evidence;
- repository policy;
- historical PR outcome.

The public target repository itself must **not** be edited. The mutation exists only inside UpgradePilot's controlled simulation evidence/fixture boundary.

## 9. Case pedigree

```yaml
case_origin: real_derived
evidence_origin: mutated_real
evaluation_role: contract_validation
real_anchor:
  repository: eduardoklosowski/qldebugger
  pull_request: 27
  head_sha: a454b47b8e483dffc825a3c9998f38e7634ec93b
controlled_variable:
  kind: withheld_test_coverage
  path: tests/qldebugger/config/test_file_parser.py
  test: test_hander_should_raise_erro_on_receive_non_str
```

The real anchor and the controlled mutation must remain distinguishable in every later case report.

## 10. Independent oracle

The S006 oracle is frozen **before** any UpgradePilot behavior is evaluated.

It has three independent legs:

1. **Upstream authority:** Pydantic V2 documents direct propagation of validator `TypeError` rather than conversion to `ValidationError`.
2. **Target activation:** the exact frozen qldebugger source raises `TypeError` inside a Pydantic validator for non-string handler input.
3. **Withheld target contract evidence:** the untouched real target test expects that non-string handler behavior to produce `ValidationError` with the repository's asserted error structure.

The oracle therefore does not depend on UpgradePilot first proposing the check and then grading itself against a newly invented expectation.

## 11. What the targeted check should discriminate

The minimum useful check must exercise the exact activated boundary, not merely rerun a large generic suite.

Conceptually:

```text
construct ConfigLambda with a non-string handler
→ observe/assert the exception contract
→ distinguish:
   repository-expected ValidationError behavior
   versus
   direct TypeError propagation under the proposed Pydantic behavior
```

A strong S006 result should be able to explain **why this check** is more discriminating than an unrelated or broad test command.

The case does not require UpgradePilot to prescribe the final code fix. Potential fixes belong to the target maintainer and are outside S006 unless separately authorized.

## 12. Admission-gate result

| Mandatory gate | Result | Reason |
| --- | --- | --- |
| Named uncertainty | PASS | exact check-selection question is isolated |
| Existing-case gap | PASS | S001–S005 do not isolate derivation of one discriminating check from upstream behavior + target activation + missing exact coverage |
| Product consequence | PASS | directly informs the current whole-product question of best next investigation/check |
| Safe boundary | PASS | public read-only anchor; controlled mutation occurs only inside UpgradePilot simulation evidence |
| Evidence feasibility | PASS | immutable PR/base/head identity, exact source, exact real test, and authoritative upstream behavior are available |
| Honest negative-result value | PASS | failure to identify the gap, broad/non-discriminating recommendations, or justified stopping would all be informative |
| Stop condition | PASS | stop after coverage classification and one supported discriminating-check conclusion, or after proving no supported check can materially discriminate |
| Claim boundary | PASS | controlled-case behavior only; no prevalence, production-readiness, or universal planner claim |
| Correct case form | PASS | real-derived one-variable mutation is less artificial than a fully synthetic repository |
| Synthetic realism basis | PASS | mutation is anchored to an untouched real PR and a withheld real target test |

The earlier screening matrix gave this design an indicative comparative score of **71**. That score supports prioritization but does not override these gates.

## 13. Prospective execution checkpoints

S006 must preserve prospective execution. Do not write the final finding first and retrofit evidence later.

### Checkpoint S006-0 — admission and identity freeze

Freeze:

- target repository and PR;
- base/head SHAs;
- changed file and dependency mutation;
- target source path;
- withheld test identity;
- upstream behavior source;
- one-variable mutation rule;
- claim limits and stop condition.

This file completes S006-0.

### Checkpoint S006-1 — restricted transparent baseline

Before exposing full target/upstream semantic evidence to the full investigation, freeze the historical transparent-baseline comparator using only its permitted input families.

The baseline remains a comparator. Its historical action label is not current product truth and must not force S006's final product-model interpretation.

### Checkpoint S006-2 — upstream impact evidence

Establish the Pydantic behavior change with source authority and exact dependency/version applicability.

Output should identify the behavior and its activation condition without yet claiming target relevance.

### Checkpoint S006-3 — target activation mapping

Map the upstream activation condition to the exact frozen target-owned validator.

Expected shape:

```text
upstream behavior
→ activation condition
→ exact target surface
→ present / absent / uncertain
```

### Checkpoint S006-4 — visible coverage evaluation

Evaluate the **simulation-visible** test/CI evidence with the withheld test excluded.

The result must distinguish:

- direct coverage proven;
- indirect coverage only;
- coverage absent;
- coverage unresolved;
- acquisition/evidence unavailable.

Do not reveal the withheld oracle during this checkpoint.

### Checkpoint S006-5 — best-next-check selection

If the activated behavior remains materially unresolved, determine whether one additional check can discriminate between materially different outcomes.

A successful recommendation should be traceable to:

```text
unresolved behavior question
→ exact target surface
→ missing coverage
→ discriminating input/observation
→ expected information gained
```

Broad test commands are not automatically wrong, but they must not be preferred when a narrower supported check provides the relevant discrimination at lower cost.

### Checkpoint S006-6 — oracle reveal and evaluation

Only after the recommendation is frozen, reveal the untouched real target test as withheld oracle evidence.

Compare:

- did UpgradePilot identify the same behavior boundary?
- did it recommend a check that exercises the same material condition?
- was the recommendation narrower, equivalent, broader, irrelevant, or missing?
- did it overstate what the check could prove?

### Checkpoint S006-7 — stopping and synthesis

Stop when the case has enough evidence to conclude whether the check-selection reasoning was useful at this bounded depth.

Do not extend S006 into unrelated Pydantic migration analysis merely because additional breaking changes exist.

## 14. Success, partial success, and failure

### Strong success

S006 is strongly successful if UpgradePilot:

1. grounds the upstream TypeError behavior change;
2. maps it to the exact target validator;
3. correctly recognizes that the simulation-visible evidence does not directly close the behavior question;
4. identifies a narrow check around non-string `ConfigLambda.handler` behavior;
5. explains what outcomes the check discriminates;
6. preserves uncertainty and avoids claiming global Pydantic compatibility or merge safety;
7. stops after the central question is resolved.

### Partial success

Examples:

- correct behavior and target mapping, but check recommendation is broader than necessary;
- correct coverage-gap recognition but weak explanation of information value;
- useful check but incomplete claim limits;
- justified abstention because an evidence dependency is unavailable.

### Material failure

Examples:

- missing the exact target activation despite available source evidence;
- claiming the existing visible suite covers the behavior without evidence;
- recommending unrelated checks;
- recommending only generic full-suite execution when the exact discriminating boundary is already known and executable;
- inventing target intent not supported by the real anchor;
- revealing/using the withheld oracle before the recommendation checkpoint;
- treating a passing targeted check as proof of global compatibility or merge safety.

## 15. Honest negative-result value

S006 remains valuable if the preferred planner hypothesis does not work.

Useful negative findings include:

- target-code mapping is too ambiguous to justify a precise check;
- static evidence cannot establish whether the target contract matters externally;
- a broad existing check is in fact the cheapest reliable discriminator;
- the proposed targeted check cannot be expressed safely or reproducibly;
- the current product model needs a richer representation of behavior questions before check planning is useful;
- the controlled mutation is too artificial and should be rejected after execution evidence.

No preferred success classification is required.

## 16. Stop condition

Stop S006 when one of these becomes true:

1. the unresolved activated behavior has been closed by sufficient visible evidence;
2. one bounded additional check has been selected and its discriminating value can be evaluated against the withheld oracle;
3. no supported additional check can materially discriminate the remaining uncertainty;
4. evidence required to preserve the case's claim boundary is unavailable;
5. continuing would broaden the case into general Pydantic migration or full maintainer-decision analysis.

A stop may be a positive, negative, unresolved, or abstaining result.

## 17. Allowed claims

S006 may support claims such as:

- a controlled real-derived scenario can represent a missing exact-coverage condition;
- an upstream behavior change can be mapped to a concrete target-owned source path;
- a particular targeted check was or was not derived from that evidence;
- the proposed check was more or less discriminating than alternatives considered;
- the method respected or violated the defined uncertainty/claim boundary.

## 18. Claims S006 cannot establish

S006 alone cannot establish:

- how frequently this scenario occurs in real repositories;
- that UpgradePilot can always generate useful targeted checks;
- that model-assisted check planning is reliable in production;
- that qldebugger should have merged or rejected PR #27;
- that Pydantic V2 is compatible or incompatible with the repository as a whole;
- that one passing check proves the update safe;
- that a final maintainer action should be automated;
- representative corpus performance;
- production readiness;
- Ali-owned mastery or capability.

## 19. External safety boundary

All target-repository work remains read-only unless Ali later gives exact authorization for a specific external mutation.

Do not:

- comment on the qldebugger PR;
- reopen or close the PR;
- rerun target CI;
- push target branches;
- file target issues;
- modify target repository content;
- use ambient credentials beyond the minimum read access needed for public evidence.

Any executable controlled variant must live inside UpgradePilot's own simulation/evaluation boundary.

## 20. Admission decision

**S006 is admitted.**

The selected form is:

> **Real-derived qldebugger/Pydantic validator coverage-gap case with one withheld real test as the controlled variable and independent oracle.**

The case owns only the bounded check-selection uncertainty defined above.

Execution may proceed prospectively on this branch through Checkpoint S006-1. Product implementation, active product-contract changes, governance realignment, synthesis changes, and `MEMORY.md` changes are not authorized by this admission.
