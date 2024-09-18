"""
Nathan Scott
Test Revision
BFS
"""

from search import *
from collections import deque


class BFSFrontier(Frontier):

    def __init__(self):
        self.container = deque()

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.container) > 0:
            next_path = self.container.popleft()
            return next_path
        else:
            raise StopIteration

