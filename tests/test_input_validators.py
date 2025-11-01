import pytest
from app.input_validators import validate_number, validate_two_numbers
from app.exceptions import ValidationError

def test_valid_numbers():
    assert validate_number("5") == 5.0
    assert validate_two_numbers("3", "7") == (3.0, 7.0)

def test_invalid_input():
    with pytest.raises(ValidationError):
        validate_number("abc")

def test_overflow():
    with pytest.raises(ValidationError):
        validate_number(999999999)
