import io
import unittest

from bfs_frontier import BFSFrontier
from dfs_frontier import *

from contextlib import redirect_stdout

# Input Graphs
graph1 = ExplicitGraph(nodes=set('SAG'),
                       edge_list=[('S', 'A'), ('S', 'G'), ('A', 'G')],
                       starting_nodes=['S'],
                       goal_nodes={'G'})

graph2 = ExplicitGraph(nodes=set('SAG'),
                       edge_list=[('S', 'G'), ('S', 'A'), ('A', 'G')],
                       starting_nodes=['S'],
                       goal_nodes={'G'})

available_flights = ExplicitGraph(
    nodes=['Christchurch', 'Auckland',
           'Wellington', 'Gold Coast'],
    edge_list=[('Christchurch', 'Gold Coast'),
               ('Christchurch', 'Auckland'),
               ('Christchurch', 'Wellington'),
               ('Wellington', 'Gold Coast'),
               ('Wellington', 'Auckland'),
               ('Auckland', 'Gold Coast')],
    starting_nodes=['Christchurch'],
    goal_nodes={'Gold Coast'})


# Expected Outputs

expected_1 = """Actions:
  S->G.
Total cost: 1"""

expected_2 = """Actions:
  S->A,
  A->G.
Total cost: 2"""

expected_3 = """Actions:
  Christchurch->Wellington,
  Wellington->Auckland,
  Auckland->Gold Coast.
Total cost: 3"""

expected_4 = """Actions:
  Christchurch->Gold Coast.
Total cost: 1"""


class MyTestCase(unittest.TestCase):
    def test_dfs_frontier_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            solutions = generic_search(graph1, DFSFrontier())
            solution = next(solutions, None)
            print_actions(solution)
        output = f.getvalue().strip()
        self.assertEqual(expected_1, output)

    def test_dfs_frontier_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            solutions = generic_search(graph2, DFSFrontier())
            solution = next(solutions, None)
            print_actions(solution)
        output = f.getvalue().strip()
        self.assertEqual(expected_2, output)

    def test_dfs_frontier_3s(self):
        f = io.StringIO()
        with redirect_stdout(f):
            my_itinerary = next(generic_search(available_flights, DFSFrontier()), None)
            print_actions(my_itinerary)
        output = f.getvalue().strip()
        self.assertEqual(expected_3, output)

    def test_bfs_frontier_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            solutions = generic_search(graph1, BFSFrontier())
            solution = next(solutions, None)
            print_actions(solution)
        output = f.getvalue().strip()
        self.assertEqual(expected_1, output)

    def test_bfs_frontier_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            my_itinerary = next(generic_search(available_flights, BFSFrontier()), None)
            print_actions(my_itinerary)
        output = f.getvalue().strip()
        self.assertEqual(expected_4, output)


if __name__ == '__main__':
    unittest.main()
