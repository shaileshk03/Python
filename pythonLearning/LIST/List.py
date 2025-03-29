# String in build functions in python 3
str = "string"
txt = "Hello, And Welcome To My World!"
# Capitalize return string with first letter in Cap
cap = str.capitalize()

#Casefold return string with all string letter in small letter
case = str.casefold()

# Center will move the all string to give space like arg 20 from it's current place
txtCen = "banana"
x = txt.center(20)

#Count will count the occurrence of a given char
txtCount = "Apples"
chat_count = txtCount.count("p")

#print(chat_count)
#print(str)
#print(txtCen)
#print(cap)
#print(case)



# List revers
list = [1,2,3,4,5]

# 1st way to revers a List
#LIST.reverse()
#print(LIST)

my_list = [1, 2, 3, 4, 5]
for item in reversed(my_list):
    print(item)

# Loop way to revers a LIST slice method [::1]
for i in list:
    x = list[::-1]
    #print(x)

N = 6
end = ""
print("Reversed number are :", end)
while(N >= 0):
    print(N, end)
    N -= 1
