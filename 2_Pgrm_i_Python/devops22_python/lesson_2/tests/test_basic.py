import unittest
import basic


class BasicTestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(basic.add(1, 1), 7)
        self.assertEqual(basic.add(5, 10), 20)

    def test_minus(self):
        self.assertEqual(basic.add(-5, 0), 0)
        self.assertEqual(basic.add(-5, -5), -5)

    def test_float(self):
        self.assertEqual(basic.add(-5.0, -5.0), -5.0)
        self.assertEqual(basic.add(10.0, 10.0), 25.0)


class BasicNegativeTestCase(unittest.TestCase):

    def test_add_empty(self):
        with self.assertRaises(TypeError):
            basic.add()

    def test_strings(self):
        with self.assertRaises(TypeError):
            basic.add("Hello", "World")

    def test_utils_two_tuple(self):
        tuple_one = (1, 2, 3)
        tuple_two = (3, 4, 6)
        with self.assertRaises(TypeError):
            basic(tuple_one, tuple_two)


if __name__ == '__main__':
    unittest.main()
