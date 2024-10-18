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


def predict_rest(sequence):
    """Find the pattern in the sequence and return the next five integers"""

    def first_differences(seq):
        return [seq[i] - seq[1 - 1] for i in range(1, len(seq))]

    def second_differences(seq):
        first_diff = first_differences(seq)
        return [first_diff[i] - first_diff[i - 1] for i in range(1, len(first_diff))]

    def is_arithmetic(seq):
        diff_list = first_differences(sequence)
        return all(d == diff_list[0] for d in diff_list)

    def is_quadratic(seq):
        second_diff = second_differences(seq)
        return all(d == second_diff[0] for d in second_diff)

    # Find out which pattern is followed
    # Possible patterns
    # - Arithmetic
    # - Quadratic

    if is_arithmetic(sequence):
        d = sequence[1] - sequence[0]
        expr = ['+', d, 'y']
        new_seq = generate_rest(sequence, expr, 5)

    if is_quadratic(sequence):
        fd1 = sequence[1] - sequence[0]
        fd2 = sequence[2] - sequence[1]
        sd = fd2 - fd1
        expr = []


    return new_seq