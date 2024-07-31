import io
import unittest
from contextlib import redirect_stdout
from search import *
from location import LocationGraph, LCFSFrontier

# Inputs
graph1 = LocationGraph(
    location={'A': (0, 0),
              'B': (3, 0),
              'C': (3, 4),
              'D': (7, 0), },
    radius=5,
    starting_nodes=['A'],
    goal_nodes={'C'}
)

graph2 = LocationGraph(
    location={'SW': (-2, -2),
              'NW': (-2, 2),
              'NE': (2, 2),
              'SE': (2, -2)},
    radius = 5,
    starting_nodes=['NE'],
    goal_nodes={'SW'}
)

graph3 = LocationGraph(
    location={'A': (25, 7),
              'B': (1, 7),
              'C': (13, 2),
              'D': (37, 2)},
    radius=15,
    starting_nodes=['B'],
    goal_nodes={'D'}
)

graph4 = ExplicitGraph(nodes=set('ABCD'),
                       edge_list=[('A', 'D', 7), ('A', 'B', 2),
                                  ('B', 'C', 3), ('C', 'D', 1)],
                       starting_nodes=['A'],
                       goal_nodes={'D'})

# Expected Outputs
expected_1 = """Arc(tail='A', head='B', action='A->B', cost=3.0)
Arc(tail='A', head='C', action='A->C', cost=5.0)

Arc(tail='B', head='A', action='B->A', cost=3.0)
Arc(tail='B', head='C', action='B->C', cost=4.0)
Arc(tail='B', head='D', action='B->D', cost=4.0)

Arc(tail='C', head='A', action='C->A', cost=5.0)
Arc(tail='C', head='B', action='C->B', cost=4.0)"""

expected_1_2 = """Arc(tail='NE', head='NW', action='NE->NW', cost=4.0)
Arc(tail='NE', head='SE', action='NE->SE', cost=4.0)

Arc(tail='NW', head='NE', action='NW->NE', cost=4.0)
Arc(tail='NW', head='SW', action='NW->SW', cost=4.0)

Arc(tail='SW', head='NW', action='SW->NW', cost=4.0)
Arc(tail='SW', head='SE', action='SW->SE', cost=4.0)

Arc(tail='SE', head='NE', action='SE->NE', cost=4.0)
Arc(tail='SE', head='SW', action='SE->SW', cost=4.0)"""

expected_2 = """(Arc(tail=None, head=None, action=None, cost=11), Arc(tail=None, head=None, action=None, cost=4))
(Arc(tail=None, head=None, action=None, cost=7), Arc(tail=None, head=None, action=None, cost=8))
(Arc(tail=None, head=None, action=None, cost=17),)"""

expected_3 = """Actions:
  B->C,
  C->A,
  A->D.
Total cost: 39.0"""

expected_4 = """Actions:
  A->B,
  B->C,
  C->D.
Total cost: 6"""


class MyTestCase(unittest.TestCase):
    def test_location(self):
        f = io.StringIO()
        with redirect_stdout(f):
            for arc in graph1.outgoing_arcs('A'):
                print(arc)
            print()
            for arc in graph1.outgoing_arcs('B'):
                print(arc)
            print()
            for arc in graph1.outgoing_arcs('C'):
                print(arc)
        output = f.getvalue().strip()
        self.assertEqual(expected_1, output)

    def test_location_1_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            for arc in graph2.outgoing_arcs('NE'):
                print(arc)
            print()
            for arc in graph2.outgoing_arcs('NW'):
                print(arc)
            print()
            for arc in graph2.outgoing_arcs('SW'):
                print(arc)
            print()
            for arc in graph2.outgoing_arcs('SE'):
                print(arc)
        output = f.getvalue().strip()
        self.assertEqual(expected_1_2, output)

    # def test_lcfs_1(self):
    #     f = io.StringIO()
    #     with redirect_stdout(f):
    #         frontier = LCFSFrontier()
    #         frontier.add((Arc(None, None, None, 17),))
    #         frontier.add((Arc(None, None, None, 11), Arc(None, None, None, 4)))
    #         frontier.add((Arc(None, None, None, 7), Arc(None, None, None, 8)))
    #
    #         for path in frontier:
    #             print(path)
    #     output = f.getvalue().strip()
    #     self.assertEqual(expected_2, output)
    #
    # def test_lcfs_2(self):
    #     f = io.StringIO()
    #     with redirect_stdout(f):
    #         solution = next(generic_search(graph3, LCFSFrontier()))
    #         print_actions(solution)
    #     output = f.getvalue().strip()
    #     self.assertEqual(expected_3, output)
    #
    # def test_lcfs_3(self):
    #     f = io.StringIO()
    #     with redirect_stdout(f):
    #         solution = next(generic_search(graph4, LCFSFrontier()))
    #         print_actions(solution)
    #     output = f.getvalue().strip()
    #     self.assertEqual(expected_4, output)


if __name__ == '__main__':
    unittest.main()
