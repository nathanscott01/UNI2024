import unittest
from all_paths_backtrack import *
from adjacency import adjacency_list

# All Paths Examples
example1 = """\
U 3
0 1
1 2
2 0
"""

example2 = """\
U 5
0 2
1 2
3 2
4 2
1 4
"""

example3 = """\
D 7
6 0
6 5
0 1
0 2
1 2
1 3
2 4
2 5
4 3
5 4
"""

# Expected Outputs
output1 = [(0, 1, 2), (0, 2)]

output2 = [(1,)]

output3 = [(0, 2, 1), (0, 2, 4, 1)]

output4 = [(6, 0, 1, 2, 4, 3),
           (6, 0, 1, 2, 5, 4, 3),
           (6, 0, 1, 3),
           (6, 0, 2, 4, 3),
           (6, 0, 2, 5, 4, 3),
           (6, 5, 4, 3)]


class TestAllPathsBacktrackCase(unittest.TestCase):
    def test_example1(self):
        adj_list = adjacency_list(example1)
        result = sorted(all_paths(adj_list, 0, 2))
        self.assertEqual(output1, result)

    def test_example2(self):
        adj_list = adjacency_list(example1)
        result = sorted(all_paths(adj_list, 1, 1))
        self.assertEqual(output2, result)

    def test_example3(self):
        adj_list = adjacency_list(example2)
        result = sorted(all_paths(adj_list, 0, 1))
        self.assertEqual(output3, result)

    def test_example4(self):
        adj_list = adjacency_list(example3)
        result = sorted(all_paths(adj_list, 6, 3))
        self.assertEqual(output4, result)


if __name__ == '__main__':
    unittest.main()
