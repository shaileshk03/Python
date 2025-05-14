# Insertion Sort technique is used to split lists into two sections - sorted and unsorted.
# Iterate through the unsorted section and insert every list item into their correct position in the sorted list.
# This algorithm can also be implemented by using the ‘while’ loop

def InsertionSort(array):
    n = len(array) # get the length of the input list array

    # The outer loop starts from the second element (index 1) and goes through each element in the array.
    for i in range(1, n):

        # keeps track of where this value should be inserted.
        insert_idx = i

        # stores the element to be inserted into the sorted portion of the array
        current_value = array[i]

        # This inner loop goes backward through the sorted portion of the array (from index i-1 to 0)
        for j in range(i - 1, -1, -1):

            # If the current element in the sorted portion is greater than current_value,
            if array[j] > current_value:
                # it is shifted one position to the right.
                array[j + 1] = array[j]

                # insert_idx is updated to the current index j, indicating where current_value should be inserted
                insert_idx = j
            else:
                # If the current element is not greater, the loop breaks early (since the rest of the array is already sorted).
                break

        # current_value is inserted at the correct position.
        array[insert_idx] = current_value

# array to be sorted
array = [10, 5, 13, 8, 2]
print("Array before sorting:")
print(array)
InsertionSort(array)
print("Array after sorting:")
print(array)
