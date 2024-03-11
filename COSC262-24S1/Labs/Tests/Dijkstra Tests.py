import unittest
from Labs.adjacency import *
from Labs.shortest_path import *

# Strongly Connected Examples
connected_example1 = """\
D 3
0 1
1 0
0 2
"""

connected_example2 = """\
D 3
0 1
1 2
2 0
"""



# Connected Expected Outputs
output1 = False

output2 = True



class TestDijkstra(unittest.TestCase):

    def test_dijkstra_example1(self):
        graph_adj_list = adjacency_list(dijkstra_example1)
        result = dijkstra(graph_adj_list, 1)
        self.assertEqual(result, output1)

    def test_connected_example2(self):
        graph_adj_list = adjacency_list(connected_example2)
        result = is_strongly_connected(graph_adj_list)
        self.assertEqual(result, output2)



if __name__ == '__main__':
    unittest.main()
