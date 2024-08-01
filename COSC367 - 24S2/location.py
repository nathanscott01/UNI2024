"""
Nathan Scott
COSC367 Lab 2
Location Graph
LCFS Frontier
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
        return node == self.goal_nodes

    def outgoing_arcs(self, tail):
        """Iterate through each node. Check if node meets criterea and add to list"""
        arcs = []
        tail_coord = self.location[tail]    # The co-ordinates referenced by tail
        for head, coord in self.location.items():
            if head is not tail:
                distance = sqrt((coord[0] - tail_coord[0]) ** 2 + (coord[1] - tail_coord[1]) ** 2)
                if distance <= self.radius:
                    arcs.append(Arc(tail, head, str(tail) + '->' + str(head), distance))
        return sorted(arcs, key=lambda arc: arc.head)


class LCFSFrontier(Frontier):
    """Implements a frontier container appropriate for lowest cost first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []
        self.counter = 0

    def add(self, path):
        total_cost = sum(arc.cost for arc in path)
        heapq.heappush(self.container, (total_cost, self.counter, path))
        self.counter += 1

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if not self.container:
            raise StopIteration
        return heapq.heappop(self.container)[2]
