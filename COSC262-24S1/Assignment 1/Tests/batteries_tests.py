import unittest
from batteries_modified_dijsktra import *

# Battery Examples
example1 = """\
U 4 W
0 2 5
0 3 2
3 2 1
"""

example2 = """\
U 3 W
0 1 3
0 2 5
"""

example3 = """\
U 7 W
0 1 6
1 2 6
0 2 10
0 3 3
3 4 3
4 5 1
"""

example4 = """\
U 1000 W
810 820 100
830 840 100
810 830 100
820 840 200
810 840 500
840 850 100
860 850 100
860 840 150
880 870 100
890 880 100
"""


# Expected Outcomes
outcome1 = 12

outcome2 = 0

outcome3 = 12

outcome4 = 8


class TestMinCapacityFunction(unittest.TestCase):
    def test_example1(self):
        result = min_capacity(example1, 0)
        self.assertEqual(outcome1, result)

    def test_example2(self):
        result = min_capacity(example1, 1)
        self.assertEqual(outcome2, result)

    def test_example3(self):
        result = min_capacity(example1, 2)
        self.assertEqual(outcome3, result)

    def test_example4(self):
        result = min_capacity(example1, 3)
        self.assertEqual(outcome4, result)

    def test_example5(self):
        result = min_capacity(example2, 0)
        self.assertEqual(20, result)

    def test_example6(self):
        result = min_capacity(example2, 1)
        self.assertEqual(32, result)

    def test_example7(self):
        result = min_capacity(example2, 2)
        self.assertEqual(32, result)

    def test_example8(self):
        result = min_capacity(example3, 0)
        self.assertEqual(40, result)

    def test_example9(self):
        result = min_capacity(example3, 1)
        self.assertEqual(52, result)

    def test_example10(self):
        result = min_capacity(example3, 2)
        self.assertEqual(68, result)

    def test_example11(self):
        result = min_capacity(example3, 3)
        self.assertEqual(52, result)

    def test_example12(self):
        result = min_capacity(example3, 4)
        self.assertEqual(64, result)

    def test_example13(self):
        result = min_capacity(example3, 5)
        self.assertEqual(68, result)

    def test_example14(self):
        result = min_capacity(example3, 6)
        self.assertEqual(0, result)

    def test_example15(self):
        result = min_capacity(example4, 810)
        self.assertEqual(1400, result)

    def test_example16(self):
        result = min_capacity(example4, 820)
        self.assertEqual(1400, result)

    def test_example17(self):
        result = min_capacity(example4, 890)
        self.assertEqual(800, result)


if __name__ == '__main__':
    unittest.main()
