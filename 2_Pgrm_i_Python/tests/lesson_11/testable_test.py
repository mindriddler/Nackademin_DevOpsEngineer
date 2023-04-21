from lesson_11.example import testable_main


def test_this_will_fail():
    assert testable_main.add(1, 1) == 2


def test_greet_user():
    assert testable_main.greet_user("Mrs Oprah") == "hello Mrs Oprah"


def test_calculate_user_tuple():
    assert testable_main.calculate_user_input((2, 5)) == 7


def test_user_input():
    assert testable_main.get_user_input(lambda x: 1) == (1, 1)
