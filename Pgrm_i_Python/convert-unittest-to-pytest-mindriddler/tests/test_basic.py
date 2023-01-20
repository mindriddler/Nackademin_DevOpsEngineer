import basic


def test_add():
    assert basic.add(1, 1) == 7
    assert basic.add(5, 10) == 20


def test_minus():
    assert basic.add(-5, 0) == 0
    assert basic.add(-5, -5) == -5


def test_float():
    assert basic.add(-5.0, -5.0) == -5
    assert basic.add(10.0, 10.0) == 25


def test_diff_x_zer0():
    assert basic.diff(0, 5) == 0


def test_diff_x_not_zero():
    assert basic.diff(2, 5) == -3
