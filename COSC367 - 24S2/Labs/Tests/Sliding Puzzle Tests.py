import io
import unittest

from sliding_puzzle_graph import *
from contextlib import redirect_stdout

# Inputs
graph1 = SlidingPuzzleGraph([[1, 2, 5],
                            [3, 4, 8],
                            [6, 7, ' ']])

graph2 = SlidingPuzzleGraph([[3,' '],
                            [1, 2]])

graph3 = SlidingPuzzleGraph([[1, ' ', 2],
                            [6,  4,  3],
                            [7,  8,  5]])

# Expected Outputs
expected_1 = """Actions:
  Move 8 down,
  Move 5 down,
  Move 2 right,
  Move 1 right.
Total cost: 4"""

expected_2 = """Actions:
  Move 3 right,
  Move 1 up,
  Move 2 left,
  Move 3 down,
  Move 1 right.
Total cost: 5"""

expected_3 = """Actions:
  Move 4 up,
  Move 3 left,
  Move 5 up,
  Move 8 right,
  Move 7 right,
  Move 6 down,
  Move 3 left,
  Move 4 down,
  Move 1 right.
Total cost: 9"""


class MyTestCase(unittest.TestCase):
    def test_sliding_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            solutions = generic_search(graph1, BFSFrontier())
            print_actions(next(solutions))
        output = f.getvalue().strip()
        self.assertEqual(expected_1, output)

    def test_sliding_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            solutions = generic_search(graph2, BFSFrontier())
            print_actions(next(solutions))
        output = f.getvalue().strip()
        self.assertEqual(expected_2, output)

    def test_sliding_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            solutons = generic_search(graph3, BFSFrontier())
            print_actions(next(solutons))
        output = f.getvalue().strip()
        self.assertEqual(expected_3, output)


if __name__ == '__main__':
    unittest.main()
