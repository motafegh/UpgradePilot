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


## 14. Step 1 — current limitation / unresolved / deferred inventory

### 14.1 Evidence snapshot and reconciliation

This inventory was refreshed against current `main` through:

`b37bed22af2dd958b46dda417834cc64cbb255ab` — `record phase D real-case teaching priority`.

At that live snapshot, Increment 2 Verification is GREEN and its D evidence-backed ownership-learning phase is current. Product verification #10 is green and the full deterministic regression passed 653 tests. The branch base remains the earlier exact snapshot `e838fa6`; this section records later observed `main` state without pretending that the analysis branch itself has been rebased.

Three September-8 investigation findings were explicitly rechecked and are **not current limitations**:

1. **comment / quoted-text command false positives** — superseded by the parser-backed static-command architecture and current shared command analysis;
2. **PR changed-file / frozen-head mismatch** — current `GitHubPullRequestClient` validates each changed-file locator against the frozen head and performs a post-acquisition base/head/count identity recheck;
3. **workflow run-attempt / jobs mismatch** — current Actions acquisition uses the attempt-specific jobs endpoint for the captured `run_attempt`.

These historical defects remain useful provenance, but carrying them into this register would duplicate already-absorbed work.

### 14.2 Classification vocabulary for Step 1

This step is intentionally **not yet choosing AI/LLM/agent mechanisms**.

Each item is classified only by why the current product stops:

- **bounded unsupported** — the current admitted implementation explicitly excludes a syntax/mechanism/family;
- **unresolved representation/logic** — evidence exists, but the current representation or deterministic rule cannot safely establish the proposition;
- **missing evidence/acquisition** — the needed observation is not currently acquired or is unavailable;
- **deferred responsibility** — the mature product responsibility is recognized but not yet implemented/admitted;
- **intentional claim boundary** — stronger inference is prohibited because the available evidence does not prove it;
- **bounded operational safeguard** — hard acquisition/resource/safety limits deliberately trade coverage for trustworthy operation.

An item can belong to more than one class.

### 14.3 Current whole-pipeline inventory

| Area | Current unsupported / unresolved / deferred boundary | Exact missing proposition or evidence | Current pressure / relevance |
| --- | --- | --- | --- |
| GitHub acquisition scale | Changed files, workflow runs, and jobs are acquired under explicit completeness/resource caps; evidence beyond those caps is rejected rather than sampled. | Complete bounded provider snapshot inside the supported resource envelope. | Operational safeguard; important for unusually large PR/CI surfaces, but not currently evidence for an AI problem. |
| Repository-file / runtime evidence availability | Exact repository files can be explicitly unavailable; runtime step summaries may be absent. Generic job-log/stdout/artifact acquisition is still outside the first runtime-state route. | Exact source or exact command/runtime-state observation at the required revision/boundary. | S002 shows historical logs/resolved environment can become unavailable; runtime-state plan keeps logs/artifacts as a conditional later source rather than assuming them. |
| PyPI provenance / upstream repository identity | File provenance may be unavailable or use an unsupported provenance contract; upstream repository association may be unsupported or ambiguous; current repository association is GitHub-oriented. | Trustworthy publisher/source repository identity for the exact release/file. | Important trust/provenance boundary; missing provenance remains a real abstention source rather than something semantic reasoning can invent. |
| Changelog / upstream source discovery | Changelog discovery deliberately does not rank ambiguous documentation sources. Missing release sections, conflicting source order, unavailable tags/releases, or incomplete authoritative release series remain explicit problems. | One sufficiently authoritative, correctly bounded upstream source window for the exact release interval. | Directly affects semantic extraction availability; model output cannot substitute for missing authority. |
| Requirements dependency-transition extraction | Requirements-family extraction supports an in-place modified admitted requirements/constraints file with one unambiguous removed exact pin and one added exact pin. Broader specifier/edit shapes abstain. | One exact dependency transition with trustworthy source identity. | Bounded current source family; expansion may matter for broader Dependabot shapes but has not yet been justified universally. |
| Pyproject dependency-transition extraction | Current pyproject rule is deliberately limited to one exact-pin transition in `[project.optional-dependencies]` with conservative base/head comparison. Direct-reference transitions, broader edits, ambiguity, and other dependency sections/forms remain outside this first rule. | One exact dependency transition plus source/environment identity across broader pyproject dependency forms. | S011 pressure justified optional-extra support and has largely been absorbed; broader pyproject coverage remains open rather than automatically generalized. |
| uv lock structure / reachability | Current uv proof is bounded by admitted schema/structure. Repeated resolution branches, unsupported structural changes, marker/fork ambiguity, unsupported bindings/selectors, and unevaluated conditions can remain unresolved. Presence somewhere in `uv.lock` is not treated as selected-environment membership. | Exact selected-root/environment reachability of the changed package under material marker/fork context. | Real dependency-environment pressure; intentionally avoids unioning all lock paths. |
| Project environment selection | Current static selection recognizes bounded pip/uv project forms, working-directory context, admitted groups/extras/selectors. Dynamic project paths/groups/extras and unsupported selectors remain unresolved; arbitrary package-manager/task-runner semantics are outside the current rule. | Exact project environment selected by the command under the repository/workflow context. | S005 remains a concrete deferred transfer case because tox + uv-venv-lock-runner is materially different from direct uv commands. |
| Shell syntax family | Shared command analysis admits bounded Bash/sh, PowerShell/pwsh, and CMD/batch syntax families. Python-shell mode and arbitrary custom interpreters are not treated as shell scripts; dynamic shell identity and some custom templates remain unresolved. | Trustworthy syntax/execution profile for the exact `run:` body. | Common workflow variability; deliberately fail-closed because wrong parsing can create false positive evidence. |
| Command atoms / dynamic shell material | Expression-backed or shell-dynamic command atoms are preserved as dynamic/unsupported rather than guessed into literal executables/options/paths. Material parser error makes the command analysis unresolved with no textual fallback. | Literal/grounded value of a material command token or a stronger safe representation of the dynamic expression. | Cross-cutting pressure for package-manager, path, and control-flow reasoning. |
| Conditional and path-dependent command execution | Known conditional bodies, loops, deferred function/block bodies, status inversion, asynchronous/background execution, and process substitution are currently **ineligible** for step-success runtime strengthening. | Proof that the exact occurrence lies on the successful executed path under the exact runtime inputs. | This is our first concrete AI-architecture case. The command can be real static evidence while execution remains unproven. |
| Short-circuit / pipeline / nested / later-chain execution | Generic short-circuit, pipelines, nested/subshell/compound structures, later sequential occurrences, and some shell-specific complex shapes remain unresolved because the IR does not yet preserve enough operator/position/status-contribution semantics. | A bounded structural relation sufficient to infer exact-command execution from the containing step, or direct command-level runtime evidence. | S004's real `. ./venv/bin/activate && pip install ...` form is an explicit re-entry case; this is real rather than synthetic pressure. |
| Static↔runtime workflow correlation | Current correlation requires ordinary non-strategy jobs, literal unique job identities, deterministic step display identities, and available ordered runtime step summaries. Reusable-workflow jobs, strategy/matrix jobs, dynamic names, ambiguous duplicates, and unavailable step summaries remain unresolved/unsupported. | Exact one-to-one static/runtime job+step identity under expanded workflow semantics. | Material for matrix/reusable-workflow repositories and for any stronger exact-command runtime claim. |
| Checkout / working-directory provenance | Dynamic higher-precedence working-directory declarations, ambiguous/dynamic checkout repository/path inputs, conditional checkout shapes, or unresolved project-root relations prevent stronger source/path conclusions. | Exact repository root/project root and path provenance seen by the command. | Cross-cuts requirements installs, project selection, and environment membership. |
| Package-manager operation declaration | Increment 2 currently provides one reusable **pip install** operation declaration. Unknown/dynamic material before `install`, unsupported pip global options, and some module-invocation ambiguity become explicit problems rather than being reinterpreted downstream. | One exact package-manager operation identity with all material command-local tokens classified. | Current live implementation boundary; designed to be extended only from real semantic pressure rather than into a universal package-manager parser. |
| Effective package-manager semantics | Increment 2 resolves command-local decisive facts such as explicit `--python`, destination selectors, `--dry-run`, and direct-requirement handling. Multiple selectors can be unsupported; dynamic arguments can block a fact. When no decisive CLI override exists, process environment / persistent config / executable/default evidence is explicitly still required. | Effective manager environment, destination, mutation mode, and direct-requirement handling after command line → process env → config → default precedence. | This is the immediate post-Increment-2 program gap; it is already the accepted next runtime-state responsibility, not a newly discovered AI idea. |
| Runtime dependency-state proof | Exact command execution still does not prove exact proposed-version presence. The command-derived requirement-state composer and application integration are later increments; direct target-owned runtime-state/log evidence remains conditional Route B. | Exact proposed requirement satisfied in the exact relevant package-state scope at the justified command-completion boundary. | Central current technical-completion responsibility. |
| Target CI environment interpretation | Target artifact environment currently handles a bounded job slice. Ambiguous target-job selection, reusable-workflow jobs, multiple setup-python steps, non-single-literal runner forms, strategy/matrix context, and container context remain unsupported or partially interpreted. Exact wheel compatibility state remains unresolved at this layer. | Exact target interpreter/platform/environment sufficient for the artifact proposition. | S008 demonstrates real artifact/target-environment pressure; simply seeing a successful unpinned CI job is not enough. |
| Target Python declaration/comparison | Current Python-support applicability uses exact target `pyproject.toml [project].requires-python` evidence and an admitted deterministic specifier comparison subset. Missing/invalid declarations and unsupported specifier forms remain unresolved. | Exact target declared Python range and a supported comparison to the dropped line. | Current first impact mechanism; narrow by design. |
| Artifact-serviceability / installation-path consequences | Exact wheel inventory can establish bounded wheel-compatibility facts, but absence of a compatible wheel does not prove installation failure because source-distribution fallback may remain. Exact target tags/context can also remain unresolved. | Exact installation-path consequence in the relevant interpreter/platform environment. | S008 explicitly proves this distinction and shows why artifact availability is a separate impact mechanism. |
| Broad technical-impact candidate discovery | The product does **not** yet implement general discovery of all material mechanisms created by a dependency update. Current implemented mechanisms are bounded examples, not transition-level discovery completeness. | A bounded, reviewable set of materially plausible impact candidates plus an honest statement about discovery coverage. | S010 is direct real-case pressure: one NumPy proposal exposed multiple distinct mechanisms with different target-handling states. |
| Repository-purpose / policy / provenance context | Mechanism-specific applicability does not currently constitute a general repository-purpose/context reasoning layer. | Material repository context whose truth can affect appropriateness even when technical compatibility remains unresolved. | S009 shows a real reproducibility repository where exact version identity is part of the artifact/purpose, not merely a solver constraint. |
| Coordinated package-family / platform-family reasoning | No general product responsibility currently establishes coordinated multi-package family coherence across platform-specific distribution channels/environments. | Cross-package version/platform family relationship for the exact target environment. | S007 provides real CUDA/PyTorch-family pressure and demonstrates that one dependency cannot always be reasoned about in isolation. |
| Persisted-state / producer-version applicability | Product applicability does not yet generally model runtime artifacts/state produced under the old dependency version and later consumed under the new one. | Artifact existence, relevant embedded dependency-owned state, producer version, and post-update reuse/selection. | S012 provides real scikit-learn persisted-artifact pressure; arbitrary deployment artifact history may remain unknowable from repository evidence alone. |
| Discriminating targeted-check derivation | The implemented Python-support selector chooses only one predefined read-only action: acquire exact target Python declaration. General targeted-check derivation from arbitrary behavior/coverage gaps is not a product capability. | Which concrete observation would maximally discriminate one decision-relevant unresolved proposition, with bounded expected outcomes. | S006 gives direct pressure and also exposes evaluation/oracle-isolation difficulty. |
| Adaptive multi-step investigation | Existing EvidenceGapPlanner / LangGraph work remains experimental and initially has only one real selectable action. The product does not yet run a general adaptive evidence-acquisition loop. | A sufficiently rich admitted action catalog, state transition semantics, budgets/stopping, and evidence that adaptive choice outperforms simpler sequencing. | Prior experiments prove the boundary can work, but framework/product adoption was correctly deferred because the action surface was too small. |
| Candidate applicability coverage | Applicability can represent established/refuted/unresolved/conflicted paths, but negative candidate closure requires sufficient path-model coverage. Omitted viable routes prevent global non-applicability claims. | Evidence that the represented path model is sufficiently complete for the bounded candidate. | General proof limitation; AI confidence cannot manufacture path coverage. |
| Overall evidence sufficiency / maintainer actions | Stable action semantics exist, but the current product evaluator intentionally admits **only `abstain`**. Merge, targeted checks, investigate/block, and defer remain unavailable until their positive normal-producer prerequisites are proven. | Action-specific positive permission from trustworthy evidence/context/coverage. | Major current product limitation by design; do not “unlock” actions by weakening evidence rules. |
| Cross-evidence synthesis / maintainer explanation | A future LLM-assisted synthesis proposal exists, but there is no admitted product LLM that chooses final action from evidence. | Validated reasoning/explanation inside a deterministic permission envelope, with complete citation/uncertainty preservation. | Recognized future responsibility; must not be conflated with the already experimental investigation planner. |
| Persistence / replay / recovery / evaluation | Runtime persistence/replay/corpus evaluation remains mostly B3/B5/future work. Product-simulation artifacts are evidence for design, not the operational product store. Some simulation cases (for example S006) deliberately lack self-contained raw-source replay. | Durable evidence identity/content, reproducible state transitions, recovery semantics, and trustworthy evaluation corpus/oracles. | Important for debugging, longitudinal proof, planner/model evaluation, and production robustness; not solved by better reasoning alone. |
| Dynamic/behavioral execution | UpgradePilot does not generally execute arbitrary target/upstream code merely to settle compatibility. Resolver/runtime execution is gated by security, cost, isolation, and proposition value. | A safe, exact, decision-discriminating observation that cannot be established more cheaply/trustworthily from static evidence. | S004/S007/S008/S012 all demonstrate cases where stopping before expensive execution can be correct; missing execution is not automatically a capability defect. |

### 14.4 Real-case pressure map

The most useful preserved real cases for the current limitation inventory are:

- **S002** — historical logs/exact resolved environment can disappear; acquisition/durability boundaries matter.
- **S004** — real `&&` command structure is a concrete operator-aware runtime-strengthening re-entry case.
- **S005** — tox + uv-venv-lock-runner demonstrates that direct package-manager interpretation cannot be assumed universal; exact resolver evidence materially changed the decision in the simulation.
- **S006** — a behavior-specific coverage gap creates a real targeted-check-selection problem and exposes blind-evaluation/oracle-isolation requirements.
- **S007** — coordinated package-family + platform environment reasoning is a distinct mechanism family.
- **S008** — wheel disappearance/source fallback and exact target-environment coverage are separate propositions.
- **S009** — repository purpose/provenance can be decision-relevant without first resolving deeper runtime compatibility.
- **S010** — broad candidate discovery can miss multiple materially distinct mechanisms from one update.
- **S011** — optional-extra/environment selection and CI non-coverage were real pressure; much of this pressure has already been absorbed by current dependency/environment work, so it should not be misreported as wholly unsupported now.
- **S012** — persisted artifacts make old-environment producer state part of applicability; arbitrary deployment history may remain genuinely unavailable.

### 14.5 Cross-cutting findings from Step 1

#### Finding A — “unsupported” is not one kind of problem

The register contains at least five materially different reasons the system stops:

```text
representation too weak
evidence missing
product responsibility not implemented yet
claim intentionally prohibited
operation deliberately bounded for safety/cost/trust
```

Treating all five as one “AI opportunity” would be architecturally wrong.

#### Finding B — many current limits sit at the boundary between static evidence and runtime truth

This is especially visible in:

- conditional/control-flow execution;
- static↔runtime workflow correlation;
- project environment selection;
- effective package-manager semantics;
- runtime dependency-state proof;
- target environment / artifact compatibility.

These areas repeatedly ask:

> what additional proposition would let existing trustworthy evidence become stronger without changing its meaning?

That is likely a central organizing question for Step 2.

#### Finding C — the largest mature-product gaps are not parser edge cases

The broadest still-open responsibilities are:

1. technical-impact candidate discovery breadth;
2. heterogeneous repository-context discovery;
3. discriminating/adaptive investigation;
4. evidence sufficiency → non-abstention action permission;
5. durable replay/evaluation.

Therefore our AI architecture work should not become only a project about solving shell conditionals.

#### Finding D — some “missing” capabilities should remain missing until a decision-critical proposition requires them

Real cases repeatedly show that deeper execution can be unnecessary:

- S004 stopped when stronger work would not change the action;
- S007 can stop at static package-family evidence;
- S008 does not need a source-build reproduction to establish wheel-path transition;
- S012 does not need a cross-version runtime experiment to establish the documented persistence boundary.

So the mature architecture needs to represent **justified stopping**, not only ever-increasing capability.

#### Finding E — current typed-state architecture already preserves many useful future reasoning seams

The inventory repeatedly exposes typed states such as:

```text
unsupported
unresolved
not_established
ineligible
conflicted
source_unavailable
ambiguous
needs_lower_source_evidence
```

and separates propositions such as:

```text
static occurrence
exact execution
manager environment
destination
mutation mode
environment membership
target relevance
artifact serviceability
candidate applicability
maintainer-action permission
```

This supports the earlier conclusion that the deterministic work is not inherently making the future AI system weaker. The main design risk would be collapsing these distinctions later, not their existence today.

### 14.6 Step-1 status and boundary

**Step 1 initial whole-pipeline inventory: COMPLETE ENOUGH FOR DISCUSSION / STEP 2.**

This does not claim an exhaustive catalog of every error code or every unsupported package-manager flag. It captures the material current responsibility families and the most important real-case pressures needed for the AI/agent architecture question.

No source, test, accepted specification, ADR, plan, or `MEMORY.md` was changed by this analysis.

The next planned step remains:

> classify each material family by the simplest adequate mechanism — deterministic-only, bounded LLM, agentic investigation, hybrid, or intentionally unresolved — while separately defining model-visible state, model authority, deterministic authority, required tools/evidence, and failure/abstention behavior.

Do not enter that classification silently; discuss this Step-1 register with Ali first.


## 15. Step 2 — mechanism classification and authority design

### 15.1 Step-2 decision rule

Step 2 does **not** ask:

> Where can we insert an LLM?

It asks:

> For each real responsibility or limitation, what is the simplest mechanism that can establish the needed proposition at the required proof strength?

Use these mechanism classes:

- **D — deterministic-first / deterministic authority**
  - parsing, identity, exact comparison, provenance validation, bounded graph/reachability, policy/admission, and trusted proposition composition where explicit rules exist;
- **L — bounded LLM semantic component**
  - irreducible natural-language/software-meaning interpretation where the model can propose structured semantic claims that remain grounded and validated;
- **A — agentic investigation**
  - choosing among several admitted evidence-gathering actions, conditionally sequencing them, reacting to observations/failures, and stopping when further work is not justified;
- **H — hybrid**
  - deterministic evidence/authority plus bounded LLM interpretation and/or agentic evidence acquisition;
- **U — intentionally unresolved / abstain**
  - the required fact is unavailable, unsafe, unaffordable, outside the product boundary, or not decision-critical enough to justify more work.

A responsibility can be **H** while still giving the model very little authority. “Hybrid” means multiple mechanisms cooperate; it does **not** mean the LLM becomes co-authority over evidence truth.

### 15.2 Universal authority constraints

The following remain the default design constraints unless later evidence justifies a narrower exception:

```text
MODEL / AGENT MAY
- interpret bounded semantic material;
- formulate candidate mechanisms/propositions;
- choose among currently offered investigation actions;
- prioritize evidence/checks/reasons;
- propose a stop/defer/unresolved disposition inside its semantic contract;
- synthesize explanation from already-trusted state.

MODEL / AGENT MUST NOT BY ITSELF
- invent repository/revision/path/source identity;
- upgrade static evidence into runtime evidence;
- manufacture missing provenance or completeness;
- authorize its own tool/action execution;
- change hidden action parameters;
- establish package/version/environment truth from confidence alone;
- declare candidate/path/discovery completeness;
- grant maintainer-action permission;
- erase mandatory uncertainty/conflict/claim limits.

DETERMINISTIC PRODUCT CODE OWNS
- exact identity and provenance;
- trusted evidence-state promotion;
- mechanical parsing/comparison/reachability where explicit;
- action catalog and execution admission;
- security/mutation/cost policy;
- freshness/rebinding before effects;
- trusted proposition state;
- action-permission envelope;
- replayable state transition and claim limits.
```

This generalizes the already-proven EvidenceGapPlanner pattern:

```text
trusted state
→ explicit model projection
→ untrusted model proposal
→ deterministic rebind/admission
→ bounded effect
→ deterministic evidence interpretation
→ trusted next state
```

It also matches the implemented upstream support-drop pattern:

```text
authoritative bounded source
→ LLM semantic candidate
→ deterministic source-line grounding / validation
→ trusted bounded claim or explicit problem
```

### 15.3 Detailed mechanism map

| Responsibility / limitation | Best mechanism | Model-visible state / AI role | Deterministic authority | Failure / abstention behavior |
| --- | --- | --- | --- | --- |
| GitHub acquisition scale/resource caps | **D** | Normally none. AI has no useful role in deciding whether an incomplete provider snapshot should count as complete. | Pagination, total-count coherence, bounds, identity, retry policy. | Reject/degrade explicitly when the bounded complete snapshot cannot be acquired. |
| Repository-file/runtime evidence availability | **H (D acquisition + optional A fallback choice)** | Agent may see the unresolved proposition, source-unavailable reason, and a closed set of alternative read-only evidence sources. It may choose which admitted source to try next. | Exact locator, fetch execution, source identity, freshness, result parsing, evidence promotion. | If no admitted alternative can establish the fact, preserve unavailable/unresolved. |
| PyPI provenance / upstream repository identity | **D** | No model authority. A planner could choose another admitted provenance/source lookup, but the identity proposition itself remains deterministic. | Publisher provenance contract parsing, repository normalization, conflict/ambiguity detection. | Missing/ambiguous provenance remains unresolved; model confidence cannot substitute. |
| Changelog / upstream authoritative-source discovery | **H** | A bounded LLM/agent may propose likely documentation/release-source candidates or rank investigation value from model-visible descriptors, especially when names/locations are semantically variable. | Repository/source identity, admitted authority classes, exact path/tag/revision, source acquisition, final source admission. | Ambiguous authority remains unresolved; AI-selected text cannot self-authorize as authoritative. |
| Requirements dependency-transition extraction | **D** | None normally. | Patch/file identity, requirement parsing, exact version comparison, ambiguity rejection. | Unsupported edit shape remains explicit problem until real pressure justifies deterministic expansion. |
| Pyproject dependency-transition extraction | **D** | None for exact transition truth. LLM may later help candidate discovery from broader repository context, but not parse the authoritative dependency transition. | TOML/Requirement parsing, exact base/head comparison, source/group identity. | Unsupported specifier/direct-reference/multi-change forms remain unresolved rather than model-inferred. |
| uv lock structure / selected-root reachability | **D** | None for reachability truth. A planner may request missing target marker/environment inputs if those are separately acquirable. | Lock parsing, graph traversal, marker/fork handling, bounded universe/coverage. | Marker/fork or unsupported-binding ambiguity remains unresolved. Do not let an LLM “reason through” a graph and promote that to proof. |
| Direct project-environment selection | **D first; H for indirect mechanisms** | For direct pip/uv forms, none. For tox/nox/Make/custom scripts, a model may inspect bounded repository-owned script/config evidence and propose an environment-selection relationship or next evidence need. | Working-directory/source identity; supported direct selectors; grounding of any model-proposed relation; trusted environment-membership proposition. | If indirect semantics cannot be grounded, preserve unresolved. |
| Shell syntax family / parser selection | **D** | None. | Effective shell resolution, parser choice, parser-error policy. | Dynamic/custom shell identity remains unresolved/unsupported. |
| Dynamic command atoms / expressions | **D first; H when evidence must be acquired** | Agent may request exact matrix/env/config inputs. LLM is normally unnecessary for GitHub-expression mechanics; semantic assistance only becomes credible for repository-defined scripts/custom logic. | Expression/value resolution when supported, source identity, token interpretation. | Unknown material token stays dynamic/unresolved; no guessed literal. |
| Conditional / path-dependent command execution | **H — strong candidate** | Model/agent sees the exact unresolved execution proposition, structural predicate summary, known inputs, missing inputs, and admitted evidence actions. LLM may help understand repository-defined predicate scripts; agent may acquire missing inputs/log evidence. | Shell/control-flow semantics for admitted predicate classes; exact runtime input identity; action admission; final exact-command-executed proposition. | If branch execution cannot be proven, retain static occurrence but no runtime promotion. |
| Short-circuit / pipelines / nested / later-chain execution | **D first; H fallback** | Usually no LLM. Agent may choose direct runtime evidence when structural inference is insufficient and such evidence is admitted. | Operator/position/status-contribution semantics and exact command identity. | Unsupported relation remains unresolved; do not use model intuition about shell behavior. |
| Static↔runtime workflow correlation | **D** | None for identity/correlation truth. | Workflow expansion/correlation, matrix/reusable-workflow identity, step matching, revision/attempt identity. | Ambiguous or missing correlation remains unresolved. |
| Checkout / working-directory / repository-root provenance | **D** | Agent may acquire referenced workflow/action/config evidence if explicitly needed, but model does not own the path proposition. | Precedence, path normalization, repository identity, checkout semantics for admitted forms. | Dynamic/ambiguous provenance remains unresolved. |
| Package-manager operation declaration | **D** | None. | Parser-neutral command atoms → exact admitted operation declaration. | Unsupported manager/option/form remains explicit problem; no semantic guessing. |
| Effective package-manager semantics | **H — deterministic semantics + agentic evidence acquisition** | Agent may see which semantic dimension is blocked and which lower-precedence evidence source is missing: process env, config, executable/default provenance. It may choose the next admitted read. LLM is normally low-value unless custom tooling/config semantics are irreducibly semantic. | CLI/env/config/default precedence, exact values, semantic-fact state and provenance. | If a material lower-precedence source cannot be resolved, fact stays unresolved. |
| Runtime dependency-state proof | **H, with deterministic proof authority** | Agent may choose between command-derived evidence and justified fallback runtime/log/artifact evidence. Model may prioritize which evidence closes the exact state gap. | Exact command execution, effective package semantics, requirement/version/source identity, package-state witness composition. | No exact witness → no “proposed version present” claim. |
| Target CI environment interpretation | **D first; H for custom/indirect setup** | Agent may acquire matrix/container/action/config evidence. LLM may help interpret custom repository setup/action prose only as a candidate relation. | Job identity, matrix/container/setup-python/environment facts, exact target proposition. | Ambiguous target environment remains unresolved. |
| Target Python declaration/comparison | **D** | None. | Exact pyproject declaration parsing and deterministic supported specifier comparison. | Unsupported comparison stays unresolved even if a model says it is obvious. |
| Artifact serviceability / wheel compatibility | **D** | None for wheel/tag compatibility. | Exact release artifact inventory, filename/tag parsing, target compatibility sets. | Missing compatible wheel does not become “installation fails”; source fallback remains a separate proposition. |
| Broad technical-impact candidate discovery | **H — strongest LLM/semantic candidate** | Model may receive a deliberately bounded combination of exact transition, authoritative upstream semantic evidence, selected target structural/context evidence, current candidate set, and coverage state. It may propose one or more structured mechanism candidates and discovery reasons. Agent may iteratively inspect additional target/upstream evidence when candidate discovery is materially incomplete. | Source identity, evidence authority, grounding, candidate schema, dedup/lineage, proposition state, discovery-coverage constraints. | Model-generated candidate remains hypothesis/structured candidate; model cannot declare it applicable or discovery complete. |
| Repository-purpose / policy / provenance context discovery | **H — strong LLM candidate** | LLM may interpret README/docs/config/comments that express reproducibility, archival, compatibility, release, or operational intent and propose structured context claims with source refs. Agent may locate additional relevant repository-owned context. | Exact source/revision, context claim grounding, conflict preservation, decision-effect admission. | If purpose/policy is ambiguous or contradictory, preserve ambiguity; do not infer maintainer intent from weak prose. |
| Coordinated package-family / platform-family reasoning | **H** | LLM may interpret official compatibility prose/tables where semantics are heterogeneous; agent may acquire the exact family metadata/docs. | Exact package/release/platform identity, deterministic version/artifact relations where machine-readable, grounding of semantic family claims. | Unverified family coherence remains unresolved; no package-family conclusion from one model narrative. |
| Persisted-state / producer-version applicability | **H** | LLM can interpret authoritative persistence contracts and target producer/consumer semantics; agent may inspect artifact/config/deployment evidence when an admitted source exists. | Exact target/source identity, persisted-artifact relation, producer-version evidence, actual artifact-history admission. | Arbitrary deployment artifact history may remain genuinely unknowable; do not invent it. |
| Discriminating targeted-check derivation | **H / A — strong agentic candidate** | Model sees unresolved proposition, activating target path, current evidence, admissible observation families, costs/risks, and may propose the smallest check plus expected discriminating outcomes. | Check catalog/boundary, security and mutation policy, command/action binding, execution admission, observation interpretation. | If no admissible check can materially discriminate the proposition, stop unresolved rather than recommend generic “test more”. |
| Adaptive multi-step investigation | **A — strongest agentic responsibility** | Model sees typed investigation state, consumed actions, remaining budget, allowed action descriptors, material unresolved/conflicted propositions, and chooses one next action or justified stop. | Closed action catalog, exact locators, freshness/rebind, budget, execution, result interpretation, state transition/replay. | Invalid/stale/unauthorized choice is rejected deterministically; no-action/unresolved is a valid endpoint. |
| Candidate path-model / discovery-coverage challenge | **H, but AI cannot certify completeness** | A model can act as a challenger: propose omitted alternative activation paths/candidates from bounded evidence and explain why they may matter. | Coverage state, candidate/path identity, acceptance of any new path/candidate, negative-inference permission. | Absence of model suggestions never proves completeness; confidence cannot close open-world coverage. |
| Overall evidence sufficiency / maintainer-action permission | **D authority; optional H synthesis later** | A model may eventually see a semantic decision bundle and deterministic permission envelope. It may choose/prioritize among already-permitted actions/reasons if comparison evidence justifies this. | Action-specific permission, prohibited actions, mandatory uncertainty/conflict/checks, claim limits. | If no non-abstention permission is proven, emit abstain regardless of model preference. |
| Cross-evidence synthesis / maintainer explanation | **H — strong bounded LLM candidate** | LLM may rank decisive vs supporting reasons, choose among already-permitted actions, preserve residual uncertainty, and draft maintainer-facing explanation from evidence references. | Permission envelope, citation existence, mandatory uncertainty/check inclusion, prohibited-claim validation. | Invalid synthesis is rejected/falls back to deterministic baseline; model cannot widen permission. |
| Persistence / replay / recovery | **D** | Models may consume replayed state for evaluation, but should not own storage identity or recovery semantics. | Durable evidence IDs/content hashes, checkpoints, idempotence, supersession/staleness, deterministic replay. | Corrupt/incomplete replay remains explicit failure. |
| Evaluation / model quality judging | **D foundation + limited L supplement** | LLM-as-judge may assist qualitative semantic review only after deterministic metrics, frozen cases, oracle isolation, and human review boundaries exist. | Dataset partitioning, ground truth/oracle protection, deterministic authority violations, reproducibility, final adoption gate. | Self-judging or contaminated evaluation cannot justify adoption. |
| Dynamic / behavioral execution | **D execution + A selection; U when unjustified** | Agent may propose/select an admitted sandboxed check when it is decision-discriminating. LLM may help formulate the semantic check but does not gain shell authority. | Security policy, exact command/action binding, isolation, credentials/network/mutation limits, execution, observation validation. | Unsafe, unaffordable, non-discriminating, or unauthorized execution is not performed; question may remain unresolved. |

### 15.4 The main architectural pattern by layer

Step 2 suggests that UpgradePilot should not have one generic “AI layer”. It has at least four materially different intelligence roles.

#### Role 1 — bounded semantic extractor

Use when:

```text
authoritative text/source exists
+
the difficult part is software meaning in natural language
```

Examples:

- current upstream Python-support-drop extraction;
- future compatibility/configuration/persistence semantic claims;
- some repository-purpose/context interpretation.

Architecture:

```text
trusted bounded source
→ semantic model
→ structured candidate
→ grounding / deterministic validation
→ trusted claim or explicit unresolved
```

The model owns **interpretation**, not source authority.

#### Role 2 — candidate-discovery reasoner

Use when:

```text
the system must discover which technical mechanisms deserve consideration
```

Examples:

- S010-style multiple mechanism discovery;
- repository-purpose/context candidates;
- target-driven API/config/build/install surface discovery.

Architecture:

```text
trusted transition + selected source/context evidence
→ bounded model discovery
→ structured candidate(s)
→ deterministic source/evidence binding
→ independent applicability evaluation
```

The model owns **proposal breadth/semantic search**, not applicability or completeness.

#### Role 3 — EvidenceGap / targeted-investigation planner

Use when:

```text
one or more material propositions remain non-final
+
several independently useful evidence actions exist
+
their relative value depends on current state
```

Architecture already experimentally proven:

```text
typed trusted investigation state
→ bounded model action choice / stop
→ deterministic fresh admission
→ exact read-only or otherwise admitted effect
→ deterministic evidence interpretation
→ new typed state
→ repeat only while justified
```

The model owns **selection/sequencing**, not execution authority.

#### Role 4 — bounded decision/report synthesizer

Use only after:

```text
technical evidence exists
+
deterministic action-specific permission semantics exist
```

Architecture:

```text
trusted DecisionEvidenceBundle
→ deterministic PermissionEnvelope
→ bounded LLM synthesis
→ deterministic validation
→ maintainer-facing report
```

The model owns **cross-evidence prioritization/explanation** and possibly selection among already-permitted alternatives, not permission itself.

### 15.5 Responsibilities where AI should normally stay out

Step 2 identifies a substantial deterministic core that should remain boring and strong:

```text
repository / PR / revision identity
provider snapshot coherence
path normalization
exact dependency version parsing/comparison
requirements/TOML structure
uv lock structural/reachability proof
shell parser selection
static/runtime identity correlation
package-manager operation identity
CLI/env/config precedence rules
exact target Python comparison
wheel/tag compatibility
provenance admission
evidence-state promotion
action execution admission
maintainer-action permission
persistence/replay identity
security/mutation policy
```

Adding an LLM here would usually reduce inspectability without solving a semantic problem.

A future agent can **request** some of these deterministic capabilities as tools. That does not convert the underlying responsibility into an AI responsibility.

### 15.6 Conditional-command case — Step-2 final classification

The original motivating example now has a concrete architecture.

#### Layer A — structural parse

```text
shell source
→ deterministic parser
→ conditional occurrence + predicate/control relation
```

**Mechanism:** D.

#### Layer B — simple supported predicate

Example:

```text
if matrix_python == "3.12"; then ...
```

If exact predicate inputs are known:

```text
predicate structure + exact values
→ deterministic predicate evaluation
```

**Mechanism:** D.

#### Layer C — missing predicate inputs

Example:

```text
predicate depends on env/config/result from prior step
```

Represent:

```text
ExactCommandExecutionGap(
    missing = exact predicate input / prior observation
)
```

Then:

```text
agent sees gap + allowed reads
→ selects one evidence action
→ deterministic acquisition
→ deterministic predicate evaluator retries
```

**Mechanism:** H with A for acquisition.

#### Layer D — repository-defined semantic predicate

Example:

```text
if ./scripts/should_install.sh; then ...
```

A model may help interpret the bounded script/config relationship or propose which inputs matter, but:

```text
LLM says "this script should return true"
!=
exact branch execution proven
```

Either deterministic evaluation or direct runtime evidence must establish the final execution proposition.

**Mechanism:** H.

#### Layer E — unavailable/unobservable runtime fact

If the required runtime input/result cannot be recovered:

**Mechanism:** U.

The correct result remains:

```text
static command exists
+
runtime path unresolved
→ no exact-command-executed promotion
```

### 15.7 Design implications for work happening on main

This analysis does **not** require the current Increment-2/Increment-3 deterministic route to stop or be redesigned around an agent framework.

Instead, when new product responsibilities are designed, preserve these seams where naturally justified:

1. **typed fact/proposition output** rather than opaque final booleans;
2. **explicit unresolved reason** naming what blocks stronger evidence;
3. **provenance/source identity** sufficient to re-fetch or challenge the fact;
4. **independent semantic dimensions** rather than one giant “safe/valid” object;
5. **closed action capability** when an evidence gap has an executable next step;
6. **model-visible projection separated from trusted internal state** if a model is later used;
7. **deterministic post-model validation/admission** before trusted-state change;
8. **replay/evaluation hooks** for any nondeterministic model decision that could affect investigation or output.

Do **not** pre-build generic model interfaces, tool registries, graph runtimes, middleware, or “AI-ready” string blobs merely because these seams may later be useful.

The correct current principle is:

> preserve semantic and authority seams now; instantiate AI machinery only when a real responsibility and comparative evidence justify it.

### 15.8 What should receive AI attention first?

This is a **product/engineering sequencing hypothesis**, not a new live plan.

#### Highest-value AI-shaped responsibilities

**A. Broad technical-impact candidate discovery**

Why:

- open-ended semantic search is intrinsic to the responsibility;
- S010 provides direct real-case pressure;
- deterministic metadata alone is unlikely to cover heterogeneous software changes;
- output can remain a structured candidate rather than trusted truth.

Preferred first comparison:

```text
transparent deterministic/keyword/structured baseline
vs
bounded semantic discovery model
```

Measure:

- materially relevant candidate recall on frozen cases;
- unsupported candidate rate;
- grounding/source traceability;
- candidate duplication/granularity;
- discovery-coverage honesty.

#### B. Discriminating investigation / EvidenceGap planning

Why:

- UpgradePilot already has a proven architecture and real LangGraph/ordinary-Python evidence;
- agent value becomes real once multiple independent product actions exist;
- state-dependent choice/sequencing is inherently agent-shaped.

Re-entry trigger remains the existing one:

```text
several real admitted actions
+
relative value/order changes with proposition state, failures, consumed history, or budget
+
fixed policy becomes brittle/combinatorial/contextual
```

Do not manufacture actions to meet the trigger.

#### C. Repository-context semantic discovery

Why:

- S009 proves that repository purpose/provenance can be materially relevant;
- this information is often expressed in prose, comments, docs, and heterogeneous config;
- bounded source-grounded semantic extraction is a natural fit.

It should likely feed candidate/context state, not final action authority directly.

#### D. Maintainer-facing synthesis/reporting

Why:

- heterogeneous evidence creates real semantic/presentation pressure;
- an existing bounded PermissionEnvelope design already protects action authority.

But sequencing should remain:

```text
deterministic non-abstention permission baseline
→ observed cross-evidence synthesis/report limitation
→ bounded LLM comparison
```

It should not be the first new AI integration merely because report generation is easy to demo.

### 15.9 AI areas that should wait

#### Conditional-command semantic assistance

Interesting and legitimate, but not necessarily the highest-value first AI expansion.

Most common conditional/operator forms should first be attacked with deterministic control-flow representation/evaluation or direct runtime evidence because those can produce stronger proof than model interpretation.

AI becomes useful mainly for:

- repository-defined predicate scripts;
- deciding which missing evidence to acquire;
- semantically complex indirect environment setup.

#### General package-manager semantic reasoning

Do not turn pip/uv semantics into model reasoning while explicit precedence/config rules can be represented deterministically.

AI may help later with arbitrary custom task-runner/config ecosystems, but only after direct deterministic families are insufficient in representative cases.

#### Multi-agent systems

No current evidence justifies multiple specialized autonomous agents as a product requirement.

A single bounded planner over deterministic capabilities is already enough to test the actual orchestration responsibility. Multi-agent designs should require a demonstrated coordination problem that one planner/tool loop cannot handle cleanly.

### 15.10 Adoption evidence required by AI role

#### Semantic extractor / discovery model

Require:

- frozen development vs protected evaluation separation;
- structured output contract;
- source-grounding / citation validation;
- unsupported-candidate / hallucination measurement;
- representative paraphrase and mechanism variation;
- deterministic baseline comparison;
- explicit rejection/defer threshold.

#### Investigation planner

Require:

- at least several independently useful real actions;
- frozen action catalog and hidden exact locators;
- deterministic stale-state/budget/policy admission;
- replayable transitions;
- protected cases where best next action varies by state;
- baseline policy comparison;
- zero authority/identity violations for adoption.

#### Decision/report synthesizer

Require:

- deterministic PermissionEnvelope;
- valid deterministic fallback;
- mandatory uncertainty/check/claim-limit validation;
- cross-mechanism protected cases;
- comparison on decision usefulness and explanation quality;
- no prohibited action/claim authority violations;
- evaluation not judged only by the same model family that generated the output.

### 15.11 Step-2 conclusion

The Step-2 classification supports a specific architecture thesis:

> UpgradePilot should mature as a **deterministic evidence and authority substrate with selectively embedded semantic models and agentic investigation loops**, not as either a purely hand-coded rule engine or an LLM-first autonomous agent.

More concretely:

```text
DETERMINISTIC CORE
identity
provenance
typed evidence
explicit proposition state
mechanical semantics
authority
admission
replay

        ↕ bounded contracts

LLM SEMANTIC COMPONENTS
meaning extraction
candidate discovery
repository-context interpretation
cross-evidence explanation

        ↕ bounded contracts

AGENTIC ORCHESTRATION
choose next admitted evidence action
adapt after results/failures
stop when further work is unjustified

        ↓

DETERMINISTIC TRUSTED-STATE UPDATE
```

The most important architectural property is therefore not “how much AI is used”.

It is:

> **whether every AI contribution has a precise semantic responsibility, explicit observation boundary, explicit authority limit, deterministic admission path, and evaluable failure mode.**

### 15.12 Step-2 status / next route

**Step 2: COMPLETE ENOUGH FOR DISCUSSION AND WHOLE-PIPELINE MAPPING.**

No product source/test, accepted specification, ADR, active plan, or `MEMORY.md` was changed.

The next planned responsibility from the original workstream is Step 3:

> walk the entire UpgradePilot pipeline from Dependabot PR input to final maintainer output and construct one coherent end-to-end architecture map showing where the Step-2 deterministic, LLM, agentic, hybrid, and intentional-unresolved responsibilities sit, how typed state flows between them, and which pieces are implemented / experimental / designed / future.

Before Step 3, discuss/challenge the Step-2 classifications with Ali rather than silently promoting them into accepted architecture.


## 16. Method correction — add independent/de-anchored architecture challenge before Step 3

Ali identified a methodological weakness in the original route: Step 1 and Step 2 were strongly conditioned by UpgradePilot's current specifications, ADRs, source boundaries, prior experiments, and product-simulation interpretations. Their conclusions are useful as **project-conditioned analysis**, but they do not independently validate the architecture.

That concern is accepted.

A new supporting plan now governs the correction:

`plans/AI_AGENTIC_ARCHITECTURE_INDEPENDENT_CHALLENGE_AND_COMPARISON_PLAN.md`

### 16.1 What was missing

The original route was:

```text
Step 1 — current limitation inventory
Step 2 — mechanism classification
Step 3 — whole-pipeline map
Step 4 — compare to existing UpgradePilot AI experiments
Step 5 — identify gaps
```

This route had no genuinely separate external architecture derivation. Even Step 4 remained internally anchored because it compared against UpgradePilot's own prior AI/agent experiments.

Therefore Step 3 is now blocked until an independent challenge is completed.

### 16.2 Revised route

```text
TRACK A — PROJECT-CONDITIONED
Step 1
current limitation/unresolved/deferred inventory
→ COMPLETE initial pass

Step 2A
current deterministic / LLM / agent / hybrid classification
→ COMPLETE initial pass


TRACK B — INDEPENDENT / DE-ANCHORED
Step 2B
start from product problem + externally necessary constraints
temporarily bracket current UpgradePilot architecture choices
research current external approaches broadly
derive multiple materially different candidate architectures
→ NOT STARTED


TRACK C — ADVERSARIAL COMPARISON
Step 2C
compare independently derived architectures against Track A
classify each current principle:
  independently supported
  too restrictive
  too permissive
  incomplete
  project-specific
  historical
  contradicted
  experiment required
→ BLOCKED BY 2B


Step 3
whole-pipeline architecture map
→ BLOCKED BY 2B + 2C

Step 4
reconcile independently identified needs with existing UpgradePilot experiments
→ BLOCKED BY Step 3

Step 5
select actual architecture/design changes, experiments, or explicit deferrals
→ BLOCKED BY prior steps
```

### 16.3 Independence protocol

Track B must not use current UpgradePilot method choices as premises.

It may retain the product problem and externally necessary boundaries:

```text
public Python OSS maintainer
dependency-update PR
trustworthy uncertainty-aware decision support
incomplete/conflicting external evidence
security/auditability requirements
human decision authority
```

But it must not assume in advance:

```text
deterministic code must own all trusted propositions
models should see only typed projections
agents must use closed action catalogs
current A→B→C reasoning spine is optimal
PermissionEnvelope is necessarily the right final-synthesis design
static analysis must precede model reasoning
current evidence-state vocabulary is optimal
LangGraph/LangChain are or are not appropriate
multi-agent systems are unnecessary
current package/CI decomposition is optimal
```

Those become hypotheses tested in Step 2C.

### 16.4 Independent research scope

Track B will deliberately research competing approaches including:

- dependency-update automation and software-supply-chain systems;
- change-impact analysis;
- static/program analysis;
- abstract interpretation and symbolic execution;
- CI/workflow simulation and observability;
- repository-scale code intelligence;
- LLM code reasoning;
- retrieval-augmented repository reasoning;
- tool-using software-engineering agents;
- debugging/investigation agents;
- verifier-guided LLM systems;
- LLM + executable sandbox designs;
- provenance/evidence graphs;
- planning/search for diagnosis;
- human-in-the-loop decision-support;
- multi-agent/specialist/debate approaches where evidence justifies consideration;
- model uncertainty, calibration, and evaluation methods.

The research must seek evidence **against** current UpgradePilot instincts as actively as evidence supporting them.

### 16.5 Required independent alternatives

Before reintroducing current UpgradePilot architecture, Track B must formulate credible materially different candidates such as:

```text
deterministic-heavy / formal-analysis architecture

LLM-first repository reasoner
+ deterministic/verifier guardrails

tool-using agent
+ sandbox / execution feedback

hybrid evidence-graph
+ semantic reasoning architecture

additional architecture discovered from research
```

These are comparison candidates, not required product directions.

### 16.6 Final comparison output required

Step 2C must produce a challenge matrix such as:

| Current principle / design choice | Independent evidence | External alternative | Disposition | Needed experiment/evidence |
| --- | --- | --- | --- | --- |
| deterministic authority for X | ... | ... | independently supported / too restrictive / etc. | ... |

The comparison must consider:

```text
correctness
coverage
uncertainty preservation
auditability
security
cost/latency
engineering complexity
maintainability
replay/evaluation
adaptability
maintainer usefulness
```

### 16.7 Terminology correction

Do not describe Track B as literally **unbiased**.

Because this investigation has already seen UpgradePilot's design, perfect blindness is impossible.

Use:

> **independent / de-anchored / adversarial external challenge**

The purpose is to reduce confirmation bias procedurally and make competing architectures receive fair consideration.

### 16.8 Current next step

The next analysis responsibility is now:

> **Step 2B — independent external research and architecture derivation.**

Do not proceed directly to the old Step 3 whole-pipeline map.


## 18. Research-program expansion checkpoint

Ali broadened the independent challenge beyond AI/agent architecture to cover adjacent products, tools, standards, evidence systems, workflow/runtime techniques, maintainer UX, and evaluation.

Controlling supporting plan expanded:
- `plans/AI_AGENTIC_ARCHITECTURE_INDEPENDENT_CHALLENGE_AND_COMPARISON_PLAN.md`

Pre-research discovery record:
- `working-memory/2026-09-29_external-research-area-discovery.md`

The earlier statement that Step 2B was complete enough for immediate Track C is superseded.

Current route:

```text
Step 2B-0  broad external area discovery             COMPLETE
Step 2B-1+ staged Tier-1 deep research reports       NEXT
Step 2B-X   refresh independent candidate architectures
Step 2C     adversarial comparison against Track A
Step 3      whole-pipeline architecture map
```

The first Tier-1 report should study the closest dependency-update products/workflows before judging architectural implications.


## 19. Tier-1 deep research progression

Tier-1 Report 01 is complete:

- `working-memory/2026-09-29_tier1-01_closest-dependency-update-products-and-workflows.md`
- Dependabot/dependabot-core
- Renovate/Mend Merge Confidence
- GitHub Dependency Review
- Updatecli

Key external pattern:

```text
mature updater products
→ excel at discovering, generating, grouping, routing and governing updates

security/dependency-review products
→ excel at dependency diffs + policy enforcement

repository CI
→ commonly remains a major target-validation signal

maintainer
→ still owns much of final target-specific compatibility judgment
```

Important architecture patterns captured for later comparison:

- ecosystem adapter contracts;
- Manager / Datasource / Versioning / Platform separation;
- use the real package-manager tool instead of reverse-engineering artifact updates when appropriate;
- declarative source → condition → target → SCM → action composition;
- revision-relative state invalidation;
- population risk signals separated from target-specific evidence;
- maintainer attention/approval/queue control as a product responsibility.

These are hypotheses for later Track C, not adopted UpgradePilot architecture.

Next: Tier-1 Report 02 — risk, reachability and upgrade-impact platforms.


## 20. Tier-1 Report 02 — risk, reachability and upgrade impact

Completed external deep report:

- `working-memory/2026-09-29_tier1-02_dependency-risk-reachability-and-upgrade-impact-platforms.md`
- Endor Labs
- Semgrep Supply Chain
- Snyk Open Source
- Socket

Material correction to the research thesis:

```text
"target-specific dependency impact analysis is largely absent"
→ FALSE / too broad
```

Modern platforms already provide important forms of:

- target + dependency call-graph reachability;
- vulnerable-function/data-flow prioritization;
- old→new dependency-version breaking-change analysis;
- first-party + third-party static analysis;
- LLM-assisted upgrade guidance;
- dependency behavior-delta detection;
- dependency-graph-aware remediation planning.

Important independent architecture evidence:

- Endor: call/context graph + version diff + upgrade blast-radius analysis;
- Semgrep: target static analysis + dependency-version static analysis → LLM breaking-change report;
- Snyk: program analysis + AI/NLP + call graph + human curation, with explicit `NO PATH FOUND != unreachable`;
- Socket: multi-strength reachability, human-verified vs AI-generated vulnerability specifications, package behavior delta, and fix planning.

Revised UpgradePilot product-space hypothesis:

```text
general dependency-update decision intelligence
across multiple impact/evidence mechanisms
+
CI/runtime/environment proof
+
explicit evidence gaps and adaptive investigation
+
repository-purpose/context
+
uncertainty-aware maintainer action
```

This remains a hypothesis, not an accepted product claim.

New questions preserved for later Track C include graph-native evidence, upstream source/API diffing, graded AI evidence authority, package behavior changes, and stronger distinction among no-path / unsupported / unresolved / proven non-applicability.

Next: Tier-1 Report 03 — remediation and migration engines.


## 21. Tier-1 Report 03 — remediation and migration engines

Completed:

- `working-memory/2026-09-29_tier1-03_remediation-and-migration-engines.md`
- OSV-Scanner Guided Remediation
- OpenRewrite / Moderne
- DepRepair / DepBench
- Griffe
- LibCST

Material research finding:

```text
impact/problem detection
!= remediation strategy selection
!= target-site localization
!= source/manifest transformation
!= graph/lock regeneration
!= validation
```

External architecture patterns:

- OSV-Scanner: multiple graph-level remediation strategies with explicit risk/change trade-offs and iterative graph recomputation;
- OpenRewrite/Moderne: type-attributed format-preserving semantic IR + composable/idempotent recipes + preconditions + dry-run/commit separation;
- DepRepair: distilled cross-repository evidence + usage localization + breakage-class guide → one bounded LLM repair call → executable oracle;
- Griffe: deterministic Python old/new API breakage candidates with explicit unsupported comparison classes;
- LibCST: Python format-preserving metadata-aware codemod substrate.

Important hypotheses preserved for Track C:

- deterministic recipes and generative repair may be complementary;
- known recurring migration → recipe/codemod;
- novel evidence-rich migration → bounded model repair;
- paradigm shift / weak evidence → interactive investigation or maintainer;
- analysis/evidence graph and mutation IR may need to remain distinct representations;
- upstream source/API diff deserves first-class investigation;
- mutation execution requires security/sandbox policy;
- executable success remains bounded by test/environment fidelity.

Next: Tier-1 Report 04 — dependency/evidence graph foundations + provenance standards.


## 22. Dual product-value + learning-exposure research rule

Ali explicitly expanded the research objective: interesting tools/methods should be evaluated not only for immediate UpgradePilot utility but also for deliberate transferable engineering exposure.

This is now formalized in:

- `plans/AI_AGENTIC_ARCHITECTURE_INDEPENDENT_CHALLENGE_AND_COMPARISON_PLAN.md`
- `working-memory/2026-09-29_research-technology-learning-exposure-ledger.md`

Future research reports must separately evaluate:

```text
A. product / architecture value
B. learning / career exposure value
```

Important boundary:

```text
researched
!= hands-on experience
!= project integration
!= validated/operated experience
```

The goal is to deliberately create bounded real experiments when a technology offers strong transferable learning value, while keeping product adoption evidence-driven.

Current high-interest exposure candidates include Griffe, LibCST, Semgrep, CodeQL, GUAC, SLSA/in-toto/SPDX/CycloneDX, OSV-Scanner Guided Remediation, StepSecurity/zizmor/actionlint, Joern, and bounded symbolic-execution tools.


## 23. Tier-1 Report 04 — dependency/evidence graphs + provenance standards

Completed:

- `working-memory/2026-09-29_tier1-04_dependency-evidence-graphs-and-provenance-standards.md`
- deps.dev / Open Source Insights
- GUAC
- OSS Review Toolkit
- SPDX 3.0.1
- CycloneDX 1.7
- SLSA 1.2
- in-toto Attestation Framework v1.2
- Sigstore/Cosign
- GitHub artifact attestations and dependency submission

Most important correction:

```text
"UpgradePilot must invent its own evidence/provenance vocabulary"
→ too strong
```

External standards already represent important concepts such as:

- dependency graphs and requirements/resolution distinction;
- explicit relationship completeness;
- explicit no-assertion vs known-none;
- build inputs/outputs/tools/agents;
- evidence method + tool + confidence;
- source occurrences and call stacks;
- claims/counterclaims/assessors/citations;
- process formulation;
- signed subject-bound attestations;
- producer precedence and revision-bound dependency snapshots.

But none provides UpgradePilot's actual domain reasoning:

```text
static vs runtime execution
package-manager semantic precedence
target-specific applicability
CI proof sufficiency
adaptive investigation
cross-mechanism evidence sufficiency
maintainer-action permission
```

Current research hypothesis:

```text
UpgradePilot domain-specific internal model
+
standards-aware adapters / export / import / attestations
```

rather than either a fully isolated custom universe or a standards-native internal model.

Important learning/exposure candidates added/refined:

- deps.dev API;
- GUAC + GraphQL + Docker Compose;
- CycloneDX 1.7 evidence/declarations;
- SPDX 3.0.1 relationship/build semantics;
- SLSA + in-toto + Sigstore/GitHub artifact attestations;
- ORT as a full SCA/policy/report pipeline comparator.

Next: Tier-1 Report 05 — CI/runtime evidence + program-analysis techniques.
