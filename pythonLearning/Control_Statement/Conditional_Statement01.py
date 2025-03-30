# 1. Divisible by 7 and Multiples of 5
num1 = 1500
num2 = 2701

for i in range(num1, num2):
    if  (i % 5 == 0) and (i % 7 == 0):
        i +=1
        # Print answer horizontally
        #print(i, " ", end='', flush=True)

#2. Temperature
    temp = input("Enter temperature you would like to convert like 60F or 140C?:: ")
    # Extract the numerical part of the temperature and convert it to an integer
    degree = int(temp[:-1])
    # Extract the convention part of the temperature input (either 'C' or 'F')
    i_conversion = temp[-1]
    # Check if the input convention is in uppercase 'C' (Celsius)
    if i_conversion.upper() == "C":
        # Check if the input convention is in uppercase 'C' (Celsius)
        result = int(round((9 * degree) / 5 + 32))
        # Set the output convention as Fahrenheit
        o_conversion = "Fahrenheit"
    elif i_conversion.upper() == "F":
        # Convert the Fahrenheit temperature to Celsius
        result = int(round((degree - 32) * 5 / 9))
        # Set the output convention as Celsius
        o_conversion = "Celsius"
    else:
        print("Error Input is not form of conversion")
        quit()

    print("The temperature is ", o_conversion, "is", result)


# Write a Python program to convert a list of temperatures in Celsius to Fahrenheit and vice versa, outputting both results side-by-side.
user_input = input("Enter Celsius value as 45C separated by space:: ").split()

for x in user_input:
    degree = int(x[:-1])
    i_conversion = x[-1]

    if i_conversion.upper() == "C":
       result = int(round((9 * degree) / 5 + 32))
       o_conversion = "Fahrenheit"
    elif i_conversion.upper() == "F":
       result = int(round((degree - 32) * 5 / 9))
       o_conversion = "Celsius"
    else:
        print("Error ! not a valid list input")
        quit()
    print("The temperature is ", o_conversion, "is", result)


