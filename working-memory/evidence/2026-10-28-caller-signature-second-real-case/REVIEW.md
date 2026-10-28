# Second real caller/signature case — glyphsLib and pytest

## Result

The existing implementation, unchanged from1475abd3, processes a second real retained target/library scenario. All five pre-frozen outcomes match: four conditional bindings and one unresolved receiver comparison. No package-specific rule, source/test change, new acquisition, model call, installation or third-party execution was needed.

The [pre-execution freeze](freeze.json), [source readiness](readiness.json), [actual view](comparison-view.txt), [attempt metadata](attempt-01.json) and [inspection receipt](inspection.json) preserve inputs, expectations, method identity, results and limits. Expectations were separate review material, never analyzer inputs. This is exposed assistant development evidence, not independent usefulness or unrestricted generality acceptance.

## Why this is a different real case

The target is retained googlefonts/glyphsLib PR1145, pytest9.0.2→9.0.3, at exact recorded base/head. This differs from the HTTPX adapter/initializer case in library, target, callable form and binding structure:

- `tests/builder/components_test.py:50` calls pytest.raises with one positional argument. It is compared with the old/proposed complete declared function implementations using `as_written`, without inserting a receiver.
- `tests/regression_test.py:59` calls pytest.mark.parametrize with two positional arguments and the actual ids keyword. Captured MarkDecorator.__call__ receives positional/keyword variadics, so ids enters **kwargs; it is not a named parameter in that declaration.
- Both pytest APIs have same-named overload definitions in retained source. Exact implementation spans select the undecorated raises104 and MarkDecorator.__call__390 definitions, rather than selecting the first matching name or a typing stub.
- A fifth comparison keeps the real source unchanged but leaves receiver binding unresolved. This tests a missing premise and does not count as another independent real case.

The candidate source chain is grounded in target pytest imports, pytest package re-exports, MARK_GEN and the captured MarkGenerator→MarkDecorator factory source. This is enough to inspect an explicitly curated conditional pairing. It is not proof of effective descriptor execution, installed distribution/source correspondence or automatic discovery.

## Actual results

| Captured interaction | Receiver premise | Result | Specific evidence |
| --- | --- | --- | --- |
| Target raises call → old implementation | as written | bound | One supplied positional argument fits the declared function |
| Target parametrize call → old MarkDecorator.__call__ | one receiver assumed | bound | Extra positions enter *args; ids is received by **kwargs |
| Target raises call → proposed implementation | as written | bound | Same selected argument shape fits |
| Target parametrize call → proposed MarkDecorator.__call__ | one receiver assumed | bound | ids remains variadic-keyword reception |
| Same parametrize call → proposed implementation | unresolved | undetermined | ids reception stays observable, but complete binding is withheld |

No binding violation is present for these selected calls/signatures. This refutes a mismatch at those declared boundaries under their explicit premises. It does not establish whole-update non-applicability or compatibility, validate ids values/meaning, show that the tests ran, or establish what pytest's body accepts later. The older/newer signatures are not required to differ for this continued-binding contrast to be useful.

Combined with the untouched HTTPX record, the evidence now includes a real explicit-keyword mismatch, continued binding in another target/library, variadic keyword reception and an explicit missing-receiver state. These are two retained scenarios, not ten independent real cases, an unbiased benchmark or a broad accuracy estimate.

## Execution and preservation

The first and only new analyzer attempt completed in1.022769608s under the original limits. It read12 selected complete files/205,876 UTF-8 bytes and inspected20,917 AST nodes, producing1,113 call/signature facts and five comparisons. The tool does not execute argument values, the ids lambda, target module-level globbing, annotations, defaults or inspected library code.

The original case2 profile hash matches the prior qualified inventory. Its selected target file Git-blob identities also verify. Complete file qualification comes from the recorded archive/blob capture, not from successful parsing. Broad target inventory omissions remain explicit; this is not complete target-usage coverage. Recorded requirements pins establish declarations, not installation or historical CI state.

All13 actual cold CLI opens pass: one summary and12 selected-source pages, taking2.575517522s. Guarded opening with socket creation, AST parsing and analyzer execution forbidden also passes. Original catalog, new frozen source/selections, every new attempt member and every member of the earlier HTTPX attempt remain hash-identical. Method/source identities match the pre-freeze unchanged implementation. Private raw inputs/results/source pages retain0700/0600 modes; public artifacts expose reviewed facts, identities and views only.

The earlier165-test API regression remains applicable to hash-identical method code and is explicitly historical/reused; it was not rerun or presented as new verification. The new proof is the frozen real-source execution and offline consumer checks. No executable, product, specification, ADR, dependency or test changes were made in this cycle. No defect or unsupported-case workaround is justified by the observed outputs.

## Inspection

```sh
PYTHONPATH=src:. .venv/bin/python3 -m experiments.api_call_signature_trial open \
  --result /home/motafeq/.local/share/upgradepilot/caller-signature-evidence/retained-glyphslib-pytest-2026-10-28/attempt-01
```

Add `--source UNIT_ID --start-line N --line-count N` using the summary's unit IDs to inspect retained evidence. Opening is historical and offline; it does not refresh the PR or replay the analysis.

## Disposition and next responsibility

Retain the unchanged method for its demonstrated conditional source-binding envelope. The second materially different retained case is available and passes its declared contrasts; this earns additional evidence, not general adoption.

The next design responsibility is ordinary experimental PR→source→correspondence→saved-result integration: identify what existing acquisition owners can provide, preserve minimum necessary source and prove selected calls/signatures can be discovered without supplied answer selectors. Reconcile that retention/consumer boundary with the still-pending Workspace migration discussion before normal product adoption. A full migration is not automatically required first; indefinite product-delivery deferral is not justified either.

Historical glyphsLib CI/runtime/model limitations remain unchanged and separately owned. No new model experiment, package-manager/workflow expansion, stronger source authority or maintainer-action permission follows from this static result.
