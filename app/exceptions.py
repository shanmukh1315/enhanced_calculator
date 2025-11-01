class CalculatorError(Exception):
    """Base class for all calculator-related errors."""
    pass


class OperationError(CalculatorError):
    """Raised when an arithmetic operation fails."""
    pass


class ValidationError(CalculatorError):
    """Raised when input validation fails (non-numeric, out of range, etc.)."""
    pass
