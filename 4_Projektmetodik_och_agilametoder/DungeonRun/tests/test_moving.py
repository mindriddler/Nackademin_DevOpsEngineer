from unittest import mock
from data.Maping import Maping


@mock.patch("builtins.input", result="left")
def test_moveleft_into_wall(mocked_input):
    class_init = Maping(currpos=(0, 0),
                        map=[
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                        ])
    assert class_init.moveleft() == ([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ])


def test_moveleft():
    class_init = Maping(currpos=(1, 1),
                        map=[
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                        ])
    assert class_init.moveleft() == ([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ])


def test_moveright():
    class_init = Maping(currpos=(0, 0),
                        map=[
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                        ])
    assert class_init.moveright() == ([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ])


def test_movedown():
    class_init = Maping(currpos=(0, 0),
                        map=[
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                        ])
    assert class_init.movedown() == ([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ])


def test_moveup():
    class_init = Maping(currpos=(1, 1),
                        map=[
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                        ])
    assert class_init.moveup() == ([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ])
