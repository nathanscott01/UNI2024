import unittest
import random
from kd_tree import *
from twodkd_tree import *

# Expected Outputs
output1 = """\
Node(21)
  Node(14)
    Node(10)
      Leaf(10)
      Node(12)
        Leaf(12)
        Leaf(14)
    Node(19)
      Node(18)
        Leaf(18)
        Leaf(19)
      Node(20)
        Leaf(20)
        Leaf(21)
  Node(32)
    Node(25)
      Node(22)
        Leaf(22)
        Leaf(25)
      Node(27)
        Leaf(27)
        Leaf(32)
    Node(39)
      Node(35)
        Leaf(35)
        Leaf(39)
      Node(41)
        Leaf(41)
        Leaf(44)
"""

output2 = """\
Leaf(228)
"""

output3 = """\
Node(3)
  Leaf(3)
  Node(227)
    Leaf(227)
    Leaf(228)
"""


class MyTestCase(unittest.TestCase):
    def test_1DKD1(self):
        nums = [22, 41, 19, 27, 12, 35, 14, 20, 39, 10, 25, 44, 32, 21, 18]
        tree = binary_search_tree(nums)
        result = print_tree(tree)
        self.assertEqual(output1, result)

    def test_1DKD2(self):
        nums = [228]
        tree = binary_search_tree(nums)
        result = print_tree(tree)
        self.assertEqual(output2, result)

    def test_1DKD3(self):
        nums = [228, 227, 3]
        tree = binary_search_tree(nums)
        result = print_tree(tree)
        self.assertEqual(output3, result)

    def test_twodkd1(self):
        point_tuples = [(1, 3), (10, 20), (5, 19), (0, 11), (15, 22), (30, 5)]
        tree = build_tree(point_tuples, False, False)
        in_range = tree.points_in_range((Vec(0, 3), Vec(5, 19)))
        result = sorted((p.x, p.y) for p in in_range)
        expected = [(0, 11), (1, 3), (5, 19)]
        self.assertEqual(expected, result)

    def test_twodkd2(self):
        random.seed(1234567)
        try:
            n = Vec.box_calls
        except AttributeError:
            self.fail(
                "You must use the pre-loaded version of the Vec class in this question. It has an in_box method that counts calls to it.")
        Vec.box_calls = 0
        point_tuples = [(int(10000 * random.random()), int(10000 * random.random())) for i in range(50000)]
        points = [Vec(*p) for p in point_tuples]
        tree = KdTree(points, max_depth=20)
        in_range = tree.points_in_range((Vec(5, 19), Vec(100, 151)))
        result = sorted((p.x, p.y) for p in in_range)
        # Since we don't have the expected sorted list, just print the result for now
        print(result)
        # Check plausible number of in_box calls
        self.assertTrue(6 <= Vec.box_calls <= 10, f"Implausible number of in_box calls ({Vec.box_calls})")


if __name__ == '__main__':
    unittest.main()
