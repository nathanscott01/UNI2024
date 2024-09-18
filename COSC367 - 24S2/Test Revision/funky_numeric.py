"""
Nathan Scott
Test Revision
Funky Numeric
"""

from search import *
from collections import deque


class FunkyNumericGraph(Graph):

    def __init__(self, starting_number):
        self.starting_number = starting_number

    def is_goal(self, node):
        return node % 10 == 0

    def starting_nodes(self):
        return [self.starting_number]

    def outgoing_arcs(self, tail_node):
        arcs = []
        arcs.append(Arc(tail_node, tail_node-1, "1down", 1))
        arcs.append(Arc(tail_node, tail_node+2, "2up", 1))
        return arcs


class BFSFrontier(Frontier):

    def __init__(self):
        self.container = deque()

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.container) > 0:
            next_path = self.container.popleft()
            return next_path
        else:
            raise StopIteration
