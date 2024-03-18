"""
Nathan Scott
Student ID: 87357713
COSC262 Assignment 1
Converters
"""

from queue import Queue


# noinspection DuplicatedCode
def process_graph(graph_str):
    """Helped function for adjacency_list, this will determine if the graph is
    directed or undirected, and if it is weighted or unweighted, determine the
    number of vertices and also return the edges formatted as tuples"""
    directed = False
    weighted = False
    lines = [line.strip().split() for line in graph_str.splitlines()]
    key_information = lines[0]
    if key_information[0] == "D":
        directed = True
    if len(key_information) == 3:
        weighted = True
    n_vertices = int(key_information[1])
    edges = [tuple(map(int, line)) for line in lines[1:]]
    return directed, weighted, n_vertices, edges


def adjacency_list(graph_str):
    """Take a graph string and return an adjacency list"""
    directed, weighted, n_vertices, edges = process_graph(graph_str)
    adj_list = [[] for _ in range(n_vertices)]
    for edge in edges:
        if not weighted:
            edge = tuple((edge[0], edge[1], None))
        adj_list[edge[0]].append(edge[1:])
        if not directed:
            adj_list[edge[1]].append(tuple((edge[0], edge[2])))
    return adj_list


def bfs_loop(adj_list, q, state, parent):
    """Perform a bfs loop on the adjacency list"""
    while not q.empty():
        u = q.get()
        for v in adj_list[u]:
            if state[v[0]] == 0:
                state[v[0]] = 1
                parent[v[0]] = u
                q.put(v[0])
        state[u] = 2
    return parent


def bfs_search(adj_list, s):
    """Breadth-first search for the adjacency list starting at s"""
    n = len(adj_list)
    state = [0 for _ in range(n)]
    parent = [None for _ in range(n)]
    q = Queue()
    state[s] = 1
    q.put(s)
    return bfs_loop(adj_list, q, state, parent)


def tree_path(parent, start, destination):
    """Return the shortest path from start to destination"""
    if start == destination:
        return [start]
    elif parent[destination] is None:
        return [None]
    return tree_path(parent, start, parent[destination]) + [destination]


def format_sequence(converters_info, source_format, destination_format):
    """Return the shortest sequence of conversions required to convert the file
    from the source format to the destination format. Converters info is a
    textual graph representation of the possible conversions between file types"""
    adj_list = adjacency_list(converters_info)                          # Create an adjacency list
    parent = bfs_search(adj_list, source_format)                        # Find a Parent list using BFS
    sequence = tree_path(parent, source_format, destination_format)     # Find the shortest path
    if None not in sequence:
        return sequence
    return "No solution!"
