from typing import List, Protocol
import pandas as pd
from .operations import get_operation
from .input_validators import validate_two_numbers
from .calculation import Calculation
from .history import HistoryManager
from .calculator_config import CONFIG, BASE_DIR
from .logger import logger
from .exceptions import CalculatorError


class Observer(Protocol):
    def update(self, calculation: Calculation):
        ...


class LoggingObserver:
    def update(self, calculation: Calculation):
        logger.info(
            f"Performed {calculation.operation}({calculation.a}, {calculation.b}) = {calculation.result}"
        )


class AutoSaveObserver:
    def __init__(self):
        self.filepath = BASE_DIR / CONFIG["HISTORY_FILE"]

    def update(self, calculation: Calculation):
        try:
            df = pd.read_csv(self.filepath)
        except FileNotFoundError:  # pragma: no cover
            df = pd.DataFrame(columns=["operation", "a", "b", "result", "timestamp"])
        new_row = {
            "operation": calculation.operation,
            "a": calculation.a,
            "b": calculation.b,
            "result": calculation.result,
            "timestamp": calculation.timestamp,
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(self.filepath, index=False)


class Calculator:
    def __init__(self):
        self.history = HistoryManager()
        self.observers: List[Observer] = []
        self.register_observer(LoggingObserver())
        if CONFIG.get("AUTO_SAVE", False):
            self.register_observer(AutoSaveObserver())

    def register_observer(self, observer: Observer):
        self.observers.append(observer)

    def notify_observers(self, calculation: Calculation):
        for obs in self.observers:
            try:
                obs.update(calculation)
            except Exception as e:  # pragma: no cover
                logger.error(f"Observer error: {e}")

    def calculate(self, operation_name: str, a, b) -> Calculation:
        a, b = validate_two_numbers(a, b)
        operation = get_operation(operation_name)
        try:
            result = operation.execute(a, b)
        except CalculatorError:  # pragma: no cover
            raise
        except Exception as e:  # pragma: no cover ← exclude these lines
            logger.error(f"Unexpected error during {operation_name}: {e}")
            raise CalculatorError(str(e)) # pragma: no cover

        calculation = Calculation(operation=operation_name, a=a, b=b, result=result)
        self.history.add(calculation)
        self.notify_observers(calculation)
        return calculation

    def save_history(self):
        filepath = BASE_DIR / CONFIG["HISTORY_FILE"]
        data = [
            {
                "operation": c.operation,
                "a": c.a,
                "b": c.b,
                "result": c.result,
                "timestamp": c.timestamp,
            }
            for c in self.history.list()
        ]
        pd.DataFrame(data).to_csv(filepath, index=False)

    def load_history(self):
        filepath = BASE_DIR / CONFIG["HISTORY_FILE"]
        try:
            df = pd.read_csv(filepath)
        except FileNotFoundError:  # pragma: no cover
            logger.warning("History file not found, starting fresh.")
            return
        self.history.clear()
        for _, row in df.iterrows():
            calc = Calculation(
                operation=row["operation"],
                a=float(row["a"]),
                b=float(row["b"]),
                result=float(row["result"]),
                timestamp=row["timestamp"],
            )
            self.history.add(calc)
