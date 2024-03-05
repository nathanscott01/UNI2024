"""
Nathan Scott
COSC262 Lab 3
BFS and DFS Trees
"""

from collections import deque
from adjacency import *
from pprint import pprint


def bfs_loop(adj_list, queue, state, parent):
    while queue:
        u = queue.popleft()
        for v in adj_list[u]:
            if state[v[0]] == 0:
                state[v[0]] = 1
                parent[v[0]] = u
                queue.append(v[0])
        state[u] = 2
    return parent


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


def dfs_loop(adj_list, start, state, parent):
    """Perform a DFS traversal of an adjacency list and
    return the parent array"""
    for v in adj_list[start]:
        if state[v[0]] == 0:
            state[v[0]] = 1
            parent[v[0]] = start
            dfs_loop(adj_list, v[0], state, parent)
    state[start] = 2
    return parent


def dfs_tree(adj_list, start):
    """Perform a BFS traversal of an adjacency list and
    return the parent array"""
    n = len(adj_list)
    state = [0 for _ in range(n)]
    parent = [None for _ in range(n)]
    state[start] = 1
    return dfs_loop(adj_list, start, state, parent)
