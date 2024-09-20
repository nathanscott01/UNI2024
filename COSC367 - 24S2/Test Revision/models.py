"""
Nathan Scott
Test Revision
Models
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
    """Return all models in knowledge base"""
    atom_set = set()
    for eq in knowledge_base:
        atom_set.update(atoms(eq))
    atom_permutations = interpretations(atom_set)
    model_list = []
    for interpretation in atom_permutations:
        if all(value(equation, interpretation) for equation in knowledge_base):
            model_list.append(interpretation)
    return model_list


# knowledge_base = {
#     lambda a, b: a and not b,
#     lambda c: c
# }
#
# model_list = models(knowledge_base)
# for model in model_list:
#     print(model)

knowledge_base = {
    lambda a, b: a if b
}
