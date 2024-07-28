"""
Nathan Scott
COSC367 Lab 2
Location Graph
LCFS Frontier
"""

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
        raise NotImplementedError()  # replace this line with a correct code

    def outgoing_arcs(self, tail):
        raise NotImplementedError()  # replace this line with a correct code


class LCFSFrontier(Frontier):
    """Implements a frontier container appropriate for breadth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        raise NotImplementedError()  # replace this line with a correct code

    def add(self, path):
        raise NotImplementedError()  # replace this line with a correct code

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        raise NotImplementedError()  # replace this line with a correct code