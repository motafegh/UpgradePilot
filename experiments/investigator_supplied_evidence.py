"""One report attempt over trusted, explicitly supplied Workspace evidence.

Start at SuppliedEvidenceTrial.prepare, then run once with a scripted consumer or the
qualified StatelessInvestigatorModel. Preparation uses real adapter/source/native
deliveries and is charged separately from model work. It establishes no autonomous
discovery or stopping competence. Strict publication remains the adapter's authority.

The fixed allowance protects report/citation/termination capacity before prediction.
Whole required events cannot be omitted to fit bytes/tokens. Real source recipes and
review obligations live outside this generic composition; no expected answer is used.
"""

from __future__ import annotations

import json
import re
import time
from dataclasses import asdict, dataclass

from experiments.investigator_run_control import MonotonicDeadline, PredictionDeadlineExceeded, problem_text
from experiments.investigator_workspace_adapter import decode_object
from experiments.investigator_workspace_trial import (
    ScriptedTrialResult,
    TrialLimits,
    _admission_charge,
    pack_input,
    protocol_definition,
)
from upgradepilot.workspace.native_representation import json_bytes

SUPPLIED_EVIDENCE_PROTOCOL = "investigator-supplied-evidence-report-only/1"
PR_BRIEF = (
    "Using only the supplied packet, produce the existing full report. Use claims first "
    "to state material source observations and their exact scope, then the relationships "
    "those observations support and the premises that remain unresolved. Cite the supplied "
    "passages needed for each material relationship. Trace the declared dependency change "
    "through visible consumer use and any supplied provider changes. Where CI material is "
    "present, connect workflow steps with the supplied tool configuration and dependency "
    "inputs before drawing coverage conclusions. Distinguish static declarations, historical "
    "observations, exact-context correlation and established runtime facts; preserve native "
    "assessments at their stated strength. Derive summary, conditions and recommendation "
    "from those findings, with a specific justified check or scoped conclusion for material "
    "missing bindings. Do not infer compatibility, low risk, executed coverage, source "
    "exhaustion or action permission from a version category, a successful job, an empty "
    "tool menu or absence of a discovered issue. Preserve directly observable findings as "
    "well as uncertainty. Return only the existing report object, ordinarily at most 600 "
    "words without hiding material uncertainty."
)
SOURCE_PAIR_BRIEF = (
    "Using only the captured consumer and supplied before/after callee sources, produce "
    "the existing full report. In claims, identify the captured source identities and "
    "scope, compare accepted callee parameters across the supplied signatures, and identify "
    "the arguments actually forwarded by the captured call. Relate the material parameter "
    "changes to that actual call: distinguish a supported source-level effect, a change "
    "that does not affect this call, and a relationship that remains unresolved. Cite the "
    "passages needed for each side of a material relation. Do not invent forwarded "
    "arguments or substitute general library knowledge for the supplied call. These "
    "reference sources are not the target's observed installation or execution; a scoped "
    "finding does not establish whole-update compatibility. Use existing status and "
    "missing_observation fields to distinguish source observations, inferences and missing "
    "bindings. Base summary, conditions and recommendation on those findings and state "
    "justified next work where needed. Return only the existing report object, ordinarily "
    "at most 600 words without hiding material uncertainty."
)


@dataclass(frozen=True)
class SuppliedEvidenceLimits:
    reads: int = 13
    references: int = 16
    operations: int = 76
    packed_input_bytes: int = 128 * 1024
    seconds: int = 900

    def __post_init__(self):
        if any(type(value) is not int or value < 1 for value in asdict(self).values()):
            raise ValueError("supplied-evidence limits must be positive integers")
        if self.reads > 13 or self.references > 16 or self.operations > 76:
            raise ValueError("supplied-evidence limits exceed the admitted fixed allowance")


def mechanical_report(packed):
    """Maximum-visible-reference structural proof, explicitly no semantic conclusion."""
    return json_bytes({
        "summary": "Mechanical report-only publication proof; semantic interpretation unassessed.",
        "claims": [{
            "statement": "These are delivered references; support for substantive conclusions is unassessed.",
            "status": "unresolved",
            "evidence": [{"kind": kind, "id": identity} for kind, identity in sorted(packed.reference_pairs)],
            "missing_observation": "Separate source-to-claim semantic review",
        }],
        "conditions": [],
        "unexamined": ["Substantive dependency interpretation and maintainer usefulness"],
        "recommendation": "No action recommendation from mechanical proof.",
        "recommendation_status": "unresolved",
        "recommendation_evidence": [],
        "recommendation_missing_observation": "Separate interpretation and decision evidence",
        "stopping_reason": "Trusted preparation finished; autonomous stopping adequacy unassessed.",
    })


class SuppliedEvidenceTrial:
    """Fresh host → trusted reads/finish → complete report packet → one publication.

    The caller owns recipes, retained input validation and deployment/batch admission.
    Each instance owns a fresh assignment/ledger. Failed preparation cannot be reused;
    a feasibility instance is terminated and cannot donate IDs/state to an inference run.
    """

    def __init__(self, assignment, requests, *, case_label, source_pair=False,
                 limits=None, clock=time.monotonic):
        if assignment.events or assignment.notes or assignment.ready:
            raise ValueError("supplied-evidence trial requires a fresh assignment")
        if not re.fullmatch(r"[a-z0-9-]{1,32}", case_label):
            raise ValueError("case label must be a short opaque wire identifier")
        self.assignment, self.requests = assignment, tuple(requests)
        self.limits = limits or SuppliedEvidenceLimits()
        if len(self.requests) > self.limits.reads:
            raise ValueError("too many trusted setup reads; no dispatch")
        for content in self.requests:
            item = decode_object(content)
            if item.get("tool") not in {"read_source", "read_native"}:
                raise ValueError("trusted setup permits only source/native reads")
        self.case_label, self.source_pair = case_label, source_pair
        self.clock, self.started = clock, clock()
        self.state = "fresh"
        self.result = None
        self.charges = {
            "admission_operations": 0, "trusted_setup_read_attempts": 0,
            "consumer_invocation_attempts": 0, "report_publication_attempts": 0,
            "assignment_composition_seconds": assignment.composition_seconds,
            "assignment_composition_publications": 2,
            "reference_visibility": "complete_supplied_packet",
            "request_producer": "trusted_diagnostic_preparation",
        }

    def prepare(self):
        if self.state != "fresh":
            raise ValueError("preparation cannot be repeated")
        self.state = "preparing"
        try:
            # Setup cannot itself overspend even if the declared limit is too small.
            # Actual reference growth is checked after real deliveries, before finish
            # or any consumer invocation; no placeholder references are manufactured.
            if 4 * len(self.requests) + 3 + 4 + 1 > self.limits.operations:
                raise ValueError("fixed packet cannot afford setup and terminal base allowance")
            for content in self.requests:
                self.charges["admission_operations"] += 4
                self.charges["trusted_setup_read_attempts"] += 1
                event = self.assignment.invoke(content)
                if event.outcome not in {"observed", "empty"}:
                    raise ValueError("required setup read unavailable/refused/failed")
                item = decode_object(content)
                if item["tool"] == "read_native":
                    delivery = json.loads(json.loads(event.content)["content"])
                    if delivery["omitted"]:
                        raise ValueError("required native packet material omitted; no prediction")
                if len(self.reference_pairs) > self.limits.references:
                    raise ValueError("supplied packet exceeds eligible-reference allowance")
            required = self.charges["admission_operations"] + 3 + 4 + len(self.reference_pairs) + 1
            if required > self.limits.operations:
                raise ValueError("fixed packet cannot afford cited report and termination")
            self.charges["admission_operations"] += 3
            event = self.assignment.invoke(json_bytes({"tool": "finish_investigation", "arguments": {}}))
            if event.outcome != "ready":
                raise ValueError("trusted procedural finish failed")
            self.state = "prepared"
            packed = self.pack()
            self.charges["preparation_seconds"] = self.clock() - self.started
            self.charges["declared_terminal_reserve"] = 4 + len(self.reference_pairs) + 1
            return packed
        except BaseException as error:
            self.state = "failed"
            try:
                self.charges["admission_operations"] += 1
                self.charges["termination_id"] = self.assignment.host.terminate(
                    self.assignment.host.lineage_id, "failed", problem_text(error)
                )
            except BaseException as secondary:
                self.charges["termination_problem"] = problem_text(secondary)
            raise

    @property
    def reference_pairs(self):
        return frozenset(pair for event in self.assignment.events for pair in event.reference_pairs)

    def protocol(self):
        protocol = protocol_definition(self.assignment, TrialLimits(
            consumer_turns=2, operations=self.limits.operations,
            packed_input_bytes=self.limits.packed_input_bytes,
            seconds=self.limits.seconds, terminal_corrections=0,
        ))
        protocol["system"] = protocol["system"].replace(
            "Investigate the declared dependency update using only offered evidence.\n"
            "Discover relevant sources and counterevidence without assuming applicability or execution.",
            "Interpret explicitly supplied evidence without assuming applicability or execution.\n"
            "Preparation/finish were trusted scripted work, not model discovery or adequacy proof.",
        )
        protocol["task"].update(
            goal=SOURCE_PAIR_BRIEF if self.source_pair else PR_BRIEF,
            case_label=self.case_label,
            diagnostic_protocol=SUPPLIED_EVIDENCE_PROTOCOL,
            prior_request_producer="trusted_diagnostic_preparation",
        )
        protocol["budget_observation"] = {
            "format": SUPPLIED_EVIDENCE_PROTOCOL,
            "limits": asdict(self.limits),
            "spent_before_report": dict(self.charges),
            "remaining_operation_units": self.limits.operations - self.charges["admission_operations"],
            "report_attempts_remaining": 1,
            "required_terminal_units": 4 + len(self.reference_pairs) + 1,
            "limit": "Capacity for contract-valid publication, not semantic or latency success.",
        }
        return protocol

    def pack(self, consumer=None):
        if self.state != "prepared":
            raise ValueError("supplied packet is not prepared")
        packer = (
            consumer.pack_complete if consumer is not None and hasattr(consumer, "pack_complete")
            else consumer.pack if consumer is not None and hasattr(consumer, "pack") else pack_input
        )
        packed = packer(
            self.protocol(), self.assignment.events, "report", self.limits.packed_input_bytes
        )
        if packed.omitted_event_ids or packed.reference_pairs != self.reference_pairs:
            raise ValueError("required supplied-packet material omitted; no prediction")
        return packed

    def run(self, consumer):
        """One unmodified response; failed/unknown/interrupted work receives no retry."""
        packed = self.pack(consumer)
        self.state = "attempted"
        self.charges["consumer_invocation_attempts"] += 1
        response = publication = termination = primary = traceback = None
        outcome, problem = "failed", None
        started = self.clock()
        try:
            response = consumer(packed)
            if type(response) is not bytes:
                raise ValueError("consumer must return exact bytes")
            if self.clock() - started >= self.limits.seconds:
                raise ValueError("report deadline reached; complete response retained without dispatch")
        except BaseException as error:
            primary, traceback, problem = error, error.__traceback__, problem_text(error)
        self.charges["consumer_elapsed_seconds"] = self.clock() - started
        finalizing = self.clock()
        # Share the finalization allowance left by the model boundary. Scripted proof
        # has no transport finalization spend. No nested timer wraps model prediction.
        receipts = getattr(consumer, "receipts", [])
        spent = 0
        if receipts:
            last = receipts[-1]
            spent = last.get("finalization_elapsed_seconds", 0)
        try:
            finalization_cap = getattr(getattr(consumer, "limits", None), "finalization_seconds", 60)
            expires = getattr(consumer, "finalization_expires", None)
            remaining = expires - self.clock() if expires is not None else finalization_cap - spent
            if remaining <= 0:
                raise PredictionDeadlineExceeded("model consumed the shared finalization allowance")
            with MonotonicDeadline(remaining, clock=self.clock, label="report/termination").enforce():
                try:
                    if primary is None:
                        cost = _admission_charge(self.assignment, response, True)
                        if self.charges["admission_operations"] + cost + 1 > self.limits.operations:
                            raise ValueError("report exceeds protected terminal allowance")
                        self.charges["admission_operations"] += cost
                        self.charges["report_publication_attempts"] += 1
                        publication = self.assignment.publish_report(response, visible=packed.reference_ids)
                        outcome = "completed"
                except BaseException as error:
                    primary, traceback, problem = error, error.__traceback__, problem_text(error)
                finally:
                    self.charges["admission_operations"] += 1
                    try:
                        termination = self.assignment.host.terminate(
                            self.assignment.host.lineage_id, outcome,
                            problem or "Report-only procedural result; semantic adequacy unassessed.",
                        )
                    except BaseException as error:
                        self.charges["termination_problem"] = problem_text(error)
                        outcome = "failed"
                        if primary is None:
                            primary, traceback, problem = error, error.__traceback__, problem_text(error)
        except BaseException as error:
            self.charges["finalization_problem"] = problem_text(error)
            outcome = "failed"
            if primary is None:
                primary, traceback, problem = error, error.__traceback__, problem_text(error)
        self.charges.update(
            elapsed_seconds=self.clock() - started,
            report_finalization_elapsed_seconds=self.clock() - finalizing,
            total_finalization_elapsed_seconds=self.clock() - getattr(consumer, "finalization_started", finalizing),
            access_receipts=[asdict(receipt) for receipt in self.assignment.access.receipts],
            model_calls=len(receipts),
            model_usage_complete=getattr(consumer, "usage_complete", None),
            model_tokens={"input": consumer.input_tokens, "generated": consumer.output_tokens}
            if receipts and consumer.usage_complete else None,
        )
        self.result = ScriptedTrialResult(
            outcome, (response,), (packed,), publication, termination, dict(self.charges), problem
        )
        self.assignment.last_trial_result = self.result
        self.state = "terminated" if termination else "failed"
        if primary is not None and not isinstance(primary, Exception):
            raise primary.with_traceback(traceback)
        return self.result
