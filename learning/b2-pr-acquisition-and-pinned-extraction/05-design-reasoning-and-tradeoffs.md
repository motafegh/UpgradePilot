# 05 — Design Reasoning and Trade-offs

## Learning target

After this note, you should be able to defend the current design without saying only:

> Because the code does it this way.

Use this reasoning chain:

```text
responsibility
→ chosen mechanism
→ failure prevented
→ alternative rejected
→ cost accepted
→ evidence needed to revisit
```

Do not memorize every decision. Study the decisions that map to the source function you are tracing.

## Compact decision map

| Decision | Why selected now | Main alternative rejected | Cost accepted | Revisit trigger |
|---|---|---|---|---|
| Manual CLI locator | Smallest real path to a public PR | Webhook/GitHub App adds hosting, secrets, and event reliability | Manual invocation | Automatic invocation becomes an authorized responsibility |
| PR metadata before files | Establishes exact proposal identity and expected file count | Files-first has no independent identity/completeness anchor | Extra API request | A trustworthy event supplies equivalent identity and count |
| Base/head SHAs | Bind evidence to immutable revisions | PR number or branch names can point to changing content | Later evidence must reconcile to the same SHA | Representation may change; immutable binding should remain |
| Small read-only client | Minimizes permissions, effects, and abstraction | Full SDK/write integration enlarges surface too early | Limited endpoint coverage | Repeated authorized protocol code justifies an SDK |
| Requests + injected Session | Direct HTTP behavior and deterministic collaborator replacement | `urllib`, async clients, or global patching add complexity/coupling | Runtime dependency and synchronous path | Concurrency or broader API evidence creates need |
| Explicit connect/read timeout | Prevents indefinite CLI blocking | Requests default has no timeout | Values are not production-tuned | Observed latency or recovery needs justify tuning/retry |
| Distinct failure categories | Preserves diagnosis and product meaning | One generic error hides cause and required action | More explicit branches | Split only when user action or recovery differs |
| Validated immutable records | Separates untrusted JSON from trusted internal evidence | Raw dictionaries spread validation and mutation risk | Handwritten contracts | Contract volume makes a framework clearly cheaper |
| Pagination + final count check | Proves complete changed-file acquisition | First-page-only or short-page-only can miss evidence | More requests and bounded maximum | Repeated pagination or robustness needs justify abstraction |
| Preserve absent patch + check counts | Keeps missing/truncated evidence explicit | Empty-string substitution or fragment parsing invents certainty | Some real cases abstain | Full file/blob acquisition is later authorized |
| Acquisition separate from extraction | Keeps external failure distinct from unsupported meaning | One combined loop entangles network and interpretation | More types and hand-offs | Internal layout may change; responsibility boundary should remain |
| Unsupported returned as data | Abstention is an expected product result | Exceptions make expected limits look like defects; `None` loses reason | Callers must branch | More states may justify a richer result model |
| Exact-pin grammar only | Smallest deterministic dependency identity | Broad requirement parsing adds semantics and ambiguity | Many valid forms unsupported | A new real case justifies one bounded grammar extension |
| Normalize package names | Different spellings may identify one distribution | Raw equality creates false mismatches | Does not prove version safety | Authoritative packaging evidence changes the rule |
| Mocked tests + live smoke | Combines repeatable edge cases with real integration evidence | Mock-only or live-only leaves major gaps | Two proof modes to maintain | Robustness work authorizes captured-response/contract tests |
| Defer retry, CI, persistence, recommendation | Keeps the current responsibility learnable and attributable | Building the whole platform now blurs evidence and ownership | Product remains incomplete | Current ownership gate passes and the plan authorizes next evidence |

# High-value reasoning deep dives

## 1. Why acquire PR metadata before changed files?

**Responsibility:** establish the exact proposal before interpreting its content.

**Chosen mechanism:** request PR metadata first and construct `PullRequestIdentity` containing base SHA, head SHA, and `changed_files`.

**Why:**

- a PR number can remain stable while new commits change the proposal;
- the head SHA identifies the exact revision being evaluated;
- `changed_files` becomes an independent completeness target for the second request.

**Rejected alternative:** request changed files first and trust the endpoint path.

**Why rejected:** it provides file records without an independently validated revision identity or expected count.

**Failure prevented:** evidence from an older head or incomplete file set cannot silently support the current proposal.

**Accepted cost:** at least two API operations.

**Revisit when:** a future authenticated event supplies equivalent immutable identity and completeness evidence.

## 2. Why separate acquisition from extraction?

**Responsibility split:**

```text
GitHubReadClient
    acquire and structurally validate external evidence

extract_pinned_dependency_change
    interpret already validated evidence
```

**Why:** the two stages have different failure meanings.

- timeout, HTTP refusal, malformed JSON, and count disagreement mean evidence was not acquired reliably;
- absent patch or unsupported requirement syntax may occur after valid acquisition and should produce abstention.

**Rejected alternative:** request pages and parse dependency lines inside one combined method.

**Why rejected:** partial evidence, network errors, and unsupported syntax would become entangled and harder to test or explain.

**Failure prevented:** an unsupported requirement cannot be mislabeled as a network failure, and an acquisition failure cannot become a normal unsupported result.

**Accepted cost:** more explicit types and hand-off points.

**Revisit when:** internal file placement may change, but the responsibility and failure boundary should remain.

## 3. Why paginate and still reconcile the final count?

**Responsibility:** prove that every file GitHub reported was acquired before extraction starts.

**Chosen mechanism:** request up to 100 records per page, validate each record, then require:

```text
len(validated_records) == identity.changed_files
```

**Why both signals are needed:**

- a short page indicates that pagination probably ended;
- the metadata count independently confirms whether the acquired set is complete.

**Rejected alternatives:**

- first page only;
- trust only `len(page) < 100`;
- build a generic pagination framework before another endpoint needs it.

**Failure prevented:** the extractor cannot select one dependency change while silently missing another changed file that would make the proposal ambiguous.

**Accepted cost:** additional requests and rejection beyond the current complete-acquisition limit.

**Revisit when:** multiple endpoints need identical pagination or live evidence demonstrates retry/resume requirements.

## 4. Why preserve `patch=None` and compare patch counts?

**Responsibility:** represent the evidence GitHub actually supplied without inventing missing content.

**Chosen mechanism:** keep `patch` as `str | None`; when text exists, compare visible additions/deletions with GitHub's per-file counts.

**Why:**

- a valid file record may exist without line-level patch evidence;
- `None` communicates absence explicitly;
- count disagreement can reveal truncated or incomplete patch text.

**Rejected alternatives:**

- convert absence to `""`;
- parse whatever fragment is visible;
- treat missing patch as a transport failure.

**Failure prevented:** UpgradePilot does not produce a confident dependency identity from absent or incomplete line evidence.

**Accepted cost:** some real dependency updates are classified as unsupported.

**Revisit when:** a later authorized mechanism retrieves exact blobs or full diffs bound to the same head SHA.

## 5. Why return unsupported as a normal result?

**Responsibility:** express a trustworthy abstention when evidence is valid but outside the proven interpretation boundary.

**Chosen mechanism:**

```text
PinnedDependencyChange
or
UnsupportedDependencyChange(reason, detail)
```

**Why:** unsupported syntax is expected external reality, not automatically a program defect.

**Rejected alternatives:**

- raise an exception for every unsupported case;
- return `None`;
- guess the most likely meaning.

**Why rejected:** exceptions confuse normal abstention with system failure, `None` loses the reason, and guessing violates evidence discipline.

**Failure prevented:** callers and users can distinguish “could not acquire evidence” from “acquired evidence but intentionally did not interpret it.”

**Accepted cost:** every caller must branch on the result type.

**Revisit when:** additional normal states justify a richer result model, while abstention remains explicit.

## 6. Why support only exact pinned replacements?

**Responsibility:** identify one package, old version, and proposed version deterministically from a patch.

**Chosen grammar:**

```diff
-package==old_version
+package==new_version
```

with exactly one removed candidate and one added candidate in the same modified file.

**Why:** it is the smallest form precise enough for the current product responsibility and real S004 case without hardcoding `pytest` or the repository.

**Rejected alternatives:**

- accept ranges such as `>=`;
- accept extras, markers, URLs, editable installs, or multiline forms;
- heuristically choose one pair among several candidates;
- add a broad parser before the product owns the additional semantics.

**Failure prevented:** valid-looking but ambiguous declarations do not become false exact-version identities.

**Accepted cost:** many valid Python requirement forms remain unsupported.

**Revisit when:** a new real case and product need justify one additional syntax form, its semantics, and focused tests.

## 7. Why normalize package names?

**Responsibility:** compare Python distribution identity rather than raw spelling.

**Chosen mechanism:** lowercase the name and replace runs of `.`, `_`, and `-` with `-`.

Example:

```text
demo.package
and
demo_package
→ demo-package
```

**Why:** raw string equality would classify equivalent distribution spellings as different packages.

**Rejected alternative:** compare the captured names exactly as written.

**Failure prevented:** a legitimate version update is not rejected as `package_mismatch` solely because separators differ.

**Accepted cost:** normalization establishes package identity only. It does not establish package authenticity, version ordering, compatibility, or upgrade safety.

**Revisit when:** authoritative packaging rules or a demonstrated edge case require a changed identity rule.

## 8. Why use both deterministic tests and a live smoke run?

**Responsibility:** prove controlled behavior and one real integration path without confusing either proof with complete correctness.

**Deterministic tests are chosen because they can:**

- reproduce pagination, malformed responses, missing patch, and ambiguity;
- run quickly without network or rate-limit dependence;
- localize failures to one contract.

**The live run is chosen because it can:**

- verify the installed package and Requests dependency;
- reach the actual GitHub endpoints;
- exercise real response shapes and the end-to-end CLI path.

**Rejected alternatives:**

- mock-only: may pass while the real endpoint, headers, installation, or response differs;
- live-only: slow, unstable, rate-limit-sensitive, and poor for rare failure cases.

**Accepted cost:** two proof modes and one live case still do not establish production readiness or broad compatibility.

**Revisit when:** B3 authorizes captured-response fixtures, contract tests, or additional robustness evidence.

# Reasoning quality check

A weak explanation:

> We return a tuple because the code returns a tuple.

A stronger explanation:

> The acquisition layer returns an immutable tuple so callers cannot append or remove records after the collection has passed completeness validation. A mutable list would be convenient but would weaken the trusted-evidence boundary. The representation should change only if a later stage explicitly requires a mutable working set rather than accepted evidence.

## Transfer exercise

Choose five decisions and complete:

| Decision | Why selected | Failure prevented | Rejected alternative | Remaining cost | Revisit trigger |
|---|---|---|---|---|---|

Pass when the explanation connects product responsibility to mechanism and trade-off. Naming a Python feature without explaining the protected invariant is not enough.
