import unittest
from snow import *

# Snow Examples
example1 = """\
U 3 W
0 1 1
2 1 2
2 0 4
"""

example2 = """\
U 1 W
"""


# Expected Outcomes
outcome1 = [(0, 1), (1, 2)]

outcome2 = []


class TestWhichSegmentsFunction(unittest.TestCase):
    def test_example1(self):
        result = which_segments(example1)
        self.assertEqual(outcome1, result)

    def test_example2(self):
        result = which_segments(example2)
        self.assertEqual(outcome2, result)


if __name__ == '__main__':
    unittest.main()
