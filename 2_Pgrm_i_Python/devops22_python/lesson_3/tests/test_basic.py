import basic


def test_add():
    assert basic.add(1, 1) == 7
    assert basic.add(5, 10) == 20


def test_minus():
    assert basic.add(-5, 0) == 0
    assert basic.add(-5, -5) == -5


def test_float():
    assert basic.add(-5.0, -5.0) == -5.0
    assert basic.add(10.0, 10.0) == 25.0


def test_diff():
    assert basic.diff(1, 1) == 0


def test_diff_below_zero():
    assert basic.diff(0, 1) == 0
