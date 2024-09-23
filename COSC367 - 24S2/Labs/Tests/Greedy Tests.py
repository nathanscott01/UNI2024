import unittest
import io
from contextlib import redirect_stdout
from greedy_descent import *


# Global functions
def cost(x):
    return x**2


def neighbours(x):
    return [x - 1, x + 1]


def neighbours_1(x):
    return [x - 1, x + 1, x - 2, x + 2]


# Expected Outputs
expected1 = """4
3
2
1
0"""

expected2 = """-6.75
-5.75
-4.75
-3.75
-2.75
-1.75
-0.75
0.25"""

expected3 = """-6.75
-4.75
-2.75
-0.75
0.25"""


class MyTestCase(unittest.TestCase):
    def test_greedy_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            for state in greedy_descent(4, neighbours, cost):
                print(state)
        output = f.getvalue().strip()
        self.assertEqual(expected1, output)

    def test_greedy_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            for state in greedy_descent(-6.75, neighbours, cost):
                print(state)
        output = f.getvalue().strip()
        self.assertEqual(expected2, output)

    def test_greedy_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            for state in greedy_descent(-6.75, neighbours_1, cost):
                print(state)
        output = f.getvalue().strip()
        self.assertEqual(expected3, output)


if __name__ == '__main__':
    unittest.main()
