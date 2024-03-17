import unittest
from ..package_management import *


# Package Management Examples
example1 = """\
D 2
0 1
"""

example2 = """\
D 3
1 2
0 2
"""

example3 = """\
D 3
"""

example4 = """\
D 7
0 3
4 0
5 3
3 2
4 5
"""


# Expected Outcomes
outcome1 = [0, 1]

outcome2 = [1, 0, 2]

outcome3 = [0, 1, 2]

outcome4 = [6, 4, 5, 1, 0, 3, 2]


class TestBuildOrderFunction(unittest.TestCase):
    def test_example1(self):
        result = build_order(example1)
        self.assertEqual(outcome1, result)

    def test_example2(self):
        result = build_order(example2)
        self.assertEqual(outcome2, result)

    def test_example3(self):
        result = sorted(build_order(example3))
        self.assertEqual(outcome3, result)

    def test_example4(self):
        result = build_order(example4)
        self.assertEqual(outcome4, result)


if __name__ == '__main__':
    unittest.main()
