import unittest
from pprint import pprint
from Labs.adjacency import *

# Global Examples
example1 = """\
D 3
0 1
1 0
0 2
"""

example2 = """\
D 3 W
0 1 7
1 0 -2
0 2 0
"""

example3 = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

example4 = """\
U 17
1 2
1 15
1 6
12 13
2 15
13 4
4 5
"""

example5 = """\
U 7
1 2
1 5
1 6
3 4
0 4
4 5
"""

# Adjacency Matrix Expected Outcomes

matrix_outcome1 = [[0, 1, 1], [1, 0, 0], [0, 0, 0]]

matrix_outcome2 = [[None, 7, 0], [-2, None, None], [None, None, None]]

matrix_outcome3 = [[0, 0, 0, 0, 1, 0, 0],
 [0, 0, 1, 0, 0, 1, 1],
 [0, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0],
 [1, 0, 0, 1, 0, 1, 0],
 [0, 1, 0, 0, 1, 0, 0],
 [0, 1, 0, 0, 0, 0, 0]]

matrix_outcome4 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


class TestAdjacencyListFunction(unittest.TestCase):
    def test_example1(self):
        expected_output = [[(1, None), (2, None)], [(0, None)], []]
        result = adjacency_list(example1)
        self.assertEqual(result, expected_output)

    def test_example2(self):
        expected_output = [[(1, 7), (2, 0)], [(0, -2)], []]
        result = adjacency_list(example2)
        self.assertEqual(result, expected_output)

    def test_example3(self):
        expected_output = [[], [(2, None), (5, None), (6, None)], [(1, None), (3, None), (5, None)], [(2, None), (4, None)], [(3, None), (5, None)], [(1, None), (2, None), (4, None)], [(1, None)]]
        result = adjacency_list(example3)
        self.assertEqual(result, expected_output)

    def test_example4(self):
        expected_output = [[], [(2, None), (15, None), (6, None)], [(1, None), (15, None)], [], [(13, None), (5, None)], [(4, None)], [(1, None)], [], [], [], [], [], [(13, None)], [(12, None), (4, None)], [], [(1, None), (2, None)], []]
        result = adjacency_list(example4)
        self.assertEqual(result, expected_output)


class TestAdjacencyMatrixFunction(unittest.TestCase):
    def test_example1(self):
        result = adjacency_matrix(example1)
        self.assertEqual(result, matrix_outcome1)

    def test_example2(self):
        result = adjacency_matrix(example2)
        self.assertEqual(result, matrix_outcome2)

    def test_example3(self):
        result = adjacency_matrix(example5)
        self.assertEqual(result, matrix_outcome3)

    def test_example4(self):
        result = adjacency_matrix(example4)
        self.assertEqual(result, matrix_outcome4)


if __name__ == '__main__':
    unittest.main()
