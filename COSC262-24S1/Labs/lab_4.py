"""
Nathan Scott
COSC262 Lab 3
"""

from Labs.adjacency import *
from collections import deque


def bfs_loop(adj_list, queue, state, parent):
    while queue:
        u = queue.popleft()
        for v in adj_list[u]:
            if state[v[0]] == 0:
                state[v[0]] = 1
                parent[v[0]] = u
                queue.append(v[0])
        state[u] = 2
    return state


def bfs_tree(adj_list, start):
    """Perform a BFS traversal of an adjacency list and
    return the parent array"""
    n = len(adj_list)
    state = [0 for _ in range(n)]
    parent = [None for _ in range(n)]
    queue = deque([])
    state[start] = 1
    queue.append(start)
    return bfs_loop(adj_list, queue, state, parent)


def transpose(adj_list):
    """Take the adjacency list of a graph and return the transpose
    adjacency list"""
    transposed_adj_list = [[] for _ in range(len(adj_list))]
    for vertex in range(len(adj_list)):
        for edge in adj_list[vertex]:
            transposed_adj_list[edge[0]].append(tuple((vertex, edge[1])))
    return transposed_adj_list


def is_strongly_connected(adj_list):
    """Return true if the graph is strongly connected"""
    state = bfs_tree(adj_list, 0)
    if 0 in state:
        return False
    transposed = transpose(adj_list)
    state = bfs_tree(transposed, 0)
    if 0 in state:
        return False
    return True
