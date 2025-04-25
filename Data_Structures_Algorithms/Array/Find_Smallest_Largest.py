import numpy as np

# Using numpy library
my_array = np.array([1,2,4,2,6,8,3,4,3])
smallest_num = np.min(my_array)
largest_num = np.max(my_array)
print(smallest_num)
print(largest_num)


# Using condition
def find_smallest_num(nums):
    # Let's assume number is Max possible value
    smallest_num = float('inf')
    # Iterate over all the elements in numbers array
    for num in nums:
        if num < smallest_num:
            # update the Largest number value
            smallest_num = num
    return smallest_num