import unittest
from character_edits import *

# Expected Outcomes
expected1 = [('S', 'Line[[1]]', 'Line[[5]]'),
             ('S', '[[L]]ine[[ ]]2[[a]]', '[[l]]ine2'),
             ('C', 'Line3', 'Line3'),
             ('D', 'Line4', '')]

expected2 = ('S', "        mac_address = data['mac[[A]]ddress']", "        mac_address = data['mac[[_]][[a]]ddress']")


class MyCharacterEditsTest(unittest.TestCase):
    def test_line_edits1(self):
        s1 = "Line1\nLine 2a\nLine3\nLine4\n"
        s2 = "Line5\nline2\nLine3\n"
        result = line_edits(s1, s2)
        self.assertEqual(expected1, result)

    def test_line_edits2(self):
        with open('edit_string1.txt', 'r') as file:
            s1 = file.read()
        with open('edit_string2.txt', 'r') as file:
            s2 = file.read()
        result = line_edits(s1, s2)
        self.assertEqual(expected2, result[7])


if __name__ == '__main__':
    unittest.main()
