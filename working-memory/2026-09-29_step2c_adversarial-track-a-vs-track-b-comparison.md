# Step 2C — Adversarial Track-A vs Track-B Comparison and Reconciliation

**Recorded:** 2026-09-29  
**Branch:** \`analysis/ai-agentic-capability-map-2026-09-28\`  
**Status:** COMPLETE initial comparison  
**Live-main snapshot checked:** \`b16c984daa8f5e78ebe83856c5b010c137a405ee\`  
**Live product state at comparison:** Increment 3 CLOSED; Product verification #14 GREEN; Increment 4 selected but A0 not yet started.  
**Track A:** current/project-conditioned UpgradePilot architecture, accepted specs/ADRs, implemented source, bounded AI/agent experiments.  
**Track B:** independent/de-anchored research, Tier-1 Reports 01–07, refreshed Step 2B-X architecture set.

This record is an adversarial comparison. It does not itself alter accepted specifications, ADRs, product plans, \`MEMORY.md\`, or \`main\`.

---

## 1. Executive conclusion

The independent research does **not** expose a reason to discard UpgradePilot's current core evidence architecture.

Instead it produces a more precise result:

> **UpgradePilot's core epistemic/trust doctrine is strongly independently supported; the main weaknesses are breadth, extensibility, repository intelligence, optional runtime observation, model-context policy, interoperability, and evaluation maturity.**

The current architecture is strongest where it insists on:

- exact identity;
- evidence provenance;
- declaration ≠ execution;
- broader success ≠ exact inner-command success;
- missing evidence ≠ negative evidence;
- candidate ≠ applicability ≠ overall action;
- package-state proof ≠ later use/compatibility;
- explicit unresolved/conflicted states;
- deterministic admission/promotion;
- fixed/simple methods before agentic complexity.

The external research mainly challenges assumptions that could become overly restrictive if treated as permanent:

- only narrow typed model projections;
- only handcrafted workflow/data-flow logic;
- only changelog/release prose as upstream semantic evidence;
- binary model authority rather than empirically graded admission;
- typed records without reusable repository/graph views;
- static inference without optional runtime telemetry;
- custom evidence schemas without standards interoperability;
- machine-centric evaluation without protected corpora and maintainer decision-quality metrics.

No accepted Increment-3 proof boundary is contradicted.

Increment 4's selected composer remains technically coherent and independently supported.

---

## 2. Disposition vocabulary

Each current principle/design choice is classified as:

- **INDEPENDENTLY SUPPORTED**
- **SUPPORTED BUT TOO RESTRICTIVE**
- **SUPPORTED BUT TOO PERMISSIVE**
- **SUPPORTED BUT INCOMPLETE**
- **PROJECT-SPECIFIC CHOICE**
- **HISTORICAL / NO LONGER JUSTIFIED**
- **CONTRADICTED BY STRONGER APPROACH**
- **UNCERTAIN — EXPERIMENT REQUIRED**

Where a principle and its current implementation boundary differ, both are classified separately.

---

# 3. Core trust / evidence doctrine

| Current UpgradePilot principle | Track-B challenge / evidence | Disposition | Consequence |
| --- | --- | --- | --- |
| Exact repository/revision/source/environment identity precedes semantic use | External provenance, SCA, attestation, dependency-submission, graph systems all depend on stable identity/context | **INDEPENDENTLY SUPPORTED** | Preserve as foundational |
| Evidence from different scopes must not be silently combined | Runtime/provenance/reachability tools expose scope-specific limits | **INDEPENDENTLY SUPPORTED** | Preserve |
| Static declaration/configuration is not runtime execution | actionlint/CodeQL/static-vs-runtime research strongly supports this separation | **INDEPENDENTLY SUPPORTED** | Preserve |
| Successful workflow/job/step does not imply every inner command executed | CodeQL CFG semantics and runtime telemetry reinforce this | **INDEPENDENTLY SUPPORTED** | Preserve |
| Successful execution does not automatically equal valid evidence for a proposition | Runtime telemetry, tests, SWE-bench oracle research independently support this distinction | **INDEPENDENTLY SUPPORTED** | Preserve |
| Missing evidence is not negative evidence | Snyk \`NO PATH FOUND != unreachable\`, Socket reachability states, SPDX/CycloneDX completeness semantics strongly support this | **INDEPENDENTLY SUPPORTED** | Preserve |
| \`unresolved\` / \`conflicted\` are legitimate final technical states | Commercial reachability products + selective prediction + benchmark research support abstention/uncertainty | **INDEPENDENTLY SUPPORTED** | Preserve and eventually evaluate explicitly |
| Completeness is itself an evidence claim | Graph/reachability/SBOM research strongly supports explicit coverage semantics | **INDEPENDENTLY SUPPORTED** | Preserve |
| Candidate discovery, candidate applicability, evidence sufficiency, and final action are distinct | External systems often separate discovery, reachability, remediation, policy and human decision | **INDEPENDENTLY SUPPORTED** | Preserve |
| A model-generated candidate cannot self-authorize applicability/completeness/action | Hybrid systems ground/validate model output; human/verification layers remain separate | **INDEPENDENTLY SUPPORTED** | Preserve self-authorization prohibition |
| Trusted-state promotion requires an admitted validation path | External agent/sandbox/analysis systems support separation of proposal from authority | **INDEPENDENTLY SUPPORTED** | Preserve |

### Track-C judgment

The core decision-model specification survives the external challenge unusually well.

The external research generally arrives at the same epistemic distinctions through different domains:

\`\`\`text
observation
!= inference
!= completeness
!= decision authority
\`\`\`

No core trust principle should be reopened merely because newer AI/graph tooling exists.

---

# 4. Runtime dependency-state architecture after Increment 3

## 4.1 Exact-command execution as a separate proof layer

Current:

\`\`\`text
static/runtime step correlation
+
admitted shell/execution profile
+
exact parsed command identity
→ exact-command execution evidence
\`\`\`

External challenge:

- workflow CFG/dataflow can sometimes establish more paths statically;
- runtime telemetry can sometimes observe actual process execution directly.

**Disposition: INDEPENDENTLY SUPPORTED**, with **implementation breadth incomplete**.

The proposition boundary is correct.

The current supported syntax/path family is intentionally bounded and may expand through better producers later.

## 4.2 Package-manager semantics remain dependency-owned

Current:

\`\`\`text
workflow/provider/shell
→ environment/executable evidence

dependency/package-manager layer
→ pip/uv precedence and meaning
\`\`\`

External challenge:

mature tools generally separate generic workflow/runtime structure from ecosystem/package-manager semantics.

**Disposition: INDEPENDENTLY SUPPORTED.**

This ownership split should remain.

## 4.3 Parse one package-manager operation once

Current:

\`\`\`text
parser-neutral command occurrence
→ PackageManagerOperationDeclaration
→ independent semantic resolvers
\`\`\`

External challenge:

mature compilers/analyzers similarly favor one structural representation consumed by multiple analyses.

**Disposition: INDEPENDENTLY SUPPORTED.**

## 4.4 Independent semantic facts + precedence

Current first-family semantic facts are separate dimensions with:

\`\`\`text
CLI
> exact process environment
> persistent config
> manager default
\`\`\`

and unresolved higher-precedence evidence blocks lower fallback.

External challenge:

environment/package-manager tools and supply-chain analyzers repeatedly expose the cost of incomplete environment knowledge; no external evidence supports inventing defaults through unknown state.

**Disposition: INDEPENDENTLY SUPPORTED.**

## 4.5 Demand-driven environment/config evidence

Current principle:

> inspect only the evidence source needed to settle the requested semantic dimension rather than reconstructing the entire runner environment.

External challenge:

external systems strongly support bounded/query-driven analysis, but CodeQL/runtime telemetry may make some broader reusable context cheaper than repeated bespoke producers.

**Disposition: INDEPENDENTLY SUPPORTED as a principle; implementation strategy remains open.**

Meaning:

- do not build a universal ambient-state simulator;
- but a reusable workflow-dataflow/runtime evidence backend may be better than many one-off adapters.

## 4.6 Current conditional/loop/background exact-command exclusions

Current implementation leaves many shell/control-flow shapes unresolved.

External evidence:

- CodeQL Actions provides richer workflow CFG/dataflow;
- runtime process telemetry may establish actual execution without statically proving every path;
- symbolic execution can help only on bounded pure conditions.

**Disposition: SUPPORTED BUT TOO RESTRICTIVE if treated as a mature permanent boundary.**

As a current verified implementation boundary it is valid.

Do not reopen Increment 3.

Before substantially expanding bespoke control-flow support, run the CodeQL/runtime comparator.

## 4.7 Command-derived package state separated from CI coverage

Current ADR:

\`\`\`text
CI exercise/coverage evidence
!=
RequirementSatisfiedAtCommandCompletion
\`\`\`

External evidence:

security/reachability/remediation platforms distinguish dependency presence, reachability, runtime use and impact.

**Disposition: INDEPENDENTLY SUPPORTED.**

## 4.8 Command-completion package state separated from later use / compatibility / action

Current Increment-4 target establishes only a bounded package-state witness.

External evidence strongly separates:

- resolved/installed dependency state;
- code reachability;
- behavioral compatibility;
- test coverage;
- remediation;
- policy/action.

**Disposition: INDEPENDENTLY SUPPORTED.**

### Increment-4 conclusion

Track C finds **no architectural contradiction requiring Increment 4 to be replanned before A0**.

The composer remains justified.

One A0 check is recommended:

> ensure the new witness preserves enough provenance/type information that future directly observed runtime-state evidence can coexist without being conflated with command-derived inference.

ADR-0010 already anticipates this, so this is a verification point rather than a requested redesign.

---

# 5. Static workflow analysis and runtime observation

## 5.1 Bespoke workflow semantics as the only future route

Track A/current implementation has built bounded GitHub Actions/workflow semantics internally.

Track B found mature external alternatives, especially CodeQL Actions.

**Disposition: UNCERTAIN — EXPERIMENT REQUIRED.**

The question is not whether current code is valid.

The question is:

> before adding materially broader workflow CFG/dataflow/matrix/reusable-workflow/environment propagation, should UpgradePilot import/query CodeQL instead?

### Required experiment

Use one real environment-propagation + conditional package-manager case.

Compare:

1. current UpgradePilot analysis;
2. custom CodeQL Actions query;
3. actionlint/zizmor where relevant;
4. actual GitHub runtime evidence.

Measure:

- proposition coverage;
- precision;
- implementation complexity;
- mapping/provenance cost;
- runtime/setup cost.

## 5.2 Static inference as primary route to execution truth

Track B found optional process/network/file telemetry can turn some inference into direct observation.

**Disposition: SUPPORTED BUT INCOMPLETE.**

Static inference remains necessary because telemetry may be unavailable historically.

But runtime observation should be treated as a first-class optional producer, not merely an exotic fallback.

## 5.3 \`act\` / emulated execution as proof

Current architecture does not rely on local emulation as historical authority.

**Disposition: INDEPENDENTLY SUPPORTED.**

Keep:

\`\`\`text
emulated execution
!= historical GitHub runtime observation
\`\`\`

---

# 6. Repository intelligence and graph architecture

## 6.1 Current typed records without a persistent repository graph

Current UpgradePilot relies primarily on typed evidence/results and mechanism-specific composition.

External evidence shows strong value from:

- code graphs;
- build/test graphs;
- workflow CFGs;
- dependency/supply-chain graphs;
- queryable repository indexes.

**Disposition: SUPPORTED BUT INCOMPLETE.**

Typed records remain correct for domain authority.

But they may not be enough as the mature **repository-intelligence substrate**.

## 6.2 One universal evidence graph

Current UpgradePilot does not currently require one.

External research weakened the universal-graph idea.

**Disposition: INDEPENDENTLY SUPPORTED rejection of a premature universal graph.**

The stronger alternative is:

\`\`\`text
stable identities
+
multiple bounded views
+
evidence-backed cross-links
\`\`\`

## 6.3 Multi-view repository-intelligence service

Not currently a product component.

Track B suggests possible views:

- code structure;
- build/test;
- workflow;
- dependency;
- supply-chain;
- decision evidence.

**Disposition: UNCERTAIN — EXPERIMENT REQUIRED.**

Do not build infrastructure first.

Run one bounded RIG/repository-graph experiment before accepting this as product architecture.

---

# 7. Upstream evidence and impact discovery

## 7.1 Changelog / release prose as the main semantic source

Current implemented support-drop vertical slice uses tagged changelog/release text with a bounded LLM extractor.

External evidence shows:

- Endor/Semgrep compare old/new dependency code;
- Griffe can produce deterministic Python API-diff facts;
- DepRepair benefits from distilled migration evidence.

**Disposition: SUPPORTED BUT INCOMPLETE.**

Changelog evidence is valuable, but should not become the mature exclusive upstream source.

### Experiment

For a Python update corpus compare:

\`\`\`text
release/changelog only
vs
Griffe/API diff only
vs
combined evidence
\`\`\`

Measure impact-candidate recall, false candidates and source-grounding quality.

## 7.2 Broad impact candidate discovery as hybrid

Current mature horizon already expects hybrid discovery.

External research independently supports:

- deterministic structured signals;
- static/source/API diff;
- repository structure;
- semantic reasoning;
- runtime evidence.

**Disposition: INDEPENDENTLY SUPPORTED.**

## 7.3 Package behavior-delta mechanisms

Current mature mechanism horizon does not emphasize package behavior changes such as:

- install scripts;
- new network/shell/filesystem access;
- native-code introduction;
- telemetry behavior.

Socket shows this can be decision-relevant.

**Disposition: SUPPORTED BUT INCOMPLETE.**

This should enter future candidate-discovery taxonomy/research, but it does not block runtime-state work.

---

# 8. Model-context and AI authority

## 8.1 Bounded semantic extraction with deterministic source recovery

Current support-drop extractor:

\`\`\`text
trusted bounded source window
→ model chooses semantic candidate + source line ID
→ deterministic exact source recovery/validation
→ candidate result
\`\`\`

External evidence strongly supports structured/distilled evidence before model reasoning.

**Disposition: INDEPENDENTLY SUPPORTED.**

This remains a strong pattern.

## 8.2 Permanent “models only see narrow typed projections” rule

Current experiments are intentionally narrow.

Track B found that open-ended repository discovery often benefits from:

- graph navigation;
- structural search;
- exact raw-source retrieval;
- progressively expanded context.

**Disposition: SUPPORTED BUT TOO RESTRICTIVE if treated as a permanent mature rule.**

Better mature distinction:

\`\`\`text
model-visible context
!= trusted-state authority
\`\`\`

A model may inspect raw source for discovery while still being unable to self-promote claims.

## 8.3 Deterministic code must own every trusted semantic proposition

Current experiments are very conservative.

External selective-prediction/verification systems suggest a possible alternative:

\`\`\`text
model-derived claim
+ fixed producer/config identity
+ source grounding
+ empirical selective-risk threshold
+ independent validation where available
→ admitted claim class
\`\`\`

**Disposition: SUPPORTED BUT TOO RESTRICTIVE as a universal mature rule.**

However:

- deterministic **admission policy** remains strongly supported;
- the model must never self-authorize;
- no change should be made without protected evaluation.

### Experiment

Protected semantic corpus:

- deterministic/validated baseline;
- model outputs;
- risk-coverage curves;
- OOD cases;
- source-grounding failures.

Until that evidence exists, current conservative authority remains appropriate.

---

# 9. Agent architecture

## 9.1 Fixed pipeline before adaptive agent

Current project repeatedly prefers deterministic/fixed orchestration first.

External evidence from Agentless, DepRepair and mature analysis systems strongly supports this.

**Disposition: INDEPENDENTLY SUPPORTED.**

## 9.2 Current one-action EvidenceGapPlanner

The current planner pilot intentionally has a closed, pre-bound read-only catalog and cannot justify general planner adoption with one action.

External agent research supports tool-interface constraints and fixed baseline comparisons.

**Disposition: PROJECT-SPECIFIC CHOICE, independently reasonable for the current experiment.**

It should not be mistaken for the mature agent architecture.

## 9.3 Closed action catalog as permanent mature agent principle

Generalist agents and repository-intelligence systems show that long-tail investigations may require broader query/action capabilities.

**Disposition: SUPPORTED BUT TOO RESTRICTIVE if permanent.**

Possible mature direction:

- trusted capability registry;
- bounded parameter schemas;
- policy/admission;
- dynamic selection among registered capabilities;
- rare sandboxed broader escalation.

## 9.4 Generalist agent as default

Track B does not support this.

**Disposition: INDEPENDENTLY SUPPORTED rejection.**

Use a generalist agent only as:

- escalation;
- comparator;
- long-tail repository investigation.

## 9.5 Multi-agent architecture as default

External evidence shows possible challenger/debate value but substantial coordination/cost uncertainty.

**Disposition: INDEPENDENTLY SUPPORTED rejection as default.**

Selective challenger/verifier remains plausible for high-consequence or low-confidence cases.

## 9.6 LangGraph/framework adoption

Current experiment found ordinary Python sufficient for the bounded loop.

External research does not create a new need for framework adoption.

**Disposition: INDEPENDENTLY SUPPORTED current non-adoption.**

Reassess only if checkpointing, resumability, distributed tool execution or state branching becomes a concrete product need.

---

# 10. Evidence graphs, standards and provenance

## 10.1 Fully custom internal domain model

Current system owns domain-specific evidence types.

External standards do not replace the product's reasoning semantics.

**Disposition: INDEPENDENTLY SUPPORTED for the internal decision model.**

## 10.2 No standards interoperability

CycloneDX/SPDX/in-toto/SLSA/GitHub dependency submission expose useful concepts already aligned with UpgradePilot:

- relationship completeness;
- no-assertion;
- evidence methods/tools/confidence;
- occurrences/call stacks;
- build provenance;
- producer identity;
- signed revision/artifact binding.

**Disposition: SUPPORTED BUT INCOMPLETE.**

Do not rewrite internals around standards.

But run a mapping experiment before inventing more external/report provenance vocabulary.

## 10.3 Provenance authenticity vs semantic authority

Current doctrine already separates evidence identity from interpretation.

External attestation research reinforces:

\`\`\`text
cryptographically authentic
!= semantically correct
\`\`\`

**Disposition: INDEPENDENTLY SUPPORTED.**

Future attestations could add integrity without changing semantic authority.

---

# 11. Final synthesis / maintainer action

## 11.1 Current only-admitted action = \`abstain\`

Current source intentionally admits only explained abstention.

External research supports abstention and human decision authority, but not permanent abstention-only product behavior.

**Disposition: PROJECT-SPECIFIC CHOICE.**

It is a valid current proof boundary, not a mature target.

## 11.2 Action permission must not be inferred directly from one technical result

Current design refuses:

\`\`\`text
technical result
→ guessed merge/block action
\`\`\`

**Disposition: INDEPENDLY SUPPORTED.**

Action-specific prerequisites should remain explicit.

## 11.3 Proposed deterministic PermissionEnvelope + bounded LLM selection

This is a proposal, not accepted architecture.

Track B suggests alternatives:

- deterministic projection + model phrasing;
- selective calibrated model claim admission;
- human-interactive decision support;
- richer cross-candidate evidence state before action projection.

**Disposition: UNCERTAIN — EXPERIMENT REQUIRED.**

Do not adopt or reject the proposal before:

- action prerequisites exist;
- protected synthesis cases exist;
- maintainer UX can be evaluated.

## 11.4 Maintainer decision support as product objective

Current project is maintainer-centered but evaluation is still mostly machine/proof oriented.

External HCI/review research says decision quality/time/appropriate trust matter directly.

**Disposition: SUPPORTED BUT INCOMPLETE.**

This should become a later evaluation/output requirement.

---

# 12. Evaluation architecture

## 12.1 Current focused tests + regression + product simulations

This is strong for deterministic implementation ownership.

But Tier-1 found benchmark/oracle quality, contamination and protected evaluation concerns.

**Disposition: INDEPENDENTLY SUPPORTED but INCOMPLETE for AI/mature product evaluation.**

## 12.2 Development cases reused as final evidence

The agent plan already protects against this for its bounded pilot.

External benchmark history strongly validates that separation.

**Disposition: INDEPENDENTLY SUPPORTED.**

Extend the principle to future semantic/discovery/evaluation work.

## 12.3 One model/agent run as evidence

Not acceptable for stochastic method evaluation.

**Disposition: SUPPORTED BUT INCOMPLETE.**

Future scoring needs repeated runs/distributions where stochasticity matters.

## 12.4 System success = technical result accuracy alone

External maintainer research challenges this.

**Disposition: SUPPORTED BUT INCOMPLETE.**

Mature evaluation should include:

- time-to-decision;
- appropriate trust;
- external lookups;
- ability to catch a wrong system suggestion;
- cognitive load;
- usefulness;
- retained rationale.

---

# 13. Consolidated challenge matrix

| Current principle / design choice | Disposition |
| --- | --- |
| exact identity before semantic use | **INDEPENDENTLY SUPPORTED** |
| explicit provenance/scope | **INDEPENDENTLY SUPPORTED** |
| declaration != execution | **INDEPENDENTLY SUPPORTED** |
| step success != every command execution | **INDEPENDENTLY SUPPORTED** |
| successful execution != valid evidence | **INDEPENDENTLY SUPPORTED** |
| unresolved/conflicted preserved | **INDEPENDENTLY SUPPORTED** |
| missing evidence != negative evidence | **INDEPENDENTLY SUPPORTED** |
| candidate != applicability != action | **INDEPENDENTLY SUPPORTED** |
| candidate discovery completeness separate | **INDEPENDENTLY SUPPORTED** |
| model candidate cannot self-authorize | **INDEPENDENTLY SUPPORTED** |
| provider vs package-manager semantics separation | **INDEPENDENTLY SUPPORTED** |
| parse operation once | **INDEPENDENTLY SUPPORTED** |
| independent semantic dimensions + fail-closed precedence | **INDEPENDENTLY SUPPORTED** |
| demand-driven env/config proof | **INDEPENDENTLY SUPPORTED** |
| CI coverage != package-state proof | **INDEPENDENTLY SUPPORTED** |
| command-completion state != later behavior/action | **INDEPENDENTLY SUPPORTED** |
| Increment-4 command-derived composer | **INDEPENDENTLY SUPPORTED** |
| current shell/control-flow eligible subset | **SUPPORTED BUT TOO RESTRICTIVE** as mature boundary |
| handcrafted workflow-dataflow expansion | **UNCERTAIN — EXPERIMENT REQUIRED** |
| runtime observation only optional/future | **SUPPORTED BUT INCOMPLETE** |
| typed records with no repository-intelligence substrate | **SUPPORTED BUT INCOMPLETE** |
| one universal graph | **INDEPENDENTLY SUPPORTED rejection** |
| multi-view repository intelligence | **UNCERTAIN — EXPERIMENT REQUIRED** |
| changelog/release prose as upstream evidence | **SUPPORTED BUT INCOMPLETE** |
| source/API diff not first-class | **SUPPORTED BUT INCOMPLETE** |
| package behavior delta absent | **SUPPORTED BUT INCOMPLETE** |
| bounded semantic extraction + deterministic source validation | **INDEPENDENTLY SUPPORTED** |
| permanently narrow model context | **SUPPORTED BUT TOO RESTRICTIVE** |
| deterministic owner for every trusted semantic proposition | **SUPPORTED BUT TOO RESTRICTIVE** as universal mature rule |
| fixed pipeline before agents | **INDEPENDENTLY SUPPORTED** |
| one-action closed planner pilot | **PROJECT-SPECIFIC CHOICE** |
| permanently closed agent action catalog | **SUPPORTED BUT TOO RESTRICTIVE** |
| generalist agent default | **INDEPENDENTLY SUPPORTED rejection** |
| multi-agent default | **INDEPENDENTLY SUPPORTED rejection** |
| no LangGraph/framework without need | **INDEPENDENTLY SUPPORTED** |
| custom internal domain model | **INDEPENDENTLY SUPPORTED** |
| no standards mapping/interoperability | **SUPPORTED BUT INCOMPLETE** |
| cryptographic provenance != semantic truth | **INDEPENDENTLY SUPPORTED** |
| only current maintainer action = abstain | **PROJECT-SPECIFIC CHOICE** |
| technical result cannot self-authorize action | **INDEPENDENTLY SUPPORTED** |
| deterministic PermissionEnvelope proposal | **UNCERTAIN — EXPERIMENT REQUIRED** |
| current deterministic regression/product simulations | **INDEPENDENTLY SUPPORTED but INCOMPLETE** |
| maintainer decision quality as explicit metric | **SUPPORTED BUT INCOMPLETE** |

No accepted core principle is currently classified:

- \`SUPPORTED BUT TOO PERMISSIVE\`;
- \`HISTORICAL / NO LONGER JUSTIFIED\`;
- \`CONTRADICTED BY STRONGER APPROACH\`.

That is not because Track C protected the current architecture.

The external challenge instead found that the existing architecture's largest weaknesses are **missing capabilities and overly narrow future assumptions**, not unsafe permissiveness in the current trust model.

---

# 14. What should change in our mental model now?

## 14.1 Keep the epistemic spine

Do **not** replace:

\`\`\`text
identity
→ evidence
→ proposition
→ applicability
→ uncertainty
→ investigation
→ later action
\`\`\`

with an agent-first architecture.

The external evidence supports this spine.

## 14.2 Broaden the evidence-producing world around it

The mature system should be able to learn from more than today's handcrafted producers:

\`\`\`text
CodeQL / static analysis
Griffe / upstream API diff
runtime telemetry
package/build tools
repository/build/test graphs
deps.dev / supply-chain data
standards/provenance
model semantic discovery
maintainer knowledge
\`\`\`

## 14.3 Treat AI primarily as discovery/reasoning/planning, not authority

But do not freeze today's narrow input/action boundary forever.

Separate:

\`\`\`text
what AI may inspect
what AI may propose
what evidence validates
what policy admits
what maintainer decides
\`\`\`

## 14.4 Escalate adaptivity

Default:

\`\`\`text
deterministic/fixed
→ structured semantic reasoning
→ bounded planner
→ runtime evidence
→ rare generalist agent
\`\`\`

not:

\`\`\`text
general agent first
\`\`\`

## 14.5 Evaluate the whole decision-support product

Eventually ask:

> did the maintainer reach the right evidence-informed decision efficiently and with appropriate trust?

not merely:

> did our classifier/agent produce the expected label?

---

# 15. Experiment queue produced by Track C

These are **not all immediate tasks**.

They are the discriminating experiments now justified by real architecture questions.

## E1 — CodeQL Actions comparator — HIGH PRIORITY

Use before substantial expansion of custom workflow CFG/dataflow/environment propagation.

Learning value: very high.

## E2 — Griffe/API-diff vs changelog evidence — HIGH PRIORITY

Use before broadening upstream semantic discovery heavily.

Learning value: very high.

## E3 — runtime telemetry vs static inference — HIGH PRIORITY WHEN A REAL CASE NEEDS IT

Use StepSecurity-like process telemetry on one real workflow.

Learning value: very high.

## E4 — small multi-view RIG/repository graph — MEDIUM/HIGH PRIORITY

Do only when a real cross-file/build/test query justifies it.

Learning value: very high.

## E5 — typed-only vs controlled raw-source model context — HIGH PRIORITY BEFORE BROAD DISCOVERY MODEL

Measure discovery recall/noise.

Learning value: high.

## E6 — fixed investigation sequence vs bounded planner — REQUIRED BEFORE PLANNER ADOPTION

Use a protected evidence-gap corpus.

Learning value: very high.

## E7 — bounded planner vs generalist agent — LOWER PRIORITY / LONG-TAIL

Use only on genuinely atypical cases.

Learning value: high.

## E8 — calibrated model-claim admission — LATER

Protected semantic corpus + risk/coverage curves.

Learning value: very high.

## E9 — CycloneDX/SPDX/in-toto mapping — NON-BLOCKING LAB

Useful interoperability/security exposure.

## E10 — maintainer decision-quality study — LATER PRODUCT MATURITY

Run only when report/action UX stabilizes.

---

# 16. Immediate consequence for main / Increment 4

Main currently states:

\`\`\`text
Increment 3 CLOSED
→ Increment 4 SELECTED
→ fresh Increment-4 A0 next
\`\`\`

Track C does **not** change that sequencing.

Recommended handling:

1. **Do not reopen Increment 3.**
2. **Do not redesign Increment 4 into a graph/agent/CodeQL experiment.**
3. At Increment-4 A0, note this Track-C result as parallel architecture evidence.
4. Verify the composer:
   - preserves evidence origin/provenance;
   - keeps command-derived inference distinct from future direct observation;
   - does not claim later use/compatibility/action.
5. Continue Increment 4 if those accepted contracts remain intact.
6. Schedule the architecture experiments above only when their corresponding broader responsibility activates.

This keeps product progress moving while preventing today's bounded implementation from silently becoming tomorrow's permanent architecture.

---

# 17. Step status

\`\`\`text
Track A
  Step 1   project-conditioned limitation inventory       COMPLETE
  Step 2A  project-conditioned mechanism classification  COMPLETE

Track B
  broad external discovery                               COMPLETE
  Tier-1 #01–#07                                         COMPLETE
  Step 2B-X refreshed independent architecture           COMPLETE

Track C
  Step 2C adversarial comparison/reconciliation           COMPLETE

Next
  Step 3 whole-pipeline architecture map                 READY
\`\`\`

Step 3 should now map the complete public dependency-update PR → maintainer-output pipeline and label every responsibility as:

- current implemented reality;
- independently supported mature direction;
- project-specific current choice;
- experimental candidate;
- unresolved architecture competition;
- optional future subsystem.

That map should **not** flatten the distinctions recovered in Track C.
