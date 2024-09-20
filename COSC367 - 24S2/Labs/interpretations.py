"""
Nathan Scott
COSC367 Lab 3
Interpretations
"""

import itertools


def interpretations(atoms):
    """Take the non-empty set of atoms and return all interpretations
    The parameters are as follows:
        - Each interpretation is a dictionary
        - The keys are atoms, and the values are True or False
        - Atoms are in alphabetical order"""
    atom_list = list(atoms)
    atom_list.sort()
    n = len(atom_list)
    atom_permutations = list(itertools.product([False, True], repeat=n))
    atom_interpretations = [dict(zip(atom_list, permutation)) for permutation in atom_permutations]
    return atom_interpretations


