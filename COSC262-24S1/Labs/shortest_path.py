""""
Nathan Scott
COSC262 Lab 4
Shortest Path Algorithms
"""


import math


def next_vertex(in_tree, distance):
    """Find the next vertex to process"""
    min_distance = float('inf')
    vertex_next = 0
    for vertex in range(len(in_tree)):
        if not in_tree[vertex] and (distance[vertex] <= min_distance):
            min_distance = distance[vertex]
            vertex_next = vertex
    return vertex_next


def dijkstra(adj, s):
    """Use Dijkstra's Algorithm to find the shortest path"""
    n = len(adj)
    in_tree = [False for _ in range(n)]
    distance = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[s] = 0
    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj[u]:
            if not in_tree[v] and ((distance[u] + weight) < distance[v]):
                distance[v] = distance[u] + weight
                parent[v] = u
    return parent, distance
