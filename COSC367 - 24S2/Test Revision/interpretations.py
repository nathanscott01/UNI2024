"""
Nathan Scott
Test Revision
Interpretations
"""

from itertools import product


def interpretations(atoms):
    """Return all possible interpretations for atoms"""
    atom_list = list(atoms)
    atom_list.sort()
    n = len(atom_list)
    permutations = product([False, True], repeat=n)
    atom_permutations = [dict(zip(atom_list, permutation)) for permutation in permutations]
    return atom_permutations
