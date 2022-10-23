import pytest
from kalkulator import add, sub, mul, div, kalkulator


def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(-5, -10) == -15
    assert add(10, 0) == 10


def test_sub():
    assert sub(1, 2) == -1
    assert sub(1, -1) == 2
    assert sub(-5, -10) == 5
    assert sub(10, 0) == 10


def test_mul():
    assert mul(1, 2) == 2
    assert mul(1, -1) == -1
    assert mul(-5, -10) == 50
    assert mul(10, 0) == 0


def test_div():
    assert div(1, 2) == 0.5
    assert div(1, -1) == -1.0
    assert div(-5, -10) == 0.5
    assert div(10, 0) == "Nie dziel przez zero"


@pytest.mark.parametrize(
    "op,a,b,result",
    [
        ("1", 1, 2, 3),
        ("2", 1, 2, -1),
        ("3", 1, 2, 2),
        ("4", 1, 2, 0.5),
        ("4", 1, 0, "Nie dziel przez zero"),
        ("5", 1, 2, "Nieokreślona operacja"),
    ]
)
def test_kalkulator(op, a, b, result):
    assert kalkulator(op, a, b) == result
