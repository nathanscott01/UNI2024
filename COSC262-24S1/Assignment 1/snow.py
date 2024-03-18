"""
Nathan Scott
Student ID: 87357713
COSC262 Assignment 1
Snow
"""


# noinspection DuplicatedCode
def process_graph(graph_str):
    """Process the graph"""
    directed = False
    weighted = False
    lines = [line.strip().split() for line in graph_str.splitlines()]
    key_info = lines[0]
    if key_info[0] == "D":
        directed = True
    if len(key_info) == 3:
        weighted = True
    n_vertices = int(key_info[1])
    edges = [tuple(map(int, line)) for line in lines[1:]]
    return directed, weighted, n_vertices, edges


def adjacency_list(graph_str):
    """Create an adjacency list from the graph_str"""
    directed, weighted, n_vertices, edges = process_graph(graph_str)
    adj_list = [[] for _ in range(n_vertices)]
    for edge in edges:
        if not weighted:
            edge = tuple((edge[0], edge[1], None))
        adj_list[edge[0]].append(edge[1:])
        if not directed:
            adj_list[edge[1]].append(tuple((edge[0], edge[2])))
    return adj_list


def next_vertex(in_tree, distance):
    """Return the closest vertex that is not part of the tree"""
    min_distance = float("inf")
    closest_vertex = None
    for i in range(len(in_tree)):
        if not in_tree[i] and (distance[i] < min_distance):
            closest_vertex = i
            min_distance = distance[i]
    return closest_vertex


def prims(adj_list, start=0):
    """Run prims algorithm to find a minimum spanning tree"""
    n = len(adj_list)
    in_tree = [False for _ in range(n)]
    distance = [float("inf") for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[start] = 0
    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for vertex, weight in adj_list[u]:
            if not in_tree[vertex] and (weight < distance[vertex]):
                distance[vertex] = weight
                parent[vertex] = u
    return parent


def find_segments(parent_array):
    """Turn each segment into tuples of adjacent vertices"""
    segments = list()
    for i in range(len(parent_array)):
        if parent_array[i] is not None:
            segment = tuple((parent_array[i], i))
            segments.append(segment)
    return segments


def which_segments(city_map):
    """Find a MST for the city map to show which roads need cleared"""
    adj_list = adjacency_list(city_map)     # Create an adjacency list
    parent_array = prims(adj_list)          # Find a minimal spanning tree
    return find_segments(parent_array)      # Return the segments of the tree as tuples (u, v)
