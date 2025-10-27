from itertools import chain
nested = [[1, 2, 3], [4, 5], [6]]
# flat = []

# for sublist in nested:
#     for item in sublist:
#         flat.append(item)

# print(flat)


# flat = [item for sublist in nested for item in sublist]
# print(flat)

flat = list(chain.from_iterable(nested))
print(flat)


def flatten(lst):
    flat = []
    for i in lst:
        if isinstance(i, list):
            flat.extend(flatten(i))
        else:
            flat.append(i)
    return flat

nested = [[1, 2, [3, 4]], [5], 6]
print(flatten(nested))  # [1, 2, 3, 4, 5, 6]





# 1-level flatten
flat = [x for sub in nested for x in sub]

# Multi-level flatten
def flatten(lst):
    return [i for sub in lst for i in (flatten(sub) if isinstance(sub, list) else [sub])]





