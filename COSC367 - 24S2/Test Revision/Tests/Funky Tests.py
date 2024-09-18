import io
import unittest

from funky_numeric import *
from contextlib import redirect_stdout
from itertools import dropwhile

# Expected Outputs
expected_1 = """4"""

expected_2 = """Arc(tail=7, head=6, action='1down', cost=1)
Arc(tail=7, head=9, action='2up', cost=1)"""

expected_3 = """Actions:
  1down,
  1down,
  1down.
Total cost: 3

Actions:
  1down,
  2up,
  2up,
  2up,
  2up.
Total cost: 5"""

expected_4 = """Actions:
  1down,
  2up,
  2up,
  2up,
  2up,
  2up,
  2up,
  2up,
  2up,
  2up.
Total cost: 10"""


class MyTestCase(unittest.TestCase):
    def test_funky_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            graph = FunkyNumericGraph(4)
            for node in graph.starting_nodes():
                print(node)
        output = f.getvalue().strip()
        self.assertEqual(expected_1, output)

    def test_funky_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            graph = FunkyNumericGraph(4)
            for arc in graph.outgoing_arcs(7):
                print(arc)
        output = f.getvalue().strip()
        self.assertEqual(expected_2, output)

    def test_funky_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            graph = FunkyNumericGraph(3)
            solutions = generic_search(graph, BFSFrontier())
            print_actions(next(solutions))
            print()
            print_actions(next(solutions))
        output = f.getvalue().strip()
        self.assertEqual(expected_3, output)

    def test_funky_4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            graph = FunkyNumericGraph(3)
            solutions = generic_search(graph, BFSFrontier())
            print_actions(next(dropwhile(lambda path: path[-1].head <= 10, solutions)))
        output = f.getvalue().strip()
        self.assertEqual(expected_4, output)


if __name__ == '__main__':
    unittest.main()
