import unittest
import io
from contextlib import redirect_stdout
from prediction import predict_rest


# Expected Outputs
expected_1 = """[0, 1, 2, 3, 4, 5, 6, 7]
[8, 9, 10, 11, 12]"""

expected_2 = """[16, 18, 20, 22, 24]"""

expected_3 = """[19, 17, 15, 13, 11]"""

expected_4 = """[64, 81, 100, 121, 144]"""

expected_5 = """[51, 66, 83, 102, 123]"""

expected_6 = """[21, 34, 55, 89, 144]"""

expected_7 = """[5, -4, 29, -13, 854]"""

expected_8 = """[-1055, 2547, -6149, 14845, -35839]]"""


class MyPredictTestCase(unittest.TestCase):
    def test_predict_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            sequence = [0, 1, 2, 3, 4, 5, 6, 7]
            the_rest = predict_rest(sequence)
            print(sequence)
            print(the_rest)
        output = f.getvalue().strip()
        self.assertEqual(expected_1, output)

    def test_predict_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            sequence = [0, 2, 4, 6, 8, 10, 12, 14]
            print(predict_rest(sequence))
        output = f.getvalue().strip()
        self.assertEqual(expected_2, output)

    def test_predict_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            sequence = [31, 29, 27, 25, 23, 21]
            print(predict_rest(sequence))
        output = f.getvalue().strip()
        self.assertEqual(expected_3, output)

    def test_predict_4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            sequence = [0, 1, 4, 9, 16, 25, 36, 49]
            print(predict_rest(sequence))
        output = f.getvalue().strip()
        self.assertEqual(expected_4, output)

    def test_predict_5(self):
        f = io.StringIO()
        with redirect_stdout(f):
            sequence = [3, 2, 3, 6, 11, 18, 27, 38]
            print(predict_rest(sequence))
        output = f.getvalue().strip()
        self.assertEqual(expected_5, output)

    def test_predict_6(self):
        f = io.StringIO()
        with redirect_stdout(f):
            sequence = [0, 1, 1, 2, 3, 5, 8, 13]
            print(predict_rest(sequence))
        output = f.getvalue().strip()
        self.assertEqual(expected_6, output)

    def test_predict_7(self):
        f = io.StringIO()
        with redirect_stdout(f):
            sequence = [0, -1, 1, 0, 1, -1, 2, -1]
            print(predict_rest(sequence))
        output = f.getvalue().strip()
        self.assertEqual(expected_7, output)

    def test_predict_8(self):
        f = io.StringIO()
        with redirect_stdout(f):
            sequence = [1, 3, -5, 13, -31, 75, -181, 437]
            print(predict_rest(sequence))
        output = f.getvalue().strip()
        self.assertEqual(expected_8, output)


if __name__ == '__main__':
    unittest.main()
