import unittest
import io
from contextlib import redirect_stdout
from neighbours import n_queens_cost as cost


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        output = cost((1, 2))
        self.assertEqual(1, output)

    def test_example2(self):
        output = cost((1, 3, 2))
        self.assertEqual(1, output)

    def test_example3(self):
        output = cost((1, 2, 3))
        self.assertEqual(3, output)

    def test_example4(self):
        output = cost((1,))
        self.assertEqual(0, output)

    def test_example5(self):
        output = cost((1, 2, 3, 4, 5, 6, 7, 8))
        self.assertEqual(28, output)

    def test_example6(self):
        output = cost((2, 3, 1, 4))
        self.assertEqual(1, output)


if __name__ == '__main__':
    unittest.main()
