"""Bounded analysis and exact measurement records for native source evidence."""
from __future__ import annotations
import math
from dataclasses import dataclass, fields


@dataclass(frozen=True)
class AnalysisLimits:
    max_files: int = 32
    max_source_bytes: int = 4 * 1024 * 1024
    max_nodes_per_file: int = 100_000
    max_nodes: int = 250_000
    max_facts: int = 4096
    max_pairs: int = 256
    timeout_seconds: float = 60.0
    memory_bytes: int = 512 * 1024 * 1024

    def __post_init__(self):
        ceilings = (32, 4 * 1024 * 1024, 100_000, 250_000, 4096, 256, 60.0, 512 * 1024 * 1024)
        for field, ceiling in zip(fields(self), ceilings):
            value = getattr(self, field.name)
            expected = (int, float) if field.name == "timeout_seconds" else (int,)
            if type(value) not in expected or not 0 < value <= ceiling:
                raise ValueError("Invalid analysis limit: " + field.name)



@dataclass(frozen=True)
class MeasuredDuration:
    """An exact retained binary-float measurement, not a clock-accuracy claim."""
    seconds_hex: str
    scope: str

    def __post_init__(self):
        if type(self.seconds_hex) is not str or len(self.seconds_hex) > 64:
            raise ValueError("Invalid measured seconds.")
        try:
            seconds = float.fromhex(self.seconds_hex)
        except (ValueError, OverflowError) as error:
            raise ValueError("Invalid measured seconds.") from error
        if not math.isfinite(seconds) or seconds < 0 or seconds.hex() != self.seconds_hex:
            raise ValueError("Noncanonical measured seconds.")
        if type(self.scope) is not str or not self.scope.strip() or len(self.scope) > 256:
            raise ValueError("Invalid measurement scope.")

    @classmethod
    def from_seconds(cls, seconds: float, scope: str):
        if type(seconds) is not float:
            raise ValueError("Expected an actual float measurement.")
        return cls(seconds.hex(), scope)

    @property
    def seconds(self) -> float:
        return float.fromhex(self.seconds_hex)
