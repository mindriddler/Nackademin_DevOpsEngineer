import unittest
from basic import line, diff_twist


class BasicTestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(line(1, 1, 0), 1)

    def test_diff_twist(self):
        self.assertEqual(diff_twist(0, 5), 0)

    def test_diff_twist_x_1(self):
        self.assertEqual(diff_twist(1, 5), -4)


if __name__ == '__main__':
    unittest.main()
