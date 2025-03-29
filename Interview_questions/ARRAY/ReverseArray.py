

arr = [2,4,7,5]
# Using the reverse() method
arr.reverse()
#print(arr)

ArrayList = ["Red", "Green", "Orange", "White", "Blue"]
#print(ArrayList)

#Using the slicing technique
res = ArrayList[::-1]
print(res)

#Using the reverse functions
arr = [2,4,7,5]
reversed_array = list(reversed(arr))
print(reversed_array)


#Coding interview recommended reverse array
array = [1, 2, 3, 4, 5]
rev_array = []
for i in range(len(array) -1, -1, -1):
    rev_array.append(array[i])
print(rev_array)
