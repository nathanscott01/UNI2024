"""
Nathan Scott
COSC367 Lab 7
Greedy Descent
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


def greedy_descent(initial_state, neighbours, cost):
    """Iteratively improve the state until local minima is reached.
    Return a list of states encountered"""
    current_cost = cost(initial_state)
    states = [initial_state]
    cost_improved = True
    min_cost = float('INF')
    while cost_improved:
        neighbour_states = neighbours(initial_state)
        n_states = len(neighbour_states)
        cost_list = [_ for _ in range(n_states)]
        for i in range(n_states):
            cost_list[i] = cost(neighbour_states[i])
            min_cost = min(cost_list)
        if min_cost < current_cost:
            current_cost = min_cost
            i = cost_list.index(min_cost)
            initial_state = neighbour_states[i]
            states.append(initial_state)
        else:
            cost_improved = False
    return states, current_cost


def greedy_descent_with_random_restart(random_state, neighbours, cost):
    """Find a minimum solution"""
    """
    - random_state() generates a random state in the form (2, 3, 1)
    - neighbours(state) references n_queens_neighbours(state), generates
    neighbour states as tuples like [(1, 2, 3), (2, 3, 1), (3, 1, 2)]
    - cost(state) references n_queens_cost(state) and returns number of conflicts
    
    1. Random state generated
    2. Use greedy_descent(state, neighbours, cost) to find states checked, and minima
    3. If minima is not 0, or not global minima, generate another random state
    """
    global_found = False
    while not global_found:
        state = random_state()
        state_list, g_min = greedy_descent(state, neighbours, cost)
        for n_state in state_list:
            print(n_state)
        if g_min != 0:
            print("RESTART")
        else:
            global_found = True
