import unittest
import math
import io
from contextlib import redirect_stdout
from routing_table import *

# Input Graphs
map_str1 = """\
+-------+
|   G   |
|       |
|   S   |
+-------+
"""

map_str2 = """\
+-------+
|  GG   |
|S    G |
|  S    |
+-------+
"""

map_str3 = """\
+-------+
|     XG|
|X XXX  |
| S     |
+-------+
"""

map_str4 = """\
+-------+
|  F  X |
|X XXXXG|
| 3     |
+-------+
"""

map_str5 = """\
+--+
|GS|
+--+
"""

map_str6 = """\
+---+
|GF2|
+---+
"""

map_str7 = """\
+----+
| S  |
| SX |
|GX G|
+----+
"""

map_str8 = """\
+---------+
|         |
|    G    |
|         |
+---------+
"""


# Expected outputs
expected1 = """Actions:
  N,
  N.
Total cost: 10"""

expected2 = """Actions:
  N,
  N.
Total cost: 10"""

expected3 = """Actions:
  E,
  E,
  E,
  NE,
  NE.
Total cost: 29"""

expected4 = """Actions:
  N,
  NE,
  Fuel up,
  SW,
  SE,
  E,
  E,
  E,
  NE.
Total cost: 63"""

expected5 = """Actions:
  W.
Total cost: 5"""

expected6 = """Actions:
  W,
  W.
Total cost: 10"""

expected7 = """Actions:
  SW.
Total cost: 7"""

expected8 = """There is no solution!"""


class MyTestCase(unittest.TestCase):
    def test_map1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            map_graph = RoutingGraph(map_str1)
            frontier = AStarFrontier(map_graph)
            solution = next(generic_search(map_graph, frontier), None)
            print_actions(solution)
        output = f.getvalue().strip()
        self.assertEqual(expected1, output)

    def test_map2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            map_graph = RoutingGraph(map_str2)
            frontier = AStarFrontier(map_graph)
            solution = next(generic_search(map_graph, frontier), None)
            print_actions(solution)
        output = f.getvalue().strip()
        self.assertEqual(expected2, output)

    def test_map3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            map_graph = RoutingGraph(map_str3)
            frontier = AStarFrontier(map_graph)
            solution = next(generic_search(map_graph, frontier), None)
            print_actions(solution)
        output = f.getvalue().strip()
        self.assertEqual(expected3, output)

    def test_map4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            map_graph = RoutingGraph(map_str4)
            frontier = AStarFrontier(map_graph)
            solution = next(generic_search(map_graph, frontier), None)
            print_actions(solution)
        output = f.getvalue().strip()
        self.assertEqual(expected4, output)

    def test_map5(self):
        f = io.StringIO()
        with redirect_stdout(f):
            map_graph = RoutingGraph(map_str5)
            frontier = AStarFrontier(map_graph)
            solution = next(generic_search(map_graph, frontier), None)
            print_actions(solution)
        output = f.getvalue().strip()
        self.assertEqual(expected5, output)

    def test_map6(self):
        f = io.StringIO()
        with redirect_stdout(f):
            map_graph = RoutingGraph(map_str6)
            frontier = AStarFrontier(map_graph)
            solution = next(generic_search(map_graph, frontier), None)
            print_actions(solution)
        output = f.getvalue().strip()
        self.assertEqual(expected6, output)

    def test_map7(self):
        f = io.StringIO()
        with redirect_stdout(f):
            map_graph = RoutingGraph(map_str7)
            frontier = AStarFrontier(map_graph)
            solution = next(generic_search(map_graph, frontier), None)
            print_actions(solution)
        output = f.getvalue().strip()
        self.assertEqual(expected7, output)

    def test_map8(self):
        f = io.StringIO()
        with redirect_stdout(f):
            map_graph = RoutingGraph(map_str8)
            frontier = AStarFrontier(map_graph)
            solution = next(generic_search(map_graph, frontier), None)
            print_actions(solution)
        output = f.getvalue().strip()
        self.assertEqual(expected7, output)


if __name__ == '__main__':
    unittest.main()
