"""
Nathan Scott
Student ID: 87357713
COSC262 Test 1 Revision
Travel Itinerary
"""


def next_vertex(in_tree, dist):
    """Find the next vertex that is not in tree and has the smallest distance"""
    min_distance = float('inf')
    closest_vertex = None
    for i in range(len(in_tree)):
        if not in_tree[i] and (dist[i] < min_distance):
            closest_vertex = i
            min_distance = dist[i]
    if closest_vertex is None:
        for i in range(len(in_tree)):
            if not in_tree[i] and (dist[i] == min_distance):
                closest_vertex = i
    return closest_vertex


def dijkstra(city_adj_list, start_point):
    """Use diskstras algorithm to find the shortest path from the starting vertex
    to all other points on the tree"""
    n = len(city_adj_list)
    in_tree = [False for i in range(n)]
    dist = [float('inf') for i in range(n)]
    parent = [None for i in range(n)]
    dist[start_point] = 0
    while not all(in_tree):
        u = next_vertex(in_tree, dist)
        in_tree[u] = True
        for vertex, weight in city_adj_list[u]:
            if not in_tree[vertex] and ((weight + dist[u]) < dist[vertex]):
                dist[vertex] = weight + dist[u]
                parent[vertex] = u
    return parent, dist


def tree_path(parent, s, t):
    """Find the path from the start to finish using the parent array"""
    if s == t:
        return [s]
    return tree_path(parent, s, parent[t]) + [t]


def travel_time(city_adj_list, path):
    """Take the path from start to finish, and return a list of tuples
    showing each point on the path, and the approximate time of arrival"""
    travel_clock = 0
    itinerary = [tuple((path[0], travel_clock))]
    for i in range(len(path) - 1):
        for element in city_adj_list[path[i]]:
            if element[0] == path[i + 1]:
                travel_clock += element[1]
                itinerary.append(tuple((path[i + 1], travel_clock)))
    return itinerary


def city_name_itinerary(itinerary, city_list):
    """Take the travel itinerary and where each tuple represents (location, time)
    and replace the location number with the name of the actual location"""
    city_itinerary = []
    for location in itinerary:
        city_itinerary.append(tuple((city_list[location[0]], location[1])))
    return city_itinerary


def travel_itinerary(adjacency_list, city_list, s, t):
    """Create a travel itinerary, with a path from the start to finish and the
    times of arrival at each stop"""
    parent, distance_array = dijkstra(adjacency_list, s)
    if distance_array[t] == float("inf"):
        return "No possible path from start to destination"
    path = tree_path(parent, s, t)
    itinerary = travel_time(adjacency_list, path)
    itinerary = city_name_itinerary(itinerary, city_list)
    return itinerary


cities = [
    "Invercargill",
    "Te Anau",
    "Milford Sound",
    "Dunedin",
    "Queenstown",
    "Christchurch",
    "Westport",
    "Nelson"
]

adj_list = [
    [(3, 2), (4, 2)],           # Invercargill, 0
    [(2, 1)],                   # Te Anau, 1
    [(1, 1)],                   # Milford Sound, 2
    [(0, 2), (5, 4), (4, 2)],   # Dunedin, 3
    [(0, 2), (3, 2), (5, 7)],   # Queenstown, 4
    [(3, 4), (4, 7), (7, 6)],   # Christchurch, 5
    [(7, 3)],                   # Westport, 6
    [(5, 6), (6, 3)]            # Nelson, 7
]

start = 6
destination = 4
print(travel_itinerary(adj_list, cities, start, destination))
