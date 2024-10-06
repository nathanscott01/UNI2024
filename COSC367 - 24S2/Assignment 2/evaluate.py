"""
Nathan Scott
COSC367 Assignment 2
Evaluate
"""


def evaluate(expression, bindings):
    """Take the expression and the dictionary of bindings and return the
    value of the expression"""
    if type(expression) is int:
        return expression
    elif type(expression) is str and expression in bindings:
        return bindings[expression]
    elif type(expression) is list and len(expression) == 3:
        e0, e1, e2 = bindings[expression[0]], evaluate(expression[1], bindings), evaluate((expression[2]), bindings)
        return e0(e1, e2)
