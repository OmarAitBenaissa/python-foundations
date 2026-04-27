from calc.operations import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 
    assert add(1.5, 2.5) == 4.0
    assert add(1.5, 2.5) == 4.0
    assert add(Decimal("1.5"), Decimal("2.5")) == Decimal("4.0")

def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(1.5, 2.5) == -1.0
    assert subtract(1.5, 2.5) == -1.0
    assert subtract(Decimal("1.5"), Decimal("2.5")) == Decimal("-1.0")

def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(1.5, 2.5) == 3.75
    assert multiply(1.5, 2.5) == 3.75
    assert multiply(Decimal("1.5"), Decimal("2.5")) == Decimal("3.75")