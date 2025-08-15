# 1. Write a program that takes a sentence and creates a dictionary with word counts

from collections import Counter

s = "Sushant how are you, what are you dong sushant ?"

l = s.lower().split()

print(Counter(l))

# 2. Write a program to map roll numbers to names using two lists and form a dictionary

l1 = ['sushhh', 'sushii', 'drishhh', 'yashhh']
l2 = [1, 2, 3, 4]

print(dict(zip(l1, l2)))

# 3. Write a program that takes a dictionary of students and their marks, and prints the name of the student with the highest marks

marks = {'John': 90, 'Emma': 85, 'Jack': 95 }

print(max(marks, key=marks.get))

