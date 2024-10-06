"""
Nathan Scott
COSC367 Assignment 2
Representation
"""


"""
An object can be defined as an expression if one of the three properties hold:
    - Leaf is a constant eg 1, 4, 374
    - Leaf is a variable that appears in leaf_symbols
    - Leaf is a 3 part object
        * First element is a string found in function_symbol
        * Remaining two elements are expressions
"""


def is_valid_expression(object, function_symbols, leaf_symbols):
    """Determine if the first object is a valid expression"""
    if type(object) is int:
        return True
    elif type(object) is str and object in leaf_symbols:
        return True
    elif type(object) is list and len(object) == 3:
        e1, e2, e3 = object
        if e1 in function_symbols:
            if is_valid_expression(e2, function_symbols, leaf_symbols) and \
                    is_valid_expression(e3, function_symbols, leaf_symbols):
                return True
    return False


def depth(expression):
    """Determine the depth of the expression tree"""
    if type(expression) is int or type(expression) is str:
        return 0
    else:
        return 1 + max(depth(expression[1]), depth(expression[2]))

