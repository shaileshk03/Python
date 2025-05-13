
# def greater_than_30(number):
#     count = 0
#     for n in number:
#         if n > 30:
#             count +=1
#         return count
#


# Print 1 to 6 numbers using a control statement
i = 0
while i < 6:
  i += 1 # Increment we can write (i = i+) as well, Increment will move to the next element.
  # if i == 3:
  #  continue -- It will continue to next
  #  break -- break as soon as condition is met
  print(i)


# Print a message once the condition is false.
  j = 1
  while j < 6:
      print(j)
      j += 1 # increment
  else:
      print("J is no longer less than 6")


 # If, elif...else uses
  a = 30
  b = 33
  # First code will check if block code if condition gets satisfied will print "A is greater than B"
  if a > b:
      print("A is greater than B :")
  # In case if the condition above not satisfied in above block then it will move to elif block and check condition here.
  elif a == b:
      print("A and B are equals :")
  # If all the above conditions are not satisfied, it will simply print the else statement.
  else:
      print("B is greater than A :")


# Short Hand If ... Else
  c = 2
  d = 330
  print("C") if c > d else print("D")


# AND-and OR, NOT conditional statement
a = 200
b = 33
c = 500
# if a > b and c > a:
# if a > b or a > c:
# if not a > b:
if b < a < c:
  print("Both conditions are True")


# Nested If statement
x = 41

if x > 10:
  print("Number is above ten,")
  if x > 20:
    print("Number is also above 20!")
  else:
    print("but not above 20.")


# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content,
# put in the pass statement to avoid getting an error.

  a = 33
  b = 200

  if b > a:
      pass