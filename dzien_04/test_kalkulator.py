from kalkulator import add, sub

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(-5, -10) == -15
    assert add (10, 0) == 10

def test_sub():
    assert sub(1, 2) == -1
    assert sub(1, -1) == 2
    assert sub(-5, -10) == 5
    assert sub (10, 0) == 10
