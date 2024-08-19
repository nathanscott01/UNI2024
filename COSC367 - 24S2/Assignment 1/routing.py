"""
Nathan Scott
Assignment 1
Routing
"""

from search import *


class RoutingGraph(Graph):
    def __init__(self, str_map):
        self.str_map = str_map
        self.start_nodes = []
        self.goal_nodes = []
        self.obstacle = []
        self.fuel = []
        self.portal = []
        self.max_y = -1
        self.max_x = -1


    def starting_nodes(self):
        # raise NotImplementedError
        if not self.start_nodes:
            self.build_map()
        return self.start_nodes


    def is_goal(self, node):
        if not self.goal_nodes:
            self.build_map()
        node_ij = (node[0], node[1])
        return node_ij in self.goal_nodes

    def build_map(self):
        self.max_y = len(self.str_map.splitlines()) - 1
        self.max_x = len(self.str_map.splitlines()[0]) - 1
        for i in range(len(self.str_map.splitlines())):
            for j in range(len(self.str_map.splitlines()[0])):
                current_node = self.str_map.splitlines()[i][j]
                if current_node == 'G':
                    self.goal_nodes.append((i, j))
                elif current_node == 'S':
                    self.start_nodes.append((i, j, float('inf')))
                elif current_node.isnumeric():
                    self.start_nodes.append((i, j, int(current_node)))
                elif current_node == 'X':
                    self.obstacle.append((i, j))
                elif current_node == 'F':
                    self.fuel.append((i, j))
                elif current_node == 'P':
                    self.portal.append((i, j))



    def outgoing_arcs(self, tail_node):
        arcs = []
        direction_order = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'Fuel up']
        if tail_node[2] > 0:
            current_coord = (tail_node[0], tail_node[1])
            for i in range(-1, 2):
                for j in range(-1, 2):
                    fuel_up = False
                    new_y = current_coord[0] + i
                    new_x = current_coord[1] + j
                    if (0 < new_y < self.max_y) and (0 < new_x < self.max_x):
                        if (new_y, new_x) not in self.obstacle:
                            if tail_node[2] != float('inf'):
                                if (new_y, new_x) not in self.fuel:
                                    head_node = (new_y, new_x, tail_node[2] - 1)
                                else:
                                    head_node = (new_y, new_x, 9)
                                    if tail_node != head_node:
                                        fuel_up = True
                                        arcs.append(Arc(tail_node, head_node, 'Fuel up', 15))
                            else:
                                head_node = (new_y, new_x, float('inf'))

                            if not fuel_up:

                                if i == -1 and j == -1:
                                    arcs.append(Arc(tail_node, head_node,'NW', 7))

                                elif i == -1 and j == 0:
                                    arcs.append(Arc(tail_node, head_node, 'N', 5))

                                elif i == -1 and j == 1:
                                    arcs.append(Arc(tail_node, head_node, 'NE', 7))

                                elif i == 0 and j == -1:
                                    arcs.append(Arc(tail_node, head_node, 'W', 5))

                                elif i == 0 and j == 0:
                                    continue

                                elif i == 0 and j == 1:
                                    arcs.append(Arc(tail_node, head_node, 'E', 5))

                                elif i == 1 and j == -1:
                                    arcs.append(Arc(tail_node, head_node, 'SW', 7))

                                elif i == 1 and j == 0:
                                    arcs.append(Arc(tail_node, head_node, 'S', 5))

                                elif i == 1 and j == 1:
                                    arcs.append(Arc(tail_node, head_node, 'SE', 7))

        return sorted(arcs, key=lambda arc: direction_order.index(arc.action))


