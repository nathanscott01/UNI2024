"""
Nathan Scott
COSC262 Lab 1
"""

def concat_list(strings):
    """Take a list of strings and return them concatenated together
    >>> ans = concat_list(['a', 'hot', 'day'])
    >>> print(ans)
    ahotday
    >>> ans = concat_list(['x', 'y', 'z'])
    >>> print(ans)
    xyz
    >>> concat_list([])
    ''
    """
    if len(strings) > 1:
        return strings[0] + concat_list(strings[1:])
    elif len(strings) == 1:
        return strings[0]
    else:
        return ''

def product(data):
    """Return the product of all elements within the list data, 
    unless it is empty in which case 1 is returned
    >>> product([])
    1
    >>> product([1, 13, 9, -11])
    -1287
    >>> product([1, 13, 9, 11])
    1287
    """
    if len(data) > 1:
        return data[0] * product(data[1:])
    elif len(data) == 1:
        return data[0]
    else:
        return 1
    
def backwards(s):
    """Return the string backwards recursively
    >>> backwards("Hi there!")
    '!ereht iH'
    >>> backwards("racecar")
    'racecar'
    >>> backwards("")
    ''
    """
    if len(s) > 1:
        return s[-1] + backwards(s[:-1])
    elif len(s) == 1:
        return s
    else:
        return ''
    
def odds(data):
    """Return the a list of the odd elements within data
    >>> odds([0, 1, 12, 13, 14, 9, -11, -20])
    [1, 13, 9, -11]
    >>> odds([])
    []
    >>> odds([0, 0, 0])
    []
    >>> odds([-1, -3, -7])
    [-1, -3, -7]
    >>> odds([-2, -4, -6])
    []
    >>> odds([1.2, 1.4, 1.5])
    []
    """
    if not data:
        return []
    if data[0] % 2 == 1:
        return [data[0]] + odds(data[1:])
    return odds(data[1:])
    
def squares(data):
    """Return a list of all the squares of the numbers in data
    >>> squares([1, 13, 9, -11])
    [1, 169, 81, 121]
    >>> squares([0, -3, 2])
    [0, 9, 4]
    >>> squares([])
    []
    """
    if not data:
        return []
    return [data[0] ** 2] + squares(data[1:])

def find(data, value):
    """Return the index of the first occurance of value in data
    >>> find(["hi", "there", "you", "there"], "there")
    1
    >>> find([10, 20, 30], 0)
    >>> find([10, 20, 30], 10)
    0
    >>> find([10, 20, 30], 30)
    2
    """
    if not data:
        return None
    if data[0] == value:
        return 0
    else:
        if find(data[1:], value) is not None:
            return 1 + find(data[1:], value)
        return None
    ### Major run time, is searching recursive tree twice for each comparison
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
 
print(squares([1, 13, 9, -11])) 	
#print(find(list(range(0,51)), 50))
