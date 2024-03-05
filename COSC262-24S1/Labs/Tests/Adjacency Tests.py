import unittest
from Labs.adjacency import adjacency_list


class TestAdjacencyListFunction(unittest.TestCase):
    def test_example1(self):
        graph_str = """\
        D 3
        0 1
        1 0
        0 2
        """
        expected_output = [[(1, None), (2, None)], [(0, None)], []]
        result = adjacency_list(graph_str)
        self.assertEqual(result, expected_output)

    def test_example2(self):
        graph_string = """\
        D 3 W
        0 1 7
        1 0 -2
        0 2 0
        """
        expected_output = [[(1, 7), (2, 0)], [(0, -2)], []]
        result = adjacency_list(graph_string)
        self.assertEqual(result, expected_output)

    def test_example3(self):
        graph_string = """\
        U 7
        1 2
        1 5
        1 6
        2 3
        2 5
        3 4
        4 5
        """
        expected_output = [[], [(2, None), (5, None), (6, None)], [(1, None), (3, None), (5, None)], [(2, None), (4, None)], [(3, None), (5, None)], [(1, None), (2, None), (4, None)], [(1, None)]]
        result = adjacency_list(graph_string)
        self.assertEqual(result, expected_output)

    def test_example4(self):
        graph_string = """\
        U 17
        1 2
        1 15
        1 6
        12 13
        2 15
        13 4
        4 5
        """
        expected_output = [[], [(2, None), (15, None), (6, None)], [(1, None), (15, None)], [], [(13, None), (5, None)], [(4, None)], [(1, None)], [], [], [], [], [], [(13, None)], [(12, None), (4, None)], [], [(1, None), (2, None)], []]
        result = adjacency_list(graph_string)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
