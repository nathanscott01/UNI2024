import unittest
from longest_common_string import *


class MyLCSTest(unittest.TestCase):
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
        expected = "CommonSubString"
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
