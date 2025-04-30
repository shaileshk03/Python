# Insertion Sort technique is used to list into two sections - sorted and unsorted.
# Iterate through the unsorted section and insert every list item into their correct position in the sorted list.
# This algorithm can also be implemented by using the ‘while’

def InsertionSort(array):
    n = len(array)

    for i in range(1, n):
        insert_idx = i

        current_value = array[i]

        for j in range(i - 1, -1, -1):
            if array[j] > current_value:
                array[j + 1] = array[j]
                insert_idx = j
            else:
                break
        array[insert_idx] = current_value

# array to be sorted
array = [10, 5, 13, 8, 2]
print("Array before sorting:")
print(array)
InsertionSort(array)
print("Array after sorting:")
print(array)
