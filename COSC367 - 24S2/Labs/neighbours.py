"""
Nathan Scott
COSC367 Lab 7
Neighbours
"""


def n_queens_neighbours(state):
    """Return a sorted list of states that are neighbours
    of the assignment"""
    n = len(state)
    neighbour_list = []
    for i in range(n):
        for j in range(n):
            neighbour_state = list(state)
            neighbour_state[i], neighbour_state[j] = neighbour_state[j], neighbour_state[i]
            neighbour_state = tuple(neighbour_state)
            if neighbour_state not in neighbour_list and neighbour_state != state:
                neighbour_list.append(tuple(neighbour_state))
    return sorted(neighbour_list)


def n_queens_cost(state):
    """Return number of conflicts in this state"""
    n = len(state)
    n_conflict = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                if abs(i - j) == abs(state[i] - state[j]):
                    n_conflict += 1
    return n_conflict // 2
