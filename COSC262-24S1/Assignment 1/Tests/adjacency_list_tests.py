"""
Nathan Scott
Student ID: 87357713
COSC262 Assignment 1
Used to test the adjacency list method for each file
"""

import unittest
from ..snow import adjacency_list


# Adjacency String Examples
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


# Expected Outcomes
outcome1 = [[(1, None), (2, None)],
            [(0, None)],
            []]

outcome2 = [[(1, 7), (2, 0)],
            [(0, -2)],
            []]

outcome3 = [[],
            [(2, None), (5, None), (6, None)],
            [(1, None), (3, None), (5, None)],
            [(2, None), (4, None)],
            [(3, None), (5, None)],
            [(1, None), (2, None), (4, None)],
            [(1, None)]]

outcome4 = [[],
            [(2, None), (15, None), (6, None)],
            [(1, None), (15, None)],
            [],
            [(13, None), (5, None)],
            [(4, None)],
            [(1, None)],
            [],
            [],
            [],
            [],
            [],
            [(13, None)],
            [(12, None), (4, None)],
            [],
            [(1, None), (2, None)],
            []]


class TestAdjacencyListFunction(unittest.TestCase):
    def test_example1(self):
        result = adjacency_list(example1)
        self.assertEqual(outcome1, result)

    def test_example2(self):
        result = adjacency_list(example2)
        self.assertEqual(outcome2, result)

    def test_example3(self):
        result = adjacency_list(example3)
        self.assertEqual(outcome3, result)

    def test_example4(self):
        result = adjacency_list(example4)
        self.assertEqual(outcome4, result)


if __name__ == '__main__':
    unittest.main()
