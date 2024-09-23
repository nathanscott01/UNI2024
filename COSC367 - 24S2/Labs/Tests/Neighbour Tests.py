import unittest
import io
from contextlib import redirect_stdout
from neighbours import n_queens_neighbours as neighbours

# Expected Outputs
expected1 = """[(2, 1)]"""

expected2 = """[(1, 2, 3), (2, 3, 1), (3, 1, 2)]"""

expected3 = """[(1, 3, 2), (2, 1, 3), (3, 2, 1)]"""

expected4 = """[]"""

expected5 = """(1, 2, 3, 4, 5, 6, 8, 7)
(1, 2, 3, 4, 5, 7, 6, 8)
(1, 2, 3, 4, 5, 8, 7, 6)
(1, 2, 3, 4, 6, 5, 7, 8)
(1, 2, 3, 4, 7, 6, 5, 8)
(1, 2, 3, 4, 8, 6, 7, 5)
(1, 2, 3, 5, 4, 6, 7, 8)
(1, 2, 3, 6, 5, 4, 7, 8)
(1, 2, 3, 7, 5, 6, 4, 8)
(1, 2, 3, 8, 5, 6, 7, 4)
(1, 2, 4, 3, 5, 6, 7, 8)
(1, 2, 5, 4, 3, 6, 7, 8)
(1, 2, 6, 4, 5, 3, 7, 8)
(1, 2, 7, 4, 5, 6, 3, 8)
(1, 2, 8, 4, 5, 6, 7, 3)
(1, 3, 2, 4, 5, 6, 7, 8)
(1, 4, 3, 2, 5, 6, 7, 8)
(1, 5, 3, 4, 2, 6, 7, 8)
(1, 6, 3, 4, 5, 2, 7, 8)
(1, 7, 3, 4, 5, 6, 2, 8)
(1, 8, 3, 4, 5, 6, 7, 2)
(2, 1, 3, 4, 5, 6, 7, 8)
(3, 2, 1, 4, 5, 6, 7, 8)
(4, 2, 3, 1, 5, 6, 7, 8)
(5, 2, 3, 4, 1, 6, 7, 8)
(6, 2, 3, 4, 5, 1, 7, 8)
(7, 2, 3, 4, 5, 6, 1, 8)
(8, 2, 3, 4, 5, 6, 7, 1)"""

expected6 = """(1, 3, 2, 4)
(2, 1, 3, 4)
(2, 3, 4, 1)
(2, 4, 1, 3)
(3, 2, 1, 4)
(4, 3, 1, 2)"""


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            print(neighbours((1, 2)))
        output = f.getvalue().strip()
        self.assertEqual(expected1, output)

    def test_example2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            print(neighbours((1, 3, 2)))
        output = f.getvalue().strip()
        self.assertEqual(expected2, output)

    def test_example3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            print(neighbours((1, 2, 3)))
        output = f.getvalue().strip()
        self.assertEqual(expected3, output)

    def test_example4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            print(neighbours((1,)))
        output = f.getvalue().strip()
        self.assertEqual(expected4, output)

    def test_example5(self):
        f = io.StringIO()
        with redirect_stdout(f):
            for neighbour in neighbours((1, 2, 3, 4, 5, 6, 7, 8)):
                print(neighbour)
        output = f.getvalue().strip()
        self.assertEqual(expected5, output)

    def test_example6(self):
        f = io.StringIO()
        with redirect_stdout(f):
            for neighbour in neighbours((2, 3, 1, 4)):
                print(neighbour)
        output = f.getvalue().strip()
        self.assertEqual(expected6, output)


if __name__ == '__main__':
    unittest.main()
