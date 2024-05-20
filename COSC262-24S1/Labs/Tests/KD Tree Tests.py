import unittest
from kd_tree import *

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


if __name__ == '__main__':
    unittest.main()
