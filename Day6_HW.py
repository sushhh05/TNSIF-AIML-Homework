# 1. Write a program to take two lists from the user and print the common elements using sets.

l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]

print( set(l1).union(set(l2)))

# 2. Write a program to check if two sets are disjoint or not.

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print(s1.isdisjoint(s2))

# 3. Write a program to find all unique vowels present in a given string using set.

s = "Sushant how are you, what are you dong ?"

vowels = {"a", "e", "i", "o", "u"} 

print(set(s.lower()) & vowels)
    
