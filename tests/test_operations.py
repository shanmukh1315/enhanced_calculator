from app.operations import get_operation

def test_add():
    op = get_operation("add")
    assert op.execute(5, 3) == 8

def test_power():
    op = get_operation("power")
    assert op.execute(2, 3) == 8

def test_modulus():
    op = get_operation("modulus")
    assert op.execute(10, 3) == 1

def test_int_divide():
    op = get_operation("int_divide")
    assert op.execute(10, 3) == 3

def test_percent():
    op = get_operation("percent")
    assert round(op.execute(50, 200), 2) == 25.0
