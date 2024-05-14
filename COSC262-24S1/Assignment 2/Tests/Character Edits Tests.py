import unittest
from character_edits import *

# Expected Outcomes
expected1 = [('S', 'Line[[1]]', 'Line[[5]]'),
('S', '[[L]]ine[[ ]]2[[a]]', '[[l]]ine2'),
('C', 'Line3', 'Line3'),
('D', 'Line4', '')]


class MyCharacterEditsTest(unittest.TestCase):
    def test_line_edits1(self):
        s1 = "Line1\nLine 2a\nLine3\nLine4\n"
        s2 = "Line5\nline2\nLine3\n"
        result = line_edit(s1, s2)
        self.assertEqual(expected1, result)


if __name__ == '__main__':
    unittest.main()
