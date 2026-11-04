"""Compare normal-composition meaning after reviewed source/fact ID readdressing.

The exact retained-input channel independently checks against the original fixed
envelope. This comparison then binds normal composition to that qualified native
result by repository/revision/path/content and fact kind/span. It never searches
for a passing subset. Candidate multiplicity, ordered path/trace steps, premises,
outcomes, gaps, admission states and work remain comparison material.
"""
from dataclasses import asdict
from hashlib import sha256
import json


def canonical(value):
    return json.dumps(value, sort_keys=True)


def normalized(sources, result):
    scopes = {s.source_id: (s.repository, s.revision) for s in sources.catalog.scopes}
    names = {sid: "scope:" + canonical(value) for sid, value in scopes.items()}
    for file in sources.catalog.files:
        uid = sources.catalog.descriptor(file)["file_id"]
        names[uid] = "file:" + canonical((*scopes[file.source_id], file.path, sha256(file.content.encode()).hexdigest()))
    for unit in result.units:
        if unit.facts:
            for kind, facts in (("call", unit.facts.calls), ("signature", unit.facts.signatures)):
                for fact in facts:
                    names[fact.fact_id] = canonical((kind, names[unit.unit_id], asdict(fact.span)))

    def map_ids(value, key=None):
        if isinstance(value, dict):
            return {k: map_ids(v, k) for k, v in value.items() if k != "candidate_id"}
        if isinstance(value, (list, tuple)):
            return [map_ids(v, key) for v in value]
        if key in {"source_id", "unit_id", "fact_id", "call_id", "signature_id", "root_call_id"} and isinstance(value, str):
            return names[value]
        return value

    units = [map_ids(asdict(u)) for u in result.units]
    candidates = [map_ids(asdict(c)) for c in result.candidates]
    admission = [map_ids(asdict(a)) for a in result.admission]
    return dict(
        files=sorted(names[sources.catalog.descriptor(f)["file_id"]] for f in sources.catalog.files),
        modules=sorted((map_ids(asdict(m)) for m in sources.modules), key=canonical),
        units=sorted(units, key=canonical),
        candidates=sorted(candidates, key=canonical),
        gaps=sorted((map_ids(asdict(g)) for g in result.gaps), key=canonical),
        admission=sorted(admission, key=canonical), work=asdict(result.work),
        ordered_candidates=candidates, ordered_admission=admission,
    )


def compare(reference, actual):
    left = normalized(reference.sources, reference.comparison.result)
    right = normalized(actual.sources, actual.comparison.result)
    return {name + "_equal": canonical(left[name]) == canonical(right[name]) for name in left}


def native_pairing(run):
    if run is None or run.result is None:
        return dict(paired_roots=0, native_witnesses=0)
    roles = {}
    count = 0
    for candidate in run.result.candidates:
        role = candidate.callee_role.role
        if role in {"old_dependency", "proposed_dependency"}:
            roles.setdefault(candidate.root_call_id, set()).add(role)
            count += 1
    return dict(paired_roots=sum(value == {"old_dependency", "proposed_dependency"} for value in roles.values()),
                native_witnesses=count)
