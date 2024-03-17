import unittest
from converters import *


# Converters Examples
example1 = """\
D 2
0 1
"""

example2 = """\
D 2
0 1
"""

example3 = """\
D 2
0 1
"""

example4 = """\
D 5
1 0
0 2
2 3
1 2
"""

example5 = """\
D 1
"""


# Expected Outcomes
outcome1 = [0, 1]

outcome2 = [1]

outcome3 = "No solution!"

outcome4 = [1, 2]

outcome5 = [0]


class TestConvertersFunction(unittest.TestCase):
    def test_example1(self):
        result = format_sequence(example1, 0, 1)
        self.assertEqual(outcome1, result)

    def test_example2(self):
        result = format_sequence(example2, 1, 1)
        self.assertEqual(outcome2, result)

    def test_example3(self):
        result = format_sequence(example3, 1, 0)
        self.assertEqual(outcome3, result)

    def test_example4(self):
        result = format_sequence(example4, 1, 2)
        self.assertEqual(outcome4, result)

    def test_example5(self):
        result = format_sequence(example5, 0, 0)
        self.assertEqual(outcome5, result)


if __name__ == '__main__':
    unittest.main()
