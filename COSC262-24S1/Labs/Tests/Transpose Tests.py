import unittest
from Labs.adjacency import *
from Labs.lab_3 import *

# Transpose Examples
transpose_example1 = """\
D 3
0 1
1 0
0 2
"""

transpose_example2 = """\
D 3 W
0 1 7
1 0 -2
0 2 0
"""

transpose_example3 = """"\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

transpose_example4 = """\
U 17
1 2
1 15
1 6
12 13
2 15
13 4
4 5
"""

# Transpose Outputs
transpose_output1 = [[(1, None)],
                     [(0, None)],
                     [(0, None)]]

transpose_output2 = [[(1, -2)],
                     [(0, 7)],
                     [(0, 0)]]

transpose_output3 = [[],
                     [(2, None), (5, None), (6, None)],
                     [(1, None), (3, None), (5, None)],
                     [(2, None), (4, None)],
                     [(3, None), (5, None)],
                     [(1, None), (2, None), (4, None)],
                     [(1, None)]]

transpose_output4 = [[],
                     [(2, None), (6, None), (15, None)],
                     [(1, None), (15, None)],
                     [],
                     [(5, None), (13, None)],
                     [(4, None)],
                     [(1, None)],
                     [],
                     [],
                     [],
                     [],
                     [],
                     [(13, None)],
                     [(4, None), (12, None)],
                     [],
                     [(1, None), (2, None)],
                     []]


class TestTranspose(unittest.TestCase):
    def test_transpose_example1(self):
        graph_adj_list = adjacency_list(transpose_example1)
        result = transpose(graph_adj_list)
        self.assertEqual(result, transpose_output1)

    def test_transpose_example2(self):
        graph_adj_list = adjacency_list(transpose_example2)
        result = transpose(graph_adj_list)
        self.assertEqual(result, transpose_output2)

    def test_transpose_example3(self):
        graph_adj_list = adjacency_list(transpose_example3)
        result = transpose(graph_adj_list)
        self.assertEqual(result, transpose_output3)

    def test_transpose_example4(self):
        graph_adj_list = adjacency_list(transpose_example4)
        result = transpose(graph_adj_list)
        self.assertEqual(result, transpose_output4)


if __name__ == '__main__':
    unittest.main()
