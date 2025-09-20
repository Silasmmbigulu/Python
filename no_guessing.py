#Python number guessing game

import random

#declare two variables for the range of guesing numbers
lowest_number = 1
highest_number = 100

#a variable answer selected randomly from lowest and highest number
answer = random.randint(lowest_number, highest_number )

#keeping truck for the number of guesses
guesses = 0

is_running = True
#print a welcoming message
print("Python Number guessing game")
print(f"Select a number between {lowest_number} and {highest_number}")

#while loop to continue gaming each round
while is_running:
    #promt the user for gueses
    guess = input("Enter your guess: ")

    #ensuring the user enters valid guesses
    if guess.isdigit():
        #if the guess is a digit, type caste it ito int
        guess = int(guess)
        guesses += 1  #increament our guesses since we initialized it to 0

        #ensuring the guesses aren't out of range
        if guess < lowest_number or guess > highest_number:
            print("That number is out of range!!")
            print(f"Please select a number between {lowest_number} and {highest_number}")
            #ensure guesses are not < or > the answer
        elif guess < answer:
            print("Too low! Please try again")
        elif guess > answer:
            print("Too high! Please try again")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False #escape the while loop

    else:
        print("Invalid guess!")
        print(f"Please select a number between {lowest_number} and {highest_number}")
        print("          ")

        


