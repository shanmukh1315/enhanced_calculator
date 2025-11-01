from app.calculation import Calculation

def test_calculation_creation():
    calc = Calculation(operation="add", a=2, b=3, result=5)
    assert calc.operation == "add"
    assert calc.a == 2
    assert calc.b == 3
    assert calc.result == 5
