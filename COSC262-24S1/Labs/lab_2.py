"""
Nathan Scott
COSC262 Lab 2
"""

def sequence_length(n):
    """Return the number of numbers generated in the Collatz Sequence
    >>> sequence_length(22)
    16
    >>> sequence_length(1)
    1
    """
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + sequence_length(n/2)
    else:
        return 1 + sequence_length(3 * n + 1)
    
def recursive_divide(x, y):
    """Return what x // y would typically return
    >>> recursive_divide(8, 3)
    2
    """
    if x < y:
        return 0
    else:
        return 1 + recursive_divide(x-y, y)
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()

