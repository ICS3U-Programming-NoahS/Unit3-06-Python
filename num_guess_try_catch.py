#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Oct. 24th, 2023
# This program asks the user to guess a number between 0 and 9
# and tells the user if they got it correct, using random numbers,
# with try, except, finally.
import random


def main():
    # Get the user's guess
    user_guess_as_string = input("Guess a number between 0 and 9: ")

    # Generate random number between 0 and 9
    random_number = random.randint(0, 9)

    # Making sure the user's guess is an integer
    try:
        user_guess_as_int = int(user_guess_as_string)

        # Check if the user's guess is correct
        if random_number == user_guess_as_int:
            print("You have guessed the correct number!")
        else:
            print("You are incorrect. The number was {}.".format(random_number))
    except:
        print("{} is not an integer.".format(user_guess_as_string))
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
