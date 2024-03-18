"""
Nathan Scott
Student ID: 87357713
COSC262 Assignment 1
Package Management
"""


# noinspection DuplicatedCode
def process_graph(graph_string):
    """Process the graph"""
    directed = False
    weighted = False
    lines = [line.strip().split() for line in graph_string.splitlines()]
    key_info = lines[0]
    if key_info[0] == "D":
        directed = True
    if len(key_info) == 3:
        weighted = True
    n_vertices = int(key_info[1])
    edges = [tuple(map(int, line)) for line in lines[1:]]
    return directed, weighted, n_vertices, edges


def adjacency_list(graph_string):
    """Return the adjacency list of the graph string"""
    directed, weighted, n_vertices, edges = process_graph(graph_string)
    adj_list = [[] for _ in range(n_vertices)]
    for edge in edges:
        if not weighted:
            edge = tuple((edge[0], edge[1], None))
        adj_list[edge[0]].append(edge[1:])
        if not directed:
            adj_list[edge[1]].append(tuple((edge[0], edge[2])))
    return adj_list


def topological_dfs_loop(adj_list, start, state, parent, stack):
    """Perform a modified dfs loop"""
    for v, weight in adj_list[start]:
        if state[v] == 0:
            state[v] = 1
            parent[v] = start
            topological_dfs_loop(adj_list, v, state, parent, stack)
    state[start] = 2
    stack.insert(0, start)
    return stack


def topological_order(adj_list):
    """Return a stack showing the topological order of the graph"""
    n = len(adj_list)
    state = [0 for _ in range(n)]
    parent = [None for _ in range(n)]
    stack = list()
    for u in range(n):
        if state[u] == 0:
            stack = topological_dfs_loop(adj_list, u, state, parent, stack)
    return stack


def build_order(programs):
    """Find the build order for the programs based on their dependencies
    which is the topological order for the graph represented by programs"""
    adj_list = adjacency_list(programs)
    return topological_order(adj_list)
