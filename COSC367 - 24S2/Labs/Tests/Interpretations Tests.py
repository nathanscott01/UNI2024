import unittest
import io
from contextlib import redirect_stdout
from interpretations import *

# Expected Outputs
expected1 = """{'p': False, 'q': False}
{'p': False, 'q': True}
{'p': True, 'q': False}
{'p': True, 'q': True}"""

expected2 = """{'human': False, 'mortal': False, 'rational': False}
{'human': False, 'mortal': False, 'rational': True}
{'human': False, 'mortal': True, 'rational': False}
{'human': False, 'mortal': True, 'rational': True}
{'human': True, 'mortal': False, 'rational': False}
{'human': True, 'mortal': False, 'rational': True}
{'human': True, 'mortal': True, 'rational': False}
{'human': True, 'mortal': True, 'rational': True}"""


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            atoms = {'q', 'p'}
            for i in interpretations(atoms):
                print(i)
        output = f.getvalue().strip()
        self.assertEqual(expected1, output)

    def test_example2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            atoms = {'human', 'mortal', 'rational'}
            for i in interpretations(atoms):
                print(i)
        output = f.getvalue().strip()
        self.assertEqual(expected2, output)


if __name__ == '__main__':
    unittest.main()
