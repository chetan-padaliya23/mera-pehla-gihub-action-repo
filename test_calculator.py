import pytest
from calculator import add, subtract, multiply, divide


def test_add():
    assert add(5, 3) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(6, 7) == 42
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(15, 3) == 5.0
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
