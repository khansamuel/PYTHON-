#Exercise ,Number Guessing Game 
#Make a variable ,like winning_number and assign any number to it .
#Ask user to guess a number .
#If user guessed correctly then print "YOU WIN!!! "
#If user didnt gesed correctly then :
#If user guessed lower thn actual number then print "too low "
#If user guessed higher  thn actual number then print "too high "

#bonus
 ""how to generate random number in python to generate random winning number"
#winning number 


import random  # Import the random module for generating random numbers

# Generate a random winning number between 1 and 100
winning_number = random.randint(1, 100)

# Game loop
while True:
    try:
        # Ask the user to guess a number
        guess = int(input("Guess a number between 1 and 100: "))

        # Check if the guess is correct
        if guess == winning_number:
            print("YOU WIN!!!")
            break  # Exit the loop if the user wins

        elif guess < winning_number:
            print("Too low. Try again!")

        else:
            print("Too high. Try again!")

    except ValueError:
        print("Invalid input. Please enter a whole number.")