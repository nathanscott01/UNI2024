"""
Nathan Scott
COSC367 Lab 6
Max and Min Value
Game Tree
"""
import math


def terminal_test(tree):
    """Check if tree is a leaf"""
    if type(tree) == int:
        return True
    return False


def max_value(tree):
    """Return the utility of tree when root is a max node"""
    if terminal_test(tree):
        return tree
    v = -1 * math.inf
    for child in tree:
        v = max(v, min_value(child))
    return v


def min_value(tree):
    """Return the utility of tree when root is a min node"""
    if terminal_test(tree):
        return tree
    v = math.inf
    for child in tree:
        v = min(v, max_value(child))
    return v
