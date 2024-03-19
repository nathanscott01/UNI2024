"""
Nathan Scott
COSC262 Lab 5
Floyd-Warshall Algorithm
"""
import copy


def distance_matrix(adj_list):
    """Construct a distance matrix that can be used as an input for the floyd-warshall algorithm
    Input is an adjacency list where the graph is weighted"""
    matrix = [[0 for _ in range(len(adj_list))] for _ in range(len(adj_list))]
    for i in range(len(adj_list)):
        for j in range(len(adj_list)):
            adj_vertices = []
            for edge in adj_list[i]:
                if j == edge[0]:
                    matrix[i][j] = edge[1]
                    adj_vertices.append(j)
            if j not in adj_vertices and i is not j:
                matrix[i][j] = float('inf')
    return matrix


def floyd(distance):
    """Compute all-pairs shortest path using Floyd-Warshall Algorithm"""
    n = len(distance)
    updated_distance = copy.deepcopy(distance)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if updated_distance[i][j] > (updated_distance[i][k] + updated_distance[k][j]):
                    updated_distance[i][j] = updated_distance[i][k] + updated_distance[k][j]
    return updated_distance
