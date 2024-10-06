import unittest
import io
from contextlib import redirect_stdout
from generation_manipulation import *


# Expected Outputs
expected_1 = """Expression:  ['*', 'x', ['+', 'y', 1]]
Pruned Expression:  ['*', 'x', '!']"""

expected_2 = """Expression:  ['-', ['+', 'a', ['*', 'b', 'c']], ['*', ['+', 'x', 1], 'y']]
Pruned Expression:  ['-', ['+', 'a', '!'], ['*', '!', 'y']]"""

expected_3 = """Expression:  ['+', 'x', 'z']
Pruned Expression:  !"""

expected_4 = """a
a"""

expected_6 = """['+', ['+', ['+', '!', 9998], 9999], 10000]"""


def make_staircase_tree(n):  # bottom up so we don't hit recursion depth
    i = 1
    tree = ['+', 0, i]
    while i < n:
        tree = ['+', tree, i + 1]
        i += 1
    return tree


class MyPrunedTestCase(unittest.TestCase):
    def test_pruned_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            expression = ['*', 'x', ['+', 'y', 1]]
            max_depth = 1
            pruned = prune(expression, max_depth, ['!'])
            print("Expression: ", expression)
            print("Pruned Expression: ", pruned)
        output = f.getvalue().strip()
        self.assertEqual(expected_1, output)

    def test_pruned_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            expression = ['-', ['+', 'a', ['*', 'b', 'c']], ['*', ['+', 'x', 1], 'y']]
            max_depth = 2
            pruned = prune(expression, max_depth, ['!'])
            print("Expression: ", expression)
            print("Pruned Expression: ", pruned)
        output = f.getvalue().strip()
        self.assertEqual(expected_2, output)

    def test_pruned_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            expression = ['+', 'x', 'z']
            max_depth = 0
            pruned = prune(expression, max_depth, ['!'])
            print("Expression: ", expression)
            print("Pruned Expression: ", pruned)
        output = f.getvalue().strip()
        self.assertEqual(expected_3, output)

    def test_pruned_4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            expression = 'a'
            max_depth = 1
            pruned = prune(expression, max_depth, ['!'])
            print(expression)
            print(pruned)
        output = f.getvalue().strip()
        self.assertEqual(expected_4, output)

    def test_pruned_5(self):
        expression = ['*', 'x', ['+', 'y', 1]]
        max_depth = 2
        pruned = prune(expression, max_depth, ['!'])
        self.assertEqual(expression, pruned)

    def test_pruned_6(self):
        f = io.StringIO()
        with redirect_stdout(f):
            expression = make_staircase_tree(10000)
            max_depth = 3
            pruned = prune(expression, max_depth, ['!']) # This should not blow the stack
            print(pruned)
        output = f.getvalue().strip()
        self.assertEqual(expected_6, output)


if __name__ == '__main__':
    unittest.main()
