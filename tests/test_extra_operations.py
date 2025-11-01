from app.operations import get_operation
from app.exceptions import OperationError
import pytest

@pytest.mark.parametrize("op,a,b,expected", [
    ("root", 16, 2, 4.0),
    ("abs_diff", 10, 6, 4.0),
])
def test_extra_operations(op, a, b, expected):
    operation = get_operation(op)
    result = operation.execute(a, b)
    assert round(result, 2) == expected

def test_divide_by_zero():
    op = get_operation("divide")
    with pytest.raises(OperationError):
        op.execute(5, 0)
