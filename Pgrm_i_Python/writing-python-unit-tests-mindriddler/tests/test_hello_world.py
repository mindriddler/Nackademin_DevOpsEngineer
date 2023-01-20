import unittest


class HelloWorldTestCase(unittest.TestCase):

    def test_hello(self):
        self.assertEqual("hello_world", "hello_world")


if __name__ == '__main__':
    unittest.main()
