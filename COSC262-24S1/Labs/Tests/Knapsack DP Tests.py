import unittest
from knapsack_dp import *

# The example from the lecture notes
items_1 = [
    Item(45, 3),
    Item(45, 3),
    Item(80, 4),
    Item(80, 5),
    Item(100, 8)]


class TestKnapsackDP(unittest.TestCase):
    def test_knapsack_1(self):
        result = max_value(items_1, 10)
        self.assertEqual(170, result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
