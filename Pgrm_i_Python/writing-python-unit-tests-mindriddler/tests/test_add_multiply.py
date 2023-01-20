import unittest
from basic import add_multiply


class MyFirstTest(unittest.TestCase):

    def test_add_multiply(self):
        self.assertEqual(add_multiply(5, 7), 24)
        # First number = x, second number = y, third number = the expected outcome


if __name__ == '__main__':
    unittest.main()
