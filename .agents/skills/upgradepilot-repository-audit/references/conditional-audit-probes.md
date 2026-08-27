# Conditional Repository-Audit Probes

Use this reference only when the main Repository-Audit Skill identifies one of the two conditional audit pressures below.

This file is **procedural and non-controlling**. `OPERATING_GUIDE.md` remains the owner of project-wide reasoning, proportionality, evidence interpretation, and Source Clarity outcomes. The Naming Clarity specification remains the naming/terminology owner. Root governance and normal responsibility owners retain their existing authority.

Apply only the probe family relevant to the selected audit question. Do not treat this file as a universal checklist, and return to the main Audit procedure after applying the relevant probes.

## 1. Source-Clarity and maintainability probes

Use this family when source readability/maintainability is materially part of the audit and the compact Source Clarity outcomes are not enough to inspect the specific ambiguity.

Review outcomes, not comment volume. Useful optional probes include:

- **Reader orientation / primary API** — can a new maintainer identify the component responsibility, deliberate exclusions, and main semantic entry point without prior chat?
- **Bidirectional cross-file flow** — can important inputs/evidence be traced upstream to their origin/meaning and downstream through transformation and handoff?
- **Representative data shapes** — when type names/signatures are insufficient, is the important shape/meaning of inputs and outputs recoverable without implying one fixture is the whole supported domain?
- **Material constants, regexes, sentinels, and domain vocabulary** — is their project-specific semantic role clear where misunderstanding would change behavior or maintenance decisions?
- **Decision-boundary why-comments** — do non-obvious rejects, abstentions, precedence rules, conservative branches, and evidence-source preferences explain the ambiguity/failure mode they prevent rather than narrating syntax?
- **Guard clauses as permissions/invariants** — when guards form an evidence or proof ladder, is it clear both why failure stops and what successful passage allows later code to trust?
- **Semantic/proof transformations** — when evidence is parsed, normalized, filtered, correlated, narrowed, promoted, or aggregated, is it clear what information/authority is retained, removed, strengthened, weakened, or deliberately not inferred?
- **Meaningful algorithms/control flow/data structures** — where an implementation mechanism encodes a project invariant or ambiguity-handling strategy, is the semantic reason recoverable?
- **Terminology collisions** — are similar terms disambiguated where confusion could change interpretation?
- **Current / transitional / legacy visibility** — when surfaces coexist, can a maintainer tell what is current, what remains for compatibility/migration, what still depends on it, and any known removal trigger?

Names and structure should carry responsibility before comments compensate for vague ownership. Do not create an architecture essay for a small clear file or turn a bounded audit into a repository-wide documentation campaign.

## 2. Governance-system quality probes

Use this family only when governance, agent controls, Skills, specifications/plans as a governance system, or the governance evaluation harness itself is materially under audit.

Inspect proportionately:

- **Canonical semantic ownership** — is each durable rule owned by the correct canonical artifact rather than independently redefined across several controls?
- **Deliberate reinforcement** — when a high-salience rule is repeated, does the reinforcement point back to the owner and preserve rather than subtly alter its meaning?
- **Activation and context cost** — is operation-specific procedure kept out of always-loaded context when progressive disclosure can preserve behavior more cheaply?
- **Routing distinctness** — are operation/Skill boundaries clear enough to avoid unnecessary loading or skill-shadowing/collision?
- **Live-state leakage** — has current continuation, dated status, or lifecycle state leaked into a durable non-state owner?
- **Control versus implementation proof** — is documentation/governance intent being mistaken for executable behavior or runtime validation?
- **Deterministic enforcement opportunities** — are objective repeated invariants enforced mechanically where a low-noise checker is appropriate?
- **Semantic judgment boundary** — are fuzzy engineering/governance judgments left to evidence-backed reasoning instead of brittle regex or mechanical linting?
- **Behavioral regression coverage** — do high-risk routing/action-boundary failures have discriminating behavioral cases, including both positive and negative trigger paths when relevant?
- **Persistent agent machinery** — do new Skills, adapters, hooks, client-specific metadata, or other agent infrastructure have a demonstrated recurring responsibility and a simpler-baseline check?

Do not interpret every governance difference as duplication or every repeated instruction as waste. Preserve justified high-salience reinforcement and distinguish structural/objective checks from semantic judgment.
