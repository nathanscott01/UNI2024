"""
Nathan Scott
Test Revision
Forward Deduce
"""

import re

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 2 Aug 2021

    """
    ATOM   = r"[a-z][a-zA-Z\d_]*"
    HEAD   = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY   = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB     = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")


def forward_deduce(kb):
    """Find all atoms that can derived from knowledge base"""
    kb_list = list(clauses(kb))
    atom_set = set()
    new_atom_set = set()
    kb_rules = list()

    # Find atomic facts
    for head, body in kb_list:
        if not body:
            atom_set.update(head)
        else:
            kb_rules.append([head, body])

    # Iterate through rules
    atom_set_updated = True
    new_atom_set.update(atom_set)
    while atom_set_updated:
        for head, body in kb_rules:
            if head not in new_atom_set and all(body_atom in new_atom_set for body_atom in body):
                new_atom_set.update(head)
        if new_atom_set == atom_set:
            atom_set_updated = False
        else:
            atom_set.update(new_atom_set)
    return new_atom_set


kb1 = """
a :- b.
b.
"""

kb2 = """
good_programmer :- correct_code.
correct_code :- good_programmer.
"""

kb3 = """
a :- b, c.
b :- d, e.
b :- g, e.
c :- e.
d.
e.
f :- a,
     g.
"""

print(", ".join(sorted(forward_deduce(kb1))))
print(", ".join(sorted(forward_deduce(kb2))))
print(", ".join(sorted(forward_deduce(kb3))))
