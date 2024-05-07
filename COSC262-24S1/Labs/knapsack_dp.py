""""
Nathan Scott
COSC262 Lab 8
Knapsack Problem DP
"""

import sys
import numpy as np

sys.setrecursionlimit(2000)


class Item:
    """An item to (maybe) put in a knapsack. Weight must be an int."""

    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        """The representation of an item"""
        return f"Item({self.value}, {self.weight})"


def max_value(item_list, max_capacity):
    """Find the maximum value of the collective items that the knapsack can hold"""
    n_items = len(item_list)
    weight_table = np.zeros((n_items + 1, max_capacity + 1), dtype=int)

    for i in range(1, n_items + 1):
        for j in range(1, max_capacity + 1):
            if item_list[i].weight <= j:
                weight_table[i, j] = max(weight_table[i - 1, j],
                                         weight_table[i - 1, j - item_list[i].weight] + item_list[i].value)

    return weight_table[-1, -1]


    # def knapsack_topdown(n, capacity):
    #     """Use top down algorithm to find max value"""
    #     if weight_table[n, capacity] != -1:
    #         return weight_table[n, capacity]
    #     elif n == 0 or capacity == 0:
    #         result = 0
    #     else:
    #         if item_list[n - 1].weight > capacity:
    #             result = knapsack_topdown(n-1, capacity)
    #         else:
    #             result = max(knapsack_topdown(n-1, capacity),
    #                          item_list[n-1].value +
    #                          knapsack_topdown(n-1, capacity-item_list[n-1].weight))
    #     weight_table[n, capacity] = result
    #     return result

    # return knapsack_topdown(n_items, max_capacity)
