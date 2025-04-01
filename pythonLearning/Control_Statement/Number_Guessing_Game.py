import random

# Generate 1 to 10 random number
target_num = random.randint(1,10)
# Guess number we assume as zero as this point.
guess_num = 0

# While loop will run until the condition is not satisfied (operator (!=)  means - (not equals to))
while target_num != guess_num:
    # input method will pop up to ask user to input a guess number, it will take only integer number (int)
    guess_num = int(input('Guess a number between 1 and 10 until you get it right :'))

# Print a message indicating successful guessing once the correct number is guessed
print('Well guessed!')