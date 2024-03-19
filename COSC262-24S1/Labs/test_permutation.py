"""Test ways of creating a permutation"""


input_data = {1, 2, 3}
candidate = ()

data = list(input_data)

tuples_needed = len(data) - len(candidate)
new_tuple_length = len(candidate) + 1

perm_list = [[] for _ in range(tuples_needed)]

i = 0
for perm in perm_list:
    while (i < len(data)) and (len(perm) < new_tuple_length):
        if data[i] not in perm:
            perm.append(data[i])
    i += 1

print(tuple(tuple(perm) for perm in perm_list))
