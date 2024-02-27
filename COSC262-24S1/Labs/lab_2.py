"""
Nathan Scott
COSC262 Lab 2
"""

import sys
sys.setrecursionlimit(10000)


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
    
def dumbo_func(data, n=0):
    """Take a list of numbers and record how many elements
    are not divisible by 3
    >>> data = [677, 90, 785, 875, 7, 90393, 10707]
    >>> dumbo_func(data)
    3
    """
    if n == len(data):
        return 0
    else:
        if (data[n] // 100) % 3 != 0:
            return 1 + dumbo_func(data, n + 1)
        else:
            return dumbo_func(data, n + 1)
        
def my_enumerate(items, n=0):
    """Create an enumerate function that works recursively
    >>> my_enumerate([10, 20, 30])
    [(0, 10), (1, 20), (2, 30)]
    >>> my_enumerate(['dog', 'pig', 'cow'])
    [(0, 'dog'), (1, 'pig'), (2, 'cow')]
    >>> my_enumerate([])
    []
    """
    if n == len(items):
        return []
    return [(n, items[n])] + my_enumerate(items, n + 1)

def num_rushes(slope_height, rush_height_gain, back_sliding):
    """Return the number of rushes it takes
    >>> num_rushes(10, 10, 9)
    1
    >>> num_rushes(100, 15, 7)
    19
    """
    if slope_height <= rush_height_gain:
        return 1
    slope_height = slope_height - rush_height_gain + back_sliding
    return 1 + num_rushes(slope_height, rush_height_gain * 0.95, back_sliding * 0.95)


NUM_RMDS = 9   # number of right-most digits required

def multiply2by2(A, B):
    """Takes two 2-by-2 matrices, A and B, and returns their product. The
    product will only contain a limited number of digits to cope with
    large numbers.  The input and output matrices are in the form of
    lists of lists (of lengths 2). This function only works for 2-by-2
    matrices. The size (dimensions) of the input does not grow with
    respect to n in the original problem. Therefore the time
    complexity of this function is Theta(1). This is different from
    the general matrix multiplication problem where the time
    complexity for multiplying two n-by-n matrices is O(n^3).

    """

    # compute the matrix product
    product = [
        [A[0][0]*B[0][0]+A[0][1]*B[1][0],	A[0][0]*B[0][1]+A[0][1]*B[1][1]],	 
        [A[1][0]*B[0][0]+A[1][1]*B[1][0],	A[1][0]*B[0][1]+A[1][1]*B[1][1]]
        ]
    
    # retain only the required number of digits on the right
    product = [[x % 10**NUM_RMDS for x in row] for row in product]
    
    return product

def matrix_power(A, n):
    """Takes a 2x2 matrix A and a non-negative integer n as exponent and
    returns A raised to the power of n (which will be a 2x2 matrix)."""
    
    # if n is 0 then return the identity matrix.
    if n == 0:
        return [[1, 0],
                [0, 1]]
    # Complete the rest
    else:
        p = matrix_power(A, n // 2)
        if n % 2 == 0:
            return multiply2by2(p, p)
        return multiply2by2(A, multiply2by2(p, p))
    

def fib(n):
    """Returns the n-th Fibonacci number by raising a special matrix to the
    power of n and returning an element on the off-diagonal.
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(7)
    13
    >>> fib(100)
    261915075
    """
    
    A = [[1, 1], 
         [1, 0]]
         
    return matrix_power(A, n)[0][1]



    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()

