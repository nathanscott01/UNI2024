import unittest
import io
from contextlib import redirect_stdout
from generation_manipulation import *


# Expected Outputs
expected_1 = """['+', 'x', 'b']"""

expected_2 = """['+', 'a', ['-', 'x', 'y']]"""

expected_3 = """Expression: ['*', 'x', ['+', 'y', 1]]
New subtree: ['-', 'a', 'b']
Subtree attached at position 1: ['*', ['-', 'a', 'b'], ['+', 'y', 1]]"""

expected_4 = """Expression: ['*', 'x', ['+', 'y', 1]]
New subtree: ['-', 'a', 'b']
Subtree attached at position 3: ['*', 'x', ['+', ['-', 'a', 'b'], 1]]"""

expected_5 = """Expression: a
New subtree: b
Subtree attached at position 0: b"""

expected_6 = """Attached at position 0: ['h', 'i', 'j']
Attached at position 1: ['+', ['h', 'i', 'j'], ['f', 'x', 2]]
Attached at position 2: ['+', ['g', ['h', 'i', 'j'], 4], ['f', 'x', 2]]
Attached at position 3: ['+', ['g', 3, ['h', 'i', 'j']], ['f', 'x', 2]]
Attached at position 4: ['+', ['g', 3, 4], ['h', 'i', 'j']]
Attached at position 5: ['+', ['g', 3, 4], ['f', ['h', 'i', 'j'], 2]]
Attached at position 6: ['+', ['g', 3, 4], ['f', 'x', ['h', 'i', 'j']]]"""


class MyAttachTestCase(unittest.TestCase):
    def test_attach_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            expression1 = ['+', 'a', 'b']
            expression2 = 'x'
            position = 1
            print(attach(expression1, expression2, position))
        output = f.getvalue().strip()
        self.assertEqual(expected_1, output)

    def test_attach_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            expression1 = ['+', 'a', 'b']
            expression2 = ['-', 'x', 'y']
            position = 2
            print(attach(expression1, expression2, position))
        output = f.getvalue().strip()
        self.assertEqual(expected_2, output)

    def test_attach_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            expression = ['*', 'x', ['+', 'y', 1]]
            subtree = ['-', 'a', 'b']
            position = 1
            print("Expression:", expression)
            print("New subtree:", subtree)
            print(f"Subtree attached at position {position}:", attach(expression, subtree, position))
        output = f.getvalue().strip()
        self.assertEqual(expected_3, output)

    def test_attach_4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            expression = ['*', 'x', ['+', 'y', 1]]
            subtree = ['-', 'a', 'b']
            position = 3
            print("Expression:", expression)
            print("New subtree:", subtree)
            print(f"Subtree attached at position {position}:", attach(expression, subtree, position))
        output = f.getvalue().strip()
        self.assertEqual(expected_4, output)

    def test_attach_5(self):
        f = io.StringIO()
        with redirect_stdout(f):
            expression = 'a'
            subtree = 'b'
            position = 0
            print("Expression:", expression)
            print("New subtree:", subtree)
            print(f"Subtree attached at position {position}:", attach(expression, subtree, position))
        output = f.getvalue().strip()
        self.assertEqual(expected_5, output)

    def test_attach_6(self):
        f = io.StringIO()
        with redirect_stdout(f):
            expression = ['+', ['g', 3, 4], ['f', 'x', 2]]
            sub_expression = ['h', 'i', 'j']

            for position in range(7):
                print(f"Attached at position {position}:", attach(expression, sub_expression, position))
        output = f.getvalue().strip()
        self.assertEqual(expected_6, output)


if __name__ == '__main__':
    unittest.main()
