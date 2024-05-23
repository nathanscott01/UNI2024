"""
Nathan Scott
Student ID: 87357713
COSC262 Assignment 2
Line Edits

Notes:
    This program uses an edit-distance algorithm where it compares lines instead
    of characters. To solve this, two processes must occur:

    1. Make a table using Bottom-Up DP representing edit distance
    2. Back track on table to find the edits
"""


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
                    edit_list.append(('S', string1[i - 1], string2[j - 1]))
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
    is of the form (operation, left_line, right_line)"""
    s1 = s1.splitlines()
    s2 = s2.splitlines()
    distance_table = make_distance_table(s1, s2)
    edits_list = find_edits(distance_table, s1, s2)
    return edits_list
