import unittest
import io
from contextlib import redirect_stdout
from prediction import generate_rest


# Expected Outputs
expected_1 = """[3, 4, 5, 6, 7]"""

expected_2 = """[3, 4, 5, 6]"""

expected_3 = """[12, 14, 16, 18, 20]"""

expected_4 = """[12, 14, 16, 18, 20]"""

expected_5 = """[0, 1, 0, 1, 0, 1]"""

expected_6 = """[1, 2, 3, 5, 8]"""

expected_7 = """[367, 367, 367, 367, 367]"""

expected_8 = """[-1, -1, -1, -1, -1]"""

expected_9 = """[]"""


class MyGenerateTestCase(unittest.TestCase):
    def test_generate_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            initial_sequence = [0, 1, 2]
            expression = 'i'
            length_to_generate = 5
            print(generate_rest(initial_sequence, expression, length_to_generate))
        output = f.getvalue().strip()
        self.assertEqual(expected_1, output)

    def test_generate_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            initial_sequence = [-1, 1, 367]
            expression = 'i'
            length_to_generate = 4
            print(generate_rest(initial_sequence, expression, length_to_generate))
        output = f.getvalue().strip()
        self.assertEqual(expected_2, output)

    def test_generate_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            initial_sequence = [4, 6, 8, 10]
            expression = ['*', ['+', 'i', 2], 2]
            length_to_generate = 5
            print(generate_rest(initial_sequence, expression, length_to_generate))
        output = f.getvalue().strip()
        self.assertEqual(expected_3, output)

    def test_generate_4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            initial_sequence = [4, 6, 8, 10]
            expression = ['+', 2, 'y']
            length_to_generate = 5
            print(generate_rest(initial_sequence, expression, length_to_generate))
        output = f.getvalue().strip()
        self.assertEqual(expected_4, output)

    def test_generate_5(self):
        f = io.StringIO()
        with redirect_stdout(f):
            initial_sequence = [0, 1]
            expression = 'x'
            length_to_generate = 6
            print(generate_rest(initial_sequence, expression, length_to_generate))
        output = f.getvalue().strip()
        self.assertEqual(expected_5, output)

    def test_generate_6(self):
        f = io.StringIO()
        with redirect_stdout(f):
            initial_sequence = [0, 1]
            expression = ['+', 'x', 'y']
            length_to_generate = 5
            print(generate_rest(initial_sequence, expression, length_to_generate))
        output = f.getvalue().strip()
        self.assertEqual(expected_6, output)

    def test_generate_7(self):
        f = io.StringIO()
        with redirect_stdout(f):
            initial_sequence = [367, 367, 367]
            expression = 'y'
            length_to_generate = 5
            print(generate_rest(initial_sequence, expression, length_to_generate))
        output = f.getvalue().strip()
        self.assertEqual(expected_7, output)

    def test_generate_8(self):
        f = io.StringIO()
        with redirect_stdout(f):
            initial_sequence = [0, 1, 2]
            expression = -1
            length_to_generate = 5
            print(generate_rest(initial_sequence, expression, length_to_generate))
        output = f.getvalue().strip()
        self.assertEqual(expected_8, output)

    def test_generate_9(self):
        f = io.StringIO()
        with redirect_stdout(f):
            initial_sequence = [0, 1, 2]
            expression = 'i'
            length_to_generate = 0
            print(generate_rest(initial_sequence, expression, length_to_generate))
        output = f.getvalue().strip()
        self.assertEqual(expected_9, output)


if __name__ == '__main__':
    unittest.main()
