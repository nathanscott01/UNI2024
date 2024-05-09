import unittest
from lcs import *


class MyLCSTest(unittest.TestCase):
    def test_lcs1(self):
        s1 = "abcde"
        s2 = "qbxxd"
        lcs_string = lcs(s1, s2)
        expected_lcs = "bd"
        self.assertEqual(expected_lcs, lcs_string)

    def test_lcs2(self):
        s1 = "Look at me, I can fly!"
        s2 = "Look at that, it's a fly"
        lcs_string = lcs(s1, s2)
        expected_lcs = "Look at ,  a fly"
        self.assertEqual(expected_lcs, lcs_string)

    def test_lcs3(self):
        s1 = "abcdefghijklmnopqrstuvwxyz"
        s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
        lcs_string = lcs(s1, s2)
        self.assertEqual("", lcs_string)

    def test_lcs4(self):
        s1 = "balderdash!"
        s2 = "balderdash!"
        lcs_string = lcs(s1, s2)
        expected_lcs = "balderdash!"
        self.assertEqual(expected_lcs, lcs_string)


if __name__ == '__main__':
    unittest.main()
