"""Historical binding imports and experiment-specific observation projection.

The single active analyzer lives in upgradepilot.caller_signature.bindings.
This adapter preserves experimental imports and saved manifest shapes; it does
not maintain a separate analysis implementation or native capture authority.
"""
from dataclasses import asdict, fields
from upgradepilot.caller_signature.bindings import (
    BINDING_ANALYSIS_VERSION, MAX_BINDING_ORIGINS, MAX_BINDING_TRACE_STEPS,
    ImportFact, BindingTraceStep, BindingAssessment, ReferenceFact,
    binding_state, analyze_python_bindings,
)


def python_facts_manifest(imports, references) -> dict:
    """Intern source trace steps once; indices preserve each assessment's trace.

    Native facts remain typed. This version-2 saved representation avoids copying
    the same import/assignment history into every reference and exceeding the
    existing replay input budget. Tables are local to one target/sample packet.
    """
    steps = []
    indices = {}
    records = []
    for reference in references:
        record = {
            field.name: getattr(reference, field.name)
            for field in fields(reference)
            if field.name != "binding"
        }
        binding = reference.binding
        record["binding"] = None
        if binding is not None:
            trace = []
            for step in binding.trace:
                if step not in indices:
                    indices[step] = len(steps)
                    steps.append(asdict(step))
                trace.append(indices[step])
            record["binding"] = {
                field.name: getattr(binding, field.name)
                for field in fields(binding)
                if field.name != "trace"
            }
            record["binding"]["trace"] = trace
        records.append(record)
    return {
        "binding_analysis_version": BINDING_ANALYSIS_VERSION,
        "binding_trace_steps": steps,
        "imports": [asdict(fact) for fact in imports],
        "references": records,
    }
