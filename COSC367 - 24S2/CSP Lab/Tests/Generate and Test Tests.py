import unittest
import io
from contextlib import redirect_stdout
from csp import *
from generate_and_test import *
import itertools

# Inputs
simple_csp = CSP(
    var_domains={x: set(range(1, 5)) for x in 'abc'},
    constraints={
        lambda a, b: a < b,
        lambda b, c: b < c,
        })


crossword_puzzle = CSP(
    var_domains={
        # read across:
        'a1': set("ant,big,bus,car".split(',')),
        'a3': set("book,buys,hold,lane,year".split(',')),
        'a4': set("ant,big,bus,car,has".split(',')),
        # read down:
        'd1': set("book,buys,hold,lane,year".split(',')),
        'd2': set("ginger,search,symbol,syntax".split(',')),
        },
    constraints={
        lambda a1, d1: a1[0] == d1[0],
        lambda d1, a3: d1[2] == a3[0],
        lambda a1, d2: a1[2] == d2[0],
        lambda d2, a3: d2[2] == a3[2],
        lambda d2, a4: d2[4] == a4[0],
        })


# Expected Outputs
expected1 = """[('a', 1), ('b', 2), ('c', 3)]
[('a', 1), ('b', 2), ('c', 4)]
[('a', 1), ('b', 3), ('c', 4)]
[('a', 2), ('b', 3), ('c', 4)]"""

expected2 = """bus
u e
year
s r
  car
  h"""


class MyTestCase(unittest.TestCase):
    def test_simple(self):
        f = io.StringIO()
        with redirect_stdout(f):
            solutions = sorted(str(sorted(solution.items())) for solution
                               in generate_and_test(simple_csp))
            print("\n".join(solutions))
        output = f.getvalue().strip()
        self.assertEqual(expected1, output)

    def test_crossword(self):
        f = io.StringIO()
        with redirect_stdout(f):
            solution = next(iter(generate_and_test(crossword_puzzle)))
            # printing the puzzle similar to the way it actually  looks
            pretty_puzzle = ["".join(line) for line in itertools.zip_longest(
                solution['d1'], "", solution['d2'], fillvalue=" ")]
            pretty_puzzle[0:5:2] = solution['a1'], solution['a3'], "  " + solution['a4']
            print("\n".join(pretty_puzzle))
        output = f.getvalue().strip()
        self.assertEqual(expected2, output)

if __name__ == '__main__':
    unittest.main()
