import os
import unittest
from min_cost_path import *


class TestMinCostPath(unittest.TestCase):
    def test_min_cost_trivial(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        input_file = os.path.join(dir_path, '..', 'Test Examples', 'checkerboard.trivial.in')
        result = file_cost(input_file)
        self.assertEqual(3, result)
        # self.assertEqual(3, len(result))

    def test_min_cost_small(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        input_file = os.path.join(dir_path, '..', 'Test Examples', 'checkerboard.small.in')
        result = file_cost(input_file)
        self.assertEqual(8, result)

    def test_min_cost_medium(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        input_file = os.path.join(dir_path, '..', 'Test Examples', 'checkerboard.medium.in')
        result = file_cost(input_file)
        self.assertEqual(15479095, result)


if __name__ == '__main__':
    unittest.main()
