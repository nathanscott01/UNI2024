"""
Nathan Scott
COSC262 Lab 5
Backtracking
"""


def permutations(s):
    solutions = []
    dfs_backtrack((), s, solutions)
    return solutions


def dfs_backtrack(candidate, input_data, output_data):
    if should_prune(candidate):
        return
    if is_solution(candidate, input_data):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, input_data):
            dfs_backtrack(child_candidate, input_data, output_data)


def add_to_output(candidate, output_data):
    output_data.append(candidate)


def should_prune(candidate):
    return False


def is_solution(candidate, input_data):
    """Returns True if the candidate is a complete solution"""
    return len(candidate) == len(input_data)


def children(candidate, input_data):
    """Returns a collection of candidates that are the children of the given
    candidate."""
    # Complete the code
    data = list(input_data)
    candidate_list = list(candidate)
    n = len(data)
    tuples_needed = n - len(candidate)
    new_tuple_length = len(candidate) + 1
    tuple_list = [candidate_list[:] for _ in range(tuples_needed)]
    i = 0
    for perm in tuple_list:
        while i < n and len(perm) < new_tuple_length:
            if data[i] not in perm:
                perm.append(data[i])
            i += 1
    return tuple(tuple(perm) for perm in tuple_list)
