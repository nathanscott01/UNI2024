import unittest
import io
from contextlib import redirect_stdout
from gradient_optimise import *
import numpy as np

# Expected Outputs
expected1 = """x* = 0.00, f(x*) = 0.00"""

expected2 = """x* = 0.00, f(x*) = 1.00"""

expected3 = """True True"""

expected4 = """x0 = -1, x* = -0.4254, f(x*) = 0.9288
x0 = 1, x* = 1.1754, f(x*) = -0.0967"""


class MyTestCase(unittest.TestCase):
    def test_gradient_optimize_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            def func(x):
                return x ** 2

            def func_prime(x):
                return 2 * x

            x0 = 2
            x_star = gradient_optimize(x0, func_prime, 0.1, -1, 250)
            print(f"x* = {x_star:.2f}, f(x*) = {func(x_star):.2f}")

        output = f.getvalue().strip()
        self.assertEqual(expected1, output)

    def test_gradient_optimize_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            def func(x):
                return 1 - x ** 2

            def func_prime(x):
                return -2 * x

            x0 = 2
            x_star = gradient_optimize(x0, func_prime, 0.1, 1, 250)
            print(f"x* = {x_star:.2f}, f(x*) = {func(x_star):.2f}")

        output = f.getvalue().strip()
        self.assertEqual(expected2, output)

    def test_gradient_optimize_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            # single maximum at x* = [1, -1] with f(x*) = 2
            def func(x):
                return 2 - (1 - x[0]) ** 2 - (x[1] + 1) ** 2

            def gradient_of_f(x):
                return np.array([2 * (1 - x[0]), -2 * (x[1] + 1)])

            x_star = gradient_optimize(np.zeros(2), gradient_of_f, 0.1, 1, 250)

            print(np.all(np.isclose(x_star, np.array([1, -1]))), np.isclose(func(x_star), 2))

        output = f.getvalue().strip()
        self.assertEqual(expected3, output)

    def test_gradient_optimize_4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            def func(x):  # This function has two minimums
                return x ** 4 - x ** 3 - x ** 2 + 1

            def func_prime(x):
                return 4 * x ** 3 - 3 * x ** 2 - 2 * x

            x0 = -1  # if x < 0 we get stuck in a local minimum
            x_star1 = gradient_optimize(-1, func_prime, 0.1, -1, 250)

            x0 = 1  # if x > 0 we should converge to the global minimum
            x_star2 = gradient_optimize(1, func_prime, 0.1, -1, 250)

            print(f"x0 = -1, x* = {x_star1:.4f}, f(x*) = {func(x_star1):.4f}")
            print(f"x0 = 1, x* = {x_star2:.4f}, f(x*) = {func(x_star2):.4f}")

        output = f.getvalue().strip()
        self.assertEqual(expected4, output)


if __name__ == '__main__':
    unittest.main()
