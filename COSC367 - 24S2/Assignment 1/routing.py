"""
Nathan Scott
Assignment 1
Routing
"""

from search import *


class RoutingGraph(Graph):
    def __init__(self, str_map):
        raise NotImplementedError

    def starting_nodes(self):
        raise NotImplementedError

    def is_goal(self, node):
        raise NotImplementedError

    def outgoing_arcs(self, tail_node):
        raise NotImplementedError
