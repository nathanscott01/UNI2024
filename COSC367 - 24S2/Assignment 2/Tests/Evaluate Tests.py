import unittest
from evaluate import evaluate


class MyEvaluateTestCase(unittest.TestCase):
    def test_evaluate_1(self):
        bindings = {}
        expression = 12
        result = evaluate(expression, bindings)
        self.assertEqual(12, result)

    def test_evaluate_2(self):
        bindings = {'x': 5, 'y': 10, 'time': 15}
        expression = 'y'
        result = evaluate(expression, bindings)
        self.assertEqual(10, result)

    def test_evaluate_3(self):
        bindings = {'x': 5, 'y': 10, 'time': 15, 'add': lambda x, y: x + y}
        expression = ['add', 12, 'x']
        result = evaluate(expression, bindings)
        self.assertEqual(17, result)

    def test_evaluate_4(self):
        import operator
        bindings = dict(x=5, y=10, blah=15, add=operator.add)
        expression = ['add', ['add', 22, 'y'], 'x']
        result = evaluate(expression, bindings)
        self.assertEqual(37, result)


if __name__ == '__main__':
    unittest.main()
