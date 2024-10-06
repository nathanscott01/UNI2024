import unittest
from generation_manipulation import *
from representation import is_valid_expression


class MyRandomExpressionTestCase(unittest.TestCase):
    def test_random_expression_1(self):
        function_symbols = ['f', 'g', 'h']
        constant_leaves = list(range(-2, 3))
        variable_leaves = ['x', 'y', 'i']
        leaves = constant_leaves + variable_leaves
        max_depth = 4

        for _ in range(10000):
            expression = random_expression(function_symbols, leaves, max_depth)
            if not is_valid_expression(expression, function_symbols, leaves):
                result = False
                break
        else:
            result = True
        self.assertEqual(True, result)

    def test_random_expression_2(self):
        function_symbols = ['f', 'g', 'h']
        leaves = ['x', 'y', 'i'] + list(range(-2, 3))
        max_depth = 4

        expressions = [random_expression(function_symbols, leaves, max_depth)
                       for _ in range(10000)]

        # Out of 10000 expressions, at least 1000 must be distinct
        result = check_distinctness(expressions)
        self.assertEqual(True, result)

    def test_random_expression_3(self):
        function_symbols = ['f', 'g', 'h']
        leaves = ['x', 'y', 'i'] + list(range(-2, 3))
        max_depth = 4

        expressions = [random_expression(function_symbols, leaves, max_depth)
                       for _ in range(10000)]

        # Out of 10000 expressions, there must be at least 100 expressions
        # of depth 0, 100 of depth 1, ..., and 100 of depth 4.

        result = check_diversity(expressions, max_depth)
        self.assertEqual(True, result)


if __name__ == '__main__':
    unittest.main()
