""""
Nathan Scott
COSC262 Lab 8
Longest Common Subsequence
"""


def lcs(s1, s2):
    """Find the longest common subsequence in s1 and s2"""
    string_dict = {}

    def lcs_helper(s1, s2, string_dict):
        if (s1, s2) in string_dict:
            return string_dict[(s1, s2)]
        if s1 == "" or s2 == "":
            return ""
        elif s1[-1] == s2[-1]:
            result = lcs_helper(s1[:-1], s2[:-1], string_dict) + s1[-1]
        else:
            soln1 = lcs_helper(s1[:-1], s2, string_dict)
            soln2 = lcs_helper(s1, s2[:-1], string_dict)
            if len(soln1) > len(soln2):
                result = soln1
            else:
                result = soln2
        string_dict[(s1, s2)] = result
        return result

    return lcs_helper(s1, s2, string_dict)
