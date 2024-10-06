"""
Nathan Scott
COSC367 Assignment 2
Generation and Manipulation
"""


def check_distintness(expressions):
    """Check that there are at least 1000 distinct expressions"""
    return NotImplementedError


def check_diversity(expressions):
    """Check that there are at least 100 expressions each for depths 0 upto max depth"""
    return NotImplementedError


def random_expression(function_symbols, leaves, max_depth):
    """Generate a random expression"""
    return NotImplementedError


def prune(expression, max_depth, leaf_symbols):
    """Remove any nodes that are deeper than max_depth and return expression"""
    return NotImplementedError


def attach(expression1, expression2, position):
    """Return the expression that results from replacing the node at position
    in expression1 with expression2"""
    return NotImplementedError
