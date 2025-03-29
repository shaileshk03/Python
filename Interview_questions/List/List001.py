from sys import flags

#find Second largest in LIST

a = [10, 20, 4, 45, 99]

# Initialize largest (max1)
# and second largest (max2) to negative infinity
max_ = float('-inf')
second_largest = float('-inf')
# Loop through each number in LIST
for n in a:

    if n > max_:
        # update the second largest to previous largest
        second_largest = max_
        # update the largest to current max
        max_ = n
        #if current number is less than largest but greater than second largest
    elif n > second_largest and n != max_:
       #
      second_largest = n

print(second_largest)
print(max_)