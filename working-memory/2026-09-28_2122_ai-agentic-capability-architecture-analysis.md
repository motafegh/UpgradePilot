# AI / Agentic Capability Architecture Analysis — Parallel Design Workstream

**Date/time:** 2026-09-28 21:22 local
**Session status:** ACTIVE
**Primary responsibility/mode:** Planning / Design analysis — identify where deterministic logic, LLM reasoning, agentic investigation, or hybrid composition belong across UpgradePilot
**Branch:** analysis/ai-agentic-capability-map-2026-09-28
**Branch base:** e838fa656964a898c037cca6ef0d390983f106ad — advance Increment 2 to verification gate
**Canonical live-state owner:** MEMORY.md on current main; this record is intentionally not a competing live-state owner.
**Relevant owners / prior work:** PROJECT_CHARTER.md, AGENTS.md, OPERATING_GUIDE.md, ADR-0009, ADR-0010, plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md, prior EvidenceGapPlanner/LangGraph experiments, bounded LLM support-drop extraction, and the maintainer-decision synthesis proposal.

UP-SKILL:upgradepilot-planning-design
UP-SKILL:upgradepilot-working-memory

## 1. Session anchor

This branch exists so the AI/LLM/agent architecture investigation can proceed without interfering with the active product work on main.

The workstream is analysis/design only unless Ali later authorizes another operation. It must not silently modify the active runtime-state implementation, redefine accepted specifications/ADRs, or make itself the live project continuation owner.

The branch was created only after refreshing current main. During this conversation the product work advanced materially:

1. the first refresh showed Increment 1 fully closed and verified and Increment 2 Build-ready;
2. before branch creation, parallel main advanced again;
3. branch base e838fa6 records Increment 2 at the Verification/Evidence gate;
4. MEMORY.md at this branch base reports Increment 2 Build implemented in dependency/package_manager_operation.py and dependency/package_manager_semantics.py, migrated direct_install.py and pip project-selection consumption, retired the superseded pip_command.py helper, and added/extended focused tests;
5. Increment 2 is implementation truth at this snapshot, but focused/broader verification is still pending, so this branch must not describe Increment 2 as verified.

Because main is progressing in parallel, any later comparison, merge decision, or claim about the current product state must first refresh main again.

## 2. Why this workstream was started

Ali raised four connected questions:

1. continuously sync with new project work happening in parallel;
2. UpgradePilot deliberately treats many cases/states as unsupported, unresolved, or ineligible — for example conditional CI commands — so investigate whether AI/LLMs/agents can help cover some of those cases;
3. while the system is currently being designed and implemented mostly through deterministic responsibilities, ask whether failing to consider AI during design could make the architecture weaker or harder to extend later;
4. systematically examine the entire UpgradePilot pipeline from input to maintainer output and classify each responsibility by the appropriate mechanism.

Ali agreed with the initial architectural analysis and wants these questions worked through properly rather than treated as an isolated "add AI" feature.

## 3. Core conclusion established so far

The current deterministic direction is not inherently making UpgradePilot weak for AI.

In several areas it is doing the opposite: the product is increasingly producing explicit typed evidence, independent semantic facts, provenance, unresolved states, and authority boundaries. Those are strong interfaces for future bounded model reasoning.

The important refinement is:

> Design for AI extensibility now; adopt AI only when evidence justifies it.

This is different from either extreme:

    bad extreme A:
    ignore AI completely until the deterministic system is finished

    bad extreme B:
    replace difficult deterministic responsibilities with an LLM because they are difficult

The preferred architecture is:

    trustworthy typed evidence / source identity / provenance
            ↓
    explicit propositions + unresolved gaps
            ↓
    deterministic logic where the proposition is computable
            ↓
    bounded LLM interpretation where semantic understanding is the missing capability
            ↓
    agentic investigation where additional evidence/actions are needed
            ↓
    deterministic validation / admission / trusted-state update

A recurring authority rule is:

    model may propose / interpret / prioritize / investigate
    !=
    model automatically proves the trusted proposition

For many high-value product claims, deterministic code should remain the authority that admits evidence and establishes trusted state.

This rule is not meant to ban models from raw or semi-structured evidence forever. Some future responsibilities — especially broad technical-impact candidate discovery — may legitimately need LLM inspection of source, release notes, configuration, diffs, or other less-structured material. The requirement is that source identity, provenance, claim boundaries, and promotion into trusted state remain explicit and testable.

## 4. Conditional CI commands — first concrete case

Current accepted command analysis deliberately distinguishes:

    real command occurrence exists in static source
    !=
    that command executed
    !=
    that command succeeded

For example:

    if SOME_CONDITION; then
        pip install -r requirements.txt
    fi

The parser can preserve a real pip install occurrence and mark its structural context as conditional.

A successful GitHub Actions step does not prove that the conditional branch executed. Therefore current runtime strengthening correctly treats known conditional structures as ineligible for the stronger step-success-derived exact-command-execution proposition.

The architectural insight is:

> currently ineligible does not necessarily mean permanently unsupported.

The right question is not "can an LLM guess whether it ran?" but:

> What exact fact prevents the stronger proposition from being established, and what mechanism could legitimately establish that fact?

### Case A — simple condition with known values

Example:

    if [[ "$MATRIX_PYTHON" == "3.12" ]]; then
        pip install -r requirements.txt
    fi

If UpgradePilot can establish the exact runtime value and supports this predicate form, a bounded deterministic control-flow evaluator may be sufficient.

Conceptually:

    conditional command occurrence
    + exact predicate structure
    + exact predicate inputs
    + deterministic predicate evaluation = true
    + required execution-profile/runtime evidence
    → stronger command-execution reasoning may become possible

An LLM is probably unnecessary here.

### Case B — complex but repository-contained condition

Example:

    if ./scripts/should_install.sh; then
        pip install -r requirements.txt
    fi

Now the unresolved fact may require understanding another repository script, its inputs, and what it establishes.

Possible architecture:

    conditional occurrence
    → deterministic resolver cannot settle predicate
    → explicit EvidenceGap
    → bounded semantic interpretation / investigation
    → inspect referenced script and required inputs
    → produce typed candidate facts/evidence
    → deterministic validation/admission
    → retry proposition

This may be a strong hybrid case.

### Case C — evidence is missing, not merely logic

A condition may depend on runtime environment, generated files, previous steps, tool outputs, repository configuration, or other evidence not yet acquired.

That is more naturally agentic investigation:

    unresolved proposition
    → identify evidence gap
    → select one admitted read-only action
    → acquire evidence
    → deterministic interpretation / trusted-state update
    → retry proposition

This resembles the already-proven EvidenceGapPlanner architecture.

### Case D — fact is fundamentally unobservable at the available boundary

Some runtime facts may remain unknowable from the evidence UpgradePilot can safely/reliably acquire.

In that case:

    AI confidence != evidence

The correct result remains unresolved / abstention rather than manufacturing proof.

## 5. General method for every currently excluded or unsupported case

Before deciding that AI is useful, classify why the case is unsupported.

For each limitation ask:

    1. What exact proposition is currently not established?
    2. What evidence/fact is missing?
    3. Is the missing capability:
       - deterministic computation?
       - semantic interpretation?
       - additional evidence acquisition?
       - multi-step orchestration?
       - prioritization among possible investigations?
       - fundamentally unavailable/unknowable?
    4. What is the simplest adequate mechanism?
    5. If an LLM is used, what may it claim?
    6. If an agent is used, what actions may it choose/execute?
    7. What deterministic admission/validation remains?
    8. What evidence would justify promoting the mechanism into product architecture?

Only then choose among:

    deterministic algorithm
    LLM semantic component
    agentic investigation
    hybrid composition
    remain explicitly unresolved

This prevents "unsupported = use AI" from becoming an architectural shortcut.

## 6. Why the current deterministic architecture can be AI-friendly

AI extensibility becomes easier when the deterministic system preserves rich intermediate state.

Good examples already visible in UpgradePilot include separation of:

- source identity and provenance;
- observation vs interpretation;
- static command occurrence vs runtime execution;
- exact-command execution vs package-manager effect;
- manager environment vs installation destination;
- package mutation mode vs direct-requirement handling;
- supported / unsupported / unresolved distinctions;
- evidence state vs maintainer-action authority.

Increment 2 is especially relevant. Its design avoids collapsing package-manager meaning into a single boolean such as:

    valid_install = true

and instead exposes independent semantic facts.

That makes later deterministic composition better and gives future models better structured state to reason over.

A weak AI-hostile architecture would collapse many responsibilities into opaque booleans or ad-hoc procedural heuristics, forcing a future model to re-read raw implementation details to recover meaning.

A stronger AI-extensible architecture preserves:

    typed fact
    + provenance
    + confidence/authority state
    + unresolved reason
    + relationship to the product proposition

## 7. Existing UpgradePilot AI / agentic work that this analysis must reuse

This is not a greenfield "add agents" discussion.

### A. Implemented bounded LLM semantic extraction

The upstream Python-support-drop extraction path already uses the local LM Studio model as a bounded semantic extractor.

Important existing boundary:

    model proposes semantic candidate
    → deterministic code recovers/validates exact source evidence
    → model does not own compatibility/safety/maintainer action

This is a real product example of LLM usefulness without giving it source authority.

### B. EvidenceGapPlanner experiments

The ordinary-Python EvidenceGapPlanner and the independent LangGraph implementation already established a useful agentic architecture:

    typed InvestigationSnapshot
    → model chooses one admitted action or stop/defer/unresolved
    → deterministic post-model admission/rebind
    → read-only execution
    → deterministic evidence interpretation/state transition

Real public Pydantic proof showed model proposal + deterministic authorization + exact tool effect + deterministic product interpretation.

This is highly relevant to future unsupported-case investigation.

### C. LangGraph framework experiment

LangGraph demonstrated useful explicit topology, runtime node-path observability, state/context separation, and routing/effect isolation, but framework adoption was correctly deferred because the actual planner-selectable action surface was still too small.

Do not manufacture agent complexity merely to justify a framework.

### D. Future maintainer decision/report synthesis

The existing non-controlling proposal already separates EvidenceGapPlanner from a later DecisionSynthesizer.

The proposed synthesis boundary is:

    completed typed evidence
    → deterministic PermissionEnvelope
    → bounded LLM synthesis
    → deterministic validation
    → validated explanation/report

This analysis should evaluate that boundary against the complete pipeline rather than assume it is already admitted.

### E. Mature technical-impact candidate discovery

The mature-system horizon identifies broad impact-candidate discovery as likely hybrid territory. This remains one of the strongest places to investigate LLM value because the problem is open-ended semantic discovery rather than a narrow deterministic proof.

## 8. Preliminary whole-pipeline mechanism map

This is an initial hypothesis, not an accepted architecture decision.

| Responsibility | Current architectural direction |
| --- | --- |
| PR / repository / revision / dependency identity | deterministic only |
| Public evidence acquisition | deterministic execution; agent may later choose what evidence to acquire |
| Provenance / trust / evidence-state admission | deterministic authority |
| Workflow / shell parsing | deterministic parser foundation; hybrid semantic assistance may later help selected hard cases |
| Conditional / control-flow resolution | strong hybrid candidate |
| Exact runtime command-execution proof | deterministic trusted proposition; agent may investigate gaps |
| Package-manager semantic facts | primarily deterministic; selective semantic assistance only if a real unsupported semantic class justifies it |
| Upstream release-text interpretation | bounded LLM already useful |
| Technical impact-candidate discovery | very strong future LLM/hybrid candidate |
| Candidate-specific applicability | deterministic propositions plus bounded semantic reasoning where needed |
| Discriminating investigation / next evidence choice | very strong agentic candidate |
| Evidence sufficiency | deterministic authority |
| Maintainer-action permission | deterministic authority |
| Cross-evidence reasoning / prioritization | future bounded LLM candidate |
| Maintainer explanation/report synthesis | strong LLM candidate after deterministic permission/validation |
| Replay / regression / evaluation | deterministic foundation; model-as-judge only supplementary and carefully controlled |

Two particularly strong AI-shaped responsibilities remain:

1. technical-impact candidate discovery — "what could this exact dependency change materially affect in this repository?";
2. adaptive evidence-gap investigation — "what evidence should we obtain next to resolve the important uncertainty?"

These are more naturally model/agent problems than deterministic package/version parsing, provenance admission, or source identity.

## 9. Important distinction: AI-aware design vs premature AI integration

Future design work should add one explicit question:

> If an LLM or agent later needed to help with this responsibility, are we preserving the right typed state, provenance, unresolved reasons, authority boundaries, and action seams?

This does not mean every current design must implement an AI hook, model abstraction, prompt interface, agent framework, or generic tool registry.

Avoid speculative machinery such as:

- generic agent interfaces with no admitted product responsibility;
- model adapters only for possible future use;
- universal orchestration frameworks before there are real multi-step actions;
- converting deterministic facts into "AI-ready" strings instead of typed contracts;
- broad raw-context dumping when a smaller evidence projection is enough.

The aim is architectural optionality, not AI ceremony.

## 10. Candidate limitation inventory for the next analysis

The initial command/CI family includes at least:

- conditional commands;
- short-circuit chains;
- loops;
- functions / blocks;
- nested/subshell execution;
- process substitution;
- asynchronous/background commands;
- dynamic GitHub expressions;
- dynamic shell selection;
- custom shell templates;
- unresolved matrix/environment values;
- environment propagation across steps;
- setup-python / PATH executable provenance;
- virtual-environment activation;
- ambient PIP_* / UV_* process variables;
- persistent package-manager configuration;
- third-party action effects;
- runtime-only package state;
- logs/artifacts that may expose otherwise missing evidence.

This inventory must not stay limited to CI/commands. The same classification should later be applied across upstream interpretation, dependency semantics, impact discovery, applicability, investigation, synthesis, reporting, evaluation, and recovery.

## 11. Current analysis route

This is a working-session route, not yet a new controlling plan.

### Step 1 — map limitations / unresolved cases

Build a structured inventory of important currently unsupported, deliberately ineligible, unresolved, or deferred cases across the product.

For each one record:

    responsibility
    current boundary
    why it is unsupported/unresolved
    missing proposition/evidence
    decision criticality

Start with CI/command/control-flow because it gives a concrete case, then broaden to the rest of the pipeline.

### Step 2 — classify the appropriate mechanism

For each limitation classify:

    deterministic-only
    LLM useful
    agentic useful
    hybrid
    AI probably inappropriate

Also record:

    model-visible state
    allowed model authority
    deterministic authority
    required tools/actions
    failure/abstention behavior

### Step 3 — map the entire product pipeline

Traverse:

    Dependabot PR / public repository input
    → acquisition
    → normalization / provenance
    → dependency + CI + upstream + repository evidence
    → impact discovery
    → applicability
    → investigation
    → evidence sufficiency
    → maintainer-action permission
    → synthesis/explanation
    → final maintainer output
    → replay/evaluation

Classify each responsibility rather than classifying modules or frameworks.

### Step 4 — compare the map to existing AI experiments

Determine which needs are already served by:

- bounded support-drop semantic extraction;
- EvidenceGapPlanner;
- ordinary-Python orchestration;
- LangGraph workflow;
- proposed DecisionSynthesizer;
- existing development evaluation/rubric work.

Avoid duplicate experiments.

### Step 5 — identify actual architecture/design gaps

Only after the map exists decide whether anything needs promotion to:

- accepted specification change;
- ADR;
- bounded plan;
- new experiment;
- product implementation;
- or no action.

Do not create AI machinery simply because an area is interesting.

## 12. Questions intentionally still open

- Which current exclusions are genuinely decision-critical in representative public repositories rather than merely theoretical edge cases?
- Which conditional/control-flow classes can be resolved cheaply and transparently with deterministic analysis before AI is considered?
- Where should an explicit reusable EvidenceGap-style representation exist across product responsibilities?
- Should model-assisted semantic reasoning be allowed to create only candidate facts, or can some narrowly defined model outputs become trusted after deterministic grounding/validation?
- Which evidence gaps require new acquisition capabilities versus better interpretation of evidence already present?
- At what point does the action catalog become rich enough that LangGraph/LangChain or another agent framework provides measurable value over ordinary Python?
- How should broad technical-impact candidate discovery be evaluated for recall/false discovery without turning an LLM into an ungrounded oracle?
- How should final synthesis be evaluated without self-judging contamination from the same model family?
- Which current typed contracts already give sufficient AI seams, and where are we accidentally collapsing information that a later reasoner would need?

## 13. Current stop / handoff

Established in this session:

- dedicated analysis branch created from exact main snapshot e838fa6;
- current parallel product state re-synced through Increment 2 Build → Verification gate;
- agreed that unsupported/ineligible cases should be analyzed by missing proposition/evidence type, not automatically assigned to AI;
- agreed that conditional commands provide a useful first case for distinguishing deterministic control-flow reasoning, semantic assistance, agentic evidence acquisition, and legitimate unresolved states;
- agreed that current deterministic typed-fact/provenance architecture is generally compatible with future AI and should be designed with AI extensibility in mind;
- established a preliminary whole-pipeline AI responsibility map;
- established the next analysis route without yet creating a new controlling product plan or changing accepted architecture.

Next discussion should begin from Step 1: limitation/unresolved-case inventory, while refreshing main whenever parallel product progress becomes relevant to a conclusion.
