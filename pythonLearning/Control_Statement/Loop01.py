# When we want to perform a repetitive task a number of times, we use a loop to perform such a task in coding.
# Let's learn how to create loops and how to use them in coding.

# Input() method takes input as a String.
# If you want the input method to take input as float, int etc. we need to add int(input()), float(input()) instead of input().

user_input = input("Enter value you would like to add in list :")

# For loop will iterate over all the element input given by user
for x in user_input:
    # Print all the String input one by one
    # print(x)
    # Extract numbers from string one by one
    element = int(x[:-1])
    print("List : ", element)


# Range for loop for each String
#for i in range(len(user_input)):
