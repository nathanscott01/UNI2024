import unittest
from backtracking import *

# Floyd Examples
example1 = {1, 2, 3}

example2 = {'a'}

example3 = set()

# Expected Outcomes
outcome1 = [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

outcome2 = [('a',)]


class TestPermutations(unittest.TestCase):
    def test_example1(self):
        result = sorted(permutations(example1))
        self.assertEqual(outcome1, result)

    def test_example2(self):
        result = sorted(permutations(example2))
        self.assertEqual(outcome2, result)

    def test_example3(self):
        result = permutations(example3)
        self.assertEqual([()], list(result))


if __name__ == '__main__':
    unittest.main()
