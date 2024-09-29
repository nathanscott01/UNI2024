"""
Nathan Scott
COSC367 Lab 8
Joint Probability
"""


# def joint_prob(network, assignment):
#     p = 1  # p will eventually hold the value we are interested in
#     for var in network:
#         parents = network[var]["Parents"]
#         if not parents:
#             p_true = network[var]["CPT"][()]
#             if assignment[var]:
#                 p *= p_true
#             else:
#                 p *= (1 - p_true)
#         else:
#             parent_list = []
#             for parent in parents:
#                 parent_list.append(assignment[parent])
#             for cpt in network[var]["CPT"]:
#                 if parent_list == list(cpt):
#                     p_true = network[var]["CPT"][cpt]
#                     if assignment[var]:
#                         p *= p_true
#                     else:
#                         p *= (1 - p_true)
#     return p

def joint_prob(network, assignment):
    """Find the joint probability of the assignment within the network"""
    p = 1
    for var, data in network.items():
        parents = tuple(assignment[parent] for parent in data["Parents"])
        p_true = data["CPT"].get(parents, data["CPT"][parents])
        p *= p_true if assignment[var] else (1 - p_true)
    return p
