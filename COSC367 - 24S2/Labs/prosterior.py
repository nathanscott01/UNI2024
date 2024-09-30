"""
Nathan Scott
COSC367 Lab 9
Prosterior
"""


def posterior(prior, likelihood, observation):
    """Return the prosterior probability of the class variable being true"""
    n = len(likelihood)
    # prob_true = prior * prod([likelihood[i][1] for i in range(n)])
    # prob_false = (1 - prior) * prod([likelihood[i][0] for i in range(n)])
    # alpha = 1 / (prob_false + prob_true)
    prob_true = 1
    prob_false = 1
    for i in range(n):
        prob_true *= likelihood[i][1] if observation[i] else (1 - likelihood[i][1])
        prob_false *= likelihood[i][0] if observation[i] else (1 - likelihood[i][0])
    alpha = 1 / (prior * prob_true + (1 - prior) * prob_false)
    prosterior_prob = alpha * prob_true * prior
    return prosterior_prob
