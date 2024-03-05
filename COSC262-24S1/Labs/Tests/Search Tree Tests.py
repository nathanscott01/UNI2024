import unittest
from Labs.search_trees import *
from Labs.adjacency import *

# Global Examples
example1 = [
    [(1, None)],
    [(0, None), (2, None)],
    [(1, None)]
]

example2 = [
    [(1, None)],
    []
]

example3 = """\
D 2
0 1
"""

example4 = """\
D 2
0 1
1 0
"""

example5 = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

example6 = """\
D 2 W
0 1 99
"""

# Expected Outcomes - BFS
outcome_BFS1_1 = [None, 0, 1]

outcome_BFS1_2 = [1, None, 1]

outcome_BFS2_1 = [None, 0]

outcome_BFS2_2 = [None, None]

outcome_BFS3 = [None, 0]

outcome_BFS4 = [1, None]

outcome_BFS5 = [None, None, 1, 2, 5, 1, 1]

outcome_BFS6 = [None, 0]


# Global DFS Examples

DFS_example1 = [
    [(1, None), (2, None)],
    [(0, None), (2, None)],
    [(0, None), (1, None)]
]

DFS_example2 = example2

DFS_example3 = example5

DFS_example4 = """\
U 4
2 3
2 1
0 3
1 0
"""

# Expected Outcomes - DFS
outcome_DSF1_1 = [None, 0, 1]

outcome_DSF1_2 = [1, None, 0]

outcome_DSF1_3 = [2, 0, None]

outcome_DSF2_1 = [None, 0]

outcome_DSF2_2 = [None, None]

outcome_DSF3 = [None, None, 1, 2, 3, 4, 1]

outcome_DSF4 = [None, 2, 3, 0]


class TestBSF(unittest.TestCase):
    def test_BSF_example1_1(self):
        result = bfs_tree(example1, 0)
        self.assertEqual(result, outcome_BFS1_1)

    def test_BSF_example1_2(self):
        result = bfs_tree(example1, 1)
        self.assertEqual(result, outcome_BFS1_2)

    def test_BSF_example2_1(self):
        result = bfs_tree(example2, 0)
        self.assertEqual(result, outcome_BFS2_1)

    def test_BSF_example2_2(self):
        result = bfs_tree(example2, 1)
        self.assertEqual(result, outcome_BFS2_2)

    def test_BSF_example3(self):
        result = bfs_tree(adjacency_list(example3), 0)
        self.assertEqual(result, outcome_BFS3)

    def test_BSF_example4(self):
        result = bfs_tree(adjacency_list(example4), 1)
        self.assertEqual(result, outcome_BFS4)

    def test_BSF_example5(self):
        result = bfs_tree(adjacency_list(example5), 1)
        self.assertEqual(result, outcome_BFS5)

    def test_BSF_example6(self):
        result = bfs_tree(adjacency_list(example6), 0)
        self.assertEqual(result, outcome_BFS6)


class TestDFS(unittest.TestCase):

    def test_DFS_example1_1(self):
        result = dfs_tree(DFS_example1, 0)
        self.assertEqual(result, outcome_DSF1_1)

    def test_DFS_example1_2(self):
        result = dfs_tree(DFS_example1, 1)
        self.assertEqual(result, outcome_DSF1_2)

    def test_DFS_example1_3(self):
        result = dfs_tree(DFS_example1, 2)
        self.assertEqual(result, outcome_DSF1_3)

    def test_DFS_example2_1(self):
        result = dfs_tree(DFS_example2, 0)
        self.assertEqual(result, outcome_DSF2_1)

    def test_DFS_example2_2(self):
        result = dfs_tree(DFS_example2, 1)
        self.assertEqual(result, outcome_DSF2_2)

    def test_DFS_example3(self):
        result = dfs_tree(adjacency_list(DFS_example3), 1)
        self.assertEqual(result, outcome_DSF3)

    def test_DFS_example4(self):
        result = dfs_tree(adjacency_list(DFS_example4), 0)
        self.assertEqual(result, outcome_DSF4)


if __name__ == '__main__':
    unittest.main()
