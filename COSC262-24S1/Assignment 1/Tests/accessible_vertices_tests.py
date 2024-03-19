import unittest
from batteries_modified_dijsktra import *


# Locations Examples
example1 = """\
U 4 W
0 2 5
0 3 2
3 2 1
"""

example2 = """\
U 7 W
0 1 6
1 2 6
0 2 10
0 3 3
3 4 3
4 5 1
"""

example3 = """\
U 1000 W
810 820 100
830 840 100
810 830 100
820 840 200
810 840 500
840 850 100
860 850 100
860 840 150
880 870 100
890 880 100
"""


# Expected Outcomes
outcome1 = [0, 2, 3]

outcome2 = [0, 1, 2, 3, 4, 5]

outcome3 = [810, 820, 830, 840, 850, 860]

outcome4 = [870, 880, 890]


class TestDFSSearchCase(unittest.TestCase):
    def test_example1(self):
        adj_list = adjacency_list(example1)
        result = dfs_search(adj_list, 0)
        self.assertEqual(outcome1, result)  # add assertion here

    def test_example2(self):
        adj_list = adjacency_list(example1)
        result = dfs_search(adj_list, 1)
        self.assertEqual([1], result)

    def test_example3(self):
        adj_list = adjacency_list(example2)
        result = dfs_search(adj_list, 0)
        self.assertEqual(outcome2, result)

    def test_example4(self):
        adj_list = adjacency_list(example2)
        result = dfs_search(adj_list, 6)
        self.assertEqual([6], result)

    def test_example5(self):
        adj_list = adjacency_list(example3)
        result = dfs_search(adj_list, 0)
        self.assertEqual([0], result)

    def test_example6(self):
        adj_list = adjacency_list(example3)
        result = dfs_search(adj_list, 810)
        self.assertEqual(outcome3, result)

    def test_example7(self):
        adj_list = adjacency_list(example3)
        result = dfs_search(adj_list, 870)
        self.assertEqual(outcome4, result)


if __name__ == '__main__':
    unittest.main()
