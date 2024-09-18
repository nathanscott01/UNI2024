"""
Nathan Scott
Test Revision
DFS Frontier
"""

from search import *


class DFSFrontier(Frontier):
    """Search Frontier for DFS"""
    def __init__(self):
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.container) > 0:
            next_path = self.container.pop()
            return next_path
        else:
            raise StopIteration

