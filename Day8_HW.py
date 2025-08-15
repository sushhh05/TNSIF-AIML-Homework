# 1. Write a program that converts a list of tuples into a dictionary

l = [('a', 2), ('b', 4), ('c', 6)]

print(dict(l))


# 2. Given a dictionary with values as lists, write a program to flatten all values into a single list.

d = {
    'a': [1, 2, 3],
    'b': [4, 5],
    'c': [6, 7, 8]
}

flattened_list = [item for sublist in d.values() for item in sublist]
print(flattened_list)


# 3. Write a program that takes a list with duplicate elements and returns a dictionary with elements as keys and their frequency as values

from collections import Counter

l1 = [1, 2, 2, 3, 4, 4, 4, 5]

print(dict(Counter(l1)))