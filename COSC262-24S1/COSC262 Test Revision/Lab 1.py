"""Lab 1 Revision"""


def concat_list(strings):
    """Concatenate the strings recursively"""
    if not strings:
        return ''
    return strings[0] + concat_list(strings[1:])


def product(data):
    """Return the product of all elements in data, or -1 if data is empty"""
    if not data:
        return 1
    return data[0] * product(data[1:])


def backwards(s):
    """Return the string but backwards"""
    if not s:
        return ''
    return backwards(s[1:]) + s[0]


def odds(data):
    """Return a list of the odd elements in data"""
    if not data:
        return []
    elif data[0] % 2 == 1:
        return [data[0]] + odds(data[1:])
    else:
        return odds(data[1:])


def squares(data):
    """Return a list of all the squares of the elements in data"""
    if not data:
        return []
    return [data[0] ** 2] + squares(data[1:])


def find(data, value):
    """Find and return the index of the first occurrence of value in data"""
    if not data:
        return None
    if data[0] == value:
        return 0
    else:
        index = find(data[1:], value)
        if index is None:
            return None
        return 1 + index


def almost_all(numbers):
    """Asympotically most efficient implementation"""
    total = sum(numbers)
    return [total - x for x in numbers]