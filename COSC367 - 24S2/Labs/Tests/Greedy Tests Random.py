import unittest
import io
import random
from contextlib import redirect_stdout
from greedy_descent import *
from greedy_descent import n_queens_neighbours as neighbours, n_queens_cost as cost

# Expected Outputs
expected1 = """(4, 6, 1, 2, 3, 5)
(4, 6, 1, 2, 5, 3)
RESTART
(3, 4, 6, 5, 1, 2)
(3, 4, 6, 1, 5, 2)
RESTART
(3, 2, 1, 6, 5, 4)
(3, 2, 6, 1, 5, 4)
(3, 4, 6, 1, 5, 2)
RESTART
(3, 1, 5, 6, 2, 4)
(3, 1, 6, 5, 2, 4)
RESTART
(5, 1, 3, 2, 4, 6)
(3, 1, 5, 2, 4, 6)
(1, 3, 5, 2, 4, 6)
RESTART
(5, 4, 6, 3, 2, 1)
(2, 4, 6, 3, 5, 1)
RESTART
(5, 1, 6, 3, 2, 4)
(3, 1, 6, 5, 2, 4)
RESTART
(5, 4, 3, 1, 2, 6)
(5, 4, 1, 3, 2, 6)
(2, 4, 1, 3, 5, 6)
RESTART
(2, 5, 6, 1, 3, 4)
(2, 4, 6, 1, 3, 5)"""

expected2 = """(7, 8, 4, 1, 3, 6, 2, 5)
(5, 8, 4, 1, 3, 6, 2, 7)"""

expected3 = """(1,)"""


class MyTestCase(unittest.TestCase):
    def test_greedy_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            N = 6
            random.seed(0)

            def random_state():
                return tuple(random.sample(range(1, N + 1), N))

            greedy_descent_with_random_restart(random_state, neighbours, cost)
        output = f.getvalue().strip()
        self.assertEqual(expected1, output)

    def test_greedy_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            N = 8
            random.seed(0)

            def random_state():
                return tuple(random.sample(range(1, N + 1), N))

            greedy_descent_with_random_restart(random_state, neighbours, cost)
        output = f.getvalue().strip()
        self.assertEqual(expected2, output)

    def test_greedy_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            N = 1
            random.seed(0)

            def random_state():
                return tuple(random.sample(range(1, N + 1), N))

            greedy_descent_with_random_restart(random_state, neighbours, cost)
        output = f.getvalue().strip()
        self.assertEqual(expected3, output)


if __name__ == '__main__':
    unittest.main()
