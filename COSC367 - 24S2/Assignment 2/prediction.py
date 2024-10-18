"""
Nathan Scott
COSC367 Assignment 2
Prediction
"""

""" The initial expression is made up of integers a[0], a[1], ... a[i] where i
is the position of the variable. The possible values within expression 
are x, y and i, and take the form f(x, y, i). These are defined as the following:
    1. x = a[i - 2]
    2. y = a[i - 1]
    3. i = position"""


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


def generate_rest(initial_sequence, expression, length):
    """Using the input expression and the initial sequence, return a list with
    the given length containing values that extend the initial sequence."""
    new_sequence = initial_sequence + [None] * length
    start = len(initial_sequence)
    for i in range(start, len(new_sequence)):
        binding = {'x' : new_sequence[i - 2], 'y' : new_sequence[i - 1], 'i' : i,
                   '+' : lambda x, y: x + y, '-' : lambda x, y: x - y,
                   '*' : lambda x, y: x * y}
        new_sequence[i] = evaluate(expression, binding)
    return new_sequence[len(initial_sequence):]
