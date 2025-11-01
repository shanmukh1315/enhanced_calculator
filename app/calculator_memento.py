from dataclasses import dataclass
from typing import List
from .calculation import Calculation


@dataclass
class CalculatorMemento:
    """
    Stores the state (history) of the calculator to enable undo/redo.
    """
    history: List[Calculation]
