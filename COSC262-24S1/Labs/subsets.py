def all_subsets(s):
    """Return all subsets"""
    if len(s) == 0:
        return [set()]
    x = s.pop()
    subsets = all_subsets(s)
    subsets_copy = [subset.copy() for subset in subsets]
    for subset in subsets_copy:
        subset.add(x)
    return subsets + subsets_copy

counter = {1, 2, 3, 4, 5, 6}
# print(sorted(map(sorted, all_subsets(counter))))
set_1 = all_subsets(counter)
set_four = [x for x in set_1 if len(x) == 3]
print(set_four)