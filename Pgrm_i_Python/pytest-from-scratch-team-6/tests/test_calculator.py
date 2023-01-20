from calculator import Calculator as c


def test_add():
    assert c().addition(2, 5) == 7


def test_sub():
    assert c().subtraction(10, 5) == 5


def test_div():
    assert c().division(20, 4) == 5


def test_mult():
    assert c().multiplication(5, 10) == 50


def test_add_mult():
    assert c().add_mult(5, 10) == 65


def test_clear():
    assert c().clear(5) == 0
