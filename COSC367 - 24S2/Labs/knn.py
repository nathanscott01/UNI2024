"""
Nathan Scott
COSC367 Lab 10
KNN
"""

from math import sqrt
from collections import Counter


def euclidean_distance(v1, v2):
    """Find the distance between the two objects"""
    n = len(v1)
    squared_sum = 0
    for i in range(n):
        squared_sum += (v1[i] - v2[i]) ** 2
    return sqrt(squared_sum)


def majority_element(labels):
    """Return the label with the highest frequency"""
    counter = Counter(labels)
    return counter.most_common()[0][0]


def knn_predict(input, examples, distance, combine, k):
    """Predict the output"""
    distances = [(distance(input, e[0]), e[1]) for e in examples]
    distances.sort(key=lambda x: x[0])
    k_neighbours = distances[:k]
    k_d = k_neighbours[-1][0]

    for i in range(k, len(distances)):
        if distances[i][0] == k_d:
            k_neighbours.append(distances[i])

    n_outputs = [output for _, output in k_neighbours]
    return combine(n_outputs)


# print(euclidean_distance([0, 3, 1, -3, 4.5],[-2.1, 1, 8, 1, 1]))
# print(majority_element([0, 0, 0, 0, 0, 1, 1, 1]))
# print(majority_element("ababccc") in "ab")


examples = [
    ([2], '-'),
    ([3], '-'),
    ([5], '+'),
    ([8], '+'),
    ([9], '+'),
]

distance = euclidean_distance
combine = majority_element

for k in range(1, 6, 2):
    print("k =", k)
    print("x", "prediction")
    for x in range(0,10):
        print(x, knn_predict([x], examples, distance, combine, k))
    print()
