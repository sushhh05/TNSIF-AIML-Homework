# 1. Write a program that takes the radius as input and calculates the area and circumference of a circle.

def circle():
    rad = int(input("Enter the radius of circle : "))
    area = 3.14 * (rad ** 2)
    circumference = 2 * 3.14 * rad
    print(f"Area of circle is : {round(area, 2)}")
    print(f"Circumference of circle is : {round(circumference, 2)}")

circle()


# 2. Write a program to check if a number is divisible by both 3 and 5.

n = int(input("Enter a number: "))

if n % 3 == 0 and n % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")


# 3. Write a program that takes a 4-digit number from the user and prints the sum of its digits.

n = int(input("Enter a 4-digit number: "))

sum = 0
for i in range (4):
    sum += n % 10
    n = n // 10

print(sum)
