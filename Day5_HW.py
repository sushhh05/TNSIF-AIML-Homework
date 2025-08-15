# 1. Write a program to take 5 numbers from the user and store them in a tuple, then print the maximum and minimum.

l =[]
n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))
n3 = int(input("Enter the third number : "))
n4 = int(input("Enter the fourth number : "))
n5 = int(input("Enter the fifth number : "))

l.append(n1)
l.append(n2)
l.append(n3)
l.append(n4)
l.append(n5)

print(tuple(l))
print(f"The maximum number from the above tuple is {max(l)}")
print(f"The minimum number from the above tuple is {min(l)}")


# 2. Given a tuple of integers, write a program to count how many elements are divisible by

t = (1, 2, 3, 4, 5, 6, 9)

count = 0
for i in t:
    if i % 3 == 0:
        count += 1
print(count)

# 3. Write a program to reverse the contents of a tuple without using reversed()

tup = (1, 2, 3, 4, 5)

print(tup[::-1])