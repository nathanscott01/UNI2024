import unittest
from Labs.adjacency import *
from Labs.lab_4 import *

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

connected_example3 = """\
D 4
0 1
1 2
2 0
"""

connected_example4 = """\
U 5
2 4
3 1
0 4
2 1
"""

# Connected Expected Outputs
output1 = False

output2 = True

output3 = False

output4 = True


class TestStronglyConnected(unittest.TestCase):

    def test_connected_example1(self):
        graph_adj_list = adjacency_list(connected_example1)
        result = is_strongly_connected(graph_adj_list)
        self.assertEqual(result, output1)

    def test_connected_example2(self):
        graph_adj_list = adjacency_list(connected_example2)
        result = is_strongly_connected(graph_adj_list)
        self.assertEqual(result, output2)

    def test_connected_example3(self):
        graph_adj_list = adjacency_list(connected_example3)
        result = is_strongly_connected(graph_adj_list)
        self.assertEqual(result, output3)

    def test_connected_example4(self):
        graph_adj_list = adjacency_list(connected_example4)
        result = is_strongly_connected(graph_adj_list)
        self.assertEqual(result, output4)


if __name__ == '__main__':
    unittest.main()
