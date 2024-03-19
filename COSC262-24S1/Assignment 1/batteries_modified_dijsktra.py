"""
Nathan Scott
Student ID: 87357713
COSC262 Assignment 1
Batteries
Dijkstra's algorithm slightly modified

Description: The purpose of this exercise is to determine the battery required for vehicles.
We are given a city map in the form of a graph string. Each vertex represents a location, and each
edge represents the path between two locations, and its distance between the two locations.

The following conditions must be applied:
    - The company has a single depot and must be able to deliver to any location reachable from the
    depot
    - A delivery vehicle can travel 2 units of distance with 3 units of battery
    - A vehicle with a fully charged battery must be able to travel to any depot in the city and
    return with a minimum of 25% battery capacity
    - Given a destination, the vehicle will travel the minimum distance to get to that location

Edge cases:
    - Start vertex has no path to any locations
    - Graph is not strongly connected


Notes:
    - Dijkstra's algorithm is the first option to solving the minimum distance to each location
    from the depot. However, this algorithm iterates over ALL vertices in the tree, regardless of
    whether they are accessible. If algorithm is constructed poorly, the algorithm will run an
    infinite loop trying to solve an impossible problem (see batteries.py).
    - To iterate over only nodes accessible from the depot, should construct an alternative graph,
    where each node in the alternative graph represents the node in original graph.
    - Typically, a node is represented by its position in an adjacency list. To reference a node in
    the alternative graph, there must be a dictionary or a reference system set up so the algorithm
    only iterates over the relevant nodes, but can still represent the original data structure.
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


def dfs_loop(adj_list, start, state, location_list):
    """Run a dfs loop on the adjacency list. Return a list of accessible
    locations from start"""
    for vertex, weight in adj_list[start]:
        if state[vertex] == 0:
            state[vertex] = 1
            dfs_loop(adj_list, vertex, state, location_list)
    state[start] = 2
    location_list.append(start)
    return location_list


def dfs_search(adj_list, start):
    """Run a depth-first search to find all locations accessible from the
    starting location. Return a list of the accessible locations"""
    n = len(adj_list)
    state = [0 for _ in range(n)]
    state[start] = 1
    location_list = list()
    return sorted(dfs_loop(adj_list, start, state, location_list))


def smaller_adj_list(location_list, adj_list):
    """Create a smaller adjacency_list with only the locations reachable from depot"""
    modified_adj_list = []                          # Initialise a new adjacency list
    for location in location_list:
        modified_adj_list.append(adj_list[location])
    return modified_adj_list


def next_vertex(in_tree, distance):
    """Return the closest location to the tree"""
    min_distance = float("inf")
    for i in range(len(in_tree)):
        if not in_tree[i] and (distance[i] < min_distance):
            min_distance = distance[i]
            closest_vertex = i
    return closest_vertex


def dijkstra(reachable_locations, adj_list, start):
    """Use dijkstra's algorithm to find the shortest path from the start to each
    accessible location"""
    n = len(reachable_locations)
    in_tree = [False for _ in range(n)]
    distance = [float('inf') for _ in range(n)]
    distance[start] = 0
    if len(reachable_locations) == 1:
        return distance
    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for vertex, weight in adj_list[u]:
            vertex2 = reachable_locations.index(vertex)     # Use position of the vertex in the smaller distance list
            if not in_tree[vertex2] and ((distance[u] + weight) < distance[vertex2]):
                distance[vertex2] = distance[u] + weight
    return distance


def battery_required(distance):
    """Return the battery required to travel to the furthest location and
    return with 25% battery capacity left"""
    min_battery = 4 * max(distance)
    return min_battery


def min_capacity(city_map, depot_position):
    """Determine the minimum battery capacity needed to make a trip from the depot
    to any location within the city, and return with 25% of the capacity"""

    # Create an adjacency list
    adj_list = adjacency_list(city_map)

    # Find all the locations reachable from the depot
    reachable_locations = dfs_search(adj_list, depot_position)

    # Create a new adjacency list for only the reachable locations from depot
    modified_adj_list = smaller_adj_list(reachable_locations, adj_list)

    # Find the distance to each location
    depot_position_modified = reachable_locations.index(depot_position)
    distance_array = dijkstra(reachable_locations, modified_adj_list, depot_position_modified)

    # Return the battery required
    return battery_required(distance_array)
