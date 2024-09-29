"""
Nathan Scott
COSC367 Lab 8
Queries
"""

from itertools import product


def joint_prob(network, assignment):
    """Find the joint probability of the assignment within the network"""
    p = 1
    for var, data in network.items():
        parents = tuple(assignment[parent] for parent in data["Parents"])
        p_true = data["CPT"].get(parents, data["CPT"][parents])
        p *= p_true if assignment[var] else (1 - p_true)
    return p


def query(network, query_var, evidence):
    """Return the distribution of query_var"""
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    distribution = [0, 0]
    assignment = dict(evidence)
    for query_val in {True, False}:
        assignment.update({query_var: query_val})
        for values in product((True, False), repeat=len(hidden_vars)):
            hidden_assignments = {var: val for var, val in zip(hidden_vars, values)}
            assignment.update(hidden_assignments)
            p = joint_prob(network, assignment)
            if query_val is True:
                distribution[0] += p
            else:
                distribution[1] += p
    query_probability = {True: distribution[0] / sum(distribution), False: distribution[1] / sum(distribution)}
    return query_probability


network = {
    'Virus': {
        'Parents': [],
        'CPT': {
            (): 0.01
        }
    },

    'A': {
        'Parents': ['Virus'],
        'CPT': {
            (True,): 0.95,
            (False,): 0.1,
        }
    },

    'B': {
        'Parents': ['Virus'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
        }
    }
}

answer = query(network, 'Virus', {'B': True})
print("The probability of carrying the virus\n"
      "if test B is positive: {:.5f}"
      .format(answer[True]))
