---
name: upgradepilot-working-memory
description: Maintain UpgradePilot session working memory as a compact support workflow: create or continue the right dated record, progressively preserve the meaningful engineering evolution of the active responsibility, link related records, maintain time-scoped handoff state, and reconcile MEMORY.md when live project position changes. Use when Ali asks to create/update working memory or an active substantive session intentionally maintains one.
---

# UpgradePilot Working Memory

Use this Skill as the compact **support/composition procedure** for `working-memory/`.

**Skill provenance marker:** `UP-SKILL:upgradepilot-working-memory`

This is **not a primary operation mode** and does not authorize Build, Audit, Planning, Learning-Only, external actions, or other work. The active primary operation keeps its own procedure and action boundary.

`working-memory/README.md` is the canonical owner for working-memory meaning, authority, naming, structure, linking, safety, and the progressive-preservation model. This Skill applies that owner without duplicating it.

## Activate proportionately

Use this Skill when:

- Ali explicitly asks to create, start, update, or close a working-memory record;
- a session already has an active working-memory record that should be maintained progressively;
- a material stopping point needs a detailed dated handoff/context record.

Once active for a session record, keep using the same procedure for ordinary updates. **Do not reload/re-route the Skill for every append.**

## 1. Re-anchor only what is needed

For a new or resumed session, normally inspect:

```text
current MEMORY.md
→ selected plan/owner needed for this responsibility
→ latest directly relevant working-memory record(s)
→ current session evidence as work proceeds
```

Do not scan the full working-memory history. If Ali gives only an old clue, search by likely date/scope/error/concept/keyword and follow relevant links.

## 2. Choose NEW vs CONTINUE

Prefer **NEW** when Ali asks for a new session/day/time record, the responsibility materially changes, or a separate record improves retrieval.

Prefer **CONTINUE** when the same session/responsibility/investigation is still active and the existing record remains clear.

Multiple records on one day are allowed. Do not create a new record merely because another small command or edit occurred.

## 3. Start a new record compactly

Use the naming guidance from `working-memory/README.md`, normally:

```text
YYYY-MM-DD_HHMM_<scope-or-step>_<short-topic>.md
```

Seed only what helps the session:

```text
identity / links
→ starting point
→ session goals
→ selected near-term plan steps
→ temporary session rules/boundaries
→ initial route
```

Restating a few plan steps for today's focus is allowed; clearly treat them as **session focus**, not a replacement plan.

When the new record directly continues another, link back to it. If the older record still looks `ACTIVE` or has an unqualified handoff that would now mislead, minimally mark it `CONTINUED` or `SUPERSEDED` and add `Continued by: <new record>`. Otherwise leave history untouched.

## 4. Preserve the meaningful progression, not the activity stream

At meaningful points, append or refine the record so the **engineering evolution of the active responsibility can be reconstructed accurately**.

Use this mental model:

```text
starting state / assumptions / questions
→ decisions and reasoning
→ bounded work performed
→ observations and evidence
→ discoveries / failures / surprises
→ diagnosis / correction / changed understanding
→ alternatives / deferred ideas
→ changed route when applicable
→ resulting state / proof limits / handoff
```

Typical material includes:

- decisions and why they were made;
- user-defined session rules or changed constraints;
- implementations/analyses completed and what they actually established;
- important observations, errors, failed attempts, surprises, diagnosis, and repair;
- important questions, corrected assumptions or mental models, ideas, alternatives, and deferred changes;
- validation performed/unavailable and proof limits;
- changed assumptions, understanding, or session route;
- exact names/files/error phrases, subtle implementation/API/tool behavior, or other distinctive details that help reconstruct how the result was reached.

Do not make the agent repeatedly classify every detail as “handoff-critical” or “educational enough” before preserving it. If a locally small but distinctive event contributes to the real engineering story and would be hard to recover later, a concise sentence is enough.

At the same time:

```text
complete enough engineering progression
!=
complete activity log
```

Do **not** dump the chat, every command, every ordinary edit, repeated safe operations, or large logs. Summarize routine activity and link/reference large or canonical artifacts.

Working memory may later provide historical/rationale evidence for audits, reviews, and Learning-Artifact authoring. Preserve the real path accurately enough for those later consumers, but do not turn the record itself into a tutorial, study guide, or second `learning/` artifact.

## 5. Keep the route usable

Maintain a short current-session route when useful.

If the route changes, make the current route accurate. Preserve the previous route only when the change/reason matters historically. Do not leave several conflicting `next steps` looking simultaneously active.

Temporary session rules stay session-local unless separately promoted to the correct durable owner.

## 6. Stop / handoff

When pausing or closing, preserve proportionately:

```text
what was completed / established
→ exact stopping point
→ unresolved / deferred / blocked items
→ material proof and non-proof
→ intended next steps as of this stopping point
→ useful links
```

Time-scope the handoff. A future session must reconcile it with current `MEMORY.md`, the controlling plan/owners, and newer evidence before treating it as current.

If live project position materially changed, update `MEMORY.md` separately. The working record keeps the detailed context; `MEMORY.md` keeps the compact canonical current position.

## 7. Preserve authority boundaries

Working memory may preserve reasoning, chronology, session focus, and a detailed dated handoff. It must not independently redefine:

- accepted product semantics;
- architecture/method decisions;
- plan authority;
- current live project position;
- authorization to perform new work.

Promote stable reusable conclusions to the correct owner when warranted; keep the working record as provenance rather than rewriting its history.

## Provenance

When this full Skill is materially used and a normal handoff surface exists, emit:

```text
UP-SKILL:upgradepilot-working-memory
```

Do not create a record solely to preserve the marker.
