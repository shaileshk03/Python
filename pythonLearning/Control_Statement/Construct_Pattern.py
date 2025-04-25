# Approach:

# Nested loops used for printing the patterns. For the outer loop, we count the number of lines/rows and loop for them
# count the vertical stars line numbers as I have taken 5
#*
#* *
#* * *
#* * * *
#* * * * *
#* * * *
#* * *
#* *
#*

n = 5

# Outer loop
for i in range(5):
    # loop for printing star
    for j in range(i):
        print('* ', end="")
    # Move the line one line
    print('')

for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
        # Move the line one line
    print('')



n = 1

for i in range(5):
    #loop for print star
        print('* ')
