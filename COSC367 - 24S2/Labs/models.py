"""
Nathan Scott
COSC367 Lab 3
Models
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


def atoms(formula):
    """Takes a formula in the form of a lambda expression and returns a set of
    atoms used in the formula. The atoms are parameter names represented as
    strings.
    """
    return {atom for atom in formula.__code__.co_varnames}


def value(formula, interpretation):
    """Takes a formula in the form of a lambda expression and an interpretation
    in the form of a dictionary, and evaluates the formula with the given
    interpretation and returns the result. The interpretation may contain
    more atoms than needed for the single formula.
    """
    arguments = {atom: interpretation[atom] for atom in atoms(formula)}
    return formula(**arguments)


def models(knowledge_base):
    """Return a list of interpretations that are models of the KB"""
    atom_set = set()
    for equation in knowledge_base:
        atom_set.update(atoms(equation))
    atom_interpretations = interpretations(atom_set)
    for element in atom_interpretations:
        print(element)
    print("\n")
    model_set = []
    for interpretation in atom_interpretations:
        if all(value(equation, interpretation) for equation in knowledge_base):
            model_set.append(interpretation)
    return model_set


knowledge_base = {
    lambda p, q: not q or p,
    lambda a, b: not b or a,
    lambda b: b
}

for element in models(knowledge_base):
    print(element)

