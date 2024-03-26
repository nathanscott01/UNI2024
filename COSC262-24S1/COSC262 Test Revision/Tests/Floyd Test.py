import unittest
from floyd_warshall import *
from adjacency import adjacency_list

# Floyd Examples
example1 = """\
D 3 W
0 1 1
1 2 2
2 0 4
"""

example2 = """\
U 7 W
0 1 5
0 2 7
0 3 12
1 2 9
2 3 4
1 4 7
2 4 4
2 5 3
3 5 7
4 5 2
4 6 5
5 6 2
"""

# Expected Outcomes
outcome1 = [[0, 1, 3],
            [6, 0, 2],
            [4, 5, 0]]

outcome2 = [[0, 5, 7, 11, 11, 10, 12],
            [5, 0, 9, 13, 7, 9, 11],
            [7, 9, 0, 4, 4, 3, 5],
            [11, 13, 4, 0, 8, 7, 9],
            [11, 7, 4, 8, 0, 2, 4],
            [10, 9, 3, 7, 2, 0, 2],
            [12, 11, 5, 9, 4, 2, 0]]


class TestFloyd(unittest.TestCase):
    def test_example1(self):
        adj_list = adjacency_list(example1)
        distance = distance_matrix(adj_list)
        result = floyd(distance)
        self.assertEqual(outcome1, result)

    def test_example2(self):
        adj_list = adjacency_list(example2)
        distance = distance_matrix(adj_list)
        result = floyd(distance)
        self.assertEqual(outcome2, result)


if __name__ == '__main__':
    unittest.main()
