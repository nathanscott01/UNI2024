import unittest
import io
from contextlib import redirect_stdout
from models import *

# Expected Outputs
expected1 = """[{'a': True, 'b': False, 'c': True}]"""

expected2 = """{'a': True, 'b': False, 'c': False, 'd': True}
{'a': True, 'b': False, 'c': True, 'd': False}
{'a': True, 'b': False, 'c': True, 'd': True}"""


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            knowledge_base = {
                lambda a, b: a and not b,
                lambda c: c
            }
            print(models(knowledge_base))
        output = f.getvalue().strip()
        self.assertEqual(expected1, output)

    def test_example2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            knowledge_base = {
                lambda a, b: a and not b,
                lambda c, d: c or d
            }
            for interpretation in models(knowledge_base):
                print(interpretation)
        output = f.getvalue().strip()
        self.assertEqual(expected2, output)


if __name__ == '__main__':
    unittest.main()
