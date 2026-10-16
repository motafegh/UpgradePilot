# Investigator Workspace mechanical qualification

This experiment connects a bounded Investigator consumer to the existing product Workspace.
It tests mechanical fidelity and authority/reference boundaries with a local script. It does
not contain a model transport or establish semantic usefulness. The [integration plan](../plans/INVESTIGATOR_INTEGRATION_AND_COMPARATIVE_EVALUATION_PLAN.md)
owns the comparison and later qualification gates; [MEMORY](../MEMORY.md) owns live selection.

## Reading and execution route

1. [InvestigatorAssignment](investigator_workspace_adapter.py) initializes a fresh volatile
   product host from a retained native boundary and exact-target source catalog. Trusted
   composition installs bounded view methods and a generic discovery purpose, with no
   execution authority/capabilities. Only the closed tool menu is consumer-facing.
2. [run_scripted_trial](investigator_workspace_trial.py) renders the prompt/task/tool/report
   schemas plus newest complete events that fit the declared byte envelope. Omitted whole
   events retain IDs, sizes and hashes. It calls a trusted local script, retains original
   response bytes, then admits a tool request or final report under bounded resources.
3. [Offline qualifier](qualify_investigator_workspace.py) verifies a declared input inventory
   and code correspondence, reads checkpoints through the supported read-only API and runs
   both treatments with generic source discovery. It preserves owner-only private artifacts
   and emits a public summary of identities, counts, costs and hashes.

From the repository root, with a **new** output directory and summary filename:

```bash
PYTHONPATH=src:. .venv/bin/python -m experiments.qualify_investigator_workspace \
  --qualification working-memory/evidence/2026-10-16-common-investigator-input-snapshot/qualification.json \
  --output /absolute/owner-only/output-directory \
  --summary /absolute/new-summary.json

PYTHONPATH=src:. .venv/bin/python -m unittest discover \
  -s experiments/tests -p test_investigator_workspace_trial.py -v
```

No acquisition, model load, inference or target execution is involved. The qualifier guards
socket connect, requests HTTP, subprocess creation and the named native producer/model-session
entry points. It rechecks retained hashes after execution. These are bounded diagnostic guards,
not a general sandbox. The unit tests use controlled unfinished native captures; real-input
qualification is separately retained as [dated evidence](../working-memory/evidence/2026-10-16-investigator-adapter-mechanical/README.md).

## Evidence and treatment contract

Raw and structured assignments share immutable inputs, each with a separate host/lineage,
reference registry, events and notes. Raw access has source list/path/read/literal-search/resolve;
structured access additionally has native views/pages. Withheld native access is not absent
data. Preparation demonstration history is not restored. Notes and read-back events are explicitly
laboratory interpretations, not independent source corroboration.

Product delivery content is retained exactly inside the outer tool event. Each laboratory
`{kind,id}` reference maps to its actual delivery, exact source range/native digest/page range
and assignment. A search result can be cited as a search observation, not relabeled as full
source lines. A complete read/resolve creates its own source-line reference. Native omissions
have no full-record reference; page references remain pages. The driver admits report references
only after their complete containing event reached a consumer input. That establishes observable
input inclusion, not hidden examination or entailment.

`investigator-contract2-workspace/1` preserves the Contract-2 report fields and
asserted/inferred/unresolved statuses, extending typed evidence kinds with `native_record` and
`native_page`. Legacy kinds are not fabricated when the adapter offers no corresponding event.
Report validation checks shape and reference relationships before publication. The host retains
one attributed laboratory report and mapped citations, with semantic evaluation `unsupported`.
Summary/recommendation/conditions remain subject to later semantic review even when their shape
is valid. Procedural finish/termination is separately recorded and never claims adequacy.

## Accounting, packing and failure

| Admission charge | Units and meaning |
| --- | --- |
| Raw navigation or native view/page | 4: consumer request, bounded read/projection, view preparation, delivery attempt |
| Note | 1: request/local note operation |
| Event read-back | 3: request, view preparation, delivery attempt |
| Finish request | 3: request, stopping proposal, unsupported evaluation |
| Final report | 4 plus unique references: request, view, proposal, evaluation and each citation |
| Malformed/unoffered request | 1; no backend execution |
| Procedural termination | 1 reserved before calls |

These are conservative admission charges, not claims that every reserved operation executed.
Early refusals are not refunded. Actual product access receipts retain examined files/lines,
delivered bytes and failure state, including work before a publication failure. Composition cost,
scripted elapsed time, exact input/response/observation bytes and earlier shared preparation are
reported separately. Capacity is reserved conservatively before backend work; unused byte
reservation is released. Current code has no native producer calls or model calls. Token usage
is unavailable, not inferred from bytes.

The byte envelope is a mechanical packing limit, not a chosen model context. Actual rendered
tokenizer/template fit, generation/reasoning reserve, context and GPU/cache placement remain
later measured deployment responsibilities. The qualifier uses a 4096-byte native view to exercise
omission/page behavior; this does not automatically choose a future inference configuration.

Malformed responses receive bounded visible corrections with originals preserved. Refused, empty,
scoped-negative, problem, failed and exhausted outcomes remain distinct. A backend/publication
failure stops without automatic replay. The synchronous driver checks deadlines around work;
it does not claim interruptible CPU execution or durable/exactly-once recovery. Volatile host
history and private diagnostic artifacts are experiment evidence, not a product checkpoint service.

The mechanical manifest freezes exact protocol/schema/packing/charging/code/input identities and
sets `inference_admitted=false`, with deployment fields unresolved. It is not a runnable final
model manifest. The later qualification must supply actual model/runtime/template/placement and
token/resource evidence under the existing protocol. No old Qwen configuration is inherited.
