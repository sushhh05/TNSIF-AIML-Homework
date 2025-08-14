# 1. Write a program to find the difference between the maximum and minimum elements in a list.
l = [2, 4, 6, 8, 10]

diff = max(l) - min(l)
print(diff)


# 2. Write a program to remove all elements at odd indices from a list.
l1 = [1, 2, 3, 5, 4]

result = [l1[i] for i in range(len(l1)) if i % 2 == 0]

print(result)


# 3. Write a program that takes a list of integers and prints only the elements that appear exactly once.
l2 = [1, 2, 2, 3, 4, 3]

print(list(set(l2)))