




# Input will take value as String
# If you want to take input as string float etc. we need to add int(input()), float(input()).

user_input = input("Enter value you would like to add in list :")

# This for loop will iterate over all the string input given by user
for x in user_input:
    # Print all String input one by one
    #print(x)
    # Extract numbers from string one by one
    element = int(x[:-1])
    print("List : ", element)


# Range for loop for each String
#for i in range(len(user_input)):
