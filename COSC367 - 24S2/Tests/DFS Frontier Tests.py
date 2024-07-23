import unittest
from dfs_frontier import *

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
Total cost: 1
"""

expected_2 = """Actions:
  S->A,
  A->G.
Total cost: 2
"""

expected_3 = """Actions:
  Christchurch->Wellington,
  Wellington->Auckland,
  Auckland->Gold Coast.
Total cost: 3
"""


class MyTestCase(unittest.TestCase):
    def test_dfs_frontier_1(self):
        solutions = generic_search(graph1, DFSFrontier())
        solution = next(solutions, None)
        self.assertEqual(print_actions(solution), expected_1)

    def test_dfs_frontier_2(self):
        solutions = generic_search(graph2, DFSFrontier())
        solution = next(solutions, None)
        self.assertEqual(print_actions(solution), expected_2)

    def test_dfs_frontier_3s(self):
        my_itinerary = next(generic_search(available_flights, DFSFrontier()), None)
        self.assertEqual(print_actions(my_itinerary), expected_3)


if __name__ == '__main__':
    unittest.main()
