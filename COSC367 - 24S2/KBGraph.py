"""
Nathan Scott
COSC367 Lab 3
KBGraph
"""
import copy
import re
from search import *


def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 2 Aug 2021

    """
    ATOM = r"[a-z][a-zA-Z\d_]*"
    HEAD = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")


class KBGraph(Graph):
    def __init__(self, kb, query):
        self.clauses = list(clauses(kb))
        self.query = list(query)

    def starting_nodes(self):
        return self.query

    def is_goal(self, node):
        return len(self.query) == 0

    def outgoing_arcs(self, tail_node):
        new_arcs = []
        new_atoms = []

        for head, body in self.clauses:
            if head == tail_node:
                if body:
                    for child in body:
                        new_atoms.append(child)
                        new_arcs.append(Arc(tail_node, child, str(tail_node) + "->" + str(child), None))
                else:
                    new_arcs.append(Arc(tail_node, [], str(tail_node) + "->" + str([]), None))

        self.query = new_atoms + self.query
        if tail_node in self.query:
            self.query.remove(tail_node)

        return new_arcs[::-1]


class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if len(self.container) > 0:
            next_element = self.container.pop()
            return next_element
        else:
            raise StopIteration



kb = """
a :- c, d.
c.
"""

query = {'a'}
if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
    print("The query is true.")
else:
    print("The query is not provable.")