from .exceptions import ValidationError
from .calculator_config import CONFIG


def validate_number(value):
    """
    Validates that the provided value can be converted to a float
    and is within the configured maximum input range.
    """
    try:
        num = float(value)
    except (TypeError, ValueError):
        raise ValidationError(f"Invalid number: {value}")

    if abs(num) > CONFIG["MAX_INPUT_VALUE"]:
        raise ValidationError(
            f"Input {num} exceeds maximum allowed value ({CONFIG['MAX_INPUT_VALUE']})"
        )
    return num


def validate_two_numbers(a, b):
    """
    Validates both inputs and returns them as floats.
    """
    return validate_number(a), validate_number(b)
