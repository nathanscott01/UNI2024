"""
Nathan Scott
Student ID: 87357713
COSC262 Assignment 2
Longest Common String

Notes:
    LCS function written in Lab 9 Question 6 used recursion and was a top down solution.
    For this exercise, a bottom up approach needs to be implemented without recursion.
    Steps needed to solve this:

    1. Create a table
    2. Backtrack on the table to obtain the longest common string
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


def lcs(s1, s2):
    """Return the longest common string"""

    # Build a table
    lcs_table = build_lcs_table(s1, s2)
    # Find the longest common string
    longest_sequence = determine_sequence(lcs_table, s1, s2)
    return longest_sequence
