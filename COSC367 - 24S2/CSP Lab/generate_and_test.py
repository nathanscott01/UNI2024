"""
Nathan Scott
COSC367 Lab 5
CSP Generate and Test
"""

from csp import *
import itertools

def generate_and_test(csp):
    names, domains = zip(*csp.var_domains.items())
    for values in itertools.product(*domains):
        assignment = {#COMPLETE for x, v in zip(names, values)}
        if all(satisfies(#COMPLETE):
            yield assignment