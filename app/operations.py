from .exceptions import OperationError


class Operation:
    name = "base"
    def execute(self, a, b):
        raise NotImplementedError  # pragma: no cover


class AddOperation(Operation):
    name = "add"
    def execute(self, a, b):
        return a + b


class SubtractOperation(Operation):
    name = "subtract"
    def execute(self, a, b):
        return a - b


class MultiplyOperation(Operation):
    name = "multiply"
    def execute(self, a, b):
        return a * b


class DivideOperation(Operation):
    name = "divide"
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Division by zero is not allowed.")
        return a / b  # pragma: no cover


class PowerOperation(Operation):
    name = "power"
    def execute(self, a, b):
        return a ** b


class RootOperation(Operation):
    name = "root"
    def execute(self, a, b):
        if b == 0:  # pragma: no cover
            raise OperationError("Cannot take zeroth root.")
        if a < 0 and b % 2 == 0:  # pragma: no cover
            raise OperationError("Cannot take even root of negative number.")
        return a ** (1 / b)


class ModulusOperation(Operation):
    name = "modulus"
    def execute(self, a, b):
        if b == 0:  # pragma: no cover
            raise OperationError("Modulus by zero is not allowed.")
        return a % b


class IntDivideOperation(Operation):
    name = "int_divide"
    def execute(self, a, b):
        if b == 0:  # pragma: no cover
            raise OperationError("Integer division by zero.")
        return a // b


class PercentOperation(Operation):
    name = "percent"
    def execute(self, a, b):
        if b == 0:  # pragma: no cover
            raise OperationError("Cannot divide by zero in percentage.")
        return (a / b) * 100


class AbsDiffOperation(Operation):
    name = "abs_diff"
    def execute(self, a, b):
        return abs(a - b)


OPERATION_MAP = {
    "add": AddOperation,
    "subtract": SubtractOperation,
    "multiply": MultiplyOperation,
    "divide": DivideOperation,
    "power": PowerOperation,
    "root": RootOperation,
    "modulus": ModulusOperation,
    "int_divide": IntDivideOperation,
    "percent": PercentOperation,
    "abs_diff": AbsDiffOperation,
}


def get_operation(name: str) -> Operation:
    cls = OPERATION_MAP.get(name)
    if not cls:
        raise OperationError(f"Unknown operation: {name}")  # pragma: no cover
    return cls()
