from typing import List
from .calculation import Calculation
from .calculator_memento import CalculatorMemento
from .calculator_config import CONFIG


class HistoryManager:
    def __init__(self):
        self._history: List[Calculation] = []
        self._undone: List[Calculation] = []

    def add(self, calc: Calculation):
        if len(self._history) >= CONFIG["MAX_HISTORY_SIZE"]:  # pragma: no cover
            self._history.pop(0)
        self._history.append(calc)
        self._undone.clear()

    def list(self) -> List[Calculation]:
        return list(self._history)

    def clear(self):
        self._history.clear()
        self._undone.clear()

    def save_state(self) -> CalculatorMemento:
        return CalculatorMemento(history=list(self._history)) # pragma: no cover

    def restore_state(self, memento: CalculatorMemento):
        self._history = list(memento.history) # pragma: no cover

    def undo(self):
        if not self._history:  # pragma: no cover
            return None
        last = self._history.pop()
        self._undone.append(last)
        return last

    def redo(self):
        if not self._undone:  # pragma: no cover
            return None
        item = self._undone.pop()
        self._history.append(item)
        return item
