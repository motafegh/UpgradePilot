# 05 — Design Reasoning and Trade-offs

## Learning target

After this note, you should be able to defend the current design without saying only
“because the code does it this way.” For each important choice, explain:

```text
responsibility
→ chosen mechanism
→ failure it prevents
→ alternative not chosen
→ remaining cost or limitation
→ evidence that would justify revisiting it
```

This is the reasoning pattern expected when reviewing future AI-generated code.

## How to use this note

Do not memorize every card. Select the cards that correspond to the source you are tracing.
For each selected card, close the file and reconstruct the five-part reasoning chain.

# Decision cards

## 1. Start with a manual repository and PR locator

**Choice**

The current interface accepts `owner/repository` and a positive PR number through the CLI.

**Why this was chosen**

It is the smallest real input that reaches a public pull request without requiring webhook
hosting, event authentication, queues, or repository installation. It lets the project learn
the complete evidence path before automating the trigger.

**Alternative not chosen**

A GitHub App or webhook could start automatically when a PR opens. That would add deployment,
secret handling, event-delivery reliability, and replay concerns before the evidence logic is
owned.

**Cost or limitation**

Invocation is manual and does not yet model event delivery or repeated updates to a PR.

**Revisit when**

The manual vertical slice is owned and the next authorized responsibility requires automatic
or repeated invocation.

## 2. Acquire PR metadata before changed files

**Choice**

UpgradePilot first acquires `PullRequestIdentity`, including base SHA, head SHA, and expected
changed-file count, then requests changed-file records.

**Why this was chosen**

The metadata establishes which exact proposal is being observed and supplies the count used to
check later acquisition completeness. Without that anchor, changed-file records would not be
bound to a verified proposal identity.

**Alternative not chosen**

The program could request changed files first and infer the PR only from the endpoint path.
That would provide file content without an independent proposal identity or expected count.

**Failure prevented**

Evidence from an older or different PR head cannot silently support the current proposal, and
partial file acquisition cannot be mistaken for the complete change set.

**Cost or limitation**

The path requires at least two API operations instead of one.

**Revisit when**

A future GitHub response or authenticated event supplies equivalent exact identity and
completeness evidence in one trustworthy object.

## 3. Bind evidence to base and head SHAs

**Choice**

The identity records both the exact base commit and exact proposed head commit.

**Why this was chosen**

A pull request number is stable while its head can change after new commits are pushed. The SHA
is the immutable revision identifier needed for later CI and upstream evidence.

**Alternative not chosen**

Using branch names or PR number alone is simpler, but both can refer to different content at
different times.

**Failure prevented**

A successful check or dependency observation from one revision cannot be attributed to a newer
revision merely because the PR number is unchanged.

**Cost or limitation**

Later evidence sources must also expose or be reconciled to the same head SHA.

**Revisit when**

Do not remove this invariant. Only change its representation if a stronger immutable proposal
identity is introduced.

## 4. Use one small read-only GitHub client

**Choice**

`GitHubReadClient` performs only public read operations needed by the current slice.

**Why this was chosen**

Read-only scope minimizes credentials, permissions, security risk, and accidental effects on a
target repository. A small client keeps the external trust boundary visible and testable.

**Alternative not chosen**

A full GitHub SDK or write-capable integration would provide more features but would enlarge the
dependency, permission, and behavioral surface before those features are required.

**Cost or limitation**

The client currently implements only the endpoints and response shapes needed by B2.

**Revisit when**

Several authorized GitHub responsibilities create repeated protocol code that a maintained SDK
would simplify enough to outweigh its dependency and abstraction costs.

## 5. Use Requests with an injectable Session

**Choice**

The client uses `requests.Session`, with the session optionally supplied to the constructor.

**Why this was chosen**

Requests offers direct, readable HTTP behavior with mature timeout and exception handling. An
injected session allows deterministic tests to replace the network collaborator without
patching global functions.

**Alternatives not chosen**

- `urllib.request` would avoid a dependency but would require more low-level error and response
  handling for this learning slice.
- A larger async or generated GitHub client would add concepts and abstraction not required by
  the current synchronous command.
- Patching `requests.get` globally would make tests more coupled to implementation details.

**Cost or limitation**

Requests is an admitted runtime dependency, and the current interface remains synchronous.

**Revisit when**

Concurrency, streaming, a broader API surface, or dependency policy creates a demonstrated need.

## 6. Use explicit connect and read timeouts

**Choice**

Every request receives a tuple containing a connection timeout and response-read timeout.

**Why this was chosen**

A network call without a timeout can block the CLI indefinitely. Separating connection time from
read time reflects two different waiting phases and produces a bounded user-visible operation.

**Alternative not chosen**

Using Requests defaults would be shorter, but the default has no timeout. One scalar timeout is
acceptable but less explicit about the two phases.

**Cost or limitation**

The selected values are practical defaults, not yet tuned through production measurements.

**Revisit when**

Observed latency, rate limiting, or deployment conditions provide evidence for different values
or retry behavior.

## 7. Separate transport, HTTP, response, and evidence failures

**Choice**

The client distinguishes input rejection, transport failure, HTTP refusal, malformed successful
content, and contradictory evidence.

**Why this was chosen**

These failures have different causes and different corrective actions. A timeout suggests a
network problem; a non-array `200` suggests a response-contract problem; a count disagreement
suggests incomplete evidence.

**Alternative not chosen**

One generic `GitHubError` would reduce classes and branches, but it would destroy diagnostic and
product meaning.

**Failure prevented**

The CLI does not tell the user that a valid but unsupported dependency shape is a network error,
or that a malformed response is merely “not supported.”

**Cost or limitation**

Callers must handle several explicit categories.

**Revisit when**

New categories are added only when they change user action, product claims, or recovery behavior.
Do not split categories merely for taxonomy detail.

## 8. Convert untrusted JSON into immutable records

**Choice**

External mappings are validated field by field and converted to frozen, slotted dataclasses.

**Why this was chosen**

The broad JSON shape is appropriate at the network boundary, but later logic should operate on
small records whose required fields and types are already established. Immutability reduces the
chance that validated identity or evidence is changed accidentally after acquisition.

**Alternative not chosen**

Passing raw dictionaries through every layer is shorter initially but repeats validation,
encourages string-key errors, and makes trusted versus untrusted states unclear. A larger
validation framework was unnecessary for the current small contracts.

**Cost or limitation**

Validation helpers are handwritten and must be extended carefully as fields are added.

**Revisit when**

Contract count, nesting, serialization, or cross-field validation becomes large enough that a
framework provides clear net value.

## 9. Request 100 files per page and reconcile the final count

**Choice**

Changed files are requested in pages of 100, and the final validated record count must equal the
count in `PullRequestIdentity`.

**Why this was chosen**

A larger permitted page size reduces network round trips. The final count check is the actual
completeness proof; a short page alone is only a pagination signal.

**Alternatives not chosen**

- Reading only the first page is simpler but silently truncates larger PRs.
- Trusting only “page length < 100” cannot detect all contradictory or incomplete responses.
- Building a generic pagination framework would be premature for one endpoint.

**Failure prevented**

Dependency extraction cannot analyze the first valid record while silently missing another
changed file that could make the proposal ambiguous or unsupported.

**Cost or limitation**

The current method rejects PRs beyond the endpoint's complete-acquisition boundary and has no
resume or retry support.

**Revisit when**

Another authorized endpoint needs the same pagination behavior or live evidence shows a need for
retries, link-header traversal, or resumable acquisition.

## 10. Preserve `patch=None` and verify patch counts

**Choice**

A changed-file record may contain `patch=None`. When patch text exists, visible additions and
deletions must agree with GitHub's per-file counts before extraction trusts it.

**Why this was chosen**

A file record can be valid even when line-level patch evidence is unavailable. Preserving absence
keeps the evidence honest. Count reconciliation helps detect truncated or incomplete patch text.

**Alternatives not chosen**

- Converting absence to an empty string would erase the difference between “no patch supplied”
  and “a complete patch with no lines.”
- Parsing whatever fragment is visible would produce confident findings from incomplete evidence.

**Cost or limitation**

Some real dependency updates will be classified as unsupported even though a human could obtain
more evidence through another endpoint or a checkout.

**Revisit when**

A later authorized acquisition mechanism can retrieve exact file blobs or full diffs and bind
them to the same head SHA.

## 11. Keep acquisition and extraction in separate modules

**Choice**

`github_client.py` acquires and validates external evidence. `dependency_change.py` interprets
already validated records without network I/O.

**Why this was chosen**

The two responsibilities have different failure semantics and testing needs. Pure extraction
can be tested with small deterministic values, while acquisition tests focus on HTTP contracts
and completeness.

**Alternative not chosen**

One method could request pages and parse dependency lines at the same time. That would be fewer
functions, but partial evidence, network errors, and unsupported syntax would become entangled.

**Failure prevented**

A syntax outside the supported grammar cannot be reported as an acquisition failure, and a
network failure cannot accidentally become an unsupported dependency result.

**Cost or limitation**

The program contains more explicit types and hand-off points.

**Revisit when**

The boundary should remain. Internal function placement may change only if responsibilities stay
separate and tests preserve their failure meanings.

## 12. Return unsupported as data, not as an exception

**Choice**

The extractor returns either `PinnedDependencyChange` or `UnsupportedDependencyChange`.

**Why this was chosen**

Unsupported evidence is an expected product outcome: the external data may be valid while its
meaning is outside the current proven scope. Expected abstention should be representable,
printable, and testable without using exception control flow.

**Alternative not chosen**

Raising an exception for every unsupported case would make ordinary abstention look like a
system defect. Returning `None` would discard the reason and reduce diagnosability.

**Cost or limitation**

Every caller must branch on the result type and preserve the reason correctly.

**Revisit when**

More result states may justify a richer result model, but unsupported evidence should remain an
explicit normal state rather than becoming a guessed answer.

## 13. Support only exact pinned requirement replacements

**Choice**

The current grammar recognizes one removed `package==old_version` line and one added
`package==new_version` line.

**Why this was chosen**

This is the smallest dependency-update form that is precise enough to identify package, old
version, and proposed version deterministically from a patch. It matches the selected public
case without hardcoding that case.

**Alternatives not chosen**

- Accepting `>=`, compatible-release operators, extras, markers, URLs, editable installs, or
  multiline forms would require broader packaging semantics and more ambiguity controls.
- Using a full requirement parser could parse more syntax, but it would not by itself establish
  that a removed and added expression represent one safe version update.
- Heuristically choosing one pair among several candidates would hide ambiguity.

**Cost or limitation**

Many valid Python dependency declarations remain unsupported.

**Revisit when**

A new real case and bounded product need justify one additional syntax form, with explicit
semantics and tests before activation.

## 14. Normalize package names before identity comparison

**Choice**

Runs of `.`, `_`, and `-` are converted to `-`, and names are lowercased before comparison.

**Why this was chosen**

Python distribution names can use different spellings that identify the same normalized
package. Raw string equality would incorrectly classify `demo.package` and `demo_package` as
different dependencies.

**Alternative not chosen**

Comparing raw names is simpler but wrong for the package identity rule. Normalizing versions as
well was not added because version interpretation is a separate responsibility.

**Cost or limitation**

Normalization establishes package identity only; it does not prove package authenticity,
version ordering, compatibility, or safety.

**Revisit when**

The rule changes only with an authoritative packaging requirement or a demonstrated edge case.
The next Ali-owned test protects this boundary.

## 15. Combine deterministic tests with one live smoke run

**Choice**

The current proof uses mocked deterministic tests plus a real public GitHub command.

**Why this was chosen**

Mocks provide repeatable control over rare or malformed responses. The live run verifies that
the installed package, actual network, GitHub endpoints, and real response shape work together
for one observed case.

**Alternative not chosen**

- Live-only tests would be slow, rate-limit-sensitive, and unable to reproduce every failure.
- Mock-only tests could pass while the real endpoint, headers, installation, or response shape
  is wrong.

**Cost or limitation**

One live case does not prove broad compatibility, production reliability, or recommendation
correctness.

**Revisit when**

Captured-response fixtures, contract tests, or additional live smoke cases are authorized by a
specific robustness need.

## 16. Defer retry, persistence, replay, CI, and recommendation logic

**Choice**

The current increment stops after exact dependency identity and explicit unsupported output.

**Why this was chosen**

Each deferred capability introduces a separate responsibility and new failure modes. Adding them
before the acquisition and extraction boundary is understood would increase ceremony and blur
which evidence supports which conclusion.

**Alternative not chosen**

Building a complete platform immediately might look more impressive, but it would make learning,
diagnosis, and evidence attribution substantially weaker.

**Cost or limitation**

UpgradePilot does not yet determine CI relevance, package quality, upgrade safety, or a final
recommendation.

**Revisit when**

The current ownership gate is completed and the controlling B2 plan authorizes the next exact-head
CI evidence responsibility.

# Reasoning quality check

A weak explanation says:

> We use a tuple because the code returns a tuple.

A stronger ownership explanation says:

> The acquisition layer returns a tuple so callers cannot append or remove records after the
> collection has passed completeness validation. A list would be easier to mutate but would
> weaken the trusted-evidence boundary. We would revisit the representation only if later stages
> require an explicitly versioned mutable working set rather than accepted evidence.

## Transfer exercise

Choose five decision cards. For each, write one row:

| Decision | Why selected | Failure prevented | Rejected alternative | Remaining cost | Revisit trigger |
|---|---|---|---|---|---|

Pass when your explanation connects the product responsibility to the mechanism. Naming a Python
feature without explaining the protected invariant is not enough.
