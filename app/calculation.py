"""
Data model representing a single calculation.

Using dataclass keeps the code concise and readable.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Calculation:
    """
    Represents one calculator operation record.
    """
    operand1: float
    operand2: float
    operation: str
    result: float

    # Timestamp helps track when calculation occurred
    timestamp: datetime = datetime.now()