import unittest
from floyd_warshall import *
from adjacency import *

# Distance Matrix Examples
example1 = """\
U 3 W
0 1 5
2 1 7
"""

example2 = """\
D 2 W
0 1 4
"""

example3 = """\
D 4 W
0 1 -3
1 2 1
2 0 3
2 3 -2
3 0 6
3 1 4
"""

example4 = """\
D 3 W
0 1 1
1 2 2
2 0 4
"""

# Expected outputs
output1 = [[0, 5, float('inf')],
           [5, 0, 7],
           [float('inf'), 7, 0]]

output2 = [[0, 4],
           [float('inf'), 0]]

output3 = [[0, -3, float('inf'), float('inf')],
           [float('inf'), 0, 1, float('inf')],
           [3, float('inf'), 0, -2],
           [6, 4, float('inf'), 0]]

output4 = [[0, 1, float('inf')],
           [float('inf'), 0, 2],
           [4, float('inf'), 0]]


class TestDistanceMatrix(unittest.TestCase):
    def test_example1(self):
        adj_list = adjacency_list(example1)
        result = distance_matrix(adj_list)
        self.assertEqual(output1, result)

    def test_example2(self):
        adj_list = adjacency_list(example2)
        result = distance_matrix(adj_list)
        self.assertEqual(output2, result)

    def test_example3(self):
        adj_list = adjacency_list(example3)
        result = distance_matrix(adj_list)
        self.assertEqual(output3, result)

    def test_example4(self):
        adj_list = adjacency_list(example4)
        result = distance_matrix(adj_list)
        self.assertEqual(output4, result)


if __name__ == '__main__':
    unittest.main()
