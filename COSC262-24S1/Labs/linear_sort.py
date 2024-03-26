"""
Nathan Scott
COSC262 Lab 6
Linear Time Sort
"""


def key_positions(seq, key):
    """Count the number of times each key value appears in the sequence"""
    k = max(key(i) for i in seq)
    c_array = [0 for _ in range(k + 1)]
    for a in seq:
        c_array[key(a)] += 1
    counter = 0
    for i in range(k + 1):
        c_array[i], counter = counter, counter + c_array[i]
    return c_array


def sorted_array(seq, key, positions):
    """Return an array of positions sorted according to key function"""
    b_array = [None for _ in range(len(seq))]
    for a in seq:
        b_array[positions[key(a)]] = a
        positions[key(a)] += 1
    return b_array


def counting_sort(iterable, key):
    positions = key_positions(iterable, key)
    return sorted_array(iterable, key, positions)


def radix_key(d):
    """Return a function that takes the integer and returns the d'th digit"""
    return lambda number: int(str(number)[-d]) if len(str(number)) >= d else 0


def radix_sort(numbers, d):
    """Perform a radix sort on numbers"""
    radix_sorted = numbers.copy()
    for i in range(d):
        radix_sorted = counting_sort(radix_sorted, radix_key(i + 1))
    return radix_sorted
