"""
Nathan Scott
COSC367 Lab 6
Minimax Algorithm
"""


import math


def terminal_test(tree):
    """Check if tree is a leaf"""
    if type(tree) == int:
        return True
    return False


def successors(state):
    """Return all possible states"""
    state_list = []
    for i in range(len(state)):
        state_list.append(tuple((i, state[i])))
    return state_list


def max_action_value(game_tree):
    """Return a pair (best action from root, utility of root)"""
    if terminal_test(game_tree):
        return tuple((None, game_tree))
    v = -1 * math.inf
    w = -1
    for a, s in successors(game_tree):
        w1, v1 = min_action_value(s)
        if v1 > v:
            w, v = a, v1
    return w, v


def min_action_value(game_tree):
    """Return a pair (best action from root, utility of root)"""
    if terminal_test(game_tree):
        return tuple((None, game_tree))
    v = math.inf
    w = -1
    for a, s in successors(game_tree):
        w1, v1 = max_action_value(s)
        if v1 < v:
            w, v = a, v1
    return w, v

