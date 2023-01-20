from data.Maping import Maping
from unittest import mock


@mock.patch("builtins.input", side_effect=["wrong_input_test", " ", "small"])
def test_get_map_size_wrong(mocked_input):
    class_init = Maping()
    assert class_init.get_map_size() == (4, 4, "small")


@mock.patch("builtins.input", side_effect=["small"])
def test_get_map_size_small(mocked_input):
    class_init = Maping()
    assert class_init.get_map_size() == (4, 4, "small")


@mock.patch("builtins.input", side_effect=["medium"])
def test_get_map_size_medium(mocked_input):
    class_init = Maping()
    assert class_init.get_map_size() == (5, 5, "medium")


@mock.patch("builtins.input", side_effect=["large"])
def test_get_map_size_large(mocked_input):
    class_init = Maping()
    assert class_init.get_map_size() == (8, 8, "large")


# @mock.patch("builtins.input", side_effect=["small"])
# def test_create_map_small(mocked_input):
#     class_init = Maping()
#     assert class_init.create_map() == (4, 4, "small", [
#         ['O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O'],
#     ])

# @mock.patch("builtins.input", side_effect=["medium"])
# def test_create_map_medium(mocked_input):
#     class_init = Maping()
#     assert class_init.create_map() == (5, 5, "medium",
#                                        [['O', 'O', 'O', 'O', 'O'],
#                                         ['O', 'O', 'O', 'O', 'O'],
#                                         ['O', 'O', 'O', 'O', 'O'],
#                                         ['O', 'O', 'O', 'O', 'O'],
#                                         ['O', 'O', 'O', 'O', 'O']])

# @mock.patch("builtins.input", side_effect=["large"])
# def test_create_map_large(mocked_input):
#     class_init = Maping()
#     assert class_init.create_map() == (8, 8, "large", [
#         ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#     ])

# @mock.patch("builtins.input", side_effect=["top left"])
# def test_start_location_top_left(mocked_input):
#     class_init = Maping(width=4,
#                         length=4,
#                         map=[
#                             [0, 0, 0, 0],
#                             [0, 0, 0, 0],
#                             [0, 0, 0, 0],
#                             [0, 0, 0, 0],
#                         ])
#     assert class_init.start_location() == ([
#         [0, 0, 0, 0],
#         [0, 0, 0, 0],
#         [0, 0, 0, 0],
#         [0, 0, 0, 0],
#     ])

# @mock.patch("builtins.input", side_effect=["top right"])
# def test_start_location_top_right(mocked_input):
#     class_init = Maping(width=4,
#                         length=4,
#                         map=[
#                             [0, 0, 0, 0],
#                             [0, 0, 0, 0],
#                             [0, 0, 0, 0],
#                             [0, 0, 0, 0],
#                         ])
#     assert class_init.start_location() == ([
#         [0, 0, 0, "P"],
#         [0, 0, 0, 0],
#         [0, 0, 0, 0],
#         [0, 0, 0, 0],
#     ])

# @mock.patch("builtins.input", side_effect=["bottom left"])
# def test_start_location_bottom_left(mocked_input):
#     class_init = Maping(width=4,
#                         length=4,
#                         map=[
#                             [0, 0, 0, 0],
#                             [0, 0, 0, 0],
#                             [0, 0, 0, 0],
#                             [0, 0, 0, 0],
#                         ])
#     assert class_init.start_location() == ([
#         [0, 0, 0, 0],
#         [0, 0, 0, 0],
#         [0, 0, 0, 0],
#         ["P", 0, 0, 0],
#     ])

# @mock.patch("builtins.input", side_effect=["bottom right"])
# def test_start_location_bottom_right(mocked_input):
#     class_init = Maping(width=4,
#                         length=4,
#                         map=[
#                             [0, 0, 0, 0],
#                             [0, 0, 0, 0],
#                             [0, 0, 0, 0],
#                             [0, 0, 0, 0],
#                         ])
#     assert class_init.start_location() == ([
#         [0, 0, 0, 0],
#         [0, 0, 0, 0],
#         [0, 0, 0, 0],
#         [0, 0, 0, 0],
#     ])

# @mock.patch("builtins.input",
#             side_effect=["test_wrong_location", "bottom right"])
# def test_start_location_wrong_location(mocked_input):
#     class_init = Maping(width=4,
#                         length=4,
#                         map=[
#                             [0, 0, 0, 0],
#                             [0, 0, 0, 0],
#                             [0, 0, 0, 0],
#                             [0, 0, 0, 0],
#                         ])
#     assert class_init.start_location() == ([
#         [0, 0, 0, 0],
#         [0, 0, 0, 0],
#         [0, 0, 0, 0],
#         [0, 0, 0, 0],
#     ])
