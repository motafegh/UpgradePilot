"""Current-use checks for retained material, separate from publication predecessors.

The host supplies an original lifecycle record/basis and its current trusted bindings.
This module compares retained identities and the transitive native input closure; it does
not acquire evidence or evaluate its domain meaning. Revision inequality is not staleness.
"""

from dataclasses import dataclass
from typing import Literal

from .lifecycle_boundary import CapturedLifecycleRecord
from .lifecycle_records import LifecycleMethodIdentity
from .native_boundary import CapturedNativeBoundary


@dataclass(frozen=True, slots=True)
class MaterialBasisValidity:
    status: Literal["valid", "stale", "unsupported"]
    reasons: tuple[str, ...]


def native_material_closure(
    boundary: CapturedNativeBoundary, record_ids: tuple[str, ...]
) -> tuple[str, ...]:
    """Return the supplied roots and their actual retained inputs, without evaluation."""
    by_id = {item.record_id: item for item in boundary.records}
    pending = list(record_ids)
    found: set[str] = set()
    while pending:
        identity = pending.pop()
        if identity in found:
            continue
        if identity not in by_id:
            raise ValueError("Material reference is outside the declared native basis.")
        found.add(identity)
        pending.extend(by_id[identity].input_record_ids)
    return tuple(item.record_id for item in boundary.records if item.record_id in found)


def validate_current_material_basis(
    record: CapturedLifecycleRecord,
    original: CapturedNativeBoundary,
    current: CapturedNativeBoundary,
    *,
    original_scope: str | None,
    current_scope: str | None,
    current_method: LifecycleMethodIdentity | None,
    capability_available: bool = True,
) -> MaterialBasisValidity:
    """Validate current use, never grant current execution or semantic authority.

    Native equality includes scoped identity, bytes, input references and producer metadata.
    A changed unrelated record does not invalidate a retained material closure. Original
    reference gaps and unavailable method/capability checks block affected use explicitly.
    """
    if original.target != current.target:
        return MaterialBasisValidity("stale", ("target_changed",))
    if original_scope != current_scope:
        return MaterialBasisValidity("stale", ("scope_changed",))
    if not capability_available:
        return MaterialBasisValidity("unsupported", ("capability_unavailable",))
    if current_method is None or current_method.method is None:
        return MaterialBasisValidity("unsupported", ("method_unavailable",))
    if record.method != current_method:
        return MaterialBasisValidity("stale", ("method_changed",))
    try:
        material = native_material_closure(original, record.native_record_ids)
    except ValueError:
        return MaterialBasisValidity("unsupported", ("original_material_missing",))
    original_records = {item.record_id: item for item in original.records}
    current_records = {item.record_id: item for item in current.records}
    if any(
        current_records.get(identity) != original_records[identity]
        for identity in material
    ):
        return MaterialBasisValidity("stale", ("material_changed",))
    return MaterialBasisValidity("valid", ())
