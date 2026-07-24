# 01 — Request-to-Evidence Flow

## Learning target

After this note, you should be able to draw the current flow from memory and explain where a failure belongs without reading the source.

## The complete current flow

```text
manual CLI input
→ local locator validation
→ read-only PR metadata request
→ transport and HTTP handling
→ JSON/object/field validation
→ PullRequestIdentity
→ paginated changed-file requests
→ changed-file record validation
→ expected/acquired count reconciliation
→ patch-evidence classification
→ exact pinned dependency extraction
→ supported or explicit unsupported result
→ concise terminal output
```

The stages are separated because each one answers a different question.

## 1. Manual input and local validation

Current input:

```text
owner/repository
positive PR number
```

Local validation proves only that the locator has a supported form. It does not prove that the repository or PR exists.

```text
valid syntax ≠ accessible remote resource
```

A future webhook or GitHub event may supply the locator, but it is not part of this snapshot.

## 2. PR metadata acquisition

UpgradePilot requests the public PR resource and obtains the minimum proposal identity:

- repository and PR number;
- base branch and exact base SHA;
- head branch and exact head SHA;
- changed-file count;
- selected descriptive metadata.

The base and head SHAs matter because a PR can change over time. Evidence about an older head cannot silently support a newer proposal.

```text
base SHA = exact starting revision
head SHA = exact proposed revision
```

## 3. Validation layers

Do not collapse every failure into “the API failed.”

| Layer | Question | Example failure |
|---|---|---|
| Input | Can this program interpret the locator? | malformed `owner/repository` |
| Transport | Did a usable HTTP response arrive? | timeout or connection error |
| HTTP | Did GitHub accept the request? | `404`, `403`, `429`, `500` |
| Representation | Is successful content valid JSON of the broad expected kind? | object expected, array received |
| Schema | Are required fields present with valid types? | missing `head.sha` |
| Semantic consistency | Does the response agree with the request and related evidence? | requested PR 1145, returned another number |

A `200 OK` establishes only HTTP success. It does not establish valid product evidence.

## 4. Changed-file acquisition is a separate responsibility

The PR metadata gives an expected count. It does not provide the complete individual file records needed for extraction.

```text
PR response:
    changed_files = 1

changed-files response:
    [ChangedFile(filename="requirements-dev.txt", ...)]
```

UpgradePilot therefore requests the changed-files endpoint separately.

## 5. Pagination and completeness

GitHub may return changed files across several pages. The current implementation requests up to 100 records per page and continues until it has enough records or the response indicates no more records.

Example:

```text
identity.changed_files = 101
page 1 = 100 records
page 2 = 1 record
```

After acquisition, UpgradePilot requires:

```text
number of validated acquired records
==
identity.changed_files
```

If metadata says two files but only one record is acquired, extraction must not begin. That is an acquisition/evidence-consistency failure, not an unsupported requirement syntax.

## 6. A changed-file record and its patch

The current `ChangedFile` record preserves:

```text
filename
status
additions
 deletions
changes
patch: text or absent
```

A unified patch uses:

```diff
 unchanged context
-removed old line
+added new line
```

For the live S004 case:

```diff
-pytest==9.0.2
+pytest==9.0.3
```

The patch markers are not part of the Python requirement. They identify the old and proposed lines.

## 7. Acquisition and extraction must remain separate

### Acquisition asks

> Did we obtain a complete, structurally valid representation of every changed file GitHub reported?

### Extraction asks

> Does the validated patch evidence contain exactly one change inside the currently supported grammar?

A valid record with `patch=None` means:

```text
changed-file acquisition succeeded
patch evidence is unavailable
exact dependency extraction is unsupported
```

This is more accurate than throwing a network error or inventing an empty patch.

## 8. Current supported extraction grammar

Only this form is supported:

```diff
-package==old_version
+package==new_version
```

The extractor additionally requires:

- exactly one removed pinned candidate;
- exactly one added pinned candidate;
- both candidates in the same modified file;
- equivalent normalized package names;
- different explicit versions;
- patch addition/deletion counts consistent with GitHub metadata.

Everything else remains explicit unsupported evidence rather than guessed meaning.

## 9. Supported, unsupported, and failed are different

| Outcome | Meaning |
|---|---|
| Supported | Complete evidence matched the current exact grammar |
| Unsupported | Acquisition succeeded, but meaning is outside the proven extraction boundary |
| Acquisition failure | Remote evidence could not be obtained reliably |
| Response/evidence failure | Successful remote content was malformed, incomplete, or contradictory |

Examples:

```text
pytest>=9.0.2 → pytest>=9.0.3
    unsupported grammar

patch absent
    unsupported due to missing line evidence

metadata says 2 files, acquisition returns 1
    evidence-consistency failure

GitHub request times out
    acquisition failure
```

## 10. What the live run proved

The real command proved that this current path worked for one public PR:

```text
googlefonts/glyphsLib#1145
→ exact base/head identity
→ one validated changed file
→ requirements-dev.txt
→ pytest 9.0.2 → 9.0.3
```

It did not prove:

- the update is safe;
- relevant CI exercised pytest;
- all Python dependency declaration forms are supported;
- the implementation is production-ready;
- Ali independently owns the source.

## Recall action

Without looking above, write the flow as 10–12 arrows. Then classify these three cases:

1. GitHub returns HTTP 200 with a JSON object for the changed-files endpoint.
2. GitHub returns two valid file records, but PR metadata expected three.
3. A complete record contains `-demo.package==1.0.0` and `+demo_package==1.1.0`.

Expected classifications:

1. representation failure: the endpoint requires an array;
2. evidence-consistency failure;
3. potentially supported after package-name normalization, assuming all other invariants hold.