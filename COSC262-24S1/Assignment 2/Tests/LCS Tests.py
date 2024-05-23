import unittest
from longest_common_string import *
import numpy as np
import numpy.testing as npt

lcs_values = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 2, 2, 2, 2, 2],
    [0, 0, 1, 1, 2, 2, 2, 3, 3],
    [0, 0, 1, 1, 2, 2, 2, 3, 4],
    [0, 1, 1, 2, 2, 2, 3, 3, 4],
    [0, 1, 2, 2, 2, 2, 3, 4, 4]
]


class MyLCSTest(unittest.TestCase):
    def test_lcs_table(self):
        s1 = "xyxxzx"
        s2 = "zxzyyzxx"
        result = build_lcs_table(s1, s2)
        self.assertEqual(result, lcs_values)

    def test_lcs1(self):
        s1 = "Look at me, I can fly!"
        s2 = "Look at that, it's a fly"
        result = lcs(s1, s2)
        expected = "Look at ,  a fly"
        self.assertEqual(expected, result)

    def test_lcs2(self):
        s1 = "abcdefghijklmnopqrstuvwxyz"
        s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
        result = lcs(s1, s2)
        expected = ""
        self.assertEqual(expected, result)

    def test_lcs3(self):
        s1 = "balderdash!"
        s2 = "balderdash!"
        result = lcs(s1, s2)
        expected = "balderdash!"
        self.assertEqual(expected, result)

    def test_lcs4(self):
        s1 = 1500 * 'x'
        s2 = 1500 * 'y'
        result = lcs(s1, s2)
        expected = ""
        self.assertEqual(expected, result)

    def test_lcs5(self):
        with open('string1.txt', 'r') as file:
            s1 = file.read()
        with open('string2.txt', 'r') as file:
            s2 = file.read()
        result = lcs(s1, s2)
        expected = " commonsubstring20"
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
