"""
Nathan Scott
COSC262 Lab 7
Greedy Algorithms
"""


def change_greedy(amount, coinage):
    """Take the coinage values and return a list of tuples
    showing how many of each coin is needed to make up the amount
    using a greedy algorithm"""
    ordered_coinage = sorted(coinage)[::-1]
    counts = [0 for i in range(len(ordered_coinage))]
    value = amount
    i = 0
    while value > 0:
        if i == len(ordered_coinage) or ordered_coinage[-1] > value:
            return None
        while ordered_coinage[i] <= value:
            counts[i] += 1
            value -= ordered_coinage[i]
        i += 1
    coin_count = []
    for i in range(len(ordered_coinage)):
        if counts[i] != 0:
            coin_count.append(tuple((counts[i], ordered_coinage[i])))
    return coin_count


def buskers_schedule(show_list):
    """Take a list of tuples of show times and return a list of the shows
    one is able to attend, such that one is able to attend as many shows as
    possible"""
    show_list2 = []
    for show in show_list:
        show_list2.append(tuple((show[0], show[1], show[1] + show[2])))
    show_list2 = sorted(show_list2, key=lambda x: x[2])
    finish_time = 0
    attending = []
    for show in show_list2:
        if show[1] >= finish_time:
            attending.append(show)
            finish_time = show[2]
    # return sorted(attending, key=lambda x: x[1])
    return attending


def fractional_knapsack(capacity, items):
    """Solve knapsack problem"""
    if not items:
        return 0.0
    items = sorted(items, key=lambda x: x[1]/x[2])[::-1]
    value = 0
    current_weight = 0
    i = 0
    while current_weight < capacity and i < len(items):
        item_added = False
        if items[i][2] <= capacity - current_weight:
            value += items[i][1]
            current_weight += items[i][2]
            item_added = True
            print(items[i])
        if not item_added:
            value += items[i][1] / items[i][2] * (capacity - current_weight)
            current_weight += items[i][2] * (capacity - current_weight)
        i += 1
    return value


item_set = [
    ("A", 140, 2),
    ("B", 150, 3),
    ("C", 160, 4),
    ("D", 180, 3)]

print(fractional_knapsack(7, item_set))

for item in item_set:
    print(item[1] / item[2])