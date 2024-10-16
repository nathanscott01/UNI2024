"""
Nathan Scott
COSC367 Assignment 2
Generation and Manipulation
"""

from representation import depth
import random


def check_distinctness(expressions):
    """Check that there are at least 1000 distinct expressions"""
    expression_list = []
    for e in expressions:
        if e not in expression_list:
            expression_list.append(str(e))
    return len(expression_list) >= 1000


def check_diversity(expressions, max_depth):
    """Check that there are at least 100 expressions each for depths 0 upto max depth"""
    depth_counter = [0 for _ in range(max_depth + 1)]
    for e in expressions:
        d = depth(e)
        depth_counter[d] += 1
    diverse = True
    for i in depth_counter:
        if i < 100:
            diverse = False
    return diverse


def random_expression(function_symbols, leaves, max_depth):
    """Generate a random expression"""
    choose_leaf = random.randint(0, 1)
    if max_depth == 0 or choose_leaf == 0:
        return random.choice(leaves)
    e1 = random.choice(function_symbols)
    e2 = random_expression(function_symbols, leaves, max_depth-1)
    e3 = random_expression(function_symbols, leaves, max_depth-1)
    return [e1, e2, e3]


def prune(expression, max_depth, leaf_symbols):
    """Remove any nodes that are deeper than max_depth and return expression"""
    if type(expression) is int:
        return expression
    elif len(expression) == 1:
        return expression
    elif max_depth == 0:
        return random.choice(leaf_symbols)
    else:
        e1, e2, e3 = expression
        e2_p = prune(e2, max_depth - 1, leaf_symbols)
        e3_p = prune(e3, max_depth - 1, leaf_symbols)
        return [e1, e2_p, e3_p]


def attach(expression1, expression2, position):
    """Return the expression that results from replacing the node at position
    in expression1 with expression2"""
    def replace_node(expr, pos):
        """Perform a preorder traversal to find the node at position"""
        if pos[0] == position:
            return expression2

        if isinstance(expr, list) and len(expr) == 3:
            pos[0] += 1
            l = replace_node(expr[1], pos)
            pos[0] += 1
            r = replace_node(expr[2], pos)
            return [expr[0], l, r]

        return expr

    return replace_node(expression1, [0])
