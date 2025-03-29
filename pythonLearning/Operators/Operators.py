### MUST READ THE COMMENTED OUT LINE FOR BETTER UNDERSTANDING AND EXPLAIN ###

###########  Arithmetic Operators #############
# Addition(+): a + b
# Subtraction(-): a - b
# Multiplication(*): a * b
# Division(/): a / b
# Modulus(%): a % b
# Floor division(//): a // b
# Exponentiation(**): a ** b
from graphlib import TopologicalSorter

# print("Addition:", 3 + 2)
# print("Subtraction:",  5 - 3)
# print("Multiplication:", 6 * 3)
# print("Division:", 4 / 16)
# print("Modulus:", 3 % 2)
# print("Floor division:", 7 // 2)
# print("Exponentiation:", 3 ** 2)

# Calculating area of a circle
radius = 10
area_of_circle = 3.14 * radius ** 2
#print("area of circle :", radius)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
#print("Area of rectangle :" ,area_of_rectangle)

#print(3 > 2)

x = abs(-7)
#print(x)

#print(pow(2, 8))

a = 5
a += 3
print(a) #output will be 8 make sure you aware about it.

#### OPERATORS USES EXPLAIN ####

#How to check if "apple" is present in the fruits object.
#Use in operator to check
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

# Check or operator uses
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")

# Integer Division (//)
# You can use the double forward slash (//) to perform integer division.
# This will divide the numbers and return the whole number part of the result, discarding the remainder.
#In this example, 10 divided by 3 equals 3.333.... The integer division returns only the whole number part, which is 3.

result = 10 // 3
print(result)  # prints 3


