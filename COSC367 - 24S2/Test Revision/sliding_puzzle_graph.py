"""
Nathan Scott
Test Revision
Sliding Puzzle
"""

from search import *
from collections import deque
import copy

BLANK = ' '


class SlidingPuzzleGraph(Graph):
    """Objects of this type represent (n squared minus one)-puzzles.
    """

    def __init__(self, starting_state):
        self.starting_state = starting_state

    def outgoing_arcs(self, state):
        """Given a puzzle state (node) returns a list of arcs. Each arc
        represents a possible action (move) and the resulting state."""

        n = len(state)  # the size of the puzzle

        def find_blank():
            """Find the blank state"""
            for row in range(n):
                for col in range(n):
                    if state[row][col] == BLANK:
                        return row, col

        # Find i and j such that state[i][j] == BLANK
        i, j = find_blank()  # COMPLETE (or rewire as multiple statements)

        arcs = []
        if i > 0:
            action = "Move {} down".format(state[i - 1][j])  # or blank goes up
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if i < n - 1:
            action = "Move {} up".format(state[i + 1][j])  # or blank goes down
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j > 0:
            action = "Move {} right".format(state[i][j - 1])  # or blank goes left
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j < n - 1:
            action = "Move {} left".format(state[i][j + 1])
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        return arcs

    def starting_nodes(self):
        return [self.starting_state]

    def is_goal(self, state):
        """Returns true if the given state is the goal state, False
        otherwise. There is only one goal state in this problem."""

        n = len(state)

        # Check if the first element is BLANK
        if state[0][0] != BLANK:
            return False
        number_list = []
        for row in range(n):
            for col in range(n):
                if not (row == 0 and col == 0):
                    number_list.append(int(state[row][col]))
        for i in range(1, n * n - 1):
            if number_list[i] < number_list[i - 1]:
                return False
        return True


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
