"""
Nathan Scott
Student ID: 87357713
COSC262 Assignment 1
Batteries
"""


# noinspection DuplicatedCode
def process_graph(graph_str):
    """Process the graph string"""
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
    """Create an adjacency list from the graph string"""
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
    """Find the next closest vertex in the tree"""
    min_distance = float('inf')
    closest_vertex = None
    for i in range(len(in_tree)):
        if not in_tree[i] and (distance[i] < min_distance):
            min_distance = distance[i]
            closest_vertex = i
    if closest_vertex is None:
        return distance.index(min_distance)
    return closest_vertex


def dijkstra(adj_list, start):
    """Use dijkstra's method to find the shortest path from the starting vertex
    to every other vertex"""
    n = len(adj_list)
    in_tree = [False for _ in range(n)]
    distance = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[start] = 0
    if adj_list[start] == []:
        return distance
    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for vertex, weight in adj_list[u]:
            if not in_tree[vertex] and ((distance[u] + weight) < distance[vertex]):
                distance[vertex] = distance[u] + weight
                parent[vertex] = u
    return distance


def battery_required(distance_array):
    """Calculate the minimum battery required to travel the max distance.
    3 units of battery can travel 2 units of distance"""
    for i in range(len(distance_array)):
        if distance_array[i] == float("inf"):
            distance_array[i] = -1
    min_battery = 4 * max(distance_array)
    return min_battery


def min_capacity(city_map, depot_position):
    """Determine the minimum battery capacity needed to make a trip from the depot
    to any location within the city, and return with 25% of the capacity"""
    adj_list = adjacency_list(city_map)                     # Create an adjacency list
    distance_array = dijkstra(adj_list, depot_position)     # Find the distances to each location
    return battery_required(distance_array)                 # Find the minimum battery capacity
