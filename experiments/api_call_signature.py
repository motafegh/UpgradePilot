"""Historical experimental imports for the product-owned source analyzer.

Fixed old envelopes retain their readers; new extraction/comparison delegates to
one implementation in upgradepilot.caller_signature.analysis. This compatibility
surface grants no additional product/runtime authority.
"""
from upgradepilot.caller_signature.analysis import (
    METHOD_VERSION, ReceiverMode, ParameterKind, SourceSpan, fact_identity,
    CallArguments, ParameterFact, CallableSignature, SourceFacts, AnalysisLimit,
    KeywordReception, BindingViolation, ArgumentComparison,
    extract_python_source, compare_arguments,
)
