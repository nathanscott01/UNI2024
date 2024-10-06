import unittest
from representation import is_valid_expression


class MyRepresentationValidTestCase(unittest.TestCase):
    def test_is_valid_1(self):
        function_symbols = ['f', '+']
        leaf_symbols = ['x', 'y']
        expression = 1
        result = is_valid_expression(expression, function_symbols, leaf_symbols)
        self.assertEqual(True, result)

    def test_is_valid_2(self):
        function_symbols = ['f', '+']
        leaf_symbols = ['x', 'y']
        expression = 'y'
        result = is_valid_expression(expression, function_symbols, leaf_symbols)
        self.assertEqual(True, result)

    def test_is_valid_3(self):
        function_symbols = ['f', '+']
        leaf_symbols = ['x', 'y']
        expression = 2.0
        result = is_valid_expression(expression, function_symbols, leaf_symbols)
        self.assertEqual(False, result)

    def test_is_valid_4(self):
        function_symbols = ['f', '+']
        leaf_symbols = ['x', 'y']
        expression = ['f', 123, 'x']
        result = is_valid_expression(expression, function_symbols, leaf_symbols)
        self.assertEqual(True, result)

    def test_is_valid_5(self):
        function_symbols = ['f', '+']
        leaf_symbols = ['x', 'y']
        expression = ['f', ['+', 0, -1], ['f', 1, 'x']]
        result = is_valid_expression(expression, function_symbols, leaf_symbols)
        self.assertEqual(True, result)

    def test_is_valid_6(self):
        function_symbols = ['f', '+']
        leaf_symbols = ['x', 'y']
        expression = ['+', ['f', 1, 'x'], -1]
        result = is_valid_expression(expression, function_symbols, leaf_symbols)
        self.assertEqual(True, result)

    def test_is_valid_7(self):
        function_symbols = ['f', '+']
        leaf_symbols = ['x', 'y', -1, 0, 1]
        expression = ['f', 0, ['f', 0, ['f', 0, ['f', 0, 'x']]]]
        result = is_valid_expression(expression, function_symbols, leaf_symbols)
        self.assertEqual(True, result)

    def test_is_valid_8(self):
        function_symbols = ['f', '+']
        leaf_symbols = ['x', 'y']
        expression = 'f'
        result = is_valid_expression(expression, function_symbols, leaf_symbols)
        self.assertEqual(False, result)

    def test_is_valid_9(self):
        function_symbols = ['f', '+']
        leaf_symbols = ['x', 'y']
        expression = ['f', 1, 0, -1]
        result = is_valid_expression(expression, function_symbols, leaf_symbols)
        self.assertEqual(False, result)

    def test_is_valid_10(self):
        function_symbols = ['f', '+']
        leaf_symbols = ['x', 'y']
        expression = ['x', 0, 1]
        result = is_valid_expression(expression, function_symbols, leaf_symbols)
        self.assertEqual(False, result)

    def test_is_valid_11(self):
        function_symbols = ['f', '+']
        leaf_symbols = ['x', 'y']
        expression = ['g', 0, 'y']
        result = is_valid_expression(expression, function_symbols, leaf_symbols)
        self.assertEqual(False, result)


if __name__ == '__main__':
    unittest.main()
