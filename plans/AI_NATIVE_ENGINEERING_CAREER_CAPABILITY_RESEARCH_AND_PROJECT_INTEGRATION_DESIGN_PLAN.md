# AI-Native Engineering and Career Capability Research and Project-Integration Design Plan

**Status:** Branch-local research/design plan. Non-controlling for `main`.

**Research branch:** `research/ai-native-career-capability-strategy-2026-10-20`

**Initial main anchor:** `ecd11a4a424bd1b6cecc8a8c83e9e17370ab88db` (`Add FCI001 current CI diagnostic case`)

**Primary input:** [`proposals/2026-10-20_UPGRADEPILOT_AI_NATIVE_ENGINEERING_AND_CAREER_CAPABILITY_HORIZON_PROPOSAL.md`](../proposals/2026-10-20_UPGRADEPILOT_AI_NATIVE_ENGINEERING_AND_CAREER_CAPABILITY_HORIZON_PROPOSAL.md)

**Authority:** This plan authorizes research/design artifacts on this branch only. It does not change `main`, product source/tests, the Charter, accepted specifications/ADRs, live `MEMORY.md`, product action permissions, dependencies, services, infrastructure, or portfolio claims.

## 1. Responsibility

Determine, with current project evidence and career value kept distinct, **what should be added, strengthened, exposed, qualified, kept outside the runtime, deferred, or rejected** so UpgradePilot can remain a coherent product while becoming a stronger AI-native engineering and career flagship.

The branch must answer four coupled questions:

1. **Product:** Which candidate capabilities solve a real UpgradePilot product, reliability, security, evaluation, operability, or user-value responsibility?
2. **Learning/ownership:** Which capabilities materially improve Ali's ability to explain, modify, diagnose, transfer, and defend the system?
3. **Career/hiring:** Which evidence would make Ali more credible for realistic adjacent roles as well as the longer-term AI-security specialization?
4. **Integration:** Which findings, if any, should later be proposed for `main`, through which correct owner, and only after reconciliation with the then-current `main` state?

## 2. Governing principles

Use the existing project owners rather than creating a second control system.

- `PROJECT_CHARTER.md` continues to own mission, user, product boundary, evidence doctrine, technology admission, and claim limits.
- `plans/UPGRADEPILOT_90_DAY_PLAN.md` continues to own the current route until explicitly revised through its normal responsibility.
- `MEMORY.md` on `main` remains the sole owner of live main continuation.
- Accepted specifications/ADRs retain their existing authority.
- The horizon proposal remains an opportunity catalog, not a backlog.
- Active source/tests and reproducible evidence establish implemented truth.

Apply these strategy rules throughout the research:

```text
career value is legitimate
!=
career value silently becomes a product requirement

implemented sophistication
!=
Ali-owned capability

internal evidence
!=
external usefulness

framework exposure
!=
engineering capability

more agents/services/infrastructure
!=
better architecture
```

## 3. Research boundaries

### Allowed on this branch

- read-only repository analysis and cross-owner reconciliation;
- current-market/role research when it materially affects prioritization;
- branch-local research, design, comparison, learning, audit, and portfolio-strategy artifacts;
- small non-product diagnostic/prototype designs when needed to discriminate an architecture or career-proof decision;
- explicit draft recommendations for later owner changes, without editing those controlling owners merely to make the draft look accepted;
- periodic comparison with advancing `main`.

### Not authorized by this plan

- product-runtime implementation under `src/upgradepilot/`;
- product-test changes intended to admit new behavior;
- changes to accepted specifications or ADRs;
- changing `PROJECT_CHARTER.md`, `MEMORY.md`, or the controlling route merely to reflect branch research;
- new production dependencies, services, queues, databases, agents, cloud infrastructure, or deployment systems;
- product action-permission expansion;
- claims of job readiness, mastery, production readiness, or product usefulness not supported by evidence;
- merging or rebasing the branch into `main` as an automatic consequence of successful research.

If a discriminating executable experiment becomes necessary, design its exact bounded responsibility first and obtain separate authorization before creating experiment code.

## 4. Main-state coexistence rule

`main` is expected to progress in parallel. This branch must not freeze October 20 assumptions into final recommendations.

Use three state categories:

- **branch-base evidence** — facts established at the initial `ecd11a4a` anchor;
- **later-main evidence** — material changes observed on `main` while research continues;
- **final-integration evidence** — a fresh comparison against `main` immediately before any merge/adoption recommendation.

Do not continuously merge every main commit into the research branch merely for freshness. Reconcile at meaningful research milestones and always before the final integration recommendation. If later `main` already solves, invalidates, or materially changes a proposed capability, update or reject the branch recommendation rather than preserving it for sunk-cost reasons.

## 5. Research sequence

### 5.1 Establish the current capability/evidence inventory

Build an evidence-backed map of the important capability families from the horizon proposal against the actual project.

Classify each relevant capability as approximately:

```text
implemented + sufficiently proven
implemented but proof/ownership incomplete
partially present
accepted/planned elsewhere
credible natural opportunity
career/learning-only opportunity
not currently justified
conflicts with product boundary
superseded or already sufficient
```

For material rows, distinguish:

- product capability evidence;
- engineering proof;
- AI-native/agent evidence;
- Ali-owned evidence;
- external/user evidence;
- employer-facing legibility.

Do not score by file count, test count, technology count, or architectural sophistication alone.

### 5.2 Identify the highest-value gaps

Find the smallest set of gaps whose closure would materially strengthen both the real system and the career story without distorting either.

Evaluate at least these candidate families because current evidence suggests they may be high leverage, while keeping selection open:

- trustworthy evaluation and empirical method;
- AI/agent security and adversarial robustness;
- reliability/recovery/operability;
- observability and evidence-based diagnosis;
- bounded agent/tool architecture where a real responsibility justifies it;
- backend/service exposure only if a real product/operational boundary needs it;
- external maintainer/user validation;
- Ali-owned capability qualification;
- reviewer-first portfolio presentation;
- software/backend/Linux/networking fundamentals that may be better practised outside product runtime.

Explicitly test counterarguments. A capability can be valuable for hiring and still be rejected as a product addition.

### 5.3 Map each retained gap to the correct integration surface

For every retained candidate, choose among:

```text
product runtime / normal product tests
bounded experiment or evaluation
security/adversarial fixture or corpus
developer tooling / diagnostics
operations / deployment artifact
learning / ownership exercise
portfolio / case-study artifact
external collaboration / OSS activity
separate career practice outside UpgradePilot
defer / reject
```

Name the existing owner or proposed owner. Avoid creating a generic "career architecture" layer inside the product.

### 5.4 Design proof before implementation

For each serious candidate, define the evidence that would make it credible.

At minimum ask:

1. What real limitation or career-proof gap is being addressed?
2. What is the simplest credible baseline?
3. What observable result would justify keeping the capability?
4. What negative result would cause rejection/defer?
5. What does Ali need to understand, predict, modify, diagnose, or defend?
6. What external/user evidence is required, if any?
7. What maintenance, security, cost, or complexity obligation would adoption create?
8. Which stronger claims would still remain unsupported?

### 5.5 Build a prioritized strategy, not a technology checklist

The final design should normally identify a small number of **signature capability threads**, not attempt to schedule the entire horizon proposal.

A credible final prioritization should make explicit:

- near-term high-leverage threads;
- capabilities already strong enough to stop investing in for now;
- fundamentals requiring separate deliberate practice;
- external-validation/hiring work that code cannot substitute for;
- deferred advanced horizons and their re-entry triggers.

### 5.6 Final reconciliation and integration decision

Before recommending any merge or main-owner change:

1. inspect the then-current `main` head and material new work;
2. compare branch assumptions/recommendations against that state;
3. classify each branch artifact/finding as `merge/adapt`, `reference-only`, `superseded`, `defer`, or `discard`;
4. identify the correct owner for every proposed durable change;
5. preserve branch-only research evidence that should not enter main control surfaces;
6. produce a bounded integration recommendation rather than automatically merging.

No final integration decision may rely only on the October 20 branch base.

## 6. Expected research outputs

Do not pre-create every possible document. Create the smallest artifacts justified by the evidence.

By completion, the branch should make these results recoverable, whether in one document or several:

1. **Capability evidence matrix** — what UpgradePilot and Ali demonstrably have versus what remains unproven.
2. **Prioritized gap/opportunity map** — product-integrated, branch/experiment, learning-only, portfolio/external, deferred/rejected.
3. **Target-role and claim boundary** — realistic adjacent first-role evidence versus longer-term specialization evidence, without inflated titles or mastery claims.
4. **Signature demonstration strategy** — the few end-to-end demonstrations with the highest compound engineering/career value.
5. **Ali-owned qualification strategy** — how ownership evidence is generated and assessed without equating manual typing with ownership.
6. **External validation strategy** — maintainer use, OSS interaction, installation/usability, or other independent signals that internal AI review cannot establish.
7. **Final main-integration recommendation** — exact proposed owner changes/additions after fresh reconciliation with then-current `main`.

## 7. Evidence standard

Prefer, in order:

```text
current source/tests/reproducible project evidence
→ accepted repository owners and preserved experiments
→ current external role/security/engineering evidence when material
→ explicit reasoned inference with uncertainty
```

Do not infer a skill from repository sophistication. Do not infer product value from internal rigor. Do not infer market value from one job posting. Do not infer external usefulness from AI review.

For market research, use a diverse sample of relevant roles and extract responsibility/skill patterns rather than optimizing to one employer's stack.

## 8. Completion conditions

Research/design is complete enough for an integration decision when:

- the major horizon capabilities relevant to the target profile have been classified against actual evidence;
- the highest-value gaps are prioritized with explicit reasons and counterarguments;
- product-integrated work is separated from learning-only, portfolio, operations, experiment, and external-validation work;
- proposed additions have proof/rejection criteria and correct owners;
- Ali-owned evidence requirements are explicit;
- realistic near-term role families and longer-term specialization are distinguished;
- technology stuffing and architecture-for-career-signaling have been actively screened out;
- the branch has been reconciled against the then-current `main`;
- a merge/adapt/reference/defer/discard recommendation exists for branch findings;
- no branch research result is represented as implemented main behavior merely because it is well designed.

## 9. Stop line

Stop before product implementation or main integration.

The research may conclude that the best action is **not** to append a proposed capability to UpgradePilot. Rejection, external-only practice, or postponement are valid successful outcomes when evidence supports them.

UP-SKILL:upgradepilot-planning-design
UP-SKILL:upgradepilot-learning-by-doing
