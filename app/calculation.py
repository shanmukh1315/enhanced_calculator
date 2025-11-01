"""
calculation.py
Defines the Calculation data structure used to store operation details.
"""

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class Calculation:
    operation: str
    a: float
    b: float
    result: float
    timestamp: str = datetime.now(timezone.utc).isoformat()
