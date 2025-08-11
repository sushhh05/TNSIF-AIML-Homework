# 1. Write a program to print the factorial of a number using a for loop.

n = int(input("Enter a number: "))
def factorial(n):
    if (n == 0 or n == 1):
        return 1
    return n * factorial(n-1)

print(f"The factorial of {n} is {factorial(n)}")


# 2. Write a program that prints all numbers from 1 to 100 that are divisible by 7 but not a multiple of 5.

for i in range (1, 101):
    if i % 7 == 0 and i % 5 != 0:
        print(i)

# 3. Write a program that takes a number and prints whether it is a palindrome or not.

n = (input("Enter a number: "))

if n == n[::-1] :
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
