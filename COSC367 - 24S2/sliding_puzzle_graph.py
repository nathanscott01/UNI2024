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

        # Find i and j such that state[i][j] == BLANK
        i, j = next((i, j) for i, row in enumerate(state) for j, value in enumerate(row) if value == BLANK)

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
        number_list = [item for sublist in state for item in sublist if item != BLANK]
        numbers_ordered = all(number_list[i-1] <= number_list[i] for i in range(1, len(number_list)))
        return numbers_ordered and state[0][0] == BLANK


class BFSFrontier(Frontier):
    """Implements a frontier container appropriate for breadth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = deque([])

    def add(self, path):
        self.container.appendleft(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if len(self.container) > 0:
            next_element = self.container.pop()
            return next_element
        else:
            raise StopIteration  # don't change this one
