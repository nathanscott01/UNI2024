"""
Nathan Scott
COSC262 Lab 5
All Paths Backtrack
"""


def dfs_backtrack(candidate, adj_list, destination, output_data):
    if should_prune(candidate):
        return
    if is_solution(candidate, destination):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, adj_list):
            dfs_backtrack(child_candidate, adj_list, destination, output_data)


def add_to_output(candidate, output_data):
    if candidate not in output_data:
        output_data.append(candidate)


def should_prune(candidate):
    return False


def is_solution(candidate, destination):
    """Returns True if the candidate is a complete solution"""
    return candidate[-1] == destination


def possible_paths(path, adj_list):
    """Return all possible edges that do not circle back onto path"""
    last_node = path[-1]
    next_paths = []
    for vertex, weight in adj_list[last_node]:
        if vertex not in path:
            next_paths.append(vertex)
    return next_paths


def children(candidate, adj_list):
    """Return all possible paths with the next possible vertex."""
    current_path = list(candidate)
    last_vertex = current_path[-1]
    new_path_length = len(current_path) + 1
    next_nodes = possible_paths(current_path, adj_list)
    new_paths = [current_path[:] for _ in range(len(next_nodes))]
    i = 0
    for path in new_paths:
        while i < len(next_nodes) and len(path) < new_path_length:
            if next_nodes[i] not in path:
                path.append(next_nodes[i])
            i += 1
    return tuple(tuple(path) for path in new_paths)


def all_paths(adj_list, source, destination):
    """Return a list of all possible simple paths from source to destination using backtracking"""
    solutions = []
    starting_node = tuple((source, ))
    dfs_backtrack(starting_node, adj_list, destination, solutions)
    return solutions
