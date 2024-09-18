"""
Nathan Scott
Test Revision
Location
"""
import heapq

from search import *
from math import sqrt


class LocationGraph(Graph):
    def __init__(self, location, radius, starting_nodes, goal_nodes):
        self.location = location
        self.radius = radius
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes

    def starting_nodes(self):
        return self._starting_nodes

    def is_goal(self, node):
        return node in self.goal_nodes

    def outgoing_arcs(self, tail):
        outgoing = []
        x1, y1 = self.location(tail)
        for node in self.location:
            if node != tail:
                x2, y2 = self.location(node)
                if sqrt((x1 - x2) ^ 2 + (y1 - y2) ^ 2) <= 5:
                    outgoing.append(node)
        return outgoing


class LCFSFrontier(Frontier):
    def __init__(self):
        self.container = []

    def add(self, path):
        heapq.heappush()

    def __iter__(self):
        return self

    def __next__(self):
