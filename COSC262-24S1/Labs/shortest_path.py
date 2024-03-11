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
