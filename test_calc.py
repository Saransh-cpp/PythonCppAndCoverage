import pytest
from calc_py import add, subtract, multiply, divide


def test_multiply():
    assert multiply(3, 2, "python") == 6
    assert multiply(3, 2, "cpp") == 6
    with pytest.raises(ValueError):
        multiply(3, 2, "java")


def test_add():
    assert add(3, 2, "python") == 5
    assert add(3, 2, "cpp") == 5
    with pytest.raises(ValueError):
        add(3, 2, "java")


def test_divide():
    assert divide(3, 2, "python") == 3 / 2
    assert divide(3, 2, "cpp") == 1  # int / int
    with pytest.raises(ValueError):
        divide(3, 2, "java")
    with pytest.raises(ValueError):
        divide(3, 0, "python")


def test_subtract():
    assert subtract(3, 2, "python") == 1
    assert subtract(3, 2, "cpp") == 1
    with pytest.raises(ValueError):
        subtract(3, 2, "java")
