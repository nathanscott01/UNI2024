import unittest
import io
from contextlib import redirect_stdout
from KBGraph import *

# Inputs
kb1 = """
a :- b, c.
b :- d, e.
b :- g, e.
c :- e.
d.
e.
f :- a,
     g.
"""

kb2 = """
a :- b, c.
b :- d, e.
b :- g, e.
c :- e.
d.
e.
f :- a,
     g.
"""

kb3 = """
all_tests_passed :- program_is_correct.
all_tests_passed.
"""

kb4 = """
a :- b.
"""


class MyTestCase(unittest.TestCase):
    def test_kb1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            query = {'a'}
            if next(generic_search(KBGraph(kb1, query), DFSFrontier()), None):
                print("The query is true.")
            else:
                print("The query is not provable.")
        expected = "The query is true."
        output = f.getvalue().strip()
        self.assertEqual(expected, output)  # add assertion here

    def test_kb2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            query = {'a', 'b', 'd'}
            if next(generic_search(KBGraph(kb2, query), DFSFrontier()), None):
                print("The query is true.")
            else:
                print("The query is not provable.")
        expected = "The query is true."
        output = f.getvalue().strip()
        self.assertEqual(expected, output)

    def test_kb3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            query = {'program_is_correct'}
            if next(generic_search(KBGraph(kb3, query), DFSFrontier()), None):
                print("The query is true.")
            else:
                print("The query is not provable.")
        expected = "The query is not provable."
        output = f.getvalue().strip()
        self.assertEqual(expected, output)

    def test_kb4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            query = {'c'}
            if next(generic_search(KBGraph(kb4, query), DFSFrontier()), None):
                print("The query is true.")
            else:
                print("The query is not provable.")
        expected = "The query is not provable."
        output = f.getvalue().strip()
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
