import unittest
import io
from contextlib import redirect_stdout
from arc_consistent import *

# Inputs
simple_csp = CSP(
    var_domains={x: set(range(1, 5)) for x in 'abc'},
    constraints={
        lambda a, b: a < b,
        lambda b, c: b < c,
        })


csp2 = CSP(var_domains={x:set(range(10)) for x in 'abc'},
          constraints={lambda a,b,c: 2*a+b+2*c==10})

# Expected Outputs
expected1 = """a: [1, 2]
b: [2, 3]
c: [3, 4]"""

expected2 = """a: [0, 1, 2, 3, 4, 5]
b: [0, 2, 4, 6, 8]
c: [0, 1, 2, 3, 4, 5]"""


class MyTestCase(unittest.TestCase):
    def test_simple(self):
        f = io.StringIO()
        with redirect_stdout(f):
            csp = arc_consistent(simple_csp)
            for var in sorted(csp.var_domains.keys()):
                print("{}: {}".format(var, sorted(csp.var_domains[var])))
        output = f.getvalue().strip()
        self.assertEqual(expected1, output)

    def test_crossword(self):
        f = io.StringIO()
        with redirect_stdout(f):
            csp = arc_consistent(csp2)
            for var in sorted(csp.var_domains.keys()):
                print("{}: {}".format(var, sorted(csp.var_domains[var])))
        output = f.getvalue().strip()
        self.assertEqual(expected2, output)

if __name__ == '__main__':
    unittest.main()
