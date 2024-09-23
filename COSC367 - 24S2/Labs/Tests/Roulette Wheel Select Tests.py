import unittest
import io
from contextlib import redirect_stdout
from roulette_wheel import *

# Expected Outputs
expected1 = """a
a
a
b
b
b"""

expected2 = """1
1
2
2
2
2"""


class MyTestCase(unittest.TestCase):
    def test_roulette_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            population = ['a', 'b']

            def fitness(x):
                return 1  # everyone has the same fitness

            for r in [0, 0.33, 0.49999, 0.51, 0.75, 0.99999]:
                print(roulette_wheel_select(population, fitness, r))

        output = f.getvalue().strip()
        self.assertEqual(expected1, output)

    def test_roulette_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            population = [0, 1, 2]

            def fitness(x):
                return x

            for r in [0.001, 0.33, 0.34, 0.5, 0.75, 0.99]:
                print(roulette_wheel_select(population, fitness, r))

        output = f.getvalue().strip()
        self.assertEqual(expected2, output)


if __name__ == '__main__':
    unittest.main()
