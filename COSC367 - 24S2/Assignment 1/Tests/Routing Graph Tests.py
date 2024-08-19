import unittest
import math
import io
from contextlib import redirect_stdout
from routing import RoutingGraph

# Input Graphs

map_str1 = """\
+-------+
|  9  XG|
|X XXX P|
| S  0FG|
|XX P XX|
+-------+
"""

map_str2 = """\
+--+
|GS|
+--+
"""

map_str3 = """\
+------+
|S    S|
|  GXXX|
|S     |
+------+
"""

# Expected Outputs
expected1 = """Starting nodes: [(1, 3, 9), (3, 2, inf), (3, 5, 0)]
Outgoing arcs (available actions) at starting states:
(1, 3, 9)
  Arc(tail=(1, 3, 9), head=(1, 4, 8), action='E', cost=5)
  Arc(tail=(1, 3, 9), head=(2, 2, 8), action='SW', cost=7)
  Arc(tail=(1, 3, 9), head=(1, 2, 8), action='W', cost=5)
(3, 2, inf)
  Arc(tail=(3, 2, inf), head=(2, 2, inf), action='N', cost=5)
  Arc(tail=(3, 2, inf), head=(3, 3, inf), action='E', cost=5)
  Arc(tail=(3, 2, inf), head=(4, 3, inf), action='SE', cost=7)
  Arc(tail=(3, 2, inf), head=(3, 1, inf), action='W', cost=5)
(3, 5, 0)"""

expected2 = """Is (1, 1, 5) goal? False
Outgoing arcs (available actions) at (1, 1, 5):
  Arc(tail=(1, 1, 5), head=(1, 2, 4), action='E', cost=5)
  Arc(tail=(1, 1, 5), head=(2, 2, 4), action='SE', cost=7)"""

expected3 = """Is (1, 7, 2) goal? True
Outgoing arcs (available actions) at (1, 7, 2):
  Arc(tail=(1, 7, 2), head=(2, 7, 1), action='S', cost=5)
  Arc(tail=(1, 7, 2), head=(2, 6, 1), action='SW', cost=7)"""

expected4 = """Is (3, 7, 0) goal? True"""

expected5 = """Is (3, 7, inf) goal? True"""

expected6 = """Is (3, 6, 5) goal? False
Outgoing arcs (available actions) at (3, 6, 5):
  Arc(tail=(3, 6, 5), head=(2, 6, 4), action='N', cost=5)
  Arc(tail=(3, 6, 5), head=(2, 7, 4), action='NE', cost=7)
  Arc(tail=(3, 6, 5), head=(3, 7, 4), action='E', cost=5)
  Arc(tail=(3, 6, 5), head=(4, 5, 4), action='SW', cost=7)
  Arc(tail=(3, 6, 5), head=(3, 5, 4), action='W', cost=5)
  Arc(tail=(3, 6, 5), head=(3, 6, 9), action='Fuel up', cost=15)"""

expected7 = """Is (3, 6, 9) goal? False
Outgoing arcs (available actions) at (3, 6, 9):
  Arc(tail=(3, 6, 9), head=(2, 6, 8), action='N', cost=5)
  Arc(tail=(3, 6, 9), head=(2, 7, 8), action='NE', cost=7)
  Arc(tail=(3, 6, 9), head=(3, 7, 8), action='E', cost=5)
  Arc(tail=(3, 6, 9), head=(4, 5, 8), action='SW', cost=7)
  Arc(tail=(3, 6, 9), head=(3, 5, 8), action='W', cost=5)"""

expected8 = """Outgoing arcs (available actions) at (2, 7, 4):
  Arc(tail=(2, 7, 4), head=(1, 7, 3), action='N', cost=5)
  Arc(tail=(2, 7, 4), head=(3, 7, 3), action='S', cost=5)
  Arc(tail=(2, 7, 4), head=(3, 6, 3), action='SW', cost=7)
  Arc(tail=(2, 7, 4), head=(2, 6, 3), action='W', cost=5)
  Arc(tail=(2, 7, 4), head=(4, 4, 4), action='Teleport to (4, 4)', cost=10)"""

expected9 = """Starting nodes: [(1, 2, inf)]
Outgoing arcs (available actions) at the start:
  Arc(tail=(1, 2, inf), head=(1, 1, inf), action='W', cost=5)"""

expected10 = """Is (1, 1, 1) goal? True
Outgoing arcs (available actions) at (1, 1, 1):
  Arc(tail=(1, 1, 1), head=(1, 2, 0), action='E', cost=5)"""

expected11 = """Starting nodes: [(1, 1, inf), (1, 6, inf), (3, 1, inf)]"""


class MyRoutingTests1(unittest.TestCase):
    def test_1(self):
        graph = RoutingGraph(map_str1)
        f = io.StringIO()
        with redirect_stdout(f):
            print("Starting nodes:", sorted(graph.starting_nodes()))
            print("Outgoing arcs (available actions) at starting states:")
            for s in sorted(graph.starting_nodes()):
                print(s)
                for arc in graph.outgoing_arcs(s):
                    print("  " + str(arc))
        output = f.getvalue().strip()
        self.assertEqual(expected1, output)

    def test_2(self):
        graph = RoutingGraph(map_str1)
        f = io.StringIO()
        with redirect_stdout(f):
            node = (1, 1, 5)
            print("\nIs {} goal?".format(node), graph.is_goal(node))
            print("Outgoing arcs (available actions) at {}:".format(node))
            for arc in graph.outgoing_arcs(node):
                print("  " + str(arc))
        output = f.getvalue().strip()
        self.assertEqual(expected2, output)

    def test_3(self):
        graph = RoutingGraph(map_str1)
        f = io.StringIO()
        with redirect_stdout(f):
            node = (1, 7, 2)
            print("\nIs {} goal?".format(node), graph.is_goal(node))
            print("Outgoing arcs (available actions) at {}:".format(node))
            for arc in graph.outgoing_arcs(node):
                print("  " + str(arc))
        output = f.getvalue().strip()
        self.assertEqual(expected3, output)

    def test_4(self):
        graph = RoutingGraph(map_str1)
        f = io.StringIO()
        with redirect_stdout(f):
            node = (3, 7, 0)
            print("\nIs {} goal?".format(node), graph.is_goal(node))
        output = f.getvalue().strip()
        self.assertEqual(expected4, output)

    def test_5(self):
        graph = RoutingGraph(map_str1)
        f = io.StringIO()
        with redirect_stdout(f):
            node = (3, 7, math.inf)
            print("\nIs {} goal?".format(node), graph.is_goal(node))
        output = f.getvalue().strip()
        self.assertEqual(expected5, output)

    def test_6(self):
        graph = RoutingGraph(map_str1)
        f = io.StringIO()
        with redirect_stdout(f):
            node = (3, 6, 5)
            print("\nIs {} goal?".format(node), graph.is_goal(node))
            print("Outgoing arcs (available actions) at {}:".format(node))
            for arc in graph.outgoing_arcs(node):
                print("  " + str(arc))
        output = f.getvalue().strip()
        self.assertEqual(expected6, output)

    def test_7(self):
        graph = RoutingGraph(map_str1)
        f = io.StringIO()
        with redirect_stdout(f):
            node = (3, 6, 9)
            print("\nIs {} goal?".format(node), graph.is_goal(node))
            print("Outgoing arcs (available actions) at {}:".format(node))
            for arc in graph.outgoing_arcs(node):
                print("  " + str(arc))
        output = f.getvalue().strip()
        self.assertEqual(expected7, output)

    def test_8(self):
        graph = RoutingGraph(map_str1)
        f = io.StringIO()
        with redirect_stdout(f):
            node = (2, 7, 4)  # at a location with a portal
            print("\nOutgoing arcs (available actions) at {}:".format(node))
            for arc in graph.outgoing_arcs(node):
                print("  " + str(arc))
        output = f.getvalue().strip()
        self.assertEqual(expected8, output)


class MyRoutingTests2(unittest.TestCase):
    def test_1(self):
        graph = RoutingGraph(map_str2)
        f = io.StringIO()
        with redirect_stdout(f):
            print("Starting nodes:", sorted(graph.starting_nodes()))
            print("Outgoing arcs (available actions) at the start:")
            for start in graph.starting_nodes():
                for arc in graph.outgoing_arcs(start):
                    print("  " + str(arc))
        output = f.getvalue().strip()
        self.assertEqual(expected9, output)

    def test_2(self):
        graph = RoutingGraph(map_str2)
        f = io.StringIO()
        with redirect_stdout(f):
            node = (1, 1, 1)
            print("\nIs {} goal?".format(node), graph.is_goal(node))
            print("Outgoing arcs (available actions) at {}:".format(node))
            for arc in graph.outgoing_arcs(node):
                print("  " + str(arc))
        output = f.getvalue().strip()
        self.assertEqual(expected10, output)


class MyRoutingTests3(unittest.TestCase):
    def test_1(self):
        graph = RoutingGraph(map_str3)
        f = io.StringIO()
        with redirect_stdout(f):
            graph = RoutingGraph(map_str3)
            print("Starting nodes:", sorted(graph.starting_nodes()))
        output = f.getvalue().strip()
        self.assertEqual(expected11, output)


if __name__ == '__main__':
    # # Individual Tests
    # # suite = unittest.TestLoader().loadTestsFromTestCase(MyRoutingTests1)
    # # suite = unittest.TestLoader().loadTestsFromTestCase(MyRoutingTests2)
    # suite = unittest.TestLoader().loadTestsFromTestCase(MyRoutingTests3)
    # unittest.TextTestRunner().run(suite)

    # All Tests
    unittest.main()
