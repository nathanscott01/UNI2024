"""
Nathan Scott
Assignment 1
Routing
"""
import heapq
from search import *
import math


class RoutingGraph(Graph):
    def __init__(self, str_map):
        self.str_map = [line.strip() for line in str_map.splitlines() if line.strip()]


    def starting_nodes(self):
        agents = []
        for i in range(len(self.str_map)):
            for j in range(len(self.str_map[i])):
                if self.str_map[i][j] == 'S':
                    agents.append((i, j, math.inf))
                elif self.str_map[i][j].isdigit():
                    agents.append((i, j, int(self.str_map[i][j])))
        return agents


    def is_goal(self, node):
        row, col, fuel = node
        if self.str_map[row][col] == 'G':
            return True
        return False


    def outgoing_arcs(self, tail_node):
        obstacle = '+-|X'
        direction_list = [
            ('N', -1, 0),  # North: move up
            ('NE', -1, 1),  # Northeast: move up and right
            ('E', 0, 1),  # East: move right
            ('SE', 1, 1),  # Southeast: move down and right
            ('S', 1, 0),  # South: move down
            ('SW', 1, -1),  # Southwest: move down and left
            ('W', 0, -1),  # West: move left
            ('NW', -1, -1)  # Northwest: move up and left
        ]
        row, col, f = tail_node
        outgoing = []

        # Find outgoing arcs
        if f > 0:
            for direction in direction_list:
                next_dir, y, x = direction
                n_row, n_col = row + y, col + x
                if self.str_map[n_row][n_col] not in obstacle:
                    if x == 0 or y == 0:
                        move_time = 5
                    else:
                        move_time = 7
                    outgoing.append(Arc(tail_node, (n_row, n_col, f - 1), next_dir, move_time))

        # Check if agent at a fuel stop
        if self.str_map[row][col] == 'F' and f < 9:
            outgoing.append(Arc(tail_node, (row, col, 9), "Fuel up", 15))

        # Check if agent at a portal
        if self.str_map[row][col] == 'P':
            for i in range(len(self.str_map)):
                for j in range(len(self.str_map[i])):
                    if self.str_map[i][j] == 'P':
                        if i != row and j != col:
                            outgoing.append(Arc(tail_node, (i, j, f), "Teleport to ({}, {})".format(i, j), 10))

        return outgoing

    def estimated_cost_to_goal(self, node):
        return 0


class AStarFrontier(Frontier):

    def __init__(self, str_map):
        self.container = []
        self.nodes = {}
        self.str_map = str_map

    def add(self, path):
        path_cost = sum(arc.cost for arc in path)
        head = path[-1].head
        goal_cost = self.str_map.estimated_cost_to_goal(head)
        total_cost = path_cost + goal_cost
        if head not in self.nodes or total_cost < self.nodes[head]:
            heapq.heappush(self.container, (total_cost, path))
            self.nodes[head] = total_cost


    def __iter__(self):
        return self

    def __next__(self):
        if not self.container:
            raise StopIteration
        return heapq.heappop(self.container)[1]