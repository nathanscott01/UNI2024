"""
Nathan Scott
Student ID: 87357713
COSC262 Assignment 1
Bubbles
"""
from queue import Queue


# noinspection DuplicatedCode
def process_graph(graph_string):
    """Process the graph string"""
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
    """Take a string representation of a graph and return an adjacency list"""
    directed, weighted, n_vertices, edges = process_graph(graph_string)
    adj_list = [[] for _ in range(n_vertices)]
    for edge in edges:
        if not weighted:
            edge = tuple((edge[0], edge[1], None))
        adj_list[edge[0]].append(edge[1:])
        if not directed:
            adj_list[edge[1]].append(tuple((edge[0], edge[2])))
    return adj_list


def modified_bfs(adj_list, q, state):
    """Perform a modified BFS loop on the adjacency list to find connected
    components. This only updates and returns the state array"""
    while not q.empty():
        u = q.get()
        for vertex, weight in adj_list[u]:
            if state[vertex] == 0:
                state[vertex] = 1
                q.put(vertex)
        state[u] = 2
    return state


def new_vertices(state, previous_state):
    """Return a set of vertices that are discovered in state,
    but not in the previous state"""
    component_list = list()
    for i in range(len(state)):
        if state[i] == 2 and previous_state[i] == 0:
            component_list.append(i)
    return component_list


def connected_components(adj_list):
    """Return a set of the connected components in the graph represented by
    adjacency list"""
    n = len(adj_list)
    state = [0 for _ in range(n)]
    q = Queue()
    components = list()
    for i in range(n):                                              # Iterate across all vertices
        if state[i] == 0:
            previous_state = state.copy()                           # Copies list across instead of referencing state
            q.put(i)
            state = modified_bfs(adj_list, q, state)                # Perform a BFS to find connected vertices
            new_component = new_vertices(state, previous_state)     # Create a list of the connected components
            components.append(new_component)                        # Add to the list of connected components
    return components


def bubbles(physical_contact_info):
    """Return a list of the connected components, which represent the bubbles
    of people within physical contact"""
    adj_list = adjacency_list(physical_contact_info)    # Create an adjacency list
    return connected_components(adj_list)         # Return the connected components
