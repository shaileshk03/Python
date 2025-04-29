# Bubble Sort algorithm, sorts an array by repeatedly comparing adjacent elements and swapping them if they are in the wrong order.

def bubblesort(arr):
    # len function will return the length of the array
    n = len(arr)

    # for loop to iterate over all the elements in array
    for i in range(n):
        # for each interation last element always going to be sorted
        for j in range(n - i - 1):
            # compare the element at position of J with its next element (to it's right) in an array.
            if arr[j] > arr[j+1]:
                # SWAP
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# Unsorted array
arr = [3,1,2,4,5,2,34]
# call the Bubble sort function
bubblesort(arr)
# print the array
print(arr)
