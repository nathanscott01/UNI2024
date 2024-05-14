import unittest
from line_edits import *

# Expected Outcomes
expected1 = [('C', 'Line1', 'Line1'),
             ('D', 'Line2', ''),
             ('C', 'Line3', 'Line3'),
             ('C', 'Line4', 'Line4'),
             ('I', '', 'Line5')]

expected2 = [('S', 'Line1', 'Line5'),
             ('S', 'Line2', 'Line4'),
             ('C', 'Line3', 'Line3'),
             ('D', 'Line4', '')]

expected3 = [('C', '# ============== DELETEs =====================', '# ============== DELETEs ====================='),
             ('D', '# TODO: add docstrings', ''),
             ('C', "@app.route('/queue/', methods=['DELETE'])", "@app.route('/queue/', methods=['DELETE'])"),
             ('C', 'def delete(hostname):', 'def delete(hostname):'),
             ('I', '', '    """Handle delete request from the given host"""'),
             ('C', '    try:', '    try:'),
             ('C', '        data = json.loads(request.get_data())', '        data = json.loads(request.get_data())'),
             ('S', "        mac_address = data['macAddress']", "        mac_address = data['mac_address']"),
             ('C', '    except:', '    except:')]


class MyLineEditsTest(unittest.TestCase):
    def test_line_edits1(self):
        s1 = "Line1\nLine2\nLine3\nLine4\n"
        s2 = "Line1\nLine3\nLine4\nLine5\n"
        result = line_edit(s1, s2)
        self.assertEqual(expected1, result)

    def test_line_edits2(self):
        s1 = "Line1\nLine2\nLine3\nLine4\n"
        s2 = "Line5\nLine4\nLine3\n"
        result = line_edit(s1, s2)
        self.assertEqual(expected2, result)

    def test_line_edits3(self):
        with open('edit_string1.txt', 'r') as file:
            s1 = file.read()
        with open('edit_string2.txt', 'r') as file:
            s2 = file.read()
        result = line_edit(s1, s2)
        self.assertEqual(expected3, result[:10])    # Only got examples upto line 9


if __name__ == '__main__':
    unittest.main()
