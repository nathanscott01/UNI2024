import unittest
from Labs.adjacency import *
from Labs.shortest_path import *

# Strongly Connected Examples
dijkstra_example1 = """\
D 3 W
1 0 3
2 0 1
1 2 1
"""

dijkstra_example2 = """\
U 4 W
0 2 5
0 3 2
3 2 2
"""


# Connected Expected Outputs
output1_1 = ([2, None, 1], [2, 0, 1])

output1_2 = ([2, None, None], [1, float('inf'), 0])

output2_1 = ([None, None, 3, 0], [0, float('inf'), 4, 2])

output2_2 = ([3, None, None, 2], [4, float('inf'), 0, 2])


class TestDijkstra(unittest.TestCase):

    def test_dijkstra_example1_1(self):
        graph_adj_list = adjacency_list(dijkstra_example1)
        result = dijkstra(graph_adj_list, 1)
        self.assertEqual(result, output1_1)

    def test_dijkstra_example1_2(self):
        graph_adj_list = adjacency_list(dijkstra_example1)
        result = dijkstra(graph_adj_list, 2)
        self.assertEqual(result, output1_2)

    def test_dijkstra_example2_1(self):
        graph_adj_list = adjacency_list(dijkstra_example2)
        result = dijkstra(graph_adj_list, 0)
        self.assertEqual(result, output2_1)

    def test_dijkstra_example2_2(self):
        graph_adj_list = adjacency_list(dijkstra_example2)
        result = dijkstra(graph_adj_list, 2)
        self.assertEqual(result, output2_2)


if __name__ == '__main__':
    unittest.main()
