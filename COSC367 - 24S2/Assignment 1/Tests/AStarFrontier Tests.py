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

map_str9 = """\
+---+
| F |
| 1 |
|   |
| G |
+---+
"""

map_str10 = """\
+-----+
|  X  |
|  XSG|
|  X  |
| SX  |
+-----+"""

map_str11 = """\
+------------+
|    P       |
| 7          |
|XXXXXXXXX   |
|P F X  G    |
+------------+
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

expected9 = """Actions:
  N,
  Fuel up,
  S,
  S,
  S.
Total cost: 35"""

expected10 = """Actions:
  E.
Total cost: 5"""

expected11 = """Actions:
  E,
  E,
  NE,
  Teleport to (4, 1),
  E,
  E,
  Fuel up,
  W,
  W,
  Teleport to (1, 5),
  E,
  E,
  E,
  SE,
  SE,
  SW,
  W.
Total cost: 113"""


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
        self.assertEqual(expected8, output)

    def test_map9(self):
        f = io.StringIO()
        with redirect_stdout(f):
            map_graph = RoutingGraph(map_str9)
            frontier = AStarFrontier(map_graph)
            solution = next(generic_search(map_graph, frontier), None)
            print_actions(solution)
        output = f.getvalue().strip()
        self.assertEqual(expected9, output)

    def test_map10(self):
        f = io.StringIO()
        with redirect_stdout(f):
            map_graph = RoutingGraph(map_str10)
            frontier = AStarFrontier(map_graph)
            solution = next(generic_search(map_graph, frontier), None)
            print_actions(solution)
        output = f.getvalue().strip()
        self.assertEqual(expected10, output)

    def test_map11(self):
        f = io.StringIO()
        with redirect_stdout(f):
            map_graph = RoutingGraph(map_str11)
            frontier = AStarFrontier(map_graph)
            solution = next(generic_search(map_graph, frontier), None)
            print_actions(solution)
        output = f.getvalue().strip()
        self.assertEqual(expected11, output)


if __name__ == '__main__':
    unittest.main()
