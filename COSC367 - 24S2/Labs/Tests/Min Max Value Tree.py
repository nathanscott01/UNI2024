import unittest
import io
from contextlib import redirect_stdout
from min_max_value import *

# Expected Outputs
expected1 = """Root utility for minimiser: 3
Root utility for maximiser: 3"""

expected2 = """Root utility for minimiser: 1
Root utility for maximiser: 3"""

expected3 = """1
3"""

expected4 = """2
3"""


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            game_tree = 3
            print("Root utility for minimiser:", min_value(game_tree))
            print("Root utility for maximiser:", max_value(game_tree))
        output = f.getvalue().strip()
        self.assertEqual(expected1, output)

    def test_example2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            game_tree = [1, 2, 3]
            print("Root utility for minimiser:", min_value(game_tree))
            print("Root utility for maximiser:", max_value(game_tree))
        output = f.getvalue().strip()
        self.assertEqual(expected2, output)

    def test_example3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            game_tree = [1, 2, [3]]
            print(min_value(game_tree))
            print(max_value(game_tree))
        output = f.getvalue().strip()
        self.assertEqual(expected3, output)

    def test_example4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            game_tree = [[1, 2], [3]]
            print(min_value(game_tree))
            print(max_value(game_tree))
        output = f.getvalue().strip()
        self.assertEqual(expected4, output)


if __name__ == '__main__':
    unittest.main()
