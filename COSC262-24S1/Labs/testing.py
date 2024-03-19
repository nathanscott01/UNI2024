"""Test out different ways of making tuples"""
from pprint import pprint
from adjacency import *

def just_tuple(graph_str):
    lines = [line.strip() for line in graph_str.splitlines()]
    edges = [tuple((line[0], line[1])) for line in lines[1:]]
    return edges

def mapped_tuples(graph_str):
    lines = [line.strip().split() for line in graph_str.splitlines()]
    edges = [tuple(map(int, line)) for line in lines[1:]]
    return lines[0]

def split_tuples(graph_str):
    lines = [line.strip() for line in graph_str.splitlines()]
    edges = [tuple(line.split()) for line in lines[1:]]
    return edges

def map_split_tuples(graph_str):
    lines = [line.strip() for line in graph_str.splitlines()]
    edges = [tuple(map(int, line.split())) for line in lines[1:]]
    return edges

def stripped_lines(graph_str):
    lines = [line.strip() for line in graph_str.splitlines()]
    line_stripped = lines[1]
    line_split = lines[1].split()
    return line_stripped, line_split, lines[0]


graph_string1 = """\
D 3
0 1
1 0
0 2
"""

graph_string2 = """\
D 3
"""

graph_string3 = """\
D 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

# pprint(adjacency_list(graph_string3))

# print(just_tuple(graph_string1))
# print(mapped_tuples(graph_string1))
# print(split_tuples(graph_string1))
# lines = mapped_tuples(graph_string1)
# print(lines[1])
# stripped, split, first = stripped_lines(graph_string1)
# print(len(first))
# print(stripped)
# print(split)
# print(tuple(map(int, split)))

