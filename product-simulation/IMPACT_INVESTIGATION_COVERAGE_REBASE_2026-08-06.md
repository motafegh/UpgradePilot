# Impact and Investigation Coverage Rebase — 2026-08-06

**Status:** Dated cross-case discovery analysis; non-controlling  
**Owner:** Ali Rajabi  
**Scope:** Re-read S001–S005 through impact, activation, applicability, investigation, uncertainty, and stopping without changing their historical records

## 1. Purpose

The original S001–S005 cycle was organized primarily around evidence-to-decision contrasts and
runtime/artifact discovery. Major product progress since then makes a second reading useful.

This analysis asks:

> What did the five historical cases actually teach us about possible dependency-update
> impacts, the conditions that activate them, the target evidence needed to establish
> applicability, the investigations that add information, and the conditions under which
> investigation should stop?

It does not replace the original syntheses. Historical actions remain historical outputs.

## 2. Common analysis frame

For each case, inspect these dimensions:

1. **change signal** — what upstream, package, CI, or dependency observation raised a concern;
2. **possible impact/problem** — what could materially go wrong or change;
3. **activation condition** — what must be true for that impact to matter;
4. **target surface** — what target configuration, source, dependency path, environment, or
   execution path can establish activation;
5. **applicability state** — present, absent, partially established, unresolved, or mediated;
6. **coverage state** — what CI/test/execution evidence covers the affected responsibility;
7. **open question** — what remained decision-relevant after current evidence;
8. **useful investigation** — what additional evidence/check discriminated between meaningful
   alternatives;
9. **low-value investigation** — what deeper work would not materially improve the bounded
   question;
10. **stopping basis** — why the case could stop or what prevented closure;
11. **reusable reasoning pattern** — the more general shape exposed by the case.

These are analysis dimensions, not a frozen runtime schema.

## 3. S001 — Soup Sieve 2.6 → 2.8.4 in Pydantic

### Historical case shape

S001 was a transitive documentation-tooling dependency update with relevant green CI,
advisory/remediation context, and upstream changes spanning several releases.

Later production work reused S001 and established a stronger exact path for one bounded
concern: Soup Sieve 2.8 dropped Python 3.8 support, while the target Pydantic revision declared
`requires-python >=3.10`; under the implemented target-Python method that support-drop concern
is outside the target's declared Python range.

### Rebased analysis

| Dimension | S001 observation |
|---|---|
| Change signal | Multi-release upstream change plus advisory/support information |
| Possible impact/problem | Runtime/language-support mismatch; historically also security/exploitability calibration and transitive-tooling relevance |
| Activation condition | Target actually supports/executes the affected Python line or otherwise activates the specific upstream concern |
| Target surface | Exact target Python declaration; documentation/dependency path; relevant CI responsibility |
| Applicability | Current implemented support-drop slice: absent from declared Python range; broader historical concerns were bounded by transitive/docs context |
| Coverage | Relevant exact-head docs CI existed historically; current product still distinguishes CI dependency exercise from global green status |
| Open question | A closed Python-support concern does not prove overall update compatibility or safety; other impact classes can remain unexamined |
| Useful investigation | Crossed-release upstream authority → exact support-drop claim → exact target Python declaration → deterministic applicability |
| Low-value investigation | Exploitability or runtime work after the bounded concern is shown not to intersect the target's declared Python line, unless a different evidence-backed question activates it |
| Stopping basis | Stop that concern when activation/applicability is deterministically absent; do not convert closure of one concern into universal safety |

### Reusable pattern

```text
upstream support/environment change
→ affected runtime condition
→ exact target support declaration/environment
→ applicability present / absent / unresolved
→ investigate only if intersection remains material
```

### Product-learning value

S001 is the strongest existing proof that an apparently important upstream change may become
non-applicable after target-specific evidence. It also demonstrates that **closing one impact
branch is not the same as deciding the entire dependency update**.

## 4. S002 — HTTPX 0.27.2 → 0.28.1 in Kubernetes Dashboard Token API

### Historical case shape

S002 involved a direct dependency declaration, adapter/framework-mediated usage, an upstream
removed/changed API surface, and CI where installation/build evidence existed but relevant
Python tests did not trigger.

The historical full result requested targeted checks because the material behavior path was
not adequately exercised by available exact-head evidence.

### Rebased analysis

| Dimension | S002 observation |
|---|---|
| Change signal | Upstream API/behavior change in HTTPX |
| Possible impact/problem | Adapter/framework compatibility or runtime call-site breakage |
| Activation condition | Target or an adapter/framework used by the target invokes the affected API/behavior |
| Target surface | Direct declaration plus framework/adapter execution path and relevant Python tests |
| Applicability | Material path appeared plausible through adapter-mediated use rather than simple direct import alone |
| Coverage | Docker install/build passed, but relevant Python tests were skipped/not triggered; global green evidence was insufficient |
| Open question | Does the exact target adapter/runtime path work against the proposed HTTPX version? |
| Useful investigation | Establish mediated usage and run or recommend a check that actually exercises the affected adapter path |
| Low-value investigation | More generic build/install checks that do not execute the changed responsibility |
| Stopping basis | Cannot close the compatibility question from unrelated green evidence; stop only after a discriminating path-specific check or honest unresolved result |

### Reusable pattern

```text
upstream API/behavior change
→ affected call/adapter condition
→ target direct or mediated usage path
→ exact execution coverage
→ targeted check if material path remains uncovered
```

### Product-learning value

S002 is the strongest historical host for **direct behavioral/API impact + incomplete target
coverage**. It is therefore a prototype for the kind of future real case that should receive
high priority after recalibration.

It also shows why direct imports are not the only relevant usage signal: adapter/framework
relationships can activate an upstream change.

## 5. S003 — TypeScript 5.9.3 → 7.0.2 in event-handler-loader

### Historical case shape

S003 was the first prospective failing case. `npm ci` failed before ESLint executed. The target
retained TypeScript-ESLint 8.65.0 whose peer declaration supported TypeScript
`>=4.8.4 <6.1.0`; the proposed TypeScript 7.0.2 was outside that range. A same-base adjacent
Dependabot PR passed installation/linting in a comparable environment.

Historical attribution was strongly supported as update-caused at the dependency-tree /
installability layer, with explicit limits because exact local reproduction was unavailable.

### Rebased analysis

| Dimension | S003 observation |
|---|---|
| Change signal | Major dependency update plus failing install execution |
| Possible impact/problem | Dependency-relationship incompatibility / installability failure |
| Activation condition | Proposed version violates a retained tool's peer/support range and the resolver enforces that relationship in the target install path |
| Target surface | `package.json`/lock/tooling relationship, `npm ci`, Node/npm environment, exact failing workflow step |
| Applicability | Strongly present: exact proposed version and retained peer range conflict on the target path |
| Coverage | Failure occurred in the owning installation step; adjacent same-base comparison reduced alternative explanations but did not eliminate all confounders |
| Open question | Exact diagnostic/local reproduction remained unavailable; causality was strong rather than absolute |
| Useful investigation | Decompose workflow to failing command; compare declared peer range; use same-base adjacent execution; evaluate competing causal hypotheses |
| Low-value investigation | Treating workflow color or unrelated passing jobs as proof of cause; suppressing peer checks without understanding compatibility |
| Stopping basis | Stop at calibrated strong attribution once remaining unavailable evidence cannot materially improve the bounded action without disproportionate or impossible acquisition |

### Reusable pattern

```text
dependency relationship constraint
→ proposed version violates activation predicate
→ target install/resolution path
→ observed failure
→ compare competing causes
→ calibrated causal attribution
```

### Product-learning value

S003 introduces a different impact family from S001/S002: the problem is not merely target
usage of a changed API but **the dependency graph/constraint system itself**.

It also demonstrates that investigation may need to answer a causal question rather than an
applicability question, and that an honest result can remain probabilistically/calibrationally
bounded when perfect reproduction is unavailable.

## 6. S004 — pytest 9.0.2 → 9.0.3 in glyphsLib

### Historical case shape

S004 was deliberately selected as a baseline-sufficient control. The changed development
requirement was actually consumed by tox; exact-head ordinary and regression pytest
responsibilities passed; official upstream material described 9.0.3 as a bug-fix/drop-in
replacement; no decision-critical contradiction remained.

The full process intentionally stopped without activating deeper conditional investigations.

### Rebased analysis

| Dimension | S004 observation |
|---|---|
| Change signal | Small pytest patch update with benign official upstream description |
| Possible impact/problem | Ordinary regression/compatibility uncertainty associated with changing a test dependency |
| Activation condition | Proposed pytest version is actually installed/executed in the target's owning test path and changes behavior relevant to that path |
| Target surface | `requirements-dev.txt`, tox install path, pytest commands, matrix runs |
| Applicability | The dependency was definitely exercised, but no specific material concern remained after authority confirmation |
| Coverage | Exact-head ordinary and regression pytest responsibilities passed across relevant matrix environments |
| Open question | None with enough information value to justify a targeted investigation |
| Useful investigation | Minimal authority confirmation: dependency consumption, exact-head execution, coherent upstream source |
| Low-value investigation | Advisory exploitability, runtime usage search, adapter analysis, local reproduction, platform/native analysis, or generic targeted checks with no named question |
| Stopping basis | All precommitted authority/sufficiency conditions passed and no remaining supported investigation could change the bounded conclusion |

### Reusable pattern

```text
coarse low-concern signal
→ confirm authority-critical assumptions
→ no material unresolved impact
→ do not activate deeper investigations
→ stop
```

### Product-learning value

S004 is the strongest evidence that **investigation selection includes declining to
investigate**. More analysis is not automatically better.

It is also a useful future control against any impact model that activates every possible
concern indiscriminately.

## 7. S005 — pytest 9.0.3 → 9.1.1 in ModelArrayIO

### Historical case shape

S005 deliberately tested a baseline action change. Literal upstream `breaking`, `removals`,
and `deprecations` language caused the transparent baseline to request targeted checks.

Deeper evidence established that the breaking behavior required `--doctest-modules` and a
specific fixture-placement condition that the target did not use; named deprecated surfaces
were absent or used in supported form; lock-backed pytest 9.1.1 matrix executions passed;
and no remaining target-specific uncertainty named a useful additional check.

### Rebased analysis

| Dimension | S005 observation |
|---|---|
| Change signal | Upstream breaking/deprecation language |
| Possible impact/problem | Behavior/configuration/API incompatibility |
| Activation condition | Target uses the exact configuration/API/pattern described by upstream |
| Target surface | pytest configuration, source/API search, lock consumption, tox runner, exact matrix cells |
| Applicability | Material breaking condition absent for the frozen target; deprecated surfaces absent or supported |
| Coverage | Exact proposed-version lock-backed pytest matrix covered relevant target tests, including downloaded-data tests in one cell |
| Open question | No remaining target-specific question with enough information value to justify another check |
| Useful investigation | Convert prose into concrete activation predicates; inspect exact target configuration/source; prove dependency identity in CI; inspect matrix coverage |
| Low-value investigation | Keyword-driven generic targeted checks after activation predicates are shown absent |
| Stopping basis | Concern closed through target non-activation plus adequate execution evidence; no unresolved question could name a discriminating check |

### Reusable pattern

```text
upstream statement/change
→ activation condition
→ target configuration/source/usage surface
→ exact execution/evidence coverage
→ unresolved question OR closure
```

### Product-learning value

S005 remains the strongest historical expression of the likely reusable middle of the
product. It demonstrates why release-note caution is a **signal** rather than a conclusion.

It also gives a concrete rule for targeted checks:

> A targeted check should answer a named unresolved target question. If no such question
> remains, adding a check is ceremony rather than evidence-seeking.

## 8. Cross-case impact families already observed

The five cases already expose several materially different problem families.

| Observed family | Primary case(s) | Core question |
|---|---|---|
| Runtime/language support boundary | S001 | Does the upstream support change intersect the target's supported environment? |
| API/behavior/framework compatibility | S002, S005 | Does the target directly or indirectly activate the changed behavior? |
| Dependency/peer/constraint installability | S003 | Does the proposed version violate a relationship enforced on the target path? |
| Evidence authority and CI responsibility coverage | S001–S005 | Did the exact proposed dependency/version actually exercise the responsibility we are using as evidence? |
| Baseline sufficiency / no material additional investigation | S004 | Is there any unresolved question with enough information value to justify deeper work? |
| Target-scoped caution/non-applicability | S001, S005 | Is a concerning upstream change actually relevant to this frozen target? |
| Causal failure attribution | S003 | Did the dependency update cause the observed failure, or is another explanation more credible? |

This table is empirical coverage, not a final taxonomy.

## 9. Cross-case reasoning patterns strengthened

### Pattern A — impact is conditional

```text
upstream change
!= target impact
```

A change becomes a target impact only through an activation/applicability relationship that is
supported by evidence.

### Pattern B — target surface can be indirect

Relevant surfaces include more than direct imports:

- declarations and constraints;
- adapters/frameworks/plugins;
- runtime/language policy;
- configuration flags;
- install/resolution paths;
- test/development tooling;
- workflow commands and matrices.

### Pattern C — CI authority is impact-specific

A green workflow is useful only if its exact execution covers the dependency identity and
responsibility relevant to the open question.

### Pattern D — targeted investigation needs discrimination

A useful investigation must be capable of separating materially different interpretations or
next steps. “Run more tests” without a named unresolved question is weak product behavior.

### Pattern E — stopping is impact/question relative

A case can stop one concern while other impact classes remain unexamined. Stopping should mean
“the bounded question no longer benefits materially from more supported work,” not “the update
is proven safe.”

### Pattern F — missing evidence has different meanings

Unavailable reproduction, skipped tests, missing CI, negative code search, absent activation
configuration, and unsupported acquisition are not interchangeable uncertainty states.

## 10. Coverage gaps after the rebase

The next cases should not be chosen merely because these gaps exist. They are areas where
current evidence is materially weaker and a strong real candidate could add value.

### High-value gaps

1. **Real runtime/API impact with demonstrated target usage and incomplete coverage**
   - S002 approximates this but external behavior remained unconfirmed.
   - Strong future case: affected API is definitely used; available CI misses or ambiguously
     covers it; one targeted check can discriminate.

2. **Repeated activation/applicability behavior across a different impact family**
   - Current strongest examples are Python support and pytest configuration/API scope.
   - Need evidence that the same reasoning shape survives a changed package/repository/domain.

3. **Targeted-check counterfactual**
   - One case where the check is clearly justified and its pass/fail outcome changes what can
     be concluded.

4. **Unresolved end state**
   - Existing final cases mostly reached a broad historical action.
   - Need a case where honest unresolved/unsupported state is itself the durable result.

### Important later gaps

5. **Temporal/yanked/supersession behavior**
   - theHarvester Requests sequence remains a strong real candidate.

6. **Changed-head / stale-evidence lifecycle**
   - Prefer real-derived or synthetic revision control first unless a well-preserved real case
     is found.

7. **Platform/native/compiler/toolchain applicability**
   - Historically named but weakly demonstrated.

8. **Supply-chain/provenance degradation**
   - Distinguish package identity/provenance failure from behavioral incompatibility.

9. **Adversarial/untrusted semantic content**
   - Particularly relevant now that bounded local semantic extraction exists; best handled as
     controlled evaluation attached to real source structure.

10. **Multiple simultaneous impact classes**
    - Useful only after single-impact reasoning is clear enough to avoid creating an
      uninterpretable mega-case.

11. **Repository-policy sensitivity**
    - The current wider design discussion is questioning how maintainer policy should affect
      final action; simulation can later provide contrasts without inventing universal policy.

## 11. Implications for future case selection

The first new full case after recalibration should ideally do more than produce a novel final
action. It should force the system/design discussion to answer a meaningful chain such as:

```text
specific upstream behavior change
→ exact activation condition
→ demonstrable target usage/configuration
→ incomplete or ambiguous existing coverage
→ one decision-relevant unresolved question
→ one discriminating investigation/check
→ clear closure or honest unresolved result
```

This would exercise a materially different impact family from the implemented Python-support
slice while remaining close enough to the emerging reasoning model to generate useful design
evidence.

## 12. What this analysis does not establish

It does not prove:

- that the listed impact families are exhaustive;
- that every future case should use the same sequence;
- that target applicability must become one production schema;
- that the current five historical action classes survive or disappear;
- that S002 is the correct next case to replay;
- that the next new case must be API-related;
- that a real case is always superior to a controlled variant;
- that any historical maintainer decision was objectively correct.

The purpose is to make existing discovery coverage visible enough that the next simulation
adds genuinely new information.
