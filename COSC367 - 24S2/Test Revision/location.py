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
        x1, y1 = self.location[tail]
        for head in self.location:
            if head != tail:
                x2, y2 = self.location[head]
                distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                if distance <= self.radius:
                    outgoing.append(Arc(tail, head, str(tail) + '->' + str(head), distance))
        return sorted(outgoing, key=lambda arc: arc.head)


class LCFSFrontier(Frontier):
    def __init__(self):
        self.container = []
        self.counter = 0
        self.node_tracker = {}

    def add(self, path):
        total_cost = sum(arc.cost for arc in path)
        head = path[-1].head
        if head is None:
            heapq.heappush(self.container, (total_cost, self.counter, path))
            self.counter += 1
        elif head not in self.node_tracker or total_cost < self.node_tracker[head]:
            heapq.heappush(self.container, (total_cost, self.counter, path))
            self.counter += 1
            self.node_tracker[head] = total_cost

    def __iter__(self):
        return self

    def __next__(self):
        if not self.container:
            raise StopIteration
        return heapq.heappop(self.container)[2]
