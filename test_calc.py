from build import calc


def test_multiply():
    assert calc.multiply(3, 2) == 6


def test_add():
    assert calc.add(3, 2) == 5


def test_divide():
    assert calc.divide(3, 2) == 1  # int / int


def test_subtract():
    assert calc.subtract(3, 2) == 1
