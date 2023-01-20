import unittest
from _functions import rec_calc, tri_calc, return_value_above_2, return_string, return_sum, return_product


class TestFunctions(unittest.TestCase):

    def test_rec_calc(self):
        self.assertEqual(rec_calc(2, 3), 6)

    def test_tri_calc(self):
        self.assertEqual(tri_calc(2, 3), 3)

    def test_return_value_above_2(self):
        self.assertEqual(return_value_above_2(3), True)

    def test_return_value_below_2(self):
        self.assertEqual(return_value_above_2(1), False)

    def test_return_string(self):
        self.assertEqual(return_string("John", "Doe"), "hello John Doe")

    def test_return_sum(self):
        self.assertEqual(return_sum(1, 2, 3), 6)

    def test_return_product(self):
        self.assertEqual(return_product(1, 2, 3), 6)


if __name__ == '__main__':
    unittest.main()
