import unittest
from representation import depth


class MyRepresentationValidTestCase(unittest.TestCase):
    def test_depth_1(self):
        expression = 12
        result = depth(expression)
        self.assertEqual(0, result)

    def test_depth_2(self):
        expression = 'weight'
        result = depth(expression)
        self.assertEqual(0, result)

    def test_depth_3(self):
        expression = ['add', 12, 'x']
        result = depth(expression)
        self.assertEqual(1, result)

    def test_depth_4(self):
        expression = ['add', ['add', 22, 'y'], 'x']
        result = depth(expression)
        self.assertEqual(2, result)

    def test_depth_5(self):
        expression = ['+', ['*', 2, 'i'], ['*', -3, 'x']]
        result = depth(expression)
        self.assertEqual(2, result)


if __name__ == '__main__':
    unittest.main()
