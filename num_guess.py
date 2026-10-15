#! /usr/bin/env python3
# created by : Serke Asfeday
# Date :  15, October, 2026
# This program is a guessing game that have a constant number and the user guess the number

import constants


def main():

    # here ask the user to guess a number between 1 and 9
    user_guess = int(input("Guess a number between 1 and 9: "))

    # if they guessed right the program tells them that they are correct
    if user_guess == constants.NUMBER:
        print("You guessed correctly!")
    
    # if it is not the correct answer it kills the program and prints "You guessed incorrectly!"
    else:
        print("You guessed incorrectly!")

    # close function to run the code
if __name__ == "__main__":
    main()
