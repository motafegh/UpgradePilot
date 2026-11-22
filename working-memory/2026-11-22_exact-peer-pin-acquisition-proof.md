# Exact peer-pin acquisition proof

- **Product and design baseline:** `6d940cbaa72e87d15ecdd640047368ba46afbbce`
- [Preceding design review](2026-11-22_exact-peer-pin-conflict-design-review.md)
- UP-SKILL:upgradepilot-planning-design
- UP-SKILL:upgradepilot-repository-audit
- UP-SKILL:upgradepilot-working-memory

The selected work is an offline acquisition comparison over retained evidence. Ali's earlier instruction puts learning in a separate workstream, so this record preserves the engineering progression and proof. The comparison uses a diagnostic and leaves the product implementation alone.

## Protocol frozen before the contrast review

- **Selection.** Use the exact head, CI-selected requirements path and one changed exact pin as inputs from the retained case evidence. Infer one candidate companion path by removing the final `-lock` from the basename of a same-directory `*-lock.txt` file. Admit the pair only when both leading comment blocks name each other's exact bare basename and name no competing requirements-style text path. Treat conventional names alone as insufficient. The comments nominate a source and carry no authority to run commands. Refuse missing, conflicting, or separately scoped declarations. Do not list or search the tree for a better companion.
- **Candidates.** Parse single-line registry requirements. Reject ambiguous duplicate declarations and unsupported directives or direct references that affect the selected source. Join plain, unconditional direct roots to unique, plain, exact co-pins in the consumed file, omitting the changed name. Roots with extras or markers are outside the evaluated coverage. Use canonical package-name order. Once a pair is admitted, evaluate only plain, unconditional `Requires-Dist` edges for the changed package from an identified exact release record. Report excluded or unresolved evidence explicitly. A missing record or missing field cannot yield a compatibility result.
- **Budget.** Cap each arm at two exact-head file attempts and 20 exact version-scoped release attempts. Use zero retries and at most one attempt per unique key in an arm. Use a one-million-byte cap per decoded file or release body, matching existing representation limits. Refuse an over-cap candidate set before the first release attempt. Measure attempted and fulfilled reads, retained payload bytes, and offline elapsed time separately for each arm. Server availability, transfer bytes, and network latency are outside retained replay.
- **Cases.** ApplyPilot S017 is the exposed positive. Use server-nexe S019 as the first separate retained contrast because it supplies ordinary CI and requirements artifacts. Use MapProxy S018 to check entry refusal if its consumed dependency source does not have the selected shape. Select these by the visible case inventory before reading their retained case bodies. Use only provider evidence with a bounded case or retained release identity. A receipt missing from the replay is an unavailable replay input, distinct from a recorded provider denial.
- **Comparators and pass criteria.** Compare the existing report, an operator-nominated exact peer, and automatic nomination with the same retained input pool. The operator arm may name a co-pin but needs the same exact lock and metadata proof. Exercise compatible old pin, missing metadata, missing and contradictory companion, over-budget candidate set, and direct-root omission of a transitive co-pin as offline controls. For an automatic Build recommendation, require an additional defensible real selection beyond the exposed positive, correct refusal, and adequate measured acquisition evidence. A narrower positive or correct real layout refusal still informs where to stop.

## What replay established

The [replay diagnostic](evidence/2026-11-22-peer-pin-acquisition/replay.py) ran twice under Python 3.12.3 with networking isolated. Both runs verified reference report digests and reader identity, selected paths, retained file digests, and the S017 Playwright release digest. All observations agreed after excluding local timings. Case identities and raw-input hashes are in the [ApplyPilot](../product-simulation/scenarios/S017-applypilot-pyee-lockfile-conflict/CASE_EVIDENCE.json), [server-nexe](../product-simulation/scenarios/S019-server-nexe-psutil-skipped-sibling/CASE_EVIDENCE.json), and [MapProxy](../product-simulation/scenarios/S018-mapproxy-soupsieve-matrix-coverage/CASE_EVIDENCE.json) manifests. The ApplyPilot companion is an archive member retained at the exact head, with the provenance limits in the preceding design review. The verified lock member agrees with the independent case hash.

| Case and arm | Result | Attempted / fulfilled file reads | Attempted / fulfilled release reads | Decoded retained payload | Diagnostic time |
|---|---|---:|---:|---:|---:|
| ApplyPilot, saved ordinary report | Shows the exact failed install step and abstains. The report carries no Playwright evidence. | 0 / 0 | 0 / 0 | Historical report read separately | Report open excluded |
| ApplyPilot, known peer supplied | Playwright 1.64.1 conflicts with the new pyee pin. The operator supplied Playwright. | 1 / 1 | 1 / 1 | 12,232 bytes | 0.78–0.80 ms |
| ApplyPilot, automatic companion selection | 17 eligible roots from 59 other exact pins. Playwright was selected eighth and its declaration conflicts. The other 16 are unresolved. | 2 / 2 | 17 / 1 | 13,010 bytes | 1.41–1.99 ms |
| server-nexe, automatic | The exact command consumes `requirements.txt` directly. Layout refused. | 0 / 0 | 0 / 0 | 0 bytes | Under 0.03 ms |
| MapProxy, automatic | The exact command consumes `requirements-tests.txt` directly. Layout refused. | 0 / 0 | 0 / 0 | 0 bytes | Under 0.03 ms |

Both contrasts had an exact ordinary-consumption report that reopened and retained its recorded action of `abstain`. Neither supplied a known operator nomination. Server-nexe illustrates the scope problem with finding siblings by name: its separately retained Windows ARM64 requirements file has its own pin and install intent. The reviewed command consumes the root requirements file. An exploratory inventory of the four target archives in the same retained case directory found only one `*-lock.txt` member, the ApplyPilot lock; this inventory is descriptive and says nothing about prevalence elsewhere.

The automatic arm compared lock lines 38 and 45 to the Playwright release's `info.requires_dist[0]` declaration `pyee<15,>=13`. The current report points to the failed install. Either successful comparator narrows the next observation to whether pip actually applied that constraint in the recorded run. Neither comparator can establish the historical failure cause from the retained data. The ordinary report and comparators were reviewed with the same available packet. Only the operator arm received a named candidate, based on the already exposed case.

| Control derived from ApplyPilot | Outcome |
|---|---|
| Replace the changed pin with the old `14.0.0` pin and hold peer evidence fixed | The Playwright edge matches. Sixteen release inputs remain unresolved. |
| Withhold all peer metadata | All 17 are unresolved, with zero fulfilled release reads. |
| Remove the companion, give it a conflicting scope reference, or provide a matching basename with no reciprocal reference | Each stops before release lookup. |
| Append an unsupported include directive to the consumed file | Stops on the first file read with no release lookup. |
| Raise the eligible candidate count to 21 | Stops after two file reads and zero release lookups. |
| Inject a synthetic edge from a co-pin outside the direct roots | The automatic arm misses the seeded edge. The explicit-peer arm finds it with one release read. The injected AnyIO metadata is a control and makes no claim about the actual release. |

The attempt counters are replay lookups against an identity-bound retained input pool. They quantify logical request fan-out. The payload totals cover only retained decoded bytes, and the timing excludes input setup, file/network transport, and baseline report opening. Sixteen unavailable release responses are missing replay inputs, with no evidence about live availability or their size. The diagnostic did not run the ordinary acquisition clients, a resolver, target code, or a model. Historical CI cause, live provider cost and independent maintainer usefulness remain unresolved.

## Decision

Defer the automatic product path. The frozen rule proved one known positive and two accurate refusals. It supplied neither an independent positive layout nor full retained release coverage to measure delivered cost and test the other candidate outcomes. The controls also confirm a predictable missed transitive edge. Expanding the matcher around this one success or treating missing metadata as compatibility would overstate the evidence.

Keep the operator-nominated route as the low-cost comparator and a possible diagnostic for a recurring task where a maintainer already has a defensible peer. For automatic discovery, re-enter when a separate real case with defensible companion selection and a complete or explicitly bounded release packet is available. If the remaining decision turns on live cost, a separately scoped read-only acquisition proof would have to measure it. Preserve this case finding as research until those conditions or a narrower demonstrated need justify another design.

## Reproduce from retained evidence

From the repository root, pass the private case artifact directory and the private November 21 final acceptance directory as positional arguments. The script emits a receipt to stdout and does not fetch inputs.

```sh
unshare -Urn -- env -u PYTHONPATH -u GITHUB_TOKEN .venv/bin/python \
  working-memory/evidence/2026-11-22-peer-pin-acquisition/replay.py \
  "$peer_pin_case_artifacts" "$peer_pin_acceptance_artifacts"
```
