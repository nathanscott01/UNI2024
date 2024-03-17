import unittest
from bubbles import *


# Bubbles Examples
example1 = """\
U 2
0 1
"""

example2 = """\
U 2
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
U 0
"""

example5 = """\
U 1
"""


# Expected Outcomes
outcome1 = [[0, 1]]

outcome2 = [[0], [1]]

outcome3 = [[0], [1, 2, 3, 4, 5, 6]]

outcome4 = []

outcome5 = [[0]]


class TestBubblesFunction(unittest.TestCase):
    def test_example1(self):
        result = sorted(sorted(bubble) for bubble in bubbles(example1))
        self.assertEqual(outcome1, result)

    def test_example2(self):
        result = sorted(sorted(bubble) for bubble in bubbles(example2))
        self.assertEqual(outcome2, result)

    def test_example3(self):
        result = sorted(sorted(bubble) for bubble in bubbles(example3))
        self.assertEqual(outcome3, result)

    def test_example4(self):
        result = sorted(sorted(bubble) for bubble in bubbles(example4))
        self.assertEqual(outcome4, result)

    def test_example5(self):
        result = sorted(sorted(bubble) for bubble in bubbles(example5))
        self.assertEqual(outcome5, result)


if __name__ == '__main__':
    unittest.main()
