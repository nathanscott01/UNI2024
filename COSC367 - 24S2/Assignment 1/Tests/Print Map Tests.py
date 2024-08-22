import unittest
import io
from contextlib import redirect_stdout
from routing_table import *

# Inputs
map_str1 = """\
+----------------+
|                |
|                |
|                |
|                |
|                |
|                |
|        S       |
|                |
|                |
|     G          |
|                |
|                |
|                |
+----------------+
"""

map_str2 = """\
+-------------+
| G         G |
|      S      |
| G         G |
+-------------+
"""

map_str3 = """\
+-------+
|     XG|
|X XXX  |
|  S    |
+-------+
"""


map_str4 = """\
+--+
|GS|
+--+
"""

map_str5 = """\
+----+
|    |
| SX |
| X G|
+----+
"""

map_str6 = """\
+---------------+
|    G          |
|XXXXXXXXXXXX   |
|           X   |
|  XXXXXX   X   |
|  X S  X   X   |
|  X        X   |
|  XXXXXXXXXX   |
|               |
+---------------+
"""


map_str7 = """\
+---------+
|         |
|    G    |
|         |
+---------+
"""

# Expected Outputs
expected1 = """+----------------+
|                |
|                |
|                |
|                |
|                |
|                |
|        S       |
|       *        |
|      *         |
|     G          |
|                |
|                |
|                |
+----------------+"""

expected1_2 = """+----------------+
|                |
|                |
|        .       |
|      ......    |
|     .......    |
|     .......    |
|    ....S....   |
|     ..*....    |
|     .*.....    |
|     G......    |
|        .       |
|                |
|                |
+----------------+"""

expected2 = """+-------------+
| G.... ****G |
|  ....S....  |
| G.... ....G |
+-------------+"""

expected3 = """+-------+
|     XG|
|X XXX* |
|  S**  |
+-------+"""

expected4 = """+--+
|GS|
+--+"""

expected5 = """+----+
|    |
| SX |
| X*G|
+----+"""

expected6 = """+---------------+
|    G*******   |
|XXXXXXXXXXXX*  |
|..******...X*  |
|.*XXXXXX*..X*  |
|.*X.S**X*..X*. |
|.*X....*...X*. |
|.*XXXXXXXXXX*. |
|..**********.. |
+---------------+"""

expected7 = """+---------+
|         |
|    G    |
|         |
+---------+"""


class MyTestCase(unittest.TestCase):
    def test_map1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            map_graph = RoutingGraph(map_str1)
            frontier = AStarFrontier(map_graph)
            solution = next(generic_search(map_graph, frontier), None)
            print_map(map_graph, frontier, solution)
        output = f.getvalue().strip()
        self.assertEqual(expected1, output)

    def test_map1_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            map_graph = RoutingGraph(map_str1)
            map_graph.estimated_cost_to_goal = lambda node: 0
            frontier = AStarFrontier(map_graph)
            solution = next(generic_search(map_graph, frontier), None)
            print_map(map_graph, frontier, solution)
        output = f.getvalue().strip()
        self.assertEqual(expected1_2, output)

    def test_map2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            map_graph = RoutingGraph(map_str2)
            frontier = AStarFrontier(map_graph)
            solution = next(generic_search(map_graph, frontier), None)
            print_map(map_graph, frontier, solution)
        output = f.getvalue().strip()
        self.assertEqual(expected2, output)

    def test_map3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            map_graph = RoutingGraph(map_str3)
            frontier = AStarFrontier(map_graph)
            solution = next(generic_search(map_graph, frontier), None)
            print_map(map_graph, frontier, solution)
        output = f.getvalue().strip()
        self.assertEqual(expected3, output)

    def test_map4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            map_graph = RoutingGraph(map_str4)
            frontier = AStarFrontier(map_graph)
            solution = next(generic_search(map_graph, frontier), None)
            print_map(map_graph, frontier, solution)
        output = f.getvalue().strip()
        self.assertEqual(expected4, output)

    def test_map5(self):
        f = io.StringIO()
        with redirect_stdout(f):
            map_graph = RoutingGraph(map_str5)
            frontier = AStarFrontier(map_graph)
            solution = next(generic_search(map_graph, frontier), None)
            print_map(map_graph, frontier, solution)
        output = f.getvalue().strip()
        self.assertEqual(expected5, output)

    def test_map6(self):
        f = io.StringIO()
        with redirect_stdout(f):
            map_graph = RoutingGraph(map_str6)
            frontier = AStarFrontier(map_graph)
            solution = next(generic_search(map_graph, frontier), None)
            print_map(map_graph, frontier, solution)
        output = f.getvalue().strip()
        self.assertEqual(expected6, output)


if __name__ == '__main__':
    unittest.main()
