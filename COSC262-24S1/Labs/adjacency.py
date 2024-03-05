"""
Nathan Scott
COSC262 Lab 3
Adjacency List
"""


def adjacency_list(graph_str):
    """Create an adjacency list from graph_str which is a textual
    representation of a graph"""
    directed = False
    weighted = False

    # Split the string into lines and remove newlines
    lines = [line.strip() for line in graph_str.splitlines() if line.strip()]

    # Graph Details
    graph_info = lines[0].split()
    if graph_info[0] == "D":            # Check if graph is directed
        directed = True
    if len(graph_info) == 3:            # Check if graph is weighted
        weighted = True
    v = int(graph_info[1])              # Check the number of vertices on graph

    # Extract each element and make tuples representing each edge
    edges = [tuple(map(int, line.split())) for line in lines[1:]]

    # Build adjacency list
    adj_list = [[] for _ in range(v)]       # Initialise adjacency list
    for edge in edges:
        if not weighted:
            edge = tuple((edge[0], edge[1], None))
        adj_list[edge[0]].append(edge[1:])
        if not directed:
            reversed_edge = tuple((edge[0], edge[2]))
            adj_list[edge[1]].append(reversed_edge)
    return adj_list


from pprint import pprint

graph_string = """\
U 17
1 2
1 15
1 6
12 13
2 15
13 4
4 5
"""

pprint(adjacency_list(graph_string))