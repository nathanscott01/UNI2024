import unittest
import io
from contextlib import redirect_stdout
from minimax import *

# Expected Outputs
expected1 = """Best action if playing min: 1
Best guaranteed utility: 1

Best action if playing max: 2
Best guaranteed utility: 4"""

expected2 = """Best action if playing min: None
Best guaranteed utility: 3

Best action if playing max: None
Best guaranteed utility: 3"""

expected3 = """Best action if playing min: 0
Best guaranteed utility: 1

Best action if playing max: 2
Best guaranteed utility: 3"""


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            game_tree = [2, [-3, 1], 4, 1]
            action, value = min_action_value(game_tree)
            print("Best action if playing min:", action)
            print("Best guaranteed utility:", value)
            print()
            action, value = max_action_value(game_tree)
            print("Best action if playing max:", action)
            print("Best guaranteed utility:", value)
        output = f.getvalue().strip()
        self.assertEqual(expected1, output)

    def test_example2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            game_tree = 3
            action, value = min_action_value(game_tree)
            print("Best action if playing min:", action)
            print("Best guaranteed utility:", value)
            print()
            action, value = max_action_value(game_tree)
            print("Best action if playing max:", action)
            print("Best guaranteed utility:", value)
        output = f.getvalue().strip()
        self.assertEqual(expected2, output)

    def test_example3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            game_tree = [1, 2, [3]]
            action, value = min_action_value(game_tree)
            print("Best action if playing min:", action)
            print("Best guaranteed utility:", value)
            print()
            action, value = max_action_value(game_tree)
            print("Best action if playing max:", action)
            print("Best guaranteed utility:", value)
        output = f.getvalue().strip()
        self.assertEqual(expected3, output)


if __name__ == '__main__':
    unittest.main()
