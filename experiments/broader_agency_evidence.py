"""Trial-owned claim → evidence records; never a semantic truth evaluator.

Workspace supplies immutable corpus facts, orchestration registers host packets
and tool observations, and successful provider requests establish delivery. A
reference is not entailment. Search completeness is relative to retained text;
CI/runtime capture provenance is retained rather than promoted to execution.
"""

from __future__ import annotations

import json

from .broader_agency_workspace import digest

EVIDENCE_KINDS = (
    "source_line",
    "update_packet",
    "diff",
    "search_observation",
    "inventory",
    "ci_runtime_observation",
    "trial_event",
)

EVIDENCE_GUIDE = """Claim/evidence contract v2:
Each claim has statement, status (asserted/inferred/unresolved), evidence (typed
{kind,id} references), and missing_observation (required nonempty for unresolved).
Asserted/inferred claims and recommendations need delivered evidence. Unresolved
claims may have no evidence; name the specific missing observation instead.
Source line example: {"kind":"source_line","id":"source-id:path/to/file:L7"}.
Use EXACT host-issued evidence_refs for packet/diff/search/inventory/capture/event
observations. No bare paths, line ranges or invented observation IDs. Search is
literal, not regex; zero hits support only the recorded query and retained scope.
An existing but undelivered line is not an admissible source reference. A truncated
search preview is not delivery of the full line; read it or cite the search page.
References establish evidence identity/delivery only; explain what they support.
Every factual assertion, including summary/conditions text, must be represented
in claims. Semantic review checks omitted assertions as well as referenced claims.
CI/runtime captures retain their dates, completeness and illustrative provenance;
their reference type does not prove fresh execution or installed dependencies.
Model-authored trial notes/artifacts are not independent source corroboration.
Recommendation fields: recommendation, recommendation_status,
recommendation_evidence, recommendation_missing_observation. Unknown/insufficient
evidence is a valid outcome; stage artifact format is not investigation adequacy.
Follow document pointers found in sources, paginate paths and reads, and acquire
counterevidence during challenge. Do not infer compatibility from a version label.
"""


class TrialEvidence:
    """One trial's registered observations and actual request delivery history."""

    def __init__(self, workspace):
        self.workspace = workspace
        self.records = {}
        self.delivered = {}
        self.visible = set()
        self.inventory_reference = self.register(
            "inventory",
            {"corpus_sha256": workspace.identity, "sources": workspace.sources},
        )

    def register(self, kind, payload):
        identifier = f"{kind}:{digest(payload)[:20]}"
        reference = {"kind": kind, "id": identifier}
        existing = self.records.get((kind, identifier))
        if existing is not None and existing != payload:
            raise ValueError("host evidence identifier collision")
        self.records[(kind, identifier)] = payload
        return reference

    def packet(self, packet):
        packet = dict(packet)
        references = [self.register("update_packet", packet)]
        packet["diffs"] = [
            {
                **d,
                "evidence_refs": [
                    self.register(
                        "diff", {"corpus_sha256": self.workspace.identity, **d}
                    )
                ],
            }
            for d in packet["diffs"]
        ]
        packet["evidence_refs"] = references
        return packet

    def observation(self, tool, arguments, result, event_id, call_id):
        payload = {
            "event_id": event_id,
            "call_id": call_id,
            "tool": tool,
            "arguments": arguments,
            "observation": result.get("observation"),
            "result": result,
            "corpus_sha256": self.workspace.identity,
        }
        references = [self.register("trial_event", payload)]
        if "tool_problem" not in result and "format_problem" not in result:
            kind = (
                "search_observation"
                if tool == "search_sources"
                else ("inventory" if tool in {"list_sources", "list_paths"} else None)
            )
            source = next(
                (
                    s
                    for s in self.workspace.sources
                    if s["source_id"] == arguments.get("source_id")
                ),
                {},
            )
            if (
                source.get("evidence_kind") == "ci_runtime_observation"
                or source.get("source_id") == "ci-observations"
            ):
                references.append(
                    self.register(
                        "ci_runtime_observation",
                        {**payload, "capture_provenance": source},
                    )
                )
            if kind:
                references.append(self.register(kind, payload))
        # Full immutable provenance stays in the ledger. The request already
        # supplies the source inventory; repeating it for every page can consume
        # context without delivering any additional source facts. This view
        # preserves text, exact read/search scope, offsets and completeness.
        view = {k: v for k, v in result.items() if k not in {"identity", "sha256"}}
        if "observation" in view:
            observation = dict(view["observation"])
            observation["scope"] = {
                k: v
                for k, v in observation["scope"].items()
                if k not in {"source", "sources", "corpus_sha256"}
            }
            observation["scope"]["inventory_basis"] = (
                "request.sources; full provenance retained in host evidence record"
            )
            view["observation"] = observation
        return {**view, "evidence_refs": references}

    def observe_request(self, request, request_id):
        """Mark only host evidence actually included in this answered request.

        Packed-away events remain historically delivered but not currently visible.
        Assistant-authored references do not establish delivery. Timeout/transport
        failure does not create proof of model receipt.
        """
        self.visible = set()

        def mark(value):
            if not isinstance(value, dict):
                return
            for reference in value.get("evidence_refs", []):
                key = (reference["kind"], reference["id"])
                if key in self.records:
                    self.visible.add(key)
            for line in value.get("selected_lines", []) + value.get("matches", []):
                if "citation" in line and line.get("preview_complete", True):
                    self.visible.add(("source_line", line["citation"]))

        user = json.loads(request.user)
        mark({"evidence_refs": user.get("source_inventory_evidence", [])})
        packet = user.get("update_packet", {})
        mark(packet)
        for diff in packet.get("diffs", []):
            mark(diff)
        for observation in user.get("provided_evidence", []):
            mark(observation)
        for event in request.history:
            for result in event.get("results", []):
                mark(result["result"])
        for key in self.visible:
            self.delivered.setdefault(key, []).append(request_id)

    def inspect(self, reference):
        key = (reference["kind"], reference["id"])
        exists = (
            self.workspace.source_line(reference["id"]) is not None
            if reference["kind"] == "source_line"
            else key in self.records
        )
        return {
            **reference,
            "exists": exists,
            "existence_basis": "frozen_corpus"
            if reference["kind"] == "source_line"
            else "trial_host_record",
            "delivered": key in self.delivered,
            "currently_visible": key in self.visible,
            "delivery_requests": self.delivered.get(key, []),
            "referenced": True,
            "semantic_support": "not_reviewed",
        }

    def inspect_claims(self, value):
        rows, problems = [], []
        claims = list(value["claims"])
        if "recommendation" in value:
            claims.append(
                {
                    "statement": value["recommendation"],
                    "status": value["recommendation_status"],
                    "evidence": value["recommendation_evidence"],
                    "missing_observation": value["recommendation_missing_observation"],
                }
            )
        for index, claim in enumerate(claims):
            status, references = claim["status"], claim["evidence"]
            if status not in {"asserted", "inferred", "unresolved"}:
                problems.append(f"claim {index}: unknown status")
            if status == "unresolved" and not claim["missing_observation"].strip():
                problems.append(
                    f"claim {index}: unresolved requires missing observation"
                )
            if status != "unresolved" and not references:
                problems.append(f"claim {index}: asserted/inferred requires evidence")
            evidence = [self.inspect(r) for r in references]
            for item in evidence:
                if not item["exists"] or not item["delivered"]:
                    problems.append(
                        f"claim {index}: nonexistent or undelivered {item['id']}"
                    )
            rows.append(
                {
                    "claim_index": index,
                    "statement": claim["statement"],
                    "status": status,
                    "evidence": evidence,
                    "semantic_support": "not_reviewed",
                }
            )
        return rows, problems
