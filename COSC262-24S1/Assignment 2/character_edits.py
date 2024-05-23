"""
Nathan Scott
Student ID: 87357713
COSC262 Assignment 2
Character Edits

Notes:
    Implementing a similar function to line_edits in line_edits.py, instead of
    making edits line by line, show the edits line by line, as well as highlighting
    the character(s) modified
"""


def determine_sequence(table, string1, string2):
    """Take the lcs table and backtrack to find the longest common string
    using a bottom up approach"""
    i, j = len(string1), len(string2)
    sequence = ""
    while i > 0 and j > 0:
        if string1[i - 1] == string2[j - 1]:
            sequence += string1[i - 1]
            i -= 1
            j -= 1
        else:
            if table[i - 1][j] >= table[i][j - 1]:
                i -= 1
            else:
                j -= 1
    return sequence[::-1]


def build_lcs_table(string1, string2):
    """Build a table and fill it with numbers that represent the length of the longest
    common string within the two given strings up to their respective indices"""
    # Create a table initialized to zeroes
    table = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]
    for i in range(1, len(string1) + 1):
        for j in range(1, len(string2) + 1):
            if string1[i - 1] == string2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table


def highlight_diff(s1, s2):
    """Highlight the differences between two strings using double square brackets"""
    table = build_lcs_table(s1, s2)
    lcs = determine_sequence(table, s1, s2)

    lcs_index = 0
    s1_modified = ""
    for char in s1:
        if lcs_index < len(lcs) and char == lcs[lcs_index]:
            s1_modified += char
            lcs_index += 1
        else:
            s1_modified += f"[[{char}]]"

    lcs_index = 0
    s2_modified = ""
    for char in s2:
        if lcs_index < len(lcs) and char == lcs[lcs_index]:
            s2_modified += char
            lcs_index += 1
        else:
            s2_modified += f"[[{char}]]"

    return s1_modified, s2_modified


def find_edits(table, string1, string2):
    """Make list of the edits in the form of 3-element tuples (operation, left_line, right_line).
    In the event of ties between the deletion, insertion and substitution costs,
    substitution should be preferred over deletion which in turn is to be preferred over insertion"""
    i, j = len(string1), len(string2)
    edit_list = []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and string1[i - 1] == string2[j - 1]:
            edit_list.append(('C', string1[i - 1], string2[j - 1]))
            i -= 1
            j -= 1
        elif i == 0:
            edit_list.append(('I', '', string2[j - 1]))
            j -= 1
        elif j == 0:
            edit_list.append(('D', string1[i - 1], ''))
            i -= 1
        else:
            distance = min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
            if distance == table[i - 1][j - 1]:
                if string1[i - 1] == '':
                    edit_list.append(('I', '', string2[j - 1]))
                elif string2[j - 1] == '':
                    edit_list.append(('D', string1[i - 1], ''))
                else:
                    highlighted_s1, highlighted_s2 = highlight_diff(string1[i - 1], string2[j - 1])
                    edit_list.append(('S', highlighted_s1, highlighted_s2))
                i -= 1
                j -= 1
            elif distance == table[i - 1][j]:
                edit_list.append(('D', string1[i - 1], ''))
                i -= 1
            else:
                edit_list.append(('I', '', string2[j - 1]))
                j -= 1
    return edit_list[::-1]


def make_distance_table(string1, string2):
    """Make an edit distance table from string1 and string2"""
    table = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]
    for i in range(len(string1) + 1):
        for j in range(len(string2) + 1):
            if i == 0 and j == 0:
                pass
            elif j == 0:
                table[i][j] = i
            elif i == 0:
                table[i][j] = j
            elif string1[i - 1] == string2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
    return table


def line_edits(s1, s2):
    """Return a list of the edited lines as 3 element tuples, where each tuple
    is of the form (operation, left_line, right_line) and show the individual
    modified characters"""
    s1 = s1.splitlines()
    s2 = s2.splitlines()
    distance_table = make_distance_table(s1, s2)
    edits_list = find_edits(distance_table, s1, s2)
    return edits_list
